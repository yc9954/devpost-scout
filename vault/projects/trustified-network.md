---
slug: "trustified-network"
url: "https://devpost.com/software/trustified-network"
title: "Trustified Network"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 626
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Trustified Network

> A platform to Sell Digital Services Globally and Accept Crypto Payments without paying Hefty Commissions.

[Devpost](https://devpost.com/software/trustified-network) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[finance_payments]]
**user** [[small_business]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** chainlink, ipfs, moralis, solidity, transak

## How they structured the write-up

- inspiration
- what it does
- how we built it
- trustified. network is a multichain platform which is deployed on:
- changes and upgrades in trustified network v2.0
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trustified network

## Body

GIF Sell Digital Services Globally. Accept Crypto Payments. Sell Digital Services Globally. Accept Crypto Payments. Smart contract assured Decentralised Escrow Send/Request crypto payment Fiat on ramp to get onboarded on Dapp easily. Inspiration “Trust” is a key factor for successful transactions between parties. To ensure trust, we involve third party freelancing platforms or middlemen and pay hefty commissions which highly affect the overall profit margins of parties involved in a transaction. What it does Trustified Network, a platform to Sell Digital Services Globally and Accept Crypto Payments without paying Hefty Commissions. Using inbuilt payment tools like Decentralised Escrow, Subscription Payment, Fiat On Ramp and Invoicing it becomes easy for individuals to track and manage payments while ensuring their data privacy. How we built it Trustified. Network is a Multichain platform which is deployed on: 1) Binance Smart Chain Testnet 2) Polygon - Mumbai Testnet 3) Avalanche 4) Ethereum Contracts https://github.com/Trustified-Network/TN-chainlink/blob/master/contracts.md Config https://github.com/Trustified-Network/TN-chainlink/blob/master/hardhat.config.js Chainlink We have used 1) Chainlink Price Feed Chainlink price feed used to get tokens like MATIC, ETH etc price in current USD price in Invoice. 2) Chainlink VRF Chainlink VRF is used to generate random invoice number. Implementation: https://github.com/Trustified-Network/TN-chainlink/blob/master/chainlink.md Covalent Implementation: https://github.com/Trustified-Network/TN-chainlink/blob/master/covalent.md Dashboard of Trustified is built by Covalent integration which includes: Fetch all the Escrow agreements active at a particular address (getLogEventsByContractAddress) - - Used covalent check ERC20 token balances of the address Get all the transactions done by the user address (fetching TransactionsForAddress) IPFS/Filecoin : We are Using Web3.Storage, to permanently store all the details of user invoices and subscription services.' Implementation: https://github.com/Trustified-Network/TN-chainlink/blob/master/ipfs.md Moralis : We have used Moralis for: Walletconnect with Moralis to enable users to connect with their wallet and access the dashboard Moralis cloud function: To store data of user messages, product services details, user profiles details in Moralis Database Moralis Covalent Plugin to showcase different statistics data in our Dashboard. Implementation: https://github.com/Trustified-Network/TN-chainlink/blob/master/moralis.md Changes and upgrades in Trustified Network V2.0 Escrow agreement Flow Multichain Integration Fiat on Ramp integration Push notifications for Smart contract triggered events. Usecase of core Escrow agreement platform to Help people list digital services, create pages for product/services and accept crypto payment. Crypto payment link module to claim unique url and use it to send/receive crypto payments. Challenges we ran into When we started building, we had so many ideas for features and functionalities to implement in Trustified.Netowork. We had too many ideas like we can build a freelancing platform, we can build a review system for businesses, and so on. As per our past experience of launching products we knew that building feature-rich products or trying to cover too many use cases at once is the biggest mistake most the startup does. Many of the workshops during the hackathon were very very helpful to understand and helped us take product development in the right direction from experts of Web3 who have built and scaled products successfully. Accomplishments that we're proud of Loved the MVP we built and upgraded our project during this hackathon. This Hackathon gave us a very good opportunity to showcase the work we did among an active community of the Web3 ecosystem. What we learned Learned too many things from many of the workshops and we used those learnings to build the MVP of Trustified Network. What's next for Trustified Network We would love to make Trustified Network as composable as possible so that other platforms can use our libraries, widgets, and plugins to integrate Escrow and Payments into their platform. -Next step is to spread the word and test the initial version among potential users. According to the feedback we will keep iterating and building, the product to take it to the next level after Hackathon. Screenshots Homepage Escrow Agreement Login Create Agreement Crypto Payment EPNS Notifications Invoice <div