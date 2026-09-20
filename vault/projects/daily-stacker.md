---
slug: "daily-stacker"
url: "https://devpost.com/software/daily-stacker"
title: "Daily Stacker"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 575
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Daily Stacker

> Waking up to a little bit more crypto in your wallet is a great feeling. Daily Stacker wakes up before you do and buys you a little slice of your favourite tokens and sends them to your wallet.

[Devpost](https://devpost.com/software/daily-stacker) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets


**stack** chainlink, hardhat, javascript, scaffold-eth, solidity

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i've learned
- what's next for daily stacker

## Body

Waking up to a little bit more crypto in your wallet is a great feeling. Daily Stacker wakes up before you do and buys you a little slice of your favourite tokens and sends them to your wallet. Inspiration I've always enjoyed teaching crypto to newbie nocoiners. Getting them setup with centralised exchange account and getting them to buy their first sliver of Bitcoin. Alongside that I've always explained that Dollar-cost-averaging (DCA) combined with HODLing has been proven time and time again to be the best and simplest investment strategy to adopt. Don't try and time the market, don't try and catch the dips. Just buy at set intervals - daily, weekly, or monthly. Daily Stacker takes DCA to a new level. Waking up everyday owning a little bit more crypto is a nice feeling and Daily Stacker helps achieve that. Daily Stacker first came to life as a Raspberry Pi project called SatStacker . SatStacker still runs today and buys my crypto. However I collected a lot of feedback from people asking if they could have a solution that they could run themselves without hardware. Part of the problem to solve had to include to be the management of private keys or API keys and I don't want to be responsible for other people's keys. The combination of EVM smart contracts, L2 chains, Chainlink, and gas cost-optimised DEXes such as SushiSwap + Bentobox offered a solution. What it does Here's how Daily Stacker works: connect your wallet and once a month transfer some DAI to Daily Stacker, say 300 DAI. setup a portfolio, e.g. 50% Wrapped Bitcoin, 35% LINK, 15% BAT for the next 30 days Daily Stacker will buy slivers of the tokens according to the ratios in your portfolio all purchases are automatically sent to your wallet How I built it Scaffold-Eth has been a brilliant tool that has allowed the design to emerge, by first allowing me to play around and model some basic contracts. Automate the development through testing and finally to build a DAPP UI on top that included all the necessary wallet hooks. Bill of materials: Scaffold-Eth (React, Hardhat, Ethers) Chainlink Keepers SushiSwap BentoBox (still to be done) Polygon (still to be done) Ramp Network for fiat onramp (still to be done) Challenges I ran into Learning Solidity (after many previous false starts) Dealing with the peculiarities of ERC-20 tokes (approval workflows) Accomplishments that I'm proud of Learning Solidity and getting a least a fair bit along the way to project completion. At the ripe old age of almost 50, joined my first hackathon. Old dog, new tricks. What I've learned EVM platforms are massive environment to innovate on. Solidity itself is reasonably easy to learn, however running smart contracts on the blockchain is hard. The ERC-20 Approval pattern is often a stumbling block. Chainlink Keepers are awesome. Team up with people. You can't do it all. What's next for Daily Stacker Deploy to Polygon and other L2s for cheaper gas costs but that depends on the availability of Chainlink Keepers support on those chains. Update: Keepers are now available on Polygon. I'd like integrate something like ramp.network to provide a fiat onramp straight into Daily Stacker Improve the UI. Develop a mechanism whereby the protocol buys the LINK token to support itself, paid for by the users of the protocol. Integrate yield-generating protocols that will earn a yield whilst the funds are staked but not spent. <div