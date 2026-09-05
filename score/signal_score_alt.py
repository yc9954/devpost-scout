import json, re
from pathlib import Path
D = Path('/private/tmp/claude-501/-Users-ax-toolsmith/agent-census')
rows = json.loads((D/'new_submissions_parsed.json').read_text())

SIGNALS = {
 'runtime_registration': r'register(?:Tool|_tool)|registerTool|navigator\.modelContext|window\.modelContext|document\.modelContext|at runtime|dynamically registers?|tools? (?:are |get )?registered',
 'structural_withholding': r'withhold|redact|never (?:returns?|exposes?|sends?)|omit(?:s|ted)? (?:the )?field|structurally (?:cannot|can\'t)|scrub|masked?|schema (?:refuses|forbids|prevents)|the tool cannot return|out of schema',
 'human_approved_writes': r'human[- ]in[- ]the[- ]loop|confirm(?:ation)? (?:step|dialog|before)|requires? (?:a )?(?:human|user) (?:approval|confirmation|consent)|approve[sd]? (?:the )?(?:write|action|change)|never writes? without|user must confirm|two[- ]step confirm',
 'cross_origin': r'cross[- ]origin|iframe|postMessage|third[- ]party (?:page|site)|another (?:site|origin)|federat',
 'measured_benchmark': r'benchmark|we measured|median of \d|\d+ ?(?:runs|trials)|ablation|p50|p95|success rate of \d|accuracy of \d|n ?= ?\d+',
 'teach_by_demo': r'by demonstration|demonstrat(?:e|ing) (?:their|the|your) own|record(?:s|ing|ed)? (?:the |a )?(?:user\'?s )?(?:actions|steps|workflow)|teach(?:es|ing)? (?:the )?(?:page|site|agent) (?:a |the )?new tool|non[- ]?(?:technical|developer|coder)|without writing (?:any )?code|end users? (?:can )?(?:create|define|author|build) (?:a |their own )?tools?|user[- ]authored tools?|tool from (?:a )?demonstration',
}
def blob(r):
    return ' '.join([r['title'], r['tagline'], r['description']] + r['built_with'] + list(r['sections'].values()))

out = []
for r in rows:
    t = blob(r)
    hits = {k: len(re.findall(p, t, re.I)) for k, p in SIGNALS.items()}
    has_repo = bool(r['repo_urls']); has_live = bool(r['live_urls'])
    has_vid = bool(r['video_urls'] or r['youtube_embed_ids'])
    words = r['description_words']
    score = (2*has_repo + 2*has_live + 2*has_vid + min(words,2000)/400
             + sum(2 for k,v in hits.items() if v) + min(hits['teach_by_demo'],3))
    out.append({'slug': r['slug'], 'title': r['title'], 'tagline': r['tagline'],
                'score': round(score,2), 'words': words, 'repo': has_repo, 'live': has_live,
                'video': has_vid, 'hits': hits, 'signals': sum(1 for v in hits.values() if v)})
out.sort(key=lambda x: -x['score'])
json.dump(out, open(D/'new_scored.json','w'), ensure_ascii=False, indent=1)
print(f"{'score':>6} {'sig':>3} {'w':>5} rlv  slug")
for x in out[:35]:
    print(f"{x['score']:6.2f} {x['signals']:3d} {x['words']:5d} {'R' if x['repo'] else '-'}{'L' if x['live'] else '-'}{'V' if x['video'] else '-'}  {x['slug'][:48]:48s} {x['title'][:40]}")
print()
print('teach_by_demo hits:', sum(1 for x in out if x['hits']['teach_by_demo']))
print('all six signals:', sum(1 for x in out if x['signals']==6))
