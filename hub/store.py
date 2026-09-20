#!/usr/bin/env python3
"""The idea hub: every hackathon and every collected project, searchable.

Two questions this exists to answer before you build anything:

    has someone already built this, and did it win?
    which hackathons are worth entering at all?

    python3 hub/store.py build  --hackathons data/hackathons.jsonl \\
                                --projects data/projects.jsonl --db data/ideas.db
    python3 hub/store.py search --db data/ideas.db "agent browser tool" --winners
    python3 hub/store.py orgs   --db data/ideas.db --min-prize 25000
    python3 hub/store.py stats  --db data/ideas.db

Search is FTS5 over title+tagline. That is a *shortlist*, never a ranking — the
same warning `score/signal_score.py` carries, for the same reason: a keyword
query measures your vocabulary, not the field. Read the entries it returns.
"""
import argparse
import html
import json
import re
import sqlite3
import sys
from pathlib import Path

TAG = re.compile(r'<[^>]+>')


def flat(s):
    return re.sub(r'\s+', ' ', html.unescape(TAG.sub(' ', s or ''))).strip()


# Devpost states prize amounts in the host's own currency — eight of them across
# the index. Summing the raw numbers puts a ₹12,687,120 college hackathon (about
# $150k) above Google. These rates are STATIC and approximate; `prize_local` and
# `prize_currency` are stored alongside so any figure can be re-derived, and
# `prize_usd_approx` is named for what it is.
RATES = {'USD': 1.0, 'CAD': 0.73, 'INR': 0.012, 'EUR': 1.08,
         'GBP': 1.27, 'MXN': 0.055, 'PKR': 0.0036}
SYMBOLS = [('USD$', 'USD'), ('MEX$', 'MXN'), ('$CAD', 'CAD'), ('PKR', 'PKR'),
           ('\u20b9', 'INR'), ('\u20ac', 'EUR'), ('\u00a3', 'GBP'), ('$', 'USD')]


def prize_parts(raw):
    """'$<span ...>740,000</span>' -> (740000.0, 'USD', 740000.0 in USD)."""
    text_ = flat(raw)
    currency = 'USD'
    for sym, code in SYMBOLS:
        if text_.startswith(sym):
            currency = code
            break
    digits = re.sub(r'[^\d.]', '', text_)
    try:
        local = float(digits) if digits else 0.0
    except ValueError:
        local = 0.0
    return local, currency, round(local * RATES.get(currency, 1.0), 2)


SCHEMA = """
CREATE TABLE IF NOT EXISTS hackathons (
  id INTEGER PRIMARY KEY, title TEXT, host TEXT UNIQUE, url TEXT,
  organization TEXT, state TEXT, dates TEXT, prize_usd_approx REAL,
  prize_local REAL, prize_currency TEXT,
  registrations INTEGER, themes TEXT, winners_announced INTEGER,
  gallery_url TEXT, featured INTEGER, invite_only INTEGER, location TEXT
);
CREATE TABLE IF NOT EXISTS projects (
  software_id INTEGER PRIMARY KEY, slug TEXT, url TEXT, title TEXT, tagline TEXT,
  host TEXT, hackathon_title TEXT, organization TEXT, is_winner INTEGER,
  members TEXT, gallery_page INTEGER
);
CREATE INDEX IF NOT EXISTS ix_proj_host ON projects(host);
CREATE INDEX IF NOT EXISTS ix_proj_winner ON projects(is_winner);
CREATE INDEX IF NOT EXISTS ix_hack_org ON hackathons(organization);
CREATE VIRTUAL TABLE IF NOT EXISTS projects_fts USING fts5(
  title, tagline, hackathon_title, content='projects', content_rowid='software_id'
);
"""


def connect(db):
    Path(db).parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db)
    con.executescript(SCHEMA)
    return con


def rows_of(path):
    if not path or not Path(path).exists():
        return
    for line in Path(path).read_text(encoding='utf-8').splitlines():
        if line.strip():
            yield json.loads(line)


