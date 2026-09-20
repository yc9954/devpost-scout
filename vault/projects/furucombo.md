---
slug: "furucombo"
url: "https://devpost.com/software/furucombo"
title: "Furucombo"
hackathon: "Fantom Hackathon Q1 2023"
organization: "Fantom Foundation"
winner: true
words: 451
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Furucombo

> Furucombo is a DeFi composability platform that allows users to perform position management, swaps, or sending tokens and execute it all within one transaction, including flash loans.

[Devpost](https://devpost.com/software/furucombo) · hackathon [[Fantom Hackathon Q1 2023]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]] [[web_dom]]

**stack** foundry, hardhat, solidity, typescript, vercal

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for furucombo

## Body

Inspiration Our inspiration was to create a tool that's useful to every DeFi user on Fantom. We were inspired by Fantom's ability to provide a good ecosystem for builders through their ecosystem vault and gas monetization. Dinngo loves the approach that Fantom has provided for us and other builders and were therefore inspired to build on the network to help to share in building a great product. We believe our product creates a unified interface for users to easily perform their trading actions, which makes it easy to learn and create complex combinations. Additionally, we are developing a robust SDK/API on the backend for builders to easily integrate. We want to create a cutting edge product that helps to elevate the Fantom ecosystem. What it does Furucombo is a DeFi aggregator platform developed by Dinngo that allows users to easily combine trading actions, and execute them into one transaction. We currently aggregate actions from Spookyswap, Geist, Paraswap, Curve, and Stargate to allow any trading actions to be chained together, and executed in one transaction. Additionally, it allows for combinations that otherwise wouldn't be possible, such as position management using Flash Loans. How we built it Our approach involves writing a smart contract that consolidates multiple actions into a single transaction, and designing a user-friendly website to enables users to interact with multiple projects. We use the Solidity language and Hardhat framework for writing the smart contracts, while the website is built with Typescript and React framework. Challenges we ran into Because of the uniqueness of Furucombo, it presents its own challenges in creating a proxy contract, and integrating in different protocols which each have their own security risk. This means its resource intensive, and requires implementation of custom contracts built from scratch. Accomplishments that we're proud of Because of the difficulties and challenges we've come across with building a unique platform, its created a team that's strong in developing custom contracts. We are very proud of what we've built, and are excited for what we continue to build for the blockchain ecosystem. What we learned We constructed it by leveraging Fantom's EVM-compatibility, which makes the process similar to that of Ethereum. Creating projects on Fantom utilizing the same framework and code base is a seamless process. Although there are some distinctions, such as fUSDT or Geist (a protocol similar to AAVE), they have been developed effectively. What's next for Furucombo The next step for Furucombo is to develop out a robust SDK/API, and allow protocols on Fantom to integrate and take advantage of our composability. We are also developing what we are calling the 'composable router' which will decrease the resources required for protocols on Fantom to integrate into Furucombo. <div