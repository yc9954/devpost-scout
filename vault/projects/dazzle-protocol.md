---
slug: "dazzle-protocol"
url: "https://devpost.com/software/dazzle-protocol"
title: "Dazzle Protocol"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 450
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
---

# Dazzle Protocol

> An easy first step into DeFi

[Devpost](https://devpost.com/software/dazzle-protocol) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

**substrate** [[financial_record]]

**stack** hashpack, hedera, node.js, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dazzle protocol

## Body

Inspiration According to studies, by December 2021 there were 80 million Blockchain wallet users worldwide and that is equivalent to only 1% of the world population. In countries like Venezuela or Argentina, where the stability of the local currency is low due to extraordinary economic situations, it is where the adoption of cryptocurrencies is most observed, specifically in situations where people send their relatives money for various expenses or want to protect themselves from the strong effects of the inflation by exchanging the local currency for dollar-pegged stablecoins such as USDC, however, what about those who do not have virtual wallets? How many steps do they need to take to create one and add funds to it? Taking into account that in the first handling it should be: Safe, practical and fast. What it does Dazzle is a dApp that allows you to send tokens and NFT's to anyone (Yes, anyone) through a simple LINK. How we built it Dazzle's base architecture is made up of three parts: a frontend developed with ReactJS, in the backend we have an API with ExpressJS and the Smart Contract is made in Solidity and deployed in the Hedera blockchain. For the interaction with the user's wallet, the hashconnect library was used, which allows creating and authorizing transactions in Hashpack, here we found a limitation of the library that did not allow us to successfully execute the functions of the smart contract from the client, so said interactions were handled in the backend. Challenges we ran into The initial architecture was designed to use NextJS together with Hashconnect to make calls to the smart contract directly from the client, but a couple of issues arose when using this combination of libraries, firstly because of the way NextJS compiled the modules in the frontend, it couldn't be integrated with Hashconnect so ReactJS standalone was chosen as an alternative and then the interaction between the client and the smart contract through Hashgraph and Hashconnect was not successful so that logic was placed in the backend to be able to sign the transactions without exposing any private keys. Something that should be noted is the completeness of the existing documentation for Hedera and Hashgraph. Accomplishments that we're proud of Model an easy and accessible gateway to the DeFi ecosystem What we learned How easy it is to deploy a smart contract in Hedera using Solidity. The interaction with the Token Service through Hashgraph that allowed us to create Tokens and NFTs. The Hedera blockchain is at an early stage in terms of the dApp ecosystem. What's next for Dazzle Protocol Improve the smart contract and add more functionalities on it Deploy on Hedera mainnet Go multichain <div