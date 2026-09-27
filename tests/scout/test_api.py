"""Scout backend tests — synthetic data, no network.

    python3 -m unittest discover -s tests/scout
"""
import json
import os
import sqlite3
import sys
import tempfile
import threading
import unittest
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

TMP = tempfile.mkdtemp(prefix='scout-test-')
os.environ['SCOUT_DATA_DIR'] = TMP
os.environ['SCOUT_TODAY'] = '2026-09-27'
os.environ.pop('ANTHROPIC_API_KEY', None)          # local mode, always

from scout import config, data, local_agent, server, tools       # noqa: E402
from hub.store import connect as connect_db                       # noqa: E402

TODAY = date(2026, 9, 27)


def row(i, title, dates, prize='$<span data-currency-value>10,000</span>', state='open',
        themes=('Machine Learning/AI',), org='Org', regs=100, thumb=True, url=None):
    return {'id': i, 'title': title, 'url': url or f'https://h{i}.devpost.com/',
            'open_state': state, 'submission_period_dates': dates, 'prize_amount': prize,
            'themes': [{'id': k, 'name': t} for k, t in enumerate(themes)],
            'organization_name': org, 'registrations_count': regs,
            'thumbnail_url': '//cdn.example/x.jpg' if thumb else None,
            'prizes_counts': {'cash': 3}, 'featured': False, 'winners_announced': state == 'ended',
            'submission_gallery_url': f'https://h{i}.devpost.com/project-gallery',
            'displayed_location': {'location': 'Online'}}


ROWS_ALL = [
    row(1, 'RevenueCat Shipaton 2026', 'Jul 31 - Oct 01, 2026',
        '$<span data-currency-value>740,000</span>', themes=('Design', 'Mobile'), org='RevenueCat',
        regs=23594, thumb=False, url='https://revenuecat-shipaton-2026.devpost.com/'),
    row(2, 'Ends Tomorrow Hack', 'Sep 05 - 28, 2026', '$<span>5,000</span>', regs=10),
    row(3, 'Future Hack', 'Dec 31, 2026', '$<span>1,000</span>', state='upcoming'),
    row(4, 'Long Ago Hack', 'Jan 16, 2025 - Feb 15, 2025', '$<span>99,000</span>', state='ended'),
    row(5, 'Rupee Hack', 'Sep 01 - Nov 30, 2026', '₹<span>1,000,000</span>', regs=50000,
        themes=('Fintech',), org='Bank'),
    row(6, 'No Dates Hack', '', '$<span>0</span>', state='ended'),
]
ROWS_THUMB = [dict(ROWS_ALL[0], thumbnail_url='//cdn.example/rc.jpg')]


def write_fixture():
    d = Path(TMP)
    (d / 'hackathons_all.jsonl').write_text('\n'.join(json.dumps(r) for r in ROWS_ALL) + '\n')
    (d / 'hackathons.jsonl').write_text('\n'.join(json.dumps(r) for r in ROWS_THUMB) + '\n')
    con = connect_db(str(d / 'ideas.db'))
    projects = [
        (101, 'sign-agent', 'https://devpost.com/software/sign-agent', 'SignAgent',
         'An accessibility agent that reads sign language', 'a.devpost.com', 'Access Hack', 'X', 1, '[]', 1),
        (102, 'dull-app', 'https://devpost.com/software/dull-app', 'Dull App',
         'A todo list', 'b.devpost.com', 'Todo Hack', 'Y', 1, '[]', 1),
        (103, 'agent-loser', 'https://devpost.com/software/agent-loser', 'Agent Loser',
         'An agent that did not win', 'a.devpost.com', 'Access Hack', 'X', 0, '[]', 2),
    ]
    con.executemany('INSERT OR REPLACE INTO projects VALUES (?,?,?,?,?,?,?,?,?,?,?)', projects)
    con.execute("INSERT INTO projects_fts(projects_fts) VALUES('rebuild')")
    con.commit()
    con.close()
    (d / 'chats').mkdir(exist_ok=True)


write_fixture()
STORE = data.Store(hackathons=Path(TMP) / 'hackathons.jsonl',
                   hackathons_all=Path(TMP) / 'hackathons_all.jsonl',
                   ideas_db=Path(TMP) / 'ideas.db', facets=Path(TMP) / 'facets.jsonl',
                   briefs_dir=Path(TMP) / 'run' / 'briefs', vault=ROOT / 'vault')
