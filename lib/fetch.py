#!/usr/bin/env python3
"""Plain-HTTP fetch that survives Devpost's WAF.

Project pages and public profiles answer urllib fine — until they don't. Under
concurrency Devpost's AWS WAF starts returning a 202 challenge page with a
200-shaped body. That is the dangerous failure: a challenge page parses as a
profile with zero projects, or a project that is not a submission. It does not
raise, it under-counts, and it under-counts silently.

So: detect the challenge, back off, retry, and treat exhaustion as an error the
caller must handle — never as data.
"""
import random
import time
import urllib.error
import urllib.request

UA = 'Mozilla/5.0 (compatible; devpost-scout research)'

# Markers that mean the WAF answered instead of the site.
#
# `awswaf` alone was here and rejected EVERY legitimate Devpost page: the site
# ships `window.AwsWafCookieDomainList` in its normal <head>, about 1.2KB in, so
# a healthy 136KB project page tripped the check and `membership_check.py` could
# not fetch anything at all. `/challenge.js` is out for the same reason. What is
# left appears only on an actual interstitial — verified absent from a live
# project page, a hackathon page and the search API response.
CHALLENGE = ('token.awswaf.com', 'challenge-container', 'Just a moment', 'captcha-container')


class Challenged(Exception):
    """The WAF answered instead of the site. Never treat this as content."""


def looks_challenged(html: str, min_len: int = 2000) -> bool:
    """Short or challenge-shaped bodies are errors, never data.

    `min_len` exists because the length heuristic is calibrated for HTML pages
    and false-positives on small legitimate payloads — Devpost's keyless
    `/api/hackathons` search answers in ~1KB of perfectly good JSON. Callers
    that know they are fetching an API pass a smaller floor; `get()` also drops
    the floor automatically when the response declares a JSON content type.
    """
    if len(html) < min_len:
        return True
    low = html[:6000].lower()
    return any(m.lower() in low for m in CHALLENGE)


def get(url, tries=5, timeout=35, base_sleep=1.5, min_len=2000):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                html = r.read().decode('utf-8', 'replace')
                status, final = r.status, r.url
                ctype = (r.headers.get('Content-Type') or '').lower()
            floor = 2 if 'json' in ctype else min_len
            if status == 200 and not looks_challenged(html, floor):
                return {'status': status, 'final_url': final, 'html': html}
            last = Challenged(f'{url} -> {status}, challenge-shaped')
        except urllib.error.HTTPError as e:
            if e.code in (403, 429, 202):
                last = Challenged(f'{url} -> {e.code}')
            elif e.code in (404, 410):
                return {'status': e.code, 'final_url': url, 'html': ''}
            else:
                last = e
        except Exception as e:                      # noqa: BLE001
            last = e
        time.sleep(base_sleep * (2 ** attempt) + random.random())
    raise last if isinstance(last, Exception) else Challenged(url)
