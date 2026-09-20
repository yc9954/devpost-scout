---
slug: "the-spacelink-metaverse"
url: "https://devpost.com/software/the-spacelink-metaverse"
title: "War Alpha Metaverse"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 454
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/supply_logistics"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# War Alpha Metaverse

> A Metaverse Space Shooting Game With Upgradable NFTs

[Devpost](https://devpost.com/software/the-spacelink-metaverse) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[agriculture_food]] [[supply_logistics]]
**substrate** [[code_repository]] [[financial_record]] [[video_visual]]

**stack** chainlink, ipfs, phaser.js, polygon, typescript, vrf

## How they structured the write-up

- war alpha metaverse

## Body

War Alpha Metaverse Demo video : https://youtu.be/jt2Og-RWD3Q Try it out now on https://WarAlphaMetaverse.com War Alpha Metaverse is a space shooting game with upgradable NFTs. Mint a random (VRF) spaceship to start with. Pilot it in the game and fight enemies! Harvest their parts. Upgrade your ship. Then sell your upgraded NFT. First, click "connect your wallet". Metamask opens to authorize the connection. If you are not already connected to the Matic Mumbai Testnet , Metamask will offer you to do so. The game will then fetch all your spaceship NFTs from the smart contract. If you do not yet have a War Alpha Metaverse NFT, click "Mint Random (VRF) Ship" and Metamask will open to trigger the mint. You will receive a new ship with random weapons, wings, engine, and cabin. The ship will appear in your list of ships (if not refresh the page). Select that ship to access the game. The game is built with PhaserJS, a 2D Javascript game engine that allows us to pilot our ship and fire at enemies. Use the directional arrows to move the ship and press the space bar to fire. Try to kill the enemy ship, but be careful not to get hit. When the enemy is destroyed, it drops some loot. Move your ship over it to get it into your inventory. Then open your inventory to see all the parts you have found. Drag and drop a ship part to its corresponding area on your ship to upgrade that part. A Matic transaction opens that will actually modify your NFT metadata and image with the new part. The smart contract is a modified ERC721 with a new endpoint to modify an NFT metadata and image. We have created an NFT collection of 256 unique spaceships made of 4 cabins, 4 wings, 4 engines, and 4 weapons. How it's built The GitHub repository is a mono-repo containing : The game, located in src/game , built with PhaserJS, a 2D javascript game engine. The images and metadata generator for the NFTs, located in src/generator , a custom script that takes the 4 cabins, 4 wings, 4 engines, and 4 weapons and mixes them together to create the 256 combinations of JSON metadata and png files. Note that the script automatically uploads the images to IPFS using an infura gateway and generates the metadata with the IPFS links. The smart contracts for upgradable NFTs in src/contracts , which is a modified ERC721, created with OpenZepellin, Hardhat, and Typechain. What's next? I want to create more parts to generate up to 10,000 unique ships and then sell the collection in order to finance the development of the game for more enemies, worlds, multiplayer, some storytelling, etc... <div