tools.set_store(STORE)
server.set_chats(data.ChatStore(Path(TMP) / 'chats'))


class TestDerivation(unittest.TestCase):
    def test_parse_dates_four_shapes(self):
        self.assertEqual(data.parse_dates('Sep 05 - 06, 2026'), (date(2026, 9, 5), date(2026, 9, 6)))
        self.assertEqual(data.parse_dates('Dec 31, 2026'), (date(2026, 12, 31), date(2026, 12, 31)))
        self.assertEqual(data.parse_dates('Jul 31 - Oct 01, 2026'), (date(2026, 7, 31), date(2026, 10, 1)))
        self.assertEqual(data.parse_dates('Jul 16, 2026 - Jan 15, 2027'), (date(2026, 7, 16), date(2027, 1, 15)))
        self.assertEqual(data.parse_dates('garbage'), (None, None))

    def test_status_from_dates_not_census_state(self):
        by = {c['id']: c for c in STORE.cards()}
        self.assertEqual(by[1]['status'], 'open')
        self.assertEqual(by[2]['status'], 'open')
        self.assertEqual(by[2]['days_left'], 1)
        self.assertEqual(by[3]['status'], 'upcoming')
        self.assertEqual(by[4]['status'], 'ended')
        self.assertEqual(by[4]['census_state'], 'ended')
        self.assertEqual(by[6]['status'], 'ended')          # falls back to open_state
        self.assertIsNone(by[6]['days_left'])

    def test_prize_usd_and_currency(self):
        by = {c['id']: c for c in STORE.cards()}
        self.assertEqual(by[1]['prize_usd'], 740000)
        self.assertEqual(by[1]['prize_display'], '$740,000')
        self.assertEqual(by[5]['prize_currency'], 'INR')
        self.assertEqual(by[5]['prize_usd'], 12000)          # 1,000,000 × 0.012

    def test_dedupe_prefers_thumbnail_and_https(self):
        by = {c['id']: c for c in STORE.cards()}
        self.assertEqual(len(by), 6)
        self.assertEqual(by[1]['thumbnail'], 'https://cdn.example/rc.jpg')
        self.assertEqual(by[1]['host'], 'revenuecat-shipaton-2026.devpost.com')
        self.assertEqual(by[1]['url'], 'https://revenuecat-shipaton-2026.devpost.com')

    def test_list_filter_sort(self):
        rows, total = STORE.list(status='open', sort='deadline')
        self.assertEqual(total, 3)
        self.assertEqual([r['id'] for r in rows], [2, 1, 5])
        rows, _ = STORE.list(status='open', sort='prize')
        self.assertEqual(rows[0]['id'], 1)
        rows, _ = STORE.list(status='open', sort='registrations')
        self.assertEqual(rows[0]['id'], 5)
        rows, total = STORE.list(status='all', theme='Fintech')
        self.assertEqual([r['id'] for r in rows], [5])
        rows, total = STORE.list(status='all', q='revenuecat')
        self.assertEqual(total, 1)
        rows, total = STORE.list(status='open', limit=1)
        self.assertEqual(len(rows), 1)
        self.assertEqual(total, 3)

    def test_counts_and_stats(self):
        self.assertEqual(STORE.counts(), {'open': 3, 'upcoming': 1, 'ended': 2, 'total': 6})
        st = STORE.stats()
        self.assertEqual(st['prize_total_open'], 740000 + 5000 + 12000)
        self.assertEqual(st['counts']['ending_7d'], 2)
        self.assertEqual(st['deadlines_next_14d'][0]['id'], 2)

    def test_find_by_title(self):
        self.assertEqual(STORE.find_by_title('revenuecat shipaton 2026')[0]['id'], 1)
        self.assertEqual(STORE.find_by_title('Shipaton')[0]['id'], 1)
        self.assertEqual(STORE.find_by_title('nothing like this'), [])

    def test_winners_fts_is_a_shortlist(self):
        rows = STORE.winners('agent accessibility')
        self.assertEqual([r['slug'] for r in rows], ['sign-agent'])       # winners only
        self.assertTrue(rows[0]['is_winner'])
        self.assertEqual(STORE.winners(''), [])


