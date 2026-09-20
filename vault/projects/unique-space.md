---
slug: "unique-space"
url: "https://devpost.com/software/unique-space"
title: "Unique Space"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 497
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/supply_logistics"
---

# Unique Space

> Space Shooter Game with Upgradable Nested NFTs

[Devpost](https://devpost.com/software/unique-space) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[supply_logistics]]
  <sub>weak: agriculture_food</sub>
  <sub>weak: financial_record</sub>

**stack** phaser.js, typescript, unique

## Body

Unique Space Unique Space is the first-ever game with upgradable and nested NFTs. Mint a basic spaceship to start with. Pilot it in the game and fight enemies! Harvest their parts. Upgrade your ship. Then sell your upgraded NFT. We created an NFT collection of 256 unique spaceships made of 4 cabins, 4 wings, 4 engines, and 4 weapons. We have created 2 collections on the Unique Network. One for parts (USP) and one for ships (USS). Ships are empty NFTs that act as parents for the nested parts NFTs. Each ship must have 4 nested part NFTs to be complete (Cabin, Weapon, Wings, and Engine). You later upgrade a ship by un-nesting the corresponding part, e.g. a weapon, and nesting another part instead, e.g. a better weapon. Try the game at https://uniquespace.io . As this is only a proof-of-concept so far, we have hard-coded a seed inside the game to interact with the Unique Network. Later versions will obviously integrate with the Polkadot{.js} chrome extension. We also suggest that you open the browser console in order to observe the inner workings of the game and its interaction with the blockchain as each step and transaction is logged into the console. Click "Let's go". The game will then fetch all the ship tokens owned by that seed and part tokens nested into these ship tokens. You can select any of the displayed ships or mint a new one by clicking "Mint New Ship". This will create an empty ship token and 4 part tokens for entry-level weapons, wings, engine, and cabin (Note that this operation can take up to 3 minutes to complete on-chain, check the browser console to verify its status) then nest them inside the ship token. The ship will then appear in the list of ships (You might need to refresh the page). Select that ship to access the game. The game is built with PhaserJS, a 2D Javascript game engine that allows you to pilot your ship and fire at enemies. Use the directional arrows to move the ship and press the space bar to fire. Try to kill the enemy ship, but be careful not to get hit. When the enemy is destroyed, it drops some loot. Move your ship over it to get it into your inventory. Open your inventory to see all the parts you have found. Drag and drop a ship part to its corresponding area on your ship to upgrade that part. This will un-nest the previous part from the ship NFT and nest the new part. How it's built The game is built with PhaserJS, a 2D javascript game engine. The game integrates a fork of https://github.com/UniqueNetwork/unique-playgrounds in order to create and nest the NFTs on the Unique Network. What's next? We want to create more parts to generate up to 10,000 unique ships and then sell the collection in order to finance the development of the game for more enemies, worlds, multiplayer, some storytelling, etc... <div