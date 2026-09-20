---
slug: "paylock"
url: "https://devpost.com/software/paylock"
title: "PayLock"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 314
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# PayLock

> Paypal/Interac-transfer for crypto

[Devpost](https://devpost.com/software/paylock) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** chainlinkpricefeeds, hardhat, nextjs, openzeppelindefender, react, solidity, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how i built it
- contract addresses
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for paylock

## Body

"Hello Everyone! & gm" Inspiration Everyone knows blockchain UX(User Experience) could be improved. My brother had accidentally sent a month's salary of USDC to the wrong exchange address, he wished it was easier getting back his funds. He mentioned if there was a Paypal/Interact-like interface where he could withdraw his funds. What it does Paylock charges 0.5% per transaction (capped at 50USD) determined on chain to allow users to create (Withdrawable) ERC20 payments and provides the ability to withdraw/redeem payments without paying gas. Users optionally could notify payment receiver user via text-message How I built it Front-end: React/Next.js frameworks and Tailwindcss. Deployed on Vercel. Back-end/Contract: Remix-IDE to develop and test Contracts. OpenZeppelin Defender Relayer to support gas-less payments. ChainLink Price Feed Oracles to determine fees per transaction. Contract Addresses Mumbai MinimalForwarder , PaylockAddress Goerli MinimalForwarder , PaylockAddress Challenges I ran into I had a tough time integrating OpenZeppelin Defender to relay transactions. I was able to integrate gasless functionality to support redeeming and withdrawing payments without paying gas fees. Determining maximum fees per transaction (0.5%) by calculating the USD value of the transaction and capping fees at 50USD in the contract. Creating a V1 in a relatively short period of time! Accomplishments that I'm proud of I implemented gasless functionality for withdrawing issued payments. I was able to build this platform during the period of the hackathon by myself. What I learned I learned alot about integrating Chainlink price feeds/OpenZeppelin Defender Relayer in my contracts. There is no floating point in Solidity. Ethereum addresses have 64 character hex string. I learned that TRON is very similar to EVM networks( i.e same contract code but deployment and interactions with contract is different) What's next for PayLock UI Payments table sorting + timestamps Add tooltips Functionality Multi-Payments End-to-end gasless interactions Add Contacts (Addresses Book) and Avatars Cross-Chain Transfers to support Tron (TRC20 transfers ) network <div