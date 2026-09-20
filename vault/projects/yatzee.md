---
slug: "yatzee"
url: "https://devpost.com/software/yatzee"
title: "Poker Joker Dao"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 590
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/civic_government"
  - "domain/developer_tools"
---

# Poker Joker Dao

> Poker Joker DAO is a gaming DAO designed to manage games that provide ownership to players (DAO membership) and utilities for gaming assets (NFTs).

[Devpost](https://devpost.com/software/yatzee) · hackathon [[Cosmos HackAtom VI]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[civic_government]] [[developer_tools]]

**stack** angular.js, cosmos-sdk, cosmwasm, docker, javascript, node.js, rust, secretjs, shell, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for poker joker dao

## Body

Home page | list games | list NFTs Inspiration We started off with wanting something fun and simple, and as we worked on the hackathon, we realised that our design of the smart contracts was guided by a few principles that we value: Aligning NFT value with utility: By linking the dice NFTs xp level (earned by playing) to the base bet amount, we providing a correlation between the NFT itself and the potential winnings (via [xp-table]) of an NFT in the game. This is important as it captures the skills of the previous owners of the NFT and encourages future engagement with the game. Easy onboarding for adoption: We implemented collateralisation of Dice NFT so that first time users can play the game without specifically needing PJ Dao token (to be implemented) or network gas (with the incoming feegrant in the cosmos-sdk and other gas station implmentations). Decentralised gaming and governance: As a Peer-to-Peer facility for gaming, this facilitates a fair chance for everyone to win (as opposed to casinos). Futhermore, the gamers should govern the organisation. For example, in this MVP, the DAO contract is currently responsible to mint and collateralisation of the NFTs. Such decisions, along with the scoring table will be voted by the gamers themselves. What it does There are 3 components to this project the DAO, which helps to onboard users to the games the Dice game, which utilises the psuedo-randomness provided by the TEE (please look at project README for game details the Dice NFT set, which supports collateralisation (via a CLI at the moment). This means transfer / send is prohibited. When you join the DAO, it will provide you with a NFT (if you did not already have one), one you can collateralise to play games with. Then the game itself uses randomness from the secret network TEE but also requires some skills! How we built it Webapp: Angular with SecretJS Smart contracts: Secret Network (cosmwasm) JS-CLI: nodeJS with SecretJS Challenges we ran into Storage for the smart contracts without the support of db_scan meant we tried to learn from cw-storage but was different. permit verification causes timeout (sometimes): in our deployment to testnet, we were unable to to query the testnet node with permit as the node returned with timeout error. We were able to use permit for views locally. Accomplishments that we're proud of New to the secret network, we were proud to be able to have a working MVP using the SNIP 721 implementation with permit and not viewing keys. We were able to integrate the Kelpr Wallet in the frontend to produce permits and interact with the DAO / Game contract and the NFT contract. What we learned So much! For some of us it was the first time into the world of web3, the concept of DAO, nodes, etc was very exciting. For others, it was nice to learn about how smart contracts can be written if the execution is private and that data is encrypted. What's next for Poker Joker Dao Implement shielded dice game Decouple DAO contract with Dice Game contract Support multiple games and NFTs (we would love to work with other games in this hackathon next! ) Implement member voting and governance Standard interface on top of SNIP-721 / 1155 for game assets Improve gaming logic with points system (currently uniform increase only) Put it on mainnet! Disclaimer: The Pulsar testnet sometimes returns timeout for Permit verification and may affect user experience of our webapp since viewing key was not used. <div