---
slug: "smart-strategy-trading-app-fix-dex"
url: "https://devpost.com/software/smart-strategy-trading-app-fix-dex"
title: "SleepSwap - An AI Powered Automated Trading Platform"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 649
team_size: 6
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
---

# SleepSwap - An AI Powered Automated Trading Platform

> SleepSwap is a platform to revolutionize the trading experience and making profit out of investment using strategies designed by AI Models.

[Devpost](https://devpost.com/software/smart-strategy-trading-app-fix-dex) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[developer_tools]]

**stack** amazon-web-services, chainlink, figma, finity, moralis, nginx, polygon, react, solidity, subgraph

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for a decentralized smart strategy trading app

## Body

Cover Picture Of SleepSwap SleepSwap Strategies Homepage SleepSwap Strategies Detail Page - Accumulation SleepSwap - An AI Powered Automated Trading Platform SleepSwap is a platform to revolutionize the trading experience and making profit out of investment using strategies designed by AI Models. Inspiration It is very hard to track prices all the time to insure optimal buy and sell trade for any individual trader. For example, suppose we are in the bear market and we want to accumulate LINK token for every 10% of the dip to optimize average cost of the Link token. Being active in every such dips and tracking prices is not an easy job for normal trader. Sometimes, we used to do such trades using Grid Trading available on big CEXs like Binance, Gate.io. And we came up with an idea of building strategy based automated trading platform with Decentralised experience which can work with non-custodial wallets in trustless environment. What it does User needs to deposit their funds into desired strategy pool and add a few strategy inputs such as Trigger Percentage Change and Grid Size. Once user deposits his funds, user becomes a part of the strategy pool. Now, whenever the price goes up to the trigger percentage it sells up the portion of the token and when the price goes down by trigger percentage it buys up the portion of the token. Example: -Selected Pool: ETH/USDT -Deposit Amount: $1000 USDT -Trigger Price: 10% -Grids: 4 -Current Price: $2000 USDT Now, The user’s grid amount will be $500 . The user’s buy orders will be at $1800, $1600 . The user’s sell orders will be at $2200, $2400 . Whenever the price goes below $1800 it will buy ETH for $500 and if the price goes up to $2200 it will sell ETH of worth $500. Every combo of buy and sell order grid will yield 10% of the deposited amount. And this strategy can give huge profits in long run with very less risk. And of course, the User can withdraw his stake whenever he wants. How we built it We have developed our DApp using the following technologies and services. - Smart Contract: AggregatorV3Interface for Price feeds. KeeperCompatible by Chainlink Keeper. Polygon network for deployment. - Frontend: Authentication using Web3Auth. Component building using Material UI. Deployment using AWS Servers. We choose Polygon Network for the deployment because this concept willl execute many orders sequentially which requires high gas fees. Polygon is low fees, reliable, evm supported chain which fulfils the requirements. Challenges we ran into Building a smart contract in a very short time was a bit challenging for us. Executing multiple orders of different amounts was also a challenge for us. It was the first time when we were integrating Chainlink Keeper functions and Price Feeds in the smart contract. Integration of Moralis SDK into the frontend was also a first time for us, it was challenging at the beginning but we become very comfortable as we progressed. Accomplishments that we're proud of Integration of price feeds, keeper function, and Moralis API was a true achievement for us. Triggering smart contracts using the keeper function and executing more than 1000 orders in one function call had given us a morale boost and confidence to launch this project as a product for the real-world users. What we learned Writing clean code for complex smart contracts. Chainlink price feed and Keeper integration. DApp building using Moralis SDK. Learned Web3 ecosystem in depth by top protocols sessions. Using AWS ecosystem for deployment and backend development. What's next for A Decentralized Smart Strategy Trading App After this hackathon, we will be improving the application to run multiple pools and strategies. After beta testing of the DApp, we will be launching this application into the market as SleepSwap. DAO building is also in the progress to make this product more transparent and community driven. <div