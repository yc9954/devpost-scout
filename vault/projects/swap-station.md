---
slug: "swap-station"
url: "https://devpost.com/software/swap-station"
title: "Swap Station"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 787
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Swap Station

> Swap Station is a one of a kind marketplace for NFT collectors to showcase, discover, and swap NFTs across different blockchains. So instead of selling NFTs for crypto, you swap them!

[Devpost](https://devpost.com/software/swap-station) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**domain** [[finance_payments]] [[security_privacy]]
**substrate** [[financial_record]] [[structured_db]]
  <sub>weak: video_visual</sub>

**stack** mongodb, nextjs, node.js, react, solidity, tronbox

## How they structured the write-up

- what it does
- how we built it
- technologies
- challenges we ran into
- accomplishments that we're proud of
- future work
- preview screenshots

## Body

Discover NFTs to swap Import any NFT from different chains See something you like? Make an offer to swap! Find all kinds of NFTs Manage your collections View all your offers What it does Swap NFTs across different blockchains SwapStation.io is a one of a kind marketplace for NFT collectors to showcase, discover, and swap NFTs across different blockchains. So instead of selling NFTs for crypto, you are swapping them for other NFTs whether they're on the same blockchain or across different chain. You can import any NFTs to SwapStation, put your token up for trade and start receiving swap offers. Likewise, if you see anything you like you can place an offer using a token you wish to exchange for. The swap takes place when both parties accept the trade. One of the best things about SwapStation is that nearly everything is free. We wanted to make this platform available to everyone, so no gas fee is required when importing, creating listings and making offers. The only time a payment is required is when an actual swap transaction takes place. Features Import any NFT into your personal collection. Put your tokens up for trade by creating discoverable listings. Browse other listings to find interesting NFTs where you can offer up your own NFT to exchange for it. Manage your collections, listings and offers through a personal dashboard. Accept offers for your NFT to make an exchange. Swap transactions takes place in the blockchain and is immutable. No gas fees for importing, listing and making offers. You only pay when a swap is confirmed. How we built it Seller/Maker imports NFT from supported blockchains into SwapStation, then puts their NFT up for trade by creating a listing. Buyer/Taker browses available listings and make an offer on a listing by importing their own NFT into SwapStation. If seller accepts an offer, the listed NFT is transfered to the buyer and the offered NFT is transfered to the seller. Seller can cancels a listing and remove it from discoverability and all pending offers. Buyer can retract an offer for a listing if it has not been accepted by the seller yet. Same-Chain Swap Process Cross-Chain Swap Process Technologies Architecture Web Application (UX) The frontend web application is developed in React using the NextJS framework. Currently supports integration with TRON blockchain via TronLink and TronWeb. Upcoming integrations with Ethereum, NEAR and NEO blockchains. API There is a REST API that interface between the frontend web application with the underlying offchain database. The API is developed in NodeJS Express. We have plans to expand this API in the future to allow for third party integrations with SwapStation. Offchain Database Most of the data powering the frontend application is held in an offchain database, which includes imported NFT collections, listings, offers and carbon copies of swap tranasction records. The only time where a transaction takes place in the blockchain is when an offer is accepted and a swap needs to take place. The primary purpose of this offchain database is to allow for zero fees so anyone can create as many listings and offers as they wish without worrying about cost, and they only need to pay once they decide to make a swap. Blockchain Smart Contract (TRON) SwapStation : TRON Smart Contract writen in Solidity repesenting the swap contract. This contract is responsible for the swap transaction that takes place when an offer is accepted. See SwapStation Contract functions for functions. NFT : A sample ERC-721 NFT contract using OpenZeppelin standard. We are using this contract as a sample for developing and testing the integration with the application. Challenges we ran into The challenging part about trying to build multichain support is that each blockchain has their own development stack, integration means and various NFT standard: TRC-721 (TRON), ERC-721 (Ethereum), NEP-171 (NEAR), NEP-11 (NEO). This meant that we will need to build contracts and integrations for each blockchain that we want to support. We forsee this as a huge task but we're taking things one step at a time by starting with TRON. Accomplishments that we're proud of We're particularly happy to complete the MVP in a short time, and to have developed the technical details required to bring this project to life. Future work There's a lot of work to be done before the product could be considered production ready: Prepare a strategic roadmap of the project which will include development and marketing efforts. Build the core team. Refine the user experience for better NFT discovery and collections management. Expand the number of supported blockchains. Penetration tests and close any gaps in security vulnerabilities. Implement transaction fees as a monetization strategy so the project can be self-sustainable. Preview Screenshots <div