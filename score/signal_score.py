#!/usr/bin/env python3
"""Rank newly-found confirmed submissions by the same signals used in field_position.py."""
import json, re, os, sys

CLAIMS = {
 'runtime_tool_creation': (r'(mint|forge|generate|create|compose|author)\w*\s+(a\s+)?(new\s+)?tool'
   r'|tool that did ?n.?t exist|not in the source|registers? a new tool'
   r'|dynamic(ally)?\s+(register|registration|generat|creat|add)\w*'
   r'|tools?\s+(appear|are added|are created|are generated|show up)'
   r'|register\w*\s+tools?\s+(at|on)\s+runtime|runtime\s+tool\s+(creation|registration|generation)'
   r'|at runtime.{0,30}tool|tool.{0,30}at runtime'
   r'|(turn|convert|generalis|generaliz|compile|promote|distil|record)\w*.{0,60}\binto\b.{0,40}\btool'
   r'|\btool\b.{0,60}\bfrom\b.{0,40}(demonstration|recording|trace|what you did)'
   r'|teach\w*\s+(the\s+)?(page|site|app).{0,40}tool'
   r'|(demonstration|recording|trace)\s+becomes?\s+a?\s*tool'),
 'from_demonstration': r'demonstrat\w+.{0,40}(tool|record)|record\w*.{0,30}demonstrat|teach (it|the page)|by example|show(ing)? it once|watch(es|ed)? (you|the user) (do|perform)',
 'structural_withholding': r'withh(o|e)ld|redact|never (leaves|sees|reads)|cannot (see|read)|structurally (cannot|can not)|policy.{0,30}(denies|refuses|withholds)',
 'tool_withdrawal': r'(unregister|withdraw|revoke)\w*\s+(the\s+)?tool|fingerprint',
 'human_in_the_loop': r'human (in the loop|approval|confirm)|requires? (human|user) (approval|confirmation)|waits? for (a person|the user)|user must (approve|confirm)',
 'measured_ablation': r'ablation|counterfactual|removed the (policy|guard)|without the (policy|engine|guard)|a/b|baseline.{0,40}(trials|runs)',
 'cross_origin': r'cross-origin|iframe|opaque origin|postmessage|third-party (page|site)',
 'benchmark': r'\b\d{1,3}(\.\d+)?%\s|(\d+)\s*/\s*(\d+)\s*(trials|runs|tasks)|benchmark|evaluated? on \d+',
}
REPO = re.compile(r'github\.com|gitlab\.com|bitbucket\.org', re.I)
VIDEO = re.compile(r'youtu\.?be|vimeo|loom\.com', re.I)

rows = [json.loads(l) for l in open(sys.argv[1])]
out = []
for r in rows:
    if not r.get('ok') or not r.get('webmcp'):
        continue
    txt = ''
    p = os.path.join('dumps', r['slug'] + '.txt')
    if os.path.exists(p):
        txt = open(p, encoding='utf-8', errors='replace').read()
    blob = (r['title'] + ' ' + r['tagline'] + ' ' + txt).lower()
    links = r.get('links') or []
    repo = [l for l in links if REPO.search(l)]
    video = r.get('video') or any(VIDEO.search(l) for l in links) or bool(VIDEO.search(txt))
    live = [l for l in links if not REPO.search(l) and not VIDEO.search(l)
            and 'devpost.com' not in l and l.startswith('http')]
    hits = {k: bool(re.search(v, blob, re.I)) for k, v in CLAIMS.items()}
    score = (2 * bool(repo) + 2 * bool(live) + 2 * bool(video)
             + 3 * (len(txt) > 2000) + 2 * (len(txt) > 6000) + sum(hits.values()))
    out.append({'slug': r['slug'], 'title': r['title'], 'tagline': r['tagline'][:160],
                'score': score, 'chars': len(txt), 'repo': repo[:1], 'live': live[:1],
                'video': video, 'hits': [k for k, v in hits.items() if v]})
out.sort(key=lambda x: -x['score'])
json.dump(out, open('ranked.json', 'w'), indent=1)
print('confirmed new:', len(out))
for x in out[:40]:
    print(f"{x['score']:>3} {x['chars']:>6}c {'R' if x['repo'] else '-'}{'L' if x['live'] else '-'}{'V' if x['video'] else '-'} {x['slug'][:44]:<44} {len(x['hits'])} {','.join(h[:9] for h in x['hits'])}")
