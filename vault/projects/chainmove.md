---
slug: "chainmove"
url: "https://devpost.com/software/chainmove"
title: "ChainMove"
hackathon: "Building Privacy in Web3 - Powered by Partisia's MPC"
organization: "Partisia Blockchain Foundation"
winner: true
words: 411
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# ChainMove

> The goal was the creation of a Supply-Chain Management Solution that extends an existing logistics operation and makes it secure, transparent, and more efficient.

[Devpost](https://devpost.com/software/chainmove) · hackathon [[Building Privacy in Web3 - Powered by Partisia-s MPC]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]] [[supply_logistics]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]]

**stack** blockchain, react, rust, typescript, zk-rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next

## Body

Inspiration The goal was the creation of a Supply-Chain Management Solution that extends an existing logistics operation and makes it secure, transparent, and more efficient. With the use of Smart Contracts we can automate certain logistics steps, add oversight to the whole process and create a Data Sharing platform for transportation optimization and report generation. What it does The main role that this application is trying to fill is the extension of an existing logistics process: an online store makes a request for the transportation of an item from a manufacturer to a client and this process has to meet certain requirements dispatchers can bid on such requests a driver can deliver a product. The delivery process is broken down into multiple actions. An action is completed if it meets certain requirements: a photo was taken, the package weight meets certain minimum value, etc. How we built it It consists of three parts: a dashboard with 3 different user roles: manufacturer, driver and dispatcher a host service to cache contract states and other off-chain activity a set of public and zero-knowledge contracts: delivery contract, bidding contract, statistics contract and route information sharing contract Challenges we ran into Interfacing with a contract was a new concept and with little documentation it took some time to make it work. The plan was to interact from the back-end service and manage contracts and deploy contracts dynamically, however this feature's implementation didn't take place. Accomplishments that we're proud of We managed to build a good base for supply chain management solution with the following features: a dashboard interface to manage deliveries, contracts and reports, with 3 different user roles: manufacturer, driver and dispatcher authentication, both on-chain and off-chain pipeline to read chain data, store it in Redux state and interact with Smart Contracts and ZK-contracts demo scenarios for driver and manufacturer roles with deployed contracts zero-knowledge manufacturer statistics a delivery contract, and a zero-knowledge second-layer contract a data sharing platform for route optimization. What we learned Gained understanding of Multiparty Computation and Zero-knowledge Smart Contracts. What's next Refactoring and cleanup of the codebase The ability to create and deploy contracts dynamically Extend the delivery contracts with a second-layer solution,for verification-token claims by clients and status checking of the delivery with such keys. Additionally each action verification step should happen in a similar ZK-contract. The ability for a manufacturer to generate reports. A report can have custom data inputs and every other manufacturer can contribute. <div