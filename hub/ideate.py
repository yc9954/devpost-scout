#!/usr/bin/env python3
"""Propose ideas for ONE hackathon, out of what has won in every other one.

The brain in `data/facets.jsonl` is thousands of winners across hundreds of
hackathons. The question this answers is not "what is a good idea" in the
abstract; it is:

    Given THIS hackathon's rubric, which moves are proven somewhere else
    and absent here?

Three generators, in descending order of how defensible the resulting claim is:

1. **Transfer** — a mechanism with many wins across the corpus that nobody in
   this hackathon's field has used. The strongest kind, because the mechanism is
   already proven to win; only the setting is new.
2. **Combination** — a mechanism × domain pair whose halves are both well
   populated and whose intersection is empty. This project's own field work found
   twice that single pillars are crowded and combinations are what stay rare.
3. **Under-served substrate** — something this hackathon's entrants keep reading
   in one way that another field reads better.

    python3 hub/ideate.py --config config.json --facets data/facets.jsonl --top 12

Everything is scored against the hackathon's own criteria, verbatim from
`discover/hackathon.py`, with extra weight on the **tiebreak criterion** — the
first one listed, which Devpost's standard tie-break resolves on and which
therefore decides placements once scores bunch at the top.

**Nothing here is an idea yet.** Zero occupancy is not evidence of a good idea;
nobody may have done it because it is not attractive. Each candidate ships with
the five kill tests from `position/IDEA-SELECTION.md`, and failing one kills it.
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


def strong(row, facet):
    return {n for n, h in row['facets'].get(facet, {}).items() if h['strong']}


def load(path):
    return [json.loads(l) for l in Path(path).read_text(encoding='utf-8').splitlines() if l.strip()]


def criteria_terms(cfg, corpus_df=None, n_docs=1):
    """Words the rubric uses, weighted by criterion share AND by rarity.

    Weighting by share alone let generic rubric words — project, work, real,
    deliver — dominate, so every candidate scored the same tiny number. An
    inverse-document-frequency factor over the corpus makes the *distinctive*
    rubric words (the platform's name, 'ablation', 'audience') carry the signal,
    which is what actually separates one candidate from another.
    """
    import math
    weights = defaultdict(float)
    crits = cfg.get('criteria') or []
    tie = (cfg.get('tiebreak_criterion') or '').lower()
    for c in crits:
        share = (c.get('max') or round(100 / max(len(crits), 1))) / 100.0
        if c.get('label', '').lower() == tie:
            share *= 1.5                      # the tie-break criterion decides bunched fields
        for w in re.findall(r'[a-z]{4,}', f"{c.get('label','')} {c.get('text','')}".lower()):
            if w in STOP:
                continue
            idf = math.log((n_docs + 1) / (1 + (corpus_df or {}).get(w, 0))) if corpus_df else 1.0
            weights[w] += share * max(idf, 0.1)
    return weights


def document_frequency(rows):
    df = Counter()
    for r in rows:
        seen = set(re.findall(r'[a-z]{4,}', f"{r.get('title','')} {r.get('tagline','')}".lower()))
        df.update(seen)
    return df


STOP = set('does that this what with from your they their have been will more than '
           'project projects judges judge submission entrant entrants which when '
           'well only just about into over most much some very both each other '
           'work works working using used make makes made real really'.split())


def rubric_fit(text, weights):
    """Score prose against the rubric's own vocabulary.

    Scoring the *facet name* against the rubric was worthless — 'realtime_stream'
    shares no words with 'How thoroughly does the project use the platform', so
    every candidate scored 0. What carries rubric-shaped language is the prose of
    the projects that already used the move, so that is what gets scored.
    """
    words = set(re.findall(r'[a-z]{4,}', (text or '').lower())) - STOP
    if not words:
        return 0.0
    hit = sum(weights.get(w, 0) for w in words)
    return round(hit / (len(words) ** 0.5), 2)          # length-normalised


def target_field(rows, cfg, host):
    """Projects already in this hackathon's field, if the brain has any."""
    title = (cfg.get('hackathon_title') or '').lower()
    out = []
    for r in rows:
        ht = (r.get('hackathon_title') or '').lower()
        if host and host in (r.get('hackathon_host') or ''):
            out.append(r)
        elif title and ht and title in ht:
            out.append(r)
    return out


def _exemplars(rows, mech, dom, per_side=2):
    """The best few projects proving each half, longest write-up first."""
    def pick(pred):
        hits = [r for r in rows if pred(r)]
        hits.sort(key=lambda r: -(r.get('words') or 0))
        return hits[:per_side]

    out = []
    for r in pick(lambda r: mech in strong(r, 'mechanism')):
        out.append({'slug': r['slug'], 'title': r['title'], 'side': f'mechanism {mech}',
                    'hackathon': r.get('hackathon_title'),
                    'tagline': (r.get('tagline') or '')[:120]})
    for r in pick(lambda r: dom in strong(r, 'domain')):
        out.append({'slug': r['slug'], 'title': r['title'], 'side': f'domain {dom}',
                    'hackathon': r.get('hackathon_title'),
                    'tagline': (r.get('tagline') or '')[:120]})
    return out


def generate(rows, field, cfg, min_wins, min_expected=2.0):
    n = len(rows)
    weights = criteria_terms(cfg, document_frequency(rows), n)
    tax_text = {}                                    # facet -> readable phrase
    wins = Counter()
    for r in rows:
        for f in ('mechanism', 'domain', 'substrate', 'user'):
            for name in strong(r, f):
                wins[(f, name)] += 1
                tax_text.setdefault((f, name), name.replace('_', ' '))

    here = Counter()
    for r in field:
        for f in ('mechanism', 'domain', 'substrate', 'user'):
            for name in strong(r, f):
                here[(f, name)] += 1

    has_field = bool(field)
    cands = []

    # 1 · transfer: proven globally, absent in this field
    for (f, name), c in wins.items():
        if f != 'mechanism' or c < min_wins:
            continue
        local = here[(f, name)]
        if field and local > max(1, c * 0.02):
            continue
        exemplars = [r for r in rows if name in strong(r, 'mechanism')]
        domains = Counter(d for r in exemplars for d in strong(r, 'domain'))
        cands.append({
            'kind': 'transfer' if has_field else 'rubric-fit', 'mechanism': name, 'partner': None,
            'global_wins': c, 'in_this_field': local,
            'spread_domains': len(domains),
            'fit': rubric_fit(' '.join(
                f"{e.get('title','')} {e.get('tagline','')}" for e in exemplars[:40]), weights),
            'evidence': [{'slug': e['slug'], 'title': e['title'],
                          'hackathon': e.get('hackathon_title'),
                          'tagline': (e.get('tagline') or '')[:120]} for e in exemplars[:4]],
            'why': (f'{c} winners across {len(domains)} different domains use this move; '
                    f'{local} in this field.') if has_field else
                   (f'{c} winners across {len(domains)} domains. Ranked by how closely their '
                    f'prose matches THIS rubric — absence here is unmeasured.'),
        })

    # 2 · combination: both halves proven, intersection empty
    obs = Counter()
    for r in rows:
        for m in strong(r, 'mechanism'):
            for d in strong(r, 'domain'):
                obs[(m, d)] += 1
    for (fm, m), cm in wins.items():
        if fm != 'mechanism' or cm < min_wins:
            continue
        for (fd, d), cd in wins.items():
            if fd != 'domain' or cd < min_wins:
                continue
            exp = cm * cd / n
            got = obs[(m, d)]
            # Empty cells are a small-corpus artifact. At 2,873 winners several
            # mechanism x domain pairs were genuinely unoccupied; at 8,636 almost
            # none are, because every well-populated pair picks up a few entrants.
            # So the signal is not emptiness, it is *under*-occupancy relative to
            # independence — the same quantity, measured as a ratio.
            if exp < min_expected or got > exp * 0.6:
                continue
            cands.append({
                'kind': 'combination', 'mechanism': m, 'partner': d,
                'global_wins': cm, 'in_this_field': here[('mechanism', m)],
                'expected': round(exp, 1), 'observed': got, 'spread_domains': None,
                'fit': rubric_fit(' '.join(
                    f"{e.get('title','')} {e.get('tagline','')}"
                    for e in rows if m in strong(e, 'mechanism') or d in strong(e, 'domain')), weights),
                # Show both halves. Taking the first N rows holding the mechanism
                # picked whatever sat earliest in the file — Solana DeFi entries
                # were offered as proof for a clinical-domain candidate.
                'evidence': _exemplars(rows, m, d),
                'why': (f'{m} appears in {cm} winners and {d} in {cd}. Independence predicts '
                        f'{exp:.1f} holding both. There '
                        + ('are none.' if not got else
                           f'are {got} — {(1-got/exp)*100:.0f}% under.')),
            })

    # Without the target hackathon's own corpus, "absent here" is unmeasured and
    # ranking by global frequency just reproduces a popularity list. So the weights
    # flip: rubric fit carries the ordering and the output says so.
    for c in cands:
        deficit = (c.get('expected') or 0) - (c.get('observed') or 0)
        if has_field:
            c['score'] = round(c['fit'] * 3 + (c.get('spread_domains') or 0) * 0.5
                               + min(c['global_wins'], 40) * 0.1 + deficit * 1.2, 2)
        else:
            c['score'] = round(c['fit'] * 12 + deficit * 1.2
                               + min(c['global_wins'], 40) * 0.02, 2)
    cands.sort(key=lambda c: -c['score'])
    return cands


TESTS = """
## Before this is an idea

Zero occupancy is **not** evidence of a good idea — nobody may have done it
because it is not attractive. Five tests, from `position/IDEA-SELECTION.md`.
Fail one and it is dead, not weakened.

- [ ] **Prompt** — would a person with a better prompt to a general model get the same result?
- [ ] **Server** — move it to a server API. Does it die? If it survives, the platform is decoration.
- [ ] **Occupancy** — widen the patterns until they hurt, then recount. This cell was measured
      with `hub/taxonomy.json`'s vocabulary, not the field's.
- [ ] **60-second** — does a judge, alone, with no login, say "huh" inside a minute?
- [ ] **24-hour** — can you build it reliably in the time you actually have?
"""


def write_notes(cands, out_dir, cfg):
    d = Path(out_dir)
    d.mkdir(parents=True, exist_ok=True)
    for c in cands:
        name = f"{c['mechanism']}" + (f" x {c['partner']}" if c['partner'] else " (transfer)")
        body = ['---', 'tags:', '  - "candidate"', f'  - "kind/{c["kind"]}"',
                f'score: {c["score"]}', f'fit: {c["fit"]}', '---',
                f'\n# {name}\n', f'**{c["kind"]}** · score {c["score"]} · rubric fit {c["fit"]}\n',
                f'{c["why"]}\n',
                f'Target: **{cfg.get("hackathon_title", "?")}** — tiebreak criterion '
                f'**{cfg.get("tiebreak_criterion", "?")}**.\n',
                '## Where the move is already proven\n']
        body.extend(f"- [[{e['slug']}]] — {e['tagline']}"
                    + (f"  <sub>{e['side']} · {e['hackathon']}</sub>" if e.get('side')
                       else f"  <sub>{e['hackathon']}</sub>")
                    for e in c['evidence'])
        body.append(TESTS)
        body.append('\n## Rubric\n')
        for cr in cfg.get('criteria') or []:
            body.append(f"- **{cr['label']}** ({cr.get('max')}) — {cr['text'][:150]}")
        (d / f"{name.replace('/', '-')}.md").write_text('\n'.join(body), encoding='utf-8')
    idx = ['---', 'tags:', '  - "moc"', '---', f'\n# Candidates for {cfg.get("hackathon_title","?")}\n',
           '| candidate | kind | score | fit | why |', '| --- | --- | ---: | ---: | --- |']
    idx.extend(f"| [[{c['mechanism']}{' x ' + c['partner'] if c['partner'] else ' (transfer)'}]] "
               f"| {c['kind']} | {c['score']} | {c['fit']} | {c['why'][:90]} |" for c in cands)
    (d / 'README.md').write_text('\n'.join(idx), encoding='utf-8')


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--config', default='config.json')
    ap.add_argument('--facets', default='data/facets.jsonl')
    ap.add_argument('--vault', default='vault')
    ap.add_argument('--top', type=int, default=12)
    ap.add_argument('--min-wins', type=int, default=5)
    ap.add_argument('--field', help='facets.jsonl for THIS hackathon\'s own corpus, when the '
                                    'brain does not contain it (an unpublished gallery, say)')
    ap.add_argument('--min-expected', type=float, default=2.0)
    a = ap.parse_args()

    cfg = json.loads(Path(a.config).read_text(encoding='utf-8'))
    rows = load(a.facets)
    host = cfg.get('hackathon_host', '')
    field = load(a.field) if a.field else target_field(rows, cfg, host)

    print(f'brain: {len(rows)} winners. this field in brain: {len(field)}')
    if not field:
        print('  ⚠ this hackathon\'s own field is not available (unpublished gallery, or\n'
              '    stage 2 not run). Absence here is UNMEASURED, so candidates are ranked by\n'
              '    how closely proven winners\' prose matches this rubric — a weaker claim.\n'
              '    Run the field enumeration and pass --field to get the real ordering.')
    if not cfg.get('criteria'):
        print('  ⚠ no criteria in config: scoring falls back to spread alone. '
              'Run discover/hackathon.py first.')

    cands = generate(rows, field, cfg, a.min_wins, a.min_expected)[:a.top]
    print(f'\n{"candidate":<46} {"kind":<12} {"score":>6} {"fit":>6}  why')
    for c in cands:
        nm = c['mechanism'] + (f" × {c['partner']}" if c['partner'] else '')
        print(f'{nm[:46]:<46} {c["kind"]:<12} {c["score"]:>6} {c["fit"]:>6}  {c["why"][:70]}')

    write_notes(cands, Path(a.vault) / '_candidates', cfg)
    print(f'\n{len(cands)} candidate notes -> {a.vault}/_candidates/')
    print('None of these is an idea until it survives the five tests in each note.')


if __name__ == '__main__':
    main()
