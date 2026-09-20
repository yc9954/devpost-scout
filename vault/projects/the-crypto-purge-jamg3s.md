---
slug: "the-crypto-purge-jamg3s"
url: "https://devpost.com/software/the-crypto-purge-jamg3s"
title: "The Crypto Purge"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 519
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/supply_logistics"
  - "substrate/video_visual"
---

# The Crypto Purge

> A real-time game & NFT Marketplace where players can play The Purge with crypto in a totally safe and transparent environment thanks to the Blockchain, and the winners receive the prize for each game!

[Devpost](https://devpost.com/software/the-crypto-purge-jamg3s) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[supply_logistics]]
**substrate** [[video_visual]]
  <sub>weak: code_repository</sub>

**stack** alchemyapi, blockchain, canvas, chainlink, css3, ethers, express.js, github, hardhat, heroku, html5, javascript, phaser.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the crypto purge

## Body

The Crypto Purge Metamask Wallet Home page NFT Collection Repository The Crypto Purge Game The Crypto Purge 💸 The most revolutionary crypto shooter-survival real-time NFT-based game on Binance Smart Chain . Inspiration The Crypto Purge is a crypto shooter-survival real-time NFT-based game inspired by The Purge (an American dystopian action horror film) . What it does Players will have multiple modes to play the game, single and multiplayer . Single mode includes killing zombies and social ranking with friends for earn prizes, the top scorers on the leaderboard will split the prize pool grant. Multiplayer mode allows players to contribute a certain amount of tokens to the prize pool before each game and the prize pool is split by Smart Contracts and a Server Side authority between the winners of the game. The game allow users to mint custom skins with NFTs to be used in the game ( Chainlink VRF and Oracles to assign provably rare traits). Player will differ in appearance and style, but they will have no effect on the game mode. All players will have an equal change of winning the game. How we built it The Crypto Purge has a crypto integrated backend that runs on Binance Smart Chain . Smart contracts are responsible for prize pool redistribution and web3.js (Metamask, etc) takes care of the wallet connection. We built the app using ReactJS, Phaser Framework, Hardhat with Chainlink Oracles for smart contracts development and NodeJS with Express Framework using Socket.io for real-time connections. Challenges we ran into Creating a decentralized real-time game that requires a back-end connection using WebSockets is the most challenging part of the project, additionally because "don’t trust the player. Always assume the worst – that players will try to cheat" , so it requires an authority server to create a cheat-proof architecture as cheating players tends to drive the players away from the game, therefore the core problems are human nature and physics . Developing an authoritative server architecture introduce a whole new class of challenges; Client-Side Prediction , Server Reconciliation , Entity Interpolation , Lag Compensation dealing with networks and scaling the system itself. Accomplishments that we're proud of We're proud to have created the real-time connection of the game, creating the smart contracts of the platform and the base architecture of the project; front-end , back-end and the smart contracts development using Hardhat with Chainlink Oracles. What we learned We learned about Blockchain , Smart Contracts , NFTs , Chainlink Oracles , 2D Games with WebGL/Canvas using Frameworks like PhaserJS , Physics , Real-time connections with WebSockets , Crypto wallets and much more! What's next for The Crypto Purge Allow gamers to edit their profile. Open Marketplace to buy and mint custom skins. Allow gamers to mint weapons and other assets. Allow gamers to have an inventory. Add a better configuration for the monorepo and create a Docker image with the configuration to run the project anywhere. Use Microservices strategy for complex calculations and horizontal scaling, To infinity and beyond! Apply to Y-Combinator for funding. Share the end results and inspire others with Open Source contributions. <div