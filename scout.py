#!/usr/bin/env python3
"""One command: name a hackathon, get the rubric, the field, and candidate ideas.

    python3 scout.py "agents for humans"
    python3 scout.py "revenuecat shipaton 2026" --deep 120

It chains what the rest of the repository does piecewise:

  1. resolve the hackathon and read its criteria VERBATIM        discover/hackathon.py
  2. report what fails an entry outright, and the tie-break      discover/hackathon.py
  3. pull the field that already exists                          hub/collect_gallery.py
  4. decompose it into mechanism / domain / user / substrate     hub/extract.py
  5. propose what is proven elsewhere and absent here            hub/ideate.py

Everything it prints is measured or quoted. Where a number is weak it says so —
an empty field because a gallery was never published is not an empty field, and
a candidate list built without the hackathon's own corpus is a much weaker claim
than one built with it.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))


def run(args, quiet=True):
    r = subprocess.run([sys.executable] + args, capture_output=True, text=True, cwd=ROOT)
    if r.returncode and not quiet:
        print(r.stderr[-800:], file=sys.stderr)
    return r


def rule(title):
    print(f'\n\033[1m{"═" * 72}\n  {title}\n{"═" * 72}\033[0m')


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('hackathon', help='name, or a devpost host')
    ap.add_argument('--pick', type=int, default=1, help='which search result')
    ap.add_argument('--deep', type=int, default=0,
                    help='fetch N full write-ups from this field (slower, much better)')
    ap.add_argument('--brain', default='data/facets.jsonl')
    ap.add_argument('--work', default='data/run')
    ap.add_argument('--top', type=int, default=10)
    a = ap.parse_args()

    work = ROOT / a.work
    work.mkdir(parents=True, exist_ok=True)
    cfg_path = work / 'config.json'

    # 1 ── resolve
    rule('1 · HACKATHON')
    arg = '--host' if a.hackathon.endswith('.devpost.com') else '--name'
    r = run(['discover/hackathon.py', arg, a.hackathon, '--pick', str(a.pick),
             '--out', str(cfg_path)])
    if r.returncode:
        print(r.stderr.strip() or 'could not resolve that hackathon')
        return 2
    print(r.stderr.strip())
    cfg = json.loads(cfg_path.read_text(encoding='utf-8'))

    # 2 ── the rubric, verbatim
    rule('2 · RUBRIC — quoted, never paraphrased')
    crits = cfg.get('criteria') or []
    if not crits:
        print('  ⚠ criteria did not parse. Open the hackathon page and fill config.json by hand.')
    for c in crits:
        tie = '  ◀ TIEBREAK' if c['label'] == cfg.get('tiebreak_criterion') else ''
        print(f"  {c['order']}. \033[1m{c['label']}\033[0m ({c['max']}){tie}")
        print(f"     {c['text'][:200]}")
    print(f"\n  weighting: {cfg.get('criteria_weighting')}")
    print(f"  Devpost breaks ties on the FIRST criterion, so \033[1m{cfg.get('tiebreak_criterion')}\033[0m "
          f"decides placements once scores bunch.")
    reqs = cfg.get('requirements') or {}
    if reqs:
        print('\n  fails an entry outright:')
        for k, v in reqs.items():
            print(f'    · {k} = {v}')
    if cfg.get('prizes'):
        print(f"\n  prizes: {', '.join(cfg['prizes'][:4])}")

    # 3 ── the field
    rule('3 · THE FIELD')
    host = cfg['hackathon_host']
    field_raw = work / 'field.jsonl'
    if field_raw.exists():
        field_raw.unlink()
    run(['hub/collect_gallery.py', '--host', host, '--out', str(field_raw)])
    rows = []
    if field_raw.exists():
        rows = [json.loads(l) for l in field_raw.read_text(encoding='utf-8').splitlines() if l.strip()]
    winners = [r for r in rows if r.get('is_winner')]
    print(f'  {len(rows)} submissions visible in the gallery, {len(winners)} ribboned')
    if not rows:
        print('  The gallery is unpublished or empty. That is a real state, not zero entries —\n'
              '  WebMCP\'s stayed unpublished through its deadline. Enumerate with\n'
              '  discover/search_sweep.py + verify/membership_check.py instead.')

    # 4 ── decompose this field
    field_facets = None
    if rows:
        full = work / 'field_full.jsonl'
        limit = a.deep or min(len(rows), 60)
        run(['hub/enrich_projects.py', '--in', str(field_raw), '--out', str(full),
             '--pages-dir', 'data/pages', '--limit', str(limit)])
        if full.exists():
            field_facets = work / 'field_facets.jsonl'
            fr = run(['hub/extract.py', '--in', str(full), '--out', str(field_facets)])
            tail = [l for l in fr.stdout.splitlines() if l.strip()]
            print(f'\n  read {limit} write-ups in full. What this field is made of:')
            for line in tail[-4:]:
                print('   ', line.strip())

    # 5 ── candidates
    rule('4 · CANDIDATES — proven elsewhere, absent here')
    brain = ROOT / a.brain
    if not brain.exists():
        print(f'  no brain at {brain}. Build it: hub/README.md')
        return 1
    cmd = ['hub/ideate.py', '--config', str(cfg_path), '--facets', str(brain),
           '--vault', 'vault', '--top', str(a.top)]
    if field_facets and Path(field_facets).exists():
        cmd += ['--field', str(field_facets)]
    else:
        print('  (no corpus for this field — "absent here" is measured against the whole\n'
              '   brain, which is much weaker evidence. Say so if you quote it.)\n')
    out = run(cmd)
    print(out.stdout.rstrip())

    rule('5 · NEXT')
    print("""  Nothing above is an idea yet. Zero occupancy is not evidence of a good idea —
  nobody may have done it because it is not attractive.

    position/IDEA-SELECTION.md   five tests; fail one and it is dead
    write/IMPACT.md              anchor the impact claim, never an unanchored magnitude
    write/WINNING-WRITEUPS.md    what the top of two fields actually writes
    build/TERMINAL.md            the demo, under the cap, in the first 15 seconds

  Candidate notes: vault/_candidates/  ·  gaps: vault/_gaps/""")
    return 0


if __name__ == '__main__':
    sys.exit(main())
