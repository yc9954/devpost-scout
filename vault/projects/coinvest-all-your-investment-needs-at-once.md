---
slug: "coinvest-all-your-investment-needs-at-once"
url: "https://devpost.com/software/coinvest-all-your-investment-needs-at-once"
title: "Coinvest - All your investment needs at once"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 373
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Coinvest - All your investment needs at once

> Create investment baskets according to your need and start investing lumpsum or SIP investment.

[Devpost](https://devpost.com/software/coinvest-all-your-investment-needs-at-once) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets


**stack** alchemyapi, amazon-web-services, chainlink, ethersjs, hardhat, ipfs, mongodb, moralis, nextjs, nft, node.js, polygon, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for coinvest
- update

## Body

New Dashboard New Baskets Layout New Connect Wallet New Manage Basket New Create Basket Inspiration Most of us invest in cryptos either through DEX or CEX, but there is no proper way to manage your investment goals. The idea here is to create an investment platform, where users can invest in multiple crypto tokens and staking pools at once in lump sum or SIP. First, the user has to create an Investment Account to seamlessly make investments. This account will be secured with a randomly generated NFT by using Chainlink VRF. Only the owner of that NFT can access this account. Now, users will be creating an Investment Basket for their investment goal by selecting investing ERC20 token which he/she wants to invest in and by selecting the numbers of ERC20 tokens he/she wants to invest in. After creating an investment basket you can start investing a lump sum amount or start a SIP. What it does Coinvest provides you with a simple way to manage your investments according to your goals. Whenever you invest an amount into the basket, the basket will split that amount equally for every token and buy tokens from uniswap. Every token bought from uniswap gets stored in your investing account which is protected by a randomly generated NFT. How we built it We are currently testing it on Polygon Mumbai testnet. For the analytics data we are using The Graph Portocol. Challenges we ran into We ran into liquidity issues while trying to work with Uniswap.**** Accomplishments that we're proud of We were able to build a prototype that allows users to create an Investment basket and add investing tokens to it, and users can invest the lumpsum amount or start SIP. What we learned While building this app we have learned new things about chainlink and defi. What's next for Coinvest Right now we are facing some issues while investing an amount into the basket, our next plan is to remove all possible bugs and We also want to add support for staking pools as well. Update Entirely rebuilt from the ground up, Now it has a new frontend, new Off-chain backend, and baskets are now off-chain and can be made without a gas fee. <div