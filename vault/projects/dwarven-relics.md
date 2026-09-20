---
slug: "dwarven-relics"
url: "https://devpost.com/software/dwarven-relics"
title: "Dwarven Relics"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 469
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/housing_homeless"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/structured_db"
---

# Dwarven Relics

> Dwarven Relics is a top-down browser-based web3-integrated real-time MMORPG where players must cooperate to fight back the foul creatures which have overrun the Dwarven Fortress of Dûnnbarg

[Devpost](https://devpost.com/software/dwarven-relics) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[housing_homeless]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** bootstrap, node.js, pixi.js, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- current status
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dwarven relics

## Body

Concept Art In Game Art In Game Art Character Creation Gameplay Inspiration My main inspiration for this game was Dwarf Fortress, an ASCII characters graphic game! What it does Dwarven Relics is a top-down browser-based MMORPG where players must cooperate to fight back the foul creatures which have overrun the dwarven fortress of Dûnnbarg. Dive into the depths of the fortress to scavenge the resources left by your folk's retreat and forge new equipment while searching for powerful relics lost in ancient times. Our goal is to provide a gaming experience with seamless NFT integration: we believe the ultimate goal for adoption to be making NFTs and DeFi an extra tool in your development stack and not the primary focus of a project! Current status The main features of the hackaton version of the game are: Character creation, PvP, Loot system, Inventory system, Physics engine. How we built it Using node.js backend, typescript / react / bootstrap / pixi.js frontend, solidity contracts, mongoDB database (with AWS deployment), spheron network frontend deployment (IPFS storage option). Challenges we ran into Me and my team had no previous experience in the logic behind MMO networking and we had come to a soft cap of concurrent users that we couldn't seem to surpass. This was quite the issue as we wanted the number to be a lot higher even on less powerful (and cheaper to rent) servers. After diving into Valve documentation about online games and other resources, I contacted a fellow developer that had been working on Hordes.io, a huge browser based MMORPG that I remembered playing with high concurrent player numbers. We got some tricks explained by him we where able to optimize the backend code to support 10x the past amount of players! This is a very fitting example of how we get over issues during development: I love to surround myself with more knowledgeable developers as I think its one of the best ways to improve my skills if I'm ever stuck in the development process. Accomplishments that we're proud of The amount of concurrent players possible (500-600 on low end spec server) and the fun you can have fighting other players. The blockchain integration featuring soulbound NFTs, the seamless integration with mintable items without needing to sync onchain every time you play (only need to mint when you want to trade your items on a DEX). What we learned To think hard about scaling solutions, how to use MongoDB Atlas cloud solutions, how to code GPU rendering using webGL with pixi.js, how to organize and interact between frontend, backend and blockchain for a real time MMO game. What's next for Dwarven Relics We will keep building it! Some of the next goals are to add monsters to fight, a marketplace dex for items and a crafting system. <div