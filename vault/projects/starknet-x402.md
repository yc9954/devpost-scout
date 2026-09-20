---
slug: "starknet-x402"
url: "https://devpost.com/software/starknet-x402"
title: "Starknet-x402"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 366
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
---

# Starknet-x402

> x402 payment protocol on Starknet. Pay-per-use APIs with blockchain payments in HTTP headers

[Devpost](https://devpost.com/software/starknet-x402) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** nextjs, react, starknet

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for starknet-x402

## Body

Banner Protocol Sequence About Us Success Response Inspiration Coinbase proposed x402 (HTTP 402 Payment Required) to enable HTTP-native micropayments, but no implementation existed on Starknet blockchain. We saw an opportunity to bring this vision to life on Starknet's Layer 2, making API monetization seamless and affordable. What it does Starknet x402 enables pay-per-use APIs with blockchain payments embedded directly in HTTP headers. No wallet popups, no subscription models—just cryptographic signatures in an X-PAYMENT header. Developers protect their APIs with 3 lines of code, and users pay sub-cent fees for each request. How we built it Protocol: Extended Coinbase's x402 spec for Starknet with cryptographic signature verification using Pedersen hashing Architecture: Three-component system—client signing (Starknet.js), middleware interception (Next.js), facilitator settlement (on-chain) Smart Contracts: ERC-20 token transfers via transfer_from on Starknet Sepolia SDK: Published @adipundir/starknet-x402 on npm with TypeScript support for Next.js and Express Stack: Next.js 15, Starknet.js v7, TypeScript, Challenges we ran into Starknet.js v6→v7 Migration: Major version update broke transaction execution—required complete API refactor BigInt Serialization: JSON.stringify doesn't handle BigInts—solved by converting to hex strings before encoding Pedersen Hash Constraints: Starknet's hash function requires lowercase addresses and 252-bit nonces—normalized all inputs Fee Estimation: Transaction version mismatches caused "undefined to BigInt" errors—fixed by updating library and proper fee calculation Environment Variables: Next.js client/server variable separation caused production failures—standardized naming with NEXT_PUBLIC_ prefix Accomplishments that we're proud of 🥇First Starknet blockchain implementation of Coinbase's x402 protocol ✅ Production-ready SDK published on npm with full TypeScript support ✅ Sub-cent transactions ($0.001 fees) making true micropayments viable ✅ Zero UX friction—no wallet popups, just seamless payments ✅ Complete documentation with examples for Next.js, Express, and facilitator setup ✅ Live demo with on-chain transactions on Starknet Sepolia What we learned Starknet account abstraction enables powerful patterns like pre-signed transactions and meta-transactions HTTP headers can carry complete payment authorizations securely using cryptographic signatures Layer 2 economics fundamentally change what's possible with micropayments Middleware-based payment protection is elegant and framework-agnostic Proper environment variable management is critical for Next.js production deployments What's next for Starknet-x402 Mainnet Deployment: Launch on Starknet mainnet with multi-token support (ETH, USDC, STRK) Decentralized Facilitators: Network of independent facilitators for settlement Expansion : Expanding integrations for other popular frameworks <div