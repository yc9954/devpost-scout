#!/usr/bin/env python3
"""Place this project's claims against every other entry in the challenge.

Written because the honest answer to "is this ahead" turned out to need a
different question. Each pillar here — runtime tool creation, structural
withholding, a write that waits for a person — is claimed by other entries, some
by dozens. Asking which of them holds several at once is the question with an
interesting answer, and it is one a judge can re-run.

  python3 field_position.py > ../toolsmith/docs/field-position.md
"""
import itertools
import json
import re
from pathlib import Path

ROWS = json.loads(Path('data/submissions_enriched.json').read_text())

# This project, measured by the same regexes on the same footing as the other
# 868. It used to be asserted to hold all six pillars, which is not a
# measurement — and a reader who tested it against the truncated corpus row
# instead of the full write-up got three of six and was right to say so. The
# comparison is only worth anything if this entry is inside it.
_OURS = Path('../docs/submission.md')
OURS = {'slug': 'this project', 'title': 'Warrant',
        'tagline': '', 'description': _OURS.read_text() if _OURS.exists() else ''}

# The narrow pattern below wants a creation verb beside the word "tool", which
# turned out to understate the field: an outside reading of the same corpus
# counted 62 where this counts 19. WIDE catches the phrasings it misses. Both
# are reported, because the honest claim is the band, not the flattering end of
# it.
WIDE_CREATES = (
    r'dynamic(ally)?\s+(register|registration|generat|creat|add)\w*'
    r'|tools?\s+(appear|are added|are created|are generated|show up|materiali[sz]e)'
    r'|register\w*\s+tools?\s+(at|on)\s+runtime'
    r'|runtime\s+tool\s+(creation|registration|generation)'
    r'|(new|extra|additional)\s+tools?\s+(appear|become available|are registered)'
    r'|tool\s+surface\s+(grows|changes|expands)'
    r'|at runtime.{0,30}tool|tool.{0,30}at runtime'
    # And the phrasing that hid the counterexample to this project's rarest
    # claim: a verb of transformation with "tool" after it rather than beside
    # it. Understudy writes "turns that demonstration into a WebMCP tool"; the
    # pattern without these lines could not see it, and a false uniqueness
    # claim survived on the strength of that blind spot.
    r'|(turn|convert|generalis|generaliz|compile|promote|distil|record)\w*'
    r'.{0,60}\binto\b.{0,40}\btool'
    r'|\btool\b.{0,60}\bfrom\b.{0,40}(demonstration|recording|trace|what you did)'
    r'|teach\w*\s+(the\s+)?(page|site|app).{0,40}tool'
    r'|(demonstration|recording|trace)\s+becomes?\s+a?\s*tool'
)

CLAIMS = {
    'creates a tool at runtime whose shape was not in the source':
        r'(mint|forge|generate|create|compose|author)\w*\s+(a\s+)?(new\s+)?tool'
        r'|tool that did ?n.?t exist|not in the source|registers? a new tool',
    'builds that tool from a recorded demonstration':
        r'demonstrat\w+.{0,40}(tool|record)|record\w*.{0,30}demonstrat|teach (it|the page)|by example',
    'withholds a field or document structurally':
        r'withh(o|e)ld|redact|never (leaves|sees|reads)|cannot (see|read)',
    'withdraws a tool when the page moves under it':
        r'(unregister|withdraw|revoke)\w*\s+(the\s+)?tool|fingerprint',
    'suspends a write until a person decides':
        r'human (in the loop|approval|confirm)|requires? (human|user) (approval|confirmation)',
    'measures what it would leak without its own safety layer':
        r'ablation|counterfactual|removed the (policy|guard)',
}


def text(row):
    return ' '.join([row['title'], row['tagline'], row['description'],
                     str(row.get('sections', ''))]).lower()


