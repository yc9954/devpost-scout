#!/usr/bin/env python3
"""Resolve a hackathon by name and read everything it declares about itself.

This is the entry point: you know a name, you need a config. Devpost exposes a
keyless search API that maps a name to a host, and the host's `/rules` page
states the judging criteria verbatim — which is the one thing you must never
paraphrase, because the criteria are the rubric every judge scores against.

    python3 discover/hackathon.py --name "webmcp" --out config.json
    python3 discover/hackathon.py --host webmcp.devpost.com --out config.json

Two things this extracts that are easy to miss and decide placements:

* **Criterion order.** Devpost's standard tie-break is "the tied Submission with
  the highest score in the first applicable criterion listed above wins". At the
  top of a field scores bunch hard, so the first criterion is the tiebreaker and
  should get the disproportionate effort.
* **Whether the criteria are equally weighted**, stated or not. Assume nothing.
"""
import argparse
import json
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.fetch import Challenged, get                                # noqa: E402

SEARCH = 'https://devpost.com/api/hackathons?search={}'
TAG = re.compile(r'<[^>]+>')


def flat(html_text):
    import html as h
    text = re.sub(r'(?is)<(script|style).*?</\1>', ' ', html_text)
    return re.sub(r'\s+', ' ', h.unescape(TAG.sub(' ', text))).strip()


def search(name):
    """Name -> candidate hackathons, newest/most relevant first."""
    r = get(SEARCH.format(urllib.parse.quote_plus(name)))
    rows = json.loads(r['html']).get('hackathons', [])
    out = []
    for x in rows:
        out.append({
            'title': x.get('title'),
            'url': (x.get('url') or '').rstrip('/'),
            'host': urllib.parse.urlparse(x.get('url') or '').netloc,
            'state': x.get('open_state'),
            'dates': x.get('submission_period_dates'),
            'time_left': x.get('time_left_to_submission'),
            'prize': flat(x.get('prize_amount') or ''),
            'themes': [t.get('name') for t in x.get('themes', [])],
            'registrations': x.get('registrations_count'),
        })
    return out


# Criteria live on the hackathon's MAIN page under an <h*>Judging Criteria</h*>
# heading, as <li> items whose <strong> is the label. Verified identical on four
# unrelated hackathons. The /rules page is the fallback: many hackathons do not
# restate the criteria there at all, and some state them only as prose.
CRIT_HEAD = re.compile(r'(?is)<h\d[^>]*>\s*judging\s+criteria\s*</h\d>(.{0,8000})')
# Take only the first list after the heading. A fixed character window runs past
# the criteria and swallows the site footer nav — "About", "Careers", "Help" all
# arrived as judging criteria before this was scoped.
FIRST_LIST = re.compile(r'(?is)<(ul|ol)[^>]*>(.*?)</\1>')
LI = re.compile(r'(?is)<li[^>]*>(.*?)</li>')
STRONG = re.compile(r'(?is)<strong[^>]*>(.*?)</strong>')
PCT = re.compile(r'\(\s*(\d{1,3})\s*%\s*\)')
POINTS = re.compile(r'\(\s*(\d{1,3})\s*(?:points?|pts?)\s*\)', re.I)

# Fallback, prose form: "…judged on the following equally weighted criteria: Name : text…"
CRIT_LEAD = re.compile(
    r'judged on the following([^:]{0,120})criteria[^:]{0,200}:(.{80,3000}?)'
    r'(?=\d+\.\s+[A-Z]|Tie Breaking|Intellectual Property|$)', re.S | re.I)
CRIT_ITEM = re.compile(r'([A-Z][A-Za-z&/\'\u2019-]*(?:\s+[A-Z&][A-Za-z&/\'\u2019-]*){0,4})\s*:\s*')


def _mk(label, text, order):
    weight = None
    m = PCT.search(label) or PCT.search(text[:60])
    if m:
        weight = int(m.group(1))
    pts = POINTS.search(label) or POINTS.search(text[:60])
    label = PCT.sub('', label)
    label = POINTS.sub('', label).strip(' :\u2013-\u2014')
    return {
        'key': re.sub(r'[^a-z0-9]+', '_', label.lower()).strip('_'),
        'label': label,
        'text': re.sub(r'\s+', ' ', text).strip(' .;:'),
        'order': order,
        'weight_pct': weight,
        'max': int(pts.group(1)) if pts else None,
    }


def parse_criteria_page(page_html):
    """Primary route: the main page's Judging Criteria list."""
    head = CRIT_HEAD.search(page_html)
    if not head:
        return [], None
    window = head.group(1)
    lst = FIRST_LIST.search(window)
    block = lst.group(2) if lst else window
    crits = []
    for item in LI.findall(block):
        st = STRONG.search(item)
        if st:
            label = flat(st.group(1))
            text = flat(item[st.end():])
        else:                                    # no <strong>: first sentence is the label
            whole = flat(item)
            if not whole:
                continue
            label, _, text = whole.partition('.')
        if not label:
            continue
        crits.append(_mk(label, text, len(crits) + 1))
    if not crits:                                # some render <strong> siblings, not <li>
        for st in STRONG.finditer(window):
            label = flat(st.group(1))
            nxt = STRONG.search(window, st.end())
            text = flat(window[st.end():nxt.start() if nxt else st.end() + 600])
            if label:
                crits.append(_mk(label, text, len(crits) + 1))
    return crits, None


