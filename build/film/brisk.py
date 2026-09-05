#!/usr/bin/env python3
"""
Play part of the film faster, rather than cutting it out.

The cut is under three minutes by four seconds, which is not margin. The usual
answer is to drop a beat, but a beat dropped is an argument gone; a beat played
at 1.2x is still an argument, just delivered briskly. Picture and narration are
sped together — setpts on the video, atempo on the audio, which preserves pitch
— so nothing drifts out of sync, and the subtitles are re-timed to match.

  python3 film/brisk.py --in demo.mp4 --out demo-short.mp4 --window 78:95 --rate 1.25
  python3 film/brisk.py --in demo.mp4 --out demo-short.mp4 \
      --window 78:95 --rate 1.25 --window 104:112 --rate 1.15

Rates above about 1.3 start to sound hurried; 1.15 to 1.25 reads as edited.
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path


def duration(path):
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                          '-of', 'default=nw=1:nk=1', str(path)],
                         capture_output=True, text=True).stdout.strip()
    return float(out)


def atempo_chain(rate):
    """atempo only accepts 0.5–2.0 per filter, so a bigger change is chained."""
    parts, r = [], rate
    while r > 2.0:
        parts.append('atempo=2.0')
        r /= 2.0
    while r < 0.5:
        parts.append('atempo=0.5')
        r /= 0.5
    parts.append(f'atempo={r:.6f}')
    return ','.join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='src', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--window', action='append', required=True,
                    help='START:END in seconds, repeatable')
    ap.add_argument('--rate', action='append', type=float, required=True,
                    help='speed for the matching --window, e.g. 1.25')
    ap.add_argument('--srt', default='', help='subtitles to re-time alongside')
    args = ap.parse_args()

    if len(args.window) != len(args.rate):
        sys.exit('give one --rate per --window')

    spans = []
    for w, r in zip(args.window, args.rate):
        a, b = (float(x) for x in w.split(':'))
        if b <= a:
            sys.exit(f'window {w} ends before it starts')
        spans.append((a, b, r))
    spans.sort()
    for (a1, b1, _), (a2, _, _) in zip(spans, spans[1:]):
        if a2 < b1:
            sys.exit('windows overlap')

    total = duration(args.src)
    # Cut the film into alternating ordinary and brisk segments, speed the brisk
    # ones, and concatenate. Done in one filter graph so there is no generation
    # loss from writing intermediate files.
    cuts, at = [], 0.0
    for a, b, r in spans:
        if a > at:
            cuts.append((at, a, 1.0))
        cuts.append((a, b, r))
        at = b
    if at < total:
        cuts.append((at, total, 1.0))

    parts, saved = [], 0.0
    for i, (a, b, r) in enumerate(cuts):
        parts.append(
            f'[0:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{r}[v{i}];'
            f'[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS'
            + (f',{atempo_chain(r)}' if r != 1.0 else '') + f'[a{i}];')
        saved += (b - a) * (1 - 1 / r)
    chain = ''.join(parts) + ''.join(f'[v{i}][a{i}]' for i in range(len(cuts)))
    chain += f'concat=n={len(cuts)}:v=1:a=1[v][a]'

    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', args.src,
                    '-filter_complex', chain, '-map', '[v]', '-map', '[a]',
                    '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
                    '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k',
                    '-movflags', '+faststart', args.out], check=True)

    if args.srt and Path(args.srt).exists():
        def warp(t):
            out = 0.0
            for a, b, r in cuts:
                if t >= b:
                    out += (b - a) / r
                elif t > a:
                    out += (t - a) / r
                    break
            return out

        def stamp(t):
            ms = int(round(t * 1000))
            h, ms = divmod(ms, 3_600_000)
            m, ms = divmod(ms, 60_000)
            s, ms = divmod(ms, 1000)
            return f'{h:02}:{m:02}:{s:02},{ms:03}'

        def to_seconds(text):
            h, m, rest = text.split(':')
            s, ms = rest.split(',')
            return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

        src = Path(args.srt).read_text()
        out = re.sub(
            r'(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)',
            lambda m: f'{stamp(warp(to_seconds(m.group(1))))} --> '
                      f'{stamp(warp(to_seconds(m.group(2))))}', src)
        Path(args.out).with_suffix('.srt').write_text(out)

    print(f'{args.src} {total:.1f}s → {args.out} {duration(args.out):.1f}s '
          f'({saved:.1f}s saved across {len(spans)} window'
          f'{"" if len(spans) == 1 else "s"})')


main()
