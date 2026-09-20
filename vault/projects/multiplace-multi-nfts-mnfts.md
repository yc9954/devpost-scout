---
slug: "multiplace-multi-nfts-mnfts"
url: "https://devpost.com/software/multiplace-multi-nfts-mnfts"
title: "Multiplace & Multi-NFTs (mNFTs)"
hackathon: "TRON Grand Hackathon 2022"
organization: "TRON DAO"
winner: true
words: 548
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/developer"
  - "substrate/video_visual"
---

# Multiplace & Multi-NFTs (mNFTs)

> A new token standard for Multi NFTs (TRC721m), A marketplace for trading and viewing mNFTs and some mNFT test collections (Wojaks By Price and WhaleFish).

[Devpost](https://devpost.com/software/multiplace-multi-nfts-mnfts) · hackathon [[TRON Grand Hackathon 2022]]

## Facets

**user** [[developer]]
**substrate** [[video_visual]]

**stack** react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for multiplace & multi-nfts (mnfts)

## Body

Inspiration TRC721 and TRC1155 and their respective Ethereum implementations only allow for NFTs that have a tokenURI function that returns a URI to 1 image. We wanted to create NFTs that have a tokenURI function that returns an arbitrary amount of images, specified when the collection is created. With this new kind of NFT that we call Multi-NFTs (mNFTs), we also realized that we needed to created a marketplace with native TRC721m support. What it does When you calls the URI function on a TRC721m contract, the function will check the current state of the world and compare it to previously set rules, and return a different image depending on the state. These rules are set by the creator of the particular collection. We have created two test collections to demonstrate some things that can be done with mNFTs, and here's a quick explainer of one of the collections: Wojaks By Price : Every NFT in this collection is connected to a decentralized price feed from WinkLink, and what price feed is something you choose when minting. For example, if the NFT is connected to the TRX/USD price feed, then every time you call the tokenURI function on it, it will check what the price change for TRX/USD was during the last 24 hours. Then depending on the price change, the function will return one of five different images. If the change is -2.5% or more then it's the saddest image, then gradually increasing and if the change is +2.5% or more then it's the happiest image. We also built a marketplace for mNFTs with the name Multiplace. It has native support for TRC721m, and it's the only marketplace at the moment where you can view mNFTs in the correct way. How we built it There were basically two major parts of the projects TRC721m and the test collections Multiplace We started working on the test collections and later started on multiplace. It became clear to us that we had to create a marketplace, since none of the current marketplace supported what we wanted. The contracts are of course written in solidity, and the frontend is written with Typescript and React. Challenges we ran into Building a marketplace is hard, and the syncing between contract/blockchain state and frontend state was really hard. After a while it clicked though, with how you need to have event listeners for most things. Accomplishments that we're proud of The marketplace itself became really pretty in our opinion, despite us not having a designer. So for a programmer, I think you can design that the UI and UX is very good. What we learned If you can develop on an EVM chain, you can also develop on the TVM. There are some small differences, but the experience carries over fine. What's next for Multiplace & Multi-NFTs (mNFTs) Keep working on the collection that you can see on the home page with the comment "coming soon". These projects are Plants Darkmode PFPs Timestamps. Multiplace currently only supports Tron Mainnet and the Nile Testnet, but we want to support the Shasta Testnet aswell. Make a Creation and Minting page, where users can come up with mNFTs collection without having to code, similar to how apenft have done it one their side for normal NFTs. <div