def parse_criteria_rules(rules_text):
    """Fallback: the /rules page's prose form."""
    m = CRIT_LEAD.search(rules_text)
    if not m:
        return [], None
    weighting = re.sub(r'\s+', ' ', m.group(1)).strip() or None
    blob = m.group(2)
    marks = list(CRIT_ITEM.finditer(blob))
    crits = []
    for i, mk in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(blob)
        text = blob[mk.end():end]
        if len(text.strip()) < 25:
            continue
        crits.append(_mk(mk.group(1).strip(), text, len(crits) + 1))
    return crits, weighting


def finalise(crits, weighting):
    """Fill in per-criterion maxima and say plainly how weighting was decided."""
    if not crits:
        return crits, weighting
    pcts = [c['weight_pct'] for c in crits if c['weight_pct'] is not None]
    if len(pcts) == len(crits) and abs(sum(pcts) - 100) <= 2:
        parts = ', '.join(f"{c['label']} {c['weight_pct']}%" for c in crits)
        weighting = f'weighted: {parts}'
        for c in crits:
            c['max'] = c['weight_pct']
    elif all(c['max'] for c in crits):
        weighting = weighting or f'stated points, total {sum(c["max"] for c in crits)}'
    else:
        weighting = weighting or 'not stated — assumed equal'
        share = round(100 / len(crits))
        for c in crits:
            c['max'] = c['max'] or share
    return crits, weighting


REQ_PATTERNS = {
    'video_max_minutes': r'(?:no longer than|less than|under|maximum of|up to)\s+(\w+)\s*\(?(\d+)?\)?\s*minutes',
    'video_must_be_public': r'video[^.]{0,120}(?:publicly visible|public)',
    'needs_public_url': r'(?:publicly accessible|working (?:URL|link)|live (?:URL|demo))',
    'needs_repo': r'(?:open source|public repository|source code)',
    'english_required': r'(?:must be|submitted) in English',
}


def parse_requirements(text):
    out = {}
    for key, pat in REQ_PATTERNS.items():
        m = re.search(pat, text, re.I)
        if not m:
            continue
        if key == 'video_max_minutes':
            words = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
            out[key] = int(m.group(2)) if m.group(2) else words.get(m.group(1).lower(), m.group(1))
        else:
            out[key] = True
    return out


def marker_from_title(title):
    """The literal Devpost renders in a project's #submissions block."""
    return title.strip()


def build(host, want_title=None):
    base = f'https://{host}'
    page = get(base)['html']
    rules_html = ''
    try:
        rules_html = get(base + '/rules')['html']
    except Challenged as exc:
        print(f'warning: /rules unreadable ({exc})', file=sys.stderr)

    title = want_title
    if not title:
        m = re.search(r'<title[^>]*>(.*?)</title>', page, re.S | re.I)
        title = flat(m.group(1)).split(':')[0].strip() if m else host

    rules_text = flat(rules_html)
    crits, weighting = parse_criteria_page(page)
    source = 'hackathon main page'
    if not crits:
        crits, weighting = parse_criteria_rules(rules_text)
        source = '/rules prose'
    if not crits:
        source = None
    crits, weighting = finalise(crits, weighting)
    reqs = parse_requirements(rules_text + ' ' + flat(page))

    prizes = [flat(x) for x in re.findall(r'class="prize-value"[^>]*>(.*?)</div>', page, re.S)]

    return {
        'hackathon_host': host,
        'hackathon_title': title,
        'membership_marker': marker_from_title(title),
        'primary_query': title.lower().replace('the ', '').split()[0] if title else '',
        'search_queries': [title.lower()],
        'criteria': crits,
        'criteria_weighting': weighting,
        'criteria_source': source,
        'tiebreak_criterion': crits[0]['label'] if crits else None,
        'requirements': reqs,
        'prizes': prizes[:6],
        'pillars': {},
        'chunk_size': 200,
        'text_cap_chars': 3800,
        'cdp_port': 9333,
        'notes': ('criteria are verbatim from /rules — never paraphrase them into a judge prompt. '
                  'tiebreak_criterion is the first-listed criterion, which Devpost’s standard '
                  'tie-break rule resolves ties on. pillars is yours to fill after positioning.'),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--name', help='hackathon name to search for')
    g.add_argument('--host', help='exact host, e.g. webmcp.devpost.com')
    ap.add_argument('--out', help='write config JSON here (default: stdout)')
    ap.add_argument('--pick', type=int, default=None,
                    help='choose the Nth search result (1-based) without prompting')
    a = ap.parse_args()

    host, title = a.host, None
    if a.name:
        hits = search(a.name)
        if not hits:
            sys.exit(f'no hackathon matched {a.name!r}')
        if len(hits) > 1 and a.pick is None:
            print(f'{len(hits)} matches — re-run with --pick N\n', file=sys.stderr)
            for i, h in enumerate(hits, 1):
                print(f'  {i}. {h["title"]}  [{h["state"]}]  {h["dates"]}  {h["host"]}',
                      file=sys.stderr)
            sys.exit(2)
        pick = hits[(a.pick or 1) - 1]
        host, title = pick['host'], pick['title']
        print(f'→ {pick["title"]}  [{pick["state"]}]  {pick["dates"]}', file=sys.stderr)

    cfg = build(host, title)
    text = json.dumps(cfg, ensure_ascii=False, indent=2)
    if a.out:
        Path(a.out).write_text(text, encoding='utf-8')
        print(f'wrote {a.out}', file=sys.stderr)
    else:
        print(text)

    if not cfg['criteria']:
        print('\n⚠  no criteria parsed — open the /rules page and fill them in by hand. '
              'Everything downstream scores against them.', file=sys.stderr)
    else:
        print(f'\n{len(cfg["criteria"])} criteria, {cfg["criteria_weighting"] or "weighting unstated"}. '
              f'Tiebreak: {cfg["tiebreak_criterion"]}', file=sys.stderr)


if __name__ == '__main__':
    main()
