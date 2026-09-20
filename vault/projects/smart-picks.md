---
slug: "smart-picks"
url: "https://devpost.com/software/smart-picks"
title: "Smart Picks"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 806
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/developer"
  - "substrate/financial_record"
---

# Smart Picks

> Smart Picks is a dApp that lets users create and enter into NCAA March Madness betting pools.

[Devpost](https://devpost.com/software/smart-picks) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**user** [[developer]]
**substrate** [[financial_record]]

**stack** alchemyapi, avalanche, chainlink, ethers, fleek, hardhat, ipfs, material-ui, metamask, moralis, polygon, react, remix, sportsdata.io

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smart picks

## Body

Homepage to view all pools Our custom, interactive bracket UI Inspiration Our team strongly feels that decentralized betting platforms are the next logical step for DeFi. Our goal was to create something that we could see ourselves using, and increase the adoption rate of blockchain and cryptocurrencies. Per Visual Capitalist's research, we know that online sports betting is a burgeoning industry. We see an opportunity to contribute to this space and believe that a substantial part of this market would move to trustless blockchain solutions. When the idea for Smart Picks came up, we knew immediately that we wanted to do it. We knew this would be an amazing, fun thing to create, with plenty of room for us to learn and grow as engineers. Now that Smart Picks is built, we want to continue to broaden its use cases and bring it to market in time for the 2022 March Madness Tournament. What it does Smart Picks is a dApp that lets users create and enter into NCAA March Madness betting pools. The UI allows users to build and save brackets, with an easy-to-use interface. Each pool is a smart contract, which uses Chainlink price feeds to provide the up-to-date price in $ETH, $MATIC, or $AVAX. We use SportsDataIO for our Oracle’s data source and, to maintain proper decentralization, a keeper contract will close all of the pools 24 hours after the tournament has ended. How we built it Front End The front end is a React app that uses Material UI. We used Moralis to connect to our smart contracts, and to allow us to switch between our supported chains. Metamask is used to facilitate all transactions, as well as handle authentication. Smart Contracts Each chain has its own Pool Factory smart contract, through which users can generate their own pool. All smart contracts maintain strict rules for buy-in price, number of entrants allowed, and one bracket per user. Oracle We deployed Chainlink’s Oracle smart contract and pointed it at our node. We hosted our Chainlink node and related jobs on LinkPool's NaaS. Deploying Our smart contracts were deployed using Hardhat scripts, and our dApp is deployed on IPFS via fleek. Challenges we ran into The first challenge we faced was setting up our smart contracts. We spent a lot of time reading through Solidity documentation and testing things out on Remix before we finally got everything set up as we wanted. The biggest challenge we had was setting up our oracle node to close pools. Not only did we have to learn how to set up a .toml job, but also we had to build an API call to SportsDataIO. Accomplishments that we're proud of Smart Contracts Both of us are new to Solidity, and so we are especially proud of the smart contracts that we built. We’re very happy that we were able to learn Solidity in such a short period of time and get everything working as we had envisioned. Bracket Selection We’re very pleased with how the bracket selection UI turned out. We managed to get the games to re-render appropriately from a binary tree structure. First Hackathon This is Cole’s first hackathon! I (Beckylee) have done a handful before, and I am incredibly proud of how well my partner has done. It’s been wonderful to pair with him and watch him make enormous code contributions to our project. What we learned Beckylee I am completely new to the crypto space, so it was very interesting to learn about DeFi and blockchain. I now feel like I have a good sense of the tech and how impactful it all is, across all industries. To be more specific, I learned Solidity, how to use MetaMask, Moralis, Hardhat and IPFS. A month ago, I had never heard of any of them, and now I can have a full conversation about implementation! Cole I learned Solidity, and wrote my first smart contracts. I love that I now know details and quirks of the language, and feel confident in my ability to write more. Also, I had only ever used class components in React, so this was my first time working with functional components. I’ve been a user of DeFi for many years, so learning the technical side of these things completely solidified my belief that it will gain mainstream adoption. What's next for Smart Picks In the future, we would like to expand support to more blockchains, allow more customization on pools, and allow pools and brackets for other sporting events. We’d also like to bolster our payouts with Superfluid, and set up an ENS for our dApp. We plan to continue work on Smart Picks after the hackathon ends, as it’s been so fun to work on and we both want to see it through all of the features we’ve discussed. <div