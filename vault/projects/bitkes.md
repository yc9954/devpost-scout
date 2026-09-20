---
slug: "bitkes"
url: "https://devpost.com/software/bitkes"
title: "BitKES"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 395
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "user/general_public"
---

# BitKES

> BitKES is an overcollateralized stablecoin protocol that controls the bKES token which uses both Matic & OpenSea NFTs as collateral.

[Devpost](https://devpost.com/software/bitkes) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**user** [[general_public]]

**stack** chainlink, ethers.js, hardhat, node.js, polygon, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bitkes

## Body

Home Page Mint Page Burn Page Debt Positions Page Inspiration My inspiration for building bKES was after spending some time in the crypto world and realizing how important stablecoins were to day-to-day crypto utility in the real world. After having some issues with USD-pegged stablecoins because of my country's unstable currency exchange rates for the past couple of months I thought having a KES-pegged stablecoin would solve some of the issues crypto enthusiasts from my country face. It would allow clearer and stable exchange rates and hopefully, eliminate some of the barriers to entry factors that are attached to crypto utility such as token volatility. Also, I thought BitKES would allow hodlers to access liquidity for other short-term uses while still remaining long on tokens they invested in and give them the flexibility of having on-chain lending solutions that can service their needs. link - This article also sparked a huge interest in the development of the project. What it does bKES is a stablecoin lending protocol on Polygon that accepts MATIC/USDC and OpenSea NFTs as collateral when a user creates a debt position and mints bKES(an overcollateralized stablecoin pegged 1:1 with the Kenyan Shilling). The protocol enables precise debt-collateral ratios thanks to chainlink's API consumers. It prevents negative debt positions thanks to user-incentivised liquidations on the platform by allowing anyone with MetaMask to liquidate a position whose health factor(debt-collateral ratio) is low and get a cut of the positions' collateral. How we built it I built bKES using Solidity and various EVM tooling(ethers.js, hardhat). I used chainlink API consumers to access the external MATIC/KES exchange rates. Challenges we ran into The major challenge I encountered was accessing OpenSea NFT data using chainlink API consumers because of a security implementation on OpenSea NFT API resources. Accomplishments that we're proud of I was able to gain an in-depth understanding of the Solidity works and can comfortably work on EVM-based projects with more confidence. What we learned I learned a lot about smart contract architecture and how the EVM works especially in regard to numbers and math equations. I experienced how important chainlink data is to the DeFi ecosystem as well. I had a lot of fun building this project What's next for BitKES Hopefully finishing up on loose ends(tests) and thinking through ways to launch BitKES to the world(probably listing a MATIC/bKES pair on QuickSwap) <div