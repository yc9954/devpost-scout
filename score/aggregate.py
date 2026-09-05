#!/usr/bin/env python3
"""Turn per-slice judge reports into one ranking, and say how uncertain it is.

Judges only report their own top 15, so you never get a full 2,000-row ranking.
What you get is: (a) a per-slice count of how many cleared each band, and (b)
the identity and score of the best in each slice. That is enough to place any
one entry, which is usually the question.

    python3 score/aggregate.py --results results.tsv --dist dist.tsv --me my-slug
"""
import argparse
import csv
import statistics
from collections import defaultdict


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--results', required=True, help='TSV: chunk slug L E I C total')
    ap.add_argument('--dist', required=True, help='TSV: chunk 80plus 70_79 60_69 50_59 under50')
    ap.add_argument('--me', help='slug to locate in the field')
    ap.add_argument('--slices', type=int, default=None, help='total slices, if some are missing')
    a = ap.parse_args()

    rows = [r for r in csv.DictReader(open(a.results), delimiter='\t') if r['chunk'] != 'chunk']
    dist = [r for r in csv.DictReader(open(a.dist), delimiter='\t') if r['chunk'] != 'chunk']

    # A chunk suffixed 'b' is the deliberate double-judge. Use it for spread, not for ranking.
    main_rows = [r for r in rows if not r['chunk'].endswith('b')]
    dup_rows = [r for r in rows if r['chunk'].endswith('b')]
    seen = {r['slug']: int(r['total']) for r in main_rows}

    n_slices = a.slices or len({r['chunk'] for r in dist if not r['chunk'].endswith('b')})
    band80 = sum(int(r['80plus']) for r in dist if not r['chunk'].endswith('b'))
    total_entries = sum(int(r[k]) for r in dist if not r['chunk'].endswith('b')
                        for k in ('80plus', '70_79', '60_69', '50_59', 'under50'))

    print(f'slices judged      {n_slices}')
    print(f'entries judged     {total_entries}')
    print(f'scored 80+         {band80}   ({band80/total_entries*100:.1f}% of the field)')
    print(f'reported rows      {len(seen)}  (each judge reports only its top 15)')

    if dup_rows:
        b = {r['slug']: int(r['total']) for r in dup_rows}
        both = sorted(set(seen) & set(b))
        if both:
            d = [seen[s] - b[s] for s in both]
            print(f'\n-- inter-rater spread, {len(both)} entries judged twice --')
            for s in both:
                print(f'   {s[:46]:48} {seen[s]:>3} vs {b[s]:>3}   {seen[s]-b[s]:+d}')
            print(f'   mean {statistics.mean(d):+.1f}   range {min(d):+d}..{max(d):+d}')
            print('   Quote your rank as a band this wide, never as a number.')

    print('\n-- field top 20 (as reported) --')
    for i, (s, v) in enumerate(sorted(seen.items(), key=lambda x: -x[1])[:20], 1):
        print(f'{i:>3}  {v}  {s}')

    if a.me:
        mine = seen.get(a.me)
        if mine is None:
            print(f'\n{a.me} is not in any reported top-15.')
            return
        above = sum(1 for v in seen.values() if v > mine)
        # Judges report ~15 rows each; scale the "above me" count to the real 80+ band.
        est = round(band80 * above / len(seen)) if len(seen) else above
        print(f'\n-- {a.me} --')
        print(f'score {mine}   above it among reported {above}/{len(seen)}')
        print(f'estimated rank ~{est+1} of {total_entries}  (top {(est+1)/total_entries*100:.1f}%)')
        print('This is a point estimate on top of a judge spread of several points.')


if __name__ == '__main__':
    main()
