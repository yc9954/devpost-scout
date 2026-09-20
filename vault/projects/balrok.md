---
slug: "balrok"
url: "https://devpost.com/software/balrok"
title: "BALROK"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 644
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# BALROK

> Space shooting game with upgradable NFTs.

[Devpost](https://devpost.com/software/balrok) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**domain** [[agriculture_food]] [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[video_visual]]

**stack** phaser.js, tron, typescript

## How they structured the write-up

- balrok
- about balrok

## Body

Balrok Demo Video: https://youtu.be/FM9LSidM2aw Try it out now: https://balrok.io Tron DAO link: https://forum.trondao.org/t/balrok-io-a-space-adventure/4415 About Balrok Balrok is a space shooter game with upgradable NFTs on TRON. Mint a basic spaceship to start with. Pilot it in the game and fight enemies! Harvest their parts. Upgrade your ship. Then sell your upgraded NFT. We have created an NFT collection of 256 unique spaceships made of a combination of 4 different cabins, 4 wings, 4 engines, and 4 weapons. Balrok is a fully working game and available at https://balrok.io Make sure you have installed TronLink and connected it to the Tron Nile Testenet. Click "Connect your Wallet". TronLink opens to authorize the connection. The game will then fetch all your spaceship NFTs from the smart contract. If you do not yet have a Balrok NFT, click "Mint New Ship" and TronLink will open to trigger the mint. You will receive a basic ship with entry-level weapons, wings, engine, and cabin. The ship will appear in your list of ships (if not refresh the page). Select that ship to access the game. The game is built with PhaserJS, a 2D Javascript game engine that allows us to pilot our ship and fire at enemies. Use the directional arrows to move the ship and press the space bar to fire. Try to kill the enemy ship, but be careful not to get hit. You have 10 lives then it's game over. When the enemy is destroyed, it drops some loot. Move your ship over it to get it into your inventory. Then open your inventory to see all the parts you have found. Drag and drop a ship part to its corresponding area on your ship to upgrade that part. A Tron transaction opens that will actually modify your NFT metadata and image on-chain with the new part. You can check TronScan to verify the transaction. Moreover, we have implemented a shop with its own TRC20 currency. Click the shop logo to open the shop. You can sell your parts by dragging them to the shop inventory, a transaction will open and you will earn 1 BAL per part you sell. On the other hand, you can buy new parts from the shop by dragging them to your inventory. You can then later equip them on your ship. Finally, once you have destroyed the enemy, you can move to the next area. Click the star icon to open the galaxy map. You can fly your ship to the stars in range. Click the one you want to move to and be ready to fight a harder enemy. Move from one star to another until you reach the boss of the game, an insanely powerful ship with devastating weapons. If you defeat the boss, you win Balrok! How it's built The GitHub repository is a mono-repo containing : The game, located in src/game , built with PhaserJS, a 2D javascript game engine The images and metadata generator for the NFTs, located in src/generator , a custom script that takes the 4 cabins, 4 wings, 4 engines, and 4 weapons and mixes them together to create the 256 combinations of JSON metadata and png files. The smart contracts for upgradable NFTs in src/contracts , which is a modified TRC721 with a new endpoint to modify an NFT metadata and image. It was created from a fork of https://github.com/TRON-Developer-Hub/decentralized-library Wait, there is more! Balrok is not a single game, it is a metaverse! Players can generate their own galaxy by creating a configuration file levels.json which lists the whole configuration of the game and levels. Anyone can create their own adventure in Balrok! What's next? I want to create more parts to generate up to 10,000 unique ships and then sell the collection in order to finance the development of the game for more enemies, worlds, multiplayer, some storytelling, etc... <div