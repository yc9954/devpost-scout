---
slug: "hobbits-of-polygon"
url: "https://devpost.com/software/hobbits-of-polygon"
title: "Hobbits Of Polygon"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 513
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Hobbits Of Polygon

> Web3 based RPG game on polygon with algorithmic map/character attributes powered by chainlink VRF

[Devpost](https://devpost.com/software/hobbits-of-polygon) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**substrate** [[financial_record]] [[geospatial]]

**stack** chainlink, html5, node.js, phaser.js, polygon, solidity, truffle, web3

## How they structured the write-up

- what it does
- connect metamask wallet
- dungeon map
- forest map
- ice map
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hobbits of polygon

## Body

Game Architecture Ice Map Forest Map 1 Forest Map 2 Dungeon Map Hobbits Of Polygon Hobbits of polygon is web3 based RPG game with an algorithmic engine made using chainlink VRF on Polygon. About Project Help the Dwarf king to rebuild his homeland all made up of NFT. The game is built using phaser and solidity deployed on Polygon blockchain with help of truffle. There are multiple maps of the game each map sets different attributes of players and characters. The game engine and attributes such as Health, enemy damage, etc are set by an algorithmic engine using chainlink VRF exhibiting the powerful use case of VRF not just for randomness but as to set up a game's meta. Meta can be described as an advantage, the disadvantage of characters on a certain map, or against particular characters. (Example:- 1) water type pokemon are stronger against fire type but weeker against the grass-type pokemon and this even implies on the map which the pokemon are fighting), with respect to this scenario, the meta and backend logic is created with chainlink VRF on the Polygon POS network. Demo Video * https://www.youtube.com/watch?v=eqVygMZc9GY What it does 🎮 User connects the Metamask to the game. 🎮 User pays a certain amount of entry fees to the game. (During test phases the test gold tokens can be obtained by faucet). 🎮 User triggers the chainlink VRF logic setup by entering the game. 🎮 The VRF sets the characters attributes and a random map from the multiple options is chosen. 🎮 If users win the game by overcoming all the enemies and collecting all the chest of gold user is rewarded with a 2x bounty and NFT reward. 🎮 If users lose their hp lesser than zero he/she losses. Glimpse of the Game Connect MetaMask Wallet Dungeon Map Forest Map Ice Map How we built it We used phaser.js as a game engine. Ethers library to interact with the blockchain. truffle to deploy contracts on polygon chain. IPFS to store metadata of NFT. tiled to create game maps and vs code editor. Challenges we ran into It was difficult to set dynamic in-game attributes which we overcame by using VRF. Rinkeby chain was kinda slow which was disturbing the game flow which we overcame using polygon layer2 chain for faster transaction. properly parse the bigNumber obtained as a random number from Chainlink VRF to integer as a game object. Accomplishments that we're proud of We are proud that we were able to make an MVP for the project. We plan to continue to build on this and make a big project. Metaverse GameFi Play2Earn Game Rewards and off-chain storage What we learned Chainlink VRF implementation Minting and distribution on NFTs, Switching between multiple maps in the phaser game. What's next for Hobbits Of Polygon We are working on an escrow system so players can challenge one another. We are adding additional characters to the game which can be traded on the NFT marketplace. We have implemented the lobby using socket.io so people can feel it as a metaverse. <div