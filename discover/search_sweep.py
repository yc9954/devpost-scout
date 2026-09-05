#!/usr/bin/env python3
"""Page through Devpost's project search inside the browser session."""
import json, re, sys, time
import websocket

WS = sys.argv[1]
QUERY = sys.argv[2]
PAGES = int(sys.argv[3])
OUT = sys.argv[4]


def call(ws, method, params, rid):
    ws.send(json.dumps({'id': rid, 'method': method, 'params': params}))
    while True:
        msg = json.loads(ws.recv())
        if msg.get('id') == rid:
            return msg


ws = websocket.create_connection(WS, timeout=90, suppress_origin=True)
call(ws, 'Page.enable', {}, 1)
found, meta = {}, []
rid = 100
for page in range(1, PAGES + 1):
    url = f'https://devpost.com/software/search?page={page}&query={QUERY}'
    call(ws, 'Page.navigate', {'url': url}, rid); rid += 1
    body = ''
    for _ in range(14):
        time.sleep(1.2)
        r = call(ws, 'Runtime.evaluate', {'expression': 'document.readyState + "|" + document.documentElement.outerHTML', 'returnByValue': True}, rid); rid += 1
        v = r.get('result', {}).get('result', {}).get('value', '')
        state, _, body = v.partition('|')
        if state == 'complete' and len(body) > 20000:
            break
    slugs = set(re.findall(r'devpost\.com/software/([A-Za-z0-9][A-Za-z0-9_-]*)', body)) - {'built-with', 'new', 'search'}
    text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', body))
    hit = re.search(r'([\d,]+)\s+projects?\b', text)
    for s in slugs:
        found.setdefault(s, page)
    meta.append({'page': page, 'new': len(slugs), 'total_text': hit.group(0) if hit else None})
    print(f'page {page}: {len(slugs)} slugs, cumulative {len(found)}, header={hit.group(0) if hit else None}', flush=True)
    if not slugs:
        break
json.dump({'query': QUERY, 'slugs': sorted(found), 'meta': meta}, open(OUT, 'w'))
print('total unique slugs', len(found))
