#!/usr/bin/env python3
"""A Chrome you drive over CDP, because Devpost will not talk to a plain client.

devpost.com answers urllib/curl on its *search* and *listing* routes with a 202
challenge page or a 403. Project pages and public profiles are usually fine over
plain HTTP; search never is. So discovery goes through a real browser and
verification goes through the fast path.

Launch your own instance rather than attaching to the user's: a headless profile
of your own cannot collide with their tabs, and killing it is safe.

    from lib.browser import Browser
    with Browser(port=9333) as b:
        html = b.get('https://devpost.com/software/search?query=foo')

Blocking subresources takes a page load from ~40 requests to ~3, which is what
makes exhaustive paging feasible. That is done for you.
"""
import json
import subprocess
import time
import urllib.request

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
BLOCKED = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.svg', '*.css', '*.woff*',
           '*google-analytics*', '*doubleclick*', '*segment.io*', '*sentry*']


class Browser:
    def __init__(self, port=9333, profile=None, launch=True, block=True, headless=True):
        self.port, self.block, self.proc = port, block, None
        self.profile = profile or f'/tmp/devpost-scout-chrome-{port}'
        if launch and not self._alive():
            # headless=False leaves a visible window: the only way to drive a
            # Chrome the *user* is logged into (submission), where we must never
            # attach to a Chrome someone else already drives — that hangs recv.
            flags = [CHROME, f'--remote-debugging-port={port}',
                     f'--user-data-dir={self.profile}', '--no-first-run',
                     '--no-default-browser-check', '--disable-extensions',
                     '--window-size=1400,2000']
            if headless:
                flags.insert(1, '--headless=new')
            flags.append('about:blank')
            self.proc = subprocess.Popen(
                flags, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            for _ in range(30):
                if self._alive():
                    break
                time.sleep(0.5)
        self._connect()

    def _alive(self):
        try:
            urllib.request.urlopen(f'http://127.0.0.1:{self.port}/json/version', timeout=2)
            return True
        except Exception:
            return False

    def _connect(self):
        import websocket  # pip install websocket-client
        tabs = json.loads(urllib.request.urlopen(
            f'http://127.0.0.1:{self.port}/json/list', timeout=10).read())
        pages = [t for t in tabs if t['type'] == 'page']
        if not pages:
            # /json/new needs PUT on recent Chrome; GET returns 405.
            req = urllib.request.Request(
                f'http://127.0.0.1:{self.port}/json/new?about:blank', method='PUT')
            pages = [json.loads(urllib.request.urlopen(req, timeout=10).read())]
        self.ws = websocket.create_connection(
            pages[0]['webSocketDebuggerUrl'], timeout=90, suppress_origin=True)
        self._id = 0
        self.call('Page.enable', {})
        if self.block:
            self.call('Network.enable', {})
            self.call('Network.setBlockedURLs', {'urls': BLOCKED})

    def call(self, method, params):
        self._id += 1
        self.ws.send(json.dumps({'id': self._id, 'method': method, 'params': params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get('id') == self._id:
                return msg

    def get(self, url, settle=2.5, tries=8, min_len=3000):
        """Navigate and return outerHTML once the document is complete."""
        self.call('Page.navigate', {'url': url})
        time.sleep(settle)
        body = ''
        for _ in range(tries):
            v = self.call('Runtime.evaluate', {
                'expression': 'document.readyState+"|"+document.documentElement.outerHTML',
                'returnByValue': True})['result']['result'].get('value', '')
            state, _, body = v.partition('|')
            if state == 'complete' and len(body) > min_len:
                return body
            time.sleep(1.2)
        return body

    def js(self, expr, by_value=True, await_promise=True):
        """Evaluate JS in the page and hand back the value it returns."""
        r = self.call('Runtime.evaluate', {
            'expression': expr, 'returnByValue': by_value,
            'awaitPromise': await_promise})
        res = r.get('result', {}).get('result', {})
        return res.get('value') if by_value else res

    def close(self):
        try:
            self.ws.close()
        except Exception:
            pass
        if self.proc:
            self.proc.terminate()

    def detach(self):
        """Drop the CDP connection but leave the browser running.

        Used after filling a submission: the visible window stays open so the
        human can review and press the final Submit behind the reCAPTCHA.
        """
        self.proc = None
        self.close()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.close()
