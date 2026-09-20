---
slug: "adamfo-protocol"
url: "https://devpost.com/software/adamfo-protocol"
title: "Adamfo Protocol"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 393
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/sensor_telemetry"
---

# Adamfo Protocol

> Adamfo Protocol: peer-to-pool wallet. Lets you ‘be your own bank,’ empowering you to interact autonomously and take back control of your group expenses, lending and settlement.

[Devpost](https://devpost.com/software/adamfo-protocol) · hackathon [[EthCC Hack 2022]]

## Facets

**domain** [[finance_payments]]
**substrate** [[sensor_telemetry]]

**stack** graphprotocol, hardhat, javascript, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for adamfo protocol

## Body

Inspiration In our case we have community peer-to-pool wallet which enables the user to settle expenses or providing uncollateralized lending to group members. Adamfo Protocol enables people to construct independent digital economies and regain ownership of their assets. It's a decentralized social network that allows Orbis protocol communication (tbd) Additionally the pool keeps track of metrics like how fast a debit has been paid back to the pool and - The pool also tracks how quickly a debt is repaid and who bought a collatoral from another member. This enables soulbound credit scores per participant which can be aggregated per pool. If a member wishes to collect his credit token from the communal wallet but it doesn't have enough cash, member A may sell this ERC1155 to B and be compensated, and B subsequently receives this credit token. What it does Users must register their wallet, once completed, the user gets an access membership token, which enables the member to interact with the communal wallet. Use Case 1: all participants pay equal amount of expenses in three consequtive sequences. user A submitts an expense USD 300 which involves user A, B and C A has credit token USD 200 B has debt token of USD 100 C has debt token of USD 100 user B submitts an expense USD 300 which involves user A, B and C A has credit token of USD 100 B has credit token USD 100 C has debt token of USD 200 user C submitts an expense USD 300 which involves user A,B and C A has credit token of USD 0 B has credit token of USD 0 C has debt token of USD 0 How we built it It was made with Solidty, Assembly Script for the subgraph, JavaScript/TypeScript/React for the frontend and Hardhat as a develpment platform. Challenges we ran into Creating a simple and smartcontract was quiet challenging at times We did not found time to integrate with Orbis Protocol The smart contract is ready for IPFS/FileCoin integration but it is not done in the frontend/subgraph Accomplishments that we're proud of Frontend Smart Contract Deployed on Gnosis Chain, Celo and Polygon What we learned Creating a MVP is not that easy as it appears What's next for Adamfo Protocol Polish frontend Integrating with Orbis Integration of IPFS Testing within our friends and family <div