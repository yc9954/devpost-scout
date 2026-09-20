---
slug: "stock-agent-t4qr0h"
url: "https://devpost.com/software/stock-agent-t4qr0h"
title: "Stock Agent"
hackathon: "QuantumHacks"
organization: "Quantumhacks"
winner: true
words: 553
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/on_device_local"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Stock Agent

> Stock Agent: privacy-first trading intelligence. Live grades in Chrome, email digests on your schedule; holdings never leave your device. Research that traders trust and buy.

[Devpost](https://devpost.com/software/stock-agent-t4qr0h) · hackathon [[QuantumHacks]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[on_device_local]]
**domain** [[finance_payments]] [[labor_employment]] [[supply_logistics]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[web_dom]]

**stack** actions, chrome, css, extension, fastapi, fintech, github, heroku, html, httpx, javascript, manifest, postgresql, privacy

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Gemini grade explanations Email Report Preview Automated email scheduler to get daily/weekly watchlist reports in email inbox and Gemini API key to get explanations of watchlist grades Various tickers shown in light mode sorted by grade (STRONG BUY at top, HOLD in middle and AVOID at bottom) Portfolio tracker that can be sorted by symbol (alphabetical order), grade, profit/loss & currency Inspiration Retail traders are drowning in noisy stock tips, yet every tool that promises clarity wants your holdings, your broker login, or runs opaque AI you can't verify. We wanted research-grade watchlist alerts without ever uploading portfolio data or API keys. What it does Stock Agent is a privacy-first Chrome extension that grades your watchlist using deterministic financial rules — no AI in the scoring loop. Track up to 25 tickers across USA, Canada, and India with live STRONG BUY / HOLD / AVOID grades, keep private holdings on-device, and schedule automated email digests. The cloud only ever sees your email, ticker symbols, and schedule. How we built it Chrome Manifest V3 extension (HTML/CSS/JS) with two-tier storage — shares, buy prices, and Gemini key stay in chrome.storage.local and never leave the device FastAPI backend on Heroku serving POST /api/subscribe (upsert delivery prefs) and POST /api/quotes/snapshot (live grading) yfinance for market data + a sector-aware grading engine (5 metrics: D/E, PEG, ROE, 200-SMA, RSI) with tiered news risk penalties Supabase PostgreSQL for user delivery records (RLS-hardened, service-role only) AWS EventBridge + Lambda triggering cron every 5 minutes; Resend for DKIM-signed HTML email delivery Optional Gemini BYOK for plain-English grade explanations (browser → Google directly, never our servers) Challenges Enforcing a hard privacy boundary — a runtime assertNoPrivateLeak() guard that throws if any holdings data appears in an outbound payload Matching user schedules across global timezones within a 5-minute dispatch window without double-sending Making grades readable at Chrome popup size while still conveying why a stock scored what it scored — without feeling like a black box Accomplishments that we're proud of Zero private data ever leaves the browser — verified by automated runtime checks, not just convention Same data always produces the same grade — fully deterministic, fully auditable Multi-region support (NASDAQ, NYSE, TSX, NSE, BSE) with sector-aware thresholds that don't penalize a bank for being leveraged like a tech stock Email reports deliver on time globally thanks to migrating from GitHub Actions cron (30–90 min delays) to AWS EventBridge (±1 second) What we learned Privacy can be a product feature, not just a disclaimer. Separating local state from cloud delivery made the architecture clearer, the security model auditable, and the value proposition easier to communicate. We also learned that deterministic rules build more user trust than AI — people want to know why a stock scored 4/5. What's next The MVP is live — grades run, emails deliver, privacy holds. Next up: Push alerts for grade changes via Chrome service worker (know the moment a ticker flips from HOLD to STRONG BUY without waiting for a scheduled email) Portfolio correlation warnings that flag when too many positions share the same sector or momentum risk Public grading methodology page where anyone can verify scoring without reading source code Onboarding real traders, collecting feedback, and shipping what they actually ask for — Stock Agent is built to stay useful as the audience scales <div