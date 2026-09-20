---
slug: "picasarts-io-on-tron-the-defi-nft-marketplace"
url: "https://devpost.com/software/picasarts-io-on-tron-the-defi-nft-marketplace"
title: "Picasarts.io on TRON - The Defi NFT Marketplace"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 898
team_size: 4
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Picasarts.io on TRON - The Defi NFT Marketplace

> The Defi NFT Marketplace on TRON to mint, sell, buy NFTs and Loan, Lending Borrowing, Staking, Loyalty Program for NFTs

[Devpost](https://devpost.com/software/picasarts-io-on-tron-the-defi-nft-marketplace) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]]

**stack** btfs, nextjs, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for picasarts.io on tron - the defi nft marketplace

## Body

Marketplace Loan Covenant Picasarts Defi Usecases NFT Loan Inspiration Trading in NFTs has spiked at an unprecedented speed. There are 10+ million NFTs on the market; the highest one was sold for $91.8 million (The Merge). Yet, NFT's function is only restricted to buy-and-sell. Apparently, there is more we can do with them. → We decided to create the very first Defi NFT platform on TRON. At Picasarts on TRON, we aim to offer NFT owners a convenient, secure and multi-chain platform to make the most value out of their NFTs. We chose TRON because it is a comprehensive platform with TVM (highly compatible with EVM); thus, we can save time for R&D and focus more on building features instead. Plus, TRON's BTFS is the perfect low-cost media storage system we are looking for. What it does Picasarts on TRON is an all-in-one financial solution for NFTs. Users can trade, stake, take a loan and join loyalty programs with NFTs. Fundamental functions: Buy/Sell/Auction NFTs on the marketplace Setup Royalty fee Minting NFT on TRON NFT Launchpad FT factory Integrate with TRX Wallet Use BTFS to store media Outstanding functions: Arrange a loan with NFTs as collateral The web app will act as a platform to connect Lenders and Borrowers. Borrowers can use their NFT as collateral. The value of that NFT is determined by mutual consent. Stake NFTs NFT Creators (Artists) will sell copies of their NFTs to Collectors. Collectors can then stake those NFTs in a pool created by Artists and earn rewards periodically. The reward can be a fungible token issued by Artists on Picasarts on TRON (i.e., ART). With ART, Collectors can gain an advantage in buying more NFTs from Artists at private sales before launch day. Collectors can also possess governance over Artists and their collections. As a token, ART may also have monetary value and can be traded on a platform (i.e., Ethereum). Collectors can withdraw their NFTs from the pool at any time. Loyalty Program on-chain (Coming soon) Picasarts on TRON offers a loyalty program for all NFT sellers and buyers on the platform. For each transaction, traders will be rewarded with a number of points, which will then be accumulated and exchanged for promotional codes and other benefits on Picasarts on TRON. How we built it Since TRON already has a complete toolset from TVM, TronWeb, and TronIDE to REST API, Oracle, BTFS, etc., we decided to develop based on what TRON already supports. Our tech stack: Solidity and OpenZeppelin library ( https://docs.openzeppelin.com/ ) to write smart contracts because TVM is highly compatible with Ethereum smart contracts. TronBox to compile smart contracts. Tronscan to deploy and interact with contracts on testnet TronWeb library interacts with the blockchain and users' accounts on Frontend and simultaneously loads contracts to read and write them. TronLink extension to create accounts that interact with dApp. BTFS gateway to provide endpoints for uploading and viewing files. Nginx proxy to map nodes on the server with real domain with SSL certificate NodeJS, NextJS and Ant design to complete the web app's Frontend and enhance the user's experience. Challenges we ran into Although the tech stack used inTRON is relatively basic for a Web3 developer, we encountered multiple technical problems which take quite some time to solve: Issue 1: Some OpenZeppelin's contracts had errors when compiled with TronBox. Thus, we had to customize the contracts by OpenZeppelin. Issue 2: TronBox cannot deploy contracts. We chose TronIDE and Tronscan to replace TronBox in deploying. Issue 3: Interacting with the wallet on Frontend. Some examples and sample codes do not run correctly, are hard to set up and use obsolete, incompatible libraries. Luckily, the team can still connect to the wallet by customizing these examples based on TronWeb's document. From a business side, we need to figure out unique features that differentiate Picasarts on TRON from other marketplace platforms. This part is particularly challenging since we have to look for unknown uses of NFTs and validate their potential. We tried to put ourselves in others' shoes to see if there's any other way to maximize the functions of NFTs. Accomplishments that we're proud of Build an NFT Marketplace on a new platform with limited resources. Overcome technical challenges to accomplish goals. Promote the use of NFTs and diversify the value of NFTs. Develop a full-functioning platform on 3rd attempt. Gain a lot of in-depth knowledge about blockchain and finance. Able to take a loan with our own NFTs. What we learned Throughout the journey, we have learned to Build a complete dApp on TRON. Deploy a smart contract and the concept of it on TRON Blockchain. Use the TronWeb library to interact with Wallets and Smart Contracts. Understand BTFS's model & usage, as well as Nodes configuration. General knowledge of libraries and APIs in various languages. Technical knowledge on how to increase the value of NFTs, from which to promote the launch of more NFT projects. Build up new business models/features: NFT loan, pool staking and loyalty program. What's next for Picasarts.io on TRON - The Defi NFT Marketplace Go live on TRON mainnet. NFT Lending and Borrowing: Improve NFTs Validation scheme. Configure BTFS into a storage host to receive the host Node reward. Seeking organic users and building a community. Improve user experience and flow. Optimize the Web Frontend page to look more artistic. Call for investment and mentoring. <div