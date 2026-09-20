---
slug: "crypto-recycling-machine"
url: "https://devpost.com/software/crypto-recycling-machine"
title: "Crypto Recycling Machine"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 309
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Crypto Recycling Machine

> A dapp which brings together recycling and defi. Crypto Recycling Machine gives you an opportunity to recycle plastic, aluminium and glass bottles, and get paid in crypto with multiple networks.

[Devpost](https://devpost.com/software/crypto-recycling-machine) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[revocation_withdrawal]] [[simulation_digital_twin]]
**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** chainlink, docker, hardhat, harmony, moralis, node.js, polygon, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for crypto recycling machine

## Body

The whole machine UI - Home screen UI - Payment Option screen Raspberry Pi emulator Backoffice app Inspiration Bring together recycling and crypto. What it does Crypto Recycling Machine is a project developed for Chainlink Hackathon. It gives an opportunity to recycle different kinds of bottles and get paid in crypto currency. The project consists of 3 units: Recycling Machine Emulator A service running on Raspberry Pi which uses a breadboard, some LEDs and buttons to simulate inserting the bottle into the recycling machine. Each button on the breadboard represents an inserting different kind of bottle: aluminium cans, glass bottles, tetra pak, or PET. Recycling Machine server and client Used for user interaction with the machine and interaction between the recycling machine and smart contracts on multiple networks. The Recycling Machine supports payments on Polygon Mumbai network in MATIC tokens and Harmony Testnet network in ONE tokens. There is also an option to donate the money. It uses Chainlink Data Feeds to determine the price of the tokens. Back office (Admin control panel) A Web3 app which is used to manage the recycling machine contracts. Allows administrator to deploy a new Recycling Machine contracts, manage existing ones and follow theirs statistics. For example, admin can see the balance, amount which needs to be donated, total amount donated, number of payouts, etc. There is an option to fund the machine account, withdrawal all the money, send the donation money to some charity address and list all the transactions from the particular machine contract. Developed using Moralis. How we built it Technologies used: React Node.js Solidity Docker Project developed with Chainlink price feeds Polygon network Harmony network Moralis (for the Admin control panel) Hardhat What's next for Crypto Recycling Machine To build a real Crypto Recycling Machine, which will accept the real bottles, so the many people can use it. <div