---
slug: "roosterfight"
url: "https://devpost.com/software/roosterfight"
title: "RoosterFight"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 369
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "substrate/video_visual"
---

# RoosterFight

> Claim, train and conquer.

[Devpost](https://devpost.com/software/roosterfight) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[on_device_local]]
**substrate** [[video_visual]]

**stack** hardhat, javascript, moralis, solidity, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for roosterfight

## Body

Landing Page Marketplace Inspiration I took inspiration from zed.run a virtual horse race game and a tradition of my country cockfight to bring a virtual game where users can have a like experience of raise and train a nice looking rooster and compete with others. What it does RoosterFight is an NFT game where you can claim and train a Rooster to fight and reach the top of the tournaments. User Story: I can connect my wallet using Metamask/Moralis. User Story: I can claim Roosters for free. User Story: I can join in tournaments paying a tournament fee. User Story: I can fight with other roosters to win points and climb to the top positions. User Story: I can win if at the end of the tournament I have more points. How we built it On the frontend I used: Vue.js 3 as framework Framework Moralis to manage auth and store some off-chain data as well as IPFS provider for the assets ethers.js JS library for interacting with the Ethereum Blockchain and its ecosystem Blockchain Environment and scripts: Hardhat - Flexible, extensible and fast Ethereum development environment for professionals. hardhat-deploy - Provided utilities for deployments and tasks Chainlink VRF - To get random numbers to generate damage Open Zepplin - and their contracts and utilities forn ERC721, String, SafeMath, Counters, Ownable and not reentrancy guard hashlip nft engine - to generate arts Moralis IPFS to store the NFT images Challenges we ran into I reached the Smart Contract limits so I have difficulty to deploy to the mumbai testnet i manage to reduce and remove the code that were not so important and use public vars as getters VRF Coordinator locally I found a template by patrick and adapted it to my code. Accomplishments that we're proud of Pre mint logic without using a lot of contracts typescript usage on backend and frontent tested above 90% of the code finish the project What we learned VRF Coordinator usage to generate random numbers and expand them Configure deployments with hardhat-deploy use hardhat with typescript to use moralis auth and object DB, and its IPFS What's next for RoosterFight 3D Roosters fighting Let users sell and buy roosters Different tournaments <div