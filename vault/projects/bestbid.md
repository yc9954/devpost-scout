---
slug: "bestbid"
url: "https://devpost.com/software/bestbid"
title: "BestBid"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 502
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/structural_withholding"
  - "domain/civic_government"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# BestBid

> The world's first sealed bid nft platform with the power of zero-knowledge proofs.

[Devpost](https://devpost.com/software/bestbid) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[cross_origin_web]] [[structural_withholding]]
**domain** [[civic_government]]
**user** [[general_public]]
**substrate** [[financial_record]] [[web_dom]]

**stack** ethers.js, ipfs, javascript, react.js, sequence, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bestbid

## Body

Inspiration The main reason for the creation of this project was to create a secured auction system verified with zero-knowledge proofs to increase the use cases of NFTs. One main use case we found for this project is bidding for government projects (which can be auctioned as NFTs). What it does BestBid is the World's First Sealed Bid NFT Platform. BestBid uses ZeroKnowledge Proofs to securely let users place their bids while their bids are being stored on the IPFS. BestBid has the functionality to create and list NFTs on the platform itself. Thus, creators and collectors alike can list their NFTs and sell them to the world at the best rate someone is willing to pay. BestBid strives to promote more data security when it comes to conducting auctions. Sealed bid auctions are one where the identity of the bidders and the value of their bids are not disclosed to the public which in return provides the best value to the auctioneer and the price will not be affected by public bidding. BestBid lets the auctioneer set a minimum bid and users can bid accordingly. BestBid has a featured listing also known as Live Auctions and an option to explore all other NFTs which are listed on the platform. BestBid as a platform provides its users a dark and light mode as well which is massive when it comes to UX. As for UX BestBid also makes use of animations and transitions to ensure the user falls in love with the platform. Deployed on Spheron Network : ) How we built it The front end of the project is built using React.js. The smart contracts are coded using Solidity and are deployed on the Polygon Mumbai Testnet. For interacting with the blockchain Sequence Wallet has been used which provided signing and sending transaction options. The storage of the dapp is maintained on IPFS. Challenges we ran into Web3.js compatibility issues with create-react-app v5> made us face a lot of dependency issues that had to be tackled. Circuits built using Circom were fairly new for us and we had understood everything from scratch. Accomplishments that we're proud of Creating the first NFT platform which securely lets a user bid on NFTs without having to reveal much information about oneself. Creating secure smart contracts which maintain user funds. Efficiently using IPFS for managing storage and providing user ease of access. What we learned The concept of zero knowledge. The practical use case of enabling zero knowledge in regular dapps. Circom and snarkjs library implementation. Most of our frontend earlier was built using HTML and CSS but this time we have built it using React.js and had to understand the concept of React hooks and DOM. What's next for BestBid Integration of timed auction: At the moment, the time duration for a particular auction has not yet been integrated. It has been planned for the next upgrade. Integration of user Dashboard for better access to user's bids and NFTs. Integration of more wallets. <div