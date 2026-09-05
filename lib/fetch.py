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
CHALLENGE = ('awswaf', 'challenge-container', 'Just a moment', 'captcha-container')


class Challenged(Exception):
    """The WAF answered instead of the site. Never treat this as content."""


def looks_challenged(html: str) -> bool:
    if len(html) < 2000:
        return True
    low = html[:6000].lower()
    return any(m.lower() in low for m in CHALLENGE)


def get(url, tries=5, timeout=35, base_sleep=1.5):
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                html = r.read().decode('utf-8', 'replace')
                status, final = r.status, r.url
            if status == 200 and not looks_challenged(html):
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
