---
slug: "osa"
url: "https://devpost.com/software/osa"
title: "Indigo - Refined Web 3 Data Marketplace"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 650
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "user/developer"
  - "user/general_public"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Indigo - Refined Web 3 Data Marketplace

> Ecosystem where developers/data scientists can own and monetize (via NFT) their data models. Consumers can access refined Web 3 data.

[Devpost](https://devpost.com/software/osa) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[supply_logistics]]
**user** [[developer]] [[general_public]] [[researcher]]
**substrate** [[financial_record]] [[structured_db]]

**stack** amazon-redshift, apigateway, docker, dynamodb, ethers.js, hardhat, mui, python, react, remix, serverless, solidity, sql, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for indigo

## Body

Inspiration Our team member and data scientist, Andrew, wanted to solve his own problem. How could he become more of an independent data scientist? How can real revenue opportunities and upside be created for independent data scientists and developers? The answer is Web 3 which is the future of the creator economy. Data scientists and developers are creators too. The benefits extend beyond just the data model creators; it will accelerate the growth of Web 3 by providing better data for builders and users. What it does Indigo is a marketplace for refined Web 3 data. There are two primary users; data scientists/developers and consumers. Data scientists/developers (Devs) are skilled data modeling specialists. Indigo provides the tools for Devs to create, own (NFT Minting), and sell access to their data models, thus filling the supply side of the marketplace. Consumers provide the demand side and are anyone (dApp developers, analysts, Defi platforms, etc.) that needs refined data sets. Indigo provides a marketplace to locate and pay for access to refined data sets which update as new data flows into the DB Nodes. Features: Hosted Data Nodes: Indigo ingests, organizes, and provides access via data nodes hosted by the Indigo community, thus removing barriers for Devs to access the data, write queries and build data models. NFT Minting: Devs can own, control, and monetize their work by minting an NFT of their code (Devs manage and own code, DB Nodes manage and list their outputs/the data). Marketplace Web dApp: Consumers use the dApp to locate and pay for access to data sets using the native $INDG token. $INDG Token Airdrop: $INDG is the native token of the Indigo ecosystem. The Airdrop provides a small amount of free $INDG to test and experience Indigo. How we built it Frontend React & Ethers library Separate marketing site + dApp site (follows other popular Web 3 UX such as SushiSwap) Smart Contract Written in Solidity & deployed on Aurora ERC721 for minting data model NFTs ERC20 for $INDG token Contracts for staking and registering on the network are included in the database nodes Backend Automated marketplace listing creation via DB Nodes tracking of Indigo Smart Contracts on Aurora Script to automatically add community hosted DB Nodes Utilizes industry-standard data warehousing tools Challenges we ran into Everyone on our team is new to blockchain development Smart Contract development - overcame bugs and gas usage optimization (this prototype uses more gas than wanted) Airdrop - distribution of free $INDG to empty wallets because the recipient needs gas for the transaction Frontend wallet connection - challenging to implement a smooth UX wallet connection experience due to the need to handle Web 3 network switching between tabs Video production - we lacked video production experience Composing the frontend for ease of maintainability took a lot of trial and error Accomplishments that we're proud of Overcame multiple issues/bugs and learning curves to go from idea to a working prototype in less than 4 weeks with a team of 3. Deployed first user-facing smart contract application. Created our first marketplace application from scratch with supply-side, customer side, and native payments. Built an attractive front end that we are happy to show to our friends and network. Worked super well together as a team with everyone taking initiative and contributing a unique skillset. What we learned How NEAR, Aurora, and blockchain development works (especially the available tooling) NEAR ecosystem and dApps would benefit from an influx of quality data models on customers and applications Learned how to use ethers.js, build remote SQL code on live data warehouse, implement ERC20 and ERC721 contracts What's next for Indigo Test and refine Expand dimensional data models for the NEAR ecosystem Add dashboard tools to improve UX Build out product roadmap Build a community of data specialists to expand the creation of data models Explore funding options for maintaining & expanding the current team <div