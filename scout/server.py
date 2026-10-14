"""ThreadingHTTPServer with the routes in SPEC §3. JSON everywhere, SSE for chat
messages and job streams, static web/dist with SPA fallback."""
import json
import mimetypes
import re
import sys
import threading
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, quote, unquote, urlsplit

from scout import codex_local, config, jobs, local_agent, tools
from scout.data import ChatStore
from scout.history import HistoryStore
from scout.studio import StudioError, StudioLibrary
from scout.workspace import WorkspaceError, WorkspaceStore

_chats = None
_chats_lock = threading.Lock()
_workspace = None
_workspace_lock = threading.Lock()
_codex_active = set()
_codex_active_lock = threading.Lock()
_studio = None
_studio_lock = threading.Lock()
_history = None
_history_lock = threading.Lock()


def chats():
    global _chats
    with _chats_lock:
        if _chats is None:
            _chats = ChatStore()
        return _chats


def set_chats(store):
    global _chats
    _chats = store


def workspace():
    global _workspace
    with _workspace_lock:
        if _workspace is None:
            _workspace = WorkspaceStore()
        return _workspace


def set_workspace(store):
    global _workspace
    with _workspace_lock:
        _workspace = store


def studio():
    global _studio
    with _studio_lock:
        if _studio is None:
            _studio = StudioLibrary()
        return _studio


def set_studio(library):
    global _studio
    with _studio_lock:
        _studio = library


def history():
    global _history
    with _history_lock:
        if _history is None:
            _history = HistoryStore()
        return _history


def validate_studio_project(project_id):
    if project_id is None:
        return None
    if not isinstance(project_id, str) or not re.fullmatch(r'[a-f0-9]{32}', project_id):
        raise StudioError(400, 'invalid project_id')
    if workspace().get('projects', project_id) is None:
        raise StudioError(400, 'project not found')
    return project_id


FALLBACK_HTML = """<!doctype html><html><head><meta charset="utf-8"><title>Workspace API</title>
<style>body{{font:15px/1.5 system-ui;margin:2rem auto;max-width:44rem;color:#ddd;background:#111}}
code{{background:#222;padding:.1em .3em;border-radius:3px}}</style></head><body>
<h1>Workspace · Scout</h1><p>The web UI is not built (<code>web/dist/index.html</code> missing). Scout mode: <b>{mode}</b>.</p>
<ul>
<li>GET <a href="/api/health">/api/health</a></li>
<li>GET /api/workspace/projects · /tasks · /studies · /agents</li>
<li>GET <a href="/api/hackathons?status=open&limit=10">/api/hackathons?status=&amp;q=&amp;theme=&amp;sort=&amp;limit=</a></li>
<li>GET /api/hackathons/{{id}}</li>
<li>GET <a href="/api/stats">/api/stats</a></li>
<li>GET <a href="/api/winners?q=agent&limit=10">/api/winners?q=&amp;limit=</a></li>
<li>GET <a href="/api/chats">/api/chats</a> · POST /api/chats · GET /api/chats/{{id}}</li>
<li>POST /api/chats/{{id}}/messages {{text}} → SSE</li>
<li>POST /api/jobs/scout {{hackathon}} · POST /api/jobs/refresh · GET /api/jobs · GET /api/jobs/{{id}}/stream → SSE</li>
</ul></body></html>"""