def cmd_build(a):
    con = connect(a.db)
    nh = np_ = 0
    for r in rows_of(a.hackathons):
        host = re.sub(r'^https?://|/$', '', r.get('url') or '')
        con.execute("""INSERT OR REPLACE INTO hackathons VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (
            r.get('id'), r.get('title'), host, r.get('url'),
            r.get('organization_name'), r.get('open_state'),
            r.get('submission_period_dates'), prize_parts(r.get('prize_amount'))[2],
            prize_parts(r.get('prize_amount'))[0], prize_parts(r.get('prize_amount'))[1],
            r.get('registrations_count') or 0,
            json.dumps([t.get('name') for t in r.get('themes') or []], ensure_ascii=False),
            int(bool(r.get('winners_announced'))), r.get('submission_gallery_url'),
            int(bool(r.get('featured'))), int(bool(r.get('invite_only'))),
            (r.get('displayed_location') or {}).get('location')))
        nh += 1
    for r in rows_of(a.projects):
        con.execute("""INSERT OR REPLACE INTO projects VALUES (?,?,?,?,?,?,?,?,?,?,?)""", (
            r.get('software_id'), r.get('slug'), r.get('url'), r.get('title'),
            r.get('tagline'), r.get('hackathon_host'), r.get('hackathon_title'),
            r.get('organization_name'), int(bool(r.get('is_winner'))),
            json.dumps(r.get('members') or [], ensure_ascii=False), r.get('gallery_page')))
        np_ += 1
    # projects_fts is an external-content FTS5 table over `projects`. Rebuilding it
    # with DELETE + INSERT corrupts the index ("database disk image is malformed")
    # because the delete tries to reconcile rows against content that has already
    # changed. 'rebuild' is the supported way and re-reads the content table.
    con.execute("INSERT INTO projects_fts(projects_fts) VALUES('rebuild')")
    con.commit()
    print(f'{nh} hackathon rows, {np_} project rows -> {a.db}')
    cmd_stats(a, con)


OPERATORS = re.compile(r'\b(AND|OR|NOT|NEAR)\b|[":*()]')


def fts_query(raw):
    """Bare words default to OR, not FTS5's implicit AND.

    'agent browser automation' as an AND matched nothing across 2,300 winners,
    which reads as "nobody built this" and is the exact wrong conclusion for a
    tool whose job is to stop you believing a scarcity claim. Anything using FTS
    syntax explicitly (quotes, OR, NEAR, *) is passed through untouched.
    """
    if OPERATORS.search(raw):
        return raw
    tokens = [t for t in re.findall(r'[\w]+', raw) if t]
    return ' OR '.join(tokens) if tokens else raw


def cmd_search(a, con=None):
    con = con or connect(a.db)
    where = 'WHERE p.is_winner = 1' if a.winners else ''
    q = """SELECT p.title, p.tagline, p.hackathon_title, p.organization, p.is_winner, p.url
           FROM projects_fts f JOIN projects p ON p.software_id = f.rowid
           {} {} ORDER BY bm25(projects_fts), p.is_winner DESC LIMIT ?"""
    match = 'AND' if where else 'WHERE'
    sql = q.format(where, f'{match} projects_fts MATCH ?')
    try:
        rows = con.execute(sql, (fts_query(a.query), a.limit)).fetchall()
    except sqlite3.OperationalError as exc:
        sys.exit(f'FTS query rejected: {exc}\nQuote phrases: \'"agent browser"\'')
    if not rows:
        print('no match. This is a shortlist tool — widen the query before concluding '
              'nobody has built it.')
        return
    for t, tag, hack, org, win, url in rows:
        star = '★' if win else ' '
        print(f'{star} {(t or "")[:44]:<44} {(hack or "")[:30]:<30} {(org or "")[:16]:<16}')
        if tag:
            print(f'    {tag[:110]}')
        print(f'    {url}')
    print(f'\n{len(rows)} shown. Widen the query until it hurts before trusting a scarcity claim.')


def cmd_orgs(a, con=None):
    con = con or connect(a.db)
    rows = con.execute("""
        SELECT organization, COUNT(*) n, SUM(prize_usd_approx) total, MAX(prize_usd_approx) top,
               SUM(registrations) regs
        FROM hackathons WHERE organization IS NOT NULL AND organization != ''
          AND prize_usd_approx >= ?
        GROUP BY organization ORDER BY total DESC LIMIT ?""",
        (a.min_prize, a.limit)).fetchall()
    print(f'{"organization":<34} {"hacks":>5} {"total prize":>13} {"biggest":>11} {"registrants":>11}')
    for org, n, total, top, regs in rows:
        print(f'{(org or "")[:34]:<34} {n:>5} {total:>13,.0f} {top:>11,.0f} {regs or 0:>11,}')


def cmd_stats(a, con=None):
    con = con or connect(a.db)
    q = lambda s, *p: con.execute(s, p).fetchone()[0]                # noqa: E731
    print(f"""
hackathons          {q('SELECT COUNT(*) FROM hackathons'):>8,}
  open              {q("SELECT COUNT(*) FROM hackathons WHERE state='open'"):>8,}
  winners announced {q('SELECT COUNT(*) FROM hackathons WHERE winners_announced=1'):>8,}
  with a gallery    {q('SELECT COUNT(*) FROM hackathons WHERE gallery_url IS NOT NULL'):>8,}
  prize >= $25k     {q('SELECT COUNT(*) FROM hackathons WHERE prize_usd_approx>=25000'):>8,}
  organisations     {q('SELECT COUNT(DISTINCT organization) FROM hackathons'):>8,}
total prize pool    {q('SELECT COALESCE(SUM(prize_usd_approx),0) FROM hackathons'):>8,.0f}  (USD approx, static rates)
projects            {q('SELECT COUNT(*) FROM projects'):>8,}
  winners           {q('SELECT COUNT(*) FROM projects WHERE is_winner=1'):>8,}
  hackathons covered{q('SELECT COUNT(DISTINCT host) FROM projects'):>8,}""")


def main():
    # --db is accepted on both sides of the subcommand; argparse otherwise rejects
    # the reading that everyone types first.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--db', default='data/ideas.db')

    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0], parents=[common])
    sub = ap.add_subparsers(dest='cmd', required=True)

    b = sub.add_parser('build', parents=[common])
    b.add_argument('--hackathons'); b.add_argument('--projects')
    s = sub.add_parser('search', parents=[common]); s.add_argument('query')
    s.add_argument('--winners', action='store_true'); s.add_argument('--limit', type=int, default=25)
    o = sub.add_parser('orgs', parents=[common])
    o.add_argument('--min-prize', type=float, default=0); o.add_argument('--limit', type=int, default=30)
    sub.add_parser('stats', parents=[common])

    a = ap.parse_args()
    {'build': cmd_build, 'search': cmd_search, 'orgs': cmd_orgs, 'stats': cmd_stats}[a.cmd](a)


if __name__ == '__main__':
    main()
