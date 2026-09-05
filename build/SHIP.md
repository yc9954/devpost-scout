# Shipping it: deploy, hosts, and the last 48 hours

## The live URL is the single highest-value item

Every evaluation in our run put the entry in the top tier on merit and then
noted that without a working URL it fails the rules outright. Two entries it
otherwise lost to were themselves sunk by a missing one. Deploy early, then
keep deploying — a URL that 404s during judging is the same as no URL.

## Static deploys, and the one thing that breaks

Client-side routes (`/`, `/studio`) need unknown paths rewritten to
`index.html`, or a judge who opens your deep link gets a 404:

```json
{ "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }] }
```

Keep a `.vercelignore` so the bundle does not carry your 25MB demo video, the
benchmark transcripts, or the film stills.

## Vercel friction we actually hit

- **The production alias does not always follow the newest deployment.**
  `vercel deploy --prod` succeeded, `warrant-gray.vercel.app` kept serving the
  old bundle hash for minutes. Verify by fetching the deployed JS and grepping
  for a string only the new build contains — do not trust the CLI's success line.
- **`vercel promote` on the current production deployment returns 409**
  ("already the current production deployment") even while the alias serves
  something older. That is a caching lag, not an error to fix.
- **Deployment protection makes the raw `*-<hash>.vercel.app` URL 302 to a login
  page** for anyone but you. Use `vercel curl <url>` to fetch it as yourself, and
  make sure the *alias* is what you hand a judge.
- **`.vercel/` is gitignored**, so a fresh clone has no project link:
  `vercel link --yes --project <name>` before deploying.

## Two implementations of the same spec will disagree

Our one-click demo hung in ChatGPT's in-app browser with
`executeTool requires an object input`, while working in the Chrome build it was
developed against — which had wanted the arguments as a **JSON string** and
answered the object form with `UnknownError: Failed to parse input arguments`.

Neither shape is safe to assume from inside a page. The fix is to try the spec
shape first, fall back on refusal, and remember which one the host accepted:

```js
const order = hostShape === 'string' ? ['string','object'] : ['object','string'];
for (const shape of order) {
  try {
    const raw = await host.executeTool(tool, shape === 'object' ? args : JSON.stringify(args));
    hostShape = shape;                       // remember for next call
    return typeof raw === 'string' ? JSON.parse(raw) : raw;
  } catch (e) { refusal = e; }
}
throw refusal;
```

**Test in every host a judge might use, not just your development one.** The
failure was in the button the landing page tells judges to press first.

## Make the flagless path work

If your project needs an experimental browser flag, most judges will not enable
it. Ship a fallback that runs the identical tool implementations in-page and
says plainly which mode it is in. A judge scored our Execution 23 partly because
"the live URL works with no flag, no account and no backend" — and docked it
because in that mode the page is proposing to itself.

## The last 48 hours, in order

1. Repo public, licence file at the root **visible in the About section** — the
   rules say detectable and visible, and an empty About is the first thing a
   judge lands on.
2. Live URL deployed and re-verified from a clean network.
3. Video uploaded **Public**, displayed length checked against the cap.
4. Every command in the write-up run from a fresh clone with no dev server.
5. Submission form filled; only the URLs left as placeholders. **Commit that
   file** — the folder holding ours was deleted and only what was in git
   survived.
6. Then stop. After submission the repository is frozen: a post-deadline commit
   is reachable by SHA forever and the force-push that removes it is in the
   public activity feed. Deploy to the live host if you must fix something.

Check the deadline in both places. The rules page and the countdown timer
disagreed by twelve hours in ours. Build to the earlier one.
