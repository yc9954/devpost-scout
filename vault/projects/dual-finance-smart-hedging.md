---
slug: "dual-finance-smart-hedging"
url: "https://devpost.com/software/dual-finance-smart-hedging"
title: "Dual Finance: Natural Liquidity"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 252
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Dual Finance: Natural Liquidity

> Automated Risk Management of Option Vaults on OpenBook DEX

[Devpost](https://devpost.com/software/dual-finance-smart-hedging) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets


**stack** anchor, chainlink, pyth, quicknode, rust, switchboard, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dual finance: natural liquidity

## Body

Dual Investment Pools (DIP) Staking UI for SOL, BTC & ETH Earn Real Yield. Deposit crypto to get paid USDC immediately Beginner Mode for easier to understand option trading & staking Trading logic logs. Chainlink prices used hedge and to calculate delta & gamma Connection to Quicknode RPC for polling tokenized option positions & low latency trade entry on OpenBook Risk Manager providing natural liquidity via Chainlink price to SOL/USDC on OpenBook Risk Manager providing natural liquidity on a very illiquid MNGO/USDC on OpenBook Inspiration Crypto Tokenomics are broken. Options based incentives present a better ways to align participants of decentralized communities but lack liquidity. What it does Dual Finance provides liquidity for and from on-chain option trades. Users can earn real yield by depositing crypto into Dual Investment Pools (DIPs). How we built it On Solana using OpenBook (Serum Community Fork) integrating multiple oracles including Chainlink for robust pricing & Quicknode RPCs for fast trading Challenges we ran into Managing positions and getting robust oracle pricing on illiquid products in an automated fashion creates lots of edge cases that can lead to poor trades. Accomplishments that we're proud of The seamless connection between the protocol taking on options risk and creating organic liquidity on-chain. What we learned Not all Oracles are created equal, robustness and confidence from each data sources varies greatly. What's next for Dual Finance: Natural Liquidity Planning on additional integrations onto Solana DEXs as well as moving multi-chain. DUAL token launch that dogfoods options based token distribution. <div