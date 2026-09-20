---
slug: "chainlink-portfolio-polkadot-cross-chain-activity-tracker"
url: "https://devpost.com/software/chainlink-portfolio-polkadot-cross-chain-activity-tracker"
title: "ChainLink Portfolio - Polkadot Cross-Chain Activity Tracker"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 969
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# ChainLink Portfolio - Polkadot Cross-Chain Activity Tracker

> "Unified cross-chain dashboard for Polkadot: View all parachain assets, get AI insights, check portfolio health, and execute real XCM transfers—all in one beautiful interface."

[Devpost](https://devpost.com/software/chainlink-portfolio-polkadot-cross-chain-activity-tracker) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[financial_record]]

**stack** 3.1, 8b, ai:, api, apis:, asset, astar, chain, chains:, coingecko, data), extension, frontend:-next.js-14, groq

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chainlink portfolio - polkadot cross-chain activity tracker

## Body

ChainLink Portfolio - Project Story Inspiration As a Web3 learner exploring Polkadot, I faced a frustrating problem: my crypto identity was scattered across multiple parachains. Checking my Astar balance meant opening one explorer, Moonbeam another, Polkadot yet another. I realized this fragmented experience was preventing mainstream adoption—users shouldn't need to be blockchain experts to see their assets. Polkadot's unique multi-chain architecture is powerful, but the user experience needed to catch up. I wanted to build something that made cross-chain interaction as simple as checking your bank account—one dashboard, complete visibility, and actual cross-chain actions. What it does ChainLink Portfolio is an AI-enhanced, privacy-first dashboard that unifies your Polkadot ecosystem presence: Multi-Chain Aggregation: Connects to 4 parachains (Polkadot, Astar, Moonbeam, Paseo Asset Hub) and displays all balances in real-time with USD values AI Portfolio Advisor: Powered by Groq's Llama 3.1, it analyzes your holdings and provides personalized recommendations on staking, allocation, and cross-chain opportunities Portfolio Health Score: Calculates a 0-100 score based on diversification, risk balance, chain activity, and portfolio size Real XCM Transfers: Execute actual cross-chain asset transfers using Polkadot's XCM protocol—move tokens between parachains with one click Beautiful Visualizations: Interactive pie charts, chain cards, and responsive design that works on any device Privacy-First: All data fetched client-side through Polkadot.js—no backend, you control your data How we built it Tech Stack: Next.js 14, TypeScript, Tailwind CSS, Polkadot.js API, XCM Protocol, Groq AI, Recharts Architecture Wallet Integration: Built secure connection with Polkadot.js browser extension Parallel Chain Queries: Implemented Promise.allSettled to query all 4 chains simultaneously for fast load times Price Integration: Connected to CoinGecko API for real-time token prices with mock prices for testnet tokens Portfolio Aggregation: Created utility functions to calculate total value, percentages, and format blockchain data into human-readable numbers AI Service: Integrated Groq API with carefully crafted prompts that understand Polkadot ecosystem specifics Health Score Algorithm: Developed scoring logic that evaluates diversification (entropy-based), risk balance, activity levels, and portfolio size XCM Implementation: Built real cross-chain transfer functionality using limitedTeleportAssets and limitedReserveTransferAssets , handling SS58 address encoding and XCM V3 message format Responsive UI: Designed mobile-first interface with floating AI chat, interactive charts, and smooth animations Development Approach: Used Spec-Kit methodology with clear constitution, specifications, and incremental implementation Challenges we ran into SSR vs Browser APIs: Next.js server-side rendering conflicted with Polkadot.js extension (browser-only). Solved with dynamic imports and typeof window checks. XCM Address Encoding: Spent hours debugging "Expected 32 bytes, found 48 bytes" error. Learned SS58 addresses need decodeAddress() to convert to raw 32-byte account IDs for XCM messages. Testnet Token Availability: Getting testnet tokens was harder than expected. Faucets were deprecated, rate-limited, or broken. Had to find alternative faucets and coordinate multi-chain testing. AI Data Formatting: Initially, AI recommendations were generic. Had to refine prompts extensively to ensure the AI understood users already own these tokens and should focus on allocation/staking strategies, not purchase recommendations. Zero Balance Visualization: Pie chart was hiding chains with zero/small balances, making the portfolio look incomplete. Fixed by ensuring all chains always render with minimum values and (Empty) labels. Cross-Testnet XCM Limitations: Discovered that XCM transfers between different testnets (Paseo ↔ Westend) don't always reflect balance changes due to infrastructure incompatibility, though transactions submit successfully on-chain. Price API for Testnets: Testnet tokens don't have real market prices. Implemented mock pricing logic that mirrors mainnet token prices for realistic demo values. Accomplishments that we're proud of Real XCM Transfers: Not a mock or demo—actual on-chain cross-chain asset transfers using Polkadot's XCM protocol AI That Understands Polkadot: Created an AI advisor that provides genuinely useful, ecosystem-specific recommendations about staking, XCM opportunities, and parachain strategies Complete Portfolio Analytics: Built a comprehensive health scoring system that goes beyond simple balance display Web2 UX in Web3: Achieved a polished, responsive interface that feels modern and accessible to non-technical users Privacy-First Architecture: No backend, no data collection—everything client-side while still being feature-rich Performance: Parallel queries load 4 chains simultaneously in ~2-3 seconds with graceful error handling Fully Responsive: Works beautifully on desktop, tablet, and mobile with floating AI chat that doesn't obstruct content Production-Ready Code: Type-safe TypeScript, clean architecture, comprehensive error handling, and well-documented codebase What we learned Technical Learnings Deep understanding of XCM protocol, including teleport vs reserve transfers, versioned locations/assets, and proper account encoding Polkadot.js API intricacies: chain metadata, runtime calls, transaction signing, and status monitoring How to integrate AI effectively in Web3 apps—not just bolt-on features but genuinely useful tools Browser-based blockchain architecture without compromising on features or security Efficient parallel async operations for multi-chain data fetching Blockchain Concepts Polkadot's multi-chain architecture and how parachains interoperate Account balance types: free, reserved, frozen, and how they're calculated Token decimals and proper formatting from raw blockchain values RPC endpoint reliability and fallback strategies Testnet vs mainnet differences and limitations Design Philosophy Privacy doesn't mean sacrificing UX—you can have both User-centric design means hiding complexity, not removing features Good error handling is part of great UX Mobile-first design forces clarity and priority AI in Web3 LLMs can provide valuable insights when given properly structured blockchain data Context is everything—generic prompts produce generic advice Real-time data + AI = powerful user experience multiplier What's next for ChainLink Portfolio - Polkadot Cross-Chain Activity Tracker Immediate Post-Hackathon Mainnet Support: Switch from testnet to production chains with real assets More Parachains: Add Hydration, Bifrost, Phala, Interlay, and other major parachains Transaction History: Display recent transfers, staking actions, and XCM movements NFT Gallery: Show NFTs across all parachains in unified view Ultimate Goal Make ChainLink Portfolio the go-to dashboard for Polkadot ecosystem—the place where users start their day to check their complete cross-chain presence, get actionable insights, and execute multi-chain strategies with confidence. Help bridge Web2 and Web3 by providing an experience that's both powerful for advanced users and accessible for newcomers. The future is multi-chain. ChainLink Portfolio makes it simple. <div