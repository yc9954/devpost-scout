#!/usr/bin/env python3
"""Turn a hackathon's fine print into one do-this checklist — then walk you
through the do-able steps in the browser you're logged into.

Registering, joining the Discord, claiming the sponsor credits (AWS, GCP,
MongoDB…), the submission requirements, the deadlines: a hackathon scatters these
across its front page, its /rules, and a resources tab, and missing one can
disqualify an entry that would have placed. This reads all of it, pulls it into a
brief, and sorts every item into three buckets:

  * read       — rules, eligibility, requirements you must know
  * you (login)— register, join Discord, claim credits: opened for you, but you
                 complete the login / OAuth / redeem, because those are your
                 identity and a bot must not stand in for it
  * automatable— pure navigation and reading, done here

    python3 discover/participation.py brief --host webmcp.devpost.com
    python3 discover/participation.py brief --config config.json
    python3 discover/participation.py walk        # opens each action in YOUR Chrome, one at a time

`walk` opens a visible Chrome you log in to once, navigates to each action in
order, scrolls to and banners the button, and waits for you to press Enter before
the next. It never clicks register/join/redeem, never touches a CAPTCHA or an
OAuth screen — it points, you press.
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.fetch import Challenged, get                       # noqa: E402
from discover.hackathon import flat                         # noqa: E402

A_TAG = re.compile(r'(?is)<a\b[^>]*?href\s*=\s*(["\'])(.*?)\1[^>]*>(.*?)</a>')

COMMUNITY = [
    ('discord',  re.compile(r'discord\.(?:gg|com)/', re.I)),
    ('slack',    re.compile(r'(?:join\.)?slack\.com/|\.slack\.com', re.I)),
    ('telegram', re.compile(r't\.me/|telegram\.me/', re.I)),
    ('whatsapp', re.compile(r'chat\.whatsapp\.com/', re.I)),
]
CREDIT_HINT = re.compile(
    r'credit|promo\s*code|voucher|redeem|activate|free\s+tier|\$\s?\d|perk|coupon', re.I)
RESOURCE_HINT = re.compile(
    r'resource|starter|getting\s+started|quickstart|\bdocs?\b|\bapi\b|template|tutorial|sample', re.I)
REGISTER_HINT = re.compile(r'\b(register|participate|enter the|sign\s*up|join the)\b', re.I)

# Deadline phrasing on Devpost pages and /rules prose. The gap before the date
# is LAZY: greedy, it swallowed the run-on "close: Oct 31 … deadline is Nov 3"
# as one deadline. Lazy, it stops at the first date after the trigger word, and
# the optional tail picks up a trailing "at 5:00pm PST".
DEADLINE = re.compile(
    r'(?i)((?:submission[s]?\s+(?:period|deadline|due)|deadline|due\s+date|closes?|ends?)'
    r'[^.<\n]{0,40}?'
    r'\b(?:[A-Z][a-z]{2,8}\.?\s+\d{1,2}(?:st|nd|rd|th)?,?\s+20\d\d'
    r'|\d{1,2}\s+[A-Z][a-z]{2,8},?\s+20\d\d|20\d\d-\d{2}-\d{2}|\d{1,2}/\d{1,2}/20\d\d)'
    r'(?:\s+(?:at\s+)?\d{1,2}:\d{2}\s?[ap]m(?:\s+[A-Z]{2,4})?)?)')


def links(html):
    out, seen = [], set()
    for _, href, inner in A_TAG.findall(html):
        url = href.strip()
        if not url or url.startswith(('#', 'javascript:', 'mailto:')):
            continue
        if url.startswith('//'):
            url = 'https:' + url
        text = flat(inner)
        key = (url, text)
        if key in seen:
            continue
        seen.add(key)
        out.append({'text': text, 'url': url})
    return out


def section(html, pattern, cap=1400):
    """Flat text under the first heading matching `pattern`, to the next heading."""
    head = re.search(r'(?is)<h[1-6][^>]*>\s*(?:[^<]*?)(' + pattern + r')(?:[^<]*?)\s*</h[1-6]>',
                     html)
    if not head:
        return ''
    tail = html[head.end():]
    nxt = re.search(r'(?is)<h[1-6][^>]*>', tail)
    body = tail[:nxt.start()] if nxt else tail[:cap * 4]
    return flat(body)[:cap].strip()


def classify_links(all_links, host):
    community, credits, resources = [], [], []
    for lk in all_links:
        u, t = lk['url'], lk['text']
        blob = f'{u} {t}'
        matched = False
        for kind, rx in COMMUNITY:
            if rx.search(u):
                community.append({**lk, 'kind': kind})
                matched = True
                break
        if matched:
            continue
        # skip on-site and Devpost-chrome links for the credit/resource buckets
        offsite = host not in u and 'devpost.com' not in u
        if CREDIT_HINT.search(blob) and (offsite or 'redeem' in u.lower()):
            credits.append(lk)
        elif RESOURCE_HINT.search(t) and offsite:
            resources.append(lk)
    return community, dedupe(credits), dedupe(resources)


def dedupe(items):
    out, seen = [], set()
    for x in items:
        if x['url'] in seen:
            continue
        seen.add(x['url'])
        out.append(x)
    return out


def build_brief(pages, host, title):
    """pages: {'main': html, 'rules': html, 'resources': html}. Pure — testable."""
    main = pages.get('main', '') or ''
    rules = pages.get('rules', '') or ''
    resources_html = pages.get('resources', '') or ''

    all_links = links(main) + links(resources_html) + links(rules)
    community, credits, resources = classify_links(all_links, host)

    text = ' '.join(flat(x) for x in (main, rules))
    deadlines, seen_dl = [], set()          # dedupe on the phrase, not the shared host URL
    for d in DEADLINE.findall(text):
        phrase = re.sub(r'\s+', ' ', d).strip()
        key = phrase.lower()
        if key in seen_dl:
            continue
        seen_dl.add(key)
        deadlines.append({'text': phrase, 'url': f'https://{host}/'})
    deadlines = deadlines[:6]

    sections = {
        'how_to_enter':  section(main, r'how\s+to\s+(?:enter|participate|submit)|getting\s+started')
                         or section(rules, r'how\s+to\s+(?:enter|participate|submit)'),
        'requirements':  section(main, r'requirements?|what\s+to\s+(?:build|submit)|submission')
                         or section(rules, r'(?:submission\s+)?requirements?|what\s+to\s+submit'),
        'eligibility':   section(rules, r'eligib|who\s+can\s+(?:enter|participate)'),
        'resources':     section(resources_html or main, r'resources?'),
    }

    # Ordered walkthrough. `who` decides what walk does vs hands off.
    actions = [{
        'step': 1, 'label': 'Register for the hackathon',
        'url': f'https://{host}/', 'who': 'you (login) — press the Register button',
    }]
    for c in community:
        actions.append({
            'step': len(actions) + 1,
            'label': f"Join the {c['kind']}: {c['text'] or c['kind']}",
            'url': c['url'], 'who': 'you (OAuth) — join with your own account',
        })
    for c in credits[:8]:
        actions.append({
            'step': len(actions) + 1,
            'label': f"Claim credits / perk: {c['text'] or c['url']}",
            'url': c['url'], 'who': 'you (login/redeem) — claim with your account or code',
        })
    actions.append({
        'step': len(actions) + 1, 'label': 'Read the rules in full',
        'url': f'https://{host}/rules', 'who': 'read',
    })
    for r in resources[:8]:
        actions.append({
            'step': len(actions) + 1,
            'label': f"Resource: {r['text'] or r['url']}",
            'url': r['url'], 'who': 'read',
        })

    return {
        'host': host, 'title': title,
        'register_url': f'https://{host}/',
        'rules_url': f'https://{host}/rules',
        'deadlines': deadlines,
        'community': community,
        'credits': credits,
        'resources': resources,
        'sections': sections,
        'actions': actions,
    }


# ------------------------------------------------------------------------ fetch
def fetch_pages(host):
    pages = {}
    for name, path in (('main', ''), ('rules', '/rules'), ('resources', '/resources')):
        try:
            pages[name] = get(f'https://{host}{path}')['html']
        except Challenged as exc:
            print(f'warning: {host}{path} unreadable ({exc})', file=sys.stderr)
            pages[name] = ''
    return pages


def title_of(main_html, host):
    m = re.search(r'<title[^>]*>(.*?)</title>', main_html, re.S | re.I)
    return flat(m.group(1)).split(':')[0].split('|')[0].strip() if m else host


# ------------------------------------------------------------------------ brief
def cmd_brief(args):
    host = args.host
    if not host and args.config:
        cfg = json.loads(Path(args.config).read_text(encoding='utf-8'))
        host = cfg.get('hackathon_host')
    if not host:
        sys.exit('need --host or a --config with hackathon_host')

    pages = fetch_pages(host)
    if not any(pages.values()):
        sys.exit(f'could not read {host} — check the host or your network')
    title = title_of(pages['main'], host)
    brief = build_brief(pages, host, title)

    Path(args.json).write_text(json.dumps(brief, ensure_ascii=False, indent=2), encoding='utf-8')
    md = render_brief(brief)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding='utf-8')
    print(f'wrote {args.json} and {out}', file=sys.stderr)
    print(f"{len(brief['actions'])} actions · {len(brief['community'])} community · "
          f"{len(brief['credits'])} credit link(s) · {len(brief['deadlines'])} deadline phrase(s)",
          file=sys.stderr)


def render_brief(b):
    L = [f"# Participation brief — {b['title']}", '',
         f"Host: `{b['host']}`  ·  Register: {b['register_url']}  ·  Rules: {b['rules_url']}", '']

    L += ['## Deadlines (verify against the page countdown — they can disagree)', '']
    L += [f"- {d['text']}" for d in b['deadlines']] or ['- _none parsed — read the page header_']
    L.append('')

    L += ['## Do this, in order', '']
    for a in b['actions']:
        L.append(f"{a['step']}. **{a['label']}** — {a['url']}  \n   _{a['who']}_")
    L += ['', '> `discover/participation.py walk` opens each of these in your own Chrome and '
          'marks the button. Login, OAuth and any redeem/CAPTCHA are yours to complete.', '']

    if b['community']:
        L += ['## Community', '']
        L += [f"- {c['kind']}: {c['text'] or c['url']} — {c['url']}" for c in b['community']]
        L.append('')
    if b['credits']:
        L += ['## Sponsor credits / perks', '']
        L += [f"- {c['text'] or c['url']} — {c['url']}" for c in b['credits']]
        L.append('')
    if b['resources']:
        L += ['## Resources', '']
        L += [f"- {r['text'] or r['url']} — {r['url']}" for r in b['resources']]
        L.append('')

    for key, heading in (('requirements', 'Submission requirements'),
                         ('eligibility', 'Eligibility'),
                         ('how_to_enter', 'How to enter'),
                         ('resources', 'Resources (from the page)')):
        txt = (b['sections'] or {}).get(key)
        if txt:
            L += [f'## {heading}', '', txt, '']

    L += ['## What is human-only (never automated here)', '',
          '- Discord/Slack join and any OAuth — your account.',
          '- Claiming sponsor credits behind a login or a one-time code — your account.',
          '- Any CAPTCHA or terms acceptance — a person, by the rules.']
    return '\n'.join(L) + '\n'


# ------------------------------------------------------------------------- walk
BANNER_JS = r'''
(function(text){
  var id='devpost-scout-step', old=document.getElementById(id); if(old) old.remove();
  var b=document.createElement('div'); b.id=id; b.textContent=text;
  b.setAttribute('style','position:fixed;top:0;left:0;right:0;z-index:2147483647;'
    +'background:#111;color:#fff;font:600 15px system-ui,sans-serif;'
    +'padding:12px 16px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.4)');
  if (document.body) document.body.appendChild(b);
  return true;
})(%s)
'''


def cmd_walk(args):
    brief = json.loads(Path(args.json).read_text(encoding='utf-8')) if Path(args.json).exists() else None
    if not brief:
        sys.exit(f'{args.json} not found — run `participation.py brief` first')
    actions = brief.get('actions', [])
    if not actions:
        sys.exit('no actions in the brief')

    try:
        from lib.browser import Browser
    except Exception as exc:
        sys.exit(f'need websocket-client for walk mode: pip install -r requirements.txt ({exc})')

    if args.attach:
        print(f'attaching to your Chrome on port {args.attach}…', file=sys.stderr)
        b = Browser(port=args.attach, launch=False, block=False)
    else:
        profile = str(Path(args.profile).expanduser())
        print(f'launching a visible Chrome (profile {profile}). Log in where prompted.',
              file=sys.stderr)
        b = Browser(port=args.port, profile=profile, launch=True, block=False, headless=False)

    n = len(actions)
    try:
        for a in actions:
            label = f"STEP {a['step']}/{n} · {a['label']}  ·  [{a['who']}]"
            print('\n' + label, file=sys.stderr)
            print(f"  → {a['url']}", file=sys.stderr)
            try:
                b.call('Page.navigate', {'url': a['url']})
                time.sleep(2.0)
                b.js(BANNER_JS % json.dumps(
                    f"STEP {a['step']}/{n} — {a['label']}  |  {a['who']}"))
            except Exception as exc:
                print(f"  (couldn't open: {exc})", file=sys.stderr)
            if a is not actions[-1]:
                if args.auto_advance:
                    time.sleep(args.auto_advance)
                else:
                    try:
                        input('  press Enter for the next step (Ctrl-C to stop and stay here)…')
                    except (EOFError, KeyboardInterrupt):
                        print('\nstopped — window left open on this step.', file=sys.stderr)
                        break
        print('\nDONE walking the actions. The window stays open. '
              'Complete any login / join / redeem yourself.', file=sys.stderr)
    finally:
        b.detach()          # leave the browser open for you


# -------------------------------------------------------------------------- cli
def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest='cmd', required=True)

    br = sub.add_parser('brief', help='read the hackathon and write a participation checklist')
    br.add_argument('--host', help='e.g. webmcp.devpost.com')
    br.add_argument('--config', default='config.json', help='config.json for the host (fallback)')
    br.add_argument('--json', default='participation.json')
    br.add_argument('--out', default='docs/participation.md')
    br.set_defaults(func=cmd_brief)

    wk = sub.add_parser('walk', help='open each action in YOUR Chrome, one at a time')
    wk.add_argument('--json', default='participation.json')
    wk.add_argument('--attach', type=int, default=None,
                    help='CDP port of a Chrome you launched with --remote-debugging-port')
    wk.add_argument('--port', type=int, default=9445, help='port for the visible Chrome we launch')
    wk.add_argument('--profile', default='~/.devpost-scout-chrome-profile',
                    help='persistent profile so logins survive runs')
    wk.add_argument('--auto-advance', type=int, default=0,
                    help='seconds between steps instead of waiting for Enter (0 = wait)')
    wk.set_defaults(func=cmd_walk)

    a = ap.parse_args()
    a.func(a)


if __name__ == '__main__':
    main()
