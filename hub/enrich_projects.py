#!/usr/bin/env python3
"""Fetch each collected project's full write-up and parse it into structure.

A tagline is ~100 characters. That is enough to shortlist and nowhere near
enough to reason about an idea, so this fetches the project page itself — the
2,000-to-8,000-word body, its section headings, the stack, the links and the
team — and saves the raw HTML alongside.

Saving the HTML also fills a documented hole: `verify/parse_pages.py` reads
`data/pages/*.html` and, before this script existed, nothing in the repository
wrote that directory.

    python3 hub/enrich_projects.py --in data/projects.jsonl --out data/projects_full.jsonl

Four workers, because Devpost's WAF rate-limits per route and project pages sat
comfortably at four in the run this comes from. Resumable: anything already in
the output is skipped, and a page already on disk is parsed without refetching.
"""
import argparse
import json
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from lib.fetch import Challenged, get                                # noqa: E402
from verify.parse_pages import parse                                 # noqa: E402

LOCK = threading.Lock()


def fetch_one(row, pages_dir, refetch=False):
    slug = row.get('slug')
    if not slug:
        return None
    path = pages_dir / f'{slug}.html'
    if refetch or not path.exists():
        try:
            r = get(row['url'])
        except Challenged as exc:
            return {'slug': slug, 'error': f'challenged: {exc}'}
        except Exception as exc:                                     # noqa: BLE001
            return {'slug': slug, 'error': str(exc)}
        if not r['html']:
            return {'slug': slug, 'error': f'status {r["status"]}'}
        path.write_text(r['html'], encoding='utf-8')
    try:
        parsed = parse(path)
    except Exception as exc:                                         # noqa: BLE001
        return {'slug': slug, 'error': f'parse: {exc}'}
    # carry the gallery facts the page itself does not state
    parsed.update({
        'is_winner': row.get('is_winner'),
        'hackathon_host': row.get('hackathon_host'),
        'hackathon_title': row.get('hackathon_title'),
        'organization_name': row.get('organization_name'),
        'software_id': row.get('software_id'),
        'error': None,
    })
    return parsed


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--in', dest='inp', default='data/projects.jsonl')
    ap.add_argument('--out', default='data/projects_full.jsonl')
    ap.add_argument('--pages-dir', default='data/pages')
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--refetch', action='store_true')
    a = ap.parse_args()

    pages = Path(a.pages_dir)
    pages.mkdir(parents=True, exist_ok=True)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    done = set()
    if out.exists():
        for line in out.read_text(encoding='utf-8').splitlines():
            if line.strip():
                r = json.loads(line)
                if not r.get('error'):
                    done.add(r.get('slug'))

    rows, seen = [], set()
    for line in Path(a.inp).read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if r['slug'] in seen or r['slug'] in done:
            continue
        seen.add(r['slug'])
        rows.append(r)
    if a.limit:
        rows = rows[:a.limit]
    print(f'{len(rows)} to fetch ({len(done)} already done)', file=sys.stderr)

    fh = out.open('a', encoding='utf-8')
    ok = err = 0
    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        for i, res in enumerate(pool.map(lambda r: fetch_one(r, pages, a.refetch), rows), 1):
            if res is None:
                continue
            with LOCK:
                fh.write(json.dumps(res, ensure_ascii=False) + '\n')
                fh.flush()
            if res.get('error'):
                err += 1
            else:
                ok += 1
            if i % 50 == 0:
                print(f'{i}/{len(rows)}  ok={ok} err={err}', flush=True)
    fh.close()
    print(f'\n{ok} parsed, {err} failed -> {out}')
    if err:
        print('Failures are unresolved rows, not absences. Re-run to retry them.',
              file=sys.stderr)


if __name__ == '__main__':
    main()
