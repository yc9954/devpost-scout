---
slug: "dagl"
url: "https://devpost.com/software/dagl"
title: "DAGL"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 582
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/general_public"
  - "substrate/financial_record"
---

# DAGL

> Triple-Entry Accounting on the Hedera Distributed Ledger

[Devpost](https://devpost.com/software/dagl) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

**domain** [[civic_government]] [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** c#, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dagl

## Body

Inspiration The web is filled with platforms that facilitate multi-sided value-add market interactions among their members. Examples of such market-places abound and include everything from consumer-to-consumer dating, gaming, and ecommerce sites – to business-to-business supply-chain, exchange, and brokering web sites. Often the interactions that these platforms facilitate monetary value to flow between the members. Such transactions are managed by the platform on behalf of the members, and frequently provide the platform valuable revenue models in the form of transaction fees. By transacting on these platforms members are forced to trust that these platforms to maintain their current account balances. Consider for example an online game that allows players to make in-game purchases from each other. Such interactions require the game host to maintain a “wallet” for each player containing potentially large sums of monetary value. Players must trust the platform to: • Accurately and transparently maintain transaction records for all in-game exchanges of value between players, that clearly show all transaction details, including all transaction fees, taxes and other charges that are levied • Retain enough “reserves” at all times to allow players to exchange their monetary value for local currencies (i.e.; cash out) • Remit collected local taxes to regional governmental jurisdictions as appropriate • Not go out of busy taking their monetary value with them With recent geo-political events such as Canada deploying its Emergency Act to freeze illegal demonstrators’ bank assets, and the US-led NATO sanctions regime against Russia in response to its invasion of Ukraine, along with a general erosion in confidence in the world’s fiat currency system, customers of these platforms have begun to realize that trust is a fragile thing. Over the last several years with the coming of age of cryptocurrencies and their integration with distributed ledge technology (DLT), there is mounting interest to ensure that financial transactions on every level are performed in an efficient, secure, transparent and trustless way. While there is wide acknowledgement that internet services (i.e.; SaaS) provide real value and aren’t going anywhere anytime soon, customer are nonetheless beginning to demand that monetary transactions be conducted without counter party risk. As a result, competitive platforms who wish to earn the trust of their members in order to ensure customer loyalty are looking to see how they might incorporate cryptocurrencies and DLT to solve this problem. Unfortunately integrating DLT successfully within existing platforms is difficult, requiring scarce expertise. Therefore, an opportunity exists to provide existing multi-sided web businesses with a drop-in capability that fully decentralizes their proprietary platform accounting/payment systems that grows customer loyalty through trust by providing fast, reliable, secure, transparent and counter-party risk-free transactions to their members. What it does DAGL is a free software SDK and API that allows any enterprise, institution or government to "drop-in" "Post" capability for standard Generally Accepted Accounting Practices journal entries directly to a General Ledger on the Hedera distributed ledger. It natively supports triple-entry accounting to ensure the bookkeeping transactions of all stakeholders in a financial transaction are provably congruent. How we built it DAGL is written in Dot Net (C#) and utilizes the superb Hashgraph .NET SDK written by Jason Fabritz and available on Github to interface with the Hedera APIs. Shout out to Jason for his the amazing and timely support for his SDK! Challenges we ran into Time. Never enough. Accomplishments that we're proud of Getting it working! What we learned Solidity is not as bad as I had heard. What's next for DAGL Taking it to market! <div