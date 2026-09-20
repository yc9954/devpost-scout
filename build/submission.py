#!/usr/bin/env python3
"""Assemble, validate, and (optionally) fill a Devpost submission — one field at
a time, against the rules the hackathon actually stated.

The write-up is the product; this is the envelope. Every field Devpost asks for
has a rule attached to it (a 200-char cap on the tagline, a public live URL, a
video under the cap, a visible licence), and every one of those rules is checked
here against the `config.json` that `discover/hackathon.py` read verbatim off the
hackathon's own page. Nothing here paraphrases a criterion or invents a rule.

Four steps, in order:

    python3 build/submission.py template               # a field file seeded with this hackathon's rules
    # …fill submission.json (body can live in docs/submission.md) …
    python3 build/submission.py validate               # every field vs every requirement
    python3 build/submission.py render                 # docs/submission-form.md, paste-ready and committable
    python3 build/submission.py fill --edit-url <url>   # types the fields into YOUR logged-in Chrome, then stops

The last step is deliberately not the last action. Devpost's create/submit button
sits behind a reCAPTCHA, and the rules require a person to complete it — so `fill`
drives a browser *you* are logged into, populates every field it can reach, and
stops. You review the visible window and press Submit. It never clicks it for you,
and it never touches a Chrome another process is driving.

`config.json` is optional but strongly recommended: without it the requirements
fall back to Devpost's usual set (public URL, public repo, English) and you lose
the video cap, the criteria, and the exact membership string.
"""
import argparse
import json
import re
import struct
import sys
import time
from pathlib import Path

# The Devpost project fields, in the order the form presents them. Each carries
# the guidance that build/WRITEUP.md and build/SHIP.md paid for.
FIELDS = [
    ('title',                'Project name.'),
    ('elevator_pitch',       'Tagline, 200 chars hard max. Lead with a capability and an '
                             'impossibility in one breath.'),
    ('details',              'The "About the project" body, Markdown. No relative links — '
                             'they break when pasted. Open on a structural claim, land one '
                             'sentence that is the whole idea, then the evidence.'),
    ('details_file',         'Optional path to a Markdown file holding the body instead of '
                             '"details" (e.g. docs/submission.md).'),
    ('built_with',           'Tags — a search surface. Include the spec/protocol/platform name.'),
    ('try_it_out',           'Links, ordered: the live URL first, the repo second. The live '
                             'URL is the single highest-value item in judging.'),
    ('testing_instructions', 'Assume no account and no special browser flag. Say exactly what '
                             'a judge without your flag sees, and make that path work.'),
    ('video_url',            'Public video URL (YouTube/Vimeo), with audio, under the cap.'),
    ('video_public',         'Attestation: have you set the video to Public? true/false.'),
    ('video_minutes',        "Your video's length in minutes, to check against the cap."),
    ('gallery',              '~15 images, 3:2, each with a caption written in the same pass.'),
    ('repo_url',             'Public repository URL.'),
    ('repo_path',            'Optional local checkout, so a visible LICENSE file can be verified.'),
    ('license',              'Open-source licence (e.g. MIT). Must be a LICENSE file visible in '
                             'the repo About section.'),
    ('submitted_to',         'The hackathon you are entering — must match its membership string.'),
]

DEFAULT_REQUIREMENTS = {
    'needs_public_url': True,
    'needs_repo': True,
    'english_required': True,
}


# --------------------------------------------------------------------------- io
def load(path):
    p = Path(path)
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding='utf-8'))


def resolve_body(sub):
    """Return the details body, sourced from details_file if given.

    Relative paths resolve against the working directory, so you can keep the
    body in docs/submission.md and run from the repo root as usual.
    """
    ref = (sub.get('details_file') or '').strip()
    if ref:
        p = Path(ref)
        if p.exists():
            return p.read_text(encoding='utf-8')
        return ''  # missing file: caller's validation reports it
    return sub.get('details') or ''


