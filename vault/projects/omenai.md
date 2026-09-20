---
slug: "omenai"
url: "https://devpost.com/software/omenai"
title: "OmenAI"
hackathon: " GenAI Genesis 2026"
organization: "GenAI Genesis"
winner: true
words: 485
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# OmenAI

> If you knew the answer before the market did, OmenAI will find you.

[Devpost](https://devpost.com/software/omenai) · hackathon [[GenAI Genesis 2026]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[civic_government]] [[finance_payments]] [[legal_justice]]
**substrate** [[financial_record]] [[structured_db]]

**stack** blockchain, fastapi, isolation-forest, next.js-15, polygon, polymarket-data-api, polymarket-gamma-api, postgresql, python, react-19, redis, scikit-learn, server-sent-events, sqlalchemy

## How they structured the write-up

- 🧠 inspiration
- 🚀 what it does
- ⚙️ how we built it
- ⚠️ challenges we ran into
- 🏆 accomplishments we're proud of
- 📚 what we learned
- 🔮 what's next for omenai

## Body

OmenAI (pronounced "omen eye") 🧠 Inspiration Prediction markets are only as valuable as they are fair. Platforms like Polymarket allow anyone to bet real money on real-world outcomes - FDA approvals, mergers, elections, and even military events. But what happens when someone already knows the answer? If insider trading is illegal on Wall Street, why should it be any different when the same information asymmetry exists on-chain? The key difference is transparency. Blockchain gives us a complete, immutable record of every transaction. OmenAI turns that transparency into accountability. 🚀 What It Does OmenAI is a real-time surveillance dashboard that detects potential insider trading on prediction markets. It: Ingests live trade data from Polymarket Scores every wallet across multiple fraud signals Uses machine learning + AI to detect anomalies Generates plain-English explanations for flagged wallets Think: SEC-grade surveillance tooling, but for on-chain prediction markets. ⚙️ How We Built It 📊 Data Pipeline Pulled market + trade data from Polymarket Gamma + Data APIs Stored trades in PostgreSQL Deduplicated using transaction hashes Risk Tier Classification Tier Category Multiplier 1 FDA, mergers, government, military 1.5x 2 Sports, legal, macro 1.2x 3 Crypto, entertainment 1.0x 🔍 Three-Phase Fraud Detection Phase 1 — Instant Scoring Each wallet is scored based on account age, win rate percentile, avg bet size, topic concentration and speed-to-trade. Phase 2 — Enrichment Top 200 suspicious wallets selected Full trade histories fetched using blockchain data Cached in Redis (24-hour TTL) Phase 3 — ML + AI Scoring We apply Isolation Forest for anomaly detection and assign risk tiers: $$ \text{Risk Tier} = \begin{cases} \text{High} & S \geq 80 \\ \text{Medium} & 30 \leq S < 80 \\ \text{Low} & S < 30 \end{cases} $$ AI generates human-readable explanations for flagged wallets 🖥️ Frontend Built with Next.js 15 + React 19 Features: Live SSE-streamed trade feed Radar visualizations Wallet deep-dives Real-time fraud analysis runner with progress tracking ⚠️ Challenges We Ran Into API Fragmentation No unified wallet endpoint → combined multiple APIs with rate-limit handling No Ground Truth No labeled insider trading dataset → relied on signal design + unsupervised ML Non-Blocking Pipelines Needed real-time streaming + async processing → built SSE-based architecture 🏆 Accomplishments We're Proud Of Built a real-time fraud detection pipeline end-to-end Combined rule-based + ML detection effectively Delivered explainable AI outputs , not just scores Created a polished live dashboard under hackathon constraints 📚 What We Learned Fraud detection is probabilistic, not binary The hardest part is signal calibration , not model building Combining heuristics + ML significantly improves robustness Blockchain transparency is an underutilized regulatory advantage 🔮 What's Next for OmenAI Wallet Graph Analysis Detect coordinated trading rings via fund flow tracking Real-Time Alerts Email/webhook alerts for high-risk trades Backtesting Engine Validate against historical events with suspected insider activity Cross-Market Expansion Extend to Kalshi, Manifold, and more Regulatory Reporting Export structured compliance-ready reports Community Flagging Combine crowdsourced intelligence with ML detection <div