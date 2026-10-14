"""Fetch titles and short descriptions for public links in saved one-line notes.

Only known public content domains are fetched. Private docs, account pages, internal
Slack files, tracking links, and URLs with access tokens stay in the local archive.
"""

import html
import json
import re
import sqlite3
import ssl
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

from scout import config


PUBLIC_HOSTS = {
    'www.youtube.com', 'youtube.com', 'youtu.be', 'github.com',
    'zdnet.co.kr', 'www.koreadeep.com', 'discuss.pytorch.kr',
    'www.worldlabs.ai', 'nvdli.github.io', 'developer.nvidia.com',
    'alisawuffles.github.io', 'alisawuffles.notion.site',
    'www.inflearn.com', '21st.dev', 'www.asiae.co.kr', 'v.daum.net',
    'labhub.hopto.org', 'm.blog.naver.com', 'www.instagram.com',
    'instagram.com', 'www.youtube.com', 'www.sec.gov',
    'stitch.withgoogle.com', 'sqlitebrowser.org',
    'allthingsagentichackathon.devpost.com', 'nebiusglobalaihackathon.devpost.com',
    'dorahacks.io', 'hack2skill.com', 'aibuildercup.com',
}
KEEP_QUERY = {'v', 'list', 'logNo', 'blogId', 'no'}
SSL_CONTEXT = ssl.create_default_context(cafile='/etc/ssl/cert.pem')


def public_url(url):
    parts = urllib.parse.urlsplit(url)
    if parts.hostname not in PUBLIC_HOSTS:
        return ''
    query = urllib.parse.urlencode([(key, value) for key, value in
                                    urllib.parse.parse_qsl(parts.query) if key in KEEP_QUERY])
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, parts.path, query, ''))


def metadata(url):
    parts = urllib.parse.urlsplit(url)
    endpoint = url
    if parts.hostname in ('www.youtube.com', 'youtube.com', 'youtu.be'):
        endpoint = 'https://www.youtube.com/oembed?' + urllib.parse.urlencode(
            {'url': url, 'format': 'json'})
    try:
        request = urllib.request.Request(endpoint, headers={'User-Agent': 'Mozilla/5.0 (compatible; personal-study-archive/1.0)'})
        with urllib.request.urlopen(request, timeout=8, context=SSL_CONTEXT) as response:
            data = response.read(250000).decode('utf-8', errors='replace')
        if endpoint != url:
            payload = json.loads(data)
            return {'url': url, 'title': payload.get('title', ''), 'description': '',
                    'site': payload.get('author_name', ''), 'verified': bool(payload.get('title'))}
        title_match = re.search(r'<title[^>]*>(.*?)</title>', data, re.I | re.S)
        og_match = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\'](.*?)["\']', data, re.I | re.S)
        desc_match = re.search(r'<meta[^>]+(?:name=["\']description["\']|property=["\']og:description["\'])[^>]+content=["\'](.*?)["\']', data, re.I | re.S)
        title = html.unescape((og_match or title_match).group(1)).strip() if (og_match or title_match) else ''
        description = html.unescape(desc_match.group(1)).strip() if desc_match else ''
        return {'url': url, 'title': re.sub(r'\s+', ' ', title)[:250],
                'description': re.sub(r'\s+', ' ', description)[:500],
                'site': parts.hostname, 'verified': bool(title)}
    except Exception:
        return {'url': url, 'title': '', 'description': '', 'site': parts.hostname,
                'verified': False}


def main():
    db = sqlite3.connect(config.DATA / 'workspace.db')
    urls = set()
    for (value,) in db.execute("SELECT urls_json FROM imported_notes WHERE kind = 'link'"):
        for raw in json.loads(value):
            if url := public_url(raw):
                urls.add(url)
    output = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(metadata, url): url for url in urls}
        for future in as_completed(futures):
            output.append(future.result())
    output.sort(key=lambda item: item['url'])
    path = config.DATA / 'import_2026-03/link_metadata.json'
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({'candidates': len(urls), 'verified': sum(item['verified'] for item in output),
                      'file': str(path)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
