---
slug: "nexhacks-now93q"
url: "https://devpost.com/software/nexhacks-now93q"
title: "PolyYield"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 606
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/financial_record"
---

# PolyYield

> No-risk prediction markets: users keep their capital, winners earn yield. A safe, addictive way to onboard the next wave of Polymarket users.

[Devpost](https://devpost.com/software/nexhacks-now93q) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[financial_record]]

**stack** anchor, blockchain, javascript, nextjs, polymarket, postgresql, react, rust, solana, supabase, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- how we used solana specifically
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nexhacks

## Body

Homepage Market Page Crypto Wallet Connectivity Place A Bet Inspiration Polymarket has a major onboarding challenge, new users are hesitant to trade because they’re afraid of losing money. We wanted to remove that fear and make prediction markets accessible to everyone. What it does We built no-risk prediction markets where users never lose their principal. Winners earn yield, while losers get their money back, so only upside is at stake. This is important because fear of losing money is the biggest barrier to onboarding new users. By removing downside risk, users can participate, learn, and build confidence without financial stress. This increases user adoption, engagement, and long term retention for prediction markets. How we built it Frontend: Built with Next.js, React, TypeScript, and Tailwind CSS to create a sleek, responsive UI that clearly explains the no-risk model. We also added custom WebGL particle animations using Three.js and React Three Fiber. Blockchain: Built on Solana using the Anchor framework for fast, low-cost transactions, with on-chain deposit tracking and settlement logic. Wallet Integration: Integrated Solana Wallet Adapter for seamless wallet connections and transactions. Yield Generation: Pooled USDC deposits are lent through DeFi protocols generating approximately 12% APY, and the yield is distributed only to correct predictors. Data: Integrated Polymarket’s API to fetch real-time market data and sync off-chain markets with on-chain positions. How we used Solana Specifically Each prediction pool is a Solana program written in Rust that manages USDC deposits, enforces principal protection, and tracks user positions on chain. Because Solana transactions are extremely cheap, users can enter and exit markets, update positions, and claim payouts without worrying about gas costs. We used Solana’s fast block times to make markets feel real time. Deposits are confirmed almost instantly, and pool state updates and reward calculations happen with minimal latency, which is critical for an onboarding focused product. Solana’s account model allows us to store pool state, user balances, and market metadata efficiently, enabling many users to interact with the same market concurrently. This scalability makes it possible to support large no risk pools where higher participation directly increases yield and rewards. Challenges we ran into Solana Devnet Rate Limits: Testing smart contracts was slow due to strict devnet faucet limits, which made iteration frustrating even though we were using test funds. Yield Calculation Logic: We had to carefully balance accurate yield math with a simple UX that showed realistic returns, such as around $2 on a $100 deposit over 30 days. Real-time Data Sync: Keeping Polymarket data synchronized with Solana-based user positions required careful coordination between off-chain APIs and on-chain state. Accomplishments that we're proud of We created a genuinely zero-risk prediction market where losers always get their full principal back. We built an intuitive UI that makes a complex financial model easy to understand. We achieved seamless Solana wallet integration with real on-chain deposits. We made prediction markets accessible to users who would never trade due to fear of loss. What we learned We gained a deep understanding of Solana’s architecture, the Anchor framework, and devnet limitations. We learned how DeFi yield generation can be used to create entirely new financial products. We learned how to build production-ready dApps with proper wallet integration and transaction handling. What's next for NexHacks We plan to launch Poly Yield on Solana mainnet with real USDC and live yield generation. We will expand beyond Polymarket to support custom, community-created prediction markets. We will integrate multiple DeFi protocols to optimize yield for users. We plan to build a native iOS and Android app for on-the-go predictions. We will add social features such as leaderboards, achievements, and sharing for correct predictions. <div