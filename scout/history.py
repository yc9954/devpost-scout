"""Searchable, local provenance for imported personal notes and session prompts."""

import json
import sqlite3
from contextlib import contextmanager
from pathlib import Path

from scout import config


SCHEMA = """
CREATE TABLE IF NOT EXISTS imported_notes (
    id TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    source_id TEXT NOT NULL,
    occurred_at TEXT NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    kind TEXT NOT NULL,
    urls_json TEXT NOT NULL DEFAULT '[]',
    source_url TEXT NOT NULL DEFAULT '',
    session_path TEXT NOT NULL DEFAULT '',
    project_key TEXT NOT NULL DEFAULT '',
    sensitive INTEGER NOT NULL DEFAULT 0,
    partial INTEGER NOT NULL DEFAULT 0,
    linked_type TEXT NOT NULL DEFAULT '',
    linked_id TEXT NOT NULL DEFAULT '',
    UNIQUE(source, source_id)
);
CREATE INDEX IF NOT EXISTS imported_notes_date ON imported_notes(occurred_at DESC);
CREATE INDEX IF NOT EXISTS imported_notes_source ON imported_notes(source, occurred_at DESC);
CREATE INDEX IF NOT EXISTS imported_notes_kind ON imported_notes(kind, occurred_at DESC);
CREATE INDEX IF NOT EXISTS imported_notes_project ON imported_notes(project_key, occurred_at DESC);
CREATE VIRTUAL TABLE IF NOT EXISTS imported_notes_fts USING fts5(
    title, body, content='imported_notes', content_rowid='rowid', tokenize='unicode61'
);
CREATE TRIGGER IF NOT EXISTS imported_notes_ai AFTER INSERT ON imported_notes BEGIN
    INSERT INTO imported_notes_fts(rowid, title, body) VALUES (new.rowid, new.title, new.body);
END;
CREATE TRIGGER IF NOT EXISTS imported_notes_ad AFTER DELETE ON imported_notes BEGIN
    INSERT INTO imported_notes_fts(imported_notes_fts, rowid, title, body)
    VALUES ('delete', old.rowid, old.title, old.body);
END;
CREATE TRIGGER IF NOT EXISTS imported_notes_au AFTER UPDATE ON imported_notes BEGIN
    INSERT INTO imported_notes_fts(imported_notes_fts, rowid, title, body)
    VALUES ('delete', old.rowid, old.title, old.body);
    INSERT INTO imported_notes_fts(rowid, title, body) VALUES (new.rowid, new.title, new.body);
END;
"""


