---
slug: "liminal-market"
url: "https://devpost.com/software/liminal-market"
title: "Liminal.market"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 558
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# Liminal.market

> Bridges the stock market to the blockchain world, allowing users to buy & sell stocks using their wallets. Data & smart contracts are open, allowing anybody can create products that build on top.

[Devpost](https://devpost.com/software/liminal-market) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** alchemyapi, ipfs, moralis, openzeppelin, solidity, thegraph, typescript

## How they structured the write-up

- testing
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for liminal.market
- github repositories

## Body

Testing ATTN: Any testing of the software needs to happen between 9:30 am and 4 pm EST, as this is the time when the stock market is open. Inspiration Came from me wanting to build a pension system, but limitations in law prevents crypto investment. There is no bridge for stock to blockchain so I decided to build it What it does Bridges the stock market to the blockchain. Liminal.market are for two types of customers; Stock traders & Developers. Stock traders Allows users to buy & sell stocks using blockchain technology. Users can use any wallet or service to trade stocks. This allows the user to choose the UX he likes, unlike with the current platforms, where people are locked in where they start, making it difficult and expensive to change platforms. Developers Developer's first approach will be our goal. Liminal.market opens up an avenue of product development on top of the stock market. As data & smart contracts are open, anybody can create products that build on top of Liminal.market. By writing the data on the blockchain it is available to anybody, liberating the data, and allowing anybody to use the data to create visualization and other value from the data. Using Liminal.market, DeFi services can extend their product selection & add a new revenue stream by allowing users to trade stocks and not only crypto tokens, while at the same time taking a commission on each trade, therefore increasing their revenue. How we built it Liminal.market uses Moralis as its backend service, it listens to events emitted from Liminal.market smart contract and executes orders accordingly at the broker. The orders results are then written to the blockchain using OpenZeppelin Defender. The indexing is done using TheGraph and IPFS which allows users to read the data easily. For testing, we use Alchemy to run our bot to load test the system. Liminal.market then runs on Polygon chain, although multiple chains are supported but not deployed. Challenges we ran into This is my first proper smart contract project, many issues came up. Getting a better understanding of how the EVM works. Working with hardhat had its challenges, where the wrong configuration caused delays. This is also the first project that I use TypeScript, so getting used to the setup of the project took time, but programming with it is a new life compared to Javascript. Using TheGraph and OpenZeppelin Defender was rather straightforward. Accomplishments that we're proud of Seeing how everything is working together, is a thing of beauty. I'm happy with how clean the code is for the smart contract as well as the backend. More refactoring is needed for the front end, but since the backend is the brain of the system, having that code in good condition is a great pleasure. What we learned Better knowledge of EVM, typescript, the npm libraries, and all the services, I have learned a lot from this. My realization of how simpler programming can be if everything stays on chain, blew my mind. What's next for Liminal.market Getting the project to mainnet, getting the first users, and improving the developer experience for those who want to use liminal.market, either for reading data or executing orders. Github Repositories Most liminal.market repositories are open source, there is one repository that is private. Access has been given to polygon employees. <div