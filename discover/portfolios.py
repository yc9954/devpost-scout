#!/usr/bin/env python3
"""Read public Devpost portfolios and emit their project URLs.

Only profiles listed by the WebMCP participant page are requested.  Results are
checkpointed after every completed request so a transient Devpost error does not
discard completed work.
"""
import argparse
import concurrent.futures
import json
import re
import threading
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

PROJECT = re.compile(r'https?://devpost\.com/software/([A-Za-z0-9][A-Za-z0-9_-]*)')
IGNORE = {'built-with', 'new'}
LOCK = threading.Lock()


def fetch(person):
    request = Request(person['profile_url'], headers={'User-Agent': 'Mozilla/5.0 (compatible; research; +https://devpost.com)'})
    try:
        with urlopen(request, timeout=30) as response:
            html = response.read().decode('utf-8', 'replace')
            final = response.url
            status = response.status
        urls = sorted({f'https://devpost.com/software/{slug}' for slug in PROJECT.findall(html) if slug not in IGNORE})
        return {'profile_url': person['profile_url'], 'name': person['name'], 'status': status,
                'final_url': final, 'project_urls': urls, 'error': None}
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        return {'profile_url': person['profile_url'], 'name': person['name'], 'status': None,
                'final_url': None, 'project_urls': [], 'error': str(exc)}


def save(path, source, rows):
    projects = sorted({url for row in rows.values() for url in row['project_urls']})
    payload = {'source_participants': source, 'collected_at_epoch': time.time(),
               'profiles': list(rows.values()), 'unique_project_urls': projects}
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--participants', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--workers', type=int, default=6)
    args = ap.parse_args()
    people = json.loads(Path(args.participants).read_text(encoding='utf-8'))['participants']
    people = [p for p in people if p.get('projects', 0) > 0]
    out = Path(args.output)
    done = {}
    if out.exists():
        done = {r['profile_url']: r for r in json.loads(out.read_text(encoding='utf-8')).get('profiles', [])}
    todo = [p for p in people if p['profile_url'] not in done]
    print(f'portfolio profiles: {len(people)}; already cached: {len(done)}; remaining: {len(todo)}', flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i, row in enumerate(pool.map(fetch, todo), 1):
            with LOCK:
                done[row['profile_url']] = row
                save(out, args.participants, done)
            if i % 20 == 0 or i == len(todo):
                print(f'completed {i}/{len(todo)}; unique project URLs: {len({u for r in done.values() for u in r["project_urls"]})}', flush=True)


if __name__ == '__main__':
    main()