def crit_label(c):
    """Criterion label — falls back to the key for hand-written legacy configs."""
    return (c.get('label') or c.get('key') or '').strip()


# --------------------------------------------------------------------- template
def blank_submission():
    return {
        'title': '',
        'elevator_pitch': '',
        'details': '',
        'details_file': '',
        'built_with': [],
        'try_it_out': [
            {'label': 'Live demo', 'url': ''},
            {'label': 'Source code', 'url': ''},
        ],
        'testing_instructions': '',
        'video_url': '',
        'video_public': False,
        'video_minutes': None,
        'gallery': [{'path': '', 'caption': ''}],
        'repo_url': '',
        'repo_path': '',
        'license': '',
        'submitted_to': '',
    }


def guidance_from_config(cfg):
    """A read-only block echoing what the hackathon demands, so the writer sees
    the rubric while filling the form."""
    if not cfg:
        return {'note': 'no config.json — run discover/hackathon.py to capture the '
                        'criteria, requirements and membership string.'}
    reqs = cfg.get('requirements', {})
    crits = cfg.get('criteria', [])
    return {
        'hackathon': cfg.get('hackathon_title'),
        'submitted_to_must_match': cfg.get('membership_marker'),
        'requirements': reqs or DEFAULT_REQUIREMENTS,
        'video_cap_minutes': reqs.get('video_max_minutes'),
        'tiebreak_criterion': cfg.get('tiebreak_criterion'),
        'criteria': [f"{crit_label(c)} ({c.get('max')}): {c.get('text')}" for c in crits],
        'reminder': 'criteria are verbatim — address each in the body; give the tiebreak '
                    'criterion the first screen.',
    }


def cmd_template(args):
    out = Path(args.out)
    if out.exists() and not args.force:
        sys.exit(f'{out} exists — pass --force to overwrite')
    cfg = load(args.config)
    doc = {'_guidance': guidance_from_config(cfg)}
    doc.update(blank_submission())
    if cfg and cfg.get('membership_marker'):
        doc['submitted_to'] = cfg['membership_marker']
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'wrote {out}', file=sys.stderr)
    print('field guidance is in the _guidance block; fill the rest and run validate.',
          file=sys.stderr)


# ------------------------------------------------------------------- validation
class Check:
    __slots__ = ('hard', 'ok', 'label', 'detail')

    def __init__(self, hard, ok, label, detail=''):
        self.hard, self.ok, self.label, self.detail = hard, ok, label, detail


RELATIVE_LINK = re.compile(r'\]\(\s*\.{0,2}/')          # ](/ ](./ ](../
HTTP = re.compile(r'^https?://', re.I)
REPO_HOST = re.compile(r'github\.com|gitlab\.com|bitbucket\.org', re.I)


def is_repo_url(u):
    return bool(u) and bool(REPO_HOST.search(u))


def live_urls(sub):
    """try_it_out URLs that are not repositories — the live/demo links."""
    out = []
    for link in sub.get('try_it_out') or []:
        u = (link.get('url') or '').strip()
        if HTTP.match(u) and not is_repo_url(u):
            out.append(u)
    return out


def image_size(path):
    """(w, h) for PNG/JPEG/GIF, else None — pure stdlib, for the 3:2 check."""
    p = Path(path)
    if not p.exists():
        return None
    try:
        data = p.read_bytes()
    except OSError:
        return None
    if data[:8] == b'\x89PNG\r\n\x1a\n' and data[12:16] == b'IHDR':
        return struct.unpack('>II', data[16:24])
    if data[:6] in (b'GIF87a', b'GIF89a'):
        w, h = struct.unpack('<HH', data[6:10])
        return w, h
    if data[:2] == b'\xff\xd8':                          # JPEG: walk to a SOF marker
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                h, w = struct.unpack('>HH', data[i + 5:i + 9])
                return w, h
            seg = struct.unpack('>H', data[i + 2:i + 4])[0]
            i += 2 + seg
    return None