class TestTools(unittest.TestCase):
    def test_result_shape(self):
        for name, args in [('list_hackathons', {}), ('census_stats', {}),
                           ('search_winners', {'query': 'agent'}),
                           ('vault_lookup', {'query': 'benchmark measured', 'kind': 'mechanism'})]:
            res = tools.run(name, args)
            self.assertEqual(set(res), {'ok', 'summary', 'data'}, name)
            self.assertIsInstance(res['summary'], str)

    def test_search_winners_says_shortlist(self):
        res = tools.run('search_winners', {'query': 'agent'})
        self.assertTrue(res['ok'])
        self.assertIn('not a ranking', res['summary'])
        self.assertTrue(res['data']['shortlist_not_ranking'])

    def test_unknown_keys_dropped_and_unknown_tool_fails(self):
        res = tools.run('list_hackathons', {'status': 'upcoming', 'bogus': 1})
        self.assertTrue(res['ok'])
        self.assertEqual(res['data']['total'], 1)
        self.assertFalse(tools.run('nope', {})['ok'])

    def test_ideate_without_brief_fails_clearly(self):
        res = tools.run('ideate', {'host': 'nowhere.devpost.com'})
        self.assertFalse(res['ok'])
        self.assertIn('hackathon_brief', res['summary'])

    def test_brief_from_config_shapes(self):
        cfg = {'hackathon_host': 'x.devpost.com', 'hackathon_title': 'X',
               'criteria': [{'label': 'A', 'text': 't', 'weight_pct': 60, 'max': 60},
                            {'label': 'B', 'text': 't', 'weight_pct': 40, 'max': 40}],
               'criteria_weighting': 'weighted: A 60%, B 40%', 'tiebreak_criterion': 'A',
               'requirements': {'video_max_minutes': 3, 'needs_repo': True},
               'prizes': ['$10,000'], 'criteria_source': 'hackathon main page'}
        b = tools.brief_from_config(cfg)
        self.assertEqual(b['weighting'], 'weighted')
        self.assertEqual(b['criteria'][0]['weight'], 60)
        self.assertEqual(b['tiebreak_criterion'], 'A')
        self.assertIn('Video no longer than 3 minutes', b['requirements'])
        self.assertEqual(b['prizes'][0]['amount'], '$10,000')
        self.assertEqual(b['url'], 'https://x.devpost.com')


class TestRouting(unittest.TestCase):
    def calls(self, text):
        return local_agent.route(text)['calls']

    def test_list_routes(self):
        (name, inp), = self.calls("What's open this week?")
        self.assertEqual(name, 'list_hackathons')
        self.assertEqual(inp['status'], 'open')
        (name, inp), = self.calls('upcoming hackathons by prize')
        self.assertEqual((inp['status'], inp['sort']), ('upcoming', 'prize'))
        (name, inp), = self.calls('open fintech hackathons')
        self.assertEqual(inp['theme'], 'Fintech')

    def test_brief_routes(self):
        plan = local_agent.route('Scout RevenueCat Shipaton 2026')
        self.assertEqual(plan['calls'][0], ('hackathon_brief', {'name_or_url': 'RevenueCat Shipaton 2026'}))
        self.assertEqual(plan['calls'][1][0], 'ideate')
        plan = local_agent.route('what should I build for webmcp.devpost.com?')
        self.assertEqual(plan['calls'][0][1]['name_or_url'], 'webmcp.devpost.com')
        self.assertEqual(len(plan['calls']), 2)
        plan = local_agent.route('rubric of the WebMCP Hackathon')
        self.assertEqual(plan['calls'], [('hackathon_brief', {'name_or_url': 'WebMCP'})])

    def test_winners_vault_stats_help(self):
        (name, inp), = self.calls('Winners about agents for accessibility')
        self.assertEqual(name, 'search_winners')
        self.assertEqual(inp['query'], 'agents accessibility')
        (name, inp), = self.calls('Gaps in health × voice')
        self.assertEqual((name, inp['kind'], inp['query']), ('vault_lookup', 'gap', 'health voice'))
        (name, inp), = self.calls('mechanism retrieval grounding')
        self.assertEqual((name, inp['kind']), ('vault_lookup', 'mechanism'))
        (name, _), = self.calls('How many hackathons are open?')
        self.assertEqual(name, 'census_stats')
        self.assertEqual(self.calls('hello'), [])
        self.assertEqual(self.calls('tell me a joke'), [])


