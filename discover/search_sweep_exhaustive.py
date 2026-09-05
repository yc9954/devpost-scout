#!/usr/bin/env python3
"""Resilient Devpost search sweep: backs off hard on 403, never gives up."""
import json, re, sys, time, urllib.parse
import websocket

WS, QUERY, PAGES, OUT = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
DELAY = float(sys.argv[5]) if len(sys.argv) > 5 else 2.0
MAXPAGE = int(sys.argv[6]) if len(sys.argv) > 6 else 200
ITEM = re.compile(r'data-software-id="(\d+)"[\s\S]{0,400}?link-to-software" href="https://devpost\.com/software/([A-Za-z0-9][A-Za-z0-9_-]*)"')
PAG  = re.compile(r'search\?page=(\d+)&amp;query=')
TOT  = re.compile(r'page-info">\s*<b>[^<]*</b>\s*of\s*<b>([\d,]+)</b>')

class Conn:
    def __init__(s, u): s.u=u; s.rid=0; s.connect()
    def connect(s):
        s.ws = websocket.create_connection(s.u, timeout=120, suppress_origin=True); s.call('Page.enable', {})
        s.call('Network.enable', {})
        s.call('Network.setBlockedURLs', {'urls': ['*.jpg','*.jpeg','*.png','*.gif','*.webp','*.svg','*.ico','*.woff','*.woff2','*.ttf','*.eot','*.mp4','*.css','*googletagmanager*','*google-analytics*','*doubleclick*','*newrelic*','*nr-data*','*facebook*','*fonts.g*','*/photos/*','*sentry*','*hotjar*','*intercom*','*.gif*']})

    def call(s, m, p):
        s.rid += 1; r = s.rid
        s.ws.send(json.dumps({'id': r, 'method': m, 'params': p}))
        while True:
            msg = json.loads(s.ws.recv())
            if msg.get('id') == r: return msg

c = Conn(WS)
q = urllib.parse.quote_plus(QUERY)
out = open(OUT, 'a')
pages = list(range(1, MAXPAGE + 1)) if PAGES == 'auto' else [int(x) for x in PAGES.split(',')]
i = 0
while i < len(pages):
    page = pages[i]
    url = f'https://devpost.com/software/search?page={page}&query={q}'
    html = ''
    blocked = False
    for attempt in range(3):
        try:
            c.call('Page.navigate', {'url': url})
            for _ in range(18):
                time.sleep(0.6)
                r = c.call('Runtime.evaluate', {'expression':
                    '(function(){return document.readyState+"|"+document.documentElement.outerHTML})()',
                    'returnByValue': True})
                v = r.get('result', {}).get('result', {}).get('value', '') or ''
                st, _, html = v.partition('|')
                if st == 'complete' and (len(html) > 40000 or '403 Forbidden' in html):
                    break
            if '403 Forbidden' in html or len(html) < 5000:
                blocked = True; break
            if len(html) > 20000: blocked = False; break
        except Exception as e:
            print('  err', page, e, flush=True)
            try: c.ws.close()
            except Exception: pass
            time.sleep(5); c.connect()
    if blocked:
        print(f'q={QUERY!r} page {page}: BLOCKED, sleeping 300s', flush=True)
        time.sleep(300); continue
    items = ITEM.findall(html)
    pg = [int(x) for x in PAG.findall(html)]
    last = max(pg) if pg else None
    out.write(json.dumps({'page': page, 'n': len(items), 'items': items, 'lastpage': last, 'query': QUERY, 'total': (TOT.search(html).group(1) if TOT.search(html) else None)}) + '\n'); out.flush()
    print(f'q={QUERY!r} page {page}: {len(items)} items, last={last}', flush=True)
    if PAGES == 'auto':
        if len(items) == 0: break
        if last and last < MAXPAGE: pages = list(range(1, last + 1))
    i += 1
    time.sleep(DELAY)
print('DONE', QUERY, flush=True)