def validate(sub, cfg):
    reqs = (cfg or {}).get('requirements', {}) or DEFAULT_REQUIREMENTS
    checks = []

    title = (sub.get('title') or '').strip()
    checks.append(Check(True, bool(title), 'Project name present'))

    pitch = (sub.get('elevator_pitch') or '').strip()
    checks.append(Check(True, bool(pitch), 'Elevator pitch present'))
    if pitch:
        checks.append(Check(True, len(pitch) <= 200,
                            f'Elevator pitch ≤ 200 chars (is {len(pitch)})'))

    body = resolve_body(sub)
    checks.append(Check(True, bool(body.strip()), 'Project details body present',
                        '' if body.strip() else 'empty, or details_file missing'))
    if body.strip():
        rels = RELATIVE_LINK.findall(body)
        checks.append(Check(False, not rels,
                            'No relative links in body',
                            f'{len(rels)} relative link(s) — they break when pasted' if rels else ''))

    lives = live_urls(sub)
    if reqs.get('needs_public_url'):
        checks.append(Check(True, bool(lives),
                            'Public live URL present in Try it out',
                            'no non-repo http(s) link found' if not lives else lives[0]))

    repo = (sub.get('repo_url') or '').strip()
    if reqs.get('needs_repo'):
        checks.append(Check(True, is_repo_url(repo) or (HTTP.match(repo) and 'repo' in repo.lower()),
                            'Public repository URL present',
                            repo or 'missing'))

    cap = reqs.get('video_max_minutes')
    vurl = (sub.get('video_url') or '').strip()
    if cap is not None or reqs.get('video_must_be_public') or vurl:
        checks.append(Check(cap is not None, bool(HTTP.match(vurl)),
                            'Video URL present', vurl or 'missing'))
    if cap is not None:
        mins = sub.get('video_minutes')
        if mins is None:
            checks.append(Check(False, False, f'Confirm video ≤ {cap} min',
                                'video_minutes not filled — set it'))
        else:
            checks.append(Check(True, mins <= cap,
                                f'Video length ≤ {cap} min (is {mins})'))
    if reqs.get('video_must_be_public'):
        checks.append(Check(True, bool(sub.get('video_public')),
                            'Video set to Public (attested)'))

    marker = (cfg or {}).get('membership_marker') or (cfg or {}).get('hackathon_title')
    sub_to = (sub.get('submitted_to') or '').strip()
    if marker:
        ok = sub_to and (marker.lower() in sub_to.lower() or sub_to.lower() in marker.lower())
        checks.append(Check(True, bool(ok), 'Submitted-to matches the hackathon',
                            f'expected ~ "{marker}", got "{sub_to or "(empty)"}"'))
    else:
        checks.append(Check(False, bool(sub_to), 'Submitted-to filled',
                            'no config membership string to check against'))

    # Licence: prefer a visible file in the local checkout; fall back to attestation.
    lic = (sub.get('license') or '').strip()
    repo_path = (sub.get('repo_path') or '').strip()
    if repo_path:
        rp = Path(repo_path)
        visible = any((rp / n).exists() for n in
                      ('LICENSE', 'LICENSE.md', 'LICENSE.txt', 'COPYING', 'LICENSE.rst'))
        checks.append(Check(True, visible, 'LICENSE file visible in repo root',
                            'no LICENSE/COPYING at repo_path' if not visible else ''))
    else:
        checks.append(Check(True, bool(lic), 'Licence named',
                            'set license, and make the LICENSE file visible in the repo About'))

    # ---- advisory ----
    built = sub.get('built_with') or []
    checks.append(Check(False, bool(built), 'Built with has tags',
                        'add tags; a tag is a search surface' if not built else ''))
    spec = ((cfg or {}).get('primary_query') or '').strip()
    if built and spec:
        has = any(spec.lower() in str(t).lower() for t in built)
        checks.append(Check(False, has, f'Tags include the platform name "{spec}"',
                            '' if has else 'judges searching the spec name will not find you'))

    gallery = [g for g in (sub.get('gallery') or []) if (g.get('path') or g.get('caption'))]
    if gallery:
        capless = [g for g in gallery if not (g.get('caption') or '').strip()]
        checks.append(Check(False, not capless, 'Every gallery image has a caption',
                            f'{len(capless)} without a caption' if capless else ''))
        offaspect = []
        for g in gallery:
            wh = image_size(g.get('path', ''))
            if wh and wh[1] and abs((wh[0] / wh[1]) - 1.5) > 0.12:
                offaspect.append(g['path'])
        if offaspect:
            checks.append(Check(False, False, 'Gallery images near 3:2',
                                f'{len(offaspect)} off-ratio: {", ".join(offaspect[:3])}'))
        checks.append(Check(False, len(gallery) >= 5, 'Gallery has enough images',
                            f'only {len(gallery)}; ~15 tested best' if len(gallery) < 5 else ''))
    else:
        checks.append(Check(False, False, 'Gallery has images', 'none listed'))

    ti = (sub.get('testing_instructions') or '').strip()
    checks.append(Check(False, bool(ti), 'Testing instructions present',
                        'say what a judge with no account/flag sees' if not ti else ''))

    if reqs.get('english_required'):
        checks.append(Check(False, True, 'English required',
                            'reminder — everything must be in English'))

    # Criteria coverage: does the body visibly speak to each criterion? Advisory
    # only — this shortlists gaps, it never scores (see score/signal_score.py).
    for c in (cfg or {}).get('criteria', []):
        label = crit_label(c)
        if not label:
            continue
        words = [w for w in re.split(r'[^a-z]+', label.lower()) if len(w) > 3]
        hit = any(w in body.lower() for w in words) if words else False
        note = '' if hit else 'no obvious mention in the body'
        if label == (cfg or {}).get('tiebreak_criterion'):
            note = (note + ' — this is the tiebreaker; give it the first screen').strip(' —')
        checks.append(Check(False, hit, f'Body addresses "{label}"', note))

    return checks


