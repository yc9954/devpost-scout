#!/usr/bin/env python3
"""
Put the camera on afterwards, the way the recorders that do not stutter do.

Screen Studio and the rest record the screen flat and animate the zoom during
rendering. The app never composites a moving transform, so it keeps painting at
full rate, and the pan is a crop of pixels that were already captured — every
frame is real, nothing is interpolated.

This does the same thing to a flat capture. It takes the frames record.py kept,
the camera track the film wrote down, and emits one image per output frame at a
constant rate: the frame that was on screen at that moment, cropped to where the
camera was looking, eased between beats.

  python3 film/compose.py --frames DIR --track track.json --out silent.mp4
"""
import argparse, json, os, shutil, subprocess, sys, tempfile, textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter

# A cut is instant; a move settles in under a second. Long enough to read as
# deliberate, short enough that nothing waits for the camera.
MOVE = 0.85


def ease(p: float) -> float:
    """Smooth in and out, without the overshoot an elastic curve would add."""
    p = max(0.0, min(1.0, p))
    return p * p * (3 - 2 * p)


def ease_out(p: float) -> float:
    """Leaves fast and arrives slow, which is how a hand moves and how a camera
    operator stops. Applied to the pointer, where a symmetric curve reads as a
    machine sliding a sprite."""
    p = max(0.0, min(1.0, p))
    return 1 - (1 - p) ** 3


def camera_at(track, t, fix=lambda c: c):
    """Where the camera is looking at time t, easing in from where it was.

    `fix` is the clamp that keeps a crop inside the picture and above the
    upscale budget. It is applied to the two ends and the result interpolated
    between them, never to the interpolated value: clamping every frame makes
    the correction change as the crop grows, and the centre travels an L
    instead of a line — the camera going sideways and then down when the
    pointer went diagonally.

    A mark flagged `cut` snaps. Those are the beats where the page scrolled: the
    pixels underneath teleport, so easing the crop across that teleport is the
    one motion in this film that cannot be smooth. Cutting on it is not a
    compromise, it is the edit the jump was always asking for.
    """
    i = 0
    for j, m in enumerate(track):
        if m['t'] <= t:
            i = j
        else:
            break
    to = fix(track[i])
    if i == 0 or track[i].get('cut'):
        return to
    frm = fix(track[i - 1])
    # The move starts at the mark and settles over MOVE seconds. This used to
    # read the previous mark as the destination and add MOVE to the numerator,
    # which made the eased term at least 1 for every t that reached it: the
    # easing was unreachable and every beat change was a hard cut. That is the
    # camera motion that was missing from the whole film.
    p = ease((t - track[i]['t']) / MOVE)
    return {k: frm[k] + (to[k] - frm[k]) * p for k in ('x', 'y', 'w', 'h')}


def cursor_at(track, t):
    """Where the pointer is at time t, and whether it is pressed.

    The film wrote down only the ends of each journey. Everything between them
    is drawn here, at the output rate, so the pointer is exact at 60fps even
    though the screen underneath was captured at twenty-something.
    """
    if not track or t < track[0]['t']:
        # Before it first moves there is no pointer on screen. It used to be
        # drawn at whatever the initial coordinate happened to be, which was
        # the top-left corner, so an arrow sat in the corner of the opening
        # slides for the best part of a minute.
        return None
    prev = track[0]
    nxt = None
    for m in track:
        if m['t'] <= t:
            prev = m
        else:
            nxt = m
            break
    down = False
    for m in track:
        if m['t'] > t:
            break
        if 'down' in m:
            down = m['down']
    if nxt is None or nxt['t'] <= prev['t']:
        return {'x': prev['x'], 'y': prev['y'], 'down': down}
    p = ease_out((t - prev['t']) / (nxt['t'] - prev['t']))
    return {
        'x': prev['x'] + (nxt['x'] - prev['x']) * p,
        'y': prev['y'] + (nxt['y'] - prev['y']) * p,
        'down': down,
    }


