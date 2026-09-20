---
slug: "the-dungeon-flow-chainlink-hack-upgrades"
url: "https://devpost.com/software/the-dungeon-flow-chainlink-hack-upgrades"
title: "The Dungeon Flow - Chainlink Hack Upgrades"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 764
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# The Dungeon Flow - Chainlink Hack Upgrades

> An RPG (Role-Playing) story-based multicharacter game built on the Flow Blockchain, where the player has to collect loot from chests, defeat enemies and collect NFTs & shop for new game collectibles

[Devpost](https://devpost.com/software/the-dungeon-flow-chainlink-hack-upgrades) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[financial_record]] [[video_visual]]

**stack** aseprite, blocto, cadence, fcl, flow, javascript, node.js, phaser.js, react, webpack

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the dungeon flow - chainlink hack upgrades

## Body

Inspiration We grew up playing role-playing games where the importance of the characters, stories, and gear was paramount. Giving players a feeling of ownership and accomplishment is our primary objective. What it does Present web2 games currently do not offer real ownership and players are at the mercy of game providers and centralized servers. Steam has had a huge monetization market, however, a lot of assets purchased do not have a resale value. On the blockchain, players can own collectibles and their progress on-chain and partly off-chain, in their wallets, and NFTs make web3 games truly composable and open a wide variety of opportunities for partnerships & collabs Web3 games involve building around communities where the players have skin in the game, and it also includes audiences ranging from merry investors, speculators, and real players. Moreover, token economies using NFTs and fungible tokens make it possible to introduce different mechanisms like stake-battle and play, lending mechanisms, and various other opportunities. huge open market on which they can trade the game assets. Flow Blockchain provides mobile compatibility and it becomes easy to build games for mobile. An RPG game built on the Flow Blockchain, check the youtube video to view the demo. Signup using Blockto Wallet using your email to obtain an addresss Story-based gameplay, Player has to collect loot from the chests, and kill the guarding monsters who have different hit points, unlock the locked token gates to reach the Flow NFT collectible found at the End of the gameplay. Player has three lives and is minted 4 coins and an NFT for every every Chest collected, and also mints a non-fungible token to his Blocto wallet. How we built it Contract address Game NFT Contract deployed on Flow Testnet : 0x9f690718478ff417 Verify on Flow Testnet Verify testnet deployment on Flow-view-source Proposed Design Tech Stack PhaserJS React Flow fcl Blocto Wallet Aseprite Cadence programming language How to run ? In the project root: yarn && yarn start In blockchain/src/components/App.js , please verify the flow client library config fcl.config() .put("app.detail.title", "My Flow NFT DApp") .put("accessNode.api", "https://rest-testnet.onflow.org") .put("discovery.wallet", "https://fcl-discovery.onflow.org/testnet/authn") Block explorer: https://testnet.flowscan.org/ To deploy contract flow init flow accounts create Added the new account to flow.json. Saved the private key to test.pkey. Added test.pkey to .gitignore. Fund Wallet with TEST FLOW Tokens: https://testnet-faucet.onflow.org/fund-account flow accounts add-contract .cdc -n testnet --signer Screenshots Dashboard Challenges we ran into Building on Flow for the 2nd time after the inaugural flow hackathon, this time I dived deeper into Cadence, Flow Playground, Flow View Source, Flow CLI and also sought help from Jacob Tucker and Naser.find from the Emereald City DAO discord. Flow Testnet also had a major sporking event and the RPC was down. I also sought help on Flow Hackathon discord, to seek clarity on Secure Cadence programming after breaking changes were announced in the Cadence Codebase. Accomplishments that we're proud of Finally figured out to write my first contract in Cadence, and deploy it using Flow Playground on the emulator Later I used FLC (Flow Client Library) to deploy my own smart contract to the testnet using the entire software suite. Problems associated with minting Fungible tokens to the wallet while connecting chests and problem solving using React Designing sprite animations on Aseprite and understanding key concepts of Phaser for game development. Figured out Flow installation and CLI usage using tutorials from Learn Web3 DAO and BuildSpace tutorials, and integrated with the mini-game. I explored: Fungible Token Standards Non Fungible Token Standard Using FLOW token on testnet inside the dApp for the marketplace Vault contracts, user permissions, and marketplace contract setup Custom NFT contract using Non-Fungible Standard tutorial Built a basic UI with working features from the smart contract What we learned I understood better Flow blockchain architecture, the composability of smart contracts, and the concept of accounts and how all transactions are tied to a single account I also learnt, FT, NFT and derived smart contracts using interfaces on Cadence More experience with FCL and easy onboarding to applications with connections to wallets like Blocto. What's next for The Dungeon Flow - Chainlink Hack Upgrades Develop a mobile game on Unity with Flow Unity SDK More on-chain game logic using Flow-RPG contracts to allow building composability and upgrading characters on-chain. Allow players to create and upload their own storylines and characters to the platform with DAO token incentives Stake and Battle modes In game DEX on Flow Blockchain with Increment FI contracts .find integrations to allow users to send collectibles to players inside the game using their domain names. Collaborate with FlowVerse and Flow Games Team <div