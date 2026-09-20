---
slug: "punchable"
url: "https://devpost.com/software/punchable"
title: "Punchable"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 198
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/financial_record"
---

# Punchable

> A marketplace for boxing-related NFTs.

[Devpost](https://devpost.com/software/punchable) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**substrate** [[financial_record]]

**stack** alchemyapi, chainlink, ipfs, metamask, moralis, nft.storage, openzeppelin, polygon, react, solidity, truffle, web3.js

## How they structured the write-up

- what it does
- how chainlink is used
- other technologies used
- challenges i ran into
- accomplishments that i'm proud of
- what i learned

## Body

What it does It allows users to create, sell, and buy boxing-related NFTs. Also, new users have the option to mint a (random) NFT. How Chainlink is used Chainlink's VRF is used in the getRandomNFT function to randomly pick a URI from an admin-created list, which is then used to mint a new token and assign it to the user who called the function. Other Technologies used Polygon / Matic Alchemy to connect to the Polygon Mumbai testnet NFT.Storage to save off-chain NFT metadata to IPFS Moralis to manage users and react-moralis for user-management hooks and context OpenZeppelin's Contract library Metamask to handle Smart Contract transactions Solidity, Truffle and Ganache Challenges I ran into I think the hardest part was coding the FE (spent like 2/3 of my time doing it) since I kept making tweaks to the UI; but, overall, I'd like to thank the sponsors for making it easy to implement their products/tools. Accomplishments that I'm proud of Delivering an MVP on time. What I learned How easy it is to go from an idea to an app in the new decentralized Web thanks to all the tools I was introduced to in this hackathon. <div