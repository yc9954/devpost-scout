---
slug: "carge"
url: "https://devpost.com/software/carge"
title: "Carge"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 1252
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/general_public"
  - "user/government_staff"
  - "user/researcher"
  - "user/small_business"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Carge

> Web3 PKI for decentralized collaboration, deploy workflows and collaborate with individual, organizations and AI through cryptography

[Devpost](https://devpost.com/software/carge) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**domain** [[finance_payments]] [[supply_logistics]]
**user** [[general_public]] [[government_staff]] [[researcher]] [[small_business]]
**substrate** [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** mcp, react, rust, substrate, tanssi

## How they structured the write-up

- 🎯 the problem
- 💡 the solution
- 📊 proven results (live data)
- 🏗️ how it works
- 💰 tokenomics & usage
- 🌐 why polkadot?
- 🚀 roadmap
- 💡 innovation
- 👤 team & project context
- 🎯 vision
- 🏆 hackathon categories
- 📊 key facts
- 🎬 demo & current status

## Body

Market Integrity Oracle - Polkadot Builder Party 2025 Decentralized oracle for real-time crypto market manipulation detection 🎯 The Problem Market manipulation steals billions from traders every day. Whales manipulate $10B+ daily volume through stop-loss hunts 50M+ traders have no defense against manipulation they can't see Exchanges need compliance tools but lack real-time detection Traditional oracles (Chainlink) provide prices, not market intelligence The gap: No decentralized oracle detects market manipulation in real-time. 💡 The Solution Market Integrity Oracle - A decentralized oracle that detects market manipulation in real-time and publishes certified, encrypted data on-chain via Ragchain (Substrate/Polkadot). What it provides: Real-time manipulation detection signals delivered through on-chain subscriptions. Data is encrypted and certified on-chain. Why it matters: For Traders: Real-time manipulation alerts Avoid manipulation traps Actionable trading signals ROI: +10-20% monthly performance For Exchanges: Market surveillance & compliance Regulatory reporting Suspicious pattern detection Revenue: 50-200k€/year (white-label) For DeFi: MEV-resistant oracle feeds Liquidation protection Fair price discovery 📊 Proven Results (Live Data) 24-hour testnet validation (ETH/SOL/LINK): ✅ 1,000+ manipulation patterns detected (real-time) ✅ 40-50 patterns per hour consistent detection rate ✅ 6-10s latency (detection to blockchain certification) ✅ High-confidence signals validated through forensic analysis ✅ Automated classification (manipulation score 0-100) 🏗️ How It Works Data Flow (6-second time block): 1. Market Data Stream → Real-time Detection ↓ 2. Manipulation Pattern Identified → Forensic Analysis ↓ 3. Data Encrypted (X25519) → Uploaded to IPFS ↓ 4. Encrypted CID → Certified On-Chain (Ragchain/Substrate) ↓ 5. Subscribers with Active Subscription → Decrypt & Use Tokenomics: On-chain subscriptions (paid in DOT/USDT via AssetHub) Subscribers pay monthly on-chain Access to encrypted CIDs published in real-time Only active subscribers can decrypt signals Technical Stack: Blockchain: Ragchain (Substrate/Tanssi appchain) Detection: Real-time market data analysis Storage: IPFS (decentralized, encrypted proofs) Encryption: X25519 + ChaCha20-Poly1305 (MEV-protected) Finality: 6 seconds (Substrate block time) Custom Substrate Pallets: pallet-pki - Decentralized PKI (subscriber keys) pallet-crypto-trail - On-chain certified, encrypted proofs pallet-rag - Subscription management & workflow metadata 💰 Tokenomics & Usage Open, Permissionless Platform Anyone can participate in two ways: 1. As a Subscriber (Consumer) Pay on-chain subscription (DOT/USDT via AssetHub) Access encrypted oracle feeds in real-time Decrypt signals with your private key Use data for trading, research, or compliance 2. As an Oracle Provider (Producer) Deploy your own manipulation detection algorithm Publish predictions on-chain via Ragchain Build reputation through accuracy Monetize your predictions with subscriptions How It Works: Oracle Providers → Detect & Publish → On-Chain (Ragchain) ↓ Encrypted Feeds ↓ Subscribers → Pay & Decrypt → Use Marketplace dynamics: Multiple oracle providers compete on accuracy Subscribers choose best providers Transparent on-chain performance metrics Decentralized, no gatekeepers Pricing Examples (Indicative): Basic subscription: 50-100€/month (1-3 symbols) Professional: 200-300€/month (multi-symbol, API access) Enterprise/White-label: Custom pricing for exchanges The goal: Create a decentralized marketplace for market integrity data where anyone can contribute and benefit. 🌐 Why Polkadot? Ragchain is built on Substrate, deployed as Tanssi appchain. Advantages: ✅ Shared Security - Polkadot's $7B+ economic security ✅ Interoperability - XCM for cross-chain oracle queries ✅ Scalability - Tanssi handles block production ✅ Customization - Full control over consensus & economics ✅ Ecosystem - Polkadot.js, AssetHub, IPFS gateways Integration Points: AssetHub - Subscription payments (DOT/USDT) XCM - Cross-parachain oracle queries Polkadot Cloud - Infrastructure for 24/7 operation 🚀 Roadmap Phase 1: MVP ✅ (Completed) Forensic bot with 1s precision 77 patterns detected (live) Classification algorithm (manipulation score) Ragchain pallets deployed (testnet) Phase 2: Integration (2-3 weeks) Python → Substrate publisher IPFS + encryption layer 10 beta testers (free) Phase 3: Launch (1-2 months) Open beta for subscribers Onboard first oracle providers (competition) Website + API + documentation Community building (Discord/Telegram) Phase 4: Marketplace (3-6 months) Multiple oracle providers competing Reputation system (on-chain metrics) 15+ symbols coverage White-label integrations (exchanges) 💡 Innovation For Polkadot Ecosystem: ✅ New Oracle Category - First "Market Integrity Oracle" on Polkadot ✅ Open & Permissionless - Anyone can be a provider or subscriber ✅ On-Chain Subscriptions - Native tokenomics via AssetHub ✅ Privacy-First - Encrypted data, MEV-protected ✅ Decentralized Marketplace - Competition drives quality Real-World Use Cases: For Traders: Real-time manipulation alerts Avoid stop-loss hunts Profitable trading signals For Exchanges: Market surveillance Compliance & regulatory reporting User protection tools For Researchers: Market microstructure analysis Manipulation pattern studies Algorithm development & testing For Other Oracle Providers: Deploy competing algorithms Build reputation on-chain Monetize predictions directly 👤 Team & Project Context Jean-François Meneust 5+ years blockchain development Creator of Carge.fr (Substrate supply chain platform - operational on testnet) Former military officer (logistics coordination) Solo founder (AI-augmented with Claude/Cursor) Project Evolution: Initial Hackathon Submission (Supply Chain): Built Carge.fr: AI-powered supply chain transparency on Polkadot/Substrate Use case: Anti-counterfeiting for luxury goods (wines, automotive parts, etc.) 3 custom pallets deployed: PKI, CryptoTrail, RAG Working product with QR code verification and encrypted workflows Problem discovered: Hard to find first customers (luxury brands slow to adopt) Pivot Decision (5 days before deadline): Why pivot: Supply chain solves a real problem but requires long sales cycles New opportunity: Market manipulation affects 50M+ crypto traders daily (instant market) Key insight: Same blockchain infrastructure works perfectly for encrypted oracle feeds Risk: Could reuse proven pallets, only needed to build detection algorithms Current Submission (Market Integrity Oracle): Leverages same Ragchain infrastructure (3 pallets tested 2+ months) Built Python detection algorithms and validated with live data (1000+ patterns) Faster go-to-market: traders need this NOW vs luxury brands need education Shows platform versatility: 2 completely different use cases on same blockchain Why this pivot demonstrates value: This isn't abandoning work—it's proving the infrastructure is reusable. Building one blockchain platform that supports multiple real-world applications (supply chain + market integrity) is more valuable than solving just one problem. Contact: Email: contact@carge.fr GitHub: github.com/polykrate Website: carge.fr Polkadot: 5C4kKzKyDuZTu3Qa89soZWdRfFRJzvTjVVDTNqAKPuzXcaRa 🎯 Vision Create the first decentralized marketplace for market integrity data A permissionless platform where: Anyone can deploy manipulation detection algorithms Everyone can subscribe to trusted oracle feeds All data is cryptographically certified on-chain Competition drives accuracy and innovation Long-term impact: Democratize access to market intelligence Level the playing field (retail vs institutions) Make manipulation economically unviable Prove that decentralized surveillance works 🏆 Hackathon Categories Primary: Real-World Applications Trader protection against manipulation Exchange compliance tools Transparent, fair markets Secondary: Infrastructure & Tools Novel oracle type (forensic intelligence) Privacy-preserving feeds (X25519) Substrate pallet innovation 📊 Key Facts Metric Value Detection latency 6-10s (real-time) Patterns detected 1,000+ (24h validation) Detection rate 40-50 patterns/hour Database SQLite (forensic analysis) Testnet uptime 2+ months (Ragchain/Tanssi) Custom pallets 3 (PKI, CryptoTrail, RAG) Platform Permissionless (anyone can join) 🎬 Demo & Current Status Live Detection System (Backend): Real-time bot with proven detection rate (40-50 patterns/hour) Database: forensic_reports.db (SQLite with 1000+ patterns) Blockchain: Ragchain testnet (Tanssi appchain) - operational Python detection scripts validated with live market data Infrastructure (Ready): Website: carge.fr (existing Substrate platform with PKI, CryptoTrail, RAG pallets) 3 custom pallets deployed and tested for 2+ months On-chain subscription system architecture designed Current Development Phase: ✅ Detection algorithms (Python scripts) - validation in progress ✅ Pattern classification system - operational 🔄 Algorithm optimization with 24h+ live data 📋 Next: Dedicated marketplace website + subscription integration Documentation: README.md - Full technical & business details QUICK_START.md - Run the detection bot SQL_DATABASE_GUIDE.md - Data schema & queries Validation Results: 24-hour continuous operation test completed Consistent performance across ETH, SOL, LINK pairs Automated classification with forensic analysis Why this staged approach: Building robust detection first, then marketplace. Quality signals = successful marketplace. Built for Polkadot Builder Party 2025 Code is law. Let's build transparent markets together. Submission Deadline: November 17, 2025 ⚡ <div