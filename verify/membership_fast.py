#!/usr/bin/env python3
"""Fetch Devpost project pages via CDP; record hackathon membership + signals."""
import json, os, re, sys, time
import websocket

WS, SLUGFILE, OUT, DUMPDIR = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
SHARD, NSHARD = int(sys.argv[5]), int(sys.argv[6])
DELAY = float(sys.argv[7]) if len(sys.argv) > 7 else 0.0
os.makedirs(DUMPDIR, exist_ok=True)

slugs = [l.strip() for l in open(SLUGFILE) if l.strip()]
slugs = [s for i, s in enumerate(slugs) if i % NSHARD == SHARD]

done = set()
if os.path.exists(OUT):
    for l in open(OUT):
        try: done.add(json.loads(l)['slug'])
        except Exception: pass

class Conn:
    def __init__(self, u):
        self.u = u; self.rid = 0; self.connect()
    def connect(self):
        self.ws = websocket.create_connection(self.u, timeout=120, suppress_origin=True)
        self.call('Page.enable', {})
        self.call('Network.enable', {})
        self.call('Network.setBlockedURLs', {'urls': ['*.jpg','*.jpeg','*.png','*.gif','*.webp','*.svg','*.ico','*.woff','*.woff2','*.ttf','*.eot','*.mp4','*.css','*googletagmanager*','*google-analytics*','*doubleclick*','*newrelic*','*nr-data*','*facebook*','*fonts.g*','*/photos/*','*sentry*','*hotjar*','*intercom*','*.gif*']})
    def call(self, m, p):
        self.rid += 1; r = self.rid
        self.ws.send(json.dumps({'id': r, 'method': m, 'params': p}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get('id') == r: return msg

c = Conn(WS)
out = open(OUT, 'a')
EXPR = ('(function(){var s=document.getElementById("submissions");'
        'return JSON.stringify({rs:document.readyState,'
        'sub:s?s.innerHTML:"",'
        'title:(document.querySelector("#app-title")||{}).textContent||document.title,'
        'tag:(document.querySelector("#software-header .large-4 p, .software-tagline, #app-details-left p.large-copy")||{}).textContent||"",'
        'links:Array.from(document.querySelectorAll(".app-links a")).map(a=>a.href),'
        'txt:(document.getElementById("app-details-left")||document.body).innerText,'
        'gal:document.getElementById("gallery")?document.getElementById("gallery").innerHTML.slice(0,4000):"",'
        'built:Array.from(document.querySelectorAll("#built-with li")).map(a=>a.textContent.trim()),'
        'html:document.documentElement.outerHTML.length,f403:document.title.indexOf("403")>=0})})()')

for n, slug in enumerate(slugs):
    if slug in done: continue
    url = f'https://devpost.com/software/{slug}'
    d = None
    for attempt in range(4):
        try:
            c.call('Page.navigate', {'url': url})
            for _ in range(16):
                time.sleep(0.6)
                r = c.call('Runtime.evaluate', {'expression': EXPR, 'returnByValue': True})
                v = r.get('result', {}).get('result', {}).get('value')
                if not v: continue
                d = json.loads(v)
                if d.get('f403'):
                    print('403 backoff', flush=True); time.sleep(240); d=None; break
                if d['rs'] == 'complete' and d['html'] > 25000:
                    break
                d = None
            if d: break
            if d is None: pass
        except Exception as e:
            print('err', slug, e, flush=True)
            try: c.ws.close()
            except Exception: pass
            time.sleep(3); c.connect()
    if not d:
        out.write(json.dumps({'slug': slug, 'ok': False}) + '\n'); out.flush(); continue
    sub = d['sub']
    hacks = re.findall(r'href="https?://([a-z0-9-]+)\.devpost\.com/?"', sub)
    names = re.findall(r'<a href="https?://[a-z0-9-]+\.devpost\.com/?">([^<]+)</a>', sub)
    txt = d['txt'] or ''
    rec = {'slug': slug, 'ok': True,
           'webmcp': 'webmcp' in hacks,
           'marker': 'The WebMCP Challenge' in sub and 'webmcp.devpost.com' in sub,
           'hacks': sorted(set(hacks)), 'hack_names': [x.strip() for x in names],
           'title': (d['title'] or '').strip(), 'tagline': (d['tag'] or '').strip(),
           'links': d['links'], 'built': d['built'],
           'desc_len': len(txt),
           'video': bool(re.search(r'youtube|vimeo|youtu\.be', d['gal'] or '', re.I))}
    open(os.path.join(DUMPDIR, slug + '.txt'), 'w').write(txt)
    out.write(json.dumps(rec) + '\n'); out.flush()
    time.sleep(DELAY)
    if n % 20 == 0:
        print(f'[{SHARD}] {n}/{len(slugs)} {slug} webmcp={rec["webmcp"]}', flush=True)
print(f'[{SHARD}] done', flush=True)
