---
slug: "zero-bazaar"
url: "https://devpost.com/software/zero-bazaar"
title: "Bazaar Zero"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 585
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# Bazaar Zero

> Bazaar zero is multi-channel interoperable digital assets marketplaces that allow users to deal directly with each other trust-lessly.

[Devpost](https://devpost.com/software/zero-bazaar) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[realtime_stream]] [[structural_withholding]]
**user** [[general_public]]
**substrate** [[financial_record]] [[geospatial]] [[web_dom]]

**stack** fluence, infura, moralis, node.js, polygon, react, semaphore, sequence, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bazaar zero

## Body

Shop node UI Shop node UI Process proofing the identity (ZKP) and minting Bundle NFT Deposit ERC721 to Bundle NFT Deposit ERC20 to Bundle NFT Mark the Bundle NFT for sale Unpack unused Bundle NFT, and send the assets inside back to the owner Search saleable Bunde NFT from shop nodes Buy the Bundle NFT directly from the seller Inspiration The current marketplace like Opensea, TofuNFT or Rarible are being used by a lot of users in the decentralized ecosystem. At this point, the marketplaces ecosystem is similar or going in the direction of the vendor lock concept similar to Amazon, Google and so on. As a user, you are stuck with the marketplace business rules - e.g fees, escrow duration and so on. The marketplaces also are not versatile to allow users to build more things to either expand the usage, or have a unique solution on top of it. What it does In marketplaces network would have 4 main functions: To provide the tools to continuously verify each of the nodes. To make it easy to implement new consumers , which seller can control how their products are accessed or which services can consume it. Ability to bundle multiple types of assets (ERC20, ERC721 or ERC1155) in a single product. The network can regulate transaction agreement to provide transparency and security of the network relies on the technology itself and its operation by the users. More information: Slides How we built it Key integration: Fluence Network/IPFS - the base network for nodes and services located. It handle the data routing part using libp2p. Polygon - Cheap NFT minting ftw! Sequence Wallet - Smart contract wallet located in the node. It stores the saleable NFT and its assets. Using the build in indexer, able to instantly track Bundle NFT directly from the wallet. To standardise the distribution of ERC721 (NFT) in the network, a special wrapper NFT is created which bundle multiple assets into a single NFT. Challenges we ran into Working on integrating seller verification using Zero Knowledge Proof (ZKP) - The idea is to prevent abuse by users in the network to mint the Bundle NFT randomly. We spent weeks just to understand what ZKP is and how to integrate in the network in real-time. Getting the node(s) to work seamlessly real-time using Fluence Network - The abilities of the network is very dependent on the shop node (s) able to communicate directly to or from consumer node (s). e.g In real time searching for saleable product that can be buy from the nodes. Working with 2 blockchain wallet at the same time - For this project to work properly, we need to integrate a smart contract wallet (Sequence wallet) in every node client. Users need to deposit their assets from the current wallet into the Sequence wallet. Handling approval between the wallets and smart contract quite confusing at first. Accomplishments that we're proud of Zero Knowledge Proof (ZKP) integrated in the network and smart contract !! Ability for the nodes to work in real-time. Returning result in real time from the shop node (s). What we learned ZKP! Peer-to-peer communication (Libp2p) What's next for Bazaar Zero Open source! Stabilize and speed up the communication between nodes Build more consumer services - e.g: 1. Deployer for front-end, so user able to have its own URL 2. Mart nodes - users can host their product in this node, so they don`t need to open the node all the time. Much more … <div