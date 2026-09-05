#!/usr/bin/env python3
"""Collect every WebMCP participant through the challenge page's own AJAX route.

Requires the already-open, authenticated Chrome debugging session on port 18800.
This never changes a participant's account state; it only reads the public list.
"""
import argparse
import json
import sys
import time

import websocket


def evaluate(ws, expression, request_id):
    ws.send(json.dumps({
        "id": request_id,
        "method": "Runtime.evaluate",
        "params": {"expression": expression, "awaitPromise": True, "returnByValue": True},
    }))
    while True:
        reply = json.loads(ws.recv())
        if reply.get("id") != request_id:
            continue
        result = reply.get("result", {}).get("result", {})
        if "value" not in result:
            raise RuntimeError(result.get("description", "CDP evaluation failed"))
        return result["value"]


JS = r'''(async (page) => new Promise((resolve, reject) => {
  jQuery.ajax({
    url: '/participants?page=' + page,
    headers: {'X-Requested-With': 'XMLHttpRequest'},
    timeout: 30000
  }).done((html, _status, jq) => {
    const doc = new DOMParser().parseFromString(html, 'text/html');
    const people = [...doc.querySelectorAll('[data-registrations=registrant]')].map(card => {
      const link = card.querySelector('h5 a.user-profile-link');
      const stat = label => {
        const item = [...card.querySelectorAll('.counts li')].find(x => x.textContent.includes(label));
        return Number((item?.querySelector('.participant-stat')?.textContent || '0').match(/\d+/)?.[0] || 0);
      };
      return {
        participant_id: card.dataset.participantId,
        name: link?.textContent.trim() || null,
        profile_url: link?.href || null,
        projects: stat('projects'),
        followers: stat('followers'),
        achievements: stat('achievement'),
        team_status: card.querySelector('.cp-tag')?.textContent.trim() || null,
        specialties: [...card.querySelectorAll('.specialty, .skills a')].map(x => x.textContent.trim()).filter(Boolean)
      };
    }).filter(x => x.name && x.profile_url);
    const summary = doc.querySelector('[data-role=pagination] .items_info')?.textContent.replace(/\s+/g, ' ').trim();
    resolve({page, count: people.length, summary, people});
  }).fail((jq, status, error) => reject({page, status: jq.status, statusText: status, error: String(error)}));
}))(%d)'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    ap.add_argument('--pages', type=int, default=285)
    ap.add_argument('--start-page', type=int, default=1,
                    help='first pagination page to request (default: 1)')
    ap.add_argument('--pause', type=float, default=0.7,
                    help='seconds between requests (default: 0.7)')
    ap.add_argument('--skip-errors', action='store_true',
                    help='record a page failure and continue collecting later pages')
    ap.add_argument('--ws-url', default='ws://127.0.0.1:18800/devtools/page/5250A603D92CC99318E0B7FD0D7DAE9A')
    args = ap.parse_args()

    records = []
    # Persisted checkpoints make a rate-limit interruption recoverable.
    try:
        with open(args.output, encoding='utf-8') as f:
            records = json.load(f).get('participants', [])
    except FileNotFoundError:
        pass
    seen_pages = set()
    ws = None
    try:
        for page in range(args.start_page, args.pages + 1):
            if page in seen_pages:
                continue
            for attempt in range(1, 4):
                try:
                    if ws is None:
                        ws = websocket.create_connection(args.ws_url, suppress_origin=True, timeout=45)
                    value = evaluate(ws, JS % page, page)
                    if not isinstance(value, dict) or not value.get('people'):
                        raise RuntimeError(f'unexpected response: {value!r}')
                    records.extend(value['people'])
                    by_url = {row['profile_url']: row for row in records}
                    payload = {
                        'source': 'https://webmcp.devpost.com/participants (authenticated AJAX pagination)',
                        'collected_at_epoch': time.time(),
                        'pages_requested': args.pages,
                        'records_before_dedupe': len(records),
                        'participants': list(by_url.values()),
                    }
                    with open(args.output, 'w', encoding='utf-8') as f:
                        json.dump(payload, f, ensure_ascii=False, indent=2)
                    print(f"page {page}/{args.pages}: {value['count']} ({value.get('summary')})", flush=True)
                    break
                except Exception as exc:
                    print(f"page {page}: attempt {attempt}/3 failed: {exc}", file=sys.stderr, flush=True)
                    if ws is not None:
                        try: ws.close()
                        except Exception: pass
                    ws = None
                    if attempt == 3:
                        if args.skip_errors:
                            print(f"page {page}: skipped after repeated failures", file=sys.stderr, flush=True)
                            break
                        raise
                    time.sleep(5 * attempt)
            time.sleep(args.pause)
    finally:
        if ws is not None:
            ws.close()

    # The same person can appear only once, but retain the invariant defensively.
    by_url = {row['profile_url']: row for row in records}
    payload = {
        'source': 'https://webmcp.devpost.com/participants (authenticated AJAX pagination)',
        'collected_at_epoch': time.time(),
        'pages_requested': args.pages,
        'records_before_dedupe': len(records),
        'participants': list(by_url.values()),
    }
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"saved {len(payload['participants'])} unique profiles to {args.output}")


if __name__ == '__main__':
    main()
