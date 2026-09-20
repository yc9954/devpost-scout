---
slug: "blockchain-chainlink-satellite-broadband-supply-chain"
url: "https://devpost.com/software/blockchain-chainlink-satellite-broadband-supply-chain"
title: "Blockchain/Chainlink : Satellite Broadband Service Chain"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 663
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/general_public"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Blockchain/Chainlink : Satellite Broadband Service Chain

> Mint Satellite Broadband NFTs

[Devpost](https://devpost.com/software/blockchain-chainlink-satellite-broadband-supply-chain) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[civic_government]] [[finance_payments]] [[supply_logistics]] [[transportation]]
**user** [[general_public]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** alchemyapi, chainlink, erc721, erc721uristorage, google, hardhat, infura, ipfs, javascript, kovan, metamask, moralis, node.js, npm

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for blockchain/chainlink : satellite broadband service chain

## Body

Mint Satellite Broadband NFTS - Front-End Chainlink-Node Chainlink-Node-Job External-Adapter-Bridge Inspiration Providing connectivity to the underserved remote communities with satellite broadband using cryptographic truth. What it does I believe the future of signing up and serving the underserved communities with telco broadband service will be in the form of dynamic NFTs. It is a futuristic approach proof-of-concept for automating manual processes in the Satellite Broadband Service by replacing paper contracts with hybrid smart contracts across synergies from suppliers/vendors, finance, sales, logistics with assets tracking to both partners and end users. It demonstrates the journey of solutions in both equipment and bandwidth as dynamic NFTs on blockchain augmented by the use of the Chainlink oracle to connect off-chain data feeds and can also trigger off-chain events. The Satellite Broadband Service Chain is the sequence of activities and processes involved in shipping equipment from suppliers/vendors to the broadband satellite operator. The satellite operator then package them together with broadband solutions to serve telecommunications operators, internet service providers, governments, other service providers and end users. Moreover, this project in itself is a DeFi payment gateway for remote underserved communities. It also bridge the gap that is not provided by the existing banking infrastructure. In summary, this project is the world's first direct to consumer marketplace for satellite broadband solutions and for asset-backed dynamic NFTs. It will benefit all stakeholders with the empowerment of cryptographic truth to ensure definitive truth in providing connectivity to the underserved communities by bridging the geographical boundaries thus alleviating the digital divide and leaving no one behind. How I built it Components Smart Contracts - Hardhat ( https://github.com/EdwinLiavaa/satellite-broadband-service-chain ) Front-end - Moralis ( https://github.com/EdwinLiavaa/satellite-broadband-service-chain-ui ) External Adapter - Google Cloud ( https://github.com/EdwinLiavaa/marine-traffic-external-adapter ) Chainlink Node - Google Cloud ( https://github.com/EdwinLiavaa/marine-traffic-chainlink-node ) Tools and Technologies Alchemy Ethereum Chainlink Google Cloud Hardhat Kovan Test Network Rinkeby Test Network Metamask Infura Moralis Openzeppelin Solidity Web3JS IPFS Opensea ERC721 ERC721URIStorage node.js npm yarn python Challenges I ran into Contract code size exceeds 24576 bytes Running the setup.sh script to upgrade Chainlink Node from 0.7.5 -> 0.9.10 -> 0.10.3 -> 1.0.0 crashes the Google Kubernetes Engine Cluster service and will settle on 0.7.5 for the hackathon. Datalastic Maritime API User Agreement – Terms of Service 4.1. Subject to your compliance with the Terms of this Agreement, Datalastic grants you a non-exclusive, non-transferable right to access and use the Services. Any sort of information and data acquired by being a Registered User of Datalastic is for internal use only. The User shall use such information and data for his/her use only and shall not share his/her API access information or purchased databases without the explicit consent of Datalastic. 4.2. Except as otherwise set forth herein, The User shall have no other rights with respect to the Data, including without limitation, any right otherwise to use, distribute, furnish or resell the Data to third parties or any portion or derivative thereof. Gas Fees on Ethereum Mainnet Accomplishments that I'm proud of This is the world's first direct to consumer marketplace for satellite broadand solutions and for asset-backed dynamic NFTs. What I learned Can turn on optimization to fix Contract code size exceeding 24576 bytes. Can deploy the Marine Traffic External Adapter on Chainlink Node as a Service (NaaS) with version 1.0.0 Currently looking for a Maritime API Provider with an exclusive right allowing to distribute, furnish or resell the Data to third parties. Can deploy external adapter on Polygon Mainnet to ease Gas fees. Another area of interest for a use case of the Marine Traffic External Adapter is Parametric Insurance Trigger events of shipments and ports information. What's next for Blockchain/Chainlink : Satellite Broadband Service Chain More to come in the next beta version before the production version. React Moralis Header component Main component Supplier component Transporter component Operator component Partner component EndUser component Broadband Solution List Mint Solution List Mint Equipment List Search Locate Equipment Search Locate EndUser Display Marine Traffic data feed Display Weather data feed <div