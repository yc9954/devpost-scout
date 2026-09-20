---
slug: "erc-4626-curve-cryptoswap-pool"
url: "https://devpost.com/software/erc-4626-curve-cryptoswap-pool"
title: "ERC-4626 Curve CryptoSwap Pool"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 160
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
---

# ERC-4626 Curve CryptoSwap Pool

> Composable interest-bearing token swaps on Curve V2

[Devpost](https://devpost.com/software/erc-4626-curve-cryptoswap-pool) · hackathon [[EthCC Hack 2022]]

## Facets


**stack** apeworx, curve, python, titanoboa, vyper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for erc-4626 curve cryptoswap pool

## Body

Inspiration Curve V2 (Cryptoswap) is a new AMM that auto concentrates liquidity around the current price to maximize capital efficiency and allows users to swap between uncorrelated assets, such as ETH to USDC. However, the Curve V2 AMM is currently unable to effectively swap between alternate interest-bearing tokens such as a WETH to yUSDC What it does Yearn/Aave/Compound/etc. interest bearing tokens can be wrapped in the ERC-4626 standard to be made composable with the Curve pool. How we built it Adapt CryptoSwap to work with the ERC-4626 standard, a new token standard for interest bearing tokens. Challenges we ran into Had some challenges in working with new technology such as titanoboa. Accomplishments that we're proud of We're proud of how much we accomplished during a short period of time. What we learned Learned more about the ERC-4626 standard. What's next for ERC-4626 Curve CryptoSwap Pool We hope this can be used by traders and liquidity providers on Curve V2. <div