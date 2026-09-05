#!/usr/bin/env python3
"""
Of the entries that create tools at runtime, who decides the shape of the tool?

field_position.py counts how many entries *say* they create tools at runtime.
That is the crowded question and the answer is somewhere between sixty and
ninety. This is the question underneath it, and the one this project's claim
actually rests on: a tool made at runtime still has a name, parameters,
defaults and limits, and somebody decides them.

This script selects the entries to ask about and writes them out for
classification. It does not do the classifying — that is a reading, not a
regex, and it is recorded in authorship.md with the sentence that decided each
one, so a reader can disagree entry by entry.

  cd webmcp-evaluator && python3 authorship_check.py
"""
import json
import re
from pathlib import Path

ROWS = json.loads(Path('data/submissions_enriched.json').read_text())

CREATES = (
    r'(mint|forge|generate|create|compose|author)\w*\s+(a\s+)?(new\s+)?tool'
    r'|tool that did ?n.?t exist|not in the source|registers? a new tool'
    r'|dynamic(ally)?\s+(register|registration|generat|creat|add)\w*'
    r'|tools?\s+(appear|are added|are created|are generated|show up|materiali[sz]e)'
    r'|register\w*\s+tools?\s+(at|on)\s+runtime'
    r'|runtime\s+tool\s+(creation|registration|generation)'
    r'|(new|extra|additional)\s+tools?\s+(appear|become available|are registered)'
    r'|tool\s+surface\s+(grows|changes|expands)'
    r'|at runtime.{0,30}tool|tool.{0,30}at runtime'
    # The phrasing that hid the counterexample: a verb of transformation with
    # "tool" somewhere after it rather than immediately beside it. Understudy
    # writes "turns that demonstration into a WebMCP tool" and the earlier
    # pattern could not see it, which is how a uniqueness claim survived being
    # false.
    r'|(turn|convert|generalis|generaliz|compile|promote|distil|record)\w*'
    r'.{0,60}\binto\b.{0,40}\btool'
    r'|\btool\b.{0,60}\bfrom\b.{0,40}(demonstration|recording|trace|what you did)'
    r'|teach\w*\s+(the\s+)?(page|site|app).{0,40}tool'
    r'|(demonstration|recording|trace)\s+becomes?\s+a?\s*tool'
)

# Who the shape comes from. E is the only one this project claims, and it is
# the one to be strictest about: the author is not a developer, they are doing
# their own work rather than building for others, and what they express decides
# the tool's shape rather than triggering a tool somebody else shaped.
BUCKETS = {
    'A': 'a developer, in code or config',
    'B': 'an agent or model',
    'C': 'an imported OpenAPI document, MCP server or marketplace row',
    'D': 'derived from the page itself — its DOM, forms, schema or routes',
    'E': 'an end user who is not a developer, expressing their own work',
    'F': 'not determinable from the text',
}


def text(row):
    return ' '.join(str(row.get(k) or '') for k in ('title', 'tagline', 'description'))


def main():
    hits = [r for r in ROWS if re.search(CREATES, text(r), re.I)]
    out = [{'id': r['slug'], 'title': r['title'],
            'tagline': (r.get('tagline') or '')[:200],
            'text': re.sub(r'\s+', ' ', str(r.get('description') or ''))[:3000]}
           for r in hits]
    Path('data/authorship_check.json').write_text(json.dumps(out, ensure_ascii=False))
    print(f'{len(hits)} of {len(ROWS)} entries describe creating a tool at runtime')
    print('written to data/authorship_check.json for classification')
    print()
    for key, label in BUCKETS.items():
        print(f'  {key}  {label}')
    print()
    print('The reading, with the sentence that decided each entry, is in authorship.md.')


main()
