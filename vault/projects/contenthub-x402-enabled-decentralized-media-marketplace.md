---
slug: "contenthub-x402-enabled-decentralized-media-marketplace"
url: "https://devpost.com/software/contenthub-x402-enabled-decentralized-media-marketplace"
title: "ContentHub: x402-Enabled Decentralized Media Marketplace"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 387
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/retail_commerce"
  - "user/general_public"
  - "substrate/financial_record"
---

# ContentHub: x402-Enabled Decentralized Media Marketplace

> A decentralized, premium content marketplace built on Base Sepolia empowering creators to monetize high-quality video directly through x402 offering seamless rentals and subscriptions settled in USDC.

[Devpost](https://devpost.com/software/contenthub-x402-enabled-decentralized-media-marketplace) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[finance_payments]] [[housing_homeless]] [[retail_commerce]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** base-sepolia, foundry, framer, ipfs, lighthouse, next.js, privy, solidity, viem, x402

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Inspiration The current creator economy is plagued by high platform fees and fragmented payment systems. We wanted to build a platform that "solves the internet's original sin" by re-activating the long-dormant HTTP 402 (Payment Required) status code. Our goal was to create a "zero-middleman" environment where payments are as native to the web request as the data itself, enabling both humans and AI agents to transact instantly. What it does ContentHub is an end-to-end video monetization engine: For Creators: An intuitive studio to upload content to decentralized storage (Lighthouse/IPFS) and register immutable access rights on the Base Sepolia blockchain. For Consumers: A unified library to manage 24-hour rentals and lifetime subscriptions settled in USDC. x402 Payment Flow: The hub serves content via the x402 standard. When an unauthenticated request (human or AI agent) hits a premium asset, the server responds with a 402 Payment Required header. The user then settles the transaction on-chain to unlock the resource. How we built it Frontend: Built with Next.js 15 and Tailwind CSS v4 for a high-performance, mobile-first experience. On-Chain Logic: Developed custom Solidity contracts using Foundry on Base Sepolia to handle rental durations and on-chain access verification. Identity: Integrated Privy for seamless, wallet-based authentication. Storage: Leveraged Lighthouse/IPFS for decentralized storage, ensuring content remains under creator control. Challenges we ran into Implementing the x402 handshake was our biggest technical hurdle. We had to ensure the frontend could gracefully handle the "Payment Required" response, trigger a wallet signature, and retry the request with the X-PAYMENT header. Bridging this Web3 payment flow into a standard Next.js 15 environment required building custom middleware for real-time blockchain verification. Accomplishments that we're proud of Direct Monetization: Successfully enabling a flow where 100% of the revenue goes directly to the creator. Seamless Rentals: Implementing on-chain time-locks that automatically expire access after 24 hours. Agent-Readiness: By following the x402 specification, we have built an app that is "Agent-Native." What we learned We learned that the x402 protocol is the missing link for the machine-to-machine economy. By removing traditional checkouts, we make the internet more efficient for both creators and autonomous agents. What's next Autonomous Agent Consumption: Integrating with agent frameworks so AI agents can pay to watch/process content. Dynamic Pricing Agents: Implementing smart contracts where rental prices fluctuate based on demand, managed by an autonomous "Governor Agent." <div