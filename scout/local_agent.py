"""Local mode: a deterministic router over the same tools, emitting the same SSE
event sequence as Claude mode. Prose is templated, numbers come from tool results."""
import re
import uuid

from scout import config, tools

STOP = {'the', 'a', 'an', 'of', 'for', 'about', 'on', 'in', 'with', 'that', 'to', 'and', 'or',
        'me', 'show', 'find', 'list', 'which', 'what', 'are', 'is', 'any', 'some', 'please',
        'projects', 'project', 'winners', 'winner', 'winning', 'past', 'won', 'hackathon',
        'hackathons', 'vault', 'note', 'notes', 'gap', 'gaps', 'mechanism', 'mechanisms',
        'domain', 'domains', 'substrate', 'substrates'}

_HOST = re.compile(r'([a-z0-9-]+\.devpost\.com)', re.I)
_BRIEF_VERB = re.compile(
    r'^\s*(?:please\s+|can you\s+|could you\s+)?'
    r'(?:scout|brief|research|analy[sz]e|look at|check(?: out)?|study|resolve)\s+(.+)$',
    re.I | re.S)
_BUILD = re.compile(
    r'(?:what (?:should|could|can) (?:i|we) (?:build|make|enter)|what to build|ideas?|ideate|'
    r'propose|suggest(?:ions?)?|candidates?)\s+(?:for|in|at)\s+(.+)$', re.I | re.S)
_RUBRIC = re.compile(
    r'(?:rubric|criteria|criterion|rules|requirements|judging|prizes?|tie-?break)\s+'
    r'(?:of|for|in|at|on)\s+(.+)$', re.I | re.S)
_WINNERS = re.compile(r'\b(winners?|winning|won|past projects|prior projects)\b', re.I)
_VAULT = re.compile(r'\b(mechanisms?|domains?|gaps?|vault|substrates?|convergences?)\b', re.I)
_STATS = re.compile(r'\b(stats|statistics|how many|census|overview|numbers|breakdown)\b', re.I)
_LIST = re.compile(r'\b(open|upcoming|ending|ends?|deadlines?|prizes?|closing|soon|this week|'
                   r'next week|biggest|largest|richest|popular|hackathons?|running|live)\b', re.I)
_HELP = re.compile(r'^\s*(help|hi|hello|hey|what can you do|\?)\s*[?!.]*\s*$', re.I)
_IDEA_WORDS = re.compile(r'\b(build|ideas?|ideate|propose|suggest|candidates?|scout)\b', re.I)


def _clean_name(s):
    s = re.sub(r'https?://', '', s or '').strip().strip('"\'“”‘’ ').rstrip('?.!,;:')
    s = re.sub(r'^(?:the\s+)?(?:hackathon\s+)?', '', s, flags=re.I)
    s = re.sub(r'\s+(?:hackathon|please)$', '', s, flags=re.I)
    return s.strip()


def _theme_in(text):
    low = text.lower()
    best = None
    try:
        themes = tools.store().stats()['themes_all']
    except Exception:                                                # noqa: BLE001
        themes = []
    for t in themes:
        for part in re.split(r'[/,]', t):
            p = part.strip().lower()
            if len(p) > 2 and re.search(r'\b' + re.escape(p) + r's?\b', low):
                if best is None or len(p) > len(best[0]):
                    best = (p, t)
    return best[1] if best else ''


def _keywords(text):
    return ' '.join(t for t in re.findall(r'[a-z0-9]+', text.lower()) if t not in STOP)


def _after_prep(text):
    m = re.search(r'\b(?:about|on|for|with|regarding|related to|around)\s+(.+)$', text, re.I | re.S)
    return m.group(1) if m else text


