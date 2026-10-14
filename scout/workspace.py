"""Local, single-user workspace data kept apart from Scout's research corpus."""

import sqlite3
import uuid
from contextlib import contextmanager
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

from scout import config


class WorkspaceError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status


SCHEMA = """
CREATE TABLE IF NOT EXISTS projects (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL DEFAULT '',
    goal TEXT NOT NULL DEFAULT '',
    next_action TEXT NOT NULL DEFAULT '',
    target_on TEXT,
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('planned', 'active', 'paused', 'done')),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS milestones (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    project_id TEXT NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    due_on TEXT,
    status TEXT NOT NULL DEFAULT 'planned' CHECK (status IN ('planned', 'doing', 'done')),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS learning_paths (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    outcome TEXT NOT NULL DEFAULT '',
    category TEXT NOT NULL DEFAULT 'general' CHECK (category IN ('general', 'hackathon')),
    project_id TEXT REFERENCES projects(id) ON DELETE SET NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS agents (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT '',
    launch_url TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'paused')),
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS tasks (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    details TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'todo' CHECK (status IN ('todo', 'doing', 'done')),
    priority TEXT NOT NULL DEFAULT 'medium' CHECK (priority IN ('low', 'medium', 'high')),
    due_on TEXT,
    project_id TEXT REFERENCES projects(id) ON DELETE SET NULL,
    milestone_id TEXT REFERENCES milestones(id) ON DELETE SET NULL,
    agent_id TEXT REFERENCES agents(id) ON DELETE SET NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS studies (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    summary TEXT NOT NULL DEFAULT '',
    body TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'inbox' CHECK (status IN ('inbox', 'learning', 'reviewing', 'mastered')),
    category TEXT NOT NULL DEFAULT 'general' CHECK (category IN ('general', 'hackathon')),
    source_url TEXT NOT NULL DEFAULT '',
    project_id TEXT REFERENCES projects(id) ON DELETE SET NULL,
    path_id TEXT REFERENCES learning_paths(id) ON DELETE SET NULL,
    objective TEXT NOT NULL DEFAULT '',
    review_on TEXT,
    hackathon_host TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS pages (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    body TEXT NOT NULL DEFAULT '',
    kind TEXT NOT NULL DEFAULT 'page' CHECK (kind IN ('page', 'folder')),
    space TEXT NOT NULL DEFAULT 'personal' CHECK (space IN ('personal', 'projects', 'learning', 'scout')),
    parent_id TEXT REFERENCES pages(id) ON DELETE SET NULL,
    project_id TEXT REFERENCES projects(id) ON DELETE SET NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS pages_parent ON pages(parent_id);
CREATE INDEX IF NOT EXISTS pages_project ON pages(project_id);
CREATE INDEX IF NOT EXISTS pages_space ON pages(space);
CREATE INDEX IF NOT EXISTS tasks_project ON tasks(project_id);
CREATE INDEX IF NOT EXISTS tasks_agent ON tasks(agent_id);
CREATE INDEX IF NOT EXISTS studies_project ON studies(project_id);
CREATE INDEX IF NOT EXISTS studies_category ON studies(category);
CREATE TABLE IF NOT EXISTS codex_chats (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL DEFAULT 'New chat',
    codex_thread_id TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS codex_messages (
    id TEXT PRIMARY KEY,
    chat_id TEXT NOT NULL REFERENCES codex_chats(id) ON DELETE CASCADE,
    role TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'error')),
    text TEXT NOT NULL,
    created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS codex_messages_chat ON codex_messages(chat_id, created_at);
"""

