---
slug: "tarmac-w2gbli"
url: "https://devpost.com/software/tarmac-w2gbli"
title: "Tarmac"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 1312
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/deterministic_policy"
  - "mechanism/measured_ablation"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/legal_justice"
  - "domain/supply_logistics"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
---

# Tarmac

> An airline irregular-ops agent society: sealed-bid seat claims, a mediator with signed rulings, and a bench proving it beats a single planner.

[Devpost](https://devpost.com/software/tarmac-w2gbli) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[benchmark_measured]] [[deterministic_policy]] [[measured_ablation]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[accessibility]] [[legal_justice]] [[supply_logistics]]
**user** [[general_public]] [[legal_professional]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[regulation_legal_text]] [[structured_db]]

**stack** alibaba-cloud, codeql, dashscope, ed25519, function-calling, function-compute, github-actions, mypy, pydantic, pynacl, pytest, python, qwen, qwen-cloud

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tarmac

## Body

Overview: the problem and the society at a glance (five conflicting agents over a scarce seat ledger). Architecture: negotiation flow — sealed bids → row-locked ledger → deadlock → signed mediator ruling → hash-chained log. Offline, zero-key run: the deterministic society negotiating with no API key, byte-identical every time. Negotiation close-up: sealed-bid commit/reveal and contested claims resolving on the ledger. The one number: 3 vs 17 protected passengers stranded, 100% vs 0% special-needs SLA — the measurable gain over a single planner. Auditability: Ed25519-signed, regulation-cited rulings and the hash-chained decision log that replays byte-for-byte. Live on Alibaba Cloud: the Function Compute `/verify` endpoint re-checking the committed live Qwen run in the cloud. Social/OG card (branding closer). Inspiration A 12-year-old flying alone watches the DEPARTED board go red at 6 PM. Behind a door, one dispatcher with two phones is deciding whether she or a transplant cooler gets the last seat to Denver. Airline irregular operations are exactly this: too few seats, too many people who each have a legitimate, conflicting claim, and one overworked human resolving it under pressure. We wanted to rebuild that decision not as a single all-knowing planner, but as an agent society with real, mechanical conflict — and then prove, with a number, that the society does better than the lone planner. What it does Tarmac is an airline-disruption agent society where the conflict is the architecture. Five Qwen agents hold genuinely opposed objectives — Rebooking wants throughput, Crew-Legality enforces duty clocks, Gate/Ground owns turnaround feasibility, Hotel guards the voucher budget, and the Passenger-Advocate fights for minors, medical couriers, and wheelchair passengers. They negotiate through claims on a shared seat ledger backed by SQLite row locks: a claim is a typed function call, not a sentence, so contention has physics — two threads racing the last seat, exactly one wins (tested). Sealed-bid negotiation — in contested rounds agents post SHA256(claim ‖ nonce) commitments before revealing; any reveal that doesn't re-derive its digest is rejected (invariant I4). Negotiation that is provably leak-free. Mechanical deadlock detection — a wait-for cycle, or a resource contested for two or more rounds, triggers mediation. Never vibes-based. Signed, cited rulings — the Duty-Manager mediator reads all five structured position papers and issues a binding, Ed25519-signed ruling that cites the regulation it stands on (invariant I3). With the public key you can verify what was decided and on what regulation without trusting the database. Credibility currency — contesting a claim costs points, winning refunds them with a premium, losing burns them — argument is bounded economically, no infinite loops. Hash-chained decision log — every event extends the chain; tarmac replay re-derives the identical manifest with zero API keys (invariant I5). The one number (the track's ask, a measurable efficiency gain over single-agent baselines): on the frozen storm_dfw storm (180 displaced passengers, 139 legal seats), across 10 seeds, the full society strands 3 protected passengers (medical courier, minor, wheelchair, tight connections) versus 17 for the single greedy planner — at 100% special-needs SLA versus 0%, 9 tight-connection saves versus 0, and zero crew duty violations versus one (a tested invariant, not a hope). The kicker: the same society stripped of its mediator strands 96 overnight — worse than a lone planner — proving the mediator is load-bearing, not decoration. The negotiation core ships as a domain-agnostic library, tarmac-society ( ClaimLedger , DeadlockDetector , Commitment , Mediator , Society , verify_log ), with a formal spec (state machine plus invariants I1–I5). examples/meeting_rooms.py reuses it for meeting-room booking in about 20 lines to prove it isn't airline-shaped. How we built it Python 3.12, shipped as a CLI plus library ( tarmac / tarmac-society ), not a web app. Storage is SQLite with real row-level locking so ledger contention is physical. Built on Qwen Cloud — the transport is swappable but the reasoning is Qwen-only. Five role agents run on qwen3.7-plus (persona-stable objectives across ~60 turns per run, cheap enough to actually benchmark); the Duty-Manager mediator runs on qwen3.7-max with thinking enabled, adjudicating five conflicting position papers with citations. Structured output makes every Claim/Position/Ruling machine-checkable (malformed is rejected); function calling gives ledger ops typed state mutations with row locks; context cache reuses the 4k-token storm prefix every turn (roughly 10x cost saving); the Batch API runs the 60-run ablation offline at -50%; and text-embedding-v4 retrieves regulation passages so rulings cite sources. The LiveQwen DashScope integration is not vaporware behind a flag — 19 deterministic tests ( tests/test_qwen_transport.py , a stub OpenAI-shaped client) drive the real wire path offline (model routing, embedded-JSON-schema structured output, single reject-and-retry on invalid JSON, the enable_thinking mediator flag, per-agent filtering, and text-embedding-v4 batching). Flipping on --live executes that already-verified path; it only adds tokens, not new code. Deployed on Alibaba Cloud Function Compute: a thin WSGI wrapper ( infra/fc/ ) runs the society on managed python3.10 in ap-southeast-1 , deployed straight from source with Serverless Devs (no container registry), at https://tarmac-xceukceokg.ap-southeast-1.fcapp.run . Its /verify endpoint re-runs the full invariant suite against the committed live Qwen run byte-for-byte, in the cloud — so the same replay that guards the offline path is proven server-side on Alibaba Cloud. Quality and security are gated in CI (ruff + mypy, 330 pytest tests at 100% coverage in ~5s, a zero-key offline-replay judge path, CodeQL, Dependabot + pip-audit, TruffleHog, build verification), versioned by python-semantic-release. Challenges we ran into Making negotiation lockable, not literary. Free-text agents produce nothing you can audit or replay. We forced every claim through a typed function call against a row-locked ledger, so a race for the last seat has exactly one winner — and wrote the concurrency test that proves it. Proving the mediator earns its cost. It's easy to assert a society beats a planner; the track asks you to measure it. We built ablation_bench.py (3 conditions x 10 seeds) and were kept honest by our own result: the society without its mediator is worse than a lone planner (96 stranded). That negative column is the strongest evidence in the submission. Verifying the live Qwen wire path without burning tokens. We drove the DashScope structured-output contract, one-retry logic, thinking flag, and embeddings against a stub OpenAI-shaped client in 19 deterministic tests, so --live runs an already-verified path — then ran one full live end-to-end run to capture real model judgement. Accomplishments that we're proud of A measured agent society — 3 versus 17 protected passengers stranded, 100% versus 0% special-needs SLA — not a group-chat demo. Ed25519-signed, regulation-cited rulings you can verify without trusting the database. 330 tests at 100% coverage, a zero-key offline judge path ( verify_offline.py , exit 0), and a reusable tarmac-society protocol library with a formal spec. A negative ablation column that proves the mediator is load-bearing — we published the result that could have embarrassed us. Both a real end-to-end live Qwen run (324-entry hash-chained log, qwen3.7-plus roles + qwen3.7-max mediator, all invariants PASS, replays byte-for-byte) and a live Alibaba Cloud Function Compute deployment whose /verify re-checks that run in the cloud. What we learned Conflict is a feature of a multi-agent system, not a bug to be smoothed away — but only if it's mechanical. The moment a claim became a typed ledger mutation instead of a sentence, deadlock became detectable, mediation became triggerable, and the whole society became measurable. An unmeasured agent society is exactly the demo this track is drowning in; the measurement is the moat. What's next for Tarmac Deepen the live surface — the orchestrator is already deployed on Alibaba Cloud Function Compute ( /verify re-checks the live Qwen run in the cloud); next is streaming per-round ruling signatures and cache-hit stats. More live DashScope runs across seeds — one full live run is already committed at docs/proof/live_run.db ; next is a multi-seed live ablation alongside the offline one. Publish tarmac-society to PyPI and grow the seeded storm generator toward a live GDS integration. <div