---
slug: "picasarts-io-on-polygon-the-defi-nft-marketplace"
url: "https://devpost.com/software/picasarts-io-on-polygon-the-defi-nft-marketplace"
title: "Picasarts.io on Polygon - The Defi NFT Marketplace"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 836
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Picasarts.io on Polygon - The Defi NFT Marketplace

> The Defi NFT Marketplace on Polygon to mint, sell, buy NFTs and Loan, Lending Borrowing, Staking, Loyalty Program for NFTs.

[Devpost](https://devpost.com/software/picasarts-io-on-polygon-the-defi-nft-marketplace) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[finance_payments]]
**substrate** [[financial_record]] [[geospatial]]

**stack** charka, covalenthq, ipfs, javascript, mongodb, nextjs, node.js, react, redux, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for picasarts.io on polygon - the defi nft marketplace

## Body

Use Case Diagram Loan with NFT collateral System Diagram Smart Contracts usage map Inspiration Trading in NFTs has spiked at an unprecedented speed. There are almost 50 million NFTs on the market; the highest one was sold for $91.8 million (The Merge). Yet, NFT's function is only restricted to buy-and-sell. Apparently, there is more we can do with them. → We decided to create an NFT Defi platform on multi-chains, including Near, Tron, Aurora and POLYGON. At Picasarts, we aim to offer NFT owners a convenient, secure and multi-chain platform to make the most value out of their NFTs. We chose POLYGON because it is a comprehensive platform with EVM; thus, we can save time for R&D and focus more on building features instead. Plus, IPFS is the perfect media storage system we are looking for. What it does Picasarts is an all-in-one financial solution for NFTs. Users can trade, stake, take a loan and join loyalty programs with NFTs. Fundamental functions: Create or import existing collection Minting NFT with a Royalty fee Buy/Sell/Auction NFTs on the marketplace Integrate with MetaMask Wallet Use IPFS to store user's media, NFT.storage to store NFT metadata Outstanding functions: Usage of collection contract so that artists/projects can easily create and connect with Picasarts New or existing projects can easily connect with Picasarts, and their NFTs are eligible for all functions on the platform, meaning NFTs can be used for a loan for staking features. Arrange a loan with NFTs as collateral The web app will act as a platform to connect Lenders and Borrowers. Borrowers can use their NFT as collateral. The value of that NFT is determined by mutual consent. Stake NFTs NFT Creators (Artists) will sell copies of their NFTs to Collectors. Collectors can then stake those NFTs in a pool created by Artists and earn rewards periodically. The reward can be a fungible token issued by Artists on Picasarts (i.e., PCS). With PCS, Collectors can gain an advantage in buying more NFTs from Artists at private sales before launch day. Collectors can also possess governance over Artists and their collections. As a token, PCS may also have monetary value and can be traded on a platform (i.e., Uniswap). Collectors can withdraw their NFTs from the pool at any time. Loyalty Program on-chain (Coming soon) Picasarts offers a loyalty program for all NFT sellers and buyers on the platform. For each transaction, traders will be rewarded with a number of points, which will then be accumulated and exchanged for promotional codes and other benefits on Picasarts. Use Case Diagram How we built it We divided our journey into 3 phases: Build Smart Contracts, Build DApp and Deploy & Debug. To build Smart Contracts, we use: Solidity version 0.8.4 Open Zeppelin Smart Contracts usage map: Our tech stack: NodeJS, React, NextJS, Redux, Typescript… Chakra UI: a React UI component highly suitable for building artistic apps. Javascript libraries like Web3 and Ethers to interact with smart contracts and MetaMask wallet. Mongo Atlas DB to store NFTs and users' secondary information, to easily access data and reduce the burden of calling too many different smart contracts. Covalenthq API & Tron Scan API to collect the user's token balance on registered wallet address. NFT Storage to store NFT metadata, IPFS ( https://polygon-ipfs.picasarts.io ) to store collection and user metadata. We have built a private IPFS node to speed up query process. To deploy Smart Contracts on Mumbai Testnet, we use Truffle to deploy and debug Smart Contracts. Challenges we ran into Although we already have experience in developing dApp with solidity, we encountered multiple technical problems which take quite some time to solve: The process of building a smooth portal for artists or projects to connect easily. Query to NFT metadata on various contracts. Loan-related technical process, namely adding or editing loan extension proposals. Connect and use IPFS to store media and metadata. Accomplishments that we're proud of Overcome technical challenges to accomplish goals. Promote the use of NFTs and diversify the value of NFTs. Won a few prizes for Picasarts on Near and Tron. Gain a lot of in-depth knowledge about Blockchain and finance. Able to take a loan with our own NFTs. What we learned Throughout the journey, we have learned to Build a complete dApp. Deploy a smart contract and the concept of it Blockchain. Use the TronWeb library to interact with Wallets and Smart Contracts. Understand IPFS's model & usage, as well as Nodes configuration. General knowledge of libraries and APIs in various languages. Technical knowledge on how to increase the value of NFTs, from which promote the launch of more NFT projects. Build up new business models/features: NFT loan, pool staking and loyalty program. What's next for Picasarts.io on Polygon - The Defi NFT Marketplace Go live on POLYGON mainnet. NFT Lending and Borrowing: Improve NFTs Validation scheme. Seeking organic users and building a community. Improve user experience and flow. Optimize the Web Frontend page to look more artistic. Call for investment and mentoring. NFT renting <div