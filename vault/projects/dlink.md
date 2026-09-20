---
slug: "dlink"
url: "https://devpost.com/software/dlink"
title: "dLink"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 407
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# dLink

> Mint your Dynamic NFT now!

[Devpost](https://devpost.com/software/dlink) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**substrate** [[video_visual]]

**stack** chainlink, erc721, ethereum, etherjs, nextjs, nft, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for dlink

## Body

Inspiration For the first time in the history of the Internet, creators can monetize directly using art by launching their NFT Collections.Nowadays,NFTs are used in most generative NFT art projects, play-to-earn games, and digital collectibles. But these are limited by the fact that they can't be changed once they are put on a blockchain, their metadata can't be changed. Dynamic NFTs can be utilized in such cases, which let NFTs keep their unique IDs while also getting updated information. Change in a dNFT usually means that a smart contract has changed the metadata. This is possible because the NFT smart contract has automatic updates that tell the underlying NFT when and how its information should change. But, currently the dNFT market is not as popular as traditional NFTs. The reason being lack of resources for beginners and artists to get started with, which are easy to understand and follow for someone who has no prior experience with coding. Hence we have decided to come up with a platform for users to create dNFTs on Polygon in a simple manner within a few clicks, similar to MintNft by Polygon which offers the same services for traditional NFTs. What it does Initially user needs to connect his metamask wallet upon which he is redirected to the application dashboard. Here user can fill in the details of the dynamic NFT he wants to create such as name, description, traits. The user needs to upload the images that he wants to feature in his dNFT one by one, which are uploaded to IPFS simultaneously. User can set the time upon which the NFT should change accordingly. Chainlink Upkeep for automates the NFT updating process in a timely manner according to user's settings. How we built it We built it used Nextjs to build our application. Tailwind CSS is used to design our application. Solidity for writing Smart Contracts, hardhat for deploying them. Chainlink is used for highly reliable automation based on time set according to the user choice. We chose Polygon chain to deploy the smart contract. Challenges we ran into Initially we took some time in learning about Chainlink upkeep and how it can be leveraged to deploy our Dynamic NFTs. Later while implementation, we came across some bugs in our smart contract. After spending some time we could figure them out and fix them. What's next for dLink Better UI/UX Optimize further and introduce more features Mainnnet Launch <div