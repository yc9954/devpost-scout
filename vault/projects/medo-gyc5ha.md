---
slug: "medo-gyc5ha"
url: "https://devpost.com/software/medo-gyc5ha"
title: "MeDo"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 270
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/small_business"
---

# MeDo

> MeDo - is a decentralized freelance platform where users can post paid tasks and other users can earn Matic by executing those tasks.

[Devpost](https://devpost.com/software/medo-gyc5ha) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[finance_payments]]
**user** [[small_business]]

**stack** filecoin, hardhat, ipfs, javascript, react, solidity, spheron, web3.storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for medo

## Body

MeDo home page. MeDo add task page Submit result Upload to IPFS Inspiration The idea of MeDo is to ease the difficulties faced by freelancers nowadays such as unsurity about payments and high fees charged by middlemen. Blockchain can help by guaranteeing payments with help of smart contracts, providing security and an integrated payment system that can save time delays, and fees in cases of international payments and its decentralized nature mean there is no middleman. What it does The platform allows users to add paid tasks. Two types of tasks are supported: FCFS - the first user who applied will be set as an assignee, Author Selected - task author can select an executor e.g. by their ratings. Other users can apply and get paid by executing the tasks. Executors can upload results to IPFS (Filecoin Web3.storage) or provide a link to another source. The task author can rate the executor. How we built it The smart contract is built with Solidity and Hardhat. The frontend is built with React and deployed with Spheron Network using Filecoin/IPFS. Tasks results are stored on IPFS. Challenges we ran into The biggest challenges were to support different task types and corresponding flows/use cases and to solve build problems caused by some node modules and Vite incompatibility. Accomplishments that we're proud of Entire platform. What we learned Smart contract development in solidity. Smart contract testing and deployment with Hardhat. What's next for MeDo Add new features such as milestones, the ability for executors to rate authors, in-app notifications, change requests, reward negotiation, etc. Develop to the production-ready state and deployment to mainnet. <div