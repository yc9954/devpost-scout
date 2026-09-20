---
slug: "hydraswap-xt3940"
url: "https://devpost.com/software/hydraswap-xt3940"
title: "HydraSwap"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 539
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# HydraSwap

> HydraSwap is building a next-gen DEX powered by a superior AMM focussed on Liquidity Providers. By empowering liquidity providers we aim to make DEX liquidity CEXy!

[Devpost](https://devpost.com/software/hydraswap-xt3940) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**domain** [[agriculture_food]] [[supply_logistics]]
**substrate** [[code_repository]] [[structured_db]]

**stack** amazon-web-services, react, rust, vue

## How they structured the write-up

- our story
- the making of hydraswap
- realizing the vision

## Body

Swap Function with HMM Swap Function with HMM Add Liquidity Function with HMM Add Liquidity Function with HMM Concentrated Liquidity Preview Viewing My Liquidity Trading Module Staking Function LP Farming Function Our story Our team composed of ex volatility and exotics traders from JPMorgan sought out to build a high-performance AMM focussed on maximizing the returns for liquidity providers matching the returns enjoyed by traditional market makers. By focussing on LPs, our vision is to attract more liquidity into decentralized exchanges and bring the trading experience of the average DeFi user to the same level as centralized exchanges. The Making of HydraSwap Like anyone looking to foray into DeFi, our first choice was Ethereum but we quickly realized that our vision to create a sophisticated AMM was dead-on-arrival given the gas bottlenecks. This is when Solana caught our eye and we quickly realized that a lot of the computational bottlenecks that we faced on Ethereum were not there on Solana. Digging more into it, we clearly saw that Solana’s POH coupled with the Tower-BFT was the only game in town that aspired to achieve the throughput of centralized databases. This is exactly what we needed to implement a DEX that could match up to CEXes. Moreover, it was clear to us that Solana was the frontrunner in becoming the primary blockchain for trading oriented use cases in DeFi. With the above clarity we set out to create our AMM of the future on Solana. The first thing we wanted to solve was the pricing intelligence on AMMs as the current crop of AMMs are mostly inward looking and solely rely on their inventory for pricing which is quite basic. In order to create an ‘intelligent’ AMM, we needed additional market information. Luckily for us, we found the ideal partner in Pyth . Integrating with Pyth’s high-performance oracle was a seamless experience. Our next challenge was to optimally compute our ‘smart’ pricing formulae on-chain. This was not straightforward but we eventually overcame this by creating our own numerical optimizations for this and released our beta version in September 2021. This was a major first step and allowed us to learn the ins and outs of Solana while building something usable. We are currently in the process of combining the above with two additional game-changing AMM innovations that we will discuss further in the project details section. We aim to launch our official v1 with these powerful features in November2021 and hope to change the DEX liquidity landscape in Solana and ultimately in DeFi. While we work hard on developing a top-notch product, HydraSwap is committed to building a strong community and we have already begun our go-to-market work. So far, HydraSwap has an ever-growing community of 16K+ members on Telegram and 11K+ followers on Twitter . We are also keen on sharing our technology and market insights via our GitBook and Medium pages. Realizing the Vision Looking further ahead on the roadmap, our vision is to become the one-stop application for liquidity providers in a cross-chain world. On top of a powerful AMM we aim to integrate with existing bridges like Wormhole to create cross-chain LP tokens and allow LPs to mine and farm in Solana with minimal hassle. <div