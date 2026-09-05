#!/usr/bin/env python3
"""Fetch Devpost listing pages through the open Chrome session.

devpost.com answers plain HTTP clients with a 202 challenge page, so the tag and
search listings can only be read from a real browser context.
"""
import json, re, sys, time
import websocket

WS = sys.argv[1]
URLS = sys.argv[2:]


def call(ws, method, params, rid):
    ws.send(json.dumps({'id': rid, 'method': method, 'params': params}))
    while True:
        msg = json.loads(ws.recv())
        if msg.get('id') == rid:
            return msg


def html_of(ws, url, rid):
    call(ws, 'Page.navigate', {'url': url}, rid)
    time.sleep(4.0)
    for _ in range(12):
        reply = call(ws, 'Runtime.evaluate',
                     {'expression': 'document.readyState + "|" + document.documentElement.outerHTML',
                      'returnByValue': True}, rid + 1000)
        value = reply.get('result', {}).get('result', {}).get('value', '')
        state, _, body = value.partition('|')
        if state == 'complete' and len(body) > 3000:
            return body
        time.sleep(1.5)
    return body


ws = websocket.create_connection(WS, timeout=60, suppress_origin=True)
call(ws, 'Page.enable', {}, 1)
out = {}
for i, url in enumerate(URLS):
    body = html_of(ws, url, 10 + i * 10)
    slugs = sorted(set(re.findall(r'devpost\.com/software/([A-Za-z0-9][A-Za-z0-9_-]*)', body)) - {'built-with', 'new', 'search'})
    info = re.findall(r'([\d,]+)\s+(?:projects?|results?)', body)
    out[url] = {'bytes': len(body), 'slugs': slugs, 'counts': info[:3]}
    print(url, '->', len(body), 'bytes,', len(slugs), 'slugs,', info[:3], flush=True)
json.dump(out, open('data/cdp_listing.json', 'w'))
