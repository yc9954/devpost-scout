---
slug: "liquidity-wars"
url: "https://devpost.com/software/liquidity-wars"
title: "Liquidity Wars"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 1122
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/geospatial"
---

# Liquidity Wars

> Liquidity wars is a no-loss game where players fight each other to gain as much LP rewards as they can by developing infrastructure and rob other players. The main goal is to increase DEXes liquidity.

[Devpost](https://devpost.com/software/liquidity-wars) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[geospatial]]

**stack** chai, chainlink, chainlinkboilerplate, css3, ethereum, ethers, framer-motion, hardhat, html5, javascript, kepeer, moralis, next.js, openzepellin

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for liquidity wars

## Body

Gameflow Resource ratio and earnings Protocol earnings Desired game flow Game config and strategies Architecture Inspiration Liquidity on DEXes is a crucial factor which is responsible for costs of swap (slippages) and liquidity providing efficiency (impermanent loss). Low liquidity results in volatility in cryptocurrency prices and exposes the exchanges to market manipulation. Despite the clear benefits of yield farming, DEXes may still struggle to attract liquidity providers to their exchanges. Commonly, DEXes compete for liquidity by offering high annual percentage rates with highly inflationary tokens. However, this obscures the effective APR of staking tokens. We recognize the need for an effective manner to attract liquidity providers. What better way to do so than by bringing the concept of play and earn to the DEX market. We see it as a highly-attractive commercial tool for bringing new liquidity providers to the scene. We believe games can make make token staking more enticing to users. It would also attract recurrent staking by users due to its addictive nature. What it does Liquidity Wars is a decentralized protocol that addresses the lack of liquidity in DeFi. Our protocol offers DEXes the ability to easily scaffold a no-loss, play and earn, decentralized strategy game which runs autonomously. Players deploy their liquidity to play in the game. At the end of the game each player can redeem the same amount of liquidity tokens (LP). The main objective of the game is to get as many resources (RES) as possible. The RES is the virtual in-game currency that will be the base for the calculation of the rewards distributions. Those rewards will be derived from the LP tokens rewards. In order to get RES players can attack and rob each other, develop infrastructure to get more resources, increase defense or build protection to hide RES from the attacker. The purpose of the project is not to be another play to earn game but to be play and earn game which will attract potential investors to provide and lock their liquidity. Main source of protocol income will be rewards calculated based on the RES which are transferred to the contract every building upgrade, troops creation and attacks. At the end of the game, our smart contract address will be treated similarly to other players and get the rewards proportionally to the amount of RES accumulated. Only a small percentage of RES spent in the game will be transferred to our contract and the rest will be burnt reducing the total supply of RES. The target audiences of this project are not only players but DEXes which will want to increase liquidity by implementing our game. Using our protocol, DEXes will be able to configure which Liquidity Provider (LP) tokens are required for users to deposit in order to join their game, as well as several other configurations such as: game duration, deposit amount, player attributes and determine which LP tokens will be assigned to each nation (orcs, elves, human, dwarfs). Mainly DEXes will be able to determine its own strategies for LP tokens: How we built it The smart contracts behind our protocol are written in Solidity with the help of the Hardhat framework, Openzeppelin and Chainlink sample contracts. Chainlink VRF is used for bringing randomization into our game's battle system. Chainlink Automation is used to automate the starting and ending of the game. It also automates the transfer of the LP tokens back to the players and the distribution of the rewards tokens when the game ends. Chainlink Price Feeds are used for the calculation of the price of the LP Tokens in USD. This allow the DEXes to configure a stable value in USD which will be reflected in amount of LP tokens required to participate in their games. We have chosen Polygon as blockchain due to the fact that it is currently the most popular layer 2, with several potential partners, such as DEXes and other DeFi protocols, already deployed. This allows our protocol to benefit from existing money legos and for the game to run smoothly, since the players can interact freely with our contract without caring too much about gas fees and network congestion. Quicknode was used as the RPC node provider for the smart contracts tests due to the high reliability it offers. It is also compatible with both Polygon mainnet and testnet networks for deployment. In the pre-built game interface, Quicknode was also used for querying smart contract events. Our sample frontend interface was built using NextJS, Moralis for the wallet interactions and Ethers.js for the smart contract calls. Pixel-art asset pack from sprout-lands Challenges we ran into Set up multiple keepers and using checkData and performData to steer the logic dependent on conditions. Get number of required LP tokens to start the game based on the calibrated required USD amount and price feeds. Design smart contracts structure so that they will not exceed maximum smart contract size for deployment (EIP-170). Simulate dummy rewards for the LP pool due to lack of rewards in the mumbai network. Emit event in such a way that could be queried/filtered in the frontend. No previous knowledge about building game interfaces Accomplishments that we're proud of Battle system using VRF randomized number and in-game attacker/defender stats to determine the outcome of the battle. Working keepers that assure the game automatically changes states and distributes resources when the game is running. Creating a simple, fun and creative pixel-art frontend interface. Fully-functional sample frontend to demonstrate all core functionalities and concepts of the protocol. Logging attacks/defences for each players. Complex javascript scripts for testing and deployment of the smart contracts. Map builder tool that can be found here What we learned A whole lot! But mainly: How to emit indexable events and query/filter them in the frontend. How to split the smart contract logic and design reasonably sized contracts without stack too deep erors. Core concepts of game inteface design such as tiles, sprites and map building. How to use HTML5 tag for building game maps What's next for Liquidity Wars Accept more LP tokens and assign each token to specific nations (orc, elves, human, dwarfs). Each nation will have some special bonuses to troops and buildings. Example: dwarfs will be better in defense and orcs will be better in ofense Provide fully configurable game and strategies - that allows different DEXes to configure multiple games as they wish (game duration, additional rewards, allowed LP tokens). It will be achieved by using low-level solidity encoded calldata. Introduce tradeable ERC1155 tokens with metadata stored on IPFS which creates some bonuses to the game. Introduce unique buildings for each Nation which will provide some extra bonuses. Notice: More specific functionalities which can be done is mentioned here and here <div