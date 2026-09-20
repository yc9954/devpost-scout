---
slug: "velvet-capital"
url: "https://devpost.com/software/velvet-capital"
title: "Velvet.Capital"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 470
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# Velvet.Capital

> Velvet.Capital - a cross-chain DeFi Asset Management protocol that helps people & institutions create index funds and other structured financial products as well as manage their portfolios on-chain.

[Devpost](https://devpost.com/software/velvet-capital) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[civic_government]] [[developer_tools]]
**substrate** [[financial_record]]

**stack** hardhat, javascript, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for velvet.capital

## Body

Velvet.Capital makes DeFi simple! What is Velvet.Capital? Inspiration We believe DeFi is the future that empowers people to become financially independent. But DeFi is hard! Users are intimidated by countless options, confused by the complexity of protocols and struggling to navigate solutions built for crypto-natives. As a result, people chase the highest yield and get burnt when the token price tanks to zero. What it does Velvet.Capital makes DeFi simpler and safer by helping you diversify across assets, ecosystems and yield farming solutions. It's a cross-chain DeFi Asset Management protocol that helps people & institutions create index funds and other structured financial products as well as manage their portfolios on-chain. How we built it We have a completely modular architecture built out on Polygon as a base infrastructure: Oracle module is fetching market data from Chainlink and is passing it to the Trading module, which is using Quickswap liquidity to create a target portfolio in a single transaction. Whenever there is price change more then 50bps, oracle data feed updates and our contract captures a new price feed. A portfolio-backed token representing user's share gets minted upon deposit and burnt upon withdrawal whereas underlying assets are kept within a Gnosis Safe vault. The factory contract is flexible and allows to deploy any new portfolios/strategies within a few minutes, we deployed 2 strategies as an example: Top-5 DeFi projects overall and Top-5 Projects that have highest TVL on Polygon. The fee module allows portfolio managers to set fees that would be charged at rebalancing. Used Filecoin for deploying our UI via Fleek and AWS for storing and fetching data. And using ZK-EVM for privacy components of our blockchain. Challenges we ran into Making the custom smart contract where managers can launch different portfolios with different constituents and allocations. Bringing the calculation with less slippage took some time, but at the end we were able to make it. In the future we might use 1inch to aggregate liquidity across multiple providers and minimize slippage further. Accomplishments that we're proud of Deployed our contract on Polygon mainnet , integrated with quick-swap, chainlink and implemented all the features we wanted. What we learned Quickswap integration was smooth ZK-proof working Fleek, AWS integration with data sets and UI What's next for Velvet.Capital We are adding yield farming integrations so that users will get additional yield on the assets in their portfolio (from lending, staking and liquidity provision) We are adding a strategy module that will allow to create automated portfolios that are rebalanced according to pre-set parameters (regular timeframe, thresholds and triggers) We are working on an SDK to provide DeFI-as-a-Service for institutional clients (e.g., Asset Managers) which will use our protocol to create new products for their clients We will be conducting security audit and officially launching on Polygon shortly after the hackathon <div