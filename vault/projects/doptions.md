---
slug: "doptions"
url: "https://devpost.com/software/doptions"
title: "dOptions"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 510
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# dOptions

> A Truly Decentralized P2P Crypto Options Protocol

[Devpost](https://devpost.com/software/doptions) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** nextjs, python, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for doptions
- team

## Body

Landing Screen Base Screen Writing Option Screen Buying Options Screen Positions Screen Inspiration There has been a significant increase in the volume of Options being traded in the equity markets, the volume of Options has exceeded the volume of equities (double or triple in some countries). In order to attract more traders (in turn more web3 users), the ecosystem needs more derivative protocols providing diverse experiences for users. There are a few Options protocol on already on-chain but most of them are not decentralized in real sense as they don't allow individuals to write Options and none allows for customizability. In order to tap in this gap, we came up with dOptions - a truly decentralized options protocol. What it does dOptions allows users to create Options on their own terms, allowing customizability. They can write/sell both type of options - CALL & PUT. The protocol allows interested buyers to acquire these customized contracts and execute the change of assets if the required conditions are met. Apart from offering basic CALL/PUT options, dOptions will provide different types of contracts such as Rainbow Options, Barrier Options, etc in future, currently dOptions provides functionalities of Basic and Basket Options . Moreover, dOptions will support Automated Strategy / AI Agent clients, currently a basic version of automation client is available for users to try. How we built it We built the whole project from scratch for the Block Magic Hackathon. ChainLink Price Feeds are used for both on-chain and off-chain price related queries. AggregatorValidatorInterface is used and feed addresses are obtained from the documentation . Smart contracts are written in Solidity using the Foundry framework. Foundry tests and scripts are used for fork testing and deploying contracts. Frontend is created using NextJS (typescript) and libraries such as ethers, web3, web3modal, etc are used for interacting with the contracts on-chain. Automation client has been built using python and web3.py library. What's next for dOptions We are building dOptions for the mainnet but before we deploy it, changes need to be made as per the roadmap below: July-August Improve UI/UX Implement Frontend for Basket Options & Secondary Marketplace Implement Support for EVM Chains like Linea, Canto September-October Include More Varieties of Options Implement Support for Non-EVM Chains like Starknet, ICP, Solana and Substrate Chains Raise Funds for Marketing & Trading Incentives November Soft Launch Start Working on AMM Based Secondary Marketplace for V2 ... To Be Decided Team We are experienced web3 developers who have been building DeFi primitives on different chains for gaining knowledge. We have built around 10 different projects across chains like Solana, Astar, Internet Computer, EVM Chains, etc. Our lead developer also possesses a specialization certificate in Decentralized Finance . We recently created an open source organization named "PsyCode Labs" which focuses on building next gen products across different chains and connect them together as "Future is Multi-Chain". We are very much excited to create the first truly decentralized options protocol, with our knowledge and experience we look forward to create a protocol which helps in increasing traction for DeFi. <div