---
slug: "velvet-capital-gnz50d"
url: "https://devpost.com/software/velvet-capital-gnz50d"
title: "Velvet"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 262
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Velvet

> We help people create and manage index funds & other structured products on chain

[Devpost](https://devpost.com/software/velvet-capital-gnz50d) · hackathon [[EthCC Hack 2022]]

## Facets


**stack** hardhat, javascript, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for velvet

## Body

Inspiration Even professional investors fall victims to concentration risk, chasing yields and getting burnt when the price of the underlying asset tanks to zero. Diversification is a simple answer, we see diversified index funds being the most popular product in traditional finance and believe that it's much needed in DeFi. What it does Velvet helps you create tokenized index funds across a diversified set of assets constructed based on clear strategies (e.g., top by market cap) How we built it Our solution is multichain agnostic. We have used Polygon, Gnosis, Cronos, and Celo chain for the deployment of our solution. We wrote a solidity contract and tried to deploy on EVM chains. We have used different liquidity providers and 1inch for API for the swap. We have also used Gnosis multisig wallet for the storage of funds. Details of our deployed address can be found at our Readme https://github.com/Velvet-Capital/Velvet-contract/blob/main/README.md Challenges we ran into Some functions were missing on Celo Ubeswap contract, it took time to get it up and running. xDai liquidity is not widely available, that's why we had to use bridges. Integration with Neon took longer than expected due to extra integration with Wormhole. Accomplishments that we're proud of Integrations with multiple chains (Polygon, Gnosis, Cronos, Celo) and 1inch liquidity. Use of Privy to store the data Use of Neon solution for EVM to solana chain What we learned Bridging from EVM to non-EVM chains. Privy : A new stack for storage of data What's next for Velvet Apply for grants Get contract audit done Release product on mainnet <div