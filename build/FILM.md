# The demo video, and why the obvious way looks cheap

Most hackathons cap the video at three minutes, require audio, and require it
public on YouTube. That cap is the hard part: it is not enough time to explain,
so the film has to *show* and let narration carry the argument.

`build/film/` is the pipeline that produced a 2:56 narrated 1920×1080 cut of a
real browser session — not a screen recording of someone talking over a demo.

## The one thing that matters: shoot flat, add motion later

Chrome hands you a frame **only when the picture changes**. So anything
continuous — a zoom, a pan, a moving cursor — is pinned to whatever rate the
encoder managed, and it stutters. The page's own state changes are genuinely
discontinuous and look fine at any rate; the camera move on top of them does
not.

So: capture flat at full resolution with no camera and no cursor, then draw the
camera and pointer afterwards at 60fps over the stills.

    python3 narrate.py --engine say                 # 1. speak the script, get timings
    python3 record.py --flat --flat-dir .flat \     # 2. drive the real app, save stills
        --width 1920 --height 1440 --scale 1.0
    python3 compose.py --frames .flat \             # 3. camera + pointer at 60fps
        --track .flat/track.json --cursor .flat/cursor.json \
        --fps 60 --max-upscale 1.25 --max-zoom 1.35
    python3 mux.py --video /tmp/silent.mp4 --no-subs --out demo.mp4

`make.sh` runs all four.

### Four bugs that all looked like "low frame rate"

Chased for a day as one problem. Each was one term or one line:

1. **`make.sh` never called the flat pipeline it shipped with.** The composited
   camera pass — the entire point — had never once run on a real take.
2. **The camera easing was unreachable.** `ease((t - next.t + MOVE) / MOVE)` is
   ≥1 for every `t` that reaches the line, so every zoom was a hard cut.
3. **The pointer was a DOM element eased in 16ms steps**, which pinned the one
   continuous thing on screen to the encoder's rate. Draw it in the composite.
4. **Each beat called `scrollIntoView`**, so the pixels teleported underneath a
   camera that believed it was panning.

The lesson is not the bugs. It is that **capture throughput was being measured
and improving while the film stayed bad**. A measurement that moves is very good
at hiding a defect it does not cover.

## Timing to the narration, not the other way round

`narrate.py` speaks each line first and writes `timings.json` with real
durations. `record.py` holds each beat for its line's actual length. You never
guess, and re-recording after a script edit costs one command.

Running long? `brisk.py` **plays a window faster** instead of cutting it, and
re-times the SRT to match:

    python3 brisk.py --in demo.mp4 --out short.mp4 --window 78:95 --rate 1.25 --srt narration.srt

## Subtitles

`narration.srt` is generated from the same timings, so it cannot drift.

- **YouTube will not read a subtitle track out of an mp4.** Upload the `.srt`
  separately under Subtitles → English.
- **If the lines are burned into the picture, do not also upload the SRT** —
  viewers see doubled text.
- Set the video **Public**, not Unlisted. "Publicly visible" is usually a literal
  rule, and unlisted has been ruled non-compliant.
- Check the **displayed** length after upload. A 2:56.8 source can round to 3:00
  in the player and a three-minute cap is enforced on what the judge sees. Leave
  more than three seconds of headroom. In the WebMCP field one entry was
  disqualified at 5:17 and the next-longest finalist was 2:59.

## The recorder should refuse a bad take

`record.py` asserts as it films: it reads `getTools()` on both sides of the
approval step and **fails the take if the count did not move**, and it fails if a
control the script reaches for is not on screen. A take that silently didn't
demonstrate the thing is worse than no take.

## Gallery stills

`gallery.py` drives the same private headless Chrome through the same flow and
writes 1800×1200 (exactly 3:2) frames — every image is the product actually
working, not a mockup. Shoot the whole set from one script so numbering can
never drift from your captions.

Devpost galleries want ~15 images under 5MB each. Write the captions in the same
commit as the shots.
