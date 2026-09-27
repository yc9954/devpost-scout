<h1 align="center">Scout</h1>

<p align="center"><strong>One chat agent and one dashboard for entering a Devpost hackathon on evidence, not optimism.</strong></p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#what-it-does">What it does</a> ·
  <a href="#screens">Screens</a> ·
  <a href="#the-eight-tools">Tools</a> ·
  <a href="#architecture">Architecture</a> ·
  <a href="#http-api">API</a> ·
  <a href="#the-toolkit-underneath">Toolkit</a> ·
  <a href="#credits">Credits</a>
</p>

<p align="center">
  <img src="docs/screenshots/01-chat-open-hackathons.jpg" alt="Scout — chat agent listing open Devpost hackathons" width="900">
</p>

Scout wraps a hackathon-research toolkit — a census of every hackathon Devpost lists, a corpus of 2,300 winning projects, a rubric parser that reads a hackathon's judging criteria verbatim, a field enumerator, an idea generator that scores proven mechanisms against the rubric, and an Obsidian vault of facets and gaps — into a single product you talk to. Ask *what's open this week*, *scout RevenueCat Shipaton 2026*, or *winners about agents for accessibility*, and every number that comes back is measured or quoted from Devpost. Nothing is invented; when a number is weak the agent says so.

The UI is built from the [21st-dev/1code](https://github.com/21st-dev/1code) component kit (Apache-2.0) — 32 of its `components/ui` files are used byte-for-byte, and its agent layout, sidebar, message bubbles and tool-call rows are adapted for Scout's cards.

---

## Quick start

```bash
git clone https://github.com/yc9954/devpost-scout && cd devpost-scout
./run.sh                      # → http://127.0.0.1:8780
```

That is the whole install: Python 3.10+ and nothing else. The built UI (`web/dist`) and the data the product needs (`data/hackathons*.jsonl`, `data/ideas.db`, `data/facets.jsonl`, ~31 MB) are committed, so the app runs offline in **local mode** — a deterministic router over the same tools, with templated prose that carries the real numbers.

To let Claude drive the conversation instead, add a key and restart:

```bash
echo 'ANTHROPIC_API_KEY=sk-ant-…' > .env      # or export it
pip install anthropic                           # only needed for Claude mode
./run.sh                                        # sidebar badge switches from `local` to `claude`
```

Claude mode uses `claude-opus-5` with adaptive thinking and a streaming tool loop (up to 8 rounds, parallel tool calls answered together). Both modes emit the same event stream, so the UI, the cards and the persisted transcripts are identical — Claude adds the reasoning and the prose.

Other ways in:

| | |
| --- | --- |
| `python3 -m scout --port 8780` | the server alone (no browser open) |
| `cd web && npm install && npm run dev` | Vite dev server on :5173 with `/api` proxied to :8780 |
| `cd web && npm run build` | rebuild `web/dist` after changing the UI |
| `python3 -m unittest discover -s tests/scout` | 21 tests, no network (data derivation, filters, HTTP routes, one local-mode chat over SSE) |

---

## What it does

**Chat.** Name a hackathon and Scout resolves it on Devpost, reads the judging criteria *verbatim* with their weights, flags the tie-break criterion (Devpost resolves ties on the first-listed criterion, so it decides placements in a bunched field), lists the requirements that fail an entry outright, and caches the brief. Ask for ideas and it scores every mechanism × domain pair from 8,636 faceted winners against that rubric, reporting expected wins and the evidence projects behind each candidate. Ask about winners and it shortlists from the 2,300-winner corpus — and tells you, every time, that a shortlist over 100-character taglines is not a ranking. Ask what's open and it filters the census by *derived* status (the end date Devpost states vs today), not the snapshot flag.

**Dashboard.** Open / upcoming / ending-in-7-days / prize-pool tiles, status tabs, theme filter, search, sort by deadline · prize · registrations, thumbnails, deadline countdowns, and a detail dialog with a **Scout this** button that opens a chat and runs the pipeline. A **Refresh census** button re-runs the ~1,540-request Devpost census in the background with a progress bar and swaps the file in only when the collector exits cleanly.

**Honest by construction.** Status is derived from dates, prize totals use static FX and say so, an unpublished gallery is reported as *unmeasured* rather than empty, and the idea generator's under-occupancy claims carry the caveat that they are measured against independence in a regex taxonomy. These rules come from `PITFALLS.md`, where each one was paid for once.

---

## Screens

### Chat — "What's open this week?"
The agent calls `list_hackathons(status=open, sort=deadline)`; the tool row expands into hackathon cards (thumbnail, organiser, derived status, countdown, parsed prize, registrations, themes), followed by prose that restates the same numbers.

![Open hackathons as cards inside the chat](docs/screenshots/01-chat-open-hackathons.jpg)

### Chat — "Scout RevenueCat Shipaton 2026"
`hackathon_brief` resolves the host and parses the rubric; the card lists every criterion with its weight and highlights the tie-break. (On this page Devpost lists the 21 prize categories under *Judging Criteria*, and the parser reports exactly what the page says.) `ideate` then runs against the cached brief.

![Resolved rubric card with weights and the tie-break criterion](docs/screenshots/02-chat-brief-rubric.jpg)

### Chat — "Winners about agents for accessibility"
`search_winners` is FTS5 over title + tagline of the winners corpus. The card is labelled *shortlist · not a ranking* and the prose repeats the warning.

![Winners shortlist card](docs/screenshots/03-chat-winners-shortlist.jpg)

### Chat — census stats
`census_stats` renders the same tiles the dashboard uses, plus top themes, top organisers and the deadlines of the next 14 days.

![Census statistics inside the chat](docs/screenshots/06-chat-census-stats.jpg)

### Dashboard
Every hackathon in the census, filtered to what is open today. Tiles at the top are computed from the derived status, not the census snapshot.

![Dashboard with stat tiles, filters and the hackathon grid](docs/screenshots/04-dashboard.jpg)

### Dashboard — detail
Click a card for the organiser, dates, prize, registrations, links to Devpost and the gallery, and the brief once it has been resolved. **Scout this** starts a chat with `scout <title>`.

![Hackathon detail dialog with the Scout this action](docs/screenshots/05-dashboard-detail.jpg)

Screenshots were taken in local mode against the committed data (census of 2026-09-06, viewed on 2026-09-27); Claude mode renders the same cards with model-written prose.

---

## The eight tools

Both modes share one tool table (`scout/tools.py`, JSON schemas in `SCHEMAS`). Each tool returns `{ok, summary, data}`; `data` is the card payload the UI renders.

| Tool | What it wraps | Network | Notes |
| --- | --- | --- | --- |
| `list_hackathons` | in-memory census (`scout/data.py`) | no | status derived from dates; prize parsed by `hub.store.prize_parts`; sort by deadline / prize / registrations |
| `hackathon_brief` | `discover/hackathon.py` — `search()` + `build()` | **yes** | criteria verbatim with weights, `tiebreak_criterion`, requirements, prizes; cached in `data/run/briefs/` |
| `search_winners` | FTS5 `projects_fts` in `data/ideas.db` | no | 2,300 winners; summary always says *shortlist, not a ranking* |
| `field` | `hub/collect_gallery.collect()` | **yes** | the hackathon's own gallery; cached in `data/run/fields/`; an unpublished gallery is reported as unmeasured |
| `ideate` | `hub/ideate.generate()` over `data/facets.jsonl` | no | needs a cached brief; uses the cached field for that host when present |
| `vault_lookup` | grep over `vault/` notes | no | mechanisms, domains, gaps, projects |
| `census_stats` | in-memory census | no | counts, open prize pool, themes, organisers, deadlines in 14 days |
| `scout` | brief → field → ideate as a background job | **yes** | streamed progress; also `POST /api/jobs/scout` |

**Local mode routing** (no key): "open / upcoming / deadline / prize" → `list_hackathons`; a hackathon name or URL ("scout X", "criteria of X") → `hackathon_brief` (+ `ideate` when ideas are requested); "winners / past projects about Y" → `search_winners`; "mechanism / domain / gap Y" → `vault_lookup`; "stats / how many" → `census_stats`; anything else explains what it can do.

**Claude mode**: the system prompt is the product's rules (measured numbers only, cite Devpost, shortlist ≠ rank, state the census date); Claude picks tools, runs several in parallel when useful, and writes the prose. Tool failures go back as `tool_result` with `is_error` so the model can recover or say what it could not measure.

---

## Architecture

```
browser (web/dist — React 19, 1code UI kit, zustand)
   │  GET /api/…  ·  POST /api/chats/{id}/messages → SSE
   ▼
scout/server.py     ThreadingHTTPServer (stdlib), static web/dist + SPA fallback, SSE with replay
   ├─ scout/data.py         census (13,843 rows) + winners FTS + facets + brief cache, all in memory
   ├─ scout/tools.py        the eight tools → {ok, summary, data}
   ├─ scout/local_agent.py  deterministic router → same event stream
   ├─ scout/agent.py        Claude mode: anthropic SDK, claude-opus-5, adaptive thinking, streaming tool loop
   ├─ scout/jobs.py         background jobs (scout pipeline, census refresh) with an event log
   └─ scout/config.py       .env loader, port, model, census date
        │
        ▼ wraps, never re-implements
discover/hackathon.py · hub/{store,collect_gallery,extract,ideate,collect_hackathons}.py · lib/fetch.py · vault/
```

**Event stream** for one message (`event:` / `data:` lines):
`message_start` → `thinking` (status line) → `tool_call {id, name, input}` → `tool_result {id, name, ok, summary, data}` → `text_delta` × n → `message_end`, with `job_progress` for long tools and `error` on failure. Transcripts persist as JSON under `data/chats/` and reopen with their cards intact.

**Frontend** (`web/`): Vite 7, React 19, TypeScript strict, Tailwind 3 with 1code's `tailwind.config.js` and `globals.css` (primary `#0034FF`, dark by default), `motion` for the tool-row expand/collapse and card entrance, `lucide-react` icons, `sonner` toasts, `react-markdown` + `remark-gfm` for prose. `src/api.ts` parses SSE over `fetch` + `ReadableStream`; `src/store.ts` folds events into message parts; `src/components/cards/*` render each tool's payload. `?mock=1` replays a canned stream for UI work without the engine.

The full contract both halves implement is [`docs/SPEC.md`](docs/SPEC.md).

---

## HTTP API

| Route | Purpose |
| --- | --- |
| `GET /api/health` | `{ok, mode: "claude" \| "local", model, census_date, counts: {open, upcoming, ended, total}, today}` |
| `GET /api/hackathons?status=open\|upcoming\|ended\|all&q=&theme=&sort=deadline\|prize\|registrations&limit=` | dashboard rows |
| `GET /api/hackathons/{id}` | one row, plus `brief` when already resolved |
| `GET /api/stats` | counts, open prize pool, themes, organisers, deadlines in the next 14 days |
| `GET /api/winners?q=&limit=` | FTS shortlist over the winners corpus |
| `GET /api/chats` · `GET /api/chats/{id}` · `POST /api/chats` | chat list, transcript, new chat |
| `POST /api/chats/{id}/messages` `{text}` | run the agent — **SSE** |
| `POST /api/jobs/scout` `{hackathon}` · `POST /api/jobs/refresh` | background jobs |
| `GET /api/jobs` · `GET /api/jobs/{id}` · `GET /api/jobs/{id}/stream` | job list, status, **SSE** (replay + live) |

```bash
curl -s 'http://127.0.0.1:8780/api/hackathons?status=open&sort=prize&limit=3'
curl -sN -X POST http://127.0.0.1:8780/api/chats/$(curl -s -X POST http://127.0.0.1:8780/api/chats | python3 -c 'import sys,json;print(json.load(sys.stdin)["id"])')/messages \
     -H 'Content-Type: application/json' -d '{"text":"What is open this week?"}'
```

---

## Data

| File | Rows | What it is |
| --- | --- | --- |
| `data/hackathons_all.jsonl` | 13,843 | full census from Devpost's `/api/hackathons` (plain JSON, no pagination ceiling) |
| `data/hackathons.jsonl` | 1,863 | the rows with thumbnails and `time_left_to_submission`; merged over the census by id |
| `data/ideas.db` | 13,843 + 2,300 | SQLite: `hackathons` (prize in USD, state, dates, themes) and `projects` (winners) with an external-content FTS5 index |
| `data/facets.jsonl` | 8,636 | mechanism / domain / user / substrate facets per winning project, from `hub/extract.py` |
| `vault/` | 13,599 notes | Obsidian vault: projects, mechanisms, domains, hackathons, claims, convergences, gaps |

The census date is the mtime of `hackathons.jsonl` (2026-09-06). **Refresh census** in the dashboard, or `python3 hub/collect_hackathons.py --out data/hackathons.jsonl`, re-collects it. Status shown anywhere in the product is derived at request time from `submission_period_dates` against today's date, and `census_state` keeps the snapshot value for comparison.

---

## The toolkit underneath

Everything the product calls is a standalone script you can run on its own, written and priced during a real entry (The WebMCP Challenge, 2,392 submissions):

```
discover/   resolve a hackathon (criteria, weights, tie-break, requirements, prizes); enumerate the field two independent ways
verify/     decide which projects are actually in this hackathon (membership is the page's own block, never a marker string)
position/   count how crowded your idea's pillars are before you build — five tests that kill an idea (position/IDEA-SELECTION.md)
score/      slice the corpus, fan out blind LLM judges, aggregate with error bars (double-judge one slice; report rank as a band)
hub/        the census, the winners gallery, the taxonomy, the vault, the gap finder, the idea generator
build/      film the demo (shoot flat, draw the camera afterwards), evidence discipline, the write-up, shipping
write/      what winning write-ups actually do; the four impact anchors
agents/     {{placeholder}} prompts that did the work
lib/        a CDP-driven Chrome and a WAF-aware fetch (Devpost answers concurrency with a 200-shaped challenge page)
runs/       one full run's dataset and findings
```

Read [`METHOD.md`](METHOD.md) for the pipeline in order and [`PITFALLS.md`](PITFALLS.md) before trusting any number you produce — every rule in the product is priced there. The `/scout` skill in `.claude/skills/scout/` drives the same pipeline from Claude Code.

---

## Repository layout

```
scout/            the product's Python package (server, data, tools, agents, jobs, config)
web/              the product's UI (Vite + React + 1code kit); web/dist is committed
docs/             SPEC.md (the contract) and screenshots/
tests/scout/      21 unittest cases, no network
data/             committed: census, winners DB, facets · local only: pages/, projects_full.jsonl, run/, chats/
vault/            the Obsidian vault
discover/ hub/ verify/ position/ score/ build/ write/ agents/ lib/ runs/   the toolkit
run.sh            build the UI if missing, start the server, open the browser
```

---

## Limitations

- The census is a snapshot; "open" is derived from the dates Devpost stated on the census date. Refresh before trusting a deadline.
- `hackathon_brief` reports what the hackathon page says under *Judging Criteria*. Some pages list prize categories there; the parser does not second-guess them.
- `search_winners` matches ~100-character taglines. It shortlists; it never ranks. Read the entries.
- `ideate` measures under-occupancy against independence in a regex taxonomy over winners. Widen the patterns before believing a cell is empty.
- Prize totals use static FX for non-USD prizes and are approximate.
- Claude mode needs an Anthropic key; without one the product runs in local mode with templated prose.

---

## Credits

- UI components, styles and layout patterns from [21st-dev/1code](https://github.com/21st-dev/1code), Apache License 2.0. `web/src/components/ui/README.md` lists which files are verbatim and which were adapted.
- Data from [Devpost](https://devpost.com) public pages and JSON endpoints, collected by the scripts in `hub/`.
- Claude mode uses the [Anthropic Python SDK](https://github.com/anthropics/anthropic-sdk-python).

MIT for this repository's own code; see the 1code license for the vendored components.
