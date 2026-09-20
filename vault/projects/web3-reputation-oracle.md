---
slug: "web3-reputation-oracle"
url: "https://devpost.com/software/web3-reputation-oracle"
title: "Web3 Reputation Oracle"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 532
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Web3 Reputation Oracle

> Offchain computation of web3 identity for anti-sybil defense. Computation and ranking of an identity will be exported as a chainlink adapter, which smart contracts can use.

[Devpost](https://devpost.com/software/web3-reputation-oracle) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]] [[sensor_telemetry]]

**stack** ceramic, cyberconnect, cybergraph, express.js, ipfs, moralis, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for web3 reputation oracle

## Body

Reputation Score on Ethereum Mainnet displayed for an address on portal List of POAPs and NFTs on Ethereum collected for the address displayed on the portal Inspiration With the ever-increasing advancements in Web3, Decentralised Identity (DID) is gaining widespread importance as a way for people to be in control of their personal data, as well as verify others' identities in a transparent way. Central to the notion of decentralised identity is the idea of evidence-backed reputation, i.e a permanent, timestamped record of the person's transactions, assets, accomplishments and activities on the blockchain. Though there are multiple ways a person's reputation can be measured, there is a lack of a streamlined system which collects information about the person on Web3 through multiple sources (including off-chain sources), in a sybil-proof way. We create a platform that acts as a "reputation oracle" - it computes a person's reputation score off-chain by collecting information about the person through various sources (eg: on-chain transaction history, NFT and POAP ownership, ERC 20 tokens etc) and exposes them through a Chainlink adapter. Our system is anti-sybil, is off-chain, and the adapter can be easily integrated in existent smart contracts for other developers to get reputation scores. What it does Our platform aggregates and analyzes on-chain data on the fly using Moralis SDK and uses it to generate an on-chain "reputation" score. Data aggregated includes NFT ownership, POAPs, on-chain transaction history, and ERC-20 tokens, and decentralized identity information. Users can find reputation scores and associated aggregated data for different addresses via the search bar as well as by connecting their wallets and manage their personal decentralized identity information via ceramic. We also include a backend API and chainlink adapter so that smart contracts can access and utilize our reputation scores and data. The platform currently supports Ethereum, Avalanche, Polygon, and Fantom ecosystems. How we built it Our front-end app was built using React and Typescript. The Moralis Web3 SDK was used to fetch and aggregate on-chain data for users and Ceramic + Cyberconnect (i.e CyberGraph and Ceramic social graph) were used for decentralized identity integrations. Our backend API was built using Express, Node, and Typescript. Both app and API were deployed via Heroku. Data is stored and shared through IPFS. Challenges we ran into Filtering out "noise" such as spam/scam erc-20 tokens and NFTs from aggregated data. Deriving a formula for on-chain reputation using gathered metrics. Accomplishments that we're proud of Integrated our off-chain data aggregation and reputation score with on-chain smart contracts via Chainlink adapters. Utilized multiple Web3 SDKs and libraries (Moralis, Ceramic, and CyberConnect). Worked asynchronously across 4 different timezones. What we learned We learned that blockchain data is plentiful but efficiently aggregating and integrating it is hard. Tools for extracting insights from on-chain data and creating useful metrics out of it are in short supply. We believe that a combination of off-chain computing with on-chain data is necessary to build the next generation of dApps. What's next for Web3 Reputation Oracle Add filtering to erc-20 tokens using an "allow list" and "dust" filtering. Fine-tune on-chain reputation score formula Onboard additional chains Integrate with DEXs and auto-compounders to more accurately calculate value of LP and auto-compounder tokens. <div