# macOS' arrow, as a path in a 24-unit box. Drawn rather than pasted so it stays
# crisp at whatever size the frame calls for.
ARROW = [(0, 0), (0, 16.5), (4.1, 12.8), (6.7, 19.2), (9.6, 18.0), (7.1, 11.8), (12.4, 11.6)]
# Room around the arrow for the press ring and the shadow's blur.
PAD = 22


def draw_cursor(frame, x, y, down, scale=1.55):
    """A pointer with a shadow, and a ring when it presses.

    Composited at output resolution, so its edges are the frame's edges rather
    than a screenshot's — which is the visible difference between a recording
    with a real cursor and one with a cursor that was filmed.

    Drawn into a small tile around the pointer rather than a full-frame layer.
    A blurred 1920x1080 RGBA shadow costs about eighty milliseconds; over ten
    thousand output frames that is a quarter of an hour spent on a shape that
    covers four hundred pixels.
    """
    pts = [(px * scale, py * scale) for px, py in ARROW]
    w = int(max(p[0] for p in pts)) + PAD * 2
    h = int(max(p[1] for p in pts)) + PAD * 2
    x0, y0 = int(x) - PAD, int(y) - PAD
    if x0 > frame.width or y0 > frame.height or x0 + w < 0 or y0 + h < 0:
        return

    tile = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(tile)
    if down:
        r = 15
        d.ellipse((PAD - r, PAD - r, PAD + r, PAD + r), fill=(255, 255, 255, 44),
                  outline=(255, 255, 255, 130), width=2)

    shadow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).polygon([(PAD + px + 1, PAD + py + 2) for px, py in pts],
                                   fill=(0, 0, 0, 110))
    tile = Image.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(2.4)), tile)
    ImageDraw.Draw(tile).polygon([(PAD + px, PAD + py) for px, py in pts],
                                 fill=(255, 255, 255, 255), outline=(18, 20, 24, 255))

    # Crop the tile to what actually lands on the frame, so a pointer at the
    # edge is clipped rather than refused.
    cx0, cy0 = max(0, -x0), max(0, -y0)
    cx1 = min(w, frame.width - x0)
    cy1 = min(h, frame.height - y0)
    if cx1 <= cx0 or cy1 <= cy0:
        return
    tile = tile.crop((cx0, cy0, cx1, cy1))
    frame.paste(tile, (x0 + cx0, y0 + cy0), tile)


# The narration, drawn into the picture rather than by the page. A caption the
# page renders sits at the bottom of the viewport, and the camera crops a
# window out of that viewport — so it lands wherever the crop happens to be,
# which in one shot was directly on the panel being framed.
CAPTION_FONTS = [
    '/System/Library/Fonts/Supplemental/Arial.ttf',
    '/System/Library/Fonts/Helvetica.ttc',
    '/Library/Fonts/Arial.ttf',
]


def caption_font(size):
    from PIL import ImageFont
    for path in CAPTION_FONTS:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except OSError:
                continue
    return ImageFont.load_default()


def cues_from(narration_path, timings_path, lead_in=0.35, skip=()):
    """The same arithmetic mux.py uses for the subtitle file, so the burned-in
    line and the sidecar .srt cannot disagree.

    Every beat gets its line, slides included. Skipping them was a workaround
    for a caption drawn on top of the picture, where a slide's own words and
    the spoken version of them piled up in the same place. The band made that
    moot: the words have a strip of their own, and a viewer with the sound off
    should not lose the first fifty seconds of the argument.
    """
    if not (os.path.exists(narration_path) and os.path.exists(timings_path)):
        return []
    narration = json.loads(open(narration_path).read())
    timings = json.loads(open(timings_path).read())
    starts = timings['starts']
    skip = set(skip)
    out = []
    for b in narration['beats']:
        if b['index'] >= len(starts) or b['index'] in skip:
            continue
        start = starts[b['index']] + lead_in
        out.append((start, start + b['speech'], b['text']))
    return out


