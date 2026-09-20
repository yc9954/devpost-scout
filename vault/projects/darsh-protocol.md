---
slug: "darsh-protocol"
url: "https://devpost.com/software/darsh-protocol"
title: "Darsh Protocol"
hackathon: "Fantom Hackathon Q1 2023"
organization: "Fantom Foundation"
winner: true
words: 588
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/structured_db"
---

# Darsh Protocol

> A decentralized peer-to-peer lending protocol on fantom.

[Devpost](https://devpost.com/software/darsh-protocol) · hackathon [[Fantom Hackathon Q1 2023]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** chainlink, covalent-apis, credprotocol, express.js, figjam, figma, mongodb, moralis-streams, netlify.com, openzeppelin, render.com, solidity, truffle, vuejs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for darsh protocol

## Body

Darsh Homepage Architecture Inspiration The DeFi ecosystem have flourished in the last few months and not only we've been inspired by Fantom's resiliency as one the top blockchain that offers best building blocks for DeFi, we believe DeFi can be more socialized and personalizable while maintaining it's autonomy and permissionlessness to on-board the next generation of users into the ecosystem. What it does Darsh introduces a decentralized peer to peer lending platform which offers a way enabling lenders to maximize earnings on supplied assets while allowing borrowers access to fixed-term fixed-rate loans, removing the risk exposure of their collaterals to price-based liquidations. Borrowers are required to lock a certain amount of collateral to borrow a loan, in which the Collateral ratio is determined by the Rating group the user is categorized as. Lenders and borrowers are also enabled to determine who to initiate a loan with based on their social stats and on-chain credibility. How we built it Architecture and design We ideated on the project’s architecture and userflow using Figjam on Figma after deciding on what user pain point we are determined to solve. Thereafter, proceeding to design the User interface and developing the product. Frontend Using the Vuejs framework and plugins like truffle-contract, jazzicon, time-ago and others, we were able to build the frontend application easier and faster, and Web3js library for interacting with our smart contracts. Smart contracts We used Chainlink price feed aggregatorV3 in our smart contract to get latest price of tokens, and some Openzeppelin standard contracts to build an error-safe and secured contracts. Backend For better indexing and querying of data, we used Moralis stream to sync events from our smart contracts to a mongo database via a nodejs application. Challenges we ran into Along the line we faced a few difficulties building the project which was due to scarce documentations and since it's our first time verifying smart contract code on an EVM chain like Fantom, it was a bit tricky. But Luckily, after many attempts and help from the Fantom's fantastic developer community, we were able to resolve them. Accomplishments that we're proud of Firstly, we're very proud of been able to have built a fully functioning prototype improving aspect of decentralized financing, despite the time constraint given. We are also proud of the product we built starting from the ideation stage, to a user centered and friendly interface, down to the smart contract challenges and other technical aspects we've overcome. What we learned In building Darsh in the past few weeks, we learned a lot about how intricate developing a protocol solving a user problem can be, but in doing so we believe we are now much more proficient and knowledgeable Fantom developers than we initially were at the start of the hackathon. What's next for Darsh Protocol Integrating the use of SBTs as a medium to store verified on-chain and off-chain data of a user to be used on Darsh as a reputation mechanism without the user renouncing his privacy. We plan on incorporating core services like Social graphs and Naming services, or integrate them once they are available on Fantom, helping users put their on-chain identity to use. Further decentralizing our protocol, where all decisions governing how our protocol operates are decided by a DAO, and a tokenomics that incentivize Dao members, helping the protocol thrive further. In increasing the coverage of our target audience, we plan to support other forms of collateral like Non Fungible Tokens and other forms of tokenized assets in the future. <div