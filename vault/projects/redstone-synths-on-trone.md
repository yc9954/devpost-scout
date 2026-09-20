---
slug: "redstone-synths-on-trone"
url: "https://devpost.com/software/redstone-synths-on-trone"
title: "TRON Unlimited Oracle"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 632
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# TRON Unlimited Oracle

> Integration of RedStone Unlimited Oracles with the TRON blockchain

[Devpost](https://devpost.com/software/redstone-synths-on-trone) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]]
**user** [[developer]]
  <sub>weak: general_public</sub>
**substrate** [[financial_record]] [[web_dom]]

**stack** assembly, javascript, react, solidity, tron, tronbox, tronlink, typescript

## How they structured the write-up

- inspiration
- what it does
- how it works
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tron unlimited oracle

## Body

Connecting TronLink wallet Oracle Consumer contract on TRON explorer Fetched oracle data from TRON Inspiration Builders on Tron have been restricted by the lack of diversified and custom data feeds for years. But now Tron Unlimited Oracle comes with a unique value proposition: 🚀 Frequently updated data feeds covering all the data you need for your Tron dApp 🚀 We keep data off-chain and optimize the way it's extracted by dApps. That's how we leveraged the RedStone innovative infrastructure to create Tron Unlimited Oracle offering versatile data feeds - asset prices, NFTs, stocks, commodities, weather, sports, on-chain reputation, and much, much more 🎯 What it does Tron Unlimited Oracle delivers price feeds for over 1,000 assets including tokens, Fiat currencies, NFTs floor, Commodities, and Stocks - all updated every 10 seconds ⏱ We pull data for tokens from 46 sources (including Huobi, Poloniex) for the above feeds. What's truly special is that any Web3 builder can create a custom Oracle on Tron using a Web Wizard , all you need is an URL + JSON Path and you are good to go! How it works RedStone oracles use an alternative design of providing oracle data to smart contracts. Instead of constantly persisting data on TVM storage (by data providers), the information is brought on-chain only when needed (by end users). Until that moment data remains in the decentralised cache layer, which is powered by RedStone light cache gateways and Streamr data broadcasting protocol. Data is transferred to the TVM (TRON Virtual Machine) by end users, who should attach signed data packages to their transactions. The information integrity is verified on-chain through signature and timestamp checking. To learn more about RedStone oracles design go to the RedStone website How we built it We've adjusted RedStone core smart contracts, which are used for data extraction and verification so that they can work properly with the TRON blockchain We've also prepared a new way of transferring RedStone oracle payload to the verifier smart contract We've created tests to check if everything works as expected We've prepared a dApp, which interacts with the contracts deployed on TRON and fetches oracle data from it Challenges we ran into We had few blockers while deploying Solidity smart contracts on the TRON chain, but we managed to solve it. We also needed to implement an alternative approach for attaching signed oracle data to users transactions, as our previous solution was based on ethers.js, which is not fully supported with the TRON blockchain. We've also put much effort into verifying if everything works stable & scalable in the TRON ecosystem. Integration went harder than we thought, but we managed to finish with a reliable solution for Web3 builders on TRON 🛠 Accomplishments that we're proud of End-to-end integration RedStone oracles with the TRON chain Deploying RedStone contracts on the TRON blockchain Successful creation of a TRON-based dApp Secure implementation of data extraction and ECDSA signature verification using EVM assembly Learned how to integrate a TRON dApp with the TronLink wallet In general - making the project production ready so that in can be used by TRON Builders! What we learned We learned how to integrate with TRON blockchain using TronLink wallet, and TronBox framework. We've learned how to correctly prepare Solidity contracts for deployment on TRON and how to interact with them. What's next for TRON Unlimited Oracle We are very keen on hearing feedback from hackathon organisers and the Tron builders community about Unlimited Oracle. If we manage to win a prize, we definitely would have some points on our roadmap, including: Integration of new DEX data feeds, exploring other types of data that the Tron community would like to use for building Web3 products, as well as tightening cooperation with the Tron team & ecosystem developers 🤝 <div