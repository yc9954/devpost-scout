---
slug: "green-credit-a0p2uh"
url: "https://devpost.com/software/green-credit-a0p2uh"
title: "Green Credit - A Decentralized Climate Action System"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 492
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Green Credit - A Decentralized Climate Action System

> A Web3 platform that monetizes climate-positive actions using verifiable on-chain proofs, GCT rewards, and a transparent, trust-less incentive system powered by Moonbeam.

[Devpost](https://devpost.com/software/green-credit-a0p2uh) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[civic_government]] [[climate_energy]] [[developer_tools]] [[education]] [[finance_payments]]
**substrate** [[document_pdf]] [[financial_record]] [[video_visual]]

**stack** express.js, github-jobs, hardhat, ipfs, javascript, moonbase, moonbeam, openzeppelin, react, snapshot, solidity, tailwind

## How they structured the write-up

- inspiration
- what it does
- 🏗️ how i built it
- challenges i ran into
- accomplishments i'm proud of
- what i learned
- what’s next for green credits

## Body

Landing Page Landing Page v2 🌿 Green Credit Inspiration The global carbon credit market is broken—opaque, expensive, and prone to fraud. Traditional carbon offset systems rely on centralized verification processes that are slow, costly, and inaccessible to individuals. Meanwhile, millions of people perform climate-positive actions every day—planting trees, recycling, conserving energy—yet none of these actions are recognized or rewarded. Green Credits was created to fix this gap by bringing transparency, fairness, and tokenized incentives to climate-positive behavior through decentralized verification and programmable rewards. What it does Green Credits is a decentralized climate-action system that rewards real-world environmental actions. Users can: Submit environmental actions (tree planting, recycling, cleanups, etc.) Upload proof (images, videos, documents) Have submissions verified on-chain Stake USDC and earn GCT tokens as rewards Track personal environmental impact The platform provides: Decentralized verification using smart contracts Stablecoin-based staking and rewards On-chain transparency for all contributions A public leaderboard A registry of verified climate actions 🏗️ How I built it Smart Contracts (Moonbeam Alpha) EcoActionVerifier.sol for submissions, verification, and rewards USDC mock contract for staking GCT token contract for protocol rewards Hardhat (CommonJS) for tests & compilation Deployment scripts for Moonbeam Alpha automation Backend (Render) Node.js + Express API IPFS upload pipelines Webhooks for event indexing REST endpoints for frontend consumption Frontend (Vite + React + Tailwind) Clean, responsive UI (Dashboard, Actions, Leaderboard, Rewards) Wallet connection (EVM & Polkadot compatible) Real-time transaction notifications & state updates CI/CD (GitHub Actions + Docker) Linting & tests Contract deployment Backend deploy → Render Frontend deploy → GitHub Pages Containerized services Auto-deploy on push to main Challenges I ran into Handling decimal mismatches between USDC (6 decimals) and GCT (18 decimals) BigInt issues in Chai tests (Hardhat + Ethers v6) Hardhat incompatibility with ESM → forced migration to CJS Multi-service monorepo deployment with GitHub CI + Render Reactive UI state syncing with blockchain transactions Reliable IPFS uploads under slow network conditions DNS propagation delays for global deployment Accomplishments I'm proud of A complete decentralized climate action system Stablecoin staking integrated with on-chain verification Clean monorepo architecture Dockerized backend + frontend + blockchain Automated CI/CD pipelines Production-ready deployment flows Smooth and responsive UI/UX Scalable system that can support millions of submissions What I learned How to design on-chain carbon-credit verification mechanisms Moonbeam EVM specifics and best practices Distinguishing between off-chain vs on-chain validation Optimizing IPFS pipelines for real-world uploads Best practices for decentralized identity & proofs Improving Web3 UX with React + event syncing Designing CI/CD for complex monorepos Stablecoin-based tokenomics & reward mechanisms What’s next for Green Credits Production Deployment (Moonbeam Mainnet) Move from Moonbeam Alpha → Mainnet Integrate official Moonbeam USDC contract DAO Governance Snapshot.org + Gnosis Safe Community-driven approval of new climate actions Oracles & Verification Chainlink identity verification Geolocation oracles Community verifiers (Web of Trust model) Expanding Rewards Carbon offset NFTs Sustainable brand partnerships GCT marketplace Mobile App QR-based validation Offline-first submissions Enterprise Integrations Partnerships with schools, governments, NGOs Corporate sustainability dashboards <div