#!/usr/bin/env python3
"""Find the combinations nobody has occupied — and say why that might be bad news.

This project's own field work landed on one finding twice, independently: single
pillars are always more crowded than you think, and the *combination* is what
stays rare. So the interesting question is never "has anyone done X". It is
"has anyone done X **and** Y", where both X and Y are individually proven.

For every pair of facets the expected co-occurrence under independence is

    E = count(A) * count(B) / N

and a pair whose observed count O is far below E is a hole in a field that
otherwise had every reason to fill it.

    python3 hub/gaps.py --in data/facets.jsonl --vault vault/ --top 40

**The warning that has to travel with every row of this output**, from
`position/IDEA-SELECTION.md`: *zero occupancy is not evidence of a good idea.
Nobody may have done it because it isn't attractive.* An empty cell is a
question, and the five kill tests are how you answer it — not a green light.
"""
import argparse
import json
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

PAIRS = [('mechanism', 'domain'), ('mechanism', 'substrate'),
         ('domain', 'mechanism'), ('substrate', 'domain'), ('user', 'mechanism')]


def strong(row, facet):
    return {n for n, h in row['facets'].get(facet, {}).items() if h['strong']}


def analyse(rows, facet_a, facet_b, min_expected):
    n = len(rows)
    ca = Counter(x for r in rows for x in strong(r, facet_a))
    cb = Counter(x for r in rows for x in strong(r, facet_b))
    observed = Counter()
    examples = defaultdict(list)
    for r in rows:
        for a in strong(r, facet_a):
            for b in strong(r, facet_b):
                observed[(a, b)] += 1
                examples[(a, b)].append(r)
    out = []
    for a, na in ca.items():
        for b, nb in cb.items():
            if facet_a == facet_b and a == b:
                continue
            exp = na * nb / n
            if exp < min_expected:
                continue
            obs = observed[(a, b)]
            out.append({
                'a': a, 'b': b, 'facet_a': facet_a, 'facet_b': facet_b,
                'count_a': na, 'count_b': nb, 'observed': obs,
                'expected': round(exp, 2), 'deficit': round(exp - obs, 2),
                'examples': [{'slug': p['slug'], 'title': p['title'],
                              'tagline': p.get('tagline'), 'winner': p.get('is_winner')}
                             for p in examples[(a, b)][:3]],
            })
    out.sort(key=lambda r: (-r['deficit'], -r['expected']))
    return out


def write_notes(gaps, vault, facet_dirs):
    d = Path(vault) / '_gaps'
    d.mkdir(parents=True, exist_ok=True)
    for g in gaps:
        name = f"{g['a']} x {g['b']}"
        body = [
            '---', 'tags:', '  - "gap"', f"observed: {g['observed']}",
            f"expected: {g['expected']}", f"deficit: {g['deficit']}", '---',
            f"\n# {name}\n",
            f"[[{g['a']}]] appears in **{g['count_a']}** projects. "
            f"[[{g['b']}]] appears in **{g['count_b']}**. "
            f"If the two were independent you would expect **{g['expected']}** "
            f"projects holding both. There are **{g['observed']}**.\n",
        ]
        if g['observed'] == 0:
            body.append('Nobody in this corpus has put them together.\n')
        else:
            body.append('## Who is nearest\n')
            body.extend(f"- {'★ ' if e['winner'] else ''}[[{e['slug']}]] — "
                        f"{(e['tagline'] or '')[:110]}" for e in g['examples'])
        body.append("""
## Before this counts as an idea

Zero occupancy is **not** evidence of a good idea — nobody may have done it
because it is not attractive. Run `position/IDEA-SELECTION.md`'s five tests, and
fail one and it is dead:

- [ ] **Prompt** — would a better prompt to a general model get the same result?
- [ ] **Server** — move it to a server API. Does it die? If not, the platform is decoration.
- [ ] **Occupancy** — widen the patterns until they hurt, then recount. This cell was
      measured with the taxonomy's vocabulary, not the field's.
- [ ] **60-second** — does a judge with no login say "huh" inside a minute?
- [ ] **24-hour** — can you build it reliably in the time you actually have?
""")
        safe = name.replace('/', '-')
        (d / f'{safe}.md').write_text('\n'.join(body), encoding='utf-8')

    idx = ['---', 'tags:', '  - "moc"', '---', '\n# Gaps\n',
           'Combinations both of whose halves are proven in this corpus, that few or no '
           'projects hold together. Sorted by how far below independence they sit.\n',
           '> An empty cell is a question, not a green light. '
           '`position/IDEA-SELECTION.md` is how you answer it.\n',
           '| pair | seen | expected | deficit |', '| --- | ---: | ---: | ---: |']
    idx.extend(f"| [[{g['a']} x {g['b']}]] | {g['observed']} | {g['expected']} | {g['deficit']} |"
               for g in gaps)
    (d / 'README.md').write_text('\n'.join(idx), encoding='utf-8')
    return len(gaps)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--in', dest='inp', default='data/facets.jsonl')
    ap.add_argument('--vault', default='vault')
    ap.add_argument('--top', type=int, default=40)
    ap.add_argument('--min-expected', type=float, default=3.0,
                    help='ignore pairs too rare for absence to mean anything')
    ap.add_argument('--only-empty', action='store_true', help='only cells with zero projects')
    a = ap.parse_args()

    rows = [json.loads(l) for l in Path(a.inp).read_text(encoding='utf-8').splitlines() if l.strip()]
    seen, gaps = set(), []
    for fa, fb in PAIRS:
        for g in analyse(rows, fa, fb, a.min_expected):
            key = tuple(sorted((g['a'], g['b'])))
            if key in seen:
                continue
            if a.only_empty and g['observed']:
                continue
            seen.add(key)
            gaps.append(g)
    gaps.sort(key=lambda r: (-r['deficit'], -r['expected']))
    gaps = gaps[:a.top]

    print(f'{len(rows)} projects. Top {len(gaps)} unoccupied combinations:\n')
    print(f"{'mechanism / facet A':<26} {'facet B':<24} {'seen':>5} {'exp':>7} {'deficit':>8}")
    for g in gaps:
        print(f"{g['a'][:26]:<26} {g['b'][:24]:<24} {g['observed']:>5} "
              f"{g['expected']:>7.1f} {g['deficit']:>8.1f}")
    n = write_notes(gaps, a.vault, None)
    print(f'\n{n} gap notes -> {a.vault}/_gaps/')
    print('Zero occupancy is not evidence of a good idea. Five tests before you build.')


if __name__ == '__main__':
    main()
