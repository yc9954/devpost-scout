---
slug: "nani-65mnxo"
url: "https://devpost.com/software/nani-65mnxo"
title: "Nani"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 932
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/transportation"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Nani

> Nani: event monitoring and notification service using PAPI

[Devpost](https://devpost.com/software/nani-65mnxo) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]] [[labor_employment]] [[transportation]]
**user** [[developer]]
**substrate** [[structured_db]] [[web_dom]]

**stack** acebasedb, jwt, papi, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nani

## Body

nani: event monitoring and notification infrastructure using PAPI Inspiration From my experience integrating blockchains and smart contracts, I noticed a critical gap: event monitoring infrastructure is not ergonomic for developers and notification is abscent for users. Every dApp needs real-time notifications (wallet alerts, governance updates, staking rewards), but developers face an impossible choice: Pay $10K+/year for closed-source SaaS (Notifi, Alchemy Notify) Spend 1-3 months building custom infrastructure ($10K-$30K cost) Accept limitations of free tools with no API access Totally ignore the notification feature I built Nani to democratize this infrastructure—making enterprise-grade event monitoring and notification free, open-source, and infinitely extensible through a plugin system. What it does Nani is a multi-tenant event monitoring and notification service built on Polkadot API (PAPI). It listens to real-time events from multiple Polkadot chains, filters them per user, logs them securely with AES-256 encryption, and dispatches instant notifications through pluggable channels like SMS, Discord, and email. Core Workflow : Connect : PAPI establishes WebSocket to Westend/Kusama/Polkadot RPC Subscribe : Single system.events subscription captures all on-chain events Distribute : Each event is checked against all tenant configurations (100K+ tenants/node) Filter : Activity plugins (transfers, staking, governance) determine relevance Log : Matched events are encrypted and stored per tenant Notify : Parallel dispatch to configured channels (SMS, Discord, Email) Aggregate : Real-time stats computed from encrypted logs API : RESTful endpoints exposed to client applications Key Features : ⚡ <100ms latency from block finalization to notification 🔌 Plugin system - Add Telegram/Slack/Webhook in 20 lines (no recompilation) 🏠 Self-hosted - Deploy on Railway, Docker, AWS, or bare metal 🔐 Bank-grade security - AES-256-GCM encryption + JWT auth 📊 Real-time analytics - Export logs as CSV/JSON/ZIP 🌐 Multi-chain - Westend, Asset Hub, Kusama, Polkadot (50+ chains planned) How we built it Tech Stack : Runtime : Node.js 20+ with clustering for multi-core scalability Blockchain SDK : Polkadot API (PAPI) v10.11.1+ with auto-failover across multiple RPC endpoints Language : TypeScript for type safety and maintainability API Framework : Express.js with Swagger UI for interactive documentation Storage(AceBaseDB) : Embedded realtime database with AES-256-GCM encryption Authentication : JWT tokens with rate limiting (10 req/min per tenant) Notifications : Twilio (SMS), Discord webhooks, SMTP (Email) Architecture Highlights : Multi-process clustering - Each CPU core runs a worker process monitoring different chains PAPI auto-failover - If one RPC endpoint fails, it automatically switches to backups Plugin hot-reload - Drop TypeScript files in src/plugins/ folder, they load instantly Encrypted multi-tenancy - Each tenant has isolated, encrypted storage (data/{tenantId}/) Async processing - Non-blocking notification dispatch using Promise.all ** Development Workflow**: # 1. Clone & install git clone https://github.com/cenwadike/nani npm install # 2. Configure (minimum: JWT_SECRET, ENCRYPTION_KEY, RPC URLs) cp .env.example .env # 3. Run the development server with hot reload npm run dev:cluster # 4. Test via Swagger UI or cURL curl http://localhost:3000/health { "status": "ok", "timestamp": "2025-11-11T16:01:40.360Z", "papi": { "westend": "connected", "asset-hub-westend": "connected" }, "stats": { "activeTenants": 0, "eventsProcessed24h": 0, "notificationsSent24h": 0, "uptimeHours": 0.02 }, "system": { "memoryUsageMB": 86, "cpuPercent": 37.2 } } Challenges we ran into Understanding and handling Polkadot's complex event structure - PAPI returns deeply nested objects with codec types. Solution: Built a recursive decoder utility that extracts human-readable data. Multi-tenant scalability at 100K+ users - Initially used a single-threaded architecture (crashed at 5K tenants). Solution: Implemented Node.js clustering with worker processes per chain. Ensuring plugin isolation and fault tolerance - One buggy plugin could crash the entire system. Solution: Wrapped plugin execution in try-catch, added timeout limits (5s per notification). Managing tenant-specific configurations securely - Storing plaintext config exposed API keys. Solution: AES-256-GCM encryption for all tenant data with unique initialization vectors. RPC endpoint reliability - Single RPC connection had 99.5% uptime (unacceptable). Solution: PAPI's multi-endpoint failover increased uptime to 99.9%+. Notification delivery failures - Discord/Twilio APIs occasionally timeout. Solution: Retry logic with exponential backoff (3 retries over 30 seconds). Accomplishments that we're proud of 📊 Production-ready performance (16GB RAM, 8-core CPU) : 100,000+ tenants per node 3,000+ notifications/sec <100ms latency for most events 🏆 Technical achievements : 12 built-in plugins (activities, notifications, stats) 4 chains supported (Westend, Asset Hub, Kusama, Polkadot) Swagger UI for interactive API documentation 💡 Innovation : First open-source, plugin-based notification platform for Polkadot PAPI-native architecture demonstrates Polkadot Cloud principles Zero vendor lock-in - fork, extend, commercialize freely (MIT license) 🌍 Real-world impact : Developers save $50K+ by avoiding custom builds 2,000+ Polkadot dApps need this infrastructure Community-owned (open-source) vs. centralized SaaS What we learned Clustering is essential for scaling Node.js apps - Single-threaded architecture maxes out at 10K tenants. Clustering enables 100K+. Plugin architecture makes the system extensible and maintainable - Core logic stays clean, new features added without touching core. Event filtering must be precise to avoid noisy logs and false alerts - Initially logged all events (100GB/day). Smart filtering reduced storage by 95%. PAPI's multi-endpoint design is brilliant - Auto-failover from dead RPC to a healthy one in <5 seconds (no downtime). Developer experience matters - Swagger UI + comprehensive README reduced onboarding from 4 hours to 15 minutes. Security cannot be an afterthought - AES-256 encryption, JWT auth, and rate limiting built from day one. What's next for NANI Phase 2: Enhanced Features (Next 3 months) ✅ Telegram bot integration ✅ Generic webhook plugin (HTTP POST to any URL) ✅ Advanced stats plugin (PnL calculations, yield tracking) ✅ Mobile SDKs (React Native for iOS/Android) ✅ Plugin marketplace (community-contributed plugins) Phase 3: Ecosystem Expansion (6-12 months) 🌍 Support all 50+ Polkadot parachains 🤖 Smart contract events (WASM, EVM) ⛓️ Multi-chain adapters (Ethereum, Solana, Cosmos) 🏛️ DAO governance for public instances AI analytic plugins <div