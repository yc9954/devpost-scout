---
slug: "agi-14q6d3"
url: "https://devpost.com/software/agi-14q6d3"
title: "Canary"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 659
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "substrate/code_repository"
---

# Canary

> An autonomous agent that catches the silent bugs your tests and Sentry both miss, then fixes them and writes the regression test.

[Devpost](https://devpost.com/software/agi-14q6d3) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[human_in_the_loop]]
**domain** [[developer_tools]] [[health_clinical]] [[retail_commerce]] [[transportation]]
**substrate** [[code_repository]]

**stack** anthropic, browserbase, claude, next.js, node.js, playwright, react, redis, sentry, typescript, vitest

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for canary

## Body

Inspiration Every team ships two kinds of bugs: The kind that throws (crashes, 500s, timeouts) The kind that's silently wrong (a total that's off, money leaking on every order) Your tests pass, and your app is still broken. These bugs hide for months until a customer or a finance report finds them for you. That's the gap nobody's watching, so we built Canary to watch it. What it does Canary is a self-healing correctness agent — an agent that catches the bug, root-causes it, fixes it, writes the regression test, proves the fix works, and remembers it, with zero humans in the loop. It runs on two oracles: Sentry watches what throws (errors, 500s, traces) and gives the agent the trace context to reason over. Impact: instant root-cause instead of hours digging through logs. The Computer Use Agent is an agent in a real cloud browser that takes action and watches what's silently wrong. Impact: catches the revenue-leaking bugs your tests and error monitoring both miss. In our demo, Canary caught a checkout charging $26 for two $52 seats (a 50% revenue leak every unit test passed right over) and a silent 54% drop in average order value, then fixed both with no human in the loop. Together they power one agentic, memory-backed loop: detect, fix, verify, remember. How we built it TypeScript end to end. A Next.js app is both the seeded checkout and the live dashboard. Claude (Anthropic) is the brain for exploration, triage, and fix synthesis. The explorer drives a real Browserbase cloud browser over CDP, with a synthetic in-page cursor so every click shows up in the live view and the replay. The Sentry SDK supplies trace correlation, unified fingerprinting, breadcrumb reasoning trails, and the resolved-to-regressed lifecycle. Redis backs the knowledge base. Every external dependency sits behind an interface with a fake implementation, so 226 tests and CI run fully offline and live integrations switch on only when their keys are present. Challenges we ran into Browserbase only records the context it hands you. Spin up a fresh one and the replay is blank, so we drive the recorded page directly. Dev-mode hot reload cannot upgrade through a tunnel, so we serve a production build and run all checkout traffic from inside the cloud page. The Sentry and Browserbase SDKs fought over Node globals until we registered the Browserbase shim first. We refused to label a fix "verified" unless a real verifier actually ran the test, which closed the gap between looking done and being done. A naive threshold detector either misses the drop or cries wolf, so median and MAD plus a drop gate plus a post-resolve cooldown made it fire once, on the real thing. Accomplishments that we're proud of A genuinely autonomous loop, no human click, that detects, fixes, verifies, and remembers. Honesty as a feature: verified means a test ran, backed by 226 deterministic offline tests. Every sponsor is load-bearing, not bolted on. Anthropic is the brain, Sentry is the oracle and memory, Browserbase is the body, Redis is the long-term memory. A test suite that grows itself, because every bug found writes the assertion nobody wrote. What we learned Catching silent bugs needs an oracle that declares intent, not one that waits for a crash. Robust statistics matter: median and MAD survive the outliers that sink mean and standard deviation. And observability is strongest as a substrate an agent reasons over, not a dashboard you check after the fact. Sentry is not where bugs die — it is the agent's brain. What's next for Canary Point it at any app and auto-derive invariants instead of seeding them. Open each fix as a real pull request, feeding Sentry's Seer instead of fighting it. A long-horizon miner over accumulated Sentry history that surfaces extreme outliers no single run hits. More oracle types: accessibility, performance budgets, and data-integrity checks. Built With: typescript, next.js, anthropic, claude, sentry, browserbase, redis, playwright, vitest, node.js, react <div