FIELDS = {
    'projects': {'title', 'description', 'goal', 'next_action', 'target_on', 'status'},
    'milestones': {'title', 'project_id', 'due_on', 'status'},
    'learning_paths': {'title', 'outcome', 'category', 'project_id'},
    'pages': {'title', 'body', 'kind', 'space', 'parent_id', 'project_id'},
    'tasks': {'title', 'details', 'status', 'priority', 'due_on', 'project_id', 'milestone_id', 'agent_id'},
    'studies': {'title', 'summary', 'body', 'status', 'category', 'source_url', 'project_id', 'path_id', 'objective', 'review_on', 'hackathon_host'},
    'agents': {'name', 'role', 'launch_url', 'status'},
}
DEFAULTS = {
    'projects': {'description': '', 'goal': '', 'next_action': '', 'target_on': None, 'status': 'active'},
    'milestones': {'due_on': None, 'status': 'planned'},
    'learning_paths': {'outcome': '', 'category': 'general', 'project_id': None},
    'pages': {'body': '', 'kind': 'page', 'space': 'personal', 'parent_id': None,
              'project_id': None},
    'tasks': {'details': '', 'status': 'todo', 'priority': 'medium', 'due_on': None,
              'project_id': None, 'milestone_id': None, 'agent_id': None},
    'studies': {'summary': '', 'body': '', 'status': 'inbox', 'category': 'general',
                'source_url': '', 'project_id': None, 'path_id': None, 'objective': '',
                'review_on': None, 'hackathon_host': ''},
    'agents': {'role': '', 'launch_url': '', 'status': 'active'},
}
ENUMS = {
    'projects': {'status': {'planned', 'active', 'paused', 'done'}},
    'milestones': {'status': {'planned', 'doing', 'done'}},
    'learning_paths': {'category': {'general', 'hackathon'}},
    'pages': {'kind': {'page', 'folder'},
              'space': {'personal', 'projects', 'learning', 'scout'}},
    'tasks': {'status': {'todo', 'doing', 'done'}, 'priority': {'low', 'medium', 'high'}},
    'studies': {'status': {'inbox', 'learning', 'reviewing', 'mastered'},
                'category': {'general', 'hackathon'}},
    'agents': {'status': {'active', 'paused'}},
}
TEXT_LIMITS = {'title': 200, 'name': 120, 'description': 10000, 'goal': 1000,
               'next_action': 1000, 'outcome': 2000, 'objective': 2000, 'details': 20000,
               'summary': 2000, 'body': 100000, 'role': 500, 'source_url': 2000,
               'launch_url': 2000, 'hackathon_host': 255}


def _now():
    return datetime.now(timezone.utc).isoformat(timespec='milliseconds')


