---
slug: "taxme"
url: "https://devpost.com/software/taxme"
title: "taxme"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 284
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# taxme

> As a company storing and sending sales taxes is cumbersome. We try to solve this by automatically storing the sales tax and sending to government periodically and other benefits

[Devpost](https://devpost.com/software/taxme) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[civic_government]] [[finance_payments]]
  <sub>weak: retail_commerce</sub>
**substrate** [[financial_record]]

**stack** chainlink, hardhat, moralis, nextjs, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for taxme

## Body

taxme dashboard: view tax collectors (owner can edit), view sales store demo checkout: pay with stablecoins Inspiration Companies are required to collect and transfer sales taxes to government, but taxes calculation is a complex flow, the capital needs to be parked in a checking account doing nothing plus the transfers to tax authorities might be missed easily. We can be automated this task with smart contracts: we calculate the exact taxes using third-party tax calculations apis, store them and send them at required schedules. As a bonus we can stake them until the required transfer. What it does When a client buys something online, the UI calls the smart contract's sale function, which gets the sales taxes percentages from a chainlink node and calculates the taxes. Then it charges the user with the correct amount, and passes to the store owner the funds after taxes. The taxes are stored in the smart contract which can be used for staking. A chainlink keeper transfers the taxes due to the predefined addresses for tax authorities, or the business owner withdraws them and send them manually. How we built it Blockend: solidity, chainlink node, chainlink keeper. Frontend: nextjs, moralis Challenges we ran into Solidity limitations on number of arguments solidity documentation Accomplishments that we're proud of chainlink node with adapter and keeper to update the taxes the sale and amount split works end-to-end display of transactions for easy review for business owners What we learned temper-proof taxes collection and processing in a transparent way What's next for taxme supporting US states and counties, currently we work with canadian provinces better accounting tools finishing the integration with chainlink keepers to withdraw taxes to tax collectors staking rewards <div