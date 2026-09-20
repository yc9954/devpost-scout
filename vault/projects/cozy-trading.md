---
slug: "cozy-trading"
url: "https://devpost.com/software/cozy-trading"
title: "CozyVerse"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 857
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/geospatial"
---

# CozyVerse

> On-chain game on Avalanche

[Devpost](https://devpost.com/software/cozy-trading) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** automation, avalanche, c#, foundry, nft, solidity, unity, vrf, webgl

## How they structured the write-up

- intro
- backstory
- game play
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for the cozyverse game

## Body

Connect & Activate The Campsite Player Inventory Trading (via AMM Liquidity pool) Architecture Diagram Intro CozyVerse is an on-chain game on Avalanche where Woofys, our playable NFTs and heroes of the game, explore and build in their new home. The objective is to gather resources, sell them, or craft new materials while gaining experience. The game is using Chainlink VRF & Automation to drive an MMO-lite experience, immersing players in the snowy regions on Avalanche as they guide their Woofys through a captivating exploration. Backstory Owners of Cozy Penguin NFTs leveraged Chainlink CCIP to portal their penguins from Ethereum to Avalanche. Once on Avalanche, each Cozy Penguin was able to rescue a Woofy NFT that came as an unopened capsule. There was then a public mint to buy the rest of the capsules. Each NFT holder was able to reveal their Woofy whenever they wanted. The reveal mechanic utilized Chainlink VRF to assign the NFT a random Woofy from a pre-initialized, rank-base sorted array on the contract. The contracts that implemented CCIP were built before the hackathon but the Woofy Contract including reveal mechanics were built after the start of the hackathon. Game Play After the user connects their wallet for the first time, they need to activate their address by paying a fee (fee is waived for the current hackathon). The player starts at the campsite in a snowy region. Here, the Woofy has to build out a new home and start gathering resources. While we’ll expand this to a broader exploration and resource / upgrade driven game, our focus during the hackathon centered on refining the core resource spawn and gathering loop. If a player has the required skill level and equipment, they can mine the resource. The Chainlink infrastructure plays a key role - Automation drives the resource respawning loop. Each player can gather a resource only once until it respawns - a random campsite resource, determined by VRF, respawns every 15 minutes. Resources will serve various purposes, such as crafting items, trading (via AMM Liquidity pool ), or selling for pebbles (the native in-game currency). Players will be able to use their pebbles to purchase a variety of upgrades and items from the in-game shop. How we built it The game's backend, built with Solidity and Foundry **, utilizes **Chainlink Automation for automatic resource spawning. Chainlink VRF is leveraged to randomly determine the resources to be spawned. The time-based upkeep is registered, funded and managed via Chainlink Automation App . On the frontend, the game's user interface is constructed using Unity and Thirdweb Unity SDK . Four smart contracts have been deployed on Avalanche Fuji testnet, each serving specific purposes: Campsite.sol for managing game actions. Player.sol dedicated to maintaining and managing the state of player (experience, skills, items, pebbles, inventory and more). Resources.sol designed to manage in-game resources, it seamlessly integrates Chainlink Automation and VRF, ensuring the automatic and randomized respawn of resources. Shop.sol manages the exchange of resources for pebbles (the main in-game currency), as well as the purchase of equipment and upgrades. Challenges we ran into We needed to deploy contracts locally for testing the game in the Unity Editor. While utilizing the Thirdweb Unity SDK to interact with the contracts, we encountered challenges as the SDK lacked support for localhost. Their documentation lacked clear instructions on this aspect, so we were a bit stuck while figuring out how to configure the environment for local game development. As an international team spread across different time zones, we had to strategize to plan our work and collaborate effectively. Accomplishments that we're proud of Developed and implemented a plan for integrating unpredictability into the game, using Automation and VRF , minimizing managerial oversight. Efficiently configured the development and local testing environment for both the game and contracts, overcoming initial issues. Created a unified developer script that accelerated the development process. The script deploys all contracts, automatically importing the ABIs and addresses directly into the Unity project. This eliminated the need for adjustments related to contracts within Unity. Organized work effectively, ensuring smooth coordination among team members across different time zones. Achieved a visually appealing and functional game prototype! This prototype serves as a robust foundation for future feature enhancements, marking a significant milestone in our project's progress. What's next for the CozyVerse game This is a prototype of the game, a lot of features are set to be developed in the upcoming months: Map : Expanding to include additional villages and diverse locations. AMM (Automated Market Maker): Implementing unique Liquidity Pools for each village to catalyze economic development. Skills : Expanding beyond basic mining and smithing to include new skills (including woodcutting, crafting, gardening, fishing, hunting, and more.). Items : Enabling players to purchase a variety of items from the in-game shop, including tools (axe, fishing rod, bow, etc.), equipments (backpack, skis, snowmachine, etc.) and more. Social elements : MMO-lite experience where you can see and interact with other player’s near you. Forming trading guilds to play the game with friends. As we continue our development journey, we will actively explore and evaluate additional features that will enhance the overall game experience. <div