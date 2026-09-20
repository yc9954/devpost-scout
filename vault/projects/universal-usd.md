---
slug: "universal-usd"
url: "https://devpost.com/software/universal-usd"
title: "Universal USD"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 504
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Universal USD

> UUSD is a fraction-algorithmic stablecoin that uses native token and stablecoin to collateralize its value to mint on Avalanche Chain.

[Devpost](https://devpost.com/software/universal-usd) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets


**stack** avalanche, chainlink, nextjs, solidity, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for universal usd

## Body

Inspiration As we have been operating Dopple Finance, a decentralized stablecoin exchange, for over 8 months, we have gained valuable knowledge and experience from enormous volumes of trading data. Since Dopple Finance was started, we have been studying a number of stable coins in several aspects including transparency, capital efficiency, and stability. However, we are still unable to find any stablecoin that can solve these 3 problems. Moreover, the data indicates that the biggest stablecoin dominates the market with over 50% market share. So, we would like to present Universal USD, the solution to these problems. What it does As we mentioned earlier, Universal USD was designed to overcome the obstacles such as transparency, capital efficiency, and stability. At the same time, Universal USD also brings benefits to the community. With the algorithm behind it, it will allow any Blockchain Platform to increase the utility of their own token by creating the native stablecoin partially backed by a native token which means that it will significantly boost the demand of the native token. How we built it Universal USD is fractional-algorithmic, meaning collateralized by a combination of stablecoin and native chain token. Universal USD uses a dynamic collateral ratio, which makes it more safe and stable. Stablecoin collateralizes a part of it while the other is algorithmic, using our native chain token AVAX. The Dynamic Collateral Ratio makes UUSD a highly scalable stablecoin. It creates a feedback loop between Stablecoin and AVAX, meaning that when the AVAX token is healthy (its price goes increases), the UUSD algorithm is likely to use more AVAX as collateral. In contrast, when the AVAX token is unhealthy (its price goes downwards), the UUSD algorithm will use more stablecoin as collateral. We use the Chainlink price feed to ensure that we have the correct price and the system is safe from an attacker. Challenges we ran into We implement a similar idea to make synthetic assets that are partial back by gov token, but we have to change the algorithm to lock and release native tokens instead of mint and burn. Accomplishments that we're proud of Ability of UUSD (prototype) that can peg its price The world's first fractional algorithmic stable partial back by native chain token. What we learned Since the project was started, many obstacles have been overcome. We have gained Algorithmic comprehension and knowledge on tokenization which are precious. However, there is a thing that we are learning and trying to achieve, building awareness. We found that the marketing aspect cannot be done alone. Although we have a good product, encouragement from partners is still essential. What's next for Universal USD It has been proven that Universal USD can perform as we expected. Additionally, we believe that we should not rely on a specific stablecoin but would rather make it more decentralized. Each chain should have its own stablecoin to retain the balance of power. It is also beneficial for all of us as this is a scheme to prevent the Cryptocurrency market from collapsing. <div