class Handler(BaseHTTPRequestHandler):
    server_version = 'scout/0.1'
    protocol_version = 'HTTP/1.1'

    # ---- plumbing ----------------------------------------------------------------
    def log_message(self, fmt, *args):
        if config.ROOT and '--quiet' not in sys.argv:
            sys.stderr.write('%s %s\n' % (self.address_string(), fmt % args))

    def _json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def _error(self, status, message):
        self._json({'error': message}, status)

    def _body(self):
        n = int(self.headers.get('Content-Length') or 0)
        raw = self.rfile.read(n) if n else b''
        if not raw:
            return {}
        try:
            return json.loads(raw.decode('utf-8'))
        except json.JSONDecodeError:
            return None

    def _sse_start(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/event-stream; charset=utf-8')
        self.send_header('Cache-Control', 'no-cache')
        # no Content-Length: the stream ends when the socket closes
        self.send_header('Connection', 'close')
        self.send_header('X-Accel-Buffering', 'no')
        self.end_headers()
        self.wfile.flush()
        self.close_connection = True

    def _sse(self, event, data):
        """Write one event; returns False once the client is gone."""
        try:
            if event == 'ping':
                self.wfile.write(b': ping\n\n')
            else:
                payload = json.dumps(data, ensure_ascii=False)
                self.wfile.write(f'event: {event}\ndata: {payload}\n\n'.encode('utf-8'))
            self.wfile.flush()
            return True
        except (BrokenPipeError, ConnectionResetError, OSError):
            return False

    def _file(self, path, content_type, filename=None, delete_after=False):
        size = path.stat().st_size
        start, end = 0, size - 1
        range_header = self.headers.get('Range') if not delete_after else None
        if range_header:
            match = re.fullmatch(r'bytes=(\d+)-(\d*)', range_header)
            if not match:
                return self._error(416, 'invalid byte range')
            start = int(match.group(1))
            end = int(match.group(2)) if match.group(2) else size - 1
            if start >= size or end < start:
                self.send_response(416)
                self.send_header('Content-Range', f'bytes */{size}')
                self.send_header('Content-Length', '0')
                self.end_headers()
                return
            end = min(end, size - 1)
        self.send_response(206 if range_header else 200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(end - start + 1))
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Cache-Control', 'no-store')
        if range_header:
            self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        if filename:
            self.send_header('Content-Disposition', f"attachment; filename*=UTF-8''{quote(filename)}")
        self.end_headers()
        try:
            with path.open('rb') as source:
                source.seek(start)
                remaining = end - start + 1
                while remaining:
                    chunk = source.read(min(1024 * 1024, remaining))
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    remaining -= len(chunk)
        except (BrokenPipeError, ConnectionResetError):
            pass
        finally:
            if delete_after:
                path.unlink(missing_ok=True)

    # ---- routing -----------------------------------------------------------------
    def do_GET(self):
        url = urlsplit(self.path)
        path, q = url.path, {k: v[-1] for k, v in parse_qs(url.query).items()}
        try:
            if path == '/api/workspace/imports/stats':
                return self._json(history().stats())
            if path == '/api/workspace/imports':
                try:
                    limit, offset = int(q.get('limit', 50)), int(q.get('offset', 0))
                except ValueError:
                    return self._error(400, 'limit and offset must be integers')
                return self._json(history().search(q.get('q', ''), q.get('source', ''),
                                                   q.get('kind', ''), q.get('project', ''),
                                                   limit, offset, q.get('scope', 'all')))
            m = re.fullmatch(r'/api/workspace/imports/([a-f0-9]{32})', path)
            if m:
                row = history().get(m.group(1))
                return self._json(row) if row else self._error(404, 'imported note not found')
            if path == '/api/studio/status':
                return self._json(studio().status())
            if path == '/api/studio/recordings':
                return self._json(studio().list())
            m = re.fullmatch(r'/api/studio/recordings/([a-f0-9]{32})/(file|download)', path)
            if m:
                file_path, metadata = studio().file_path(m.group(1))
                return self._file(file_path, metadata['mime_type'],
                                  f"{metadata['title']}{metadata['extension']}" if m.group(2) == 'download' else None)
            m = re.fullmatch(r'/api/studio/recordings/([a-f0-9]{32})', path)
            if m:
                return self._json(studio().get(m.group(1)))
            if path == '/api/codex/status':
                return self._json(codex_local.status())
            if path == '/api/codex/chats':
                return self._json(workspace().list_codex_chats())
            m = re.fullmatch(r'/api/codex/chats/([a-f0-9]{32})', path)
            if m:
                row = workspace().get_codex_chat(m.group(1))
                return self._json(row) if row else self._error(404, 'chat not found')
            m = re.fullmatch(r'/api/workspace/(projects|milestones|learning_paths|pages|tasks|studies|agents)(?:/([a-f0-9]{32}))?', path)
            if m:
                if m.group(2):
                    row = workspace().get(m.group(1), m.group(2))
                    return self._json(row) if row else self._error(404, 'item not found')
                return self._json(workspace().list(m.group(1)))
            if path == '/api/health':
                return self.get_health()
            if path == '/api/hackathons':
                return self.get_hackathons(q)
            m = re.fullmatch(r'/api/hackathons/(\d+)', path)
            if m:
                return self.get_hackathon(m.group(1))
            if path == '/api/stats':
                return self._json(tools.store().stats())
            if path == '/api/winners':
                return self.get_winners(q)
            if path == '/api/chats':
                return self._json(chats().list())
            m = re.fullmatch(r'/api/chats/([A-Za-z0-9_-]+)', path)
            if m:
                c = chats().get(m.group(1))
                return self._json(ChatStore.public(c)) if c else self._error(404, 'no such chat')
            if path == '/api/jobs':
                return self._json(jobs.manager.list())
            m = re.fullmatch(r'/api/jobs/([A-Za-z0-9]+)/stream', path)
            if m:
                return self.stream_job(m.group(1))
            m = re.fullmatch(r'/api/jobs/([A-Za-z0-9]+)', path)
            if m:
                j = jobs.manager.get(m.group(1))
                return self._json(j.public(with_result=True)) if j else self._error(404, 'no such job')
            if path.startswith('/api/'):
                return self._error(404, 'unknown route')
            return self.serve_static(path)
        except WorkspaceError as exc:
            return self._error(exc.status, str(exc))
        except StudioError as exc:
            return self._error(exc.status, str(exc))
        except Exception as exc:                                     # noqa: BLE001
            traceback.print_exc()
            try:
                self._error(500, f'{type(exc).__name__}: {exc}')
            except OSError:
                pass

    def do_POST(self):
        path = urlsplit(self.path).path
        try:
            if path == '/api/studio/recordings':
                return self.post_studio_recording()
            body = self._body()
            if body is None:
                return self._error(400, 'body must be JSON')
            m = re.fullmatch(r'/api/studio/recordings/([a-f0-9]{32})/export', path)
            if m:
                output, filename = studio().export(m.group(1), body)
                return self._file(output, 'video/mp4' if filename.endswith('.mp4') else 'image/gif',
                                  filename, delete_after=True)
            if path == '/api/codex/chats':
                if not isinstance(body, dict) or body:
                    return self._error(400, 'body must be an empty JSON object')
                return self._json(workspace().create_codex_chat(), 201)
            if path == '/api/codex/complete':
                try:
                    request = codex_local.validate_writing_request(body)
                except ValueError as exc:
                    return self._error(400, str(exc))
                self._sse_start()
                alive = True
                try:
                    for event, data in codex_local.complete_writing(request):
                        if alive:
                            alive = self._sse(event, data)
                except Exception as exc:
                    traceback.print_exc()
                    if alive:
                        self._sse('error', {'message': str(exc) or type(exc).__name__})
                return
            m = re.fullmatch(r'/api/codex/chats/([a-f0-9]{32})/messages', path)
            if m:
                return self.post_codex_message(m.group(1), body)
            m = re.fullmatch(r'/api/workspace/(projects|milestones|learning_paths|pages|tasks|studies|agents)', path)
            if m:
                return self._json(workspace().create(m.group(1), body), 201)
            if path == '/api/chats':
                c = chats().create((body or {}).get('title'))
                return self._json({'id': c['id'], 'title': c['title'], 'created': c['created']}, 201)
            m = re.fullmatch(r'/api/chats/([A-Za-z0-9_-]+)/messages', path)
            if m:
                return self.post_message(m.group(1), body or {})
            if path == '/api/jobs/scout':
                name = ((body or {}).get('hackathon') or '').strip()
                if not name:
                    return self._error(400, 'hackathon is required')
                j = jobs.manager.start_scout(name)
                return self._json({'job_id': j.id, 'status': j.status}, 202)
            if path == '/api/jobs/refresh':
                running = [j for j in jobs.manager.jobs.values()
                           if j.kind == 'refresh' and j.status == 'running']
                if running:
                    return self._json({'job_id': running[0].id, 'status': 'running',
                                       'note': 'a refresh is already running'}, 200)
                j = jobs.manager.start_refresh()
                return self._json({'job_id': j.id, 'status': j.status}, 202)
            return self._error(404, 'unknown route')
        except WorkspaceError as exc:
            return self._error(exc.status, str(exc))
        except StudioError as exc:
            return self._error(exc.status, str(exc))
        except Exception as exc:                                     # noqa: BLE001
            traceback.print_exc()
            try:
                self._error(500, f'{type(exc).__name__}: {exc}')
            except OSError:
                pass

    def do_PATCH(self):
        path = urlsplit(self.path).path
        try:
            m = re.fullmatch(r'/api/workspace/imports/([a-f0-9]{32})/link', path)
            if m:
                body = self._body()
                if not isinstance(body, dict) or set(body) != {'linked_type', 'linked_id'}:
                    return self._error(400, 'linked_type and linked_id are required')
                try:
                    return self._json(history().link(m.group(1), body['linked_type'], body['linked_id']))
                except ValueError as exc:
                    return self._error(400, str(exc))
                except LookupError as exc:
                    return self._error(404, str(exc))
            m = re.fullmatch(r'/api/studio/recordings/([a-f0-9]{32})', path)
            if m:
                body = self._body()
                if not isinstance(body, dict) or not body or set(body) - {'title', 'project_id'}:
                    return self._error(400, 'provide title or project_id')
                if 'project_id' in body:
                    validate_studio_project(body['project_id'])
                return self._json(studio().update(m.group(1), body))
            m = re.fullmatch(r'/api/workspace/(projects|milestones|learning_paths|pages|tasks|studies|agents)/([a-f0-9]{32})', path)
            if not m:
                return self._error(404, 'unknown route')
            body = self._body()
            if body is None:
                return self._error(400, 'body must be JSON')
            return self._json(workspace().update(m.group(1), m.group(2), body))
        except WorkspaceError as exc:
            return self._error(exc.status, str(exc))
        except StudioError as exc:
            return self._error(exc.status, str(exc))
        except Exception as exc:                                     # noqa: BLE001
            traceback.print_exc()
            return self._error(500, f'{type(exc).__name__}: {exc}')

    def do_DELETE(self):
        path = urlsplit(self.path).path
        try:
            m = re.fullmatch(r'/api/studio/recordings/([a-f0-9]{32})', path)
            if m:
                studio().delete(m.group(1))
                return self._json({'ok': True})
            m = re.fullmatch(r'/api/codex/chats/([a-f0-9]{32})', path)
            if m:
                with _codex_active_lock:
                    if m.group(1) in _codex_active:
                        return self._error(409, 'Codex is still answering in this chat')
                    workspace().delete_codex_chat(m.group(1))
                return self._json({'ok': True})
            m = re.fullmatch(r'/api/workspace/(projects|milestones|learning_paths|pages|tasks|studies|agents)/([a-f0-9]{32})', path)
            if not m:
                return self._error(404, 'unknown route')
            workspace().delete(m.group(1), m.group(2))
            return self._json({'ok': True})
        except WorkspaceError as exc:
            return self._error(exc.status, str(exc))
        except StudioError as exc:
            return self._error(exc.status, str(exc))
        except Exception as exc:                                     # noqa: BLE001
            traceback.print_exc()
            return self._error(500, f'{type(exc).__name__}: {exc}')

    # ---- handlers ----------------------------------------------------------------
    def post_studio_recording(self):
        try:
            length = int(self.headers.get('Content-Length', '0'))
            duration_hint = float(self.headers.get('X-Recording-Duration', '0'))
        except ValueError:
            raise StudioError(400, 'Invalid upload length or duration') from None
        title = unquote(self.headers.get('X-Recording-Title', 'Recording'))
        project_id = validate_studio_project(self.headers.get('X-Project-Id') or None)
        metadata = studio().save(self.rfile, length, self.headers.get('Content-Type', ''),
                                 title, duration_hint, project_id)
        return self._json(metadata, 201)

    def post_codex_message(self, chat_id, body):
        if self.headers.get('Content-Type', '').split(';', 1)[0].strip().lower() != 'application/json':
            return self._error(415, 'Content-Type must be application/json')
        if not isinstance(body, dict) or set(body) != {'text'} or not isinstance(body['text'], str):
            return self._error(400, 'text is required')
        message = body['text'].strip()
        if not message or len(message) > 10000:
            return self._error(400, 'text must be 1–10000 characters')
        chat = workspace().get_codex_chat(chat_id)
        if chat is None:
            return self._error(404, 'chat not found')
        with _codex_active_lock:
            if chat_id in _codex_active:
                return self._error(409, 'Codex is still answering in this chat')
            _codex_active.add(chat_id)
        try:
            workspace().add_codex_message(chat_id, 'user', message)
            self._sse_start()
            alive = True
            try:
                for event, data in codex_local.stream(chat['codex_thread_id'], message, workspace()):
                    if event == 'thread':
                        workspace().set_codex_thread(chat_id, data['id'])
                    elif event == 'done':
                        workspace().add_codex_message(chat_id, 'assistant', data['text'])
                    if alive:
                        alive = self._sse(event, data)
            except Exception as exc:
                traceback.print_exc()
                error = str(exc) or type(exc).__name__
                workspace().add_codex_message(chat_id, 'error', error)
                if alive:
                    self._sse('error', {'message': error})
        finally:
            with _codex_active_lock:
                _codex_active.discard(chat_id)

    def get_health(self):
        st = tools.store()
        self._json({'ok': True, 'mode': config.mode(),
                    'model': config.MODEL if config.mode() == 'claude' else None,
                    'census_date': st.census_date, 'counts': st.counts(),
                    'today': config.today().isoformat(),
                    'web': config.WEB_DIST.joinpath('index.html').exists()})

    def get_hackathons(self, q):
        rows, total = tools.store().list(status=q.get('status', 'open'), q=q.get('q', ''),
                                         theme=q.get('theme', ''), sort=q.get('sort', 'deadline'),
                                         limit=q.get('limit', 50))
        self._json({'rows': rows, 'total': total, 'census_date': tools.store().census_date})

    def get_hackathon(self, hid):
        c = tools.store().get(hid)
        if not c:
            return self._error(404, 'no such hackathon')
        cached = tools.store().cached_brief(c['host'])
        c['brief'] = (cached or {}).get('brief')
        fld = tools.cached_field(c['host'])
        c['field'] = ({'total': fld['total'], 'source': fld['source'],
                       'winners': sum(1 for r in fld['rows'] if r.get('is_winner'))}
                      if fld else None)
        self._json(c)

    def get_winners(self, q):
        query = q.get('q', '')
        try:
            limit = int(q.get('limit', 20))
        except ValueError:
            limit = 20
        self._json(tools.store().winners(query, limit=limit) if query else [])

    def post_message(self, cid, body):
        text = (body.get('text') or '').strip()
        if not text:
            return self._error(400, 'text is required')
        chat = chats().get(cid)
        if chat is None:
            return self._error(404, 'no such chat')
        if chat.get('title') in (None, '', 'New chat') and not chat['messages']:
            chat['title'] = text[:60]
        if config.mode() == 'claude':
            from scout import agent
            gen = agent.run(chat, text)
        else:
            gen = local_agent.run(chat, text)
        self._sse_start()
        alive = True
        for event, data in gen:                 # keep consuming so the transcript persists
            if alive:
                alive = self._sse(event, data)
        from datetime import datetime
        chat['updated'] = datetime.now().isoformat(timespec='seconds')
        chats().save(chat)

    def stream_job(self, job_id):
        if jobs.manager.get(job_id) is None:
            return self._error(404, 'no such job')
        self._sse_start()
        for ev in jobs.manager.stream(job_id):
            if not self._sse(ev['event'], ev['data']):
                break

    def serve_static(self, path):
        dist = config.WEB_DIST
        index = dist / 'index.html'
        if not index.exists():
            body = FALLBACK_HTML.format(mode=config.mode()).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        rel = path.lstrip('/') or 'index.html'
        target = (dist / rel).resolve()
        if not str(target).startswith(str(dist.resolve())) or not target.is_file():
            target = index
        ctype = mimetypes.guess_type(str(target))[0] or 'application/octet-stream'
        data = target.read_bytes()
        self.send_response(200)
        self.send_header('Content-Type', ctype + ('; charset=utf-8' if ctype.startswith('text/') else ''))
        self.send_header('Content-Length', str(len(data)))
        if target != index:
            self.send_header('Cache-Control', 'public, max-age=3600')
        self.end_headers()
        self.wfile.write(data)


class Server(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def make_server(host='127.0.0.1', port=None):
    return Server((host, port if port is not None else config.PORT), Handler)


def serve(host='127.0.0.1', port=None):
    srv = make_server(host, port)
    st = tools.store()
    c = st.counts()
    print(f'workspace: Scout {config.mode()} mode · census {st.census_date} · {c["total"]:,} hackathons '
          f'({c["open"]} open) · http://{host}:{srv.server_port}', flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        srv.server_close()
