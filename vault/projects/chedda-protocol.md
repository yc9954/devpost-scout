---
slug: "chedda-protocol"
url: "https://devpost.com/software/chedda-protocol"
title: "Chedda Protocol"
hackathon: "Oasis Bloom Hackathon"
organization: "Oasis Foundation"
winner: true
words: 404
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
---

# Chedda Protocol

> Chedda is a multi-asset lending protocol with isolated vaults separated by risk profile, VE token mechanics and support for NFT collateralized loans.

[Devpost](https://devpost.com/software/chedda-protocol) · hackathon [[Oasis Bloom Hackathon]]

## Facets

**domain** [[civic_government]] [[finance_payments]]

**stack** ionic, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chedda protocol

## Body

Inspiration Chedda is a DeFi 2.0 lending protocol which brings together the best elements from AAVE, Curve, and Compound with a unique spin. What it does Chedda is a lending protocol with isolated lending pools, VE token mechanics and support for NFT collateralized loans. Users can deposit collateral to take out loans of asset tokens. Our isolated model means that we can have different pools with varying risk profiles, which which allows users to deposit high grade assets such as ETH, WBTC, USDC in "safer" pools, while more risky assets can be used as collateral in riskier pools. This design ensures that having one "bad" asset in one pool does not put the entire protocol at risk, as has been the case with many DeFi hacks. This design also allows us to offer pools where blue chip ERC-721 tokens can be used as collateral. Key Features Isolated lending pools - This is a less risky design as many hacks have been due to one risky asset being added to a lending pool and draining the entire protocol. With our design, riskier assets are isolated from less risky ones. Our lending pool vault is represented by an ERC-4626 token (standardized token vault) which makes it easily composable with other protocols. Stake CHEDDA to earn rewards - xCHEDDA is also an ERC4626 token - APR depending on staking rate. 10% if 100% of tokens are staked, 20% if 50% staking rate. - High APR without being hyper-inflationary. - Stake -> Pie grows over time -> Withdraw -> Lock for longer Governance through VE Token model - Vote on protocol token emission - Other governance votes will happen. We have voting on chain and on-site, not using 3rd party service. - Locking xCHEDDA for periods reduces any sell pressure on the underlying CHEDDA tokens. How we built it Blood, sweat and hard work! Challenges we ran into Creating a DeFi protocol from scratch is a complex endeavour. Finding product-market fit was always a challenge and we had to pivot a couple times to arrive at the product we have now. Accomplishments that we're proud of We implemented an original lending protocol from scratch which brings together the best elements from other protocols What we learned How to build a DeFi protocol that is in many ways superior to some of the leading protocols. What's next for Chedda Protocol Continued development Cross chain support Main net launch <div