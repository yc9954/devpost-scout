---
slug: "flex-nodes"
url: "https://devpost.com/software/flex-nodes"
title: "Flex Nodes"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 394
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
---

# Flex Nodes

> Get on-chain activities data from others chain into smart contract using graphql and store on ipfs operate by Chainlink.

[Devpost](https://devpost.com/software/flex-nodes) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets


**stack** chainlink, digitalocean, docker, firebase, foundry, ifps, next.js, quicknode, solidity, typescript, web3.storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flex nodes

## Body

Inspiration Now almost all decentralized applications (Dapps) calculate or compute data on off-chain and push results back to on-chain smart contracts, because calculating on-chain is very expensive and geting onchain data into the smart contract is very hard to setup and maintain. This approach makes smart contracts not transparent and depends on protocol relayer or node that make a single point of failure. Flex node provide query on-chain data service using graphql and store it on ipfs and compute those data on chainlink node layer. What it does Flex node allows users to write graphql query commands or our template command to query on-chain activities such as borrows events in compounds on Polygon mainnet or nft holding in opensea on Ethereum mainnet and store those file as json file into ipfs via web3.storage. When smart contract want to calculate those file, we also provide chainink external adapter to get those file and compute on chainlink node and send result back into smartcontract. How we built it Our stack separates into 3 parts, Chainlink node, Chainlink external adapter, flex-contract and flex-frontend. Chainlink node We create our own spec and job to parse data from our external adapter on polygon mumbai testnet. Chainlink external adapter We have 2 external adapters that do different tasks. Get on-chain data using graphql command and return cid from ipfs. Get specific data that is stored on cid. Flex contracts Sample contract that gets on-chain data and how to build requests from our flex-node. Flex frontend Our frontend uses next.js framework and chakra ui and stores query data on firebase firestore. Hosting in vercel application. Challenges we ran into This project use almost every api from chainlink but most challenge part is seting up chainlink node how to define jobs that work with our external adapter. Accomplishments that we're proud of Understanding how chainlink nodes work with smart contracts. Build product from scratch until deploy it within 3 weeks. What we learned How to chainlink network with smart contract also work with external adapter, external initiator. Foundry, how to write unit tests in solidity language. Chainlink external adapter. Graphql Ipfs and web3.storage What's next for Flex Nodes The query creator has incentive from everyone using their query command. Dynamic query variable. Gas optimization. Support Non-evm chains. Support more third party query on-chain data. Create a fully unit and integration test. <div