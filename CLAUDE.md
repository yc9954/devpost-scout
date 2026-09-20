# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Not an application. A repository of standalone Python scripts, `{{placeholder}}` agent prompts, and
playbooks for entering a Devpost hackathon on measured evidence. There is no build, no test suite, no
lint config, and no dependency manifest — every script is run directly with `python3`.

Setup: `pip install -r requirements.txt` (websocket-client; eight scripts import it). External binaries:
Google Chrome (CDP), `ffmpeg` and `vhs` for film, `gh` for `verify/enrich.py`. `lib/browser.py` hard-codes
the macOS Chrome path.

A `/scout` skill in `.claude/skills/scout/` orchestrates the whole pipeline conversationally and is the
intended entry point; it routes to the documents below rather than restating them.

Analysis documents added on top of the original playbooks: `write/WINNING-WRITEUPS.md` (nine submission
bodies at the top of two fields, read in full — what the tagline, headings, impact anchors and limitations
sections actually do), `write/IMPACT.md` (the four anchors and the research procedure) and
`build/TERMINAL.md` (VHS-based terminal demos, and cutting them against browser footage).

`README.md` is the map, `METHOD.md` the pipeline in order, **`PITFALLS.md` the authority** — every rule
below is priced there. `position/IDEA-SELECTION.md` is the gate before any code gets written.

## The idea hub (`hub/`)

A census of every hackathon Devpost lists plus the winners inside the ones worth reading, in one SQLite
file. See `hub/README.md`. The reason it exists as a separate path from `discover/`: `/api/hackathons` is
plain-HTTP JSON with **no pagination ceiling** and states its own `meta.total_count`, so a true census
costs ~1,540 requests — where `/software/search` needs a browser, fights a WAF, and capped the first
corpus at a third of the field. Project galleries are also plain HTTP, 24 a page, and carry a **`winner`
ribbon**, which makes a cross-hackathon corpus of winners cheap and much higher-signal than a corpus of
everything.

```sh
python3 hub/collect_hackathons.py --out data/hackathons.jsonl
python3 hub/collect_gallery.py --from-index data/hackathons.jsonl --winners-only \
        --min-prize 25000 --limit 200 --out data/projects.jsonl
python3 hub/store.py build --hackathons data/hackathons.jsonl --projects data/projects.jsonl
python3 hub/store.py search "agent browser tool" --winners
```

`hub/enrich_projects.py` → `extract.py` → `vault.py` → `gaps.py` turns those rows into an Obsidian vault:
one note per project/facet/hackathon wired with `[[wikilinks]]`, plus gap notes for facet combinations whose
halves are both proven and whose intersection is empty. `enrich_projects.py` also fills the long-standing
`data/pages/*.html` hole that `verify/parse_pages.py` reads.

**`hub/taxonomy.json` is regex over prose and it will lie to you.** Its first version reported 54% of the
corpus as housing/homelessness — it was matching `rent` in *current*, `labor` in *collaborated*, `frame` in
*framework*, `signed` in *designed*, `aging` in *packaging*, `dom` in *random*, `url` in *curl*. Bare stems
under ~6 characters need `\b` on both sides; stems that are common English substrings must be deleted, not
bounded. Print matched context before trusting any count (`hub/README.md` has the audit snippet).

`hub/store.py search` is FTS over title+tagline: it **shortlists, never ranks**, for the same reason
`score/signal_score.py` carries that warning. Taglines are ~100 chars, so an idea distinguished in its
body will not surface — for a hackathon you are actually entering, build the full corpus through
`discover/` + `verify/` instead. `projects_fts` is external-content FTS5: rebuild with
`INSERT INTO projects_fts(projects_fts) VALUES('rebuild')`, never `DELETE` (it corrupts the index).

## Setup for a new run

```sh
python3 discover/hackathon.py --name "<hackathon name>" --out config.json
```