def route(text):
    """-> {'intent', 'calls': [(tool, input)], 'name'?}. Pure, no tool execution."""
    t = (text or '').strip()
    if not t or _HELP.match(t):
        return {'intent': 'help', 'calls': []}

    host = _HOST.search(t)
    wants_ideas = bool(_IDEA_WORDS.search(t))
    name = None
    for rx in (_BUILD, _RUBRIC, _BRIEF_VERB):
        m = rx.search(t)
        if m:
            name = _clean_name(m.group(1))
            break
    if host:
        name = host.group(1).lower()
    if name:
        calls = [('hackathon_brief', {'name_or_url': name})]
        if wants_ideas:
            calls.append(('ideate', {'host': None}))          # host filled from the brief
        return {'intent': 'brief+ideate' if wants_ideas else 'brief', 'calls': calls, 'name': name}

    if _WINNERS.search(t):
        q = _keywords(_after_prep(t))
        if q:
            return {'intent': 'winners', 'calls': [('search_winners', {'query': q, 'limit': 12})]}

    if _VAULT.search(t):
        m = _VAULT.search(t)
        word = m.group(1).lower()
        kind = ('gap' if word.startswith('gap') else 'mechanism' if word.startswith('mech')
                else 'domain' if word.startswith('dom') else 'any')
        q = _keywords(re.sub(r'[×x]\s', ' ', _after_prep(t)))
        if q:
            return {'intent': 'vault', 'calls': [('vault_lookup', {'query': q, 'kind': kind})]}

    if _STATS.search(t):
        return {'intent': 'stats', 'calls': [('census_stats', {})]}

    if _LIST.search(t):
        low = t.lower()
        status = ('upcoming' if 'upcoming' in low else
                  'ended' if re.search(r'\b(ended|past|closed|finished)\b', low) else 'open')
        sort = ('prize' if re.search(r'\b(prize|prizes|richest|biggest|largest|money)\b', low)
                else 'registrations' if re.search(r'\b(popular|registrations|crowded)\b', low)
                else 'deadline')
        return {'intent': 'list', 'calls': [('list_hackathons', {
            'status': status, 'sort': sort, 'theme': _theme_in(t), 'limit': 10})]}

    return {'intent': 'help', 'calls': []}


HELP = """I'm running in **local mode** (no `ANTHROPIC_API_KEY`), so I route your message to one tool by rule and reply with the numbers it returns. Try:

- **What's open this week?** / *upcoming hackathons by prize* → `list_hackathons`
- **Scout RevenueCat Shipaton 2026** / *rubric of webmcp.devpost.com* → `hackathon_brief` (+ `ideate` when you ask what to build)
- **Winners about agents for accessibility** → `search_winners` (a shortlist, never a ranking)
- **Gaps in health × voice** / *mechanism retrieval grounding* → `vault_lookup`
- **How many hackathons are open?** → `census_stats`

Everything I say is measured from the census of {census} or quoted from Devpost."""


# ------------------------------------------------------------------------------------
# prose templates
# ------------------------------------------------------------------------------------
def _money(n):
    return f'${n:,.0f}' if n else '—'


def _hackathon_lines(rows):
    out = []
    for i, c in enumerate(rows, 1):
        when = (f'ends {c["end"]} ({c["days_left"]}d left)' if c['status'] == 'open' and c['days_left'] is not None
                else f'opens {c["start"]}' if c['status'] == 'upcoming' else f'ended {c["end"]}')
        themes = ', '.join(c['themes'][:3]) or 'no themes'
        out.append(f'{i}. **[{c["title"]}]({c["url"]})** — {c["org"] or "unknown host"} · {when} · '
                   f'{_money(c["prize_usd"])} · {c["registrations"]:,} registered · {themes}')
    return '\n'.join(out)


def prose_list(res, inp):
    d = res['data']
    rows, total = d['rows'], d['total']
    status = inp.get('status', 'open')
    if not rows:
        return (f'No **{status}** hackathons match in the census of {d["census_date"]}. '
                f'Status is derived from each page\'s submission dates against today '
                f'({config.today().isoformat()}); a stale census undercounts what opened since.')
    within7 = sum(1 for c in rows if c['status'] == 'open' and c['days_left'] is not None and c['days_left'] <= 7)
    pool = sum(c['prize_usd'] for c in rows)
    head = (f'**{total} {status} hackathon{"s" if total != 1 else ""}** in the census of '
            f'{d["census_date"]}' + (f', theme *{inp["theme"]}*' if inp.get('theme') else '') +
            f'. Showing {len(rows)} by {inp.get("sort", "deadline")}')
    if status == 'open':
        head += f'; {within7} of these close within 7 days; prize pool of the shown rows ≈ {_money(pool)}'
    head += '.\n\n'
    return head + _hackathon_lines(rows) + (
        f'\n\nStatus is derived from the dates Devpost states vs today ({config.today().isoformat()}); '
        f'prize totals use static FX and are approximate.')


