# Scout — product spec (the contract both builders implement)

**Scout** turns the devpost-scout toolkit (census, rubric parsing, field enumeration, idea
selection, winner corpus, vault) into one product: a chat agent you talk to, plus a management
dashboard of hackathons. Everything shown is measured or quoted from Devpost — the agent never
invents numbers. Repo root is the working directory for everything below.

## 1. Layout
```
scout/              Python 3.10+ package, stdlib HTTP server (no framework) — port 8780
  __main__.py       python3 -m scout  → serves web/dist + /api
  server.py         ThreadingHTTPServer, routes, SSE
  data.py           loads data/hackathons.jsonl (+ data/ideas.db, data/facets.jsonl, vault/) into memory
  tools.py          the agent's tools — plain functions returning JSON-able dicts; each wraps toolkit modules
  agent.py          Claude mode (anthropic SDK, claude-opus-5, streaming tool loop) — used when ANTHROPIC_API_KEY is set
  local_agent.py    Local mode — deterministic intent router over the same tools; used when no key. Same event stream.
  jobs.py           background jobs (scout run, census refresh) with progress events
web/                Vite 7 + React 19 + TypeScript + Tailwind 3 — UI kit copied from reference/1code (Apache-2.0)
run.sh              ./run.sh → build web if needed, start server, open http://127.0.0.1:8780
```
`.env` (gitignored) may hold `ANTHROPIC_API_KEY=...`; `scout/config.py` loads it. Never print it.

## 2. Data (already on disk — never re-fetch on startup)
- `data/hackathons.jsonl` — 1,863 rows from Devpost `/api/hackathons` (census of 2026-09-06). Fields: id, title, url, open_state (open|upcoming|ended), submission_period_dates ("Jul 31 - Oct 01, 2026"), time_left_to_submission, themes[{id,name}], prize_amount (HTML with `<span data-currency-value>`), prizes_counts, registrations_count, organization_name, thumbnail_url (protocol-relative), featured, winners_announced, submission_gallery_url.
- `data/hackathons_all.jsonl` — full census 13,843 rows (same shape) — use for search/stats only.
- `data/ideas.db` — SQLite: `hackathons` (13,843; prize_usd_approx, state, dates, themes, host…), `projects` (2,300 winners: slug, title, tagline, host, hackathon_title, is_winner, members…), `projects_fts` (FTS5, external content — query with `MATCH`, never DELETE).
- `data/facets.jsonl` — per-project facets (mechanism/domain/user/substrate) used by `hub/ideate.py`.
- `vault/` — Obsidian notes: `projects/`, `mechanisms/`, `domains/`, `_gaps/`, `_claims/`, `_convergences/`, `hackathons/`.
- `hub/store.py` (`cmd_search`, `fts_query`, `prize_parts`), `discover/hackathon.py` (`search(name)`, `build(host)` → config with criteria verbatim + weights + tiebreak_criterion + requirements + prizes), `hub/collect_gallery.py` (`collect(host, winners_only=…)`), `hub/extract.py` (`facets_of`), `hub/ideate.py` (`generate(rows, field, cfg, min_wins)`), `hub/collect_hackathons.py` (census refresh).
- Derive **status** at request time: parse the end of `submission_period_dates` (+year) and compare to today → `open` (end ≥ today and start ≤ today), `upcoming`, `ended`; keep `open_state` as `census_state`. Parse `prize_amount` → `prize_usd` (int) via `hub.store.prize_parts`. Normalise `thumbnail_url` to https.

## 3. HTTP API (JSON; SSE where noted)
| Route | Purpose |
|---|---|
| `GET /api/health` | `{ok, mode: "claude"|"local", model, census_date, counts:{open,upcoming,ended,total}}` |
| `GET /api/hackathons?status=open|upcoming|ended|all&q=&theme=&sort=deadline|prize|registrations&limit=` | dashboard rows (see §5 `Hackathon`) |
| `GET /api/hackathons/{id}` | one row + `brief` if already resolved (cached in `data/run/briefs/{host}.json`) |
| `GET /api/stats` | `{counts, prize_total_open, themes:[{name,count}], top_orgs:[…], deadlines_next_14d:[…]}` |
| `GET /api/winners?q=&limit=` | FTS over winners (title+tagline) → `[{slug,title,tagline,host,hackathon_title,url}]` |
| `GET /api/chats` / `GET /api/chats/{id}` | chat list / transcript (JSON files under `data/chats/`) |
| `POST /api/chats` `{title?}` → `{id}` | new chat |
| `POST /api/chats/{id}/messages` `{text}` → **SSE** | run the agent on the message; events below; the transcript is persisted |
| `POST /api/jobs/scout` `{hackathon}` → `{job_id}`; `GET /api/jobs/{id}/stream` SSE | full scout pipeline (brief → field → ideas) with progress |
| `POST /api/jobs/refresh` | re-run the census in the background (progress via the same job stream) |

### SSE events for a message (`event: <type>`, `data: <json>`)
- `message_start {chat_id, message_id, mode}`
- `text_delta {text}` — assistant prose (markdown), streamed
- `thinking {text}` — optional short status ("Resolving the hackathon…")
- `tool_call {id, name, input}` — the moment a tool is invoked
- `tool_result {id, name, ok, summary, data}` — `data` is the card payload (§5); `summary` one line
- `job_progress {job_id, step, pct, note}` — for long tools
- `error {message}`; `message_end {usage?}`

