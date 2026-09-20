#!/usr/bin/env python3
"""Extract the transferable unit from a write-up: the claim, and the problem.

The facet graph collapses: 66% of 8,636 projects share an identical
mechanism/domain signature and the largest single signature holds 1,341 of them.
At that resolution nothing new can come out, because the graph cannot tell those
1,341 apart.

What actually transfers between domains is not `deterministic_policy x
supply_logistics`. It is a sentence — *"a tool that does not exist is stronger
than a tool that refuses"* — and the condition it answers — *"the approval
happens after the fact"*. Those are the node types missing from the graph, and
regex cannot find them: a sentence-pattern sweep over 2,487 long write-ups fired
on 8-34% of them and returned mostly noise ("instead of lithium batteries",
"currently an AI intern at Amazon Alexa"). Roughly one in five was usable.

So this is an LLM extractor, aimed at the entries where the signal is worth the
cost — the biggest hackathons' winners with substantial write-ups.

    export ANTHROPIC_API_KEY=...
    python3 hub/claims.py --targets data/llm_targets.json --out data/claims.jsonl

Three ways to run it, in order of what is usually available:

    python3 hub/claims.py --emit 40          # condensed write-ups for the model
                                             # already in the session to read
    python3 hub/claims.py --append rows.json # write back what it extracted
    ANTHROPIC_API_KEY=... python3 hub/claims.py   # unattended, over the API

The `--emit` / `--append` pair exists because an API key is not the constraint
when a model is already reading this repository. It is the obvious way to run
this and it was nearly missed.
"""
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

MODEL = 'claude-sonnet-5'
BODY_CAP = 9000

PROMPT = """You are building a graph of hackathon ideas. For ONE project, extract the
units that transfer to other domains. Be terse and concrete. Never invent.

Return ONLY minified JSON, no prose, with exactly these keys:

{"claim": "...", "problem": "...", "mechanism": "...", "beneficiary": "...",
 "transfers_to": ["...", "..."], "evidence_kind": "...", "confidence": 0.0}

claim        The one structural insight, as a sentence that would still make sense
             in a different industry. Strip the product name and the domain.
             Good: "a capability that is absent cannot be misused, only a refusal can be argued with"
             Bad:  "Placard checks chemical segregation rules"  (that is a description)
problem      The recurring condition it answers, stated so another field would
             recognise it. Good: "the person doing the work cannot change the tool they are given"
             Bad:  "hazmat shipping is complicated"
mechanism    The concrete technical move, 2-6 words. e.g. "withhold field at schema level"
beneficiary  Who is spared the problem, 1-4 words. e.g. "shift nurse", "small landlord"
transfers_to 1-3 OTHER domains where this exact problem recurs. Industries, not features.
evidence_kind One of: ablation | benchmark | cited-dataset | named-partner | user-study |
             concrete-instance | none
confidence   0.0-1.0, how clearly the write-up actually states a claim rather than
             you inferring one. Below 0.4 means the write-up has no real claim —
             say so with an empty claim rather than manufacturing one.

PROJECT: <<TITLE>>
TAGLINE: <<TAGLINE>>
WRITE-UP:
<<BODY>>
"""


def build_prompt(row):
    # str.format is unusable here: the prompt shows a JSON schema, and every brace
    # in it would be read as a field name.
    return (PROMPT
            .replace('<<TITLE>>', row.get('title') or '')
            .replace('<<TAGLINE>>', row.get('tagline') or '')
            .replace('<<BODY>>', re.sub(r'\s+', ' ', row.get('description') or '')[:BODY_CAP]))


SECTION_START = re.compile(
    r'(?i)\b(inspiration|the problem|why (?:we|i) built|what it does|the challenge)\b')


def salient(row, cap):
    """The part of a write-up where the claim actually lives.

    Devpost bodies open with the gallery image captions — "Landing page Home
    Dashboard Settings" — which carry no argument and were eating most of the
    budget. The claim is almost always in Inspiration or the problem statement,
    so start there and fall back to the top only when neither is present.
    """
    text = re.sub(r'\s+', ' ', row.get('description') or '')
    m = SECTION_START.search(text)
    start = m.start() if m and m.start() < len(text) * 0.6 else 0
    return text[start:start + cap]


