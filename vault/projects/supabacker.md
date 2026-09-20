---
slug: "supabacker"
url: "https://devpost.com/software/supabacker"
title: "Supabacker"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 330
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
---

# Supabacker

> Decentralized Fund Marketplace - support the things you care about. Supabacker grant model restores trust in the funding process and rewards donors with utilities like NFT or special content

[Devpost](https://devpost.com/software/supabacker) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

**mechanism** [[revocation_withdrawal]]
  <sub>weak: cross_origin_web</sub>

**stack** hashpack, hedera, ipfs, nft.storage, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for supabacker

## Body

Supabacker Landing Backer-first platform Main page Create project Detail project page Inspiration Patreon, Kickstarter, Gitcoin, DeFi What it does Its like Kickstarter for social goods and creators. But decentralized and can be launched with just an idea, like a DAO You can launch a Supabacker Project within minutes, instead of weeks or even months. Get support from backers without bureaucracy The Supabacker grant model restores trust in the funding process, fosters participation, and rewards donors with utilities like NFT, private Discord channels, exclusive merch drops and unreleased content. Artifacts provide an added incentive for donation, proof of support, and the missing sense of ownership and collective responsibility for our public goods Its Backer oriented : You can stake your money and then platform will share rewards from it to most beloved projects, also we provide an opportunity of withdrawal of funds from the project How we built it First we brainstormed the mechanics and the idea, then we sketched the design in Figma. The frontend is developed with React.js. We store basic information on ipfs using nft.storage. And only the ipfs link is written to the smart contract. Smart contracts are written in solidity with hardhat. Smart contracts are deployed on Hedera smart contract service Challenges we ran into Interaction between the frontend and smart contracts. Technologies like hethers.js, hashpack and Hedera smart contract service are still developing. There are also not many DeFi tools in the ecosystem. Like, for example, yield farming Accomplishments that we're proud of We have built a working platform that we believe can become a standard decentralized funding marketplace on Hedera Network What we learned That Hedera has a smart contract service and it's fast, it has room to grow. About the problems in traditional fundraising and how fast & secure blockchain can solve them. How to interact with smart contracts on Hedera What's next for Supabacker In the future, we plan to launch on the mainnet, launch DAO and members only communities feature <div