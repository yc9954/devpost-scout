---
slug: "spellbound-pools"
url: "https://devpost.com/software/spellbound-pools"
title: "Spellbound Pools"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 455
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/web_dom"
---

# Spellbound Pools

> Concentrated liquidity made easy!

[Devpost](https://devpost.com/software/spellbound-pools) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[web_dom]]

**stack** alchemyapi, amazon-web-services, chainlink, chakra-ui, ethers, hardhat, node.js, rainbowkit, react, solidity, thegraph, typescript, uniswapv3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spellbound pools

## Body

Sequence Inspiration The idea came out of personal needs at first as concentrated liquidity is highly attractive but hard to deal with. Moreover, we know many people who want to invest but cannot dedicate significant time to that and are afraid of traditional finances. Trust-minimized but easy-to-use solutions would really drive DeFi adoption forward. Here we've got our mission! What it does Spellbound Pools allows users to simply stake some money and watch how smart contract invests them in concentrated liquidity pools and manage positions further. It does so with the help of UniswapV3 API and Chainlink Automation. To understand how it works let's look at the detailed sequence After investing users can go to their Dashboard and check progress whenever they want. More details in docs How we built it Frontend: React app with Chakhra UI, Moralis, Ethers, and many other libraries. Uniswap-sdk has been used to get pool information and perform necessary computations. Prices obtained from Coingecko API. Frontend is deployed to AWS Amplify. Backend: Express app which computes the best position and estimates daily return based on last month's data. App queries UniswapV3 data from TheGraph GraphQL API. The backend is deployed as AWS Lambda. Blockchain: Hardhat and Solidity for smart contract development Chai and Ethers for testing Chainlink Automation to run position updates. UniswapV3 smart contracts are used heavily. @openzeppelin for some math and token standards. The website domain is registered under spellboundpools.com and linked to AWS Amplify. Documentation is available with Gitbook Challenges we ran into UniswapV3 daily return estimation is quite tricky, especially if it is implemented in a general way for every currency and network. Chainlink Automation is difficult to debug because when me calling performUpkeep result could be different from Keeper call the same function. Chainlink Functions are not supported on Goerli and UniswapV3 is not supported on Sepolia yet. So it took some time to decide on Polygon Mumbai as the preffered testnet. Chainlink Functions only support vanilla javascript so implementing UniswapV3 computation logic and GraphQL queries would be very time-consuming. VERSE-WETH doesn't exist on Goerli so we have to create it ourselves and provide initial liquidity. Accomplishments that we're proud of Nice-looking and easy-to-use UI Highly capable Smart Contract Re-mint position automation Mumbai and Goerli It is all tested and really works! What we learned Smart Contracts are hard to troubleshoot, especially if writing something complex When doing something new it always takes more time than you expect :) A LOT about Chainlink, Uniswap, and Web3 development in general. What's next for Spellbound Pools Improve UX and enhance functionality Secure smart contracts and the product itself Invest more time into experiments with Chainlink Functions Deploy to mainnet Open to the world Support more networks <div