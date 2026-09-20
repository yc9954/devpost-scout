---
slug: "crypto-recycling-machine-875ahf"
url: "https://devpost.com/software/crypto-recycling-machine-875ahf"
title: "Crypto Recycling Machine"
hackathon: "Celo's Make Crypto Mobile Hackathon"
organization: "Celo"
winner: true
words: 232
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
---

# Crypto Recycling Machine

> Crypto Recycling Machine is a project developed for Celo Make Crypto Mobile Hackathon. It gives an opportunity to recycle different kinds of bottles and get paid in crypto currency.

[Devpost](https://devpost.com/software/crypto-recycling-machine-875ahf) · hackathon [[Celo-s Make Crypto Mobile Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[finance_payments]]

**stack** celo, docker, node.js, react, remix, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for crypto recycling machine

## Body

The whole "machine" UI - home screen UI - payment option screen Raspberry Pi emulator Inspiration Bring together recycling and crypto. What it does Crypto Recycling Machine is a project developed for Celo Make Crypto Mobile Hackathon. It gives an opportunity to recycle different kinds of bottles and get paid in crypto currency. The project consists of 2 units: Recycling Machine Emulator A service running on Raspberry Pi which uses a breadboard, some LEDs and buttons to simulate inserting the bottle into the recycling machine. Each button on the breadboard represents an inserting different kind of bottle: aluminium cans, glass bottles, tetra pak, or PET. Recycling Machine server and client Used for user interaction with the machine and interaction between the recycling machine and smart contracts on Celo network. The Recycling Machine supports payments on Celo Alfajores network in CELO or cUSD tokens. There is also an option to donate the money. It uses Binance API to fetch the CELO token price. How we built it Technologies React Node.js Solidity Docker Project developed with Celo Remix IDE What's next for Crypto Recycling Machine Implement a back office web3 app, which will be used to manage the recycling machine contracts. It will allow administrator to deploy a new Recycling Machine contracts, manage existing ones and follow theirs statistics. For example, admin could see the balance, total amount donated, number of payouts, etc. <div