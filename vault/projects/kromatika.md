---
slug: "kromatika"
url: "https://devpost.com/software/kromatika"
title: "Kromatika"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 306
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
---

# Kromatika

> Next generation limit order DEX Trading, NO swap fees, NO price slippage.

[Devpost](https://devpost.com/software/kromatika) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**substrate** [[financial_record]]

**stack** cloudflare, github, react, solidity, truffle

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for kromatika

## Body

Placing limit orders Listing all limit orders Llimit orders view Chainlink upkeep configuration (Kovan) Inspiration Each time you do a Uniswap swap you are subject to swap fees and price slippage. On top of that, you have front-runner bots that make things worse for the traders. This is super painful, especially to high-volume traders. What it does Create a product that will change the way swaps are done. We call it next-get DeFI trading. Basically, we create Dapp + a crypto token that when used together you can do trading with NO Swap Fees, NO Front-Running Bots, NO Price Slippage. All of this is achieved by allowing limit orders on DEX, along with using an utility token for execution of those limit orders. How we built it Frontend DApp built with React, Solidity smart contracts deployed on mainnet, and we have utilized Chainlink Keepers decentralized smart contract automation, to execute the limit orders when the time comes. Challenges we ran into Automatic replenishment of Chainlink upkeeps with $LINK tokens. We have solved it by topping up upkeeps with LINK tokens automatically during the very same transaction of executing the limit orders. Also managed to implement batching of multiple limit orders execution within a single upkeep transaction. Accomplishments that we're proud of We manage to save traders quite a bit of money when doing swaps and prevent price-slippage for low-liquidity trades. What we learned We learned a lot on the technical side. UniswapV3 API, Chainlink Keepers, especially how Chainlink registry and network of nodes work and how we can scale up the Chainlink upkeeps for high limit order execution throughput. What's next for Kromatika For Kromatika first priority is going live with the solutions. There are a number of steps that need to happen before that: beta testing on Kovan network, security audit, marketing boost etc. <div