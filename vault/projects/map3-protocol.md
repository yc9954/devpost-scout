---
slug: "map3-protocol"
url: "https://devpost.com/software/map3-protocol"
title: "Map3 Protocol"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 471
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Map3 Protocol

> Map3 helps users locate crypto friendly businesses near them, and encourages vendors to automatically accept crypto payments in their preferred currency.

[Devpost](https://devpost.com/software/map3-protocol) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]] [[geospatial]]

**stack** api, evm, javascript, json, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for map3 protocol

## Body

Inspiration I was inspired to build map3 after realizing Cryptocurrency users (like me) have no way of finding local businesses that accept cryptocurrency. I believe Map3 is an essential tool in promoting and adopting Defi and cryptocurrency What it does Map3 is a web Dapp that helps users find businesses that accept cryptocurrency payments, While Map3Pay uses outsourced defi liquidity to mitigate p2p cryptocurrency payments, giving the sender and recipient the flexibility to decide what currency they prefer. Map3 Vendor Account manager is a registry that keeps track of data provided my different vendors. The data specifies their preferred currency, physical store address, contact and other relevant info that a potential customer would look for in a map Map3 P2P contract Supplements the account manager by taking care of all the necessary swaps to ensure the receiving vendor gets the currency they want. This means the end users/customers do not need to perform multiple swaps and convert their tokens to fiat just to complete one transaction with a vendor. Vendors are also encouraged to onboard and accept cryptocurrency since they can choose to receive all their earnings in stable/ less volatile currencies. How we built it . Essentially, all accounts are nonfungible tokens so metadata are created and uploaded to ipfs through web3 storage when users sign up. Map3 P2p Pay Contract bundles all the necessary swaps and transactions required to make payments and settles it on chain by. with the help of on-chain market makers like uniswap , 0x protocol, and the onchain Wrapped Matic contracts, Map3 pay can sell, buy and transfer the required amount of different erc20 tokens to between the end users. Challenges we ran into The biggest challenge and learning point was being able to construct meta transactions. it was essential to construct transactions into bytecode on the server for security and cross-scripting concerns. Map3 and map3 pay are now fully functional as just server-side applications, which means anyone can submit and settle the transactions generated if they have the required funds. Accomplishments that we're proud of Thanks to this Hackathon I was motivated to take my idea from conception to execution. I am proud and happy to solve my own problem and build a tool that encourages the fast adoption of cryptocurrency by vendors and businesses. What we learned I learned that it is hard to support every single currency since most currencies are not fully erc20 compliant, and it is also hard to find a good complete source for erc20 token icons !!! What's next for Map3 Protocol I hope to put map3 in front of more users and create more awareness. I also call it map3 Protocol and not just Map3 because these are the first two of many more tools I will build to improve and encourage cryptocurrency adoption in Chicago. <div