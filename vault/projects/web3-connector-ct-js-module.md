---
slug: "web3-connector-ct-js-module"
url: "https://devpost.com/software/web3-connector-ct-js-module"
title: "Web3 Connector - ct.js module"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 477
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# Web3 Connector - ct.js module

> Module provide connection with Metamask wallet for ct.js game engine. You can sign transactions, call your smart-contract and use Alchemy NFT API to get additional information about NFTs!

[Devpost](https://devpost.com/software/web3-connector-ct-js-module) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** alchemyapi, ethers, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for web3 connector - ct.js module

## Body

Module settings (used pre-defined chain) Module settings (custom chain) Game example - wrong chain Game example - transaction Inspiration In web3 world there is not so mutch dynamic and interesting games that is already launched. Launch game that is connected to blockchain require different skills for both sides: game and blockchain development as well as connection between this parts. Main questions for game developers who want join web3: how to connect blockchain and how to use NFT in my game. In other side blockchain developers that want develop game should find someone with game-engine knowledge. Great solution for both sides: ct.js is free and open-source game engine that allow to use JavaScript for building your own 2D game. But there was new question: how connect this game engine with web3 world. What it does I developed web3 module for ct.js game engine that allow to connect game to smart-contract using ethers.js and get even more information about NFTs using Alchemy NFT API . Module contain predefined methods and functionality: detect and switch chains (or add chain to metamask), read and store data in blockchain, show transaction status with link to explorer that automatically update transaction status, custom methods for more control on network/account switch in your game. All this module functionality allow anyone to spend more time for game development and simplify blockchain usage and provide new abilities with Alchemy NFT API. How we built it Learn ct.js game engine. Create module (catmod) for connecting metamask. Add custom chain settings. Add support for Alchemy NFT API. Test module by creating my own game - flying NFT cat that collect stars. Deployed game example to Spheron Network . Challenges we ran into How to create module in ct.js and connect ethers.js. How to get user NFTs minted by my smart contract (Alchemy NFT API help with that). How deal with network and account switch when you in the game. How to show transaction status and update it automatically (user use only one line of code for this). How to build some interesting game example. Accomplishments that we're proud of Simple usage and full documentation with examples. Ability to use any ethers.js functionality in the game. Support any game that can be build by ct.js. Predefined methods that allow developer spend more time for building game and less time to deal with manual stuff in blockchain. Interesting demo game that demonstrate how to use module: connect user wallet, read data from metamask (user account and balance), switch wrong network, read and store data in blockchain using you own smart-contract, read more details about user NFTs (end even more with Alchemy), how to add custom events on account and network change. What's next for Web3 Connector - ct.js module Publish as official module for ct.js. Add support for multiple smart-contracts. Create interesting games and support other developers with that. <div