class HistoryStore:
    def __init__(self, path=None):
        self.path = Path(path or config.DATA / 'workspace.db')
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self._db() as db:
            db.executescript(SCHEMA)
        self.path.chmod(0o600)

    @contextmanager
    def _db(self):
        db = sqlite3.connect(self.path, timeout=10)
        db.row_factory = sqlite3.Row
        db.execute('PRAGMA busy_timeout = 10000')
        try:
            yield db
            db.commit()
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()

    def replace(self, records):
        """Idempotent refresh of the imported provenance corpus."""
        records = list(records)
        fields = ('id', 'source', 'source_id', 'occurred_at', 'title', 'body', 'kind',
                  'urls_json', 'source_url', 'session_path', 'project_key', 'sensitive', 'partial',
                  'linked_type', 'linked_id')
        with self._db() as db:
            db.execute('CREATE TEMP TABLE import_current_ids (id TEXT PRIMARY KEY)')
            db.executemany('INSERT INTO import_current_ids (id) VALUES (?)',
                           ((record['id'],) for record in records))
            db.executemany(
                f'INSERT INTO imported_notes ({", ".join(fields)}) VALUES ({", ".join("?" for _ in fields)}) '
                'ON CONFLICT(id) DO UPDATE SET occurred_at=excluded.occurred_at, '
                'title=excluded.title, body=excluded.body, kind=excluded.kind, '
                'urls_json=excluded.urls_json, source_url=excluded.source_url, '
                'session_path=excluded.session_path, project_key=excluded.project_key, '
                'sensitive=excluded.sensitive, partial=excluded.partial',
                (tuple(record.get(key, '') for key in fields) for record in records),
            )
            db.execute('DELETE FROM imported_notes WHERE id NOT IN (SELECT id FROM import_current_ids)')
            db.commit()

    def stats(self):
        with self._db() as db:
            total = db.execute('SELECT COUNT(*) FROM imported_notes').fetchone()[0]
            sources = {row['source']: row['n'] for row in db.execute(
                'SELECT source, COUNT(*) n FROM imported_notes GROUP BY source')}
            kinds = {row['kind']: row['n'] for row in db.execute(
                'SELECT kind, COUNT(*) n FROM imported_notes GROUP BY kind')}
            links = db.execute('SELECT COUNT(*) FROM imported_notes WHERE urls_json != ?', ('[]',)).fetchone()[0]
            partial = db.execute('SELECT COUNT(*) FROM imported_notes WHERE partial = 1').fetchone()[0]
            history_total = sources.get('codex-history', 0) + sources.get('claude-history', 0)
            personal_total = total - kinds.get('result', 0) - history_total
            personal_links = db.execute("SELECT COUNT(*) FROM imported_notes WHERE kind = 'link' "
                                        "AND source NOT IN ('codex-history', 'claude-history')").fetchone()[0]
            return {'total': total, 'personal_total': personal_total,
                    'history_total': history_total, 'agent_total': kinds.get('result', 0),
                    'personal_links': personal_links, 'sources': sources, 'kinds': kinds,
                    'with_links': links, 'partial': partial}

    def search(self, query='', source='', kind='', project='', limit=50, offset=0, scope='all'):
        limit = min(max(int(limit), 1), 100)
        offset = max(int(offset), 0)
        clauses, args = [], []
        if scope == 'mine':
            clauses.append("n.source NOT IN ('codex-history', 'claude-history', 'codex-result', 'claude-result')")
        elif scope == 'history':
            clauses.append("n.source IN ('codex-history', 'claude-history')")
        elif scope == 'agent':
            clauses.append("n.kind = 'result'")
        elif scope != 'all':
            raise ValueError('invalid search scope')
        if source:
            clauses.append('n.source = ?'); args.append(source)
        if kind:
            clauses.append('n.kind = ?'); args.append(kind)
        if project:
            clauses.append('n.project_key = ?'); args.append(project)
        # LIKE handles punctuation and Korean substrings that FTS tokenisation misses.
        if query.strip():
            clauses.append("(n.title LIKE ? ESCAPE '\\' OR n.body LIKE ? ESCAPE '\\' OR n.urls_json LIKE ? ESCAPE '\\')")
            term = '%' + query.strip().replace('%', '\\%').replace('_', '\\_') + '%'
            args.extend((term, term, term))
        where = (' WHERE ' + ' AND '.join(clauses)) if clauses else ''
        with self._db() as db:
            count = db.execute('SELECT COUNT(*) FROM imported_notes n' + where, args).fetchone()[0]
            rows = [dict(row) for row in db.execute(
                'SELECT n.id, n.source, n.occurred_at, n.title, '
                'substr(n.body, 1, 350) AS excerpt, n.kind, n.urls_json, n.source_url, '
                'n.project_key, n.sensitive, n.partial, n.linked_type, n.linked_id '
                'FROM imported_notes n' + where +
                ' ORDER BY n.occurred_at DESC, n.id DESC LIMIT ? OFFSET ?', (*args, limit, offset))]
        for row in rows:
            row['urls'] = json.loads(row.pop('urls_json'))
        return {'total': count, 'items': rows, 'limit': limit, 'offset': offset}

    def get(self, note_id):
        with self._db() as db:
            row = db.execute('SELECT * FROM imported_notes WHERE id = ?', (note_id,)).fetchone()
        if not row:
            return None
        value = dict(row)
        value['urls'] = json.loads(value.pop('urls_json'))
        return value

    def link(self, note_id, linked_type, linked_id):
        if linked_type not in ('projects', 'tasks', 'studies') or len(linked_id) != 32:
            raise ValueError('invalid link target')
        with self._db() as db:
            target = db.execute(f'SELECT 1 FROM {linked_type} WHERE id = ?', (linked_id,)).fetchone()
            if not target:
                raise LookupError('target item not found')
            result = db.execute('UPDATE imported_notes SET linked_type = ?, linked_id = ? WHERE id = ?',
                                (linked_type, linked_id, note_id))
            if not result.rowcount:
                raise LookupError('imported note not found')
            db.commit()
        return self.get(note_id)