def prose_stats(res):
    d = res['data']
    c = d['counts']
    themes = ', '.join(f'{t["name"]} ({t["count"]})' for t in d['themes'][:6])
    orgs = ', '.join(f'{o["name"]} ({o["count"]})' for o in d['top_orgs'][:5])
    soon = '\n'.join(f'- {x["title"]} — {x["end"]} ({x["days_left"]}d) · {_money(x["prize_usd"])}'
                     for x in d['deadlines_next_14d'][:8]) or '- none'
    return (f'**Census of {d["census_date"]}** (today {d["today"]}): {c["total"]:,} hackathons — '
            f'**{c["open"]} open**, {c["upcoming"]} upcoming, {c["ended"]:,} ended; '
            f'{c["ending_7d"]} close within 7 days.\n\n'
            f'Open prize pool ≈ {_money(d["prize_total_open"])} across {d["registrations_open"]:,} '
            f'registrations (static FX, approximate).\n\n'
            f'Open themes: {themes}.\n\nMost frequent organisers (all time): {orgs}.\n\n'
            f'**Deadlines in the next 14 days**\n{soon}')


def prose_winners(res, inp):
    d = res['data']
    rows = d['rows']
    if not rows:
        return (f'No winner\'s title or tagline matches "{inp["query"]}". That is a shortlist '
                f'result, not evidence nobody built it — widen the query (fewer, broader words).')
    lines = '\n'.join(f'- **[{r["title"]}]({r["url"]})** — {r["tagline"] or "no tagline"} '
                      f'_{r["hackathon_title"] or r["host"]}_' for r in rows)
    return (f'**{len(rows)} winners** whose title or tagline matches "{inp["query"]}":\n\n{lines}\n\n'
            f'This is a **shortlist, not a ranking** — FTS over ~100-character taglines measures your '
            f'vocabulary, not the field. Read the entries before claiming anything is rare.')


def prose_brief(res):
    d = res['data']
    if not d.get('criteria'):
        return (f'**{d["title"]}** ({d["host"]}) — no judging criteria could be parsed from the '
                f'page or /rules. Open https://{d["host"]}/rules and read them by hand; everything '
                f'downstream scores against them.')
    crit = '\n'.join(
        f'{i}. **{c["label"]}**' + (f' ({c["weight"]}%)' if c.get('weight') else '') +
        (' — *tie-break criterion*' if c['label'] == d['tiebreak_criterion'] else '') +
        f'\n   {c["text"][:220]}' for i, c in enumerate(d['criteria'], 1))
    reqs = '\n'.join(f'- {r}' for r in d['requirements']) or '- none parsed'
    prizes = ', '.join(p['name'] for p in d['prizes'][:6]) or 'not parsed'
    return (f'**{d["title"]}** — {d["url"]}' + (f' · {d["dates"]}' if d.get('dates') else '') +
            (f' · {_money(d["prize_usd"])}' if d.get('prize_usd') else '') + '\n\n'
            f'**Judging criteria** (verbatim, {d["weighting"]} weighting'
            f'{"; " + d["weighting_note"] if d.get("weighting_note") else ""}; source: '
            f'{d.get("criteria_source")}):\n\n{crit}\n\n'
            f'Devpost\'s standard tie-break resolves ties on the first criterion, so '
            f'**{d["tiebreak_criterion"]}** decides placements once scores bunch at the top.\n\n'
            f'**Hard requirements**\n{reqs}\n\n**Prizes**: {prizes}')


