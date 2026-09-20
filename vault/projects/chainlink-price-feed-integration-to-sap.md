---
slug: "chainlink-price-feed-integration-to-sap"
url: "https://devpost.com/software/chainlink-price-feed-integration-to-sap"
title: "Chainlink Price feed integration to SAP"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 845
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "domain/supply_logistics"
  - "substrate/financial_record"
---

# Chainlink Price feed integration to SAP

> We consumed a Chainlink price feed to update foreign currency rates in SAP. After updating the foreign exchange +digital asset price data in SAP, we created a zk proof and a file in IPFS

[Devpost](https://devpost.com/software/chainlink-price-feed-integration-to-sap) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]] [[finance_payments]] [[legal_justice]] [[supply_logistics]]
**substrate** [[financial_record]]

**stack** abap, infura, proubc, prvd, sap, shuttle

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chainlink price feed integration to sap

## Body

Visual summary Inspiration SAP S/4 HANA is known to be the most widely implement enterprise resource planning system in the world. A commanding majority of Fortune 500 businesses and other large enterprises rely upon SAP to run their finance, supply chain, and other business operations. However - there have been very little to no open source resources for integrating Web3 to SAP and further the need to protect the privacy of enterprises while working on-chain is important. proUBC offers an open source SDK to make Web3 integration possible, including tools for zero knowledge proofs for protecting the privacy of enterprise data. This hackathon entry is one of the first standalone application leverage all of proUBC's capabilities. What it does Our submission integrates Chainlink price feeds into the SAP S/4 HANA enterprise resource planning system. In so few words - we used Chainlink price feeds to update the foreign currency rates in SAP. This hackathon entry enables SAP systems to use Chainlink price feeds to optimize their off-chain business processes with fiat currencies while also obtaining price feed information on digital assets such as Bitcoin, Ethereum and the many others supported by Chainlink price feeds. This serves as a technical and financial cornerstone towards enabling large enterprises to engage with Web3 based business models. Whether it’s a Euro, an Ether, or even something else in between - enterprises using SAP universally benefit from Chainlink price feeds fairness, transparency, decentralization and overall high performance in determining price data. As SAP S/4 is not a blockchain system - but rather a enterprise software typically deployed behind corporate on-premise or private cloud systems - we included some additional feedback mechanisms to bring further resilience into how Chainlink price feeds are used across multiple disparate standalone SAP instances. We also considered it important to implement an approach that could lead to SAP systems contributing their pricing data back to the Chainlink decentralized oracle network itself. Here are the two feedback mechanisms we created First - after the Chainlink price feeds are used in SAP to update its foreign currency exchange rates - the SAP ABAP Program we created for this hackathon emits a zero knowledge proof. This zero knowledge proof can be used amongst a loosely connected network of business partners to securely verify that they are all harmonized, synchronized to the same exchange rates. This zk proof - as it exists upon the PRVD Network Ethereum Layer 3 could be used for a multitude of other purposes on chain too. Second - the SAP ABAP Program generates a file that is shared to IPFS. This file on IPFS could also be shared between other business partners for data synchronization and verification. But what really excites me is that this could become a way by which the SAP ecosystem itself could contribute pricing data back to the Chainlink DON. Given the trillions of dollars and myriad of diverse B2B and B2C transactions conducted through SAP systems today - it’s an exciting prospect to have so many of those ordinary systems of commerce begin to contribute data back to Chainlink. How we built it We utilized Provide Shuttle to facilitate onboarding of Web3 credentials to SAP and to model a workflow to create zero knowledge proof later. We used the PRVD Nchain API microservice to consume the price feed smart contract on Polygon and mapped the data inputs to the standard SAP function module for updating foreign currency rates. We also configured Ethereum and Bitcoin as foreign currencies in SAP for the first time. Used Infura's IPFS API endpoint to write files to IPFS Our SAP dev environment is made possible through the Cloud Appliance Library and Azure Challenges we ran into Building an open source Web3 SDK in a new language, ABAP Differences in formatting decimal precision between SAP ABAP and Solidity Little to no prior open source resources for Web3 integration to SAP, including writing file to IPFS over HTTP Accomplishments that we're proud of Updated the foreign currency rates in SAP using data from Chainlink Price Feed Created first ever open source ABAP implementation of smart contract integration and of IPFS Achieved an enterprise-relevant use case for public blockchain mainnets for SAP What we learned Chainlink price feeds offer data for more than just digital assets, but also fiat currencies too Price feeds are gas-less as view functions in Solidity ABI files can be the same across different EVM networks There can be other uses for a zk-proofs and IPFS integrations across SAP and enterprise environments that benefit businesses. What's next for Chainlink Price feed integration to SAP Expand use Chainlink price feeds for interest rates, basis spreads / swaps, material pricing / commodity pricing, and other price data via Truflation and other Chainlink price feeds Implementing PRVD zk-proofs on a S/4 HANA’s system offchain bank reserves for audit, legal, and other reporting compliance Use Chainlink Proof of Reserve to implement off-chain business process to monitor 1:1 pegs for stablecoins Create additional examples of smart contract integration to SAP with ABAP that integrate to ERP business processes <div