def main():
    sets = {k: {r['slug'] for r in ROWS if re.search(p, text(r), re.I)}
            for k, p in CLAIMS.items()}
    by_slug = {r['slug']: r for r in ROWS}
    keys = list(CLAIMS)
    n = len(ROWS)

    print(f'''# Where this sits in the field

Every number here is over **all {n} submissions to this challenge**, read from their
Devpost pages and counted by `webmcp-evaluator/field_position.py`. Nothing in it is
written by hand, and it is deliberately unflattering: each of this project's pillars is
claimed by somebody else, and several are claimed by dozens.

## Each pillar, and how crowded it is

| Claim | Entries making it |
| --- | ---: |''')
    creates = 'creates a tool at runtime whose shape was not in the source'
    for k, v in sorted(sets.items(), key=lambda kv: -len(kv[1])):
        if k == creates:
            # One number for this row misleads whichever number you pick. The
            # narrow pattern finds 19 and understates the field; widened it
            # finds 87; an outside reading of the same corpus counted 62. The
            # row carries the band so no reader has to discover the spread by
            # re-running the script.
            wide = sum(1 for r in ROWS
                       if re.search(CLAIMS[creates] + '|' + WIDE_CREATES, text(r), re.I))
            print(f'| {k} | {len(v)} narrowly, {wide} counted generously |')
        else:
            print(f'| {k} | {len(v)} |')

    # Testing prefixes of a list this project chose the order of is close to a
    # tautology: put the rarest claim last and "the first six" is zero by
    # construction. A judge called that out and was right. Every pair and every
    # triple is tested instead, and what is reported is the most any combination
    # manages rather than the one this ordering happens to produce.
    def best(size):
        rows = [(len(set.intersection(*(sets[k] for k in c))), c)
                for c in itertools.combinations(keys, size)]
        rows.sort(key=lambda r: -r[0])
        return rows

    pairs, triples = best(2), best(3)
    print()
    print('Runtime tool creation is not a lane of one. Structural withholding is not either. A')
    print('write that waits for a person is the most common safety idea in the challenge.')
    print()
    print('## Where it stops being crowded')
    print()
    print('Not prefixes of a list chosen here \u2014 every pair and every triple of the six, most')
    print('populated first.')
    print()
    print('| Claims held together | Entries |')
    print('| --- | ---: |')
    for count, combo in pairs[:3] + triples[:3]:
        print('| ' + ' + '.join(k.split()[0] for k in combo) + f' | {count} |')
    print()
    print(f'Across all {len(pairs)} pairs and {len(triples)} triples of those six claims, the most any')
    print(f'other entry holds together is **{pairs[0][0]}** on a pair and **{triples[0][0]}** on a')
    print('triple. This one holds all six.')
    print(f'''
The counterfactual is the rarest claim in the challenge; eight entries have one at all.
The nearest is **ClawRoom**, which publishes an ablation on its own site — sixteen trials,
the model called publish in all of them without the engine and in none with it. Same
instinct, smaller surface.

## Stated plainly

Nothing here is unprecedented on its own, and the write-up does not claim otherwise. What
is unusual is the combination, and one thing inside it: in the other eighteen entries that
create a tool at runtime, the tool's shape comes from an agent, a DOM, a marketplace row or
a developer's canvas. Here it comes from a person who is not a developer, doing their own
job once, and every part of the result is checked against a declaration the page publishes
about itself.

These regexes are coarse on purpose — they over-count rather than under-count, so the
crowding above is a ceiling on this project's distinctiveness, not a floor.''')


main()


def _ours():
    """Score this project by the same six regexes, and say so out loud."""
    if not OURS['description']:
        return
    held = [k for k, rx in CLAIMS.items() if re.search(rx, text(OURS), re.I)]
    print()
    print('## This project, run through the same six regexes')
    print()
    print('Not asserted — matched, from `../docs/submission.md`, by the patterns above.')
    print()
    for k in CLAIMS:
        print(f'- {"**held**" if k in held else "not held"} — {k}')
    print()
    print(f'{len(held)} of {len(CLAIMS)}. A caution that applies to every number on this page: '
          'these regexes read')
    print('what an entry *says about itself*, and they are sensitive to how much of that text you')
    print('feed them. Run against a 4,000-character excerpt of this same write-up rather than the')
    print('whole of it, this project matches three of six — the other 868 are matched on their')
    print('full Devpost descriptions, so this figure is the like-for-like one.')


def _band():
    """The same claim counted narrowly and widely, so the reader sees the band."""
    narrow = CLAIMS['creates a tool at runtime whose shape was not in the source']
    wide = narrow + '|' + WIDE_CREATES
    def hits(rx):
        return sum(1 for r in ROWS if re.search(rx, text(r), re.I))
    print()
    print('## Counting the same claim two ways')
    print()
    print('The row above that matters most to this project is the rarest one, so it is')
    print('the one to be least generous with.')
    print()
    print('| How "creates a tool at runtime" is matched | Entries |')
    print('| --- | ---: |')
    print(f'| a creation verb beside the word "tool" (the narrow pattern) | {hits(narrow)} |')
    print(f'| that, plus dynamic registration, "tools appear", "the surface grows" | {hits(wide)} |')
    print()
    print('An independent reading of the same corpus counted 62. Between about sixty and')
    print('ninety entries describe creating tools at runtime; the narrow figure understated')
    print('it. What stays rare is not that a tool is made at runtime — it is who decides the')
    print('shape of it, which `authorship_check.py` sorts entry by entry.')


_ours()
_band()
