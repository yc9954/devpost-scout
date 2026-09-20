---
slug: "cloud-climate-chain"
url: "https://devpost.com/software/cloud-climate-chain"
title: "Cloud, Climate, Chain"
hackathon: "Dev Season of Code "
organization: "DSOC Official"
winner: true
words: 1072
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/government_staff"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Cloud, Climate, Chain

> Carbon footprint management platform that combines Cloud Computing, Climate Analysis, and Blockchain Technology to provide a comprehensive solution for monitoring and certifying environmental impact.

[Devpost](https://devpost.com/software/cloud-climate-chain) · hackathon [[Dev Season of Code]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[climate_energy]] [[finance_payments]] [[labor_employment]]
**user** [[government_staff]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** blockchain, carbon-calculated, typescript

## How they structured the write-up

- the carbon crisis in indonesian smes
- rantai 3c — cloud • climate • chain
- ☁️ cloud — data infrastructure
- 🌍 climate — ai-powered analysis
- ⛓️ chain — blockchain certification
- 🌱 carbon offset marketplace
- 🎮 gamification & engagement
- tech stack
- architecture approach
- development journey
- technical
- market
- phase 1 — mainnet launch (q2 2025)
- phase 2 — real api integrations (q3 2025)
- phase 3 — advanced features (q4 2025)
- phase 4 — scale & impact (2026)

## Body

Inspiration The Carbon Crisis in Indonesian SMEs Indonesia is the world’s 8th largest carbon emitter , yet most Small and Medium Enterprises (SMEs) lack access to affordable and transparent carbon management tools. Through direct observation, we saw how Indonesian businesses struggle with: High costs : Enterprise carbon tracking solutions cost $10,000–$50,000 per year , far beyond SME budgets Lack of transparency : Traditional carbon tracking relies on opaque third-party auditors No verifiable proof : Companies cannot credibly prove sustainability claims to stakeholders or regulators Complex processes : Existing tools require technical expertise most SMEs do not have We realized that three powerful technologies — Cloud, Climate AI, and Blockchain — could solve this problem if integrated correctly . Thus, RANTAI 3C was born: A blockchain-verified carbon management platform , purpose-built for the Indonesian market to make sustainability accessible, transparent, and affordable . What It Does RANTAI 3C — Cloud • Climate • Chain RANTAI 3C is a comprehensive carbon footprint management platform built on three core pillars: ☁️ CLOUD — Data Infrastructure Multi-source data import Upload energy consumption data via CSV/JSON or connect cloud storage (Google Drive, Dropbox, OneDrive) Automated data pulling Simulated real-time data fetching from cloud providers Data validation system Quality scoring (0–100) with detailed error detection and improvement recommendations Template downloads Pre-formatted CSV/JSON templates with Indonesian sample data 🌍 CLIMATE — AI-Powered Analysis Carbon footprint calculation Converts energy consumption (kWh) into CO₂ emissions using industry-standard emission factors 4 types of AI insights Pattern analysis Efficiency optimization Predictive analytics Industry benchmarking Interactive visualizations Bar charts, pie charts, and line graphs with drill-down capabilities Historical tracking Monitor carbon trends and performance over time Smart recommendations Actionable carbon reduction strategies prioritized by impact Professional exports Generate reports in PDF, CSV, Excel, or JSON ⛓️ CHAIN — Blockchain Certification SIWE authentication Secure Sign-In With Ethereum (wallet-based identity) 5 smart contracts deployed on Ethereum Sepolia Carbon Records – Immutable carbon data storage NFT Certificates (ERC-721) – Blockchain-verified sustainability achievements Carbon Credits (ERC-20) – Tokenized carbon credits (1 token = 1 kg CO₂) DAO Governance – Community voting on offset projects Oracle Integration – Real-time carbon credit pricing IPFS storage Decentralized storage for carbon data and NFT metadata via Pinata View-only mode Educational blockchain access without wallet connection Downloadable certificates JSON-based certificates for compliance and audits 🌱 Carbon Offset Marketplace 4 verified Indonesian offset projects Reforestation Solar Energy Mangrove Restoration Carbon Capture Flexible offset amounts Purchase from 0.01 to 1,000 tons CO₂ Dual payment system 💰 Crypto payments : ETH via MetaMask (fully decentralized) 💳 Fiat payments : PayPal for non-crypto users Automatic NFT rewards Each offset purchase mints a blockchain-verified NFT certificate with instant notification Net-zero tracking Visual progress toward carbon neutrality Dynamic pricing $12–$25 per ton CO₂ with live Oracle updates Impact metrics Transparent environmental benefits per project 🎮 Gamification & Engagement Achievement system NFT badges for sustainability milestones Sustainability levels Environmental Explorer → Carbon Conscious → Eco Champion Progress goals Visual tracking of emission reduction achievements Social sharing Share achievements to inspire others How We Built It Tech Stack Frontend Next.js 15.3.8 (App Router) — Modern React framework with SSR TypeScript (Strict Mode) — Type-safe development Tailwind CSS v4 — Utility-first styling shadcn/ui — Accessible components (Radix UI) Recharts — Interactive data visualization Blockchain & Web3 ethers.js v6 — Wallet & smart contract interaction Ethereum Sepolia Testnet 5 Solidity Smart Contracts Carbon Records NFT Certificates (ERC-721) Carbon Credit Tokens (ERC-20) DAO Governance Carbon Offset Payment (dual payment handler) IPFS + Pinata — Decentralized storage Chainlink-style Oracle — Real-time carbon pricing Payment Integration MetaMask — ETH payments PayPal REST API — Fiat payments Data Processing PapaParse — CSV parsing jsPDF — PDF report generation SheetJS (xlsx) — Excel export Architecture Approach Storage Layer Browser LocalStorage (fast access) IPFS (permanent, decentralized) Ethereum blockchain (immutable proof) Business Logic Layer React UI components Custom Web3 hooks AI carbon calculation engine Integration Layer API proxy routes Cloud provider OAuth 2.0 flows Payment gateway integrations Development Journey Week 1 : Core calculator, data upload, basic visualization Week 2 : Blockchain integration, smart contracts, IPFS Week 3 : AI insights, advanced charts, historical tracking Week 4 : Offset marketplace, dual payments, NFT rewards, DAO Challenges & Solutions 1. Dual Payment Integration Challenge: Unifying decentralized crypto and centralized PayPal payments Solution: Smart contract accepts on-chain ETH and records PayPal payments via trusted admin; unified PaymentModal UX 2. IPFS Reliability Challenge: Upload failures due to network and file limits Solution: Retry logic, compression, fallback storage, user-friendly error handling 3. Gas Optimization Challenge: High gas usage Solution: Optimized data structures, batched operations, IPFS-first storage 4. Real-Time CSV Processing Challenge: UI freezing on large files Solution: Web workers, progress indicators, O(n) optimization 5. Blockchain Education Challenge: SME unfamiliarity with Web3 Solution: View-only mode, tooltips, educational content, Indonesian language support 6. NFT Metadata Standards Challenge: Marketplace compatibility Solution: ERC-721 compliant metadata tested on OpenSea Testnet Accomplishments We’re Proud Of ✅ First blockchain-verified carbon platform for Indonesian SMEs ✅ 5 deployed smart contracts on Sepolia ✅ Dual crypto + fiat payment system ✅ Professional compliance-ready PDF reports ✅ IPFS-based decentralized storage ✅ AI-powered actionable insights ✅ Gamified sustainability with NFT badges ✅ Zero backend dependency ✅ Fully responsive design ✅ Open-source educational documentation What We Learned Technical Blockchain UX must focus on value, not jargon IPFS needs robust fallbacks Gas efficiency changes design thinking Dual payments increase adoption TypeScript strict mode prevents production failures Market Indonesian SMEs need simplicity Transparency builds trust Gamification boosts engagement Education is critical for Web3 adoption What’s Next for RANTAI 3C Phase 1 — Mainnet Launch (Q2 2025) Deploy on Base Smart contract audit Product Hunt launch Onboard 100 SMEs Phase 2 — Real API Integrations (Q3 2025) AWS, GCP, Azure integrations Automated real-time data PostgreSQL user management Team-based access control Phase 3 — Advanced Features (Q4 2025) Predictive ML forecasting Mobile app (React Native) Carbon credit trading marketplace Indonesian regulatory templates Public API Phase 4 — Scale & Impact (2026) Southeast Asia expansion Ministry of Environment partnership Public transparency dashboard B2B SaaS pricing ($50–$500/month) Carbon Credit DAO governance Long-Term Vision Make RANTAI 3C the de facto carbon management standard for Southeast Asian SMEs , helping the region meet its Paris Agreement commitments through transparent, blockchain-verified sustainability. 🌍 Mission: Empower every business to take climate action ⛓️ Approach: Web3 + practical business needs 🚀 Goal: 10,000 Indonesian SMEs reducing carbon by 2026 Built with ❤️ for a sustainable future <div