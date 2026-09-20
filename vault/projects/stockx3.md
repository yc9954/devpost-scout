---
slug: "stockx3"
url: "https://devpost.com/software/stockx3"
title: "StockX3"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 442
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# StockX3

> Sell anything in Web3 World with token gating: Gaming, Animation, Audio, Comics & Graphic Novels, Design, Drawing & Painting, Films, Music & Sound Design

[Devpost](https://devpost.com/software/stockx3) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**substrate** [[code_repository]] [[video_visual]]

**stack** ethersjs, hardhat, ipfs, nft.storage, polygon, solidity, vue3

## How they structured the write-up

- what it does
- links
- inspiration
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- features
- what's next

## Body

StockX3 What it does Sell anything in Web3 World with token gating: Gaming, Animation, Audio, Comics & Graphic Novels, Design, Drawing & Painting, Films, Music & Sound Design Links Demo Video DApp Demo DApp Source Code Smart Contract Source Code Smart Contract Deployment link All Screenshot Inspiration At first, we just want to make a web3 version of stockx.com, but then the process of the verify sneakers make it complicated for the platform in Web3. Then we turn it into "User can sell any things in Web3", but the platform does not need to do the verification process. Such as user can sell their own produce products: shoes(not branding), clothes, e-books... How we built it We use an ERC1155 NFT to build the platform, and add many helper functions and features to make the create sale function/batch checkout function. [x] IPFS [x] OpenZepplin [x] ERC1155 [x] Hardhat [x] Vercel [x] TailwindCSS [x] Vue3 [x] Pinia (state store) [x] PWA [x] Vite2 Challenges we ran into How to make the UX to simple but useful is hard for us, and we spend a lot of time removing unnecessary actions and buttons to keep the system simple and easy to use. Accomplishments that we're proud of A simple and easy UX for users to buy/sell products in the Web3 world. Features contract Build base on the ERC1155 and add many helpfull functions source platform get 1% fee for all of the token mint payments creators can add their product by create a new ERC1155 token with totalSupply setup create new token source nft image (upload to IPFS via nft.storage sdk) basic price (for the token sell price) invite commission (for club owner promote marketing) dynamic properites secret content now just simply a textarea in the future it will have multiple content type such as: image/music/movie/photo etc... all data pack into json and submit to IPFS via NFT.Stroage SDK source buyer can buy any products by add to cart and batch mint token source user can batch mint token via the abi contract code invite friends to join club and get commission rewards inviter get ${inviteCommission}% of the payment user can decrypted content source What's next make user can select category while creating new product After selecting different categories, we can show different UI/UX to help user to add more useful content for the product Implement the invite commission function Implement the category filter function Marketing && Promotion for the platform Improve the UX/UI design Make a great Landing page Find 100 NFT/creator KOLs to use our platform and sell products Help top 100 users to get earned with $1M worths of Crypto Assets <div