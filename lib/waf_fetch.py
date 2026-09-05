#!/usr/bin/env python3
"""Drive the evaluator's own collectors behind a throttled, WAF-aware urlopen.

Nothing about how a page is parsed or how membership is decided changes: this
only replaces the transport so Devpost's AWS WAF stops handing back 202
challenge pages (which the collectors would otherwise score as 'not a
submission') and 403 rate-limit pages.
"""
import io, sys, threading, time, random
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen as _urlopen

HERE = Path(__file__).parent
COOKIE = (HERE / 'cookies.txt').read_text().strip()
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36')
EXTRA = {'Cookie': COOKIE, 'User-Agent': UA,
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Language': 'en-US,en;q=0.9',
         'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'none',
         'Sec-Fetch-Dest': 'document', 'Upgrade-Insecure-Requests': '1'}

GATE = threading.Semaphore(1)      # serialises the moment of send, not the wait
PAUSE = float(sys.argv[2]) if len(sys.argv) > 2 else 0.10
COOLDOWN = threading.Event(); COOLDOWN.set()


def urlopen(req, *a, **kw):
    for key, val in EXTRA.items():
        req.add_header(key, val)
    last = None
    for attempt in range(6):
        COOLDOWN.wait()
        with GATE:
            time.sleep(PAUSE + random.uniform(0, PAUSE))
        try:
            resp = _urlopen(req, *a, **kw)
        except HTTPError as exc:
            if exc.code in (403, 429, 503):
                last = exc
                exc.read(); exc.close()
                if COOLDOWN.is_set():          # one thread parks the whole pool
                    COOLDOWN.clear()
                    time.sleep(20 + 20 * attempt)
                    COOLDOWN.set()
                continue
            raise
        if resp.status == 200:
            return resp
        resp.read(); resp.close()               # 202 = WAF challenge interstitial
        last = HTTPError(req.full_url, resp.status, 'WAF challenge', resp.headers, None)
        time.sleep(3 * (attempt + 1))
    raise last


def main():
    which = sys.argv[1]
    sys.argv = [which] + sys.argv[3:]
    sys.path.insert(0, '/Users/ax/webmcp-evaluator')
    mod = __import__(which)
    mod.urlopen = urlopen                       # collectors bound the name at import
    mod.main()


if __name__ == '__main__':
    main()
