---
slug: "dazzle-protocol-multichain"
url: "https://devpost.com/software/dazzle-protocol-multichain"
title: "Dazzle Protocol"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 441
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Dazzle Protocol

> The easy first step into DeFi

[Devpost](https://devpost.com/software/dazzle-protocol-multichain) · hackathon [[TRON Grand Hackathon 2022]]

## Facets


**stack** node.js, react, solidity, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dazzle protocol

## Body

Inspiration According to studies, by December 2021 there were 80 million Blockchain wallet users worldwide and that is equivalent to only 1% of the world population. In countries like Venezuela or Argentina, where the stability of the local currency is low due to extraordinary economic situations, it is where the adoption of cryptocurrencies is most observed, specifically in situations where people send their relatives money for various expenses or want to protect themselves from the strong effects of the inflation by exchanging the local currency for dollar-pegged stablecoins such as USDC, however, what about those who do not have virtual wallets? How many steps do they need to take to create one and add funds to it? Taking into account that in the first handling it should be: Safe, practical and fast. What it does Dazzle is a dApp that allows you to send tokens and NFT’s to anyone through a simple link, so you can onboard your friends into DeFi just by sending them a link via email or your favorite messaging app. With the Smartwallet feature users can get a wallet who is linked to a social account like Google, Facebook, Github, Twitter, etc. That's the only they need to send tokens, they can receive tokens in the Smartwallet too. At the moment only the Google authentication provider is enabled and is working with the Tron blockchain integration. How we built it Dazzle’s architecture is made up of three parts: the Smart Contracts for Dazzle Protocol and the Smartwallets which are made in Solidity and deployed over the Hedera network and Tron blockchain, the backend where we have an API with ExpressJS and the frontend made with ReactJS. For the interaction with the user’s wallet, Hashpack is used for the Hedera Network and TronLink is selected for Tron. Challenges we ran into We couldn't deploy the Smartwallet contract using the Clone Factory pattern, that pattern would allow us to save even more in fees when deploying a user's Smartwallet. As workaround we are using a regular contract deploy for them. Accomplishments that we're proud of Make a multichain deploy Model an easy and accessible gateway to the DeFi ecosystem. The Smartwallet is experimental and something that we are very excited to implement as direct and simple experiences at this level we believe are key to mass adoption. What we learned Smart contracts in Tron and interactions with TRC20 and TRC721 standards. Interactions between the dApp and the TronLink wallet. What's next for Dazzle Protocol Re-test the implementation of the Clone Factory pattern for the Smartwallets. Include a better fee calculation strategy for Smartwallet interactions. Deploy in more blockchains. <div