def prose_ideas(res):
    d = res['data']
    cands = d['candidates']
    if not cands:
        return 'No candidate cleared the minimum-wins bar for this rubric.'
    lines = []
    for i, c in enumerate(cands, 1):
        ev = ', '.join(f'[{e["title"]}](https://devpost.com/software/{e["slug"]})'
                       for e in c['evidence'][:3]) or 'none'
        lines.append(f'{i}. **{c["title"]}** — {c["kind"]}, {c["expected_wins"]} winners use this move'
                     + (f', {c["in_this_field"]} in this field' if c.get('in_this_field') is not None and d['field_measured'] else '')
                     + f'. {c["why"]}\n   Evidence: {ev}\n   Risk: {c["risk"]}')
    tail = ('' if d['field_measured'] else
            '\n\n⚠ This hackathon\'s own field was not available, so *absent here* is unmeasured; '
            'the ordering is rubric fit alone.')
    return (f'**{len(cands)} candidates for {d["title"]}** from {d["brain_size"]:,} faceted winners '
            f'(field: {d["field_source"]}); tie-break criterion **{d["tiebreak_criterion"]}**.\n\n'
            + '\n'.join(lines) + tail +
            '\n\nNone of these is an idea until it survives the five kill tests in '
            '`position/IDEA-SELECTION.md` (prompt, server, occupancy, 60-second, 24-hour).')


def prose_vault(res, inp):
    d = res['data']
    if not d['notes']:
        return (f'No vault note matches "{inp["query"]}" ({inp.get("kind", "any")}). The taxonomy is '
                f'regex over prose — try the facet\'s own spelling (e.g. `health_clinical`, '
                f'`voice_audio`).')
    lines = '\n'.join(f'- **{n["title"]}** _{n["kind"]}_ — {n["excerpt"][:180]}' for n in d['notes'])
    return (f'**{len(d["notes"])} vault notes** for "{inp["query"]}":\n\n{lines}\n\n'
            f'Facet counts come from a regex taxonomy; read them as bands, not truths.')


def prose_error(name, res):
    return f'`{name}` could not complete: {res["summary"]}'


PROSE = {
    'list_hackathons': lambda r, i: prose_list(r, i),
    'census_stats': lambda r, i: prose_stats(r),
    'search_winners': lambda r, i: prose_winners(r, i),
    'hackathon_brief': lambda r, i: prose_brief(r),
    'ideate': lambda r, i: prose_ideas(r),
    'vault_lookup': lambda r, i: prose_vault(r, i),
}

THINKING = {
    'hackathon_brief': 'Resolving the hackathon and reading its judging criteria…',
    'ideate': 'Scoring proven moves against the rubric…',
    'search_winners': 'Searching the winner corpus…',
    'vault_lookup': 'Searching the vault…',
    'list_hackathons': 'Filtering the census…',
    'census_stats': 'Counting the census…',
}


def run(chat, text):
    """Generator of (event, data) — identical sequence to Claude mode."""
    mid = uuid.uuid4().hex[:12]
    yield 'message_start', {'chat_id': chat['id'], 'message_id': mid, 'mode': 'local'}
    plan = route(text)
    chat['messages'].append({'role': 'user', 'text': text, 'tool_calls': []})
    entry = {'role': 'assistant', 'text': '', 'tool_calls': [], 'id': mid}
    chat['messages'].append(entry)

    def say(s):
        entry['text'] += s
        return 'text_delta', {'text': s}

    if not plan['calls']:
        yield say(HELP.format(census=tools.store().census_date))
        yield 'message_end', {}
        return

    pieces = []
    host = None
    for name, inp in plan['calls']:
        if name == 'ideate':
            if not host:
                pieces.append('Ideas need a resolved brief first, and the brief failed.')
                continue
            inp = {'host': host}
        yield 'thinking', {'text': THINKING.get(name, f'Running {name}…')}
        cid = f'call_{uuid.uuid4().hex[:8]}'
        yield 'tool_call', {'id': cid, 'name': name, 'input': inp}
        res = tools.run(name, inp)
        entry['tool_calls'].append({'id': cid, 'name': name, 'input': inp, 'result': res})
        yield 'tool_result', {'id': cid, 'name': name, 'ok': res['ok'],
                              'summary': res['summary'], 'data': res['data']}
        if not res['ok']:
            pieces.append(prose_error(name, res))
            continue
        if name == 'hackathon_brief':
            host = res['data'].get('host')
        pieces.append(PROSE[name](res, inp))

    text_out = '\n\n---\n\n'.join(pieces)
    # stream in sentence-ish chunks so the UI shows progress
    for chunk in re.findall(r'.{1,160}(?:\s|$)', text_out, flags=re.S) or [text_out]:
        yield say(chunk)
    yield 'message_end', {}
