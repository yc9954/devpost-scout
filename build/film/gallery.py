#!/usr/bin/env python3
"""Shoot the Devpost image gallery.

Devpost wants 3:2 images, up to fifteen, under 5 MB each. This drives the same
private headless Chrome the recorder uses — never the browser you are using —
walks the product through the mint flow, and captures one frame per stop.

  python3 film/gallery.py --url http://localhost:5173

Output: film/gallery/01-....png ... , sized 1800x1200.
"""
import argparse, base64, json, os, pathlib, sys, time, urllib.request
import websocket

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from record import find_chrome, free_port, launch

WIDTH, HEIGHT = 1800, 1200          # 3:2 exactly, at a size Devpost renders crisply


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--url', default='http://localhost:5173')
    ap.add_argument('--out', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gallery'))
    args = ap.parse_args()

    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    proc, _profile = launch(find_chrome(), (port := free_port()), WIDTH, HEIGHT, 1)
    try:
        tabs = None
        for _ in range(80):
            try:
                tabs = json.load(urllib.request.urlopen(f'http://127.0.0.1:{port}/json'))
                break
            except Exception:
                time.sleep(0.25)
        if not tabs:
            sys.exit('chrome never came up')
        ws = websocket.create_connection(
            [t for t in tabs if t['type'] == 'page'][0]['webSocketDebuggerUrl'],
            timeout=60, suppress_origin=True)

        seq = [0]

        def call(method, params=None):
            seq[0] += 1
            ws.send(json.dumps({'id': seq[0], 'method': method, 'params': params or {}}))
            while True:
                msg = json.loads(ws.recv())
                if msg.get('id') == seq[0]:
                    return msg.get('result', {})

        call('Runtime.enable')
        # --window-size is the window, not the viewport: the shots came out 1800x1057

        # while every caption and this file's own docstring said 1800x1200, exactly

        # 3:2. Pinning the metrics makes the claim true rather than aspirational.

        call('Emulation.setDeviceMetricsOverride',

             {'width': WIDTH, 'height': HEIGHT, 'deviceScaleFactor': 1, 'mobile': False})

        call('Page.enable')

        def js(expr):
            r = call('Runtime.evaluate', {'expression': expr, 'returnByValue': True, 'awaitPromise': True})
            return r.get('result', {}).get('value')

        def goto(path, fresh=False):
            call('Page.navigate', {'url': args.url.rstrip('/') + path})
            time.sleep(2.0)
            if fresh:
                # Tools persist per site, so a second run through the flow would
                # otherwise inherit the first one's tool.
                js('try { localStorage.clear(); } catch {}')
                call('Page.navigate', {'url': args.url.rstrip('/') + path})
                time.sleep(2.0)
            time.sleep(1.5)

        counter = [0]


        def shot(name):
            data = call('Page.captureScreenshot', {'format': 'png'})['data']
            got = call('Runtime.evaluate', {
                'expression': '[innerWidth, innerHeight].join("x")',
                'returnByValue': True})['result']['value']
            if got != f'{WIDTH}x{HEIGHT}':
                sys.exit(f'viewport is {got}, not {WIDTH}x{HEIGHT}; the captions say 3:2')
            counter[0] += 1
            path = out / f'{counter[0]:02d}-{name}.png'
            path.write_bytes(base64.b64decode(data))
            print(f'  {path.name}')

        def button(text):
            return f"""[...document.querySelectorAll('button')].find(b =>
                b.textContent.replace(/\\s+/g,' ').trim().toLowerCase()
                 .includes({json.dumps(text.lower())}))"""

        def click(text, wait=1.6):
            # Wait for the control to become enabled: the flow reveals each step
            # only once the previous one has actually produced something.
            for _ in range(30):
                state = js(f'(() => {{ const b = {button(text)}; return !b ? "missing" : b.disabled ? "disabled" : "ready"; }})()')
                if state == 'ready':
                    break
                time.sleep(0.4)
            else:
                sys.exit(f'"{text}" never became clickable ({state})')
            js(f'(() => {{ const b = {button(text)}; b.scrollIntoView({{block: "center"}}); b.click(); }})()')
            time.sleep(wait)

        def scroll(px):
            js(f'window.scrollTo({{top: {px}, behavior: "instant"}})')
            time.sleep(0.8)

        def frame(match, block='center'):
            """Put the region whose heading or data-film marker matches in shot."""
            js(f"""(() => {{ const want = {json.dumps(match)}.split('|');
                  const el = [...document.querySelectorAll('h2, h3, [data-film], p, div')]
                  .find(n => want.some(m => n.getAttribute?.('data-film') === m
                        || (n.children.length < 4 && n.textContent.toLowerCase().trim().startsWith(m))));
                  el?.scrollIntoView({{block: {json.dumps(block)}}}); }})()""")
            time.sleep(0.8)

        # A re-run replaces the gallery rather than adding to it. Numbering
        # from len(glob) meant the second run wrote 17-32 beside a stale 1-16,
        # and the caption list in docs/submission-form.md then described neither.
        for stale in sorted(out.glob('*.png')):
            stale.unlink()
        print('gallery →', out, '(cleared)')

        # 1-3 · the landing page: the claim, how a tool gets there, and the
        #       evidence for the claim. Framed by anchor rather than by pixel
        #       offset, so a layout change moves the shot instead of missing it.
        goto('/')
        shot('the-claim-and-its-proof')
        frame('how that report becomes a tool|they do the work once', 'start')
        shot('how-a-tool-gets-here')
        js("document.querySelector('#evidence')?.scrollIntoView({block:'start',behavior:'instant'})")
        time.sleep(0.8)
        shot('the-evidence-on-the-page')

        # 4 · the workbench as it ships: seven tools, a page full of controls.
        goto('/studio', fresh=True)
        shot('studio-seven-tools')

        # 5 · the demonstration being recorded as operations, not clicks.
        click('Record a demonstration')
        for index, value in ((0, '2026-08'), (4, '40')):
            js(f"""(() => {{ const s = document.querySelectorAll('select')[{index}];
                if (!s) return; const set = Object.getOwnPropertyDescriptor(
                  window.HTMLSelectElement.prototype, 'value').set;
                set.call(s, {json.dumps(value)});
                s.dispatchEvent(new Event('change', {{bubbles: true}})); }})()""")
            time.sleep(0.7)
        shot('demonstration-recorded')

        # 6-8 · the proposal, its reasoning, and the schema it generated.
        #       Replay the call a real agent made, the way the film does, so the
        #       gallery shows the page validating an agent's proposal rather
        #       than its own draft. Falls back to the draft when the fixture is
        #       not there, which is what a clone without a run will see.
        replayed = js("""(async () => {
            try {
              const res = await fetch('/agent-proposal.json', {cache: 'no-store'});
              if (!res.ok) return false;
              const saved = await res.json();
              if (!saved || !saved.call) return false;
              const mc = document.modelContext;
              if (!mc || !mc.getTools || !mc.executeTool) return false;
              const tool = (await mc.getTools()).find(t => t.name === 'propose_tool');
              if (!tool) return false;
              await mc.executeTool(tool, JSON.stringify(saved.call));
              return true;
            } catch (e) { return false; }
          })()""")
        if replayed:
            print('  proposal replayed from a real agent run')
            time.sleep(2.5)
        else:
            click('Draft it here instead', 4.0)
        frame('step-2|propose')
        shot('proposal')
        frame('reasoning')
        shot('reasoning-and-schema')

        # 9 · edge cases, generated and already executed against real rows.
        frame('edges|edge cases · run against real data', 'start')
        shot('edge-cases-executed')

        # 10 · every case reviewed by a person, approval now possible.
        count = js("[...document.querySelectorAll('button')].filter(b => b.textContent.trim() === 'accept').length") or 0
        for i in range(count):
            js(f"[...document.querySelectorAll('button')].filter(b => b.textContent.trim() === 'accept')[{i}]?.click()")
            time.sleep(0.3)
        shot('reviewed-and-approvable')

        # 11-12 · minting, and the tool surface with the eighth tool on it.
        click('Approve & register', 2.5)
        frame('tool-card|surface')
        shot('minted')
        scroll(0)
        shot('tool-surface-eight')

        # 12-13 · the whole point: it answers for a period nobody demonstrated.
        click('the one before', 2.2)
        frame('tool-card|published', 'start')
        shot('answers-an-undemonstrated-period')
        click('Ask it', 1.8)
        frame('what it will not do', 'center')
        shot('what-it-will-not-do')

        # 12-13 · the same flow, but the person mints a tool that acts. Shot
        # from a clean surface so the earlier tool does not confuse the frame.
        goto('/studio', fresh=True)
        click('Record a demonstration')
        for index, value in ((0, '2026-08'), (4, '40')):
            js(f"""(() => {{ const s = document.querySelectorAll('select')[{index}];
                const set = Object.getOwnPropertyDescriptor(window.HTMLSelectElement.prototype, 'value').set;
                set.call(s, {json.dumps(value)}); s.dispatchEvent(new Event('change', {{bubbles: true}})); }})()""")
            time.sleep(0.6)
        click('Draft it here instead', 4.0)
        click('and act on the answer', 1.6)
        frame('what the tool may do', 'center')
        shot('a-tool-that-acts')
        count = js("[...document.querySelectorAll('button')].filter(b => b.textContent.trim() === 'accept').length") or 0
        for i in range(count):
            js(f"[...document.querySelectorAll('button')].filter(b => b.textContent.trim() === 'accept')[{i}]?.click()")
            time.sleep(0.3)
        click('Approve & register', 2.5)
        # Call it the way an agent would, and let it stop for a person on camera.
        js("""(async () => {
            const t = (await document.modelContext.getTools()).find(t => /overtime/.test(t.name));
            window.__pending = document.modelContext.executeTool(t, JSON.stringify({ month: '2026-07' }));
        })()""")
        time.sleep(2.5)
        frame('waiting for you|confirm', 'center')
        shot('the-write-stops-for-a-person')
        js("[...document.querySelectorAll('button')].find(b => /decline|cancel/i.test(b.textContent))?.click()")
        time.sleep(1.2)

        # 14-15 · the page moves; the tool that no longer matches is withdrawn.
        scroll(0)
        click('restrict department', 2.5)
        shot('page-reclassified-a-field')
        frame('tool surface|published', 'start')
        shot('tool-withdrawn-until-reapproved')

        print(f'\n{len(list(out.glob("*.png")))} images · 3:2 · {WIDTH}x{HEIGHT}')
    finally:
        proc.terminate()


if __name__ == '__main__':
    main()
