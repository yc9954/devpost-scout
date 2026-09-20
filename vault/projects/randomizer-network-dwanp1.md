---
slug: "randomizer-network-dwanp1"
url: "https://devpost.com/software/randomizer-network-dwanp1"
title: "Randomizer Network"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 341
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
---

# Randomizer Network

> The Randomizer Network mission is to abstract the complexity of Chainlink CCIP/VRF/Automation/Feed by creating a No-Code Dashboard that empowers web3 communities to deploy custom randomization events!

[Devpost](https://devpost.com/software/randomizer-network-dwanp1) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**substrate** [[financial_record]]

**stack** hardhat, nextjs, react, solidity, typechain, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for randomizer network

## Body

Inspiration Chainlink Hackathon Barcelona What it does User Interface (UI) for CCIP ERC20 tokens transfers across 7 different Ethereum Virtual Machine (EVM) blockchains. The current architecture works for both Mainnets and Testnets on the following chains: Ethereum, Polygon, Avalanche, Arbitrum, Binance, Optimism, and Coinbase. Users can send tokens to their addresses or optionally transfer to a different address, if they so desire, instead of their address. Users can pay transaction fees with one of 3 natively supported tokens either with the General Access Mode in which the UI talks directly to CCIP Router Contracts on their respective chains or for the Early Access Mode which has a whitelisted smart contract that acts as a middleware between the UI and the CCIP Routers! How we built it Typescript + NextJS + React + Tailwind + Hardhat + Solidity Challenges we ran into The platform was built using Typescript, NextJS, React, and Tailwind. A significant update was made by switching from NextJS V12 to NextJS V13.5.6 and from Blocknative Onboard to Wallet Connect Web3Modal V3, which supports over 350 wallets. A lot of work went into getting the architecture right for both CCIP GA + PB! Accomplishments that we're proud of CCIP UI for General Access + Early Access Built a lot of architecture to support 7 blockchains and utility functions to query data between the 7 EVM Chains and 7 Tokens for CCIP which we are slowing aiming to turn it into a multi-token UI and we want it to become the standard CCIP ERC20 Frontend Boilerplate! What we learned How CCIP works in both General Access and Early Access, what are our limitations and how we can extend the UI to support Multi-Token CCIP transactions! What's next for Randomizer Network Future plans for the Randomizer Network include: adding multi-token capabilities incorporating optional message feature enabling transactions with up to five tokens across any of the seven EVM chains! refactor state to be more globally accessible by specialized components eliminate any device specific errors + memory leaks UI improvements improve speed <div