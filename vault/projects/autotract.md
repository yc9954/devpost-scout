---
slug: "autotract"
url: "https://devpost.com/software/autotract"
title: "Pact"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 709
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "user/general_public"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Pact

> Expediting the contracts and document signings process between vendors and clients by bringing clarity, transparency, and accountability.

[Devpost](https://devpost.com/software/autotract) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[deterministic_policy]] [[provenance_signing]] [[realtime_stream]] [[vision_ocr]]
**domain** [[finance_payments]] [[legal_justice]]
**user** [[general_public]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** anchor, gemini, node.js, react, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pact

## Body

Dashboard Creating Contract Approving Changes Approving Payments Inspiration Companies are taking a long time to communicate a partnership agreement, causing companies to struggle to keep up with rising clients. With slow response times, little transparency, and lengthy processing time, projects are slowly implemented. Clients feel they are forgotten when they are not reached out by the vendor, causing clients to spend excessive time in alternative solutions. Clients deserve to understand exactly what they are paying for, the objective of the projects, and the changes every contract will enable. What it does Pact is a comprehensive blockchain-powered contract management system that revolutionizes how organizations create, collaborate on, and enforce legal agreements. The platform enables users to draft contracts with AI assistance, manage multi-party approvals through transparent workflows, and anchor finalized agreements on the Solana blockchain for immutable proof of authenticity. With integrated version control similar to Git. Organizations can invite members with role-based permissions and track payment milestones tied to contract deliverables. The dashboard provides real-time visibility into active contracts, pending approvals, task management with calendar integration, and reputation leaderboards. How we built it Pact runs on three Solana programs written in Rust with Anchor. Each deal, reputation profile, and escrow vault is a separate Program Derived Address. Deal PDAs track parties, milestones, approval states, and contract hashes. Reputation PDAs store dual scores (vendor and client performance) that update via Cross-Program Invocations after deal completion. Escrow vaults are PDA-controlled token accounts that release funds programmatically when milestone approval thresholds are met through multi-signature verification. The frontend is Next.js with TypeScript, using Solana web3.js and Anchor client libraries for program interaction. Contract documents and deliverables store on IPFS with only content hashes written on-chain for verification. AI integration through Gemini API extracts security requirements from contracts, validates compliance documents, and computes fraud risk scores based on wallet age, transaction history, and behavioral patterns. Reputation scoring uses weighted algorithms that factor completion rates, delivery speed, payment timeliness, and dispute history. Recent performance weighs more heavily through exponential decay functions. Fraud detection combines on-chain signals (wallet age, transaction count) with off-chain verification (email, business registry) to generate risk scores from zero to one hundred. Scores above seventy trigger enhanced due diligence or block deal creation entirely. Challenges we ran into Integrating Solana blockchain authentication and contract verification proved to be one of the most time-intensive challenges in building Pact. The Solana development ecosystem required mastering an entirely new technology stack including the Anchor framework for Rust-based smart contracts and understanding Solana's account model. The authentication flow alone required coordinating between the frontend wallet connection, backend verification of wallet signatures, and on-chain program calls to register contract hashes. We spent considerable time optimizing transaction construction to minimize fees while ensuring reliability, implementing retry logic for failed transactions, and building fallback mechanisms when users didn't have SOL for transaction fees. Accomplishments that we're proud of We are proud of building a B2B platform that companies can use to efficiently highlight contract essentials, expediting clients to decide, make edits, and ultimately approve business proposals. Along with the beautiful front-end dashboard, users are able to focus their attention on important tasks while AI helps expedite the tedious contract review process. We successfully integrated blockchain verification on Solana for immutable proof of authenticity, implemented decentralized IPFS storage for permanent contract accessibility. The platform combines the best of traditional web app usability with Web3 guarantees, creating a trustworthy environment where every contract change is tracked, every approval is transparent, and every finalized agreement is cryptographically verifiable. What we learned We learned to use blockchain as an alternative form of authentication for contracts and transactions. With a platform that is decentralized and greater transparency while increasing the accountability of any changes made to the contract to stand out. We learned to implement Solana's account model and Program Derived Addresses (PDAs) for deterministic, trustless contract verification—a fundamentally different approach from centralized authentication systems. The process taught us how cryptographic hashing creates immutable proof of document authenticity, and how decentralized storage on IPFS ensures permanent accessibility independent of any single server. What's next for Pact Implement realistic consumer usage tools - PDF OCR readers to upload contracts. Escrow/fund transfers (Phase 3) Reputation system (Phase 2) IPFS content storage Complex approval logic <div