def print_checks(checks):
    hard_fail = 0
    for c in checks:
        mark = '✓' if c.ok else ('✗' if c.hard else '⚠')
        tag = '' if c.ok else ('  [RULE]' if c.hard else '  [advice]')
        line = f'  {mark} {c.label}{tag}'
        if c.detail and not c.ok:
            line += f'\n      {c.detail}'
        print(line)
        if c.hard and not c.ok:
            hard_fail += 1
    print()
    if hard_fail:
        print(f'{hard_fail} rule(s) failing — fix before you submit.', file=sys.stderr)
    else:
        print('All hard rules pass. Advisories above are worth a look.', file=sys.stderr)
    return hard_fail


def cmd_validate(args):
    sub = load(args.submission)
    if sub is None:
        sys.exit(f'{args.submission} not found — run `submission.py template` first')
    cfg = load(args.config)
    if cfg is None:
        print('note: no config.json — checking against Devpost defaults only.', file=sys.stderr)
    fails = print_checks(validate(sub, cfg))
    sys.exit(1 if fails else 0)


# ----------------------------------------------------------------------- render
def md_block(value):
    if isinstance(value, list):
        if value and isinstance(value[0], dict):
            return '\n'.join(
                f"- {(x.get('label') or x.get('caption') or '').strip()}: "
                f"{(x.get('url') or x.get('path') or '').strip() or '<FILL>'}"
                for x in value)
        return '\n'.join(f'- {x}' for x in value) or '<FILL>'
    if value in (None, ''):
        return '<FILL>'
    return str(value)