# Every line of the script fits two of these, measured against the longest one
# in it. A third would not fit the band, and a band that grows to suit one
# sentence moves the picture for that sentence.
WRAP = 112
BAND_INK = (247, 247, 245)
BAND_GROUND = (14, 15, 17)


def draw_caption(frame, text, font, width, top, band):
    """Write the line into the band below the picture.

    It used to be a pill drawn over the frame, and on the shot that framed the
    suspended write it landed squarely on the panel. Words that cover the thing
    they are describing are worse than no words, and the fix is not to move the
    pill around — it is to give the words somewhere of their own.
    """
    from PIL import ImageDraw
    d = ImageDraw.Draw(frame)
    lines = textwrap.wrap(text, width=WRAP)[:2] or ['']
    sizes = [d.textbbox((0, 0), ln, font=font) for ln in lines]
    lh = max(s[3] - s[1] for s in sizes) + 12
    y = top + (band - lh * len(lines)) / 2 - 2
    for ln, sz in zip(lines, sizes):
        d.text(((width - (sz[2] - sz[0])) / 2, y), ln, font=font, fill=BAND_INK)
        y += lh


def clamp(c, page_w, page_h, min_w):
    """Keep the crop big enough that blowing it up does not soften the text.

    The camera frames an element, and a small element asks for a small crop —
    a 901px window stretched to 1920 is a 2.1x upscale and it shows. The crop
    grows around its own centre until it is within the upscale budget, then
    slides back inside the picture.
    """
    aspect = c['w'] / c['h']
    w = min(page_w, max(c['w'], min_w))
    h = w / aspect
    if h > page_h:
        h = page_h
        w = h * aspect
    cx = c['x'] + c['w'] / 2
    cy = c['y'] + c['h'] / 2
    x = min(max(cx - w / 2, 0), page_w - w)
    y = min(max(cy - h / 2, 0), page_h - h)
    return {'x': x, 'y': y, 'w': w, 'h': h}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--frames', required=True, help='directory of NNNNN.jpg plus stamps.json')
    ap.add_argument('--track', required=True)
    ap.add_argument('--cursor', default='', help='pointer keyframes from the film')
    ap.add_argument('--narration', default='public/narration.json',
                    help='the script with each line\'s spoken length, for burned-in captions')
    ap.add_argument('--no-captions', action='store_true')
    ap.add_argument('--no-caption-beats', default='',
                    help='beat indices to leave without a line, comma separated')
    ap.add_argument('--caption-band', type=int, default=132,
                    help='height of the strip along the bottom that the narration lives in')
    ap.add_argument('--out', required=True)
    ap.add_argument('--fps', type=int, default=60)
    ap.add_argument('--width', type=int, default=1920)
    ap.add_argument('--height', type=int, default=1080)
    ap.add_argument('--scale', type=float, default=1.0, help='capture pixels per CSS pixel')
    ap.add_argument('--seconds', type=float, default=0.0,
                    help='stop composing at this many seconds of film')
    ap.add_argument('--max-upscale', type=float, default=1.0,
                    help='how far a crop may be blown up past 1:1; 1.0 never softens text')
    ap.add_argument('--max-zoom', type=float, default=1.35,
                    help='how far in the camera may push, sharpness aside; a hard push '
                         'slices whatever panel sits beside the thing being framed')
    args = ap.parse_args()

    src = Path(args.frames)
    stamps = json.loads((src / 'stamps.json').read_text())
    track = json.loads(Path(args.track).read_text())
    pointer = []
    if args.cursor and Path(args.cursor).exists():
        pointer = json.loads(Path(args.cursor).read_text())
    skip = [int(n) for n in args.no_caption_beats.split(',') if n.strip()]
    cues = [] if args.no_captions else cues_from(args.narration, str(src / 'timings.json'), skip=skip)
    font = caption_font(28)
    band = 0 if args.no_captions else args.caption_band
    picture_h = args.height - band
    if not track:
        sys.exit('the film wrote no camera track; was it run with __filmFlat?')

    shots = sorted(src.glob('*.jpg'))
    if len(shots) != len(stamps):
        sys.exit(f'{len(shots)} frames but {len(stamps)} stamps')

    # The capture keeps running for a beat after the film ends, and those
    # trailing frames pushed the cut past three minutes — the one hard number in
    # the rules. The film's own length is what the narration was written to, so
    # the composition stops there plus a breath.
    total = stamps[-1]
    # The film says how long it was. Trusting that rather than the capture span
    # keeps the picture and the narration the same length, which is what the
    # subtitles are timed against.
    timings = src / 'timings.json'
    if timings.exists():
        told = json.loads(timings.read_text()).get('total')
        if told:
            total = min(total, told + 0.6)
    if args.seconds:
        total = min(total, args.seconds)
    out_dir = tempfile.mkdtemp(prefix='warrant-compose-')
    print(f'composing {int(total * args.fps)} frames at {args.fps}fps into {out_dir}')

    # The upscale budget is in captured pixels, not CSS pixels. Shooting at a
    # device scale of 1.5 means a 1280 CSS-px crop already carries 1920 real
    # ones, so it fills the frame at 1:1 — the zoom costs nothing.
    first = Image.open(shots[0])
    page_w, page_h = first.width / args.scale, first.height / args.scale
    min_w = max(args.width / (args.scale * args.max_upscale), args.width / args.max_zoom)
    fix = lambda c: clamp(c, page_w, page_h, min_w)

    cur = -1
    img = None
    n_out = 0
    for i in range(int(total * args.fps)):
        t = i / args.fps
        # The frame that was on screen at t: the last one captured before it.
        while cur + 1 < len(stamps) and stamps[cur + 1] <= t:
            cur += 1
            img = None
        if cur < 0:
            cur = 0
        if img is None:
            img = Image.open(shots[cur]).convert('RGB')
        c = camera_at(track, t, fix)
        box = (
            int(c['x'] * args.scale), int(c['y'] * args.scale),
            int((c['x'] + c['w']) * args.scale), int((c['y'] + c['h']) * args.scale),
        )
        box = (max(0, box[0]), max(0, box[1]),
               min(img.width, box[2]), min(img.height, box[3]))
        picture = img.crop(box).resize((args.width, picture_h), Image.LANCZOS)
        p = cursor_at(pointer, t)
        if p is not None:
            # Viewport pixels to picture pixels, through whatever the camera is
            # doing: the pointer zooms with the picture because it is placed in
            # the picture's own coordinates, not pasted on top of the result.
            k = args.width / c['w']
            draw_cursor(picture, (p['x'] - c['x']) * k, (p['y'] - c['y']) * k, p['down'])
        if band:
            frame = Image.new('RGB', (args.width, args.height), BAND_GROUND)
            frame.paste(picture, (0, 0))
            line = next((c2[2] for c2 in cues if c2[0] <= t <= c2[1]), None)
            if line:
                draw_caption(frame, line, font, args.width, picture_h, band)
        else:
            frame = picture
        frame.save(os.path.join(out_dir, f'{i:06d}.jpg'), quality=92)
        n_out += 1
        if i and i % (args.fps * 15) == 0:
            print(f'  {i / args.fps:.0f}s of {total:.0f}s')

    subprocess.run([
        'ffmpeg', '-y', '-v', 'error', '-framerate', str(args.fps),
        '-i', os.path.join(out_dir, '%06d.jpg'),
        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium',
        '-movflags', '+faststart', args.out,
    ], check=True)
    shutil.rmtree(out_dir, ignore_errors=True)
    print(f'{n_out} frames at a constant {args.fps}fps → {args.out}'
      f" · pointer: {len(pointer)} keyframes, {len(cues)} captions, drawn here")


main()