class TestHTTP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = server.make_server('127.0.0.1', 0)
        cls.port = cls.srv.server_port
        cls.thread = threading.Thread(target=cls.srv.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f'http://127.0.0.1:{cls.port}'

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        cls.srv.server_close()

    def get(self, path):
        with urllib.request.urlopen(self.base + path, timeout=10) as r:
            return r.status, json.loads(r.read().decode('utf-8'))

    def post(self, path, body):
        req = urllib.request.Request(self.base + path, data=json.dumps(body).encode('utf-8'),
                                     headers={'Content-Type': 'application/json'}, method='POST')
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read().decode('utf-8'), r.headers.get('Content-Type')

    def test_health(self):
        status, h = self.get('/api/health')
        self.assertEqual(status, 200)
        self.assertTrue(h['ok'])
        self.assertEqual(h['mode'], 'local')
        self.assertEqual(h['counts'], {'open': 3, 'upcoming': 1, 'ended': 2, 'total': 6})
        self.assertIsNotNone(h['census_date'])

    def test_hackathons_list_and_detail(self):
        _, body = self.get('/api/hackathons?status=open&limit=2&sort=prize')
        self.assertEqual(body['total'], 3)
        self.assertEqual(len(body['rows']), 2)
        self.assertEqual(body['rows'][0]['title'], 'RevenueCat Shipaton 2026')
        _, one = self.get('/api/hackathons/1')
        self.assertEqual(one['host'], 'revenuecat-shipaton-2026.devpost.com')
        self.assertIsNone(one['brief'])
        with self.assertRaises(urllib.error.HTTPError):
            self.get('/api/hackathons/999')

    def test_stats_and_winners(self):
        _, st = self.get('/api/stats')
        self.assertEqual(st['counts']['open'], 3)
        self.assertIn('themes', st)
        _, w = self.get('/api/winners?q=agent&limit=5')
        self.assertEqual([x['slug'] for x in w], ['sign-agent'])
        _, w = self.get('/api/winners')
        self.assertEqual(w, [])

    def test_local_chat_message_sse(self):
        status, body, _ = self.post('/api/chats', {'title': 't'})
        self.assertEqual(status, 201)
        cid = json.loads(body)['id']
        status, body, ctype = self.post(f'/api/chats/{cid}/messages', {'text': "What's open this week?"})
        self.assertEqual(status, 200)
        self.assertIn('text/event-stream', ctype)
        events = []
        for block in body.strip().split('\n\n'):
            lines = dict(l.split(': ', 1) for l in block.splitlines() if ': ' in l)
            events.append((lines['event'], json.loads(lines['data'])))
        names = [e for e, _ in events]
        self.assertEqual(names[0], 'message_start')
        self.assertEqual(events[0][1]['mode'], 'local')
        self.assertIn('thinking', names)
        self.assertLess(names.index('tool_call'), names.index('tool_result'))
        self.assertLess(names.index('tool_result'), names.index('text_delta'))
        self.assertEqual(names[-1], 'message_end')
        tc = next(d for e, d in events if e == 'tool_call')
        self.assertEqual(tc['name'], 'list_hackathons')
        tr = next(d for e, d in events if e == 'tool_result')
        self.assertTrue(tr['ok'])
        self.assertEqual(tr['data']['total'], 3)
        text = ''.join(d['text'] for e, d in events if e == 'text_delta')
        self.assertIn('**3 open hackathons**', text)
        self.assertIn('RevenueCat Shipaton 2026', text)
        # transcript persisted
        _, chat = self.get(f'/api/chats/{cid}')
        self.assertEqual(len(chat['messages']), 2)
        self.assertEqual(chat['messages'][1]['tool_calls'][0]['name'], 'list_hackathons')
        self.assertNotIn('api_messages', chat)
        _, lst = self.get('/api/chats')
        self.assertTrue(any(c['id'] == cid for c in lst))

    def test_fallback_page_and_404(self):
        with urllib.request.urlopen(self.base + '/', timeout=10) as r:
            self.assertIn(b'Scout', r.read())
        with self.assertRaises(urllib.error.HTTPError) as cm:
            self.get('/api/nope')
        self.assertEqual(cm.exception.code, 404)


if __name__ == '__main__':
    unittest.main()
