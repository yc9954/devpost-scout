#!/usr/bin/env python3
"""Enumerate every hackathon Devpost lists, through its own keyless API.

`devpost.com/api/hackathons` answers plain HTTP with JSON, pages at 9 per page,
states its own `meta.total_count`, and has no pagination ceiling — page 1538 of
1538 returns rows and 1600 returns an empty list. That combination is unusual
and it is what makes a true census affordable here, unlike `/software/search`,
which needs a browser and capped this project's first corpus at a third of the
field.

    python3 hub/collect_hackathons.py --out data/hackathons.jsonl

Resumable: re-running skips pages already in the output. The run asserts its own
total against the API's stated `total_count` and refuses to report success while
they disagree, which is the one check the original search sweep did not do.
"""
import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.fetch import Challenged, get                                # noqa: E402

API = 'https://devpost.com/api/hackathons?page={}'


def load_done(path):
    """Pages already collected, and the ids seen, so a resume does not duplicate."""
    pages, ids = set(), set()
    if not path.exists():
        return pages, ids
    for line in path.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        pages.add(row.get('_page'))
        ids.add(row.get('id'))
    return pages, ids


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--out', default='data/hackathons.jsonl')
    ap.add_argument('--pause', type=float, default=0.6)
    ap.add_argument('--max-pages', type=int, default=2000)
    ap.add_argument('--start-page', type=int, default=1,
                    help='first page; lets several workers split the range')
    ap.add_argument('--end-page', type=int, default=0, help='last page, inclusive (0 = no limit)')
    ap.add_argument('--stop-after-empty', type=int, default=2,
                    help='consecutive empty pages that end the sweep')
    a = ap.parse_args()

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    done_pages, seen = load_done(out)
    if done_pages:
        print(f'resuming: {len(done_pages)} pages, {len(seen)} hackathons already recorded',
              file=sys.stderr)

    fh = out.open('a', encoding='utf-8')
    total_reported, empties, added = None, 0, 0
    page = a.start_page - 1
    limit = a.end_page or a.max_pages
    while page < limit:
        page += 1
        if page in done_pages:
            continue
        try:
            body = get(API.format(page))['html']
        except Challenged as exc:
            print(f'page {page}: {exc} — backing off', file=sys.stderr)
            time.sleep(20)
            page -= 1
            continue
        payload = json.loads(body)
        rows = payload.get('hackathons', [])
        total_reported = payload.get('meta', {}).get('total_count', total_reported)

        if not rows:
            empties += 1
            if empties >= a.stop_after_empty:
                print(f'two empty pages at {page}; stopping', file=sys.stderr)
                break
            continue
        empties = 0
        for r in rows:
            if r.get('id') in seen:
                continue
            seen.add(r['id'])
            r['_page'] = page
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
            added += 1
        fh.flush()
        if page % 25 == 0:
            print(f'page {page:>5}  collected {len(seen):>6} / {total_reported}', flush=True)
        time.sleep(a.pause)
    fh.close()

    print(f'\ncollected {len(seen)} hackathons up to page {page} (+{added} this run)')
    if total_reported and a.start_page == 1 and not a.end_page:
        gap = total_reported - len(seen)
        pct = gap / total_reported * 100
        print(f'API reports {total_reported}; difference {gap} ({pct:.1f}%)')
        if abs(pct) > 2:
            print('⚠  more than 2% from the stated total — do not quote this as a census '
                  'until you know why.', file=sys.stderr)
            sys.exit(1)
        print('✅ within 2% of the stated total')


if __name__ == '__main__':
    main()
