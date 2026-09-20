---
slug: "polypos"
url: "https://devpost.com/software/polypos"
title: "Salespage: A checkout platform built on Polygon and web3"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 585
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Salespage: A checkout platform built on Polygon and web3

> Salespage creates a Point of Sale (POS) management platform built on Polygon smart contracts to enable businesses of any size to create simple in-store purchase pages.

[Devpost](https://devpost.com/software/polypos) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]] [[transportation]]
**user** [[developer]] [[frontline_worker]] [[small_business]]
**substrate** [[financial_record]] [[video_visual]] [[web_dom]]

**stack** hardhat, polygon, react, solidity, web3

## How they structured the write-up

- salespage
- pain points:

## Body

Salespage home screen Create flow Store created Uploading a menu configuration Architecture diagram Salespage checkout screen Final Checkout screen Hosted store assets Viewing past transactions Example storefront (customer) Adding a modifier Completing payment (customer) Salespage logo Deployed contract and transactions Payment completed Uploading images for sales page Salespage A Point of Sale platform built on Polygon and web3 storage. Inspired by platforms such as Square, Clover, and Toast - Salespage creates a Point of Sale (POS) management platform built on Polygon smart contracts to enable merchants of any size to create their own in-store purchase pages. Every purchase gets emitted as a smart contract event and transactions are generated as NFTs with receipts that can be presented in-store as proof of purchase. Live demo: here Note must be connected to the Mumbai testnet for Salespage demo url above. Video: Demo video Pain points: Many of these existing providers don't integrate cryptocurrency as payment methods. Existing Providers aren't distributed and suffer downsides of existing centralized platforms (vendor lock in, variable pricing, outages, credit card fees). Existing providers often have monthly fees regardless of usage. Often transaction history entrusted to a centralized authority vs. blockchain used a decentralized permanent record-keeping system of transactions. Features Upload images and descriptions for the live page. Metadata for each page is delivered via a Ceramic stream and is hosted without fees for the end user. Show sharable product pages and images hosted on IPFS using distributed delivery and hosting. Integrated pricing and checkout using Unlock protocol (other payment integrations could also be added). Create a new wallet to support payments to help new businesses adopt and receive cryptocurrency payments. IPFS powered storage and transaction record keeping. Once the payment is complete, the user gets a receipt that they can show to the person in the store/restaurant, but an event also gets fired from the smart contract which could be subscribed to anywhere. Technologies used IPFS/Filecoin (Hosting and sharing of assets): IPFS and Filecoin are the primary drivers making Salespage possible. Using web3.storage, a storefront or product page creator can host a distributed restaurant menu. The images are pulled down every time a Point of Sale page is rendered on a device using IPFS addressing. Polygon: Smart contract 'Salespage' (see contracts folder) representing a unique store front. Each deployed restaurant/retail page gets a distinct smart contract that emits an event whenever a customer completes a purchase. Ceramic: Used for storefront metadata storage and retrieval using streams (community node: https://developers.ceramic.network/run/nodes/community-nodes/ ). When a product page is accessed, a ceramic stream with the streamId of the page cid is opened and the metadata is rendered with the products from IPFS. Ceramic is invoked when the Salespage contract is first deployed and when the data is retried on Point of sales page render. NFTPort: After payment is completed on Polygon, NFTPort generates a receipt that contains information about the items purchased, the name of the merchant, and ties it to the payer's address. Covalent: Transaction history against each Salespage. Query the events and transaction receipts generated on a contract url. Covalent enables a reporting system of merchant success (and failure) by aggregating customer purchase transactions and categorizing them by outbound (payable) or inbound (receivable). Architecture Diagram How to run Define the following env variables REACT_APP_STORAGE_KEY = {YOUR_WEB3_STORAGE_KEY} #web3.storage api key REACT_APP_COVALENT_KEY = {YOUR_COVALENT_API_KEY} # covalent api key REACT_APP_NFT_PORT_KEY = {YOUR_NFT_PORT_API_KEY} # nft port key (client side mint currently) REACT_APP_SALESPAGE_INFURA_KEY = {YOUR_INFURA_API_KEY} # for client-side RPC calls. View full information on the github here: https://github.com/cbonoz/salespage <div