def cmd_render(args):
    sub = load(args.submission)
    if sub is None:
        sys.exit(f'{args.submission} not found — run `submission.py template` first')
    cfg = load(args.config)
    checks = validate(sub, cfg)
    body = resolve_body(sub)

    lines = ['# Submission form — paste-ready', '']
    if cfg and cfg.get('hackathon_title'):
        lines += [f"For: **{cfg['hackathon_title']}**  ",
                  f"Submitted-to must read: `{cfg.get('membership_marker')}`", '']
    lines += ['> Fill this, commit it, then paste field by field. The folder holding it '
              'can vanish; only what is in git survives.', '']

    lines += ['## Checklist', '']
    for c in checks:
        mark = 'x' if c.ok else ' '
        tag = '' if c.ok else (' **[RULE]**' if c.hard else ' _(advice)_')
        lines.append(f'- [{mark}] {c.label}{tag}'
                     + (f' — {c.detail}' if c.detail and not c.ok else ''))
    lines.append('')

    lines += ['## Elevator pitch', '', f"> {sub.get('elevator_pitch') or '<FILL>'}",
              f"> _{len(sub.get('elevator_pitch') or '')} / 200 chars_", '']
    lines += ['## Project details', '', body.strip() or '<FILL — or set details_file>', '']
    lines += ['## Built with', '', md_block(sub.get('built_with')), '']
    lines += ['## Try it out (live URL first, repo second)', '', md_block(sub.get('try_it_out')), '']
    lines += ['## Testing instructions', '', sub.get('testing_instructions') or '<FILL>', '']
    lines += ['## Video', '', f"- URL: {sub.get('video_url') or '<FILL>'}",
              f"- Public: {sub.get('video_public')}",
              f"- Length (min): {sub.get('video_minutes')}", '']
    lines += ['## Gallery', '', md_block(sub.get('gallery')), '']
    lines += ['## Repository & licence', '', f"- Repo: {sub.get('repo_url') or '<FILL>'}",
              f"- Licence: {sub.get('license') or '<FILL>'} (LICENSE file visible in About)", '']

    lines += ['## Before you press Submit (human-only)', '',
              '1. Repo public; LICENSE file visible in the About section.',
              '2. Live URL deployed and re-checked from a clean network.',
              '3. Video uploaded **Public**, displayed length under the cap.',
              '4. Every command in the body run from a fresh clone.',
              '5. All fields pasted; only URLs were placeholders.',
              '6. Check the deadline in **both** the rules page and the countdown; build to the earlier.',
              '',
              'The create/submit button is behind a reCAPTCHA. A person completes it — '
              '`submission.py fill` stops before this step.']

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'wrote {out}', file=sys.stderr)
    if any(c.hard and not c.ok for c in checks):
        print('note: hard rules still failing — see the checklist at the top.', file=sys.stderr)


# ------------------------------------------------------------------------- fill
# Best-effort selectors for Devpost's project-edit form. Brittle by nature (the
# form is not ours and changes), so each field tries several and reports what it
# matched; whatever it can't reach is printed for manual paste.
FILL_SELECTORS = {
    'title': ['#software_name', 'input[name="software[name]"]',
              'input[aria-label*="name" i]', 'input[placeholder*="project name" i]'],
    'elevator_pitch': ['#software_tagline', 'input[name="software[tagline]"]',
                       'input[aria-label*="tagline" i]', 'input[placeholder*="elevator" i]',
                       'input[placeholder*="tagline" i]'],
    'details': ['#software_detail', 'textarea[name="software[detail]"]',
                'textarea.wmd-input', 'textarea[aria-label*="detail" i]'],
    'video_url': ['#software_video_url', 'input[name="software[video_url]"]',
                  'input[placeholder*="video" i]', 'input[aria-label*="video" i]'],
    'testing_instructions': ['#software_try_it_out', 'textarea[name*="try"]',
                             'textarea[aria-label*="test" i]', 'textarea[placeholder*="test" i]'],
}

SET_FIELD_JS = r'''
(function(value, selectors){
  function setNative(el, val){
    var proto = el.tagName === 'TEXTAREA'
      ? window.HTMLTextAreaElement.prototype : window.HTMLInputElement.prototype;
    var setter = Object.getOwnPropertyDescriptor(proto, 'value').set;
    setter.call(el, val);
    el.dispatchEvent(new Event('input', {bubbles:true}));
    el.dispatchEvent(new Event('change', {bubbles:true}));
  }
  for (var i=0;i<selectors.length;i++){
    var el = document.querySelector(selectors[i]);
    if (el){ setNative(el, value); return selectors[i]; }
  }
  return null;
})(%s, %s)
'''

