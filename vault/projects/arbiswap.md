---
slug: "arbiswap"
url: "https://devpost.com/software/arbiswap"
title: "ArbiSwap"
hackathon: "Evmos Momentum Hackathon led by Web3Scholarships (Deployment required for prize)"
organization: "Huobi"
winner: true
words: 426
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "substrate/geospatial"
---

# ArbiSwap

> It is a DEX aggregator with automated arbitrage.

[Devpost](https://devpost.com/software/arbiswap) · hackathon [[Evmos Momentum Hackathon led by Web3Scholarships -Deployment required for prize-]]

## Facets

**domain** [[finance_payments]] [[security_privacy]]
**substrate** [[geospatial]]

**stack** amazon-web-services, argocd, go, hardhat, nestjs, ps, redis, rust, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for arbiswap

## Body

ArbiSwap swap page ArbiSwap logo Mechanism of DEX Aggregator V2 Inspiration For evmos, there is little liquidity in each DEX, and Liquidities were separated from DEXes. If traders swap from tokenA to tokenB, huge price impacts occur due to the lack of liquidity. Many traders' willingness to swaps decrease and it affected liquidity providers also. Liquidity providers earn less than they expected as swap volume is low, and they become reluctant to provide liquidity to the pools, which makes a vicious cycle. We aim to aggregate separated liquidities and maximize users' outputs by routing engine and cyclic arbitrage logic integration to minimize slippage. By doing so, we can solve the big huddles of swap willingness problems and make additional effects on the robust price oracle with high liquidity in EVMOS ecosystem. What it does Arbiswap finds the optimal routes of the current block by searching all DEXes and executing the swaps. It is DEX Aggregator V1. We add MEV protection and slippage minimizing logic by calculating the cyclic arbitrage using flashloan and executing if the condition matches. We call it DEX Aggregator V2 How we built it We fetched block data from solidity viewer codes & found out the search algorithm to take optimal swap route. We investigated all of DEXes AMMs and make optimal engines using rust. We executed tx by deploying contracts from the hardhat framework. For user UI/UX, we used typescript, nestjs to interact server(go) and web app. We accumulated time-series data by using Redis to provide a robust price oracle(time-weighted / liquidity-weighted pricing) by using our optimal engine. We deployed web-app, server for app service, using argocd & amazon service in mainnet environment. Challenges we ran into Adapting each interface of DEX was really hard as there were few docs & contract address Infos. Integrating the front-end & back-end was difficult to build due to the time difference. Accomplishments that we're proud of Our Arbiswap engine is the first product that can find the optimal swap paths and protecting paths and it is also the first DEX aggregator project in EVMOS. ArbiSwap is expected to alleviate the potential danger of the large price impact and slippage from DEX traders on the EVMOS chain which is very vulnerable to mass swap volume because of the lack of liquidity. What we learned EVMOS De-Fi ecosystem, How should we cooperate with people who have a different background? Bridge system and COSMOS ecosystem. What's next for ArbiSwap Both swap & zap. swap and order-book trade matching solution Multichain including EVM compatible and EVM incompatible ones <div