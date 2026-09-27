"""The agent's tools. Each is a plain function returning
{"ok": bool, "summary": str, "data": {...}} and wraps a toolkit module rather than
re-implementing it. Network tools cache under data/run/ and never raise on a WAF
challenge — they return ok=False with a message that says what happened."""
import json
import re
import sys
import threading
import urllib.error
from collections import Counter
from pathlib import Path

from scout import config

sys.path.insert(0, str(config.ROOT))
from lib.fetch import Challenged                                     # noqa: E402

_store = None
_store_lock = threading.Lock()


def store():
    global _store
    with _store_lock:
        if _store is None:
            from scout.data import Store
            _store = Store()
        return _store


def set_store(s):
    global _store
    _store = s


def ok(summary, data=None):
    return {'ok': True, 'summary': summary, 'data': data or {}}


def fail(summary, data=None):
    return {'ok': False, 'summary': summary, 'data': data or {}}


def _net_error(exc, what):
    if isinstance(exc, Challenged):
        return fail(f'Devpost answered {what} with a WAF challenge instead of the page; '
                    f'nothing was recorded. Retry in a minute. ({exc})')
    if isinstance(exc, (urllib.error.URLError, OSError, TimeoutError)):
        return fail(f'Network error while fetching {what}: {exc}')
    return fail(f'{what} failed: {type(exc).__name__}: {exc}')


# ------------------------------------------------------------------------------------
# list_hackathons / census_stats — pure, instant
# ------------------------------------------------------------------------------------
def list_hackathons(status='open', query='', theme='', sort='deadline', limit=12):
    rows, total = store().list(status=status, q=query or '', theme=theme or '',
                               sort=sort or 'deadline', limit=limit or 12)
    parts = [f'{total} {status or "open"} hackathon{"s" if total != 1 else ""}']
    if theme:
        parts.append(f'themed {theme}')
    if query:
        parts.append(f'matching "{query}"')
    s = ' '.join(parts) + f' in the {store().census_date} census; showing {len(rows)}, sorted by {sort or "deadline"}.'
    return ok(s, {'rows': rows, 'total': total, 'status': status, 'sort': sort,
                  'census_date': store().census_date})


def census_stats():
    st = store().stats()
    c = st['counts']
    return ok(f'Census of {st["census_date"]}: {c["total"]:,} hackathons — {c["open"]} open, '
              f'{c["upcoming"]} upcoming, {c["ended"]:,} ended; open prize pool '
              f'≈ ${st["prize_total_open"]:,} (static FX, approximate).', st)


# ------------------------------------------------------------------------------------
# search_winners — FTS shortlist, never a ranking
# ------------------------------------------------------------------------------------
def search_winners(query, limit=15):
    if not (query or '').strip():
        return fail('search_winners needs a query.')
    rows = store().winners(query, limit=limit or 15)
    n = len(rows)
    s = (f'{n} winner{"s" if n != 1 else ""} match "{query}" across the '
         f'{store().winners_count():,}-winner corpus. This is a shortlist, not a ranking: '
         f'FTS over title+tagline measures your vocabulary, not the field — widen the query '
         f'before concluding nobody built it.')
    return ok(s, {'rows': rows, 'query': query, 'shortlist_not_ranking': True})


# ------------------------------------------------------------------------------------
# hackathon_brief — discover/hackathon.py, cached under data/run/briefs/
# ------------------------------------------------------------------------------------
def _host_from(text):
    m = re.search(r'([a-z0-9-]+\.devpost\.com)', (text or '').lower())
    return m.group(1) if m else None


