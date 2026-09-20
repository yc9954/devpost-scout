---
slug: "asm-space"
url: "https://devpost.com/software/asm-space"
title: "ASM Space"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 641
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/scientific_research"
  - "domain/supply_logistics"
  - "substrate/financial_record"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ASM Space

> Board your NFT ship and fight the ASM Brains!

[Devpost](https://devpost.com/software/asm-space) · hackathon [[EthCC Hack 2022]]

## Facets

**domain** [[agriculture_food]] [[scientific_research]] [[supply_logistics]]
**substrate** [[financial_record]] [[genomic_bio]] [[geospatial]] [[video_visual]]

**stack** asm, phaser.js, typescript

## How they structured the write-up

- asm space

## Body

ASM Space Demo Video: https://youtu.be/JLWjpsKx8Y4 Try it out now on https://asmspace.xyz ASM Space is a space shooter game on Ethereum where you can play against enemy ships controlled by ASM Brains! We snapshot 17 ASM brains and implemented them in the game to play the enemy ships in the 17 levels of ASM Space. Each ship is controlled by an ASM brain whose genome has corresponding ship attributes: speed, armor, rate of fire, etc. Additionally, we created a special ship design to display the ASM brain used by the ship. We used AlphaFarm to get the genone rank of each brain and its attributes. Your ship is an ERC 721 NFT that can be minted and upgraded on Ethereum. Mint a basic spaceship to start with. Pilot it in the game and fight ASM Brains piloting ships! Harvest their parts. Upgrade your ship. Then sell your upgraded NFT. We have created an NFT collection of 256 unique spaceships made of a combination of 4 different cabins, 4 wings, 4 engines, and 4 weapons. ASM Space is a fully working game and available at https://asmspace.xyz Make sure you have installed Metamask and connected it to the Rinkeby Testnet . Click "Connect your Wallet". Metamask opens to authorize the connection. The game will then fetch all your spaceship NFTs from the smart contract. If you do not yet have an ASM Spaceship NFT, click "Mint New Ship" and Metamask will open to trigger the mint. You will receive a basic ship with entry-level weapons, wings, engine, and cabin. The ship will appear in your list of ships (if not refresh the page). Select that ship to access the game. The game is built with PhaserJS, a 2D Javascript game engine that allows us to pilot our ship and fire at enemies. Use the directional arrows to move the ship and press the space bar to fire. Try to kill the enemy ship, but be careful not to get hit. You have 10 lives then it's game over. When the enemy is destroyed, it drops some loot. Move your ship over it to get it into your inventory. Then open your inventory to see all the parts you have found. Drag and drop a ship part to its corresponding area on your ship to upgrade that part. An Ethereum transaction opens that will actually modify your NFT metadata and image on-chain with the new part. You can check Etherscan to verify the transaction. Moreover, we have implemented a shop with its own ERC20 currency. Click the shop logo to open the shop. You can sell your parts by dragging them to the shop inventory, a transaction will open and you will earn 1 SpaceCoin per part you sell. On the other hand, you can buy new parts from the shop by dragging them to your inventory. You can then later equip them on your ship. Finally, once you have destroyed the enemy, you can move to the next area. Click the star icon to open the galaxy map. You can fly your ship to the stars in range. Click the one you want to move to and be ready to fight a harder enemy controlled by a better ASM Brain. Move from one star to another until you reach the boss of the game, an insanely powerful ship with devastating weapons, controlled by the best ASM Brain. If you defeat the boss, you win ASM Space! What's next? I want to create more parts to generate up to 10,000 unique ships and then sell the collection in order to finance the development of the game for more enemies, worlds, multiplayer, some storytelling, etc... and of course, keep integrating with ASM Brains. We can't wait for training to be available so we can train ships to fight space battles against players even more realistically! <div