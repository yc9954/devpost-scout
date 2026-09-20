---
slug: "the-counter"
url: "https://devpost.com/software/the-counter"
title: "The counter"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 378
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/mental_health"
  - "substrate/financial_record"
---

# The counter

> Provides over-the-counter deals that fill the trust gap of the reciproctiy

[Devpost](https://devpost.com/software/the-counter) · hackathon [[EthCC Hack 2022]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[mental_health]]
**substrate** [[financial_record]]

**stack** apeworx, pytest, react, vyper

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the counter

## Body

Inspirational UI from a role playing game Inspiration Until now, an over-the-counter (OTC) deal must happen through two transactions and so requires trust between parties. That's what happened when a DAO offered me a reward on the Polygon chain. Since most of the liquidity for this reward token was on Ethereum, and to avoid each individual to bridge their rewards, the DAO offered to buy back the token on Polygon and to make by itself the bridge back operation. This buy back took place over the counter (OTC), in two transactions : I sent the reward to the DAO address The DAO sent me the token and the amount we agreed on As you can imagine, the few minutes that occurred between both of them were anxiety inducing for the 2nd transaction could never have happened. What it does Here is a smart contract and an UI to fill the trust gap with an atomic swap. An OTC smart contract is available to be deployed by one party which also registers their counterpart. They settle on the deal parameter by sending ERC20 tokens to a deposit function Once it is done they can each agree , otherwise cancel If any deposit or withdraw is made before the mutual agreement, the one already agreed is reset When a mutual agreement has been acknowledged, deposit are closed and the final withdrawAll can be made How we built it Smart contract written with Vyper Tested with Apeworx and pytest Truffle react box for the UI, not interactive for now it's only a scaffold Challenges we ran into Settle on the features Learn vyper Find how to deploy it on various chains Time Accomplishments that we're proud of Having a smart contract ready What we learned Vyper How to integrate various tools together The pattern about smart contract deployement by the end-user What's next for The counter Enchance the smart contract NatSpec Event logging Deposit several types of tokens with one call Add support for ERC721 and ERC1155 UI fashionned like in a Role Playing Game deal between two players. Include token transfer approval management Tokenomics Testnet deployements : Polygon, Gnosis, Cronos web3 authenticated chat rooms and private threads to bargain over the deals Make a Metamask snap out of it <div