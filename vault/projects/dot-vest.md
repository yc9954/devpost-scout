---
slug: "dot-vest"
url: "https://devpost.com/software/dot-vest"
title: "Dot-Vest."
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 486
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/sensor_telemetry"
---

# Dot-Vest.

> Navigating DeFi can be a complex maze for newbies. Several projects, multiple tabs, and countless hours of researching, comparing, and fine-tuning yield bearing strategies.Now explore Dot Vest.

[Devpost](https://devpost.com/software/dot-vest) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[sensor_telemetry]]

**stack** acala, asset-hub-(substrate-based-chains)-apis-&-services:-supabase-(auth-&-db), bifrost, coingecko, coingecko-api-(token-prices)-cloud-&-deployment:-vercel-other:-polkadot.js-api, hydration, lucide-react-icons, next.js, next.js-blockchain:-polkadot, polkadot, polkadot.js, react, scss, scss-for-styling

## How they structured the write-up

- inspiration
- what it does.
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dot-vest.

## Body

Inspiration The inspiration to build DotVest comes from the burden of exploring and managing DeFi assets/positions across multiple Polkadot-based parachains and protocols, presenting a fragmented and challenging experiencefor retail users. Personal financial investors may also struggle to track balances, monitor token prices, and see portfolio value in real-time, as it spreads across multiple platfoms and dapps. We decidedr to create a unified, user-friendly platform that brings all assets together in a single dashboard, making multi-chain investment management simple and secure. What it does. DotVest allows users to: Connect a wallet and view balances across multiple Polkadot-based chains: Polkadot Relay, Acala, Hydration, Bifrost, and Asset Hub. See real-time USD valuations of their tokens. Find staking pools with yield bearing opportunities across all connected parachains. Track their portfolio in one dashboard, with total portfolio value calculated automatically. Reset and recover their password securely via Supabase auth. Switch between viewing relay chains, asset hub, or all chains at once. How we built it Frontend: TypeScript, React, Next.js, SCSS for responsive and elegant UI. Backend/Auth: Supabase for user authentication, password recovery, and session management. Blockchain Integration: Polkadot.js API with WebSocket RPC connections to multiple chains. Data & Pricing: CoinGecko API to fetch real-time token prices. Deployment: Vercel for production hosting and continuous deployment. Challenges we ran into Some RPC endpoints were unstable, so I had to implement dynamic error handling and retries to ensure the app remained responsive. Handling multi-chain balances efficiently without blocking the UI or causing unnecessary network requests. Ensuring secure password recovery links worked correctly on a production domain instead of localhost. Integrating real-time pricing with caching to prevent hitting API limits. Accomplishments that we're proud of Successfully built a multi-chain wallet dashboard that is responsive and production-ready. Implemented real-time portfolio value updates with USD conversions. Deployed the app to Vercel with working Supabase authentication and secure password recovery flow. Created a scalable architecture that allows adding more Substrate-based chains in the future. What we learned How to interact with multiple Substrate chains using Polkadot.js API. Handling authentication and sessions with Supabase in a React/Next.js environment. The importance of robust error handling and caching when working with unreliable RPC endpoints. Best practices for deploying a Web3 app with production-ready authentication flows. What's next for Dot-Vest. Custom Alerts: Notify users about token price changes, portfolio thresholds, or staking rewards. Expanded Parachain Support: Integrate more Substrate-based chains to increase portfolio coverage. Multi-Chain NFT Tracking: Allow users to track NFTs across Polkadot parachains alongside tokens. Social & Community Features: Enable sharing portfolio snapshots or staking performance with friends or in communities. Automated Rebalancing Suggestions: Recommend portfolio adjustments based on market movements or staking opportunities. Advanced Charting & Insights: Add historical performance charts, risk metrics, and ROI projections for deeper analysis. Mobile Push Notifications: Keep users updated in real-time on mobile devices about critical events or rewards. DeFi Integration: Explore cross-chain lending, borrowing, or liquidity pool opportunities directly within DotVest. <div