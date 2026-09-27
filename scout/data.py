"""In-memory census: hackathon rows with status/prize derived at request time,
FTS over winners, lazily loaded facets, cached briefs, and the chat store."""
import json
import re
import sqlite3
import threading
import uuid
from collections import Counter
from datetime import date, datetime
from pathlib import Path

from hub.store import fts_query, prize_parts
from scout import config

MONTHS = {m: i for i, m in enumerate(
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 1)}
_MD = r'([A-Z][a-z]{2}) (\d{1,2})'
# The four shapes the census contains: "Sep 05 - 06, 2026", "Dec 31, 2026",
# "Jul 31 - Oct 01, 2026", "Jul 16, 2026 - Jan 15, 2027".
_P_FULL = re.compile(rf'^{_MD}, (\d{{4}}) - {_MD}, (\d{{4}})$')
_P_TWO_MONTHS = re.compile(rf'^{_MD} - {_MD}, (\d{{4}})$')
_P_ONE_MONTH = re.compile(rf'^{_MD} - (\d{{1,2}}), (\d{{4}})$')
_P_SINGLE = re.compile(rf'^{_MD}, (\d{{4}})$')


def _d(mon, day, year):
    try:
        return date(int(year), MONTHS[mon], int(day))
    except (KeyError, ValueError):
        return None


def parse_dates(text):
    """'Jul 31 - Oct 01, 2026' -> (start, end) as dates, or (None, None)."""
    s = (text or '').strip()
    m = _P_FULL.match(s)
    if m:
        return _d(m[1], m[2], m[3]), _d(m[4], m[5], m[6])
    m = _P_TWO_MONTHS.match(s)
    if m:
        return _d(m[1], m[2], m[5]), _d(m[3], m[4], m[5])
    m = _P_ONE_MONTH.match(s)
    if m:
        return _d(m[1], m[2], m[4]), _d(m[1], m[3], m[4])
    m = _P_SINGLE.match(s)
    if m:
        d = _d(m[1], m[2], m[3])
        return d, d
    return None, None


def derive_status(start, end, today):
    if start is None or end is None:
        return None
    if end < today:
        return 'ended'
    if start > today:
        return 'upcoming'
    return 'open'


def host_of(url):
    return re.sub(r'^https?://|/.*$', '', url or '')


def https(url):
    if not url:
        return None
    if url.startswith('//'):
        return 'https:' + url
    return re.sub(r'^http://', 'https://', url)


def read_jsonl(path):
    p = Path(path)
    if not p.exists():
        return []
    out = []
    for line in p.read_text(encoding='utf-8').splitlines():
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return out


