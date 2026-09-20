#!/usr/bin/env python3
"""Turn extracted claims into the graph layer the facet graph could not be.

The facet graph collapses: 66% of projects shared an identical mechanism/domain
signature and the largest single signature held 1,341 of them. Claims do not
collapse the same way, because a claim is a sentence about a *condition* rather
than a label from a fixed vocabulary — and the interesting fact is that
independent projects in unrelated domains keep arriving at the same one.

This finds those convergences and writes them into the vault as first-class
notes, with directed edges:

    project --asserts--> claim
    project --answers--> problem
    claim   --recurs-in--> domain   (from the write-up's own transfers_to)

    python3 hub/claim_graph.py --claims data/claims.jsonl --vault vault/

Clustering is lexical, over content words shared between two claims. That is
crude and it is honest about being crude: it will miss a convergence expressed
in different vocabulary, which is the same blind spot `position/field_position.py`
was caught by. Widen it before concluding two ideas are unrelated.
"""
import argparse
import json
import math
import re
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

STOP = set("""the a an and or but of to in on for with that this it is are was were be been
being as at by from into than then so if not no nor only own same too very can will just
which who whom what when where how why all any both each few more most other some such
their there these those they them our your you we i he she his her its it's don't
one two three thing things people person use used using make makes made get gets got
because about after before through during while over under again further once here
because cannot does do did doing have has had having would could should may might must
system tool app application project user users way ways part parts time times work works
new old good bad big small""".split())


def words(text):
    return [w for w in re.findall(r"[a-z']{4,}", (text or '').lower()) if w not in STOP]


def _peel(members, adj, cohesion):
    """Reduce a connected component to a quasi-clique, then recurse on the rest.

    Union-find alone chains: A shares 3 words with B, B shares 3 *different*
    words with C, and A and C land in the same "convergence" having nothing in
    common. At 552 claims that produced a 41-project cluster whose first and
    last members were unrelated. A convergence is only a convergence if most of
    its members actually overlap each other, so each member must be linked to at
    least `cohesion` of the others; the weakest is dropped until that holds, and
    whatever was dropped is clustered again on its own.
    """
    out = []
    pool = set(members)
    while len(pool) >= 2:
        cur = set(pool)
        while len(cur) >= 2:
            deg = {m: len(adj[m] & cur) for m in cur}
            need = max(1, int(round(cohesion * (len(cur) - 1))))
            weakest = min(deg, key=lambda m: deg[m])
            if deg[weakest] >= need:
                break
            cur.discard(weakest)
        if len(cur) < 2:
            break
        out.append(cur)
        pool -= cur
    return out


def document_frequency(item_words):
    df = Counter()
    for w in item_words:
        df.update(w)
    return df


