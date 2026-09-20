---
slug: "coollink-crypto-jumper"
url: "https://devpost.com/software/coollink-crypto-jumper"
title: "Coollink - Crypto Jumper"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 500
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "substrate/video_visual"
---

# Coollink - Crypto Jumper

> A Chainlink inspired, NFT gated, multi-player 2D platformer game that uses a dedicated $COOL token with tokenomics to enhance gameplay and reward engagement.

[Devpost](https://devpost.com/software/coollink-crypto-jumper) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[civic_government]] [[finance_payments]]
**substrate** [[video_visual]]

**stack** chainlink, express.js, filecoin, heroku, ipfs, javascript, keepers, next.js, node.js, phaser.js, socket.io, solidity, typescript, websockets

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for coollink - crypto jumper

## Body

Home Screen Player Instructions Lava Level - Gameplay (Multiple Players) Girder Level - Gameplay What's Cool Screen Staking $COOL Tokens dialog Mint your NFT Screen Successful NFT Mint dialog Lava Level - Add Player To Game Lava Level Lava Level - Gameplay Girder Level - Gameplay Girder Level - Leaderboard Credits Screen Inspiration We were inspired by the potential to combine NFTs, tokenomics and engaging gameplay. We wanted to pragmatically blend web2 and the best of web3 technologies together into a cohesive experience. We also wanted to innovate in how Chainlink Keepers could be used in a non-traditional scenario in a game. What it does We've built a familiar web-based 2D multi-player platformer game that brings web3 capability to encourage and reward engagement. Before a player can play, they need to mint their own, unique and collectible Coollink NFT. Once minted they gain entry to the game. Each NFT mint yields a player a starting balance of 10 $COOL tokens. These tokens act as credits to play the game. A player stakes a number of their $COOL tokens to play the game. A single $COOL token permits playing one round of the game. If the player wins the round they receive all of the staked $COOL tokens from the other players in that round. A player's NFT also receives 10 $COOL tokens per hour via the power of Chainlink Keepers. The game runs on a continuous game loop, all controlled by Chainlink Keepers. Players add themselves to play the next game, play the game, view the outcome and leaderboard and repeat. How we built it The 2D platfomer game is written from scratch using the Phaser v3 library in Typescript. The main game loop and game state is controlled by Chainlink Keepers interacting with one of the three custom contracts. The contracts are currently running on the Polygon Testnet, Mumbai. The three custom contracts include a main game manager contract which delegates to an ERC-20 and ERC-721 compatible contracts for $COOL and NFT management respectively. The NFT collection is managed in a the ERC-721 compatible contract, with all metadata and images stored on Filecoin/IPFS. The multiplayer game play is coordinated by listening to contract events and using middleware to communicate to the connected player browser clients using websockets. Challenges we ran into It is not possible to expect Chainlink Keeper execution on an exact second by second cadence. We needed to expect that and code appropriately and defensibly. Good use of contract event listeners and websocket communications allows clients to display notifications to players to keep them aware of the current game state. This is was our first use of Phase game framework. Accomplishments that we're proud of Innovating with the use of Chainlink Keepers integration, and the elegant combination of NFT and custom tokenomics. The multiplayer aspect was a good addition and achievement. What we learned First use of Chainlink Keepers and Phaser game framework. What's next for Coollink - Crypto Jumper More levels, enhanced scalability, onto Mainnet. <div