def brief_from_config(cfg, card=None):
    crits = []
    for c in cfg.get('criteria') or []:
        crits.append({'label': c.get('label'), 'text': c.get('text'),
                      'weight': c.get('weight_pct') if c.get('weight_pct') is not None
                      else c.get('max')})
    w = (cfg.get('criteria_weighting') or '')
    if w.startswith('weighted') or w.startswith('stated points'):
        weighting = 'weighted'
    elif 'equal' in w:
        weighting = 'equal'
    else:
        weighting = 'unknown'
    reqs = []
    labels = {'video_max_minutes': 'Video no longer than {} minutes',
              'video_must_be_public': 'Video must be public',
              'needs_public_url': 'Publicly accessible URL / working demo required',
              'needs_repo': 'Source code / public repository required',
              'english_required': 'Submission must be in English'}
    for k, v in (cfg.get('requirements') or {}).items():
        lab = labels.get(k, k)
        reqs.append(lab.format(v) if '{}' in lab else lab)
    prizes = []
    for p in cfg.get('prizes') or []:
        if isinstance(p, dict):
            prizes.append({'name': p.get('name'), 'amount': p.get('amount')})
        else:
            m = re.search(r'([$€£₹]\s?[\d,]+(?:\.\d+)?)', str(p))
            prizes.append({'name': str(p), 'amount': m.group(1) if m else None})
    host = cfg.get('hackathon_host')
    return {
        'title': cfg.get('hackathon_title'),
        'host': host,
        'url': f'https://{host}' if host else None,
        'criteria': crits,
        'weighting': weighting,
        'weighting_note': w or None,
        'tiebreak_criterion': cfg.get('tiebreak_criterion'),
        'requirements': reqs,
        'prizes': prizes,
        'dates': (card or {}).get('dates'),
        'status': (card or {}).get('status'),
        'prize_usd': (card or {}).get('prize_usd'),
        'hackathon_id': (card or {}).get('id'),
        'criteria_source': cfg.get('criteria_source'),
    }


def resolve_host(name_or_url, pick=1):
    """-> (host, title, card, candidates) without network when the census knows the name."""
    host = _host_from(name_or_url)
    if host:
        card = store().by_host(host)
        return host, (card or {}).get('title'), card, []
    cands = store().find_by_title(name_or_url)
    if cands:
        idx = max(1, int(pick or 1)) - 1
        c = cands[min(idx, len(cands) - 1)]
        return c['host'], c['title'], c, cands
    return None, None, None, []


def hackathon_brief(name_or_url, pick=1, refresh=False):
    if not (name_or_url or '').strip():
        return fail('hackathon_brief needs a hackathon name or URL.')
    from discover import hackathon as disc
    host, title, card, cands = resolve_host(name_or_url, pick)
    if not host:
        try:
            hits = disc.search(name_or_url)
        except Exception as exc:                                     # noqa: BLE001
            return _net_error(exc, f'the Devpost search for "{name_or_url}"')
        if not hits:
            return fail(f'No hackathon matched "{name_or_url}" in the census or on Devpost.')
        idx = max(1, int(pick or 1)) - 1
        h = hits[min(idx, len(hits) - 1)]
        host, title = h['host'], h['title']
        card = store().by_host(host)
        cands = [{'title': x['title'], 'host': x['host'], 'status': x['state'],
                  'dates': x['dates']} for x in hits]
    cached = None if refresh else store().cached_brief(host)
    if cached and cached.get('brief'):
        brief = cached['brief']
        if card:
            brief.update({'dates': card.get('dates'), 'status': card.get('status'),
                          'prize_usd': card.get('prize_usd'), 'hackathon_id': card.get('id')})
        return ok(_brief_summary(brief, cached=True, cands=cands),
                  {**brief, 'candidates': cands[:6], 'cached': True})
    try:
        cfg = disc.build(host, title)
    except Exception as exc:                                         # noqa: BLE001
        return _net_error(exc, f'https://{host}')
    brief = brief_from_config(cfg, card)
    store().save_brief(host, {'brief': brief, 'config': cfg})
    return ok(_brief_summary(brief, cached=False, cands=cands),
              {**brief, 'candidates': cands[:6], 'cached': False})


def _brief_summary(b, cached, cands):
    n = len(b['criteria'])
    s = f'{b["title"]} ({b["host"]}): '
    if n:
        s += (f'{n} judging criteria, weighting {b["weighting"]}'
              f'{" — " + b["weighting_note"] if b.get("weighting_note") else ""}; '
              f'tie-break on "{b["tiebreak_criterion"]}" (first listed). ')
    else:
        s += 'no criteria could be parsed from the page — read /rules by hand. '
    if b['requirements']:
        s += f'{len(b["requirements"])} hard requirements. '
    s += f'Source: {b.get("criteria_source") or "none"}'
    s += ' (cached).' if cached else '.'
    if len(cands) > 1:
        s += f' {len(cands)} census titles matched; picked the first — pass pick=N to change.'
    return s


