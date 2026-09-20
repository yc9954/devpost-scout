---
slug: "solidroid"
url: "https://devpost.com/software/solidroid"
title: "soliDroid"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 402
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/developer"
  - "substrate/financial_record"
---

# soliDroid

> A platform that allows users to create, configure and operate a trading bot on the blockchain

[Devpost](https://devpost.com/software/solidroid) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** hardhat, node.js, solidity, typescript, visual-studio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for solidroid

## Body

soliDroid Inspiration After years of building trading bots (for centralized exchanges) in the crypto currency space, we now want to make on-chain algo-trading accessible also to anyone with a wallet address using the SoliDroid platform. What it does The SoliDroid platform allows end users to create, configure and operate a personal bot. Every bot belongs to its owner and only the owner can update configuration, buy, sell, withdraw funds or transfer the ownership of the bot (droid) to another wallet address. A web application providing the user all the online and historical information regarding its bot positions and transactions. And also let the user interact with the bot in real time. How we built it We build the business logic using Solidity on EVM and the web UI using React js and blockchain api libraries such as ethers, Moralis. We also build a backend server that query the blockchain for smart contracts events and other elements to enrich the UI. Challenges we ran into Except for the fact that our team is in different time zones, 12 hours apart. Every day of this Hackathon was a new challenge. Some remarkable challenges include: gas consumption, using DEX's API on different networks, invoking the bot periodically, doing accurate mathematical calculations using Solidity and TypeScript. And building a full React js application in a very short time. Accomplishments that we're proud of We manage to create a robust back-end on a blockchain and a rich UI in a very short time. Watching the Bot open and close positions on the blockchain makes the effort worthwhile. In the beginning of this project we were skeptical if it's even possible. What we learned First of all we learned to use Solidity to develop blockchain applications, we learned how to use many tools that are new to us. We learn how to integrate with ChainLink and Uniswap API, with Node providers and 3rd party libraries. In general we feel we learned so much in less than 4 weeks that now we are ready for a career change. From non blockchain programmers to blockchain programmers. What's next for soliDroid Is just the beginning for SoliDroid. We are planning to add support for technical analysis indicators. complex buy and sell roles. Bots that can be configured for yield farming. And to allow multiple bots per address. We have so many plans, and almost any day brings a new idea. <div