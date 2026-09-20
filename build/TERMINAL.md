# Filming a terminal, and cutting it into the demo

`FILM.md` covers the browser app: shoot flat, draw the camera afterwards. A
terminal is a different problem with a much better answer — **the session can be
source code**, so the demo becomes a build artifact you re-render instead of a
take you got lucky on.

Two of Devpost's five judges say they start with the video. It is the first
impression, the 3-minute cap is the binding constraint, and the project must be
visibly working inside the first 10–15 seconds.

## Use VHS unless you have a reason not to

[`charmbracelet/vhs`](https://github.com/charmbracelet/vhs) records a terminal
from a `.tape` script: window size, theme, typing speed, pauses, and the commands
themselves. Re-running it produces the same frames. No retakes, no fat-fingered
command on take nine, and a typo is a one-line diff.

```sh
brew install vhs          # requires ttyd and ffmpeg
vhs demo.tape
```

```vhs
Output cast/01-discover.mp4          # .gif .mp4 .webm, or a directory of PNG frames
Require scout

Set Shell zsh
Set FontSize 22
Set Width 1920
Set Height 1080
Set Theme "Catppuccin Frappe"
Set TypingSpeed 40ms
Set Framerate 60
Set Padding 40
Set WindowBar Colorful
Set BorderRadius 10
Set CursorBlink false

Hide                                  # setup the judge never sees
Type "cd ~/demo && clear" Enter
Show

Type "scout enter webmcp.devpost.com"
Sleep 400ms
Enter
Wait+Screen /2,392 submissions/       # wait on output, never a fixed Sleep
Sleep 2s

Screenshot stills/census.png          # gallery images, free, from the same run
```

The commands worth knowing beyond the obvious: `Hide`/`Show` to cut setup out of
the capture, `Wait+Screen /regex/` to synchronise on real output instead of
guessing a `Sleep`, `Screenshot` to mint gallery stills from the same take, and
`Source other.tape` to compose long demos from short files.

**`Wait` instead of `Sleep` is the one that matters.** A tape built on fixed
sleeps desynchronises the moment the machine is slower, and you will not notice
until the render is 30 seconds over the cap.

## When not to use VHS

| situation | tool | why |
| --- | --- | --- |
| Scripted, reproducible CLI demo | **VHS** | tape is source; re-renders identically |
| A real session you already ran and want to keep honest | **asciinema** → `agg` | records an actual session to `.cast`; `agg` renders GIF |
| README embed, tiny file, selectable text | **svg-term-cli** or asciinema player | SVG stays sharp, bytes stay small |
| A GUI or browser app | `build/film/` | Chrome only emits frames on change — see FILM.md |
| Cursor-following auto-zoom over a desktop | OpenScreen, or `compose.py` | the Screen-Studio effect, open source |

Do not ship a raw `.cast` as the demo video — Devpost wants a public YouTube/Vimeo
link. Render to MP4 and upload; keep the `.cast` or `.tape` in the repo as the
reproducibility artifact. That pairing is itself a rung on the ladder in
`../write/WINNING-WRITEUPS.md`: the judge can re-render your demo.

## Cutting terminal and browser together

Shoot each beat separately, then concatenate. Never try to film one continuous
session that switches between a terminal and a browser — the framerate
characteristics are different and the cut will look worse than a hard join.

```sh
# normalise every segment to identical codec/fps/size first, or concat drifts
for f in cast/*.mp4; do
  ffmpeg -i "$f" -vf "scale=1920:1080:force_original_aspect_ratio=decrease,\
pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=60" -c:v libx264 -crf 18 -pix_fmt yuv420p \
    -an "norm/$(basename "$f")" -y
done
printf "file '%s'\n" norm/*.mp4 > list.txt
ffmpeg -f concat -safe 0 -i list.txt -c copy silent.mp4 -y
```

Then narration and mux go through the existing pipeline: `film/narrate.py` speaks
the script and emits timings, `film/mux.py` lays the voice over. `film/brisk.py`
speeds a window rather than cutting it when you are over 3:00 — losing a beat
costs more than playing one at 1.25×.

## Programmatic editing, if you need titles and callouts

Only reach for these when a static overlay is not enough. Ranked by fit here:

- **Remotion** — video as React components, renders to MP4, headless/CI-friendly.
  The right choice if the video should regenerate when the numbers change.
- **Motion Canvas** — TypeScript generator functions, a real-time editor, built
  for explanatory animation. Better for one hand-crafted diagram sequence.
- **Revideo** — Motion Canvas fork with a rendering API, aimed at automated
  pipelines.

The reason to care: if your write-up's numbers come from `reproduce.sh`, a
Remotion title card can read the same JSON. Then the video cannot drift from the
claims — which is the exact defect `EVIDENCE.md` documents as most expensive.

## The 3-minute budget

| segment | seconds | must contain |
| --- | ---: | --- |
| Cold open | 0–15 | the thing working, no logo, no team intro |
| The stake | 15–35 | the anchor sentence from `../write/IMPACT.md` |
| The demo | 35–150 | one continuous task, start to finish, no cuts inside a beat |
| The proof | 150–165 | the ablation or the test count, on screen |
| Close | 165–176 | the live URL, readable, held for 3 seconds |

Leave four seconds of slack. Every render comes in longer than the tape math says.

## Checks before upload

- [ ] Renders under the cap with slack, from a clean checkout
- [ ] Audio exists (most hackathons require it) and is not clipped
- [ ] The first 10 seconds show the product working, not a title card
- [ ] Every on-screen number matches `CLAIMS.md`
- [ ] No secrets in scrollback — `Hide`/`Show` around anything with a token
- [ ] The live URL is legible at 720p, held long enough to type
- [ ] Public on YouTube/Vimeo, not unlisted-only if the rules say public
- [ ] The `.tape`/`.cast` is committed