# After filling, point the human at the last step: scroll the reCAPTCHA and the
# submit button into view and outline them, with a banner. It only draws
# attention — it never checks the box or clicks submit, because a person must.
HIGHLIGHT_SUBMIT_JS = r'''
(function(){
  function firstMatch(sels){
    for (var i=0;i<sels.length;i++){ var e=document.querySelector(sels[i]); if(e) return e; }
    return null;
  }
  var cap = firstMatch(['.g-recaptcha','#recaptcha','[data-sitekey]',
                        'iframe[src*="recaptcha"]','iframe[title*="recaptcha" i]']);
  var btn = null, re=/\b(submit|create project|save (draft|project)?|finish|publish)\b/i;
  var cands = Array.prototype.slice.call(
    document.querySelectorAll('button, input[type=submit], a.button, [role=button]'));
  for (var i=0;i<cands.length;i++){
    var t=(cands[i].innerText||cands[i].value||cands[i].getAttribute('aria-label')||'').trim();
    if (re.test(t)){ btn=cands[i]; break; }
  }
  if (!btn) btn=document.querySelector('button[type=submit], input[type=submit]');
  var anchor = cap || btn;
  if (!anchor) return 'none';
  anchor.scrollIntoView({behavior:'smooth', block:'center'});
  [cap, btn].forEach(function(el){
    if(!el) return;
    el.style.outline='3px solid #e6007a';
    el.style.outlineOffset='3px';
    el.style.boxShadow='0 0 0 6px rgba(230,0,122,0.25)';
  });
  var id='devpost-scout-banner', old=document.getElementById(id); if(old) old.remove();
  var b=document.createElement('div'); b.id=id;
  b.textContent='✅ 필드 입력 완료 — '
    + '아래 reCAPTCHA 체크 후 Submit만 누르세요 '
    + '(사람이 직접)';
  b.setAttribute('style','position:fixed;top:0;left:0;right:0;z-index:2147483647;'
    +'background:#e6007a;color:#fff;font:600 15px system-ui,sans-serif;'
    +'padding:12px 16px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.3)');
  document.body.appendChild(b);
  return (cap?'recaptcha':'') + (cap&&btn?'+':'') + (btn?'submit-button':'') || 'anchored';
})()
'''


