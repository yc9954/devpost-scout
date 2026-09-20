---
slug: "flatcoinusd"
url: "https://devpost.com/software/flatcoinusd"
title: "Lendr Network (Previously FlatcoinUSD)"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 542
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/regulation_legal_text"
---

# Lendr Network (Previously FlatcoinUSD)

> Lendr Network is a decentralized lending protocol offering 0% interest loans for real-world assets (RWAs), including the inflation-proof stablecoin LendrUSD, LendrGold, and LendrRE (US Real Estate).

[Devpost](https://devpost.com/software/flatcoinusd) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[code_repository]] [[regulation_legal_text]]

**stack** chainlink, solidity, truflation

## How they structured the write-up

- inspiration
- what lendr does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lendr network

## Body

LendrUSD Application Dashboard Liquidations Dashboard For the most recent updates on Lendr, please visit https://lendr.network Inspiration With the Terra/Luna catastrophe costing investors $60 Billion dollars , and other major stablecoins depegging such as USDC and BUSD, our company struggled to find a trustworthy stablecoin to hold funds in. When we looked into things further we found the problem was far worse than we originally imagined: Over 92% of the stablecoin market is centralized and can be shut down by regulations at any time (i.e. BUSD) Stablecoin holders lost more than $9 Billion USD of spending power last year to inflation Most major on-chain stablecoins charge an ongoing interest rate just to mint Overall, the stablecoin market was clearly in need of innovation. This led us to create LendrUSD, a decentralized inflation-proof stablecoin that offers 0% interest loans. In the process of creating LendrUSD, we also decided to bring other real-world assets on chain such as gold (LendrGold) and US real estate (LendrRE). What Lendr does Lendr Network provides 0% interest loans in an inflation-proof stablecoin (LendrUSD) and other on-chain real-world assets (LendrGold, LendrRE - Real Estate). We created LendrUSD (USDL) to solve the issues other stablecoins are facing. LendrUSD is a fully decentralized, governance-free, inflation-proof, stablecoin. It is fully over-collateralized using only verifiable decentralized on-chain assets. LendrUSD has a moving price target that is pegged to an unbiased on-chain inflation index that uses over 18 million data points to determine the true inflation rate, making LendrUSD inflation-proof. How we built it We built Lendr using Chainlink oracles, Chainlink automation, Truflation oracles, Quicknode, open-source code, and newly created code from our team. We had a clear vision in mind for a censorship-resistant, immutable stablecoin that users could depend on without having to place trust in our team. As we worked on LendrUSD, the idea expanded into a lending platform for a variety of other real-world assets. We believe this will help bridge the gap between crypto and conventional financial investors, hopefully allowing crypto as a whole to tap into the existing 40 trillion dollar US financial market. Challenges we ran into A fully decentralized inflation-proof stablecoin did not exist when we started and it took significant time to plan, build, and test a system to function as one. We had to ensure the system was robust and could withstand a variety of market conditions without our intervention. Integrating the inflation-proof token into a decentralized lending system also presented a variety of unique challenges. Finally, security was a major concern since we will not be controlling the system directly. Our choice of oracles and their integrations had to be robust and secure. Accomplishments that we're proud of The functionality of a decentralized lending platform, capable of supporting a variety of assets, and an inflation-proof stablecoin all properly running on the blockchain is something we are very proud of! What we learned Even a simple idea will be a lot harder than it looks! But in the final steps of creating this product we learned some tangible specific skills like how to integrate on-chain oracles and automation from chainlink into our smart contracts. What's next for Lendr Network We plan to launch to a mainnet within the next month after completing our security audits. <div