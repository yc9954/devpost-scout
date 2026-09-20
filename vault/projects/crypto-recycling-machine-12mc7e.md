---
slug: "crypto-recycling-machine-12mc7e"
url: "https://devpost.com/software/crypto-recycling-machine-12mc7e"
title: "Crypto Recycling Machine"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 292
team_size: 0
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
---

# Crypto Recycling Machine

> Crypto Recycling Machine is a project developed for NEAR Metabuild Hackathon. It gives an opportunity to recycle different kinds of bottles and get paid in crypto currency.

[Devpost](https://devpost.com/software/crypto-recycling-machine-12mc7e) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[developer_tools]] [[finance_payments]]

**stack** docker, near, near-api-js, near-sdk, node.js, react, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for crypto recycling machine

## Body

Inspiration Crypto Recycling Machine is a project developed for Near Metabuild Hackathon. It gives an opportunity to recycle different kinds of bottles and get paid in crypto currency. You've probably seen a recycling machines or reverse vending machines that accepts bottles and rewards you with some coupons or tokens that you can spend later or get a refund for some product. So, our idea was to bring together recycling and crypto. We decided to make a recycling machine where you can put different kind of bottles, and get a reward in crypto currency, in this case in $NEAR tokens. Obviously, we don't poses this type of machine, so we made a Proof of Concept just to illustrate what we wanted to achieve. What it does The project consists of two units: Recycling Machine Emulator A service running on Raspberry Pi which uses a breadboard, some LEDs and buttons to simulate inserting the bottle into the recycling machine. Each button on the breadboard represents an inserting different kind of bottle: aluminium cans, glass bottles, tetra pak, or PET. Recycling Machine server and client Used for user interaction with the machine and interaction between the recycling machine and smart contracts on Near network. The Recycling Machine supports payments on NEAR testnet network in $NEAR tokens. There is also an option to donate the money. How we built it Technologies React Node.js Rust Docker Project developed with near-sdk near-api-js What's next for Crypto Recycling Machine Future work/TODO Implement a back office app, which will be used to manage the recycling machine contracts. It will allow administrator to deploy a new Recycling Machine contracts, manage existing ones and follow theirs statistics. For example, admin could see the balance, total amount donated, number of payouts, etc. <div