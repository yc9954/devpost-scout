---
slug: "gweipump"
url: "https://devpost.com/software/gweipump"
title: "GweiPump"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 207
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/web_dom"
---

# GweiPump

> Robotic oil pump controlled by a fair price smart contract using WTI/USD and MATIC/USD. VockTails pumps random drinks using a robotic pump. Uses Chainlink: pricefeeds, keepers, API requests, VRFv2.

[Devpost](https://devpost.com/software/gweipump) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**substrate** [[web_dom]]

**stack** chainlink, filecoin, ipfs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gweipump

## Body

Inspiration GweiPump: -Unfair oil prices in 2022 VockTails: -Mystery Soda Vending Machine in Capitol Hill -Call of Duty: World at War: Shi No Numa: Random Drink Vending Machine Locations What it does Robotic oil pump controlled by a fair price smart contract using WTI/USD and MATIC/USD. Vocktails pours random drinks using a robotic pump. Uses Chainlink: pricefeeds, keepers, API requests, VRFv2. How we built it GitHub: https://github.com/GweiPump Smart contracts: Solidity, Hardhat, Solidity Coverage. Frontend: web3.js, HTML, CSS, Bootstrap, Fleek (Filecoin and IPFS hosting GitHub pages) Robotics: Raspberry Pi 4, Robotic Pump and electrical components, Mumbai Quicknode WSS endpoint, Golang (fast, hard to program), Geth library, Gobot library, Node.js (slow, easy to program for quick testing) Challenges we ran into Wiring the pump and making sure the hardware was working. Accomplishments that we're proud of Robotic pump is working with Golang GPIO control logic. What we learned Wiring up a robotic pump is difficult since you need to be careful you have the right hardware. What's next for GweiPump Chainlink pricefeed WTI/USD is not supported on Mumbai but on Ethererum Mainnet. Ideally two ways to get this instead of a regular JSON API that was used: -Universal Adapter (offline during this hackathon) -CCIP (still not available yet) <div