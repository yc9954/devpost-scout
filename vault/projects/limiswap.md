---
slug: "limiswap"
url: "https://devpost.com/software/limiswap"
title: "LimiSwap"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 801
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# LimiSwap

> LimiSwap is a decentralized limit order exchange for UniSwap powered by Chainlink Keepers.

[Devpost](https://devpost.com/software/limiswap) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** alchemyapi, chainlink, firebase, google-cloud, hardhat, ipfs, moralis, nextjs, solidity, thegraph, typescript, uniswap

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for limiswap
- source code
- try it out!

## Body

Welcome to LimiSwap Custom tokens are also supported Modern design, inspired by Uniswap View your orders Also support WalletConnect Inspiration What AMM lacks is being able to place limit orders. It is possible to make a backend that tracks the price and execute when it needs to, but the backend is centralized and can result in single point of failure. Even worse, the "admin" of the server has full control over user's orders. The solution is to store the limit order data on chain and use decentralized oracle service such as Chainlink to monitor and execute orders. That way, there will be no single point of failure and users can get cryptographic proof of their orders. What it does LimiSwap is a decentralized limit order exchange for Uniswap powered by Chainlink Keepers. Users can create limit orders for any token at any price. How I built it Smart contract The LimiSwap contract is written in Solidity. It stores user's limit order information such as token addresses and target price. Chainlink Keeper calls the checkUpKeep function to check for orders that needs to be executed. For unit testing, I used hardhat framework and forked the live network to test with real world data. Frontend The frontend is built using NextJS with Typescript and React Bootstrap. It is completely original and the theme is inspired by Uniswap. The challenge was to get real time data such as user balance, token prices, and order status quick as possible to display them to the user. Making RPC requests every time is slow, and by using Moralis Deep Index for token data and Moralis Server for the order status greatly minimized number of calls to the blockchain. Backend The backend is built on Moralis. It listens for OrderCreated, OrderFilled, OrderCancelled events and logs them to the database. I also made a cloud function that returns all orders filtered by user address. Another backend I built is the Uniswap subgraph hosted on Google Cloud. It monitors any change in liquidity pools and can provide spot prices. However, there was an issue syncing data from Kovan network, so for the moment, the frontend simply make RPC requests to the blockchain. Challenges I ran into There were many challenges I ran into durning the development process. One of the biggest challenge was fetching spot prices and calculating amountOut. First I built my own Uniswap subgraph node on Google Cloud but there was an issue syncing data from Kovan network. I struggled to find the solution for several days, and I eventually decided to directly talk to the blockchain to get pool information. The next problem was calculating prices and amountOut from that raw information. It took me long time but by digging into source code from Uniswap, I was able to figure it out. I could have used Quoter contract from Uniswap that calculates all of those, but it will require to do multiple RPC calls and would result in poor user experience. Accomplishments that I am proud of I am proud that I was able to build a working full stack web3 application all by myself in 2 weeks. Even for a simple exchange like this, if I try to focus on tiny details such as performance, it took a lot of effort to achieve it. And last but not least, I am proud that limit order program worked! What I learned From this hackathon I learned many of the services from the sponsors such as Chainlink Keepers, Moralis, and TheGraph. Even for the service that I did not use, I learned the basics and the uses cases from the workshops. What's next for LimiSwap LimiSwap still has lots of places to improve. First, the support for multi route swaps. Currently, it only supports A=>B and not A=>C=>B. This can be done by calculating the best trade using Uniswap's routing SDK and storing the route information on blockchain. Second, finding a smarter way to execute perform upkeep. Currently, the keeper can only execute 1 order at a time. This could be an issue if there were thousands of orders. And last but not least, Sushi's BentoBox integration. While the orders are pending, the funds are simply sitting in the contract, doing nothing. With the intergation of BentoBox, users can earn yields from strategies such as lending and staking while they are waiting for the order to fill. Source code This project is public & open source. Cloning, forking, using it as a template is welcome. Smart contract: https://github.com/REGO350/limiswap Frontend: https://github.com/REGO350/limiswap-interface Backend (moralis): https://github.com/REGO350/limiswap-backend Backend (subgraph): https://github.com/REGO350/uniswap-v3-subgraph Try it out! You can request airdrop for the test tokens. Go to one of the links below, connect your wallet then click airdrop > write. Get mock LINK: https://kovan.etherscan.io/address/0xc95b247049a8cc8e7F68Bb6fFD9Eee3c97769118#writeContract Get mock USDC: https://kovan.etherscan.io/address/0x3376D8CDCD1c6feBaf41559a39a8AcC91AD06A47#writeContract Get mock LIMI: https://kovan.etherscan.io/address/0x0a82858Ff17f84A5dF405F2504bc7f71fdbD873D#writeContract LimiSwap website: https://limiswap.web.app/ <div