def parse_reply(text):
    m = re.search(r'\{.*\}', text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--full', default='data/projects_full.jsonl')
    ap.add_argument('--targets', default='data/llm_targets.json')
    ap.add_argument('--out', default='data/claims.jsonl')
    ap.add_argument('--batch-dir', default='data/claim_batches')
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--model', default=MODEL)
    ap.add_argument('--batch-size', type=int, default=20,
                    help='projects per prompt file when there is no API key')
    ap.add_argument('--emit', type=int, default=0,
                    help='print N not-yet-extracted write-ups, condensed, for a model '
                         'already in the session to read directly')
    ap.add_argument('--emit-chars', type=int, default=1500)
    ap.add_argument('--all', action='store_true',
                    help='target every parsed write-up, not just --targets')
    ap.add_argument('--min-words', type=int, default=0)
    ap.add_argument('--max-words', type=int, default=0)
    ap.add_argument('--order', choices=['targets', 'longest', 'shortest'], default='targets',
                    help='longest first puts the highest-yield write-ups early: measured '
                         'claim rate is 41-44%% above 700 words and 11-17%% below 400')
    ap.add_argument('--append', help='JSON file of extracted rows to append to --out')
    a = ap.parse_args()

    bodies = {}
    for line in Path(a.full).read_text(encoding='utf-8').splitlines():
        if line.strip():
            r = json.loads(line)
            if not r.get('error'):
                bodies[r['slug']] = r
    if a.all:
        targets = list(bodies)
    else:
        targets = json.loads(Path(a.targets).read_text(encoding='utf-8'))
    done = set()
    out = Path(a.out)
    if out.exists():
        for line in out.read_text(encoding='utf-8').splitlines():
            if line.strip():
                done.add(json.loads(line).get('slug'))
    todo = [s for s in targets if s in bodies and s not in done]

    def wc(slug):
        return bodies[slug].get('description_words') or 0

    if a.min_words:
        todo = [s for s in todo if wc(s) >= a.min_words]
    if a.max_words:
        todo = [s for s in todo if wc(s) < a.max_words]
    if a.order == 'longest':
        todo.sort(key=lambda s: -wc(s))
    elif a.order == 'shortest':
        todo.sort(key=wc)
    if a.limit:
        todo = todo[:a.limit]
    print(f'{len(todo)} to extract ({len(done)} already done)', file=sys.stderr)

    if a.append:
        rows = json.loads(Path(a.append).read_text(encoding='utf-8'))
        with out.open('a', encoding='utf-8') as fh:
            n = 0
            for r in rows:
                if not r.get('slug') or r['slug'] in done:
                    continue
                src = bodies.get(r['slug'], {})
                r.setdefault('title', src.get('title'))
                r.setdefault('hackathon_title', src.get('hackathon_title'))
                r.setdefault('source', 'session')
                fh.write(json.dumps(r, ensure_ascii=False) + '\n')
                n += 1
        total = sum(1 for _ in out.open(encoding='utf-8'))
        print(f'appended {n} -> {out} ({total} total, {len(targets)} targeted)')
        return 0

    if a.emit:
        for slug in todo[:a.emit]:
            b = bodies[slug]
            body = salient(b, a.emit_chars)
            print(f'--- {slug} | {b.get("title")} | {b.get("hackathon_title")}')
            print(f'TAG: {(b.get("tagline") or "")[:160]}')
            print(f'{body}\n')
        print(f'### {min(a.emit, len(todo))} emitted, {len(todo)} still unextracted',
              file=sys.stderr)
        return 0

    key = os.environ.get('ANTHROPIC_API_KEY')
    if not key:
        d = Path(a.batch_dir)
        d.mkdir(parents=True, exist_ok=True)
        for i in range(0, len(todo), a.batch_size):
            chunk = todo[i:i + a.batch_size]
            payload = [{'slug': s, 'prompt': build_prompt(bodies[s])} for s in chunk]
            (d / f'batch_{i // a.batch_size:04d}.json').write_text(
                json.dumps(payload, ensure_ascii=False, indent=1), encoding='utf-8')
        print(f'no ANTHROPIC_API_KEY — wrote {len(todo)} prompts to {d}/ instead.\n'
              f'Any model can process a batch file and append {{"slug":..., ...}} '
              f'lines to {a.out}.')
        return 0

    import anthropic
    client = anthropic.Anthropic(api_key=key)
    fh = out.open('a', encoding='utf-8')
    ok = bad = 0
    for i, slug in enumerate(todo, 1):
        try:
            resp = client.messages.create(
                model=a.model, max_tokens=700,
                messages=[{'role': 'user', 'content': build_prompt(bodies[slug])}])
            parsed = parse_reply(resp.content[0].text)
        except Exception as exc:                                  # noqa: BLE001
            print(f'{slug}: {exc}', file=sys.stderr)
            time.sleep(3)
            continue
        if not parsed:
            bad += 1
            continue
        parsed['slug'] = slug
        parsed['title'] = bodies[slug].get('title')
        parsed['hackathon_title'] = bodies[slug].get('hackathon_title')
        fh.write(json.dumps(parsed, ensure_ascii=False) + '\n')
        fh.flush()
        ok += 1
        if i % 25 == 0:
            print(f'{i}/{len(todo)}  ok={ok} unparsed={bad}', flush=True)
    fh.close()
    print(f'\n{ok} extracted, {bad} unparseable -> {out}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
