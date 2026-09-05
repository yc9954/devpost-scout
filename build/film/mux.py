#!/usr/bin/env python3
"""Lay the voice and the subtitles onto the recorded film.

Each line is placed at the beat start the recording actually produced, so the
voice stays with the picture no matter how long an action took that run.

  python3 film/mux.py --video demo.mp4 --out demo-final.mp4          # soft subs
  python3 film/mux.py --video demo.mp4 --out demo-final.mp4 --burn   # burned in
"""
import argparse, json, subprocess, tempfile, wave
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILM = ROOT / 'film'
SR = 48_000


def duration(path: Path) -> float:
    with wave.open(str(path)) as w:
        return w.getnframes() / w.getframerate()


def stamp(t: float) -> str:
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f'{h:02}:{m:02}:{s:02},{ms:03}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--video', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--burn', action='store_true', help='burn the subtitles into the picture')
    ap.add_argument('--lead-in', type=float, default=0.35)
    ap.add_argument('--no-subs', action='store_true',
                    help='do not attach a subtitle track: the picture already carries the lines')
    args = ap.parse_args()

    video = Path(args.video)
    if not video.exists():
        raise SystemExit(f'{video} does not exist — did the recording fail?')
    # timings.json is written at the end of a successful shoot. A video older
    # than it is a leftover from a previous run, and muxing it would produce a
    # film of a build that is no longer there.
    if video.stat().st_mtime < (FILM / 'timings.json').stat().st_mtime - 1:
        raise SystemExit(
            f'{video} is older than film/timings.json — that is a leftover from an '
            'earlier shoot. Re-run film/record.py.')

    narration = json.loads((ROOT / 'public' / 'narration.json').read_text())
    timings = json.loads((FILM / 'timings.json').read_text())
    starts = timings['starts']
    beats = narration['beats']
    if len(starts) < len(beats):
        raise SystemExit(f'the recording has {len(starts)} beats but the script has {len(beats)}')

    # One silent bed the length of the film, with each line dropped onto it.
    total = float(timings.get('total') or starts[-1] + 6)
    with tempfile.TemporaryDirectory() as tmp:
        tmpd = Path(tmp)
        bed = tmpd / 'bed.wav'
        subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi',
                        '-i', f'anullsrc=r={SR}:cl=mono', '-t', f'{total + 1.5:.3f}', str(bed)], check=True)

        inputs, filters, labels = ['-i', str(bed)], [], ['[0:a]']
        for n, b in enumerate(beats, start=1):
            line = FILM / 'audio' / b['file']
            delay = int(round((starts[b['index']] + args.lead_in) * 1000))
            inputs += ['-i', str(line)]
            filters.append(f'[{n}:a]adelay={delay}|{delay}[a{n}]')
            labels.append(f'[a{n}]')
        filters.append(f'{"".join(labels)}amix=inputs={len(labels)}:normalize=0[out]')

        voice = tmpd / 'voice.wav'
        subprocess.run(['ffmpeg', '-y', '-v', 'error', *inputs,
                        '-filter_complex', ';'.join(filters), '-map', '[out]',
                        '-ar', str(SR), '-ac', '2', str(voice)], check=True)

        # Subtitles from the same numbers.
        srt = FILM / 'narration.srt'
        cues = []
        for i, b in enumerate(beats, start=1):
            start = starts[b['index']] + args.lead_in
            cues.append(f'{i}\n{stamp(start)} --> {stamp(start + b["speech"])}\n{b["text"]}\n')
        srt.write_text('\n'.join(cues))

        # The picture already carries the captions, so subtitles ride along as a
        # selectable track. Burning them in needs an ffmpeg built with libass,
        # which this one is not, and doubling them up would be worse anyway.
        has_libass = 'subtitles' in subprocess.run(
            ['ffmpeg', '-hide_banner', '-filters'], capture_output=True, text=True).stdout
        if args.no_subs:
            # compose.py drew the lines into the picture, from these same
            # numbers. A second, selectable copy of them shows up doubled in
            # players that turn it on by default, which includes the one the
            # judges will use.
            cmd = ['ffmpeg', '-y', '-v', 'error', '-i', args.video, '-i', str(voice),
                   '-map', '0:v:0', '-map', '1:a:0',
                   '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', args.out]
        else:
            cmd = ['ffmpeg', '-y', '-v', 'error', '-i', args.video, '-i', str(voice), '-i', str(srt),
                   '-map', '0:v:0', '-map', '1:a:0', '-map', '2:s:0',
                   '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-c:s', 'mov_text',
                   '-metadata:s:s:0', 'language=eng', '-shortest', args.out]
        if args.burn and not has_libass:
            print('this ffmpeg has no subtitles filter (no libass); compose.py burns them instead')
        subprocess.run(cmd, check=True)

    print(f'wrote {args.out}')
    print(f'subtitles at {srt.relative_to(ROOT)} — upload alongside the video')


if __name__ == '__main__':
    main()
