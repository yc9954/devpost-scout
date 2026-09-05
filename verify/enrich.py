#!/usr/bin/env python3
"""Add live-site and repository evidence to each parsed submission.

Everything recorded here is verifiable: HTTP status of the judge-facing URL,
the repository's license/date metadata from the GitHub API, and literal
`registerTool` / `modelContext` hits in the repository's own source files.
"""
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen

UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                    '(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}
CODE = ('.js', '.ts', '.tsx', '.jsx', '.mjs', '.html', '.svelte', '.vue', '.astro')
INTEREST = re.compile(r'(mcp|tool|agent|register|index|main|app)', re.I)
REGISTER = re.compile(r'registerTool\s*\(')
NAME = re.compile(r'name\s*:\s*[\'"]([A-Za-z0-9_.\-]+)[\'"]')


def gh(path):
    try:
        out = subprocess.run(['gh', 'api', path], capture_output=True, text=True, timeout=45)
        return json.loads(out.stdout) if out.returncode == 0 else None
    except Exception:                                    # noqa: BLE001
        return None


def get(url, timeout=25, limit=400_000):
    try:
        with urlopen(Request(url, headers=UA), timeout=timeout) as r:
            return r.status, r.read(limit).decode('utf-8', 'replace')
    except Exception as exc:                             # noqa: BLE001
        return None, str(exc)


def check_live(urls):
    out = []
    for u in urls[:3]:
        status, body = get(u, timeout=20, limit=300_000)
        out.append({'url': u, 'status': status,
                    'mentions_modelcontext': bool(status and re.search(r'modelContext|registerTool', body)),
                    'bytes': len(body) if status else 0,
                    'error': None if status else body[:160]})
    return out


def check_repo(url):
    m = re.search(r'github\.com/([^/]+)/([^/?#]+)', url)
    if not m:
        return {'repo_url': url, 'host': 'non-github', 'checked': False}
    owner, name = m.group(1), m.group(2).replace('.git', '')
    meta = gh(f'repos/{owner}/{name}')
    if not meta:
        return {'repo_url': url, 'host': 'github', 'checked': False, 'error': 'metadata unavailable'}
    branch = meta.get('default_branch', 'main')
    tree = gh(f'repos/{owner}/{name}/git/trees/{branch}?recursive=1') or {}
    blobs = [t for t in tree.get('tree', []) if t.get('type') == 'blob']
    code = [t for t in blobs if t['path'].endswith(CODE) and 'node_modules' not in t['path']]
    picks = sorted([t for t in code if INTEREST.search(t['path'])],
                   key=lambda t: (-('mcp' in t['path'].lower() or 'tool' in t['path'].lower()), t.get('size', 0)))[:10]
    hits, names = 0, []
    for t in picks:
        status, body = get(f'https://raw.githubusercontent.com/{owner}/{name}/{branch}/{t["path"]}')
        if not status:
            continue
        found = list(REGISTER.finditer(body))
        hits += len(found)
        for f in found:
            near = NAME.search(body[max(0, f.end() - 200): f.end() + 400])
            if near:
                names.append(near.group(1))
    return {
        'repo_url': url, 'host': 'github', 'checked': True,
        'full_name': meta.get('full_name'),
        'license': (meta.get('license') or {}).get('spdx_id'),
        'created_at': meta.get('created_at'), 'pushed_at': meta.get('pushed_at'),
        'stars': meta.get('stargazers_count'), 'size_kb': meta.get('size'),
        'files': len(blobs), 'code_files': len(code),
        'register_tool_hits': hits,
        'tool_names': sorted(set(names))[:40],
        'files_scanned': [t['path'] for t in picks],
    }


def enrich(row):
    live = check_live(row['live_urls'])
    repos = [check_repo(u) for u in row['repo_urls'][:2]]
    return {**row, 'live_checks': live, 'repo_checks': repos}


def main():
    rows = json.loads(Path('data/submissions_parsed.json').read_text())
    out = Path('data/submissions_enriched.json')
    done = {r['slug']: r for r in json.loads(out.read_text())} if out.exists() else {}
    todo = [r for r in rows if r['slug'] not in done]
    print(f'enriching {len(todo)} of {len(rows)}', flush=True)
    with ThreadPoolExecutor(max_workers=6) as pool:
        for i, row in enumerate(pool.map(enrich, todo), 1):
            done[row['slug']] = row
            if i % 10 == 0 or i == len(todo):
                out.write_text(json.dumps(list(done.values()), ensure_ascii=False, indent=2), encoding='utf-8')
                print(f'{i}/{len(todo)}', flush=True, file=sys.stderr)
    out.write_text(json.dumps(list(done.values()), ensure_ascii=False, indent=2), encoding='utf-8')
    print('enriched', len(done))


if __name__ == '__main__':
    main()