## 4. Tools (same in both modes)
| name | input | returns (data) | notes |
|---|---|---|---|
| `list_hackathons` | status, query, theme, sort, limit | `{rows:[Hackathon], total}` | pure, instant |
| `hackathon_brief` | name_or_url, pick | `Brief` | network (Devpost) via `discover/hackathon.py`; cache to `data/run/briefs/` |
| `search_winners` | query, limit | `{rows:[Winner]}` | FTS; **shortlists, never ranks** (say so) |
| `field` | host, limit, winners_only | `{rows:[Project], total, source}` | network via `hub/collect_gallery.collect`; cache `data/run/fields/{host}.jsonl`; when the gallery is unpublished say so — an empty field is not an empty field |
| `ideate` | host | `{candidates:[Idea]}` | `hub/ideate.generate` with facets + the cached brief; needs `hackathon_brief` first |
| `vault_lookup` | query, kind (mechanism|domain|gap|project|any) | `{notes:[{title, path, excerpt}]}` | grep vault titles/bodies |
| `census_stats` | — | stats payload | pure |
| `scout` | hackathon | job id + streamed progress; final `{brief, field, ideas}` | = brief → field → ideate, background job |

Local mode routing (no key): map the message to a tool by simple rules — "open/upcoming/ending/deadline/prize" → `list_hackathons`; a hackathon name or URL ("scout X", "what should I build for X", "rubric/criteria of X") → `hackathon_brief` (+ `ideate` when asked for ideas); "winners/past projects about Y" → `search_winners`; "mechanism/domain/gap Y" → `vault_lookup`; "stats/how many" → `census_stats`; otherwise reply with what it can do. Prose is templated but concrete (numbers from the tool result).

Claude mode: system prompt = the product's rules (measured numbers only; cite Devpost; shortlist ≠ rank; state census date; ask before slow network tools only if the user seems unsure); tools as above with JSON schemas; `claude-opus-5`, `thinking: {type:"adaptive"}`, streaming, manual tool loop, max 8 tool rounds; parallel tool_use handled; `eager_input_streaming` not needed.

## 5. Card payloads (frontend renders these)
```ts
Hackathon { id, title, url, host, org, status:'open'|'upcoming'|'ended', census_state, dates, start?, end?, days_left?, themes:string[], prize_usd, prize_display, prizes_counts, registrations, thumbnail, featured, winners_announced, gallery_url, location }
Brief { title, host, url, criteria:[{label, text, weight?}], weighting:'equal'|'weighted'|'unknown', tiebreak_criterion, requirements:[string], prizes:[{name, amount?}], dates, criteria_source }
Winner { slug, title, tagline, host, hackathon_title, url, is_winner }
Project { slug, title, tagline, url, is_winner, members? }
Idea { title, mechanism, domain, user, substrate, expected_wins, evidence:[{slug,title,host}], why, risk }
```

## 6. Frontend (web/) — 1code look, verbatim where possible
Copy from `reference/1code/src/renderer`: `components/ui/*` (all), `styles/globals.css` + `agents-styles.css` (drop `@source streamdown`), `lib/utils.ts`, `lib/utils/format-time-ago.ts`, `tailwind.config.js` + `postcss.config.js` (drop plugins not installed), and adapt `features/layout/agents-layout.tsx`, `features/sidebar/agents-sidebar.tsx`, `features/agents/ui/{agent-user-message-bubble,agent-tool-call,agent-thinking-tool,agent-web-search-collapsible,agent-message-usage}.tsx`, `components/ui/prompt-input.tsx`, `text-shimmer`, `typewriter-text`. Strip tRPC/electron/jotai-store imports; keep class names, motion (`motion/react`), lucide icons, sonner toasts, dark theme default (`.dark` on html). Keep `--primary: 228 100% 50%` (#0034FF).

Screens:
1. **Chat** (default): 1code agents layout — left sidebar (chats list, "New chat", nav to Dashboard, mode badge `claude`/`local`), centre thread: user bubbles, assistant markdown (react-markdown), tool calls as 1code tool-call rows that expand into cards: hackathon grid cards (thumbnail, title, org, status pill, deadline countdown, prize, themes), brief card (criteria list with weights, tie-break highlighted, requirements checklist, prizes), winners list, ideas list (expected wins, evidence chips), vault notes. Prompt input at the bottom (1code prompt-input) with suggestion chips: "What's open this week?", "Scout RevenueCat Shipaton 2026", "Winners about agents for accessibility", "Gaps in health × voice". Streaming text with shimmer while tools run.
2. **Dashboard**: stat tiles (open / upcoming / ending in 7 days / prize pool of open), filters (status tabs, theme select, search, sort), hackathon grid (same card), click → detail drawer (brief if resolved, "Scout this" button → starts a chat message `scout <title>`), census date + "Refresh census" button (job progress).
3. **Runs** (optional): list of scout jobs with progress.

Empty states, skeletons (1code skeleton), toasts on errors. Vite dev proxy `/api` → `http://127.0.0.1:8780`. `npm run build` → `web/dist`. TypeScript strict, `npm run typecheck` passes.
