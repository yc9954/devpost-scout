---
slug: "sister-dao"
url: "https://devpost.com/software/sister-dao"
title: "Sister DAO"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 325
team_size: 4
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/civic_government"
---

# Sister DAO

> This project is based on the discussion about the Paladin tokenomics and aims to create a sub DAO associated with the main one, which is compatible with the model proposed on the forum.

[Devpost](https://devpost.com/software/sister-dao) · hackathon [[EthCC Hack 2022]]

## Facets

**domain** [[civic_government]]
  <sub>weak: geospatial</sub>

**stack** hardhat, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sister dao

## Body

Work Map Inspiration This project is based on the current discussion about the New Paladin tokenomics 2.0 and aims to create a DAO associated with the Paladin one, which is compatible with the current model proposed. What it does The sister DAO will receive a part of the Paladin ecosystem revenues (Defined by the governance) to accumulate governance power by locking whitelisted tokens, which can either be used by holders to vote on their favorite pools/gauges or to optimize their yield by selling the voting and boosting power. The sister DAO will receive earnings from two different sources: A defined % of all revenues sent from the revenue splitter to the SC controlled by the Msig A chest accumulating chTokens, which can be redeemed without penalty and sent to the SC because of the growing locked hpal position. How we built it A multisig receiving locked tokens has been created, which will be admin of the revenue fletcher and of a smart contract managing several vaults. The vaults will be different depending on the asset, as they don’t have the same design. Sister DAO contract functions: Add vault Send single tokens to the vault Send all tokens to all vaults The revenues from the sister DAO will be sent to the rewarder contract where users will be able to claim everything. Challenges we ran into We tried to fork the mainnet but we had some difficulties by lack of experience. We also had some trouble interracting with smarts contracts not familiar to us. Accomplishments that we're proud of Fork mainnet, MVP of the vaults, the rewarder and the sister DAO contract. What we learned How to imagine the project from scratch to a MVP, Deliver projects under deadline What's next for Sister DAO Wait for Paladin tokenomics, finish all the code of the products, work on the tokenomics of the sister dao tokens, work on a front end and try to integrate other DAOs <div