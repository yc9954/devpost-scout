#!/usr/bin/env python3
"""Speak the shot list, and time the film to the voice.

One script file drives three things — the on-screen captions, the narration and
the subtitles — so they cannot drift apart. This renders each line, measures how
long it actually takes to say, and writes those durations back for the camera to
hold on.

  python3 film/narrate.py                      # macOS voice
  DASHSCOPE_API_KEY=... python3 film/narrate.py --engine qwen
"""
import argparse, json, os, subprocess, sys, tempfile, wave
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / 'src' / 'film' / 'script.json'
OUT_DIR = ROOT / 'film' / 'audio'
TIMINGS = ROOT / 'public' / 'narration.json'
SRT = ROOT / 'film' / 'narration.srt'
TRACK = ROOT / 'film' / 'narration.wav'

SR = 48_000
LEAD_IN = 0.35          # the camera starts moving before the voice does
TAIL = 0.26             # a beat of air after each line. Twenty-nine of these add
                        # up: at 0.45 they were thirteen seconds of the film.


def say_macos(text: str, dest: Path, voice: str, rate: int):
    aiff = dest.with_suffix('.aiff')
    subprocess.run(['say', '-v', voice, '-r', str(rate), '-o', str(aiff), text], check=True)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', str(aiff), '-ar', str(SR), '-ac', '1', str(dest)], check=True)
    aiff.unlink(missing_ok=True)


MLX_MODEL = 'mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-8bit'
MLX_VOICE = (
    'A calm, articulate woman in her thirties narrating a software walkthrough. '
    'Measured pace, warm but precise, no salesmanship.'
)


def say_mlx(text: str, dest: Path, model, voice: str):
    """Qwen3-TTS through mlx-audio. Runs locally on Apple silicon; no API key."""
    from mlx_audio.tts.generate import generate_audio
    stem = dest.with_suffix('')
    # Clear anything an earlier engine left here, or its duration would be read
    # back instead of what this run produced.
    for stale in stem.parent.glob(f'{stem.name}*.wav'):
        stale.unlink(missing_ok=True)

    generate_audio(model=model, text=text, file_prefix=str(stem),
                   instruct=voice, audio_format='wav', verbose=False)

    produced = sorted(stem.parent.glob(f'{stem.name}*.wav'))
    if not produced:
        sys.exit(f'mlx-audio produced no file for: {text[:48]}')
    source = produced[0]
    if source != dest:
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', str(source),
                        '-ar', str(SR), '-ac', '1', str(dest)], check=True)
        source.unlink(missing_ok=True)


def say_qwen(text: str, dest: Path, voice: str):
    """Qwen3-TTS through DashScope. Needs DASHSCOPE_API_KEY."""
    try:
        import dashscope
        from dashscope.audio.qwen_tts import SpeechSynthesizer
    except ImportError:
        sys.exit('pip install dashscope, then rerun with --engine qwen')
    key = os.environ.get('DASHSCOPE_API_KEY')
    if not key:
        sys.exit('DASHSCOPE_API_KEY is not set')
    dashscope.api_key = key
    result = SpeechSynthesizer.call(model='qwen3-tts-flash', text=text, voice=voice)
    url = getattr(result, 'output', {}).get('audio', {}).get('url')
    if not url:
        sys.exit(f'qwen returned no audio: {result}')
    import urllib.request
    raw = dest.with_suffix('.src')
    urllib.request.urlretrieve(url, raw)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', str(raw), '-ar', str(SR), '-ac', '1', str(dest)], check=True)
    raw.unlink(missing_ok=True)


def duration(path: Path) -> float:
    with wave.open(str(path)) as w:
        return w.getnframes() / w.getframerate()


def timestamp(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--engine', choices=['say', 'mlx', 'qwen'], default='say')
    ap.add_argument('--voice', default='')
    ap.add_argument('--rate', type=int, default=178, help='words per minute, macOS voice only')
    args = ap.parse_args()

    if args.engine == 'say':
        voice = args.voice or 'Samantha'
    elif args.engine == 'mlx':
        voice = args.voice or MLX_VOICE
    else:
        voice = args.voice or 'Cherry'

    mlx_model = None
    if args.engine == 'mlx':
        from mlx_audio.tts.utils import load_model
        print(f'loading {MLX_MODEL} …')
        mlx_model = load_model(MLX_MODEL)
    lines = json.loads(SCRIPT.read_text())['lines']
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    beats = []
    for i, text in enumerate(lines):
        dest = OUT_DIR / f'{i:02}.wav'
        if args.engine == 'say':
            say_macos(text, dest, voice, args.rate)
        elif args.engine == 'mlx':
            say_mlx(text, dest, mlx_model, voice)
        else:
            say_qwen(text, dest, voice)
        beats.append({'index': i, 'text': text, 'file': dest.name, 'speech': round(duration(dest), 3)})
        print(f'{i:2}  {beats[-1]["speech"]:5.2f}s  {text[:64]}')

    # The camera holds for as long as the line takes, plus a little air.
    for b in beats:
        b['hold'] = round(LEAD_IN + b['speech'] + TAIL, 3)

    TIMINGS.parent.mkdir(parents=True, exist_ok=True)
    TIMINGS.write_text(json.dumps({'engine': args.engine, 'voice': voice, 'beats': beats}, indent=2))

    # One track, with each line landing where its beat starts.
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for b in beats:
            silence = Path(tmp) / f'pad{b["index"]}.wav'
            subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi',
                            '-i', f'anullsrc=r={SR}:cl=mono', '-t', str(LEAD_IN), str(silence)], check=True)
            parts += [silence, OUT_DIR / b['file']]
            tail = Path(tmp) / f'tail{b["index"]}.wav'
            subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi',
                            '-i', f'anullsrc=r={SR}:cl=mono', '-t', str(TAIL), str(tail)], check=True)
            parts.append(tail)
        listing = Path(tmp) / 'list.txt'
        listing.write_text('\n'.join(f"file '{p}'" for p in parts))
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0',
                        '-i', str(listing), '-c', 'copy', str(TRACK)], check=True)

    # Subtitles, timed off the same numbers.
    cues, t = [], 0.0
    for i, b in enumerate(beats, 1):
        start = t + LEAD_IN
        end = start + b['speech']
        cues.append(f'{i}\n{timestamp(start)} --> {timestamp(end)}\n{b["text"]}\n')
        t += b['hold']
    SRT.write_text('\n'.join(cues))

    print(f'\nnarration  {TRACK.relative_to(ROOT)}  {t:.1f}s')
    print(f'subtitles  {SRT.relative_to(ROOT)}')
    print(f'timings    {TIMINGS.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
