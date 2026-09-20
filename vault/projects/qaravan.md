---
slug: "qaravan"
url: "https://devpost.com/software/qaravan"
title: "Qaravan"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 268
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Qaravan

> Decentralized On-Chain Marketplace (buy with delivery)

[Devpost](https://devpost.com/software/qaravan) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
  <sub>weak: web_dom</sub>

**stack** foundry, react, solidity, typescript, vite

## Body

Qaravan Index Page Qaravan Sellers Page Qaravan Seller Page Qaravan Add Delivery Page Qaravan Add Seller Page Qaravan Orders Page Qaravan.Store - Decentralized On-Chain Marketplace Three components of an ideal decentralized marketplace Sellers; Buyers; Delivery services. They should all have equal rights on the app. Any user can be a buyer or a seller. External Chainlink adapters check the order status from the delivery services via the API and change the order status inside the blockchain. Thus, buyers and sellers can not worry about the fact that one of them will be deceived. The seller will receive his money when the buyer picks up the goods from the delivery service. If the buyer does not receive his goods within 30 days, he has the right to return his money back. How it works? Adding a new delivery service Using the JobID of an external Chainlink adapter NovaPoshta developers portal ( NovaPoshta External Adapter ); UPS developers portal (soon...); DHL developers portal (soon...); FedEX developers portal (soon...); ... Using the request API via Chainlink (specify the URL and path in the JSON response) Adding a new seller In order to start selling products on the Caravan marketplace, you need to register as a seller. The products in the marketplace are compatible with the ERC1155 standard + several additional fields in the metadata. "attributes": [ { "trait_type": "Token", "value": "0x326C977E6efc84E512bB9C30f76E30c160eD06FB" }, { "trait_type": "Amount", "value": "0.1" } ] Specify the Token and Amount fields in the metadata of your products. Thanks to these two fields, you will be able to sell goods in any token and at any price. <div