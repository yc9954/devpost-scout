---
slug: "subscrypt"
url: "https://devpost.com/software/subscrypt"
title: "Subscrypt"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 512
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# Subscrypt

> Subscrypt: Revolutionizing subscriptions with cross-chain payments between any EVM chains, per-second billing, and seamless web2-web3 integration, all powered by dynamic NFT technology.

[Devpost](https://devpost.com/software/subscrypt) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[finance_payments]]
**substrate** [[financial_record]]

**stack** chainlink, cloudflare, docker, hardhat, nestjs, nginx, openzeppelin, react, solidity, viem

## How they structured the write-up

- inspiration
- what it does
- how we built it
- tech stack
- used chainlink technologies
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for subscrypt

## Body

Home page Shop page My subscriptions Shop's owner dashboard Balance inside system (support BSC/Polygon). For making payments/rewards Shop creating page Opensea with dNFT. You can see expire date of subscription CCIP transaction details (after pay subscription in Polygon network via BSC) Figma UI/UX smart contract sketches Inspiration Subscrypt was inspired by the need to bridge the gap between traditional subscription models and the evolving blockchain ecosystem. Our goal was to create a platform that leverages blockchain's transparency and flexibility while remaining accessible to both web2 and web3 users. What it does Subscrypt allows store owners to create subscription-based services on various blockchain networks like Ethereum, Avalanche, Polygon and etc. Customers can pay in their preferred cryptocurrency, while stores receive native network currency. Key features include cross-chain payments, per-second billing, and integration with web2 services through dNFTs and backend connectivity. How we built it We built Subscrypt using a combination of blockchain technologies and traditional web services. The platform integrates with networks like Ethereum and uses Chainlink Data Feeds for accurate currency conversions. We also incorporated dynamic NFTs to store and manage subscription data, and services like Zapier for backend integration. Tech stack Frontend: React, viem, chakra-ui, wagmi Backend: NestJS, Prisma, PostgreSQL Infrastructure: vps, Cloudflare, NGINX, Docker Smart contracts: Solidity, Hardhat, Openzeppelin, Chainlink Used Chainlink technologies Data feed (the seller sets the subscription price in US dollars. Next, a payment contract is deployed in each supported network. This contract uses Chainlink Datafeed to find out the subscription price in the native currency of network (like BNB, ETH, MATIC). For example, if the subscription price is $100 per month, and the client pays on the BSC network (although you can pay at any), then the contract uses feed BNB/USD) CCIP (this technology is used to make payments in various networks, regardless of which network the shop is located in. The user pays for the subscription and then, using CCIP, the smart contract is linked to the contract in the target network (where the shop is located) and issues the subscription to the user there in the form of an NFT) Challenges we ran into One of the biggest challenges was ensuring seamless cross-chain functionality and integrating various blockchain networks. Another challenge was implementing the per-second billing mechanism, which required innovative approaches to manage microtransactions efficiently. Accomplishments that we're proud of We're proud of creating a unique per-second billing system, which allows for a more flexible and fair subscription model. Our integration of web2 and web3 technologies and the ability to manage multiple subscriptions through one deposit also stand out as key achievements. What we learned Through this project, we've learned about the complexities of integrating different blockchain technologies and the importance of user-friendly design in blockchain applications. We also gained insights into the potential of dynamic NFTs in managing real-time data. What's next for Subscrypt Moving forward, we plan to expand the network compatibility of Subscrypt, enhance our dNFT technology, and explore more integrations with web2 services. We also aim to introduce features for one-time payments and improve overall platform scalability and security. <div