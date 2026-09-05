#!/usr/bin/env python3
"""Record the scripted walkthrough in a browser of its own.

This never touches the browser you are using. It launches a private, headless
Chrome with its own profile, drives the page's camera there, captures frames and
hands them to ffmpeg — so the same command produces the same film, and nothing
flickers on your screen while it runs.

  python3 film/record.py --out demo.mp4
"""
import argparse, base64, json, os, shutil, signal, socket, subprocess, sys, tempfile, threading, time, urllib.request
import websocket

CHROME_CANDIDATES = [
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    shutil.which('google-chrome') or '',
    shutil.which('chromium') or '',
]


def find_chrome() -> str:
    for path in CHROME_CANDIDATES:
        if path and os.path.exists(path):
            return path
    sys.exit('no Chrome found; pass --chrome /path/to/chrome')


def free_port() -> int:
    with socket.socket() as s:
        s.bind(('127.0.0.1', 0))
        return s.getsockname()[1]


def launch(chrome: str, port: int, width: int, height: int, scale: int):
    profile = tempfile.mkdtemp(prefix='warrant-chrome-')
    proc = subprocess.Popen(
        [
            chrome,
            '--headless=new',
            f'--remote-debugging-port={port}',
            f'--user-data-dir={profile}',
            f'--window-size={width},{height}',
            f'--force-device-scale-factor={scale}',
            '--hide-scrollbars',
            # Headless composites in software by default, and the camera is one
            # big transform on the whole page: every frame of a move is a full
            # re-raster on the CPU, which is what capped the capture at six or
            # seven frames a second. These hand it to the GPU instead.
            '--enable-gpu',
            '--enable-gpu-rasterization',
            '--ignore-gpu-blocklist',
            '--use-angle=metal',
            '--disable-frame-rate-limit',
            '--no-first-run',
            '--no-default-browser-check',
            '--disable-extensions',
            # Film in a browser that really implements WebMCP, so the page shown
            # is the one an agent would reach — not the no-host fallback.
            '--enable-blink-features=WebMCP',
            'about:blank',
        ],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    for _ in range(80):
        try:
            urllib.request.urlopen(f'http://127.0.0.1:{port}/json/version', timeout=1)
            return proc, profile
        except Exception:
            time.sleep(0.25)
    proc.kill()
    sys.exit('the recording browser never came up')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--url', default='http://localhost:5173/studio')
    ap.add_argument('--out', default='demo.mp4')
    ap.add_argument('--width', type=int, default=1920)
    ap.add_argument('--height', type=int, default=1080)
    ap.add_argument('--scale', type=float, default=1.0)
    ap.add_argument('--fps', type=int, default=30)
    ap.add_argument('--budget', type=int, default=300, help='hard stop, in seconds of film')
    ap.add_argument('--chrome', default='')
    ap.add_argument('--quality', type=int, default=80,
                    help='screencast JPEG quality; the frame rate is very sensitive to it')
    ap.add_argument('--keep-frames', action='store_true')
    ap.add_argument('--flat-dir', default='', help='where --flat leaves its frames')
    ap.add_argument('--interpolate', type=int, default=0, metavar='FPS',
                    help='synthesise intermediate frames up to this rate (slow, but smooth)')
    ap.add_argument('--flat', action='store_true',
                    help='record without a camera and keep the frames for film/compose.py')
    ap.add_argument('--legacy-capture', action='store_true',
                    help='one CDP screenshot per frame; slower and choppier, kept as a fallback')
    args = ap.parse_args()

    if not shutil.which('ffmpeg'):
        sys.exit('ffmpeg is required: brew install ffmpeg')

    chrome = args.chrome or find_chrome()
    port = free_port()
    # A stale file from an earlier run is worse than no file: the next step
    # would mux it and produce a film of a build that no longer exists.
    if os.path.exists(args.out):
        os.remove(args.out)

    proc, profile = launch(chrome, port, args.width, args.height, args.scale)
    print(f'recording browser on port {port} (pid {proc.pid})')

    try:
        tab = json.load(urllib.request.urlopen(
            urllib.request.Request(f'http://127.0.0.1:{port}/json/new?about:blank', method='PUT')))
        ws = websocket.create_connection(tab['webSocketDebuggerUrl'], timeout=120,
                                         suppress_origin=True, max_size=64 * 1024 * 1024)
        rid = 0

        events = []
        # One reader owns the socket. Screencast frames arrive unsolicited and
        # have to be acknowledged the moment they land or Chrome throttles the
        # stream, so replies and frames cannot share a single blocking recv.
        replies = {}
        frames_in = []
        lock = threading.Lock()
        send_lock = threading.Lock()
        reading = threading.Event()
        reading.set()

        def reader():
            while reading.is_set():
                try:
                    msg = json.loads(ws.recv())
                except Exception:
                    return
                if msg.get('method') == 'Page.screencastFrame':
                    p = msg['params']
                    with lock:
                        frames_in.append((p['metadata']['timestamp'], p['data']))
                    try:
                        with send_lock:
                            ws.send(json.dumps({'id': 0, 'method': 'Page.screencastFrameAck',
                                                'params': {'sessionId': p['sessionId']}}))
                    except Exception:
                        return
                elif 'id' in msg:
                    replies[msg['id']] = msg
                elif msg.get('method'):
                    events.append(msg)

        pump = threading.Thread(target=reader, daemon=True)
        pump.start()

        def call(method, params=None):
            nonlocal rid
            rid += 1
            mine = rid
            with send_lock:
                ws.send(json.dumps({'id': mine, 'method': method, 'params': params or {}}))
            deadline = time.time() + 180
            while time.time() < deadline:
                if mine in replies:
                    return replies.pop(mine)
                if not pump.is_alive():
                    raise RuntimeError(
                        f'the CDP reader died before {method} answered; '
                        'every later read would have come back empty')
                time.sleep(0.002)
            raise RuntimeError(f'{method} did not answer in 180s')

        def js(expr):
            r = call('Runtime.evaluate', {'expression': expr, 'returnByValue': True, 'awaitPromise': True})
            return r.get('result', {}).get('result', {}).get('value')

        def fire(expr):
            """Start something and return immediately; the film runs for a minute."""
            call('Runtime.evaluate', {'expression': expr, 'awaitPromise': False})

        call('Page.enable')
        call('Runtime.enable')
        call('Emulation.setDeviceMetricsOverride',
             {'width': args.width, 'height': args.height, 'deviceScaleFactor': args.scale, 'mobile': False})
        # Every CSS transition and keyframe in the film is continuous motion
        # rendered by the page, which means it is captured at whatever rate the
        # encoder can manage — the one thing this pipeline exists to avoid. The
        # deck's slide-entry animation was the stutter in the opening minute.
        # Emulating reduced motion turns all of them into cuts, and it reaches
        # the brief.html iframe, which a class on our own body cannot.
        call('Emulation.setEmulatedMedia',
             {'features': [{'name': 'prefers-reduced-motion', 'value': 'reduce'}]})

        url = args.url + ('&' if '?' in args.url else '?') + 'film=1'
        # Tools persist per site now, so a second take would inherit the first
        # take's tool and the mint would be refused for a duplicate name. The
        # film is always of someone arriving for the first time, so the take
        # begins from a hard reload with nothing carried over: no stored tools,
        # no service worker, no cache, and the browser's own idea of where the
        # page was scrolled to thrown away.
        call('Network.enable')
        call('Network.setCacheDisabled', {'cacheDisabled': True})
        call('Page.setBypassServiceWorker', {'bypass': True})
        call('Page.navigate', {'url': url})
        time.sleep(1.0)
        js('try { localStorage.clear(); sessionStorage.clear(); } catch {}')
        js('history.scrollRestoration = "manual"')
        call('Page.reload', {'ignoreCache': True})

        # Wait for the reload to actually finish rather than sleeping at it.
        for _ in range(80):
            if js('document.readyState') == 'complete':
                break
            time.sleep(0.25)
        else:
            sys.exit('the page never finished loading; is the dev server running?')
        js('window.scrollTo(0, 0)')

        for _ in range(60):
            if js('typeof window.__film === "function"'):
                break
            time.sleep(0.25)
        else:
            sys.exit('the page never exposed its camera; is the dev server running?')
        # A fresh load means no tool from a previous take is still registered.
        left = js('JSON.stringify(Object.keys(JSON.parse(localStorage.getItem("warrant") || "{}")))')
        if left and left not in ('[]', 'null'):
            print(f'  storage was not empty after the reload: {left}')


        # Take frames from the compositor, not one CDP round trip at a time.
        #
        # Page.captureScreenshot costs 70-120ms each, which caps capture near
        # twelve frames a second — so a 1300ms camera move was being described
        # with eighteen samples and read as a stutter. Page.startScreencast
        # pushes a frame whenever the compositor produces one, at the rate the
        # animation actually runs, and emits nothing while the picture is still.
        # Those stills cost nothing: each frame keeps the duration it was on
        # screen for, so a held shot is one frame with a long duration.
        if not args.legacy_capture:
            # Measured, not guessed. The bottleneck is Chrome's own JPEG
            # encoder, not compositing: on this machine a spinning box captured
            # at 1920x1080 gives 22fps at quality 90, 30fps at 80 and 40fps at
            # 60, while doubling the pixel scale drops it to 8.7fps. So the film
            # is captured at 1:1 and a quality that holds thirty frames a second,
            # which is the rate it is played back at.
            call('Page.startScreencast', {
                'format': 'jpeg', 'quality': args.quality, 'everyNthFrame': 1,
                'maxWidth': int(args.width * args.scale), 'maxHeight': int(args.height * args.scale),
            })
            if args.flat:
                # No camera during capture: the page paints only its own
                # changes, which is what keeps the frame rate up. compose.py
                # puts the camera on afterwards.
                js('window.__filmFlat = true')
            fire('void window.__film()')
            started = time.time()
            deadline = started + args.budget
            last_report = 0
            while time.time() < deadline:
                time.sleep(0.25)
                with lock:
                    n = len(frames_in)
                if n and n // 150 > last_report:
                    last_report = n // 150
                    print(f'  {n} frames ({time.time() - started:.0f}s elapsed)')
                if js('!!window.__filmTimings'):
                    break
            film_started = js('window.__filmStartedAt || 0') or 0
            camera_json = js('JSON.stringify(window.__filmCamera || [])') or '[]'
            # The pointer is not in these frames — only its keyframes are, and
            # compose.py draws the curve between them at the output rate.
            cursor_json = js('JSON.stringify(window.__filmCursor || [])') or '[]'
            misses_json = js('JSON.stringify(window.__filmMisses || [])') or '[]'
            timings_json = js('JSON.stringify(window.__filmTimings || null)')
            mint_json = js('JSON.stringify(window.__filmMint || null)')
            call('Page.stopScreencast')
            time.sleep(0.4)
            with lock:
                grabbed = list(frames_in)
            if not grabbed:
                sys.exit('the screencast produced no frames; try --legacy-capture')
            # Output time zero is the moment the film started, not the moment
            # the screencast did. The gap between them is the js() round trip
            # plus the fire, and it shifted every subtitle by that much.
            base = film_started if film_started else grabbed[0][0]
            stamps = [ts - base for ts, _ in grabbed]
            gaps = sorted(b - a for a, b in zip(stamps, stamps[1:]))
            if gaps:
                mid = gaps[len(gaps) // 2]
                p90 = gaps[int(len(gaps) * 0.9)]
                busiest = sum(1 for g in gaps if g <= 1 / 24)
                print(f'  frame gaps · median {mid * 1000:.0f}ms · p90 {p90 * 1000:.0f}ms'
                      f' · {busiest} of {len(gaps)} at 24fps or better')
            frames = tempfile.mkdtemp(prefix='warrant-film-')
            print(f'capturing into {frames}')
            keep_from = max(0, sum(1 for s in stamps if s < 0) - 1)
            grabbed = grabbed[keep_from:]
            stamps = [max(0.0, s) for s in stamps[keep_from:]]
            for i, (_, data) in enumerate(grabbed):
                open(os.path.join(frames, f'{i:05d}.jpg'), 'wb').write(base64.b64decode(data))
            n = len(grabbed)
            dur = stamps[-1] if stamps else 0
        else:
            fire('void window.__film()')
            frames = tempfile.mkdtemp(prefix='warrant-film-')
            print(f'capturing into {frames}')
            n, started, stamps = 0, time.time(), []
            deadline = started + args.budget
            while time.time() < deadline:
                shot = call('Page.captureScreenshot', {'format': 'jpeg', 'quality': 88})
                data = shot.get('result', {}).get('data')
                if data:
                    open(os.path.join(frames, f'{n:05d}.jpg'), 'wb').write(base64.b64decode(data))
                    stamps.append(time.time() - started)
                    n += 1
                if n % 12 == 0 and js('!!window.__filmTimings'):
                    break
            dur = time.time() - started

        timings = js('JSON.stringify(window.__filmTimings || null)')
        if timings and timings != 'null':
            (os.path.dirname(os.path.abspath(__file__)) and None)
            open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'timings.json'), 'w').write(timings)
            print('beat timings written to film/timings.json')
        dur = time.time() - started
        # The film ends by reclassifying a field, which withdraws the tool and
        # relabels it `unregistered` — so looking for "minted by you" at the end
        # said the mint never happened when it plainly had. Ask whether a tool
        # exists at all, which is what the shot was for.
        # The shot list reads getTools() either side of the approval and leaves
        # the pair here, so the take is checked against the browser's own tool
        # list rather than against a name. It used to match /high_\\w+/, which
        # broke the moment a real agent named the tool something else — and the
        # film ends by withdrawing the tool anyway, so looking for it on screen
        # said the mint never happened when it plainly had.
        # Read while the socket was known good, above, for the flat path; the
        # legacy path still asks here.
        # A control the film reached for and did not find is a beat that
        # narrated something the picture never showed. Report it: a take with
        # a miss in it is not a take.
        misses = json.loads(misses_json or '[]') if 'misses_json' in locals() else json.loads(
            js('JSON.stringify(window.__filmMisses || [])') or '[]')
        if misses:
            print('  controls the film could not find: ' + ', '.join(misses))
        mint = locals().get('mint_json') or js('JSON.stringify(window.__filmMint || null)')
        pair = json.loads(mint) if mint and mint != 'null' else None
        minted = bool(pair and pair.get('after', 0) > pair.get('before', 0))
        shown = f"{pair['before']} \u2192 {pair['after']}" if pair else 'not recorded'
        print(f'{n} frames in {dur:.1f}s · tool surface on camera: {shown}')
        if not minted:
            print('  the mint did not happen; the film is of a flow that did not run')
        # Reduced motion is what turns the page's own animation into cuts. The
        # landing page autoplays two clips; without it they run at 30fps under
        # a capture that manages a fraction of that, and that is the stutter.
        if js('matchMedia("(prefers-reduced-motion: reduce)").matches') is not True:
            print('  reduced motion is NOT on: the page will animate itself and stutter')
        if n < 30:
            sys.exit('too few frames captured')

        if args.flat:
            # Hand the frames and the camera track to compose.py rather than
            # encoding here: the output frame rate is decided there, not by how
            # fast the capture happened to run.
            keep = os.path.abspath(args.flat_dir or 'film/.flat')
            shutil.rmtree(keep, ignore_errors=True)
            os.makedirs(keep, exist_ok=True)
            for name in sorted(os.listdir(frames)):
                if name.endswith('.jpg'):
                    shutil.copy(os.path.join(frames, name), os.path.join(keep, name))
            open(os.path.join(keep, 'stamps.json'), 'w').write(json.dumps(stamps))
            if timings_json and timings_json != 'null':
                open(os.path.join(keep, 'timings.json'), 'w').write(timings_json)
            open(os.path.join(keep, 'track.json'), 'w').write(camera_json)
            open(os.path.join(keep, 'cursor.json'), 'w').write(cursor_json)
            marks = len(json.loads(camera_json))
            keys = len(json.loads(cursor_json))
            print(f'flat capture kept in {keep} · {n} frames · {marks} camera marks '
                  f'· {keys} pointer keyframes')
            if keys == 0:
                print('  the pointer wrote nothing; the film would have no cursor at all')
            print(f'  next: python3 film/compose.py --frames {keep} '
                  f'--track {keep}/track.json --cursor {keep}/cursor.json --out {args.out}')
            return

        # Every frame keeps the length it was actually on screen for, so the
        # motion plays back at the speed it was captured at.
        listing = os.path.join(frames, 'frames.txt')
        with open(listing, 'w') as fh:
            for i, t in enumerate(stamps):
                nxt = stamps[i + 1] if i + 1 < len(stamps) else t + 1.0 / args.fps
                fh.write(f"file '{i:05d}.jpg'\nduration {max(nxt - t, 0.001):.4f}\n")
            fh.write(f"file '{len(stamps) - 1:05d}.jpg'\n")

        # Capture cannot exceed about sixteen frames a second, which is not
        # enough to describe a camera move. Motion interpolation invents the
        # frames in between; on a pan over static text it holds up well.
        vf = f'scale=trunc(iw/2)*2:trunc(ih/2)*2,fps={args.fps}'
        if args.interpolate:
            vf = (f'scale=trunc(iw/2)*2:trunc(ih/2)*2,'
                  f'minterpolate=fps={args.interpolate}:mi_mode=mci:mc_mode=aobmc:'
                  f'me_mode=bidir:vsbmc=1')
            print(f'interpolating to {args.interpolate} fps — this takes several minutes')
        subprocess.run([
            'ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', listing,
            '-vf', vf,
            '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium',
            '-movflags', '+faststart', args.out,
        ], check=True, cwd=frames)
        print('wrote', args.out)
        if not args.keep_frames:
            shutil.rmtree(frames, ignore_errors=True)
    finally:
        try:
            proc.send_signal(signal.SIGTERM)
            proc.wait(timeout=8)
        except Exception:
            proc.kill()
        shutil.rmtree(profile, ignore_errors=True)


if __name__ == '__main__':
    main()
