#!/usr/bin/env python3
"""Verify which public Devpost projects explicitly say they were submitted to WebMCP."""
import argparse
import concurrent.futures
import html as html_lib
import json
import re
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

TITLE = re.compile(r'<title[^>]*>\s*(.*?)\s*</title>', re.I | re.S)
TAG = re.compile(r'<[^>]+>')
SPACE = re.compile(r'\s+')

def clean(value):
    return SPACE.sub(' ', html_lib.unescape(TAG.sub(' ', value))).strip()

def fetch(url):
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; research; +https://devpost.com)'})
        with urlopen(request, timeout=35) as response:
            raw = response.read().decode('utf-8', 'replace')
            status, final = response.status, response.url
        text = clean(raw)
        challenge = bool(re.search(r'Submitted to\s+The WebMCP Challenge', text, re.I))
        title = clean(TITLE.search(raw).group(1)) if TITLE.search(raw) else url.rsplit('/', 1)[-1]
        # Preserve only small, auditable surrounding excerpts for later scoring.
        excerpts = []
        for match in re.finditer(r'.{0,500}Submitted to\s+The WebMCP Challenge.{0,500}', text, re.I):
            excerpts.append(match.group(0))
        return {'url': url, 'final_url': final, 'status': status, 'title': title,
                'submitted_to_webmcp': challenge, 'evidence': excerpts[:2], 'error': None}
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        return {'url': url, 'final_url': None, 'status': None, 'title': None,
                'submitted_to_webmcp': False, 'evidence': [], 'error': str(exc)}

def save(path, source, rows):
    path.write_text(json.dumps({'source_portfolios': source, 'collected_at_epoch': time.time(),
                                'projects': list(rows.values())}, ensure_ascii=False, indent=2), encoding='utf-8')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--portfolios', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--workers', type=int, default=5)
    ap.add_argument('--retry-failed', action='store_true')
    args = ap.parse_args()
    urls = json.loads(Path(args.portfolios).read_text(encoding='utf-8'))['unique_project_urls']
    out = Path(args.output)
    rows = {}
    if out.exists(): rows = {r['url']: r for r in json.loads(out.read_text(encoding='utf-8')).get('projects', [])}
    todo = [u for u in urls if u not in rows or (args.retry_failed and rows[u].get('error'))]
    print(f'project URLs: {len(urls)}; cached: {len(rows)}; remaining: {len(todo)}', flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i, row in enumerate(pool.map(fetch, todo), 1):
            rows[row['url']] = row
            if i % 20 == 0 or i == len(todo):
                save(out, args.portfolios, rows)
                actual = sum(x['submitted_to_webmcp'] for x in rows.values())
                print(f'completed {i}/{len(todo)}; verified WebMCP submissions: {actual}', flush=True)

if __name__ == '__main__':
    main()
