---
slug: "fibril"
url: "https://devpost.com/software/fibril"
title: "Fibril"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 515
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/security_privacy"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Fibril

> Decentralized global creator support platform that allows fans to support Creators with Cryptocurrencies and NFTs

[Devpost](https://devpost.com/software/fibril) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[finance_payments]] [[immigration_refugee]] [[security_privacy]]
**substrate** [[structured_db]] [[video_visual]]

**stack** alchemyapi, chainlink, ipfs, metamask, moralis, polygon, solidity, thegraph, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fibril

## Body

Landing Page Dashboard Page A Creator Page An NFT Page Support Links Page Reward Page Inspiration The current and most popular creator support platforms are centralized and not censorship resistand. There have been many reports of these platforms suspending and deplatforming creators, which make it impossible for the creators to access their funds. Also, Some of these platforms are not available in some regions and countries which leaves the creators in those regions/countries at a disadvantage. What it does Fibril is a decentralized creator support platform that allows fans (A.K.A supporters) to support their favorite creators and idols with crypto tokens and NFTs. Creators and Supporters can access the platform from any region/country in the world without any fear of account suspension or deplatforming because the core and main features of the platform are smart contracts written and deployed to the blockchain network. Creators can be supported with crypto tokens which are MATIC, DAI, USDT and USDC. They can also be supported with NFTs. Support with the crypto tokens makes it very easy for supporters to support their creators across border without the hassle of converting their local currencies into that of the creators. Also, Using crypto tokens makes it easy for creators to withdraw their funds and convert it back to their local currencies with great ease on exchanges. Some of the current features of Fibril: Dashboard (for creators) Creator support with crypto tokens Creator support with NFTs Selling of NFTs by creators Buying of creators NFTs Withdrawal of crypto tokens and NFTs Creation of support links (payment links but for supporting creators) Random reward of supporters (randomness powered by Chainlink VRF) Creator's page Addition of social profile links How we built it Fibril is built with the following technologies: Solidity - The smart contracts is written in solidity Vue.js - The frontend is built with Vue.js Moralis - Moralis powers the connection of user's wallet, interacting with smart contracts, database and lot more. The Graph Protocol - The graph protocol is used to index the data of our smart contracts Alchemy - Alchemy powers the Fibril's NFTs data and metadata retreival IPFS (web3.storage) - IPFS is used to store creators profile images and support links JSON Chainlink - Powers the tokens price smart contract (using Chainlink Data Feeds) and also Random Number Neneration (using Chainlink VRF) Polygon - The smart contracts are deployed to Polygon Mumbai Challenges we ran into Below are some the challenges encountered while building this project: internal errors when chainlink vrf calls the "fulfillRandomWords" callback function issues deploying asubgraph for the first time files not reflecting on ipfs after uploading to ipfs using web3.storage for hours some couple errors when using web3.storage Accomplishments that we're proud of built a POC of the idea What we learned learnt how to work with Chainlink data feeds and Chainlink VRF learnt how to index smart contract data with The Graph protocol What's next for Fibril optimize and ensure security the smart contract from vulnerablities partner and work with social influencers and creators to bring them and their fans to the platform <div