# ------------------------------------------------------------------------------------
# field — hub/collect_gallery.collect, cached under data/run/fields/{host}.jsonl
# ------------------------------------------------------------------------------------
def _field_path(host):
    return config.FIELDS / f'{host}.jsonl'


def cached_field(host):
    p = _field_path(host)
    if not p.exists():
        return None
    meta, rows = {}, []
    for line in p.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        if '_meta' in r:
            meta = r['_meta']
        else:
            rows.append(r)
    return {'rows': rows, 'source': meta.get('source', 'cache'), 'total': meta.get('total', len(rows)),
            'winners_only': meta.get('winners_only', False)}


def _project(r):
    return {'slug': r.get('slug'), 'title': r.get('title'), 'tagline': r.get('tagline'),
            'url': r.get('url'), 'is_winner': bool(r.get('is_winner')),
            'members': r.get('members') or [], 'software_id': r.get('software_id')}


def field(host, limit=200, winners_only=False, refresh=False):
    host = _host_from(host) or (host or '').strip().lower()
    if not host:
        return fail('field needs a devpost host, e.g. webmcp.devpost.com.')
    limit = int(limit or 200)
    cached = None if refresh else cached_field(host)
    if cached and (not cached['winners_only'] or winners_only):
        rows = [r for r in cached['rows'] if r.get('is_winner')] if winners_only else cached['rows']
        return ok(_field_summary(host, rows[:limit], cached['total'], cached['source'], True),
                  {'rows': [_project(r) for r in rows[:limit]], 'total': cached['total'],
                   'source': cached['source'], 'host': host, 'cached': True,
                   'winners': sum(1 for r in cached['rows'] if r.get('is_winner'))})
    from hub.collect_gallery import collect
    max_pages = max(1, (limit + 23) // 24)
    try:
        rows, status = collect(host, pause=0.5, max_pages=max_pages, winners_only=winners_only)
    except Exception as exc:                                         # noqa: BLE001
        return _net_error(exc, f'https://{host}/project-gallery')
    source = 'gallery_unpublished' if status == 'gallery_unpublished' else (
        f'project-gallery ({status})')
    config.FIELDS.mkdir(parents=True, exist_ok=True)
    with _field_path(host).open('w', encoding='utf-8') as fh:
        fh.write(json.dumps({'_meta': {'source': source, 'total': len(rows),
                                       'winners_only': winners_only, 'status': status}}) + '\n')
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    return ok(_field_summary(host, rows, len(rows), source, False),
              {'rows': [_project(r) for r in rows[:limit]], 'total': len(rows), 'source': source,
               'host': host, 'cached': False,
               'winners': sum(1 for r in rows if r.get('is_winner'))})


def _field_summary(host, rows, total, source, cached):
    if source == 'gallery_unpublished':
        return (f'{host}: the project gallery is not published, so the field is unmeasured — '
                f'an empty result here is not an empty field.')
    w = sum(1 for r in rows if r.get('is_winner'))
    return (f'{host}: {total} project{"s" if total != 1 else ""} in the gallery, {w} with a winner '
            f'ribbon{" (cached)" if cached else ""}. Source: {source}. Gallery paging counts '
            f'entries Devpost lists; the official gallery is often incomplete.')


# ------------------------------------------------------------------------------------
# ideate — hub/ideate.generate with facets + the cached brief
# ------------------------------------------------------------------------------------
def _field_facets(rows):
    """Turn cached gallery rows (title+tagline only) into facet rows via hub/extract."""
    from hub.extract import facets_of, load_taxonomy
    tax = load_taxonomy(config.TAXONOMY)
    out = []
    for r in rows:
        out.append({'slug': r.get('slug'), 'title': r.get('title'), 'tagline': r.get('tagline'),
                    'hackathon_title': None, 'facets': facets_of(r, tax)})
    return out


def _idea(c, rows_by_slug):
    from hub.ideate import strong
    users, subs = Counter(), Counter()
    for e in c.get('evidence') or []:
        r = rows_by_slug.get(e.get('slug'))
        if r:
            users.update(strong(r, 'user'))
            subs.update(strong(r, 'substrate'))
    mech = c['mechanism'].replace('_', ' ')
    dom = (c.get('partner') or '').replace('_', ' ')
    title = f'{mech} × {dom}' if dom else f'{mech} (transfer)'
    if c['kind'] == 'combination':
        risk = ('Under-occupancy is measured against independence in an 8.6k-winner corpus, with '
                'a regex taxonomy — widen the patterns before believing the cell is empty.')
    elif c['kind'] == 'transfer':
        risk = ('Absence in this field was measured on gallery titles and taglines only; '
                'a write-up may use the move without naming it.')
    else:
        risk = ('This hackathon\'s own field was not available, so "absent here" is unmeasured; '
                'ordering is rubric fit alone — a weaker claim.')
    return {
        'title': title, 'kind': c['kind'],
        'mechanism': c['mechanism'], 'domain': c.get('partner'),
        'user': users.most_common(1)[0][0] if users else None,
        'substrate': subs.most_common(1)[0][0] if subs else None,
        'expected_wins': c.get('global_wins'),
        'in_this_field': c.get('in_this_field'),
        'expected': c.get('expected'), 'observed': c.get('observed'),
        'score': c.get('score'), 'fit': c.get('fit'),
        'evidence': [{'slug': e.get('slug'), 'title': e.get('title'),
                      'host': e.get('hackathon'), 'tagline': e.get('tagline')}
                     for e in (c.get('evidence') or [])[:4]],
        'why': c.get('why'), 'risk': risk,
    }


def ideate(host, top=10, min_wins=5):
    from hub.ideate import generate, target_field
    host = _host_from(host) or (host or '').strip().lower()
    cached = store().cached_brief(host) if host else None
    if not cached or not cached.get('config'):
        return fail(f'No brief cached for {host or "?"} — run hackathon_brief first; ideas are '
                    f'scored against the rubric verbatim.')
    cfg = cached['config']
    rows = store().facets()
    if not rows:
        return fail('data/facets.jsonl is missing — the winner brain is empty.')
    fld = cached_field(host)
    if fld and fld['rows']:
        field_rows, field_src = _field_facets(fld['rows']), f'cached gallery ({len(fld["rows"])} rows)'
    else:
        field_rows = target_field(rows, cfg, host)
        field_src = f'winner brain ({len(field_rows)} rows)' if field_rows else 'none'
    cands = generate(rows, field_rows, cfg, min_wins)[:int(top or 10)]
    by_slug = {r['slug']: r for r in rows}
    ideas = [_idea(c, by_slug) for c in cands]
    n = len(ideas)
    s = (f'{n} candidate{"s" if n != 1 else ""} for {cfg.get("hackathon_title")} from '
         f'{len(rows):,} faceted winners; this field: {field_src}. ')
    if not field_rows:
        s += ('The hackathon\'s own field is unavailable, so absence here is UNMEASURED — '
              'candidates are ordered by rubric fit alone. ')
    s += 'None of these is an idea until it survives the five kill tests.'
    return ok(s, {'candidates': ideas, 'host': host, 'title': cfg.get('hackathon_title'),
                  'tiebreak_criterion': cfg.get('tiebreak_criterion'),
                  'brain_size': len(rows), 'field_source': field_src,
                  'field_measured': bool(field_rows)})


# ------------------------------------------------------------------------------------
# vault_lookup — grep vault titles/bodies
# ------------------------------------------------------------------------------------
KIND_DIRS = {'mechanism': ['mechanisms'], 'domain': ['domains'], 'gap': ['_gaps'],
             'project': ['projects'], 'substrate': ['substrates'], 'user': ['users'],
             'hackathon': ['hackathons'], 'claim': ['_claims'], 'convergence': ['_convergences'],
             'candidate': ['_candidates']}
_BODY_DIRS = ['mechanisms', 'domains', 'substrates', 'users', '_gaps', '_candidates',
              '_convergences']


def _excerpt(text, terms, width=220):
    body = re.sub(r'^---.*?---\s*', '', text, count=1, flags=re.S)
    low = body.lower()
    pos = -1
    for t in terms:
        pos = low.find(t)
        if pos >= 0:
            break
    if pos < 0:
        pos = 0
    start = max(0, pos - 60)
    snippet = body[start:start + width].replace('\n', ' ').strip()
    return re.sub(r'\s+', ' ', snippet)


def vault_lookup(query, kind='any', limit=12):
    vault = store().paths['vault']
    if not vault.exists():
        return fail('vault/ is not present in this checkout.')
    terms = [t for t in re.findall(r'[a-z0-9]+', (query or '').lower()) if len(t) > 2]
    if not terms:
        return fail('vault_lookup needs a query.')
    kind = (kind or 'any').lower()
    dirs = KIND_DIRS.get(kind) or sorted(d.name for d in vault.iterdir() if d.is_dir())
    notes, seen = [], set()

    def add(path, score, text):
        if path in seen:
            return
        seen.add(path)
        rel = str(path.relative_to(vault))
        notes.append({'title': path.stem, 'path': rel, 'kind': path.parent.name.strip('_'),
                      'score': score, 'excerpt': _excerpt(text, terms)})

    # titles first: every term present in the file name
    for d in dirs:
        dp = vault / d
        if not dp.is_dir():
            continue
        for p in dp.glob('*.md'):
            if p.stem.upper() == 'README':
                continue
            name = p.stem.lower().replace('_', ' ').replace('-', ' ')
            hit = sum(1 for t in terms if t in name)
            if hit == len(terms):
                add(p, 2 * hit, p.read_text(encoding='utf-8', errors='replace'))
    # then bodies of the small directories (projects/ is 8.6k files — titles only)
    if len(notes) < limit:
        for d in dirs:
            if d not in _BODY_DIRS:
                continue
            dp = vault / d
            if not dp.is_dir():
                continue
            for p in dp.glob('*.md'):
                if p in seen or p.stem.upper() == 'README':
                    continue
                text = p.read_text(encoding='utf-8', errors='replace')
                low = text.lower()
                hit = sum(1 for t in terms if t in low)
                if hit == len(terms):
                    add(p, hit, text)
    notes.sort(key=lambda n: (-n['score'], n['title']))
    notes = notes[:int(limit or 12)]
    s = (f'{len(notes)} vault note{"s" if len(notes) != 1 else ""} match "{query}"'
         f'{" in " + kind if kind != "any" else ""}. Facet notes come from a regex taxonomy '
         f'over prose; counts are bands, not truths.')
    return ok(s, {'notes': notes, 'query': query, 'kind': kind})


# ------------------------------------------------------------------------------------
# scout — brief → field → ideate, with progress
# ------------------------------------------------------------------------------------
def scout_pipeline(hackathon, emit=None, field_limit=200):
    """Runs inline; `emit(step, pct, note)` reports progress. Returns the final payload."""
    def prog(step, pct, note):
        if emit:
            emit(step, pct, note)
    prog('brief', 5, f'Resolving "{hackathon}" and reading its judging criteria')
    b = hackathon_brief(hackathon)
    if not b['ok']:
        return {'ok': False, 'summary': b['summary'], 'data': {'brief': None, 'field': None,
                                                              'ideas': None}}
    host = b['data']['host']
    prog('brief', 30, b['summary'])
    prog('field', 35, f'Paging the project gallery at {host}')
    f = field(host, limit=field_limit)
    prog('field', 70, f['summary'])
    prog('ideate', 75, 'Scoring proven moves against the rubric')
    i = ideate(host)
    prog('ideate', 95, i['summary'])
    data = {'brief': b['data'], 'field': f['data'] if f['ok'] else {'error': f['summary']},
            'ideas': i['data'] if i['ok'] else {'error': i['summary']}, 'host': host}
    summary = ' | '.join([b['summary'], f['summary'], i['summary']])
    prog('done', 100, 'Scout complete')
    return {'ok': True, 'summary': summary, 'data': data}


def scout(hackathon, emit=None):
    """Tool entry: start the background job and follow it (so it also appears in /api/jobs)."""
    from scout import jobs
    job = jobs.manager.start_scout(hackathon)
    last = None
    for ev in jobs.manager.stream(job.id):
        if ev['event'] == 'job_progress' and emit:
            emit(ev['data']['step'], ev['data']['pct'], ev['data']['note'], job.id)
        elif ev['event'] == 'job_done':
            last = ev['data']
    if last is None:
        return fail('scout job ended without a result.', {'job_id': job.id})
    if last.get('status') != 'done':
        return fail(f'scout job failed: {last.get("error")}', {'job_id': job.id})
    res = last.get('result') or {}
    out = {'ok': res.get('ok', False), 'summary': res.get('summary', ''),
           'data': dict(res.get('data') or {}, job_id=job.id)}
    return out


# ------------------------------------------------------------------------------------
# registry + JSON schemas (the same declarations feed Claude mode)
# ------------------------------------------------------------------------------------
def _obj(props, required=()):
    return {'type': 'object', 'properties': props, 'required': list(required)}


SCHEMAS = [
    {'name': 'list_hackathons',
     'description': 'List hackathons from the local Devpost census (no network). Status is '
                    'derived from submission dates vs today. Pure and instant.',
     'input_schema': _obj({
         'status': {'type': 'string', 'enum': ['open', 'upcoming', 'ended', 'all']},
         'query': {'type': 'string', 'description': 'substring over title/org/themes'},
         'theme': {'type': 'string', 'description': 'exact Devpost theme name, e.g. "Machine Learning/AI"'},
         'sort': {'type': 'string', 'enum': ['deadline', 'prize', 'registrations']},
         'limit': {'type': 'integer', 'minimum': 1, 'maximum': 100}})},
    {'name': 'hackathon_brief',
     'description': 'Resolve a hackathon by name or URL and read its judging criteria verbatim, '
                    'weights, tie-break criterion, hard requirements and prizes. Network '
                    '(Devpost), cached. Run this before ideate.',
     'input_schema': _obj({
         'name_or_url': {'type': 'string'},
         'pick': {'type': 'integer', 'description': '1-based choice when several match'}},
         ['name_or_url'])},
    {'name': 'search_winners',
     'description': 'Full-text shortlist of past winning projects (title+tagline) across '
                    '2,300 winners. A shortlist, never a ranking.',
     'input_schema': _obj({'query': {'type': 'string'},
                           'limit': {'type': 'integer', 'minimum': 1, 'maximum': 50}},
                          ['query'])},
    {'name': 'field',
     'description': 'Page a hackathon\'s project gallery: the field that already exists and '
                    'which entries won. Network, cached. An unpublished gallery is reported '
                    'as such — it is not an empty field.',
     'input_schema': _obj({'host': {'type': 'string', 'description': 'e.g. webmcp.devpost.com'},
                           'limit': {'type': 'integer', 'minimum': 24, 'maximum': 2000},
                           'winners_only': {'type': 'boolean'}}, ['host'])},
    {'name': 'ideate',
     'description': 'Propose candidate ideas for a hackathon: mechanisms proven across the '
                    'winner corpus and absent (or under-occupied) in this field, scored '
                    'against the cached rubric. Needs hackathon_brief first.',
     'input_schema': _obj({'host': {'type': 'string'}}, ['host'])},
    {'name': 'vault_lookup',
     'description': 'Search the Obsidian vault of facet notes (mechanisms, domains, gaps, '
                    'projects) by title and body.',
     'input_schema': _obj({'query': {'type': 'string'},
                           'kind': {'type': 'string',
                                    'enum': ['mechanism', 'domain', 'gap', 'project', 'any']}},
                          ['query'])},
    {'name': 'census_stats',
     'description': 'Counts, open prize pool, themes, top organisers and deadlines in the next '
                    '14 days, from the local census. Pure.',
     'input_schema': _obj({})},
    {'name': 'scout',
     'description': 'Full pipeline for one hackathon: brief → field → ideas, as a background '
                    'job with progress. Slow (network). Returns {brief, field, ideas}.',
     'input_schema': _obj({'hackathon': {'type': 'string'}}, ['hackathon'])},
]

FUNCTIONS = {
    'list_hackathons': list_hackathons,
    'hackathon_brief': hackathon_brief,
    'search_winners': search_winners,
    'field': field,
    'ideate': ideate,
    'vault_lookup': vault_lookup,
    'census_stats': census_stats,
    'scout': scout,
}

_ALLOWED = {s['name']: set(s['input_schema']['properties']) for s in SCHEMAS}


def run(name, args, emit=None):
    """Dispatch by name with unknown keys dropped; never raises."""
    fn = FUNCTIONS.get(name)
    if not fn:
        return fail(f'unknown tool {name}')
    args = {k: v for k, v in (args or {}).items() if k in _ALLOWED[name]}
    try:
        if name == 'scout':
            return fn(emit=emit, **args)
        return fn(**args)
    except Exception as exc:                                         # noqa: BLE001
        return fail(f'{name} crashed: {type(exc).__name__}: {exc}')