class Store:
    def __init__(self, hackathons=None, hackathons_all=None, ideas_db=None, facets=None,
                 briefs_dir=None, vault=None):
        self.paths = {
            'hackathons': Path(hackathons or config.HACKATHONS),
            'all': Path(hackathons_all or config.HACKATHONS_ALL),
            'db': Path(ideas_db or config.IDEAS_DB),
            'facets': Path(facets or config.FACETS),
            'briefs': Path(briefs_dir or config.BRIEFS),
            'vault': Path(vault or config.VAULT),
        }
        self._lock = threading.Lock()
        self._facets = None
        self.raw = {}
        self.load()

    # ---- loading -------------------------------------------------------------------
    def load(self):
        rows = {}
        for r in read_jsonl(self.paths['all']) + read_jsonl(self.paths['hackathons']):
            rid = r.get('id')
            if rid is None:
                continue
            prev = rows.get(rid)
            if prev is None or (r.get('thumbnail_url') and not prev.get('thumbnail_url')):
                rows[rid] = r
        with self._lock:
            self.raw = rows
            self._facets = None
        self.census_date = (datetime.fromtimestamp(self.paths['hackathons'].stat().st_mtime)
                            .date().isoformat() if self.paths['hackathons'].exists() else None)

    def reload(self):
        self.load()

    # ---- derivation ----------------------------------------------------------------
    def card(self, r, today=None):
        today = today or config.today()
        start, end = parse_dates(r.get('submission_period_dates'))
        status = derive_status(start, end, today) or r.get('open_state') or 'ended'
        local, currency, usd = prize_parts(r.get('prize_amount') or '')
        display = re.sub(r'<[^>]+>', '', r.get('prize_amount') or '').strip()
        days_left = None
        if end is not None and status in ('open', 'upcoming'):
            days_left = (end - today).days
        loc = (r.get('displayed_location') or {}).get('location')
        return {
            'id': r.get('id'),
            'title': r.get('title'),
            'url': (r.get('url') or '').rstrip('/'),
            'host': host_of(r.get('url')),
            'org': r.get('organization_name'),
            'status': status,
            'census_state': r.get('open_state'),
            'dates': r.get('submission_period_dates'),
            'start': start.isoformat() if start else None,
            'end': end.isoformat() if end else None,
            'days_left': days_left,
            'themes': [t.get('name') for t in (r.get('themes') or []) if t.get('name')],
            'prize_usd': int(round(usd)),
            'prize_display': display,
            'prize_currency': currency,
            'prizes_counts': r.get('prizes_counts') or {},
            'registrations': r.get('registrations_count') or 0,
            'thumbnail': https(r.get('thumbnail_url')),
            'featured': bool(r.get('featured')),
            'winners_announced': bool(r.get('winners_announced')),
            'gallery_url': r.get('submission_gallery_url'),
            'location': loc,
            'time_left': r.get('time_left_to_submission'),
        }

    def cards(self):
        today = config.today()
        with self._lock:
            rows = list(self.raw.values())
        return [self.card(r, today) for r in rows]

    def get(self, hid):
        try:
            hid = int(hid)
        except (TypeError, ValueError):
            return None
        r = self.raw.get(hid)
        return self.card(r) if r else None

    def by_host(self, host):
        host = (host or '').lower()
        for r in self.raw.values():
            if host_of(r.get('url')).lower() == host:
                return self.card(r)
        return None

    def find_by_title(self, name):
        """Cheap local resolution before any network: exact, then substring, then tokens."""
        q = (name or '').strip().lower()
        if not q:
            return []
        cards = self.cards()
        exact = [c for c in cards if (c['title'] or '').lower() == q]
        if exact:
            return exact
        sub = [c for c in cards if q in (c['title'] or '').lower()]
        if sub:
            return sorted(sub, key=lambda c: (c['status'] != 'open', -(c['registrations'] or 0)))
        toks = set(re.findall(r'[a-z0-9]+', q)) - {'the', 'a', 'of', 'for', 'hackathon'}
        if not toks:
            return []
        scored = []
        for c in cards:
            tt = set(re.findall(r'[a-z0-9]+', (c['title'] or '').lower()))
            hit = len(toks & tt)
            if hit and hit >= max(1, len(toks) - 1):
                scored.append((hit, c))
        scored.sort(key=lambda x: (-x[0], x[1]['status'] != 'open', -(x[1]['registrations'] or 0)))
        return [c for _, c in scored]

    # ---- listing -------------------------------------------------------------------
    def list(self, status='open', q='', theme='', sort='deadline', limit=50):
        status = (status or 'open').lower()
        rows = self.cards()
        if status != 'all':
            rows = [c for c in rows if c['status'] == status]
        if theme:
            t = theme.lower()
            rows = [c for c in rows if any(t == x.lower() for x in c['themes'])]
        if q:
            ql = q.lower()
            rows = [c for c in rows if ql in (c['title'] or '').lower()
                    or ql in (c['org'] or '').lower()
                    or any(ql in x.lower() for x in c['themes'])]
        total = len(rows)
        sort = (sort or 'deadline').lower()
        if sort == 'prize':
            rows.sort(key=lambda c: (-c['prize_usd'], c['end'] or '9999'))
        elif sort == 'registrations':
            rows.sort(key=lambda c: (-(c['registrations'] or 0), c['end'] or '9999'))
        else:                                   # deadline: soonest end first, unknown last
            if status == 'ended':
                rows.sort(key=lambda c: c['end'] or '', reverse=True)
            else:
                rows.sort(key=lambda c: (c['end'] is None, c['end'] or '', -c['prize_usd']))
        try:
            limit = int(limit)
        except (TypeError, ValueError):
            limit = 50
        if limit > 0:
            rows = rows[:limit]
        return rows, total

    def counts(self):
        c = Counter(x['status'] for x in self.cards())
        return {'open': c.get('open', 0), 'upcoming': c.get('upcoming', 0),
                'ended': c.get('ended', 0), 'total': sum(c.values())}

    def stats(self):
        cards = self.cards()
        today = config.today()
        open_rows = [c for c in cards if c['status'] == 'open']
        themes = Counter(t for c in open_rows for t in c['themes'])
        orgs = Counter(c['org'] for c in cards if c['org'])
        soon = [c for c in open_rows if c['days_left'] is not None and 0 <= c['days_left'] <= 14]
        soon.sort(key=lambda c: c['end'])
        counts = self.counts()
        counts['ending_7d'] = sum(1 for c in open_rows
                                  if c['days_left'] is not None and 0 <= c['days_left'] <= 7)
        return {
            'census_date': self.census_date,
            'today': today.isoformat(),
            'counts': counts,
            'prize_total_open': sum(c['prize_usd'] for c in open_rows),
            'prize_total_all': sum(c['prize_usd'] for c in cards),
            'registrations_open': sum(c['registrations'] or 0 for c in open_rows),
            'themes': [{'name': k, 'count': v} for k, v in themes.most_common(20)],
            'top_orgs': [{'name': k, 'count': v} for k, v in orgs.most_common(15)],
            'deadlines_next_14d': [{'id': c['id'], 'title': c['title'], 'end': c['end'],
                                    'days_left': c['days_left'], 'prize_usd': c['prize_usd'],
                                    'url': c['url']} for c in soon[:20]],
            'themes_all': sorted({t for c in cards for t in c['themes']}),
        }

    # ---- winners (FTS) -------------------------------------------------------------
    def winners(self, query, limit=20, winners_only=True):
        db = self.paths['db']
        if not db.exists() or not (query or '').strip():
            return []
        con = sqlite3.connect(f'file:{db}?mode=ro', uri=True)
        try:
            where = 'AND p.is_winner = 1' if winners_only else ''
            sql = f"""SELECT p.slug, p.title, p.tagline, p.host, p.hackathon_title, p.url,
                             p.is_winner, p.organization
                      FROM projects_fts f JOIN projects p ON p.software_id = f.rowid
                      WHERE projects_fts MATCH ? {where}
                      ORDER BY bm25(projects_fts), p.is_winner DESC LIMIT ?"""
            try:
                rows = con.execute(sql, (fts_query(query), int(limit))).fetchall()
            except sqlite3.OperationalError:
                rows = con.execute(sql, ('"' + query.replace('"', '') + '"', int(limit))).fetchall()
        finally:
            con.close()
        return [{'slug': s, 'title': t, 'tagline': tg, 'host': h, 'hackathon_title': ht,
                 'url': u, 'is_winner': bool(w), 'org': o}
                for s, t, tg, h, ht, u, w, o in rows]

    def winners_count(self):
        db = self.paths['db']
        if not db.exists():
            return 0
        con = sqlite3.connect(f'file:{db}?mode=ro', uri=True)
        try:
            return con.execute('SELECT COUNT(*) FROM projects WHERE is_winner=1').fetchone()[0]
        finally:
            con.close()

    # ---- facets (lazy) -------------------------------------------------------------
    def facets(self):
        with self._lock:
            if self._facets is None:
                self._facets = read_jsonl(self.paths['facets'])
            return self._facets

    # ---- briefs cache --------------------------------------------------------------
    def brief_path(self, host):
        return self.paths['briefs'] / f'{host}.json'

    def cached_brief(self, host):
        p = self.brief_path(host)
        if not p.exists():
            return None
        try:
            return json.loads(p.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            return None

    def save_brief(self, host, payload):
        p = self.brief_path(host)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(payload, ensure_ascii=False, indent=1), encoding='utf-8')


