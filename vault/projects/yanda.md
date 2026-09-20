---
slug: "yanda"
url: "https://devpost.com/software/yanda"
title: "Yanda"
hackathon: "Celo's Make Crypto Mobile Hackathon"
organization: "Celo"
winner: true
words: 472
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Yanda

> Automated Crypto Trading connected to CELO to guarantee transparency and safety to traders.

[Devpost](https://devpost.com/software/yanda) · hackathon [[Celo-s Make Crypto Mobile Hackathon]]

## Facets

**substrate** [[financial_record]] [[video_visual]]

**stack** javascript, kubernetes, python, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for yanda

## Body

Yanda Cover Inspiration After 2 years of Yanda offering automated trading software via API keys, the team realised that malicious brokers have multiple ways to access their users’ funds. We have thought that a decentralised solution would be beneficial for the entire automated trading industry. What it does We are building a protocol that lets Brokers, Validators and Traders share access to the automated trading data on-chain to prevent malicious attempts to traders’ funds. Traders start a service provided by a Broker and lock fees into a smart contract. The Broker executes transactions via CEXs and records them into the chain. Once the customer or the broker terminates the service, the validators receive a call to audit the transaction records. The contract collects validation results and if the majority of the votes from validators are positive, then the contract settles fees. Otherwise, the contract refunds the trader (excluding validation fees). How we built it We have developed the smart contract on ERC-20, the frontend is web3 ready, the validator app is ready as a docker image, and we integrated the smart contract interaction into the backend of the service provider (which is the automated trading software of Yanda). Challenges we ran into Scaling the team is difficult, we have had an open position for a month and we only got one application for the job. Accomplishments that we're proud of We won the Startup Pathway by Celo Camp - Batch 2; have started testing the protocol on Alfajores; raised pre-seed funds to build the protocol. What we learned We have learned how to scale in DeFi, and improved our knowledge of solidity. What's next for Yanda The team at Yanda is in the process of testing and collecting data and feedback from our community; working on the Governance Token; and about to start the implementation of the tokenization of trading bots created by the community as NFTs. Anyone who creates a trading bot with a unique logic is a creator. Creators are the initial owners of the NFTs corresponding to their creations (trading bots). To become a creator, a trader must have an MVP of its trading bot ready and a deck explaining the bot. The deck and the MVP get evaluated by the Yanda Creator Program to understand if the bot can fit the ecosystem. If the trading bot passes the initial screening, its creator can submit it for a vote to be listed on Yanda from the community. If the community votes are 51%+ positive, then its trading bot gets the form of an NFT that allows the bot to be used by the Yanda community of traders. The NFT carries royalties. Every time the trading bot is used by the Yanda traders, the owner of the NFT will receive a percentage of the fee associated with the bot. <div