---
slug: "apartment-reviewer"
url: "https://devpost.com/software/apartment-reviewer"
title: "Apartment Reviewer"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 291
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/housing_homeless"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Apartment Reviewer

> A platform to review & track real estate prices in a transparent way. Whether you want to make sure you are getting a fair price or to keep track of an apartment price AR is here to help.

[Devpost](https://devpost.com/software/apartment-reviewer) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[housing_homeless]]
**user** [[general_public]]
**substrate** [[financial_record]] [[video_visual]]

**stack** express.js, javascript, node.js, solidity, sqlalchemy

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for apartment reviewer

## Body

Details Current Apartment List Prices Register Logo What it does Allows users to add reviews for apartments Users can add new prices for apartments Allows users to browse and compare apartments prices It gives users a more accurate picture of an apartment Users can send or receive tips for sharing their reviews It provides additional information for potential tenants to make a more informed decision before signing a lease. Apartments are represented as NFTs Easily collect accurate information that is available to the public using blockchain technology How we built it We use: IPFS NFTStorage: stores NFT's image, name, location, prices,reviews and metadata. The way it works is whenever the user is registering a project the information get pass to NFTStorage IPFS then the NFTStorage generates a hash called CID that is stored on the smart contract. The CID will be used to retrieve the NFT's data AVAX Network: the network I deployed the app. Covalent API for a quick way to fetch and retrieve NFTs and contract transaction history in a sealess way. NFTPort for multi-chain NFT minting, and data transparency such as distributing rewards and minting the NFT. Solidity: Solidity was used for the smart contract together with OpenZeppelin ERC721 for faster development of the smart contract Chainlink Oracle to compare apartment prices with Chainlink prices. Hardhat: for local blockchain development Frontend: React Js for the frontend, Material-UI, and Web3 to connect to the blockchain. Challenges we ran into We learned to work with IPFS NFTStorage and hardhat Accomplishments that we're proud of We are proud of the final MVP What we learned We learned to work with IPFS NFTStorage and hardhat What's next for Apartment Reviewer Post updates Upon registration, get your own token for an apartment <div