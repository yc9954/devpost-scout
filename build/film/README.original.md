# Filming

Two pieces: a camera that lives in the page, and a recorder that drives it.

## The camera

`src/film/director.ts` transforms React's own container, so a shot is one
`translate(...) scale(...)` — the target's centre moved to the middle of the
viewport, clamped so the stage always covers the frame. `src/film/shotlist.ts`
is the cut: each beat frames something, optionally does something, and holds
long enough to be understood at speaking pace.

It is loaded only when the URL carries `?film=1`, so nothing about the product
changes when nobody is filming.

Watch it live:

```
open 'http://localhost:5183/studio?film=1'   # then, in the console:
window.__film()
```

## The recorder

`film/record.py` launches its own headless Chrome with a throwaway profile,
runs the camera there, polls `Page.captureScreenshot` at 20 fps and hands the
frames to ffmpeg.

```bash
python3 film/record.py --out demo.mp4
python3 film/record.py --url http://localhost:5183/studio --width 1920 --height 1080 --scale 1
```

It never touches the browser you are using: no window resizing, no tab stealing
focus, no forced repaints on your screen. Because it drives the same scripted
beats every time, two runs produce the same film.

### Why the frame rate is what it is

A screenshot over DevTools costs 60–120 ms depending on the viewport, so capture
tops out near sixteen frames a second and it is capture, not the page, that is
the ceiling. Three things follow from that:

- Every frame carries the moment it was taken, and the encoder is given those
  durations. Pretending the frames were evenly spaced is what makes a camera
  move judder.
- The shoot is 1080p at scale 1 rather than a retina viewport, which nearly
  doubles the rate.
- `--interpolate 48` synthesises the frames in between. It costs several minutes
  and it is the only way to get a genuinely smooth pan out of this pipeline.

Chrome's virtual-time clock would be the right answer — advance the page one
exact frame at a time, photograph it, repeat — but `Page.captureScreenshot`
deadlocks while virtual time is paused, with or without `fromSurface: false`.

Requires `ffmpeg` (`brew install ffmpeg`) and the dev server on the given URL.

## The voice

`src/film/script.json` is the only place the words live: the on-screen captions,
the narration and the subtitles all read from it, so they cannot drift.

```bash
python3 film/narrate.py                       # macOS voice, works anywhere
.venv-tts/bin/python film/narrate.py --engine mlx   # Qwen3-TTS, local, no key
DASHSCOPE_API_KEY=... python3 film/narrate.py --engine qwen   # Qwen3-TTS, hosted
```

The `mlx` engine runs
[`mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-8bit`](https://huggingface.co/mlx-community/Qwen3-TTS-12Hz-1.7B-VoiceDesign-8bit)
on Apple silicon — no API key, nothing leaves the machine. It is a VoiceDesign
model, so the voice is written rather than picked:

> A calm, articulate woman in her thirties narrating a software walkthrough.
> Measured pace, warm but precise, no salesmanship.

Setup once:

```bash
python3.12 -m venv .venv-tts && .venv-tts/bin/pip install mlx-audio
```

It renders each line, measures how long it actually takes to say, and writes
those holds to `public/narration.json`. The camera reads them, so a beat lasts
as long as its sentence.

## Putting it together

```bash
./film/make.sh demo.mp4          # narrate, record, mux
ENGINE=qwen ./film/make.sh demo.mp4
```

`film/mux.py` places each line at the beat start the recording actually
produced — actions take an unpredictable amount of time, so timing against the
plan would drift — and writes `film/narration.srt` from the same numbers. The
subtitles ride as a selectable track; the picture already carries the captions,
and burning a second copy in would need an ffmpeg with libass.
