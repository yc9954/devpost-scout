#!/usr/bin/env python3
"""Split a verified corpus into equal slices for parallel LLM triage.

One agent cannot judge 2,000 entries; twelve agents judging 200 each can. The
cost of that is inter-rater spread, which is real and large — see PITFALLS.md.
Mitigate it by (a) giving every judge the identical rubric and calibration
anchors, and (b) deliberately double-judging one slice so you can measure the
spread instead of guessing at it.

    python3 score/make_chunks.py --config config.json --in corpus.json --out-dir judge/
"""
import argparse
import json
import re
from pathlib import Path


def clean(s, cap):
    return re.sub(r'\s+', ' ', s or '').strip()[:cap]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--config', default='config.json')
    ap.add_argument('--in', dest='inp', required=True,
                    help='JSON list with slug/title/tagline/description/live_urls/repo_urls/video_urls')
    ap.add_argument('--out-dir', required=True)
    ap.add_argument('--double-judge', type=int, default=None,
                    help='also emit this chunk as chunk_NNb.json, to measure judge spread')
    a = ap.parse_args()
    cfg = json.load(open(a.config))
    cap, size = cfg.get('text_cap_chars', 3800), cfg.get('chunk_size', 200)

    rows = []
    for r in json.load(open(a.inp)):
        rows.append({
            'slug': r['slug'],
            'title': r.get('title', ''),
            'tagline': clean(r.get('tagline', ''), 300),
            'live': bool(r.get('live_urls') or r.get('live')),
            'repo': bool(r.get('repo_urls') or r.get('repo')),
            'video': bool(r.get('video_urls') or r.get('youtube_embed_ids') or r.get('video')),
            'chars': len(r.get('description') or r.get('text') or ''),
            'text': clean(r.get('description') or r.get('text', ''), cap),
        })
    rows.sort(key=lambda r: r['slug'])          # stable, reproducible slices
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    n = (len(rows) + size - 1) // size
    for i in range(n):
        part = rows[i * size:(i + 1) * size]
        p = out / f'chunk_{i:02d}.json'
        p.write_text(json.dumps(part, ensure_ascii=False))
        # A judge that reads the wrong file is a silent, total loss. Print the
        # bookends so the agent prompt can carry them as a sanity check.
        print(f'{p.name}  {len(part):>4} rows  first={part[0]["slug"]}  last={part[-1]["slug"]}')
    if a.double_judge is not None:
        src = out / f'chunk_{a.double_judge:02d}.json'
        (out / f'chunk_{a.double_judge:02d}b.json').write_text(src.read_text())
        print(f'\ndouble-judge copy: chunk_{a.double_judge:02d}b.json (same rows, second judge)')


if __name__ == '__main__':
    main()
