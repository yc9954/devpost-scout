---
slug: "crusoe-nemotron-harness"
url: "https://devpost.com/software/crusoe-nemotron-harness"
title: "crusoe-nemotron-harness"
hackathon: "DevNetwork [AI + ML] Hackathon 2026"
organization: "DevNetwork"
winner: true
words: 447
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/scientific_research"
  - "user/legal_professional"
---

# crusoe-nemotron-harness

> Production harness for Nemotron agents on Crusoe Managed Inference. Cost, egress allowlist, tool-arg vetting, snapshots, traces, and budget caps in one facade. 60 tests, zero deps.

[Devpost](https://devpost.com/software/crusoe-nemotron-harness) · hackathon [[DevNetwork -AI - ML- Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**domain** [[developer_tools]] [[scientific_research]]
**user** [[legal_professional]]

**stack** agent-harness, ai-agents, cost-tracking, crusoe, llm, nemotron, nvidia, observability, openai-api, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments i'm proud of
- what i learned
- what's next for crusoe-nemotron-harness

## Body

Inspiration You can stand up a Nemotron agent on Crusoe Managed Inference in an afternoon. What you cannot do in an afternoon is answer the questions a real owner has after the first ten production runs. How much did each run actually cost? Did the agent reach a host I never approved? How often did the model hand a tool the wrong args? Today these answers come from grepping logs and squinting at five different tools. None of them know what a run is for your agent. What it does crusoe-nemotron-harness wraps any Nemotron provider on Crusoe and produces one RunReport with all the numbers a production owner asks for. Drop the harness around your provider, run your agent, get back: total cost, p50 and p95 latency, tool failure count, off-allowlist fetches blocked, token usage against cap, snapshot events, and whether the run aborted on budget. The facade is one context manager. The reports are deterministic. Six modules each own one concern, each mirroring a library the author already shipped: cost.py, egress.py, vet.py, snap.py, trace.py, budget.py. The hackathon contribution is the integration that gets all six right at once on Crusoe. How I built it Pure Python 3.10+. Zero runtime dependencies. Six concern modules under src/crusoe_nemotron_harness/ feeding a single NemotronHarness facade. FakeNemotronProvider is seed-deterministic for tests and demo (no API key needed), CrusoeNemotronProvider speaks the OpenAI-compatible chat-completions wire shape that Crusoe Managed Inference serves Nemotron through today. 60 tests pass in under a tenth of a second. Challenges I ran into The trickiest part was the per-concern boundary. Egress checks and tool-arg vetting can both reject the same call for different reasons, and the budget abort has to fire before the next provider call rather than after. Settled on a context object that the facade hands every concern, and a strict abort-first ordering inside the call sites. Accomplishments I'm proud of Six concerns, one harness, zero deps, 60 tests under 0.1 seconds. Every number in the leaderboard demo is reproducible from seed 3, so judges see the same numbers I do. The CrusoeNemotronProvider wire shape is OpenAI-compatible and the deploy path is documented as a 10-line transport shim. What I learned The OpenAI-compatible chat-completions surface is the de-facto interop layer for hosted Nemotron right now. Treating it as the wire format kept the provider portable across Crusoe, Together, and local NIM containers without changing the harness. What's next for crusoe-nemotron-harness Wire the harness into a live Crusoe-hosted Nemotron instance and publish the deploy script as its own one-command shim. Add a JSON line emitter so the RunReports stream into an observability sink. A streaming-aware token budget that can refuse mid-stream when a long completion exceeds cap. <div