---
slug: "craftpay"
url: "https://devpost.com/software/craftpay"
title: "CraftPay"
hackathon: "MNEE Hackathon: Programmable Money for Agents, Commerce, and Automated Finance"
organization: "MNEE, LLC"
winner: true
words: 583
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# CraftPay

> CraftPay converts X/Twitter engagement into instant MNEE stablecoin payouts on Ethereum.

[Devpost](https://devpost.com/software/craftpay) · hackathon [[MNEE Hackathon- Programmable Money for Agents- Commerce- and Automated Finance]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[finance_payments]] [[retail_commerce]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** ethereum-mainnet, ethers.js, express.js, mnee-stablecoin, next.js, node.js, postgresql, prisma, react, shadcn/ui, solidity, tailwindcss, typescript, x-api-v2

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for craftpay

## Body

Home Page Dashboard Campaigns System Architecture Inspiration Creators struggle to get paid fairly for their social media influence. Traditional sponsorship deals involve manual invoicing, delayed payments, and trust issues. Meanwhile, X (Twitter) provides real engagement metrics via API that could directly determine creator value. We asked: what if we could automate the entire payment flow—from brand budget to creator wallet—using verifiable on-chain transactions? What it does CraftPay is a programmable creator payment protocol that converts X/Twitter engagement metrics into automated MNEE stablecoin payouts on Ethereum mainnet . The flow: Brands create campaigns and set payout rates per engagement type Creators link their tweets to campaigns via URL X API v2 fetches real public metrics (likes, retweets, replies, quotes) Payment Links generated - shareable URLs for instant sponsor-to-creator payments Sponsor opens link → Connects wallet → Picks amount ($1, $5, $25, $100) → Signs transaction Creator receives MNEE directly to their Ethereum wallet with confetti celebration! 🎉 Every transaction is verifiable on-chain. No intermediaries, no invoices, no trust required. How we built it Smart Contracts (Solidity): CreatorPayoutPool contract deployed on Ethereum mainnet Handles campaign escrows, deposits, and payouts Emits PayoutProcessed events for full audit trail Backend (Node.js + Express + Prisma): X API v2 integration for fetching public tweet metrics (batch fetching up to 100 tweets) PostgreSQL database for campaign/creator management Payout calculation engine with configurable rates per engagement type Rate limit protection with cooldowns Frontend (Next.js 14 + React + TailwindCSS): Dashboard for campaign creation, tweet linking, metrics tracking Payment Links - shareable URLs that sponsors can open to pay creators instantly Preset payment amounts ($1, $5, $25, $100) + custom amounts Wallet connection via wagmi/MetaMask Confetti celebration on successful payments Block explorer links (Etherscan) for verification Key Integration: MNEE Stablecoin ( 0x8ccedbAe4916b79da7F3F612EfB2EB93A2bFD6cF ) - USD-pegged payments with 18 decimals X API v2 - Real public metrics without requiring creator OAuth Challenges we ran into X API Rate Limits: Free tier allows 15 requests per 15 minutes. We implemented batch fetching (single API call for multiple tweets) and cooldowns to stay within limits while still providing real-time metrics. MNEE Decimals: Initially used wrong decimal precision. Fixed to 18 decimals for proper token amounts. Mobile Wallet UX: QR codes weren't reliably working with MetaMask mobile. We pivoted to shareable Payment Links which provide a much better user experience—sponsors just click a link, connect wallet, and pay. Real-time Metrics: X API rate limits meant we needed efficient caching and snapshot-based payout calculations to track engagement since last refresh. Accomplishments that we're proud of Deployed on Ethereum Mainnet - Real MNEE moving on-chain, not testnet tokens Payment Links - Frictionless sponsor payments with preset amounts and one-click checkout End-to-end flow - From tweet URL to wallet payout in under 30 seconds Zero-trust model - Every payout verifiable on Etherscan Novel use case - First protocol converting X metrics to stablecoin payments programmatically What we learned X API v2's public_metrics endpoint is powerful for transparent creator valuation MNEE's ERC-20 standard (18 decimals) makes it trivial to integrate with custom payout flows Shareable payment links are superior UX compared to QR codes for web-native payments On-chain transactions fundamentally change the trust model for creator payments What's next for CraftPay Escrow Release Integration: Connect payment links to smart contract escrow release Multi-platform support: YouTube views, TikTok engagement, Instagram reach Creator OAuth: Allow creators to connect accounts for richer analytics Payout streaming: Real-time micro-payments as engagement accumulates using Superfluid DAO governance: Let creators and brands vote on rate structures <div