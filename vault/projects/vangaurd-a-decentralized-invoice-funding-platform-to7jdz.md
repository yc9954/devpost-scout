---
slug: "vangaurd-a-decentralized-invoice-funding-platform-to7jdz"
url: "https://devpost.com/software/vangaurd-a-decentralized-invoice-funding-platform-to7jdz"
title: "VanGaurd - A decentralized invoice funding platform"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 482
team_size: 6
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# VanGaurd - A decentralized invoice funding platform

> Transforming unpaid invoices into instant liquidity. Secure, NFT-backed debt on Shardeum,Arweave. Bridging the $2.5T SME credit gap with MNC-verified trust and RWA yields. Real-time funding for all.

[Devpost](https://devpost.com/software/vangaurd-a-decentralized-invoice-funding-platform-to7jdz) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[vision_ocr]]
**domain** [[finance_payments]] [[legal_justice]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** arweave, blockchain, ethers.js, finance, metamask, openzeppelin, sherdeum, solidity, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vangaurd

## Body

VanGaurd: A Decentralized Invoice Funding Platform Inspiration The inspiration for VanGaurd came from a staggering reality: a $2.5 Trillion global financing gap that leaves millions of SMEs struggling for survival. While traditional banks take 90 days to process paper-based invoices, we saw an "Aha!" moment in the intersection of Shardeum’s scalability and Arweave’s permanence. We set out to build a bridge where a piece of unpaid paper becomes a liquid, NFT-backed asset , empowering the "backbone of the economy" with instant cash flow. What it does VanGaurd is a triple-portal decentralized ecosystem that digitizes debt: For SMEs: A platform to anchor invoices to Arweave and mint Verified Debt NFTs for immediate funding. For MNCs: Secure, human-readable EIP-712 signing to verify debt obligations on-chain. For Investors: A marketplace for Real-World Asset (RWA) yields, where they can fund invoices and earn interest. The Math Interest is calculated via our weighted formula: $$SI = \frac{P \times N \times R}{100}$$ Financial Stability It utilizes a 4-stage USDC flow to eliminate SHM/ETH price volatility during the funding cycle. How we built it Built entirely from scratch, VanGaurd utilizes a sophisticated Web3 stack: Smart Contracts: Developed in Solidity , featuring an on-chain ecrecover validation system that matches MNC signatures against authorized public keys. Storage: Integrated Arweave for immutable document anchoring, ensuring that the legal proof of debt can never be altered or lost. Frontend: A Next.js and Tailwind CSS application with three distinct role-based dashboards. Network: Deployed on Shardeum Atomium , leveraging dynamic state sharding to keep transaction costs at a fraction of a cent. Challenges we ran into The primary challenge was ensuring Signature Integrity . We moved beyond simple hex-string signing to implement EIP-712 , allowing MNCs to see exactly what they are signing in plain text—essential for corporate trust. Additionally, building a mathematical model for Time-Weighted Interest ((N)) required meticulous testing to ensure that early investors were rewarded fairly without breaking the contract's solvency. Accomplishments that we're proud of On-Chain Verification: Successfully implementing a zero-trust model where an SME cannot mint a debt NFT unless the MNC’s signature is verified by the smart contract. Lean Architecture: Replacing the massive overhead of a traditional bank with a set of automated, immutable smart contracts. UX-First Design: Creating a "wallet-gated" entry system that handles complex Web3 logic behind an intuitive fintech interface. What we learned Building on Shardeum taught us the power of horizontal scaling and how it can democratize access to high-frequency finance. We also gained deep insights into EIP-712 and Arweave GraphQL, learning that the key to RWA adoption is making blockchain "invisible" to the end-user. What's next for VanGaurd Mainnet Launch: Moving the $250M SOM target to Shardeum Mainnet. Advanced KYB/KYC: Integrating automated business verification for seamless MNC onboarding. Secondary Market: Enabling investors to trade their funded "Debt NFTs" before the invoice matures. Legal Expansion: Formalizing our jurisdictional property-seizure framework with regional legal partners. <div