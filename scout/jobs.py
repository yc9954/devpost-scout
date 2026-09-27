"""Thread-based background jobs with an event log that can be replayed and followed.

Two kinds: `scout` (brief → field → ideate) and `refresh` (re-run the census through
hub/collect_hackathons.py in a subprocess, then reload the store)."""
import re
import shutil
import subprocess
import sys
import threading
import time
import uuid
from datetime import datetime

from scout import config


class Job:
    def __init__(self, kind, label):
        self.id = uuid.uuid4().hex[:10]
        self.kind = kind
        self.label = label
        self.status = 'running'
        self.created = datetime.now().isoformat(timespec='seconds')
        self.finished = None
        self.events = []
        self.result = None
        self.error = None
        self.cond = threading.Condition()

    def emit(self, event, data):
        with self.cond:
            self.events.append({'event': event, 'data': data})
            self.cond.notify_all()

    def progress(self, step, pct, note, job_id=None):
        self.emit('job_progress', {'job_id': self.id, 'step': step, 'pct': int(pct),
                                   'note': str(note)[:600]})

    def finish(self, result=None, error=None):
        with self.cond:
            self.status = 'failed' if error else 'done'
            self.result, self.error = result, error
            self.finished = datetime.now().isoformat(timespec='seconds')
        self.emit('job_done', {'job_id': self.id, 'status': self.status,
                               'result': result, 'error': error})

    def public(self, with_result=False):
        d = {'id': self.id, 'kind': self.kind, 'label': self.label, 'status': self.status,
             'created': self.created, 'finished': self.finished, 'error': self.error,
             'events': len(self.events)}
        last = next((e['data'] for e in reversed(self.events) if e['event'] == 'job_progress'), None)
        d['progress'] = last
        if with_result:
            d['result'] = self.result
        return d


class Manager:
    def __init__(self):
        self.jobs = {}
        self.lock = threading.Lock()

    def start(self, kind, label, fn):
        job = Job(kind, label)
        with self.lock:
            self.jobs[job.id] = job

        def body():
            try:
                res = fn(job)
                job.finish(result=res)
            except Exception as exc:                                 # noqa: BLE001
                job.finish(error=f'{type(exc).__name__}: {exc}')

        threading.Thread(target=body, name=f'job-{kind}-{job.id}', daemon=True).start()
        return job

    def get(self, job_id):
        return self.jobs.get(job_id)

    def list(self):
        return sorted((j.public() for j in self.jobs.values()),
                      key=lambda j: j['created'], reverse=True)

    def stream(self, job_id, keepalive=15.0):
        """Yield every event so far, then live ones, until job_done. Yields
        {'event': 'ping'} on idle so SSE writers can keep the socket warm."""
        job = self.jobs.get(job_id)
        if job is None:
            yield {'event': 'error', 'data': {'message': f'no job {job_id}'}}
            return
        i = 0
        while True:
            with job.cond:
                while i >= len(job.events) and job.status == 'running':
                    if not job.cond.wait(timeout=keepalive):
                        break
                batch = job.events[i:]
            if not batch:
                if job.status != 'running' and i >= len(job.events):
                    return
                yield {'event': 'ping', 'data': None}
                continue
            for ev in batch:
                i += 1
                yield ev
                if ev['event'] == 'job_done':
                    return

    # ---- the two job kinds -----------------------------------------------------------
    def start_scout(self, hackathon):
        from scout import tools

        def run(job):
            return tools.scout_pipeline(hackathon, emit=job.progress)
        return self.start('scout', hackathon, run)

    def start_refresh(self):
        def run(job):
            return refresh_census(job)
        return self.start('refresh', 'census refresh', run)


_PAGE = re.compile(r'page\s+(\d+)\s+collected\s+(\d+)\s*/\s*(\S+)')


def refresh_census(job):
    """Run hub/collect_hackathons.py into a fresh file; swap it in only on success."""
    from scout import tools
    out = config.HACKATHONS.with_name('hackathons.refresh.jsonl')
    if out.exists():
        out.unlink()                       # the collector resumes; a refresh must not
    script = config.ROOT / 'hub' / 'collect_hackathons.py'
    job.progress('census', 1, f'Starting {script.name} → {out.name}')
    proc = subprocess.Popen([sys.executable, str(script), '--out', str(out)],
                            cwd=str(config.ROOT), stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, text=True, bufsize=1)
    tail = []
    for line in proc.stdout:
        line = line.rstrip()
        if not line:
            continue
        tail.append(line)
        tail = tail[-30:]
        m = _PAGE.search(line)
        if m:
            page, got, total = int(m[1]), int(m[2]), m[3]
            try:
                pct = min(98, int(got / max(1, int(total)) * 100))
            except ValueError:
                pct = min(98, page // 16)
            job.progress('census', pct, f'page {page}: {got} / {total} hackathons')
        elif 'API reports' in line or 'within 2%' in line or '⚠' in line:
            job.progress('census', 98, line)
    rc = proc.wait()
    if rc != 0 or not out.exists():
        raise RuntimeError(f'collector exited {rc}: ' + ' | '.join(tail[-4:]))
    backup = config.HACKATHONS.with_name('hackathons.prev.jsonl')
    if config.HACKATHONS.exists():
        shutil.copy2(config.HACKATHONS, backup)
    shutil.move(str(out), str(config.HACKATHONS))
    tools.store().reload()
    counts = tools.store().counts()
    job.progress('reload', 100, f'Census reloaded: {counts["total"]:,} hackathons '
                                f'({counts["open"]} open)')
    return {'ok': True, 'summary': f'census refreshed: {counts["total"]:,} hackathons',
            'data': {'counts': counts, 'census_date': tools.store().census_date,
                     'finished': time.strftime('%Y-%m-%dT%H:%M:%S')}}


manager = Manager()
