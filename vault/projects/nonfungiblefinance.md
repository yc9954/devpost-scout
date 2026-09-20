---
slug: "nonfungiblefinance"
url: "https://devpost.com/software/nonfungiblefinance"
title: "NonFungibleFinance"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 196
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
---

# NonFungibleFinance

> NFTs the way to achieve true ownership onchain. Beyound the "JPEG" usecase, NonFungibleFinance is a project to build fundamental composable finance block, using the NFT standards for true ownership.

[Devpost](https://devpost.com/software/nonfungiblefinance) · hackathon [[EthCC Hack 2022]]

## Facets

**domain** [[finance_payments]]

**stack** ant, celo, cronos, ethers.js, gnosis, goerli, javascript, matic, neon, polygon, react, solidity, xdai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nonfungiblefinance

## Body

Inspiration A lot of onchain asset are owned but not easily transferable, or at least not in a standardized way. I believe that basic DeFi block, if designed properly and owned through standard interfaces, will be essential to the future of DeFi What it does During this hackathon, I focused on the building Non-fungible Vesting Vaults. I went that way because I fell vesting is one of the under appreciated and under developped components of DeFi How we built it A bit of solidity and a lot of React Challenges we ran into I wanted to target many chains, some of which don't have public thegraph services. I could not use this tool and had to fallback to raw events processing. Also, actually submitting the hack was a strugle :/ Accomplishments that we're proud of It works, and it doesn't look that bad. Also I support 6 chains already, and adding more is extremely easy. What we learned I discovered the "ant" framework. I also discovered quite a few EVM chains this weekend. What's next for NonFungibleFinance Adding more contracts type (payment splitters, account abstraction, ...) and making a more reactive & better looking UI. <div