def cluster(rows, key, min_overlap, min_size, cohesion=0.5, df_ceiling=0.08,
            min_shared_idf=13.0):
    """Group rows whose `key` sentences share enough *rare* content words.

    The hand-written STOP list cannot keep up. Printing each cluster's shared
    vocabulary showed clusters held together by `like`, `look`, `need`,
    `nobody`, `getting`, `still` — filler that appears in nearly every claim
    and carries no information about what two projects have in common. That is
    `hub/taxonomy.json`'s failure again: a curated word list lies as the corpus
    grows. So the ceiling is measured, not guessed — any word appearing in more
    than `df_ceiling` of the claims is dropped, and a link additionally has to
    clear a total inverse-document-frequency floor, so three rare words count
    for more than five common ones.

    The floor was swept, not guessed. At 10 it produced a six-project
    "convergence" joining Hindi surgical consent, a food recall tracer, a waste
    segregator and an employment platform — held together by `million`, `year`,
    `five`, `india`, `americans`. That is shared *statistics-citation* habit, not
    a shared claim. 13 is the point where every surviving cluster names a
    condition rather than a writing style.
    """
    items = [(r, set(words(r.get(key)))) for r in rows if r.get(key)]
    items = [(r, w) for r, w in items if len(w) >= 4]

    n = len(items)
    df = document_frequency(w for _, w in items)
    ceiling = max(2, int(n * df_ceiling))
    idf = {t: math.log(n / c) for t, c in df.items() if c <= ceiling}
    items = [(r, {t for t in w if t in idf}) for r, w in items]
    items = [(r, w) for r, w in items if len(w) >= 3]
    parent = list(range(len(items)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    pairs = []
    adj = defaultdict(set)
    for (i, (ri, wi)), (j, (rj, wj)) in combinations(list(enumerate(items)), 2):
        shared = wi & wj
        weight = sum(idf[t] for t in shared)
        if len(shared) >= min_overlap and weight >= min_shared_idf:
            pairs.append((len(shared), i, j, shared))
            adj[i].add(j)
            adj[j].add(i)
            a, b = find(i), find(j)
            if a != b:
                parent[a] = b

    components = defaultdict(list)
    for i in range(len(items)):
        components[find(i)].append(i)

    out = []
    for comp in components.values():
        if len(comp) < min_size:
            continue
        for sub in _peel(comp, adj, cohesion):
            if len(sub) >= min_size:
                out.append(sorted(sub))
    out.sort(key=len, reverse=True)

    shared_of = {(i, j): sh for _, i, j, sh in pairs}
    groups, evidence = [], []
    for sub in out:
        groups.append([items[i][0] for i in sub])
        ev = [(items[i][0], items[j][0], shared_of[(i, j)])
              for i, j in combinations(sub, 2) if (i, j) in shared_of]
        ev.sort(key=lambda t: -len(t[2]))
        evidence.append(ev)
    return groups, evidence


def slug(text, n=60):
    s = re.sub(r'[^a-z0-9]+', '-', (text or '').lower()).strip('-')
    return s[:n] or 'unnamed'


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--claims', default='data/claims.jsonl')
    ap.add_argument('--vault', default='vault')
    ap.add_argument('--min-overlap', type=int, default=3,
                    help='content words two claims must share to be linked')
    ap.add_argument('--min-size', type=int, default=2)
    ap.add_argument('--min-confidence', type=float, default=0.6)
    ap.add_argument('--df-ceiling', type=float, default=0.08,
                    help='drop words appearing in more than this fraction of claims')
    ap.add_argument('--min-shared-idf', type=float, default=13.0,
                    help='total rarity a shared vocabulary must carry to link two claims')
    ap.add_argument('--cohesion', type=float, default=0.5,
                    help='fraction of the other members each member must overlap; '
                         'guards against transitive chaining')
    a = ap.parse_args()

    rows = [json.loads(l) for l in Path(a.claims).read_text(encoding='utf-8').splitlines() if l.strip()]
    rows = [r for r in rows if r.get('claim') and r.get('confidence', 0) >= a.min_confidence]
    print(f'{len(rows)} claims at confidence >= {a.min_confidence}')

    groups, evidence = cluster(rows, 'claim', a.min_overlap, a.min_size, a.cohesion,
                               a.df_ceiling, a.min_shared_idf)
    pgroups, _ = cluster(rows, 'problem', a.min_overlap, a.min_size, a.cohesion,
                          a.df_ceiling, a.min_shared_idf)

    vault = Path(a.vault)
    cdir = vault / '_claims'
    cdir.mkdir(parents=True, exist_ok=True)

    # one note per project claim, linking to its project and its transfer domains
    for r in rows:
        name = slug(r['claim'])
        body = ['---', 'tags:', '  - "claim"', f"confidence: {r.get('confidence')}",
                f"evidence: \"{r.get('evidence_kind')}\"", '---',
                f"\n# {r['claim']}\n",
                f"Asserted by [[{r['slug']}]] — *{r.get('title')}*  ",
                f"<sub>{r.get('hackathon_title')}</sub>\n",
                f"**Problem** {r.get('problem') or '—'}\n",
                f"**Mechanism** {r.get('mechanism') or '—'}  ",
                f"**Beneficiary** {r.get('beneficiary') or '—'}\n",
                '**Recurs in** ' + ' '.join(f'[[{t}]]' for t in (r.get('transfers_to') or []))]
        (cdir / f'{name}.md').write_text('\n'.join(body), encoding='utf-8')

    # convergence notes: the same claim reached independently
    conv = vault / '_convergences'
    conv.mkdir(parents=True, exist_ok=True)
    index = ['---', 'tags:', '  - "moc"', '---', '\n# Convergences\n',
             'The same structural claim, reached independently by projects in different '
             'domains and different hackathons. These are the links a facet graph cannot '
             'produce, because the projects share no mechanism and no domain label.\n',
             '| shared claim | projects | hackathons |', '| --- | ---: | ---: |']
    for gi, g in enumerate(groups):
        hacks = {x.get('hackathon_title') for x in g}
        ev = evidence[gi]
        shared_terms = sorted(set().union(*[sh for _, _, sh in ev])) if ev else []
        title = (f'convergence-{gi:02d}-' +
                 (slug('-'.join(shared_terms[:6]), 50) if shared_terms
                  else slug(g[0]['claim'], 40)))
        body = ['---', 'tags:', '  - "convergence"', f'projects: {len(g)}',
                f'hackathons: {len(hacks)}', '---',
                f'\n# {len(g)} projects, {len(hacks)} hackathons, one claim\n',
                '**Shared vocabulary** ' + ', '.join(shared_terms or ['—']) + '\n']
        for x in sorted(g, key=lambda r: -r.get('confidence', 0)):
            body.append(f"### [[{x['slug']}]] — {x.get('title')}")
            body.append(f"> {x['claim']}\n")
            body.append(f"*{x.get('hackathon_title')}* · problem: {x.get('problem') or '—'}\n")
        (conv / f'{title}.md').write_text('\n'.join(body), encoding='utf-8')
        index.append(f"| [[{title}]] | {len(g)} | {len(hacks)} |")
    (conv / 'README.md').write_text('\n'.join(index), encoding='utf-8')

    print(f'{len(rows)} claim notes -> {cdir}/')
    print(f'{len(groups)} claim convergences, {len(pgroups)} problem convergences '
          f'-> {conv}/')
    print('\nLargest convergences:')
    for g in groups[:12]:
        hacks = len({x.get('hackathon_title') for x in g})
        print(f'  {len(g):>2} projects / {hacks:>2} hackathons  '
              f'{g[0]["claim"][:88]}')


if __name__ == '__main__':
    main()
