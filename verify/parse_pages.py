#!/usr/bin/env python3
"""Turn the saved Devpost submission pages into structured records."""
import html as html_lib
import json
import re
from pathlib import Path

TAG = re.compile(r'<[^>]+>')
SPACE = re.compile(r'\s+')
SECTION = re.compile(r'<h2[^>]*>(.*?)</h2>(.*?)(?=<h2[^>]*>|\Z)', re.S | re.I)


def text(fragment):
    fragment = re.sub(r'(?is)<(script|style).*?</\1>', ' ', fragment)
    fragment = re.sub(r'(?i)</(p|li|div|h\d|br)>', ' \n', fragment)
    return SPACE.sub(' ', html_lib.unescape(TAG.sub(' ', fragment))).strip()


def block(page, start_marker, end_marker):
    i = page.find(start_marker)
    if i < 0:
        return ''
    j = page.find(end_marker, i)
    return page[i:j if j > 0 else i + 60000]


def parse(path):
    page = path.read_text(encoding='utf-8', errors='replace')
    title = text(re.search(r'<h1 id="app-title">(.*?)</h1>', page, re.S).group(1)) if 'id="app-title"' in page else path.stem
    head = page.split('id="app-title"', 1)[-1][:4000]
    tag = re.search(r'<p class="large">(.*?)</p>', head, re.S)
    tagline = text(tag.group(1)) if tag else ''

    details = block(page, 'id="app-details-left"', 'id="app-details-right"')
    body = details.split('id="built-with"')[0]
    sections = {text(h).lower(): text(b) for h, b in SECTION.findall(body)}
    description = text(body)

    built = [text(t).lower() for t in re.findall(r'<span class="cp-tag[^"]*">(.*?)</span>', block(page, 'id="built-with"', '</div>'))]

    links = re.findall(r'href="(https?://[^"]+)"', block(page, 'class="app-links', '</nav>'))
    repo = [u for u in links if re.search(r'(github|gitlab|bitbucket)\.com/[^/]+/[^/?#]+', u)]
    video_links = [u for u in links if re.search(r'youtu\.?be|youtube\.com|vimeo|loom', u)]
    live = [u for u in links if u not in repo and u not in video_links]

    embed = re.findall(r'youtube\.com/embed/([A-Za-z0-9_-]{6,})', page)
    members = re.findall(r'<a class="user-profile-link" href="https://devpost\.com/([^"]+)">([^<]+)</a>', block(page, 'id="app-team"', '</section>'))
    seen, team = set(), []
    for handle, name in members:
        if handle not in seen:
            seen.add(handle)
            team.append({'handle': handle, 'name': html_lib.unescape(name).strip()})

    started = re.search(r'started this project\s*&mdash;|started this project\s*—\s*([A-Za-z]{3} \d{1,2}, \d{4})', page)
    date = re.search(r'started this project[^<]*?([A-Z][a-z]{2} \d{1,2}, \d{4})', text(page))

    return {
        'slug': path.stem,
        'url': f'https://devpost.com/software/{path.stem}',
        'title': title,
        'tagline': tagline,
        'description': description,
        'sections': sections,
        'description_words': len(description.split()),
        'built_with': built,
        'links': links,
        'repo_urls': repo,
        'live_urls': live,
        'video_urls': video_links,
        'youtube_embed_ids': sorted(set(embed)),
        'team': team,
        'team_size': len(team),
        'started_on': date.group(1) if date else (started.group(1) if started and started.lastindex else None),
    }


def main():
    rows = [parse(p) for p in sorted(Path('data/pages').glob('*.html'))]
    Path('data/submissions_parsed.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({
        'parsed': len(rows),
        'with_repo': sum(bool(r['repo_urls']) for r in rows),
        'with_live': sum(bool(r['live_urls']) for r in rows),
        'with_video': sum(bool(r['youtube_embed_ids'] or r['video_urls']) for r in rows),
        'median_words': sorted(r['description_words'] for r in rows)[len(rows) // 2],
        'teams_gt1': sum(r['team_size'] > 1 for r in rows),
    }, indent=2))


if __name__ == '__main__':
    main()
