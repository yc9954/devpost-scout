---
slug: "shiro-storage"
url: "https://devpost.com/software/shiro-storage"
title: "Shiro Storage"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 460
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
---

# Shiro Storage

> A platform for decentralized apps to store files - of any kind. You don't need to set up any "web2" APIs, services or daemons. All you need is a Solidity contract and a client that calls it.

[Devpost](https://devpost.com/software/shiro-storage) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** chainlink, docusaurus, ipfs, nestjs, polygon, quicknode, solidity, typescript, web3.storage

## How they structured the write-up

- inspiration
- features
- details
- challenges we ran into
- services used
- what's next for shiro storage
- relation to shiro share

## Body

Docs Architecture Inspiration There was a lack of storage platforms for the decentralized web that could work with only a client and a contract. For example, IPFS practically requires you to host a node yourself or use a provider to pin it if you need the file later. Services like web3.storage require you to pay in USD and cannot be done via a contract function call. So we sought out to build something that handled all the heavy lifting and gave a simple interface to its users (who are developers). The possibilities (use cases) for Shiro Storage are endless. Features 💾 Multiple storage backends : files can be uploaded to any one of the storage providers including IPFS and web3.storage . ✨ Easy to use : all you need is a client (UI) and a Solidity contract. 📖 Open : along with the whole codebase being open source, we do not require any special libraries. Only two very common operations are needed - uploading files to a custom IPFS relay and calling a smart contract function. 🚮 Automatic garbage collection : using Chainlink Automation , files are cleaned up once they expire. 💸 Simple pricing : all you need to do is send value (ETH/MATIC) to the contract call. Pricing is based on USD but payments are taken in ETH/MATIC with the help of Chainlink price feeds . ⛓️ Safe and reliable : the file sizes are verified on-chain using a Chainlink Any API call, which are fulfilled by a custom Chainlink Operator Node Details The documentation has all details, including the architecture , usage guide and self-hosting guides . Challenges we ran into Because of the custom nature of our Any API call, we could not find oracles to fulfill them on the test networks. To tackle this, we deployed our own Chainlink Node with a custom jobspec.toml . This makes use of a Quicknode node heavily. Services used Note: these were all necessary to bring this project to fruition. Chainlink Price Feeds: source code Chainlink Automation: source code Chainlink Any API: source code IPFS: deployment docs , storage provider web3.storage: storage provider Fleek: docs deployment Quicknode: used as the main Eth node for deploying contracts and for the chainlink operator node (which made very heavy use of the websocket API) Polygon: we used Polygon Mumbai as our testnet for all contracts. What's next for Shiro Storage Implement all of the planned storage providers Accept payment in any ERC20 token - currently only accepts ETH/MATIC Relation to Shiro Share While Shiro Share is built on Shiro Storage, they are completely different products with different use cases. Shiro Share is a simple app for anyone to share files whereas Shiro Storage is a generic storage platform for the web3. <div