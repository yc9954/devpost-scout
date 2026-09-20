---
slug: "gum3road"
url: "https://devpost.com/software/gum3road"
title: "Gum3road"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 347
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/web_dom"
---

# Gum3road

> ERC1155 NFT platform where users can mint and sell any file!

[Devpost](https://devpost.com/software/gum3road) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

  <sub>weak: supply_logistics</sub>
**substrate** [[web_dom]]

**stack** ether.js, ipfs, next.js, sass, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gum3road

## Body

Minting Home Home Home Home Inventory Store Listing Inspiration There have been NFT marketplaces all across which are based on ERC721 but I couldn't find many projects on ERC1155 standard so I created one! What it does It provides a platform where users can mint any file as NFT and adjust the number of copies to be available and put them up for sale. Other users can buy it from the store page and download the NFT files. When a user buys a file from the store 99% of the price is sent to the minter and 1% goes to the contract deployer. This website is a web3 version of gumroad.com . How we built it I used remix to create a smart contract and implemented the ERC1155 standard along with its extension ERC1155URIStorage and util ERC1155Holder to make a contract hold nfts itself. I have used the Infura IPFS client to store nfts metadata and ether.js for interacting with the contract. To be able to give users a choice to connect to a wallet of their choice I have used the web3modal package. For the frontend, I have used next.js. Challenges we ran into While implementing the ERC1155 standard, there are few projects based on it, so it was hard to get an idea of it. I started with web3 in mid may so I was learning while doing this project. It took me 6 weeks to develop it. Accomplishments that we're proud of I learned a lot about the ERC1155 standard for NFTs and made a Dapp implementing it. What we learned Foremost I learned how to make a full-fledged web3 Dapp—learned how to save data to IPFS. While making a contract I learned about the ERC1155 standard and its extensions and utils. Also learned about overriding functions when importing multiple contracts. What's next for Gum3road Adding categories for files on publish page, filter options on store page, introducing subscription models with tokens and much more. Partnerships with NFT communities. Onboarding web2 digital courses/ebooks/other sellers to web3 by incentivizing them for their initial listings. <div