class WorkspaceStore:
    def __init__(self, path=None):
        self.path = Path(path or config.DATA / 'workspace.db')
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self._db() as db:
            db.executescript(SCHEMA)
            legacy_studies = 'path_id' not in {row['name'] for row in db.execute('PRAGMA table_info(studies)')}
            additions = {
                'projects': {'goal': "TEXT NOT NULL DEFAULT ''", 'next_action': "TEXT NOT NULL DEFAULT ''", 'target_on': 'TEXT'},
                'tasks': {'milestone_id': 'TEXT REFERENCES milestones(id) ON DELETE SET NULL'},
                'studies': {'path_id': 'TEXT REFERENCES learning_paths(id) ON DELETE SET NULL',
                            'objective': "TEXT NOT NULL DEFAULT ''", 'review_on': 'TEXT'},
            }
            for table, columns in additions.items():
                existing = {row['name'] for row in db.execute(f'PRAGMA table_info({table})')}
                for column, declaration in columns.items():
                    if column not in existing:
                        db.execute(f'ALTER TABLE {table} ADD COLUMN {column} {declaration}')
            db.execute('CREATE INDEX IF NOT EXISTS tasks_milestone ON tasks(milestone_id)')
            db.execute('CREATE INDEX IF NOT EXISTS studies_path ON studies(path_id)')
            db.execute('CREATE INDEX IF NOT EXISTS milestones_project ON milestones(project_id)')
            if legacy_studies:
                self._group_existing_studies(db)
        self.path.chmod(0o600)

    @staticmethod
    def _group_existing_studies(db):
        """Give imported study records a navigable starting path without changing their content."""
        groups = db.execute('''SELECT s.project_id, s.category, p.title AS project_title
            FROM studies s JOIN projects p ON p.id = s.project_id
            WHERE s.path_id IS NULL GROUP BY s.project_id, s.category''').fetchall()
        for group in groups:
            path_id, timestamp = uuid.uuid4().hex, _now()
            db.execute('''INSERT INTO learning_paths
                (id, title, outcome, category, project_id, created_at, updated_at)
                VALUES (?, ?, '', ?, ?, ?, ?)''',
                (path_id, group['project_title'], group['category'], group['project_id'], timestamp, timestamp))
            db.execute('UPDATE studies SET path_id = ? WHERE project_id = ? AND category = ? AND path_id IS NULL',
                       (path_id, group['project_id'], group['category']))

    def _connect(self):
        db = sqlite3.connect(self.path, timeout=5)
        db.row_factory = sqlite3.Row
        db.execute('PRAGMA foreign_keys = ON')
        db.execute('PRAGMA busy_timeout = 5000')
        return db

    @contextmanager
    def _db(self):
        db = self._connect()
        try:
            yield db
            db.commit()
        except Exception:
            db.rollback()
            raise
        finally:
            db.close()

    def list(self, table):
        self._table(table)
        with self._db() as db:
            return [dict(row) for row in db.execute(
                f'SELECT * FROM {table} ORDER BY updated_at DESC, created_at DESC')]

    def get(self, table, item_id):
        self._table(table)
        with self._db() as db:
            row = db.execute(f'SELECT * FROM {table} WHERE id = ?', (item_id,)).fetchone()
            return dict(row) if row else None

    def create(self, table, data):
        values = self._validate(table, data, create=True)
        item_id, timestamp = uuid.uuid4().hex, _now()
        row = {'id': item_id, **values, 'created_at': timestamp, 'updated_at': timestamp}
        with self._db() as db:
            self._check_relations(db, table, row)
            if table == 'pages':
                self._check_page_tree(db, row)
            keys = list(row)
            db.execute(f'INSERT INTO {table} ({", ".join(keys)}) VALUES ({", ".join("?" for _ in keys)})',
                       tuple(row[k] for k in keys))
        return row

    def update(self, table, item_id, data):
        self._table(table)
        if not isinstance(data, dict) or not data:
            raise WorkspaceError(400, 'at least one field is required')
        existing = self.get(table, item_id)
        if not existing:
            raise WorkspaceError(404, 'item not found')
        values = self._validate(table, data)
        row = {**existing, **values, 'updated_at': _now()}
        if table == 'studies' and row['category'] == 'general' and row['hackathon_host']:
            raise WorkspaceError(400, 'hackathon_host requires hackathon category')
        with self._db() as db:
            self._check_relations(db, table, row)
            if table == 'learning_paths' and db.execute(
                'SELECT 1 FROM studies WHERE path_id = ? AND category != ? LIMIT 1',
                (item_id, row['category'])).fetchone():
                raise WorkspaceError(400, 'move study items before changing the learning path category')
            if table == 'milestones' and db.execute(
                'SELECT 1 FROM tasks WHERE milestone_id = ? AND project_id != ? LIMIT 1',
                (item_id, row['project_id'])).fetchone():
                raise WorkspaceError(400, 'move to dos before changing the milestone project')
            if table == 'pages':
                self._check_page_tree(db, row)
            db.execute(f'UPDATE {table} SET {", ".join(f"{key} = ?" for key in values)}, updated_at = ? WHERE id = ?',
                       (*values.values(), row['updated_at'], item_id))
        return row

    def delete(self, table, item_id):
        self._table(table)
        with self._db() as db:
            cur = db.execute(f'DELETE FROM {table} WHERE id = ?', (item_id,))
            if cur.rowcount == 0:
                raise WorkspaceError(404, 'item not found')

    def list_codex_chats(self):
        with self._db() as db:
            return [dict(row) for row in db.execute(
                'SELECT id, title, created_at, updated_at FROM codex_chats ORDER BY updated_at DESC')]

    def get_codex_chat(self, chat_id):
        with self._db() as db:
            row = db.execute('SELECT * FROM codex_chats WHERE id = ?', (chat_id,)).fetchone()
            if row is None:
                return None
            return {**dict(row), 'messages': [dict(message) for message in db.execute(
                'SELECT id, role, text, created_at FROM codex_messages WHERE chat_id = ? ORDER BY created_at, rowid',
                (chat_id,))]}

    def create_codex_chat(self):
        row = {'id': uuid.uuid4().hex, 'title': 'New chat',
               'created_at': _now(), 'updated_at': _now()}
        with self._db() as db:
            db.execute('INSERT INTO codex_chats (id, title, created_at, updated_at) VALUES (?, ?, ?, ?)',
                       tuple(row.values()))
        return row

    def delete_codex_chat(self, chat_id):
        with self._db() as db:
            if db.execute('DELETE FROM codex_chats WHERE id = ?', (chat_id,)).rowcount == 0:
                raise WorkspaceError(404, 'chat not found')

    def set_codex_thread(self, chat_id, thread_id):
        with self._db() as db:
            db.execute('UPDATE codex_chats SET codex_thread_id = ?, updated_at = ? WHERE id = ?',
                       (thread_id, _now(), chat_id))

    def add_codex_message(self, chat_id, role, text):
        if role not in ('user', 'assistant', 'error'):
            raise ValueError('invalid Codex message role')
        row = {'id': uuid.uuid4().hex, 'role': role, 'text': text, 'created_at': _now()}
        with self._db() as db:
            if not db.execute('SELECT 1 FROM codex_chats WHERE id = ?', (chat_id,)).fetchone():
                raise WorkspaceError(404, 'chat not found')
            db.execute('INSERT INTO codex_messages (id, chat_id, role, text, created_at) VALUES (?, ?, ?, ?, ?)',
                       (row['id'], chat_id, role, text, row['created_at']))
            if role == 'user':
                db.execute("UPDATE codex_chats SET title = CASE WHEN title = 'New chat' THEN ? ELSE title END, updated_at = ? WHERE id = ?",
                           (text.strip()[:60] or 'New chat', row['created_at'], chat_id))
            else:
                db.execute('UPDATE codex_chats SET updated_at = ? WHERE id = ?', (row['created_at'], chat_id))
        return row

    @staticmethod
    def _table(table):
        if table not in FIELDS:
            raise WorkspaceError(404, 'unknown workspace collection')

    def _validate(self, table, data, create=False):
        self._table(table)
        if not isinstance(data, dict):
            raise WorkspaceError(400, 'body must be a JSON object')
        extra = set(data) - FIELDS[table]
        if extra:
            raise WorkspaceError(400, f'unknown field: {sorted(extra)[0]}')
        values = {**DEFAULTS[table], **data} if create else dict(data)
        required = 'name' if table == 'agents' else 'title'
        if create and required not in values:
            raise WorkspaceError(400, f'{required} is required')
        if create and table == 'milestones' and not values.get('project_id'):
            raise WorkspaceError(400, 'project_id is required')
        for key, value in values.items():
            if key in TEXT_LIMITS:
                if not isinstance(value, str) or len(value) > TEXT_LIMITS[key]:
                    raise WorkspaceError(400, f'{key} must be text of at most {TEXT_LIMITS[key]} characters')
                values[key] = value.strip() if key in ('title', 'name', 'source_url', 'launch_url', 'hackathon_host') else value
                if key in ('title', 'name') and not values[key]:
                    raise WorkspaceError(400, f'{key} is required')
            elif key in ENUMS[table]:
                if not isinstance(value, str) or value not in ENUMS[table][key]:
                    raise WorkspaceError(400, f'invalid {key}')
            elif key in ('project_id', 'agent_id', 'parent_id', 'milestone_id', 'path_id'):
                if value is not None and (not isinstance(value, str) or not value):
                    raise WorkspaceError(400, f'{key} must be an ID or null')
            elif key in ('due_on', 'target_on', 'review_on'):
                if value is not None:
                    try:
                        if not isinstance(value, str) or date.fromisoformat(value).isoformat() != value:
                            raise ValueError()
                    except ValueError:
                        raise WorkspaceError(400, f'{key} must be YYYY-MM-DD or null') from None
        for key in ('source_url', 'launch_url'):
            if key in values and values[key]:
                parsed = urlsplit(values[key])
                if parsed.scheme not in ('http', 'https') or not parsed.netloc:
                    raise WorkspaceError(400, f'{key} must be an http(s) URL')
        if table == 'studies' and values.get('category') == 'general' and values.get('hackathon_host'):
            raise WorkspaceError(400, 'hackathon_host requires hackathon category')
        if table == 'milestones' and 'project_id' in values and not values['project_id']:
            raise WorkspaceError(400, 'project_id is required')
        return values

    @staticmethod
    def _check_relations(db, table, row):
        for key, target in (('project_id', 'projects'), ('agent_id', 'agents'),
                            ('parent_id', 'pages'), ('milestone_id', 'milestones'),
                            ('path_id', 'learning_paths')):
            if key not in FIELDS[table] or not row.get(key):
                continue
            if not db.execute(f'SELECT 1 FROM {target} WHERE id = ?', (row[key],)).fetchone():
                raise WorkspaceError(400, f'{key} does not exist')
        if table == 'tasks' and row.get('milestone_id'):
            milestone = db.execute('SELECT project_id FROM milestones WHERE id = ?', (row['milestone_id'],)).fetchone()
            if milestone['project_id'] != row.get('project_id'):
                raise WorkspaceError(400, 'milestone must belong to the selected project')
        if table == 'studies' and row.get('path_id'):
            path = db.execute('SELECT category FROM learning_paths WHERE id = ?', (row['path_id'],)).fetchone()
            if path['category'] != row.get('category'):
                raise WorkspaceError(400, 'learning path must match the study category')

    @staticmethod
    def _check_page_tree(db, row):
        if row['kind'] == 'folder' and row['body']:
            raise WorkspaceError(400, 'folders cannot have a body')
        if row['project_id'] and row['space'] != 'projects':
            raise WorkspaceError(400, 'project pages must be in the projects space')
        parent_id = row['parent_id']
        if not parent_id:
            return
        seen = {row['id']}
        while parent_id:
            if parent_id in seen:
                raise WorkspaceError(400, 'page hierarchy cannot contain a cycle')
            seen.add(parent_id)
            parent = db.execute('SELECT parent_id, space, project_id FROM pages WHERE id = ?',
                                (parent_id,)).fetchone()
            if parent['space'] != row['space'] or parent['project_id'] != row['project_id']:
                raise WorkspaceError(400, 'parent page must be in the same space and project')
            parent_id = parent['parent_id']
