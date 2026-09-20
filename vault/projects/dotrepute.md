---
slug: "dotrepute"
url: "https://devpost.com/software/dotrepute"
title: "DotRepute"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 607
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/scientific_research"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# DotRepute

> DotRepute — Your On-Chain Reputation, Verified by Polkadot.

[Devpost](https://devpost.com/software/dotrepute) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[benchmark_measured]] [[cross_origin_web]] [[deterministic_policy]] [[realtime_stream]]
**domain** [[developer_tools]] [[scientific_research]]
  <sub>weak: civic_government</sub>
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]]

**stack** chatgpt, conviction, express.js, figma, framer-motion, github, identity, luno-kit-wallet, luno-kit/react, luno-kit/ui, next.js-14, node.js, opengov, polkadot/api

## How they structured the write-up

- vision & opportunity
- platform overview
- key capabilities
- technical architecture
- workflow
- ecosystem impact
- progress & achievements
- roadmap
- deployment guide
- leadership team

## Body

DotRepute - Blockchain-Powered Contributor Reputation System Architecture DotRepute - Blockchain-Powered Contributor Reputation Flow Chart Final DotRepute - Interface Final DotRepute - Wallet Integration Final DotRepute - Perfect Chatbot Final DotRepute - Output DotRepute — A Unified Reputation Layer for the Polkadot Ecosystem Rust-First. Verifiable. Ecosystem-Ready. Vision & Opportunity Polkadot continues to grow as one of the most diverse and interconnected ecosystems in Web3. Yet, a unified, verifiable framework to assess contributor trust, engagement, and impact across parachains and domains remains absent. DotRepute introduces a standardized, on-chain-compatible reputation layer built on Polkadot primitives. Powered by Rust/WASM computation and verifiable analytics, it forms the foundation for transparent contributor evaluation across grants, governance, and community operations. By quantifying participation consistently, DotRepute strengthens ecosystem trust, enhances onboarding, and streamlines decisions for ecosystem teams, technical leads, and governance bodies. Platform Overview DotRepute generates a portable Contributor Reputation Score (CRS) through weighted aggregation of multi-source signals. Core Components: Polkadot-Native Data Integration: Leverages on-chain data from Identity, Governance, Staking, and Extrinsics across core pallets and parachains. Rust/WASM Scoring Engine: Deterministic, modular computation for reproducible and auditable scoring logic. On-Chain Verification (Optional): ink! smart contract anchors CRS proofs for tamper-resistant validation. Analytics Dashboard: Built with Next.js and PolkadotJS for granular factor visualization and identity-level insights. API & Indexing Layer: SubQuery-based indexing with GraphQL endpoints for external integrations, analytics tools, and dev-focused applications. Key Capabilities Rust-First Architecture: Native to Polkadot’s engineering culture and optimized for performance, transparency, and modularity. Multi-Signal Mapping: Consolidates governance activity, identity attributes, staking patterns, and extrinsics behavior into verifiable CRS metrics. Bias-Resistant Normalization: Calibrates models to avoid weight distortion from stake size, vote farming, or identity spam. Verifiable Proofs: CRS can optionally be anchored on-chain for independent auditability. Deployment Flexibility: Dockerized services, CI/CD pipelines, and WASM builds for seamless execution across environments. Technical Architecture Rust → WASM Scoring Engine: Deterministic module for CRS computation. SubQuery Indexer: Aggregates live and historical data streams from Polkadot core pallets. ink! Verification Layer: Smart contract for anchoring CRS commitments. Frontend Dashboard: Real-time visualization via Next.js and PolkadotJS. Developer Workflow: Dockerized environment, GitHub Actions-based CI, WASM builds for both backend and client-side execution. Workflow 1. Aggregate Identity, Governance, Staking, and Extrinsics data 2. Normalize and index data using SubQuery 3. Compute CRS via Rust/WASM scoring engine 4. (Optional) Publish CRS commitment via ink! contract 5. Display CRS breakdown and metadata on Dashboard 6. Expose CRS via API to external dApps or governance portals Ecosystem Impact DotRepute establishes a trust primitive that can serve every layer of the Polkadot ecosystem: Transparent contributor evaluations for grants and governance. Streamlined onboarding for ecosystem partners and DevRel teams. Cross-parachain consistency for identity and participation metrics. Verifiable benchmarks supporting DAOs, community programs, and reputation-driven applications. Progress & Achievements Implemented Rust-based scoring engine with WASM exports. Integrated Identity, Governance, and Staking aggregation pipeline. Prototyped ink! contract for CRS anchoring. Delivered dashboard for evaluator and onboarding workflows. Exposed documented, GraphQL-based API for partner integrations. Roadmap Cross-parachain data aggregation (Moonbeam, Astar, HydraDX). Verifiable Credentials / Reputation NFTs. Validator and developer analytics modules. Browser extension for in-dApp CRS visibility. Partner integrations: Astar Network, Bifrost, Polkadot Africa. Deployment Guide git clone https://github.com/your-org/dotrepute cd dotrepute # Frontend npm install && npm run dev # Scoring Engine cargo build --release # Indexer subql codegen && subql build && subql start # Optional ink! Deployment cargo contract build && cargo contract upload Leadership Team Aditya — Product & Engineering Lead Architecture design, UI/UX strategy, backend integration, PolkadotJS API. Steven Muanigo — Technical Lead & Rust Architect Rust computation engine, infrastructure, WASM pipelines. Dustin (OpenGuild) — Wallet Integration & DevRel Support End-to-end wallet connectivity via Luno Kit and integration tooling. <div