def cmd_fill(args):
    sub = load(args.submission)
    if sub is None:
        sys.exit(f'{args.submission} not found — run `submission.py template` first')
    if not args.edit_url:
        sys.exit('pass --edit-url of your DRAFT project\'s edit page. Create the project '
                 'first (title + hackathon) — that step\'s reCAPTCHA needs you — then re-run '
                 'here to fill the rest.')

    try:
        from lib.browser import Browser
    except Exception as exc:                              # pragma: no cover
        sys.exit(f'need websocket-client for fill mode: pip install -r requirements.txt ({exc})')

    values = {
        'title': (sub.get('title') or '').strip(),
        'elevator_pitch': (sub.get('elevator_pitch') or '').strip(),
        'details': resolve_body(sub).strip(),
        'video_url': (sub.get('video_url') or '').strip(),
        'testing_instructions': (sub.get('testing_instructions') or '').strip(),
    }

    if args.attach:
        print(f'attaching to your Chrome on port {args.attach} '
              '(launched with --remote-debugging-port)…', file=sys.stderr)
        b = Browser(port=args.attach, launch=False, block=False)
    else:
        profile = str(Path(args.profile).expanduser())
        print(f'launching a visible Chrome (profile {profile}). '
              'Log in to Devpost in that window if prompted.', file=sys.stderr)
        b = Browser(port=args.port, profile=profile, launch=True, block=False, headless=False)

    try:
        b.call('Page.navigate', {'url': args.edit_url})
        # Wait for you to be logged in and the form to render.
        deadline = time.time() + args.login_timeout
        ready = False
        while time.time() < deadline:
            try:
                found = b.js('!!document.querySelector(%s)'
                             % json.dumps(', '.join(FILL_SELECTORS['title'])))
            except Exception:
                found = False
            if found:
                ready = True
                break
            time.sleep(2)
        if not ready:
            print('could not see the edit form (not logged in, or wrong URL). '
                  'Nothing was changed.', file=sys.stderr)
            b.detach()
            sys.exit(2)

        filled, missed = [], []
        for field, sels in FILL_SELECTORS.items():
            val = values.get(field, '')
            if not val:
                continue
            expr = SET_FIELD_JS % (json.dumps(val), json.dumps(sels))
            try:
                matched = b.js(expr)
            except Exception as exc:
                matched = None
                missed.append((field, f'error: {exc}'))
                continue
            (filled if matched else missed).append((field, matched or 'no selector matched'))

        print('\nfilled:', file=sys.stderr)
        for f, sel in filled:
            print(f'  ✓ {f}  ({sel})', file=sys.stderr)
        if missed:
            print('could not fill (paste these from docs/submission-form.md):', file=sys.stderr)
            for f, why in missed:
                print(f'  ✗ {f}  ({why})', file=sys.stderr)
        # Built-with tags, gallery, and the Try-it-out links are tag/repeater
        # widgets whose markup shifts; these are always left for you to paste.
        print('\nnot attempted (widget fields — paste by hand): built_with, try_it_out links, gallery.',
              file=sys.stderr)

        # Point you at the final human step — scroll + outline it, never click it.
        try:
            anchored = b.js(HIGHLIGHT_SUBMIT_JS)
        except Exception:
            anchored = 'none'
        if anchored and anchored != 'none':
            print(f'\nmarked the last step in the window ({anchored}). A banner + pink '
                  'outline shows where.', file=sys.stderr)
        else:
            print('\ncould not locate the reCAPTCHA/submit area — scroll to it yourself.',
                  file=sys.stderr)

        print('\nDONE. The window is left open. Review every field, then check the '
              'reCAPTCHA and press Submit yourself — a person must, by the rules.',
              file=sys.stderr)
    finally:
        b.detach()          # keep the browser open for you to submit


# ------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--config', default='config.json',
                    help='hackathon config from discover/hackathon.py (default config.json)')
    ap.add_argument('--submission', default='submission.json',
                    help='the field file (default submission.json)')
    sub = ap.add_subparsers(dest='cmd', required=True)

    t = sub.add_parser('template', help='write a field file seeded with this hackathon\'s rules')
    t.add_argument('--out', default='submission.json')
    t.add_argument('--force', action='store_true')
    t.set_defaults(func=cmd_template)

    v = sub.add_parser('validate', help='check every field against every requirement')
    v.set_defaults(func=cmd_validate)

    r = sub.add_parser('render', help='write docs/submission-form.md, paste-ready and committable')
    r.add_argument('--out', default='docs/submission-form.md')
    r.set_defaults(func=cmd_render)

    f = sub.add_parser('fill', help='type fields into YOUR logged-in Chrome, then stop')
    f.add_argument('--edit-url', help='the edit page of your already-created draft project')
    f.add_argument('--attach', type=int, default=None,
                   help='CDP port of a Chrome you launched with --remote-debugging-port')
    f.add_argument('--port', type=int, default=9444, help='port for the visible Chrome we launch')
    f.add_argument('--profile', default='~/.devpost-scout-chrome-profile',
                   help='persistent profile dir so your Devpost login survives runs')
    f.add_argument('--login-timeout', type=int, default=240,
                   help='seconds to wait for you to log in and the form to appear')
    f.set_defaults(func=cmd_fill)

    a = ap.parse_args()
    a.func(a)


if __name__ == '__main__':
    main()
