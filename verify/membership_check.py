#!/usr/bin/env python3
"""Decide whether a project was actually submitted to THIS hackathon.

The loose test — the marker text appearing anywhere on the page — has false
positives: a write-up that merely names the hackathon, a "built with" blurb, a
comment. The strict test reads Devpost's own `#submissions` block, which is
where it renders "Submitted to <hackathon>", and looks for a link to the
hackathon host inside it.

On a 25-entry random sample of the WebMCP run the two agreed 25/25, so loose is
usually fine — but strict is what you quote when someone asks whether you
over-counted, and it costs nothing extra.

    python3 verify/membership_check.py --config config.json --in slugs.json --out confirmed.json
"""
import argparse
import concurrent.futures
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.fetch import Challenged, get                                # noqa: E402

BLOCK = re.compile(r'<div[^>]+id=["\']submissions["\'].*?</div>\s*</div>', re.S | re.I)
TITLE = re.compile(r'<title[^>]*>\s*(.*?)\s*</title>', re.I | re.S)


def check(url, host, marker):
    try:
        r = get(url)
    except Challenged as e:
        return {'url': url, 'status': 'challenged', 'error': str(e)}
    if not r['html']:
        return {'url': url, 'status': r['status'], 'submitted': False}
    html = r['html']
    m = BLOCK.search(html)
    block = m.group(0) if m else ''
    flat = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html))
    t = TITLE.search(html)
    return {
        'url': url,
        'status': r['status'],
        'title': t.group(1).strip() if t else '',
        'submitted': host in block,                                   # strict
        'submitted_loose': bool(re.search(
            rf'Submitted to\s*{re.escape(marker)}', flat, re.I)),
        'block_len': len(block),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='config.json')
    ap.add_argument('--in', dest='inp', required=True,
                    help='JSON list of slugs or project URLs')
    ap.add_argument('--out', required=True)
    ap.add_argument('--workers', type=int, default=4,
                    help='4 is safe; 6+ earned a ~40 minute WAF block')
    a = ap.parse_args()
    cfg = json.load(open(a.config))
    host, marker = cfg['hackathon_host'], cfg['membership_marker']

    items = json.load(open(a.inp))
    urls = [i if str(i).startswith('http') else f'https://devpost.com/software/{i}'
            for i in (items if isinstance(items, list) else items['slugs'])]

    out, done = [], 0
    with concurrent.futures.ThreadPoolExecutor(a.workers) as ex:
        for r in ex.map(lambda u: check(u, host, marker), urls):
            out.append(r)
            done += 1
            if done % 50 == 0:
                Path(a.out).write_text(json.dumps(out, ensure_ascii=False))
                ch = sum(1 for x in out if x.get('status') == 'challenged')
                print(f'{done}/{len(urls)}  confirmed={sum(1 for x in out if x.get("submitted"))}'
                      f'  challenged={ch}', flush=True)
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False))
    ch = [x for x in out if x.get('status') == 'challenged']
    print(f'\nchecked {len(out)}  confirmed {sum(1 for x in out if x.get("submitted"))}'
          f'  loose-only {sum(1 for x in out if x.get("submitted_loose") and not x.get("submitted"))}')
    if ch:
        print(f'!! {len(ch)} were never resolved (WAF). Re-run those before quoting a total.')


if __name__ == '__main__':
    main()
