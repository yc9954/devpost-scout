---
slug: "sandfuse"
url: "https://devpost.com/software/sandfuse"
title: "FUS(e)D"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 326
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/geospatial"
---

# FUS(e)D

> An overcollateralized lending protocol backed by Proof of Reserves

[Devpost](https://devpost.com/software/sandfuse) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[geospatial]]

**stack** chainlink, foundry, react, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fus(e)d

## Body

Homepage Dynamic NFT Workflow Inspiration The ongoing crypto crises, lot of which has to do with the lack of transparency in the underlying assets/protocols. What it does FUS(e)D uses Chainlinks Proof of Reserves to validate that the collateral used to borrow has reserves that are backed. Thus forming an underlying basis for creating a collateral mechanism with it. Fus(e)D is a standalone platform that does not need external actors for management. No DAO is required and everything is automatic via Chainlink Price feeds and Keepers. On the lenders side, the lender can provide liquidity for the FUSD pair and is funded by the fees paid by the borrowers. We hope to in future make the borrowing fees a portion of liquidity and amount borrowed to incentivize lenders further. How we built it We used foundry and various Chainlink API's such as Proof of Reserve, Keepers and Price feeds to build it. We created a dynamic NFT that represents the underlying position, the borrower is listed in the NFT and the NFT in future will represent the loan. Thus enabling future improvements such as auctions/refinancing etc. Challenges we ran into Keepers integration was something that we ran into some trouble because of how we wanted to check upkeep for multiple positions, so we created a mapping to help with it, but this we need to improve. Designing the dynamic NFT's were a bit tough. We have created a Keeper contract on Polygon Mainnet https://polygonscan.com/address/0xdc48e0945847e9578b2611c82001f002e55b1178 Accomplishments that we're proud of We are proud of how the system does need any external actors and can entirely self manage. Learning how to write tests and deployments in foundry. What we learned How to utilize PoR to ensure safety in protocols. How each part of web3 can be a building block to enable new protocols. What's next for FUS(e)D Improve the UI by adding subgraph Validate the smart contracts with some more robust testing Enable mass liquidations to save gas <div