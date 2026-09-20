#!/usr/bin/env python3
"""Collect a hackathon's project gallery: every idea, and which ones won.

The gallery answers plain HTTP — no browser needed, unlike `/software/search` —
and renders 24 entries a page with the winners carrying a `class="winner"`
ribbon. That flag is the point: a corpus of *winners* across many hackathons is
a far better idea hub than a corpus of everything, because it is pre-filtered by
people who read the whole field.

    python3 hub/collect_gallery.py --host webmcp.devpost.com --out data/projects.jsonl
    python3 hub/collect_gallery.py --from-index data/hackathons.jsonl --winners-only \\
            --min-prize 10000 --out data/projects.jsonl

A gallery the managers never published returns "hasn't published this gallery
yet" and zero entries — that is a real state, not an error, and it is recorded
as `gallery_unpublished` rather than counted as a hackathon with no projects.
"""
import argparse
import html as html_lib
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.fetch import Challenged, get                                # noqa: E402

ENTRY_SPLIT = re.compile(r'data-software-id="(\d+)"')
HREF = re.compile(r'href="(https://devpost\.com/software/[^"]+)"')
TITLE = re.compile(r'<h5>\s*(.*?)\s*</h5>', re.S)
TAGLINE = re.compile(r'class="small tagline"[^>]*>\s*(.*?)\s*</p>', re.S)
WINNER = re.compile(r'class="winner"|alt="Winner"')
MEMBER = re.compile(r'class="user-profile-link"[^>]*data-url="https://devpost\.com/([^"]+)"')
COUNT = re.compile(r'class="[^"]*(like|comment)-count[^"]*"[^>]*>\s*(\d+)', re.I)
UNPUBLISHED = re.compile(r"haven'?t published", re.I)
TAG = re.compile(r'<[^>]+>')


def text(fragment):
    return re.sub(r'\s+', ' ', html_lib.unescape(TAG.sub(' ', fragment))).strip()


def parse_gallery(page_html):
    """-> (rows, unpublished)."""
    if UNPUBLISHED.search(page_html):
        return [], True
    marks = list(ENTRY_SPLIT.finditer(page_html))
    rows = []
    for i, mk in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(page_html)
        seg = page_html[mk.start():end]
        href = HREF.search(seg)
        if not href:
            continue
        title = TITLE.search(seg)
        tag = TAGLINE.search(seg)
        rows.append({
            'software_id': int(mk.group(1)),
            'url': href.group(1),
            'slug': href.group(1).rsplit('/', 1)[-1],
            'title': text(title.group(1)) if title else '',
            'tagline': text(tag.group(1)) if tag else '',
            'is_winner': bool(WINNER.search(seg)),
            'members': sorted(set(MEMBER.findall(seg))),
            'counts': {k.lower(): int(v) for k, v in COUNT.findall(seg)},
        })
    return rows, False


def collect(host, pause=0.5, max_pages=400, winners_only=False, early_stop=True):
    """Page a gallery.

    Devpost renders winners first: on every hackathon checked, page 1 carried all
    the ribbons and page 2 onward carried none. So in `winners_only` mode we stop
    after the first page that yields no winner, which turns a 400-page crawl of a
    128,000-registrant hackathon into two requests. Pass `early_stop=False` if you
    suspect a gallery orders differently — the cost is the full crawl.
    """
    base = f'https://{host.rstrip("/")}/project-gallery'
    seen, out, page = set(), [], 0
    while page < max_pages:
        page += 1
        url = base if page == 1 else f'{base}?page={page}'
        try:
            body = get(url)['html']
        except Challenged as exc:
            print(f'  {host} p{page}: {exc}; backing off', file=sys.stderr)
            time.sleep(15)
            page -= 1
            continue
        rows, unpublished = parse_gallery(body)
        if unpublished:
            return [], 'gallery_unpublished'
        fresh = [r for r in rows if r['software_id'] not in seen]
        if not fresh:                            # page returned nothing new: done
            break
        winners_here = 0
        for r in fresh:
            seen.add(r['software_id'])
            if r['is_winner']:
                winners_here += 1
            elif winners_only:
                continue
            r['hackathon_host'] = host
            r['gallery_page'] = page
            out.append(r)
        if winners_only and early_stop and winners_here == 0:
            return out, 'ok' if out else 'no_winners_on_first_page'
        time.sleep(pause)
    return out, 'ok'


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--host', help='one hackathon host')
    g.add_argument('--from-index', help='hackathons.jsonl from collect_hackathons.py')
    ap.add_argument('--out', required=True)
    ap.add_argument('--winners-only', action='store_true',
                    help='keep only ribboned entries — the high-signal idea corpus')
    ap.add_argument('--min-prize', type=float, default=0, help='filter the index by prize USD')
    ap.add_argument('--min-registrations', type=int, default=0)
    ap.add_argument('--limit', type=int, default=0, help='at most N hackathons from the index')
    ap.add_argument('--pause', type=float, default=0.5)
    ap.add_argument('--no-early-stop', action='store_true',
                    help='with --winners-only, crawl the whole gallery instead of stopping '
                         'at the first page with no ribbon')
    a = ap.parse_args()

    if a.host:
        targets = [{'host': a.host, 'title': a.host}]
    else:
        targets = []
        for line in Path(a.from_index).read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            if not r.get('winners_announced') and a.winners_only:
                continue
            prize = float(re.sub(r'[^\d.]', '', text(r.get('prize_amount') or '')) or 0)
            if prize < a.min_prize or (r.get('registrations_count') or 0) < a.min_registrations:
                continue
            host = re.sub(r'^https?://|/$', '', r.get('url') or '')
            if host:
                targets.append({'host': host, 'title': r.get('title'),
                                'org': r.get('organization_name'), 'prize': prize,
                                'registrations': r.get('registrations_count')})
        targets.sort(key=lambda t: -(t.get('prize') or 0))
        if a.limit:
            targets = targets[:a.limit]

    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if out.exists():
        for line in out.read_text(encoding='utf-8').splitlines():
            if line.strip():
                done.add(json.loads(line).get('hackathon_host'))
    fh = out.open('a', encoding='utf-8')
    kept = 0
    for i, t in enumerate(targets, 1):
        if t['host'] in done:
            continue
        rows, status = collect(t['host'], a.pause, winners_only=a.winners_only,
                               early_stop=not a.no_early_stop)
        for r in rows:
            r['hackathon_title'] = t.get('title')
            r['organization_name'] = t.get('org')
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
        fh.flush()
        kept += len(rows)
        print(f'[{i}/{len(targets)}] {t["host"]:<52} {status:<20} {len(rows):>4} rows  '
              f'(total {kept})', flush=True)
    fh.close()
    print(f'\n{kept} project rows from {len(targets)} hackathons -> {out}')


if __name__ == '__main__':
    main()
