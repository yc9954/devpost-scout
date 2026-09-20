---
slug: "nft-forest"
url: "https://devpost.com/software/nft-forest"
title: "NFT Forest"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 299
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/video_visual"
---

# NFT Forest

> Help consumers offset their own CO2 footprint by taking ownership of trees.

[Devpost](https://devpost.com/software/nft-forest) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[agriculture_food]] [[climate_energy]] [[developer_tools]] [[finance_payments]]
**user** [[general_public]]
**substrate** [[video_visual]]
  <sub>weak: geospatial</sub>

**stack** chainlink, ipfs, moralis, react, solidty

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nft forest

## Body

Homepage tree map Inspiration In recent year, many corporations have launched campaign to pursue carbon neutrality. The missing component is consumer engagement in their campaign. Our Dapp encourages consumers to offset their own carbon footprint by taking ownership of trees, and thus allow consumers and companies to work together to offset CO2. What it does We use NFT to represent a physical, live tree. We offer two financial incentives to purchase a tree NFT: First, it represents the timber value when it is cut down in the distant future. Older trees are cut down to make way for new trees because new trees absorb more CO2. We’ll pass the proceeds from timber harvest to the NFT owner. Second, we issue a carbon credit NFT each year for a given tree NFT How we built it 1) Contracts are developed using Remix and deployed to Polygon Testnet 2) UI is built with Rest 3) Sponsor Tech Components: Chainlink: Chainlink VRF is used to generate rebate after purchasing Polygon: Dapp is deployed to Polygon Testnet IPFS: Use Pinata to store images and Off-chain data of tree on IPFS Moralis: Use Moralis login and SDK to interact with smart contract Covalent: Obtain user wallet data Challenges we ran into Challenging part is how to structure/architect the Tree and Carbon NFT contract Accomplishments that we're proud of Leveraging on blockchain to engage consumers to fight climate change What we learned The voluntary carbon market is still in the nascent stage. There's a lot more work to be done to get it to a mature state. We found Moralis SDK quite helpful and it is great for building out prototype. What's next for NFT Forest To incorporate a gift feature that allows users effortlessly send tree NFT as a gift to their friends/family. <div