`discover/hackathon.py` is the entry point: it resolves a name through Devpost's keyless
`/api/hackathons?search=` endpoint, then parses the hackathon's own page for the judging criteria
(verbatim), their weights, the requirements that fail an entry outright (video cap, public URL, repo,
language) and the prize table. Verified against four unrelated hackathons, including one with unequal
weights (30/20/20/15/10/5%), which it recovers automatically.

It also records **`tiebreak_criterion`** — the first-listed criterion. Devpost's standard tie-break
resolves ties on it, so at the top of a bunched field it decides placements and deserves
disproportionate effort. Hand-editing `config.example.json` still works when the parse fails
(`criteria_source` is null).

`config.json`, `data/`, `judge/` and `runs/*/corpus/` are gitignored. Find `membership_marker` by opening
one known entry and reading the block Devpost renders as *"Submitted to …"*.

## Two tiers of scripts — check the source before running any command

METHOD.md documents an idealised, config-driven CLI. **Verified: 8 of its 11 documented commands do not
run** — only `verify/membership_check.py`, `score/make_chunks.py` and `score/aggregate.py` accept the
flags METHOD.md gives them. The rest are artifacts of the WebMCP run kept verbatim: positional
`sys.argv`, hard-coded paths, WebMCP-specific regexes. A command copied from METHOD.md into one of those
crashes on an unrecognised flag or a missing file.

**Config-driven, `argparse`, portable as-is:**

| | |
| --- | --- |
| `discover/participants.py` | `--output --pages --ws-url` — the default `--ws-url` is a dead devtools page id from the original run; always pass your own |
| `discover/portfolios.py` | `--participants --output --workers` |
| `verify/membership_check.py` | `--config --in --out --workers` |
| `score/make_chunks.py` | `--config --in --out-dir --double-judge N` |
| `score/aggregate.py` | `--results --dist --me` |
| `build/film/*.py` | all take `argparse` |

**Run artifacts — read the source first:**

| | |
| --- | --- |
| `discover/search_sweep.py`, `search_sweep_exhaustive.py` | positional `WS QUERY PAGES OUT [DELAY] [MAXPAGE]`; `WS` is a CDP websocket URL |
| `verify/membership_fast.py` | positional and sharded: `WS SLUGFILE OUT DUMPDIR SHARD NSHARD [DELAY]` |
| `verify/parse_pages.py` | no arguments; `data/pages/*.html` → `data/submissions_parsed.json` |
| `verify/enrich.py` | no arguments; `data/submissions_parsed.json` → `data/submissions_enriched.json`, checkpointed and resumable |
| `verify/membership.py` | `argparse`, but the marker text is hard-coded in the regex |
| `position/field_position.py`, `position/authorship_check.py` | no arguments; read `data/submissions_enriched.json`; `field_position.py` also reads `../docs/submission.md` as "our entry" |
| `score/signal_score.py` | `sys.argv[1]` is a JSONL; writes `./ranked.json` |
| `score/signal_score_alt.py` | absolute `/private/tmp/...` path from the original run |
| `lib/waf_fetch.py`, `lib/cdp_fetch.py` | a `sys.path` pointing at another machine's checkout, and `lib/cookies.txt`, which is not tracked |

When porting, patch a run artifact to take `--config` rather than writing a replacement — the regexes and
the WAF handling inside them are the expensive part.

**The config does less than `README.md` claims.** Of nine functional keys in `config.example.json`, four
are read by two scripts: `hackathon_host` and `membership_marker` (`verify/membership_check.py`),
`chunk_size` and `text_cap_chars` (`score/make_chunks.py`). `pillars`, `primary_query`, `search_queries`,
`criteria` and `cdp_port` are read by **no code at all** — `pillars` is duplicated as inline regexes in
`position/field_position.py` and `score/signal_score*.py`, and `criteria` exists only for hand
substitution into `agents/*.md`. Porting to another hackathon means editing those regexes, plus the
literal `WebMCP` strings still hard-coded in `verify/membership.py`, `verify/membership_fast.py`,
`verify/enrich.py` and `score/signal_score.py`.

## The data pipeline

