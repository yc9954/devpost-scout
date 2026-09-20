#!/usr/bin/env python3
"""Write the faceted corpus out as an Obsidian vault — notes and [[wikilinks]].

One note per project, one per facet, one per hackathon. The links are the point:
in a graph view a mechanism note sits at the centre of every project that used
it, and the shape of what is *missing* around it becomes visible in a way a JSONL
file never makes visible.

    python3 hub/vault.py --in data/facets.jsonl --out vault/

Open `vault/` as an Obsidian vault. Start at `README.md`.
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

FACET_DIR = {'mechanism': 'mechanisms', 'domain': 'domains',
             'user': 'users', 'substrate': 'substrates'}


def safe(name):
    return re.sub(r'[^\w\-. ]+', '-', str(name or 'unknown')).strip()[:80] or 'unknown'


def front(d):
    lines = ['---']
    for k, v in d.items():
        if isinstance(v, list):
            lines.append(f'{k}:')
            lines.extend(f'  - "{str(x)}"' for x in v)
        elif isinstance(v, bool):
            lines.append(f'{k}: {str(v).lower()}')
        elif v is None or v == '':
            continue
        else:
            lines.append(f'{k}: "{str(v)}"' if isinstance(v, str) else f'{k}: {v}')
    lines.append('---')
    return '\n'.join(lines)


def strong_names(row, facet):
    return sorted(n for n, h in row['facets'].get(facet, {}).items() if h['strong'])


def all_names(row, facet):
    return sorted(row['facets'].get(facet, {}))


def write_projects(rows, out, body_by_slug):
    d = out / 'projects'
    d.mkdir(parents=True, exist_ok=True)
    for r in rows:
        links = {f: strong_names(r, f) for f in FACET_DIR}
        weak = {f: sorted(set(all_names(r, f)) - set(links[f])) for f in FACET_DIR}
        body = body_by_slug.get(r['slug'], {})
        fm = front({
            'slug': r['slug'], 'url': r['url'], 'title': r['title'],
            'hackathon': r.get('hackathon_title'), 'organization': r.get('organization_name'),
            'winner': bool(r.get('is_winner')), 'words': r.get('words'),
            'team_size': r.get('team_size'), 'has_repo': r.get('repo'),
            'has_live': r.get('live'), 'has_video': r.get('video'),
            'tags': ['project'] + [f'{f}/{n}' for f in FACET_DIR for n in links[f]],
        })
        parts = [fm, f"\n# {r['title']}\n", f"> {r.get('tagline') or ''}\n"]
        parts.append(f"[Devpost]({r['url']}) · hackathon [[{safe(r.get('hackathon_title'))}]]\n")
        parts.append('## Facets\n')
        for f, dirname in FACET_DIR.items():
            if links[f]:
                parts.append(f"**{f}** " + ' '.join(f'[[{n}]]' for n in links[f]))
            if weak[f]:
                parts.append(f"  <sub>weak: {', '.join(weak[f])}</sub>")
        if r.get('built_with'):
            parts.append(f"\n**stack** {', '.join(r['built_with'][:14])}")
        if r.get('sections'):
            parts.append('\n## How they structured the write-up\n')
            parts.extend(f'- {s}' for s in r['sections'][:20])
        if body.get('description'):
            parts.append('\n## Body\n')
            parts.append(body['description'][:12000])
        (d / f"{safe(r['slug'])}.md").write_text('\n'.join(parts), encoding='utf-8')
    return len(rows)


def write_facets(rows, out):
    """One note per facet, listing its projects and what it co-occurs with."""
    members = defaultdict(list)
    cooc = defaultdict(Counter)
    for r in rows:
        present = [(f, n) for f in FACET_DIR for n in strong_names(r, f)]
        for f, n in present:
            members[(f, n)].append(r)
        for i, a in enumerate(present):
            for b in present[i + 1:]:
                cooc[a][b] += 1
                cooc[b][a] += 1

    for (facet, name), projs in members.items():
        d = out / FACET_DIR[facet]
        d.mkdir(parents=True, exist_ok=True)
        winners = sum(1 for p in projs if p.get('is_winner'))
        partners = cooc[(facet, name)].most_common(12)
        fm = front({'facet': facet, 'name': name, 'projects': len(projs),
                    'winners': winners, 'tags': ['facet', facet]})
        parts = [fm, f'\n# {name}\n',
                 f'`{facet}` · **{len(projs)}** projects, **{winners}** of them winners.\n',
                 '## Pairs with\n']
        parts.extend(f'- [[{n}]] — {c} together  <sub>({f})</sub>' for (f, n), c in partners)
        parts.append('\n## Projects\n')
        for p in sorted(projs, key=lambda x: -(x.get('words') or 0))[:150]:
            star = '★ ' if p.get('is_winner') else ''
            parts.append(f"- {star}[[{safe(p['slug'])}]] — {(p.get('tagline') or '')[:100]}")
        (d / f'{safe(name)}.md').write_text('\n'.join(parts), encoding='utf-8')
    return len(members)


def write_hackathons(rows, out):
    d = out / 'hackathons'
    d.mkdir(parents=True, exist_ok=True)
    by = defaultdict(list)
    for r in rows:
        by[r.get('hackathon_title') or 'unknown'].append(r)
    for title, projs in by.items():
        org = next((p.get('organization_name') for p in projs if p.get('organization_name')), '')
        fm = front({'hackathon': title, 'organization': org,
                    'projects': len(projs), 'tags': ['hackathon']})
        counts = Counter(n for p in projs for f in FACET_DIR for n in strong_names(p, f))
        parts = [fm, f'\n# {title}\n', f'{org}  ·  {len(projs)} collected projects\n',
                 '## What this field was made of\n']
        parts.extend(f'- [[{n}]] × {c}' for n, c in counts.most_common(15))
        parts.append('\n## Projects\n')
        parts.extend(f"- {'★ ' if p.get('is_winner') else ''}[[{safe(p['slug'])}]] — "
                     f"{(p.get('tagline') or '')[:100]}" for p in projs)
        (d / f'{safe(title)}.md').write_text('\n'.join(parts), encoding='utf-8')
    return len(by)


def write_readme(rows, out, counts):
    tot = len(rows)
    win = sum(1 for r in rows if r.get('is_winner'))
    facet_tops = {}
    for f in FACET_DIR:
        c = Counter(n for r in rows for n in strong_names(r, f))
        facet_tops[f] = c.most_common(10)
    parts = [front({'tags': ['moc']}), '\n# Idea vault\n',
             f'{tot} projects ({win} winners) from {counts["hackathons"]} hackathons, '
             f'decomposed into {counts["facets"]} facet notes.\n',
             'An idea here is a **mechanism** applied to a **substrate** for a **user** '
             'inside a **domain**. Single facets are crowded; combinations are what stay '
             'rare — so the useful question is not "who else does X" but "who does X *and* Y".\n',
             '> Facet assignment is regex over the write-up. It measures the taxonomy\'s '
             'vocabulary as much as the field. Treat a count as a shortlist, widen '
             '`hub/taxonomy.json` until it hurts, and read the projects.\n']
    for f, top in facet_tops.items():
        parts.append(f'\n## {f}\n')
        parts.extend(f'- [[{n}]] — {c}' for n, c in top)
    parts.append('\n## Where the gaps are\n\nSee [[_gaps/README]] — combinations both of '
                 'whose halves are proven, that nobody has occupied.\n')
    (out / 'README.md').write_text('\n'.join(parts), encoding='utf-8')


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--in', dest='inp', default='data/facets.jsonl')
    ap.add_argument('--full', default='data/projects_full.jsonl',
                    help='source of the write-up bodies')
    ap.add_argument('--out', default='vault')
    a = ap.parse_args()

    rows = [json.loads(l) for l in Path(a.inp).read_text(encoding='utf-8').splitlines() if l.strip()]
    bodies = {}
    if Path(a.full).exists():
        for line in Path(a.full).read_text(encoding='utf-8').splitlines():
            if line.strip():
                r = json.loads(line)
                bodies[r.get('slug')] = r
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)

    n_proj = write_projects(rows, out, bodies)
    n_facet = write_facets(rows, out)
    n_hack = write_hackathons(rows, out)
    write_readme(rows, out, {'hackathons': n_hack, 'facets': n_facet})
    print(f'{n_proj} project notes, {n_facet} facet notes, {n_hack} hackathon notes -> {out}/')
    print(f'Open {out}/ as an Obsidian vault; start at README.md')


if __name__ == '__main__':
    main()