class ChatStore:
    """One JSON file per chat under data/chats/. `api_messages` is the Claude-side
    history (content blocks); `messages` is the rendered transcript the UI reads."""

    def __init__(self, directory=None):
        self.dir = Path(directory or config.CHATS)
        self.dir.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()

    def _path(self, cid):
        if not re.fullmatch(r'[A-Za-z0-9_-]{1,64}', cid or ''):
            raise KeyError(cid)
        return self.dir / f'{cid}.json'

    def create(self, title=None):
        cid = uuid.uuid4().hex[:12]
        chat = {'id': cid, 'title': title or 'New chat',
                'created': datetime.now().isoformat(timespec='seconds'),
                'messages': [], 'api_messages': []}
        self.save(chat)
        return chat

    def get(self, cid):
        p = self._path(cid)
        if not p.exists():
            return None
        return json.loads(p.read_text(encoding='utf-8'))

    def save(self, chat):
        with self._lock:
            self._path(chat['id']).write_text(json.dumps(chat, ensure_ascii=False),
                                              encoding='utf-8')

    def list(self):
        out = []
        for p in self.dir.glob('*.json'):
            try:
                c = json.loads(p.read_text(encoding='utf-8'))
            except json.JSONDecodeError:
                continue
            out.append({'id': c.get('id'), 'title': c.get('title'), 'created': c.get('created'),
                        'updated': c.get('updated') or c.get('created'),
                        'message_count': len(c.get('messages') or [])})
        out.sort(key=lambda c: c.get('updated') or '', reverse=True)
        return out

    @staticmethod
    def public(chat):
        return {k: v for k, v in chat.items() if k != 'api_messages'}