```
slugs ──▶ membership ──▶ pages ──▶ parsed ──▶ enriched ──▶ chunks ──▶ judge reports ──▶ aggregate
```

**The chain has a hole.** `verify/parse_pages.py` reads `data/pages/*.html`, and **nothing in this repo
writes that directory** — `membership_check.py` emits JSON only, `membership_fast.py` dumps `.txt`
innerText. Fetching and saving the confirmed pages as HTML is a step you must supply before `parse_pages`
runs.

Filenames the no-argument scripts agree on, all under gitignored `data/`:
`data/pages/<slug>.html` → `data/submissions_parsed.json` → `data/submissions_enriched.json`;
`judge/chunk_NN.json` (plus `chunk_NNb.json`, the double-judge copy).
Judge output is collected by hand into two TSVs: `results.tsv` (`chunk slug L E I C total`) and
`dist.tsv` (`chunk 80plus 70_79 60_69 50_59 under50`). `runs/webmcp-2026-09/data/` holds a real pair.

## Two transports, and which route needs which

- `lib/browser.py` — CDP-driven headless Chrome. `/software/search` and listing routes will not talk to a
  plain client at all. Launch your own instance on your own port (`/json/new` needs PUT; attaching to a
  Chrome someone else drives hangs on `ws.recv()`). Subresource blocking is on by default and is what
  makes exhaustive paging affordable. **It is imported by nothing** — it is the clean extraction of a
  pattern that all four CDP scripts still inline separately (seven hand-rolled `def call()` wrappers, the
  blocked-URL list pasted into three files). Route new CDP work through it rather than copying the
  boilerplate a fifth time. `lib/cdp_fetch.py` and `lib/waf_fetch.py` are dead: nothing references them,
  and `waf_fetch.py` carries another machine's `sys.path` and wants an untracked `lib/cookies.txt`.
- `lib/fetch.py` — plain HTTP with WAF detection. Project pages, public profiles, hackathon pages and
  Devpost's JSON APIs. Use this path wherever it works; it is an order of magnitude faster.
  **Its challenge detection used to reject every legitimate Devpost page**: `awswaf` was a marker, and
  Devpost ships `window.AwsWafCookieDomainList` in its normal `<head>` about 1.2KB in, so a healthy 136KB
  project page tripped it and `membership_check.py` could not fetch anything at all. The markers are now
  `token.awswaf.com`, `challenge-container`, `Just a moment`, `captcha-container` — verified absent from a
  live project page, a hackathon page and the search API. `get()` also drops the length floor for JSON
  responses, which a 1KB API reply used to fail. If you add a marker, regression-test it against a real
  page before trusting it.

The dangerous failure is silent: Devpost's AWS WAF answers concurrency with a 202 challenge page in a
200-shaped body, which parses cleanly as "profile with zero projects". **Never treat a short or
challenge-shaped body as data** — `Challenged` must propagate to a caller that counts it as unresolved.
Rate limits are per-route: about four workers on project pages, one sequential driver on search.

## Invariants the code encodes

Not style preferences — each was paid for once, and PITFALLS.md names the price.

- **Two independent counts.** Search sweep and participants→portfolios are separate routes; report both
  totals and their agreement (the run landed on 2,396 and 2,402). Neither is a census — search has a
  measured 2.3% index gap, and the official gallery is usually unpublished.
- **Page until a page returns zero new slugs**, and assert against the header's own total (*"1–24 of
  2484"*). A sweep that stopped at page 26 of 104 was treated as the whole field for a day and a half.
- **Membership is the page's own `#submissions` block**, never the marker text appearing anywhere on the
  page. Rows marked `challenged` are unresolved, not negative — re-run them before quoting a total.
- **Match on exact slug, then re-dedupe independently on `data-software-id`** and require agreement.
  Devpost suffixes duplicate titles: `countersign-vmy83b` and `countersign-4ym0tq` are different projects.
- **Signal scores shortlist; they never rank.** `score/signal_score.py`'s regexes were written from one
  entry's own vocabulary and put the deep-verified #1 at 444th and their author's entry at 2nd.
