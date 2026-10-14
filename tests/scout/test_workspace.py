"""Workspace HTTP roundtrips and validation, using an isolated SQLite file."""

import json
import sqlite3
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from pathlib import Path
from unittest.mock import patch

from scout import codex_local, server
from scout.workspace import WorkspaceStore
from scripts.organize_learning_paths import organize
from scripts.seed_video_learning import VIDEO_PROJECT, seed as seed_video_learning, stable_id


class TestWorkspaceHTTP(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix='workspace-test-')
        cls.path = Path(cls.tmp.name) / 'workspace.db'
        server.set_workspace(WorkspaceStore(cls.path))
        cls.http = server.make_server('127.0.0.1', 0)
        cls.base = f'http://127.0.0.1:{cls.http.server_port}'
        cls.thread = threading.Thread(target=cls.http.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.http.shutdown()
        cls.http.server_close()
        server.set_workspace(None)
        cls.tmp.cleanup()

    def test_novel_completion_validation_and_stream(self):
        request = {'mode': 'continue', 'before': 'A working demo', 'selected': '',
                   'after': '', 'instruction': '', 'title': 'Scout demo'}
        status, error = self.request('POST', '/api/codex/complete', {**request, 'mode': 'bad'})
        self.assertEqual((status, error['error']), (400, 'invalid writing mode'))
        with patch.object(codex_local, 'complete_writing', return_value=iter([
            ('delta', {'text': ' next'}), ('done', {'text': ' next step'}),
        ])) as completion:
            req = urllib.request.Request(self.base + '/api/codex/complete',
                                         data=json.dumps(request).encode(), method='POST',
                                         headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, timeout=10) as response:
                stream = response.read().decode()
                self.assertIn('text/event-stream', response.headers['Content-Type'])
        self.assertIn('event: done', stream)
        self.assertIn('next step', stream)
        self.assertEqual(completion.call_args.args[0], request)

    def test_video_learning_seed_preserves_user_edits(self):
        store = WorkspaceStore(self.path)
        project = store.create('projects', {'title': VIDEO_PROJECT})
        path = store.create('learning_paths', {'title': VIDEO_PROJECT, 'project_id': project['id']})
        scout = store.create('projects', {'title': 'Devpost Scout'})
        store.create('learning_paths', {'title': 'Devpost Scout', 'project_id': scout['id'],
                                        'category': 'hackathon'})
        self.assertEqual(seed_video_learning(store), 9)
        lesson = store.get('studies', stable_id('capture'))
        self.assertEqual((lesson['project_id'], lesson['path_id']), (project['id'], path['id']))
        self.assertTrue(store.get('learning_paths', path['id'])['outcome'])
        store.update('studies', lesson['id'], {'body': 'My notes', 'status': 'learning'})
        self.assertEqual(seed_video_learning(store), 0)
        self.assertEqual((store.get('studies', lesson['id'])['body'],
                          store.get('studies', lesson['id'])['status']), ('My notes', 'learning'))

    def request(self, method, path, body=None):
        data = json.dumps(body).encode('utf-8') if body is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method,
                                     headers={'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                return response.status, json.load(response)
        except urllib.error.HTTPError as error:
            with error:
                return error.code, json.load(error)

    def test_project_task_study_agent_roundtrip(self):
        status, project = self.request('POST', '/api/workspace/projects', {'title': 'My project'})
        self.assertEqual(status, 201)
        self.assertEqual(project['status'], 'active')
        status, agent = self.request('POST', '/api/workspace/agents', {'name': 'Research agent'})
        self.assertEqual(status, 201)
        status, task = self.request('POST', '/api/workspace/tasks', {
            'title': 'Read docs', 'project_id': project['id'], 'agent_id': agent['id'],
            'due_on': '2026-10-10'})
        self.assertEqual(status, 201)
        status, study = self.request('POST', '/api/workspace/studies', {
            'title': 'Judging rubric', 'category': 'hackathon',
            'hackathon_host': 'example.devpost.com', 'body': '# Notes',
            'project_id': project['id']})
        self.assertEqual(status, 201)
        status, revised = self.request('PATCH', f'/api/workspace/studies/{study["id"]}',
                                       {'status': 'learning', 'body': '# Updated'})
        self.assertEqual((status, revised['status'], revised['body']), (200, 'learning', '# Updated'))
        status, rows = self.request('GET', '/api/workspace/studies')
        self.assertEqual(status, 200)
        self.assertTrue(any(row['id'] == study['id'] for row in rows))
        reopened = WorkspaceStore(self.path)
        self.assertEqual(reopened.get('studies', study['id'])['status'], 'learning')

        self.assertEqual(self.request('DELETE', f'/api/workspace/projects/{project["id"]}')[0], 200)
        self.assertIsNone(reopened.get('tasks', task['id'])['project_id'])
        self.assertIsNone(reopened.get('studies', study['id'])['project_id'])
        self.assertEqual(self.request('DELETE', f'/api/workspace/agents/{agent["id"]}')[0], 200)
        self.assertIsNone(reopened.get('tasks', task['id'])['agent_id'])

    def test_validation_and_not_found(self):
        cases = [
            ('projects', {'title': '  '}),
            ('tasks', {'title': 'Invalid date', 'due_on': 'tomorrow'}),
            ('tasks', {'title': 'Unknown project', 'project_id': 'missing'}),
            ('studies', {'title': 'Wrong category', 'hackathon_host': 'example.devpost.com'}),
            ('studies', {'title': 'Bad URL', 'source_url': 'javascript:alert(1)'}),
            ('agents', {'name': 'Bad status', 'status': []}),
        ]
        for table, body in cases:
            with self.subTest(table=table, body=body):
                status, result = self.request('POST', f'/api/workspace/{table}', body)
                self.assertEqual(status, 400)
                self.assertIn('error', result)
        status, result = self.request('PATCH', '/api/workspace/tasks/' + 'a' * 32, {'status': 'done'})
        self.assertEqual((status, result['error']), (404, 'item not found'))

    def test_pages_support_nested_project_documents(self):
        status, project = self.request('POST', '/api/workspace/projects', {'title': 'Node project'})
        self.assertEqual(status, 201)
        status, folder = self.request('POST', '/api/workspace/pages', {
            'title': 'Research', 'kind': 'folder', 'space': 'projects', 'project_id': project['id']})
        self.assertEqual(status, 201)
        status, page = self.request('POST', '/api/workspace/pages', {
            'title': 'Brief', 'body': '# Plan', 'space': 'projects',
            'project_id': project['id'], 'parent_id': folder['id']})
        self.assertEqual((status, page['parent_id'], page['body']), (201, folder['id'], '# Plan'))
        self.assertEqual(self.request('PATCH', f'/api/workspace/pages/{folder["id"]}',
                                      {'parent_id': page['id']})[0], 400)
        self.assertEqual(self.request('POST', '/api/workspace/pages', {
            'title': 'Wrong space', 'space': 'learning', 'parent_id': folder['id']})[0], 400)
        self.assertEqual(self.request('POST', '/api/workspace/pages', {
            'title': 'Invalid folder', 'kind': 'folder', 'body': 'Cannot hold text'})[0], 400)
        self.assertEqual(self.request('DELETE', f'/api/workspace/pages/{folder["id"]}')[0], 200)
        self.assertIsNone(WorkspaceStore(self.path).get('pages', page['id'])['parent_id'])
        self.assertEqual(self.request('DELETE', f'/api/workspace/projects/{project["id"]}')[0], 200)
        self.assertIsNone(WorkspaceStore(self.path).get('pages', page['id'])['project_id'])

    def test_project_milestones_and_learning_paths(self):
        status, project = self.request('POST', '/api/workspace/projects', {
            'title': 'Build workspace', 'goal': 'Working project hub',
            'next_action': 'Write a brief', 'target_on': '2026-11-01'})
        self.assertEqual(status, 201)
        status, milestone = self.request('POST', '/api/workspace/milestones', {
            'title': 'First release', 'project_id': project['id'], 'due_on': '2026-10-20'})
        self.assertEqual(status, 201)
        status, task = self.request('POST', '/api/workspace/tasks', {
            'title': 'Ship editor', 'project_id': project['id'], 'milestone_id': milestone['id']})
        self.assertEqual((status, task['milestone_id']), (201, milestone['id']))
        status, other = self.request('POST', '/api/workspace/projects', {'title': 'Other'})
        self.assertEqual(status, 201)
        self.assertEqual(self.request('POST', '/api/workspace/tasks', {
            'title': 'Wrong milestone', 'project_id': other['id'],
            'milestone_id': milestone['id']})[0], 400)
        status, path = self.request('POST', '/api/workspace/learning_paths', {
            'title': 'Editor basics', 'outcome': 'Can edit Markdown',
            'category': 'general', 'project_id': project['id']})
        self.assertEqual(status, 201)
        status, study = self.request('POST', '/api/workspace/studies', {
            'title': 'Novel', 'path_id': path['id'], 'project_id': project['id'],
            'objective': 'Write a structured note', 'review_on': '2026-10-12',
            'body': '# Existing content\n\nKeep this.'})
        self.assertEqual((status, study['path_id']), (201, path['id']))
        self.assertEqual(self.request('POST', '/api/workspace/studies', {
            'title': 'Wrong category', 'category': 'hackathon', 'path_id': path['id']})[0], 400)
        self.assertEqual(self.request('PATCH', f'/api/workspace/learning_paths/{path["id"]}',
                                      {'category': 'hackathon'})[0], 400)
        reopened = WorkspaceStore(self.path)
        self.assertEqual(reopened.get('studies', study['id'])['body'], '# Existing content\n\nKeep this.')
        self.assertEqual(reopened.get('projects', project['id'])['next_action'], 'Write a brief')
        self.assertEqual(self.request('DELETE', f'/api/workspace/milestones/{milestone["id"]}')[0], 200)
        self.assertIsNone(reopened.get('tasks', task['id'])['milestone_id'])
        self.assertEqual(self.request('DELETE', f'/api/workspace/learning_paths/{path["id"]}')[0], 200)
        self.assertIsNone(reopened.get('studies', study['id'])['path_id'])

    def test_legacy_study_migration_preserves_notes(self):
        with tempfile.TemporaryDirectory(prefix='workspace-legacy-') as directory:
            path = Path(directory) / 'workspace.db'
            with sqlite3.connect(path) as db:
                db.executescript('''
                    CREATE TABLE projects (id TEXT PRIMARY KEY, title TEXT, description TEXT,
                        status TEXT, created_at TEXT, updated_at TEXT);
                    CREATE TABLE studies (id TEXT PRIMARY KEY, title TEXT, summary TEXT, body TEXT,
                        status TEXT, category TEXT, source_url TEXT, project_id TEXT,
                        hackathon_host TEXT, created_at TEXT, updated_at TEXT);
                    INSERT INTO projects VALUES ('p', 'Learning roadmap', '', 'active', '2026', '2026');
                    INSERT INTO studies VALUES ('s', 'OS notes', '', '# Processes', 'inbox',
                        'general', '', 'p', '', '2026', '2026');
                ''')
            store = WorkspaceStore(path)
            migrated = store.get('studies', 's')
            self.assertEqual(migrated['body'], '# Processes')
            self.assertEqual(store.get('learning_paths', migrated['path_id'])['title'], 'Learning roadmap')
            self.assertEqual(len(WorkspaceStore(path).list('learning_paths')), 1)

    def test_topic_organizer_keeps_unclassified_notes_and_links(self):
        with tempfile.TemporaryDirectory(prefix='workspace-topics-') as directory:
            store = WorkspaceStore(Path(directory) / 'workspace.db')
            project = store.create('projects', {'title': '개인 학습 로드맵'})
            original = store.create('learning_paths', {
                'title': project['title'], 'project_id': project['id']})
            source = store.create('studies', {'title': '운영체제 기초와 프로세스',
                'body': '# Original\n\n[Source](https://example.org)',
                'source_url': 'https://example.org', 'project_id': project['id'],
                'path_id': original['id']})
            unknown = store.create('studies', {'title': 'youtu.be/unknown',
                'body': 'Keep this link', 'project_id': project['id'],
                'path_id': original['id']})
            self.assertEqual(organize(store), 1)
            self.assertEqual(organize(store), 0)
            self.assertEqual(store.get('studies', source['id'])['body'], source['body'])
            self.assertEqual(store.get('studies', source['id'])['source_url'], source['source_url'])
            self.assertNotEqual(store.get('studies', source['id'])['path_id'], original['id'])
            self.assertEqual(store.get('studies', unknown['id'])['path_id'], original['id'])

    def test_codex_chat_persists_and_resumes(self):
        status, chat = self.request('POST', '/api/codex/chats', {})
        self.assertEqual(status, 201)
        thread_ids = []

        def fake_stream(thread_id, message, store):
            thread_ids.append(thread_id)
            yield 'thread', {'id': 'codex-test-thread'}
            yield 'delta', {'text': 'Hello'}
            yield 'done', {'text': f'Hello {message}'}

        with patch('scout.codex_local.stream', side_effect=fake_stream):
            for message in ('first', 'second'):
                req = urllib.request.Request(
                    self.base + f'/api/codex/chats/{chat["id"]}/messages',
                    data=json.dumps({'text': message}).encode(), method='POST',
                    headers={'Content-Type': 'application/json'})
                with urllib.request.urlopen(req, timeout=10) as response:
                    events = response.read().decode()
                self.assertIn('event: done', events)
                self.assertIn(f'Hello {message}', events)
        self.assertEqual(thread_ids, [None, 'codex-test-thread'])
        status, saved = self.request('GET', f'/api/codex/chats/{chat["id"]}')
        self.assertEqual(status, 200)
        self.assertEqual(saved['title'], 'first')
        self.assertEqual([item['role'] for item in saved['messages']],
                         ['user', 'assistant', 'user', 'assistant'])
        self.assertEqual(saved['messages'][-1]['text'], 'Hello second')
        self.assertEqual(self.request('DELETE', f'/api/codex/chats/{chat["id"]}')[0], 200)
        self.assertEqual(self.request('GET', f'/api/codex/chats/{chat["id"]}')[0], 404)

    def test_codex_message_validation(self):
        status, chat = self.request('POST', '/api/codex/chats', {})
        self.assertEqual(status, 201)
        for body in ({'text': ''}, {'text': 12}, {'other': 'hi'}, {'text': 'x' * 10001}):
            with self.subTest(body=str(body)[:40]):
                self.assertEqual(self.request('POST', f'/api/codex/chats/{chat["id"]}/messages', body)[0], 400)
        self.assertEqual(self.request('DELETE', f'/api/codex/chats/{chat["id"]}')[0], 200)

    def test_codex_snapshot_tracks_workspace_data(self):
        with tempfile.TemporaryDirectory(prefix='codex-context-') as directory:
            store = WorkspaceStore(Path(directory) / 'workspace.db')
            project = store.create('projects', {'title': 'Example project'})
            store.create('tasks', {'title': 'Review API', 'project_id': project['id']})
            store.create('studies', {'title': 'SQLite notes', 'body': '# Private details'})
            context = json.loads(codex_local.snapshot(store))
            self.assertEqual(context['projects'][0]['title'], 'Example project')
            self.assertEqual(context['tasks'][0]['project_id'], project['id'])
            self.assertEqual(context['studies'][0]['title'], 'SQLite notes')
            self.assertNotIn('body', context['studies'][0])


if __name__ == '__main__':
    unittest.main()
