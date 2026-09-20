#!/usr/bin/env python3
"""Decompose each write-up into the facets an idea is actually made of.

An idea is not one thing. It is a *mechanism* applied to a *substrate* on behalf
of a *user* inside a *domain* — and this project's own field work found that
single facets are always more crowded than they look while the combinations are
what stay rare. So the graph is built on facets, and the ideation that runs on
top of it looks for combinations nobody occupies.

    python3 hub/extract.py --in data/projects_full.jsonl --out data/facets.jsonl

Two honesties this carries, both inherited from `PITFALLS.md`:

* **The taxonomy is my vocabulary, not the field's.** A regex that only matches
  the phrasing I happened to think of measures me. Every count is reported at two
  strengths — `strong` (named in the title/tagline, or hit repeatedly in the body)
  and `weak` (hit at all) — so a claim can be stated as a band.
* **A facet that matches nothing may mean the idea is absent, or the pattern is.**
  Widen `hub/taxonomy.json` until it hurts before concluding a lane is empty.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STRONG_BODY_HITS = 2


def load_taxonomy(path):
    raw = json.loads(Path(path).read_text(encoding='utf-8'))
    return {facet: {k: re.compile(v, re.I) for k, v in groups.items()}
            for facet, groups in raw.items() if not facet.startswith('_')}


def blob(row):
    head = ' '.join(str(row.get(k) or '') for k in ('title', 'tagline'))
    body = ' '.join([
        str(row.get('description') or ''),
        ' '.join(str(v) for v in (row.get('sections') or {}).values()),
        ' '.join(row.get('built_with') or []),
    ])
    return head, body


def facets_of(row, taxonomy):
    head, body = blob(row)
    out = {}
    for facet, patterns in taxonomy.items():
        hits = {}
        for name, rx in patterns.items():
            in_head = len(rx.findall(head))
            in_body = len(rx.findall(body))
            if not (in_head or in_body):
                continue
            hits[name] = {
                'head': in_head,
                'body': in_body,
                'strong': bool(in_head) or in_body >= STRONG_BODY_HITS,
            }
        out[facet] = hits
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--in', dest='inp', default='data/projects_full.jsonl')
    ap.add_argument('--out', default='data/facets.jsonl')
    ap.add_argument('--taxonomy', default=str(ROOT / 'hub' / 'taxonomy.json'))
    ap.add_argument('--min-words', type=int, default=60,
                    help='skip stubs; a 20-word page has no idea in it to extract')
    a = ap.parse_args()

    taxonomy = load_taxonomy(a.taxonomy)
    rows = [json.loads(l) for l in Path(a.inp).read_text(encoding='utf-8').splitlines() if l.strip()]
    kept, skipped, blank = [], 0, 0
    for r in rows:
        if r.get('error'):
            skipped += 1
            continue
        if (r.get('description_words') or 0) < a.min_words:
            skipped += 1
            continue
        f = facets_of(r, taxonomy)
        if not any(f.values()):
            blank += 1
        kept.append({
            'slug': r['slug'], 'url': r.get('url'), 'title': r.get('title'),
            'tagline': r.get('tagline'), 'words': r.get('description_words'),
            'hackathon_title': r.get('hackathon_title'),
            'organization_name': r.get('organization_name'),
            'is_winner': r.get('is_winner'),
            'built_with': r.get('built_with') or [],
            'team_size': r.get('team_size'),
            'sections': list((r.get('sections') or {}).keys()),
            'repo': bool(r.get('repo_urls')), 'live': bool(r.get('live_urls')),
            'video': bool(r.get('video_urls') or r.get('youtube_embed_ids')),
            'facets': f,
        })

    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    with Path(a.out).open('w', encoding='utf-8') as fh:
        for r in kept:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')

    print(f'{len(kept)} projects faceted, {skipped} skipped (error or stub) -> {a.out}')
    if blank:
        pct = blank / max(len(kept), 1) * 100
        print(f'{blank} ({pct:.1f}%) matched no facet at all. If that share is large the '
              f'taxonomy is too narrow, not the field empty.')
    for facet in taxonomy:
        counts = {}
        for r in kept:
            for name, h in r['facets'][facet].items():
                c = counts.setdefault(name, [0, 0])
                c[1] += 1
                if h['strong']:
                    c[0] += 1
        top = sorted(counts.items(), key=lambda kv: -kv[1][1])[:6]
        shown = ', '.join(f'{k} {v[0]}/{v[1]}' for k, v in top)
        print(f'  {facet:<10} (strong/weak)  {shown}')


if __name__ == '__main__':
    main()