- **Widen every rarity regex until it hurts and publish the wide number.** `field_position.py` reports
  narrow and wide side by side for exactly this reason.
- **Double-judge one slice** (`--double-judge N`). Measured inter-judge spread was 6.1 points mean, 13 at
  worst — wider than most gaps being resolved. Report rank as a band at least that wide; `aggregate.py`
  computes it and prints the warning. Calibration also drifts hard between slices (4 to 35 entries
  clearing 80 under one rubric), so normalise within slice before comparing across them.
- **Blind every evaluation of your own work.** Never give a scorer the author, prior scores, or session
  history, and never run a judge from a directory holding your own analysis.

## Agent prompts

`agents/*.md` are templates whose `{{PLACEHOLDERS}}` you substitute before dispatch, not skills to invoke.
`triage-slice` fans out one per chunk on a cheap model; `field-position` runs before building; `fast-judge`
and `deep-verify` judge your own entry blind; `census` is the slow enumeration route.

Fan-out rules that come from things going wrong:

- Carry the chunk's first and last slug into the prompt as an assertion — `make_chunks.py` prints them.
  One judge read the wrong file and reported confidently.
- Give every agent a uniquely named scratch path. Two judges both wrote `batch_000.txt`.
- Keep your own `chunk → agent → status` file. At 25 live agents the runtime list stops being enough.
- Chunks run ~740KB; say so, or an agent silently reads the first page and scores 40 rows.
- Do not read a subagent's `.output` file — it is the entire JSONL transcript. Wait for the notification.
- Hand review agents a read-only copy of the tree. One deleted the working tree mid-review.

## Environment traps

- **Never run python with `/tmp` as cwd** — a stray `/tmp/inspect.py` shadows the stdlib and the traceback
  blames an unrelated library. Work in a directory you created.
- `pgrep -f "collect.py"` matches the shell whose own command line contains it. Use `pgrep -f
  "[c]ollect.py"` or a pidfile, and check whether a reported failure is the watcher rather than the work.
- No `timeout` on macOS — use `curl --max-time` or `gtimeout`.
- zsh expands `--include=*.md` before grep sees it; quote the pattern.
- `grep -oE '.{0,200}foo.{0,250}'` over a minified bundle exceeds complexity limits; use python.

## Film pipeline

`build/film/make.sh` runs narrate → record (flat) → compose → mux. The rule the pipeline exists to
enforce: **shoot flat, draw the camera and cursor afterwards at 60fps.** Chrome hands over a frame only
when the picture changes, so any continuous motion baked into capture is pinned to the encoder's rate and
stutters. `brisk.py` plays a window faster rather than cutting when the cut runs over the cap.

## Working in this repo

- `runs/` archives what a completed run measured; `runs/*/data/` is checked in, `runs/*/corpus/` is not
  (tens of megabytes, hours to re-derive — keep a copy outside the repo). `score/aggregate.py` runs
  against the checked-in TSVs and reproduces FINDINGS.md's headline numbers exactly (216 at 80+,
  inter-rater mean +6.1, max +13) — it is the one end-to-end verified path in the repo, and the right
  smoke test after touching scoring.
- `lib/cookies.txt` is **not** gitignored, and `lib/waf_fetch.py` expects a session cookie jar there. Add
  it to `.gitignore` before creating one.
- Two band counts in `runs/webmcp-2026-09/FINDINGS.md` disagree with the `dist.tsv` beside them: 50–59 is
  535 not ~475, and under-50 is 318 not ~358 (the totals still sum to 2,391). Trust the TSV.
- `build/evidence/reproduce.sh`, `build/evidence/self-audit.py` and `build/film/make.sh` are the originals
  from the WebMCP entry, kept as worked examples. They reference `bench/`, `npm test` and paths that only
  existed in that project. Port them; do not run them here.
- The playbook's own rule for a submitted entry: once the deadline passes the judged repository is frozen
  — deploy fixes to the live host, and leave the repo alone.
