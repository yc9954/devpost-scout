---
slug: "nft-bingo"
url: "https://devpost.com/software/nft-bingo"
title: "NFT Bingo"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 500
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/general_public"
  - "substrate/video_visual"
---

# NFT Bingo

> Our Dapp, NFT Bingo, helps small and big businesses, especially consumer products and services, to effortlessly create NFT collection and turn it into a promotion marketing campaign

[Devpost](https://devpost.com/software/nft-bingo) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**user** [[general_public]]
**substrate** [[video_visual]]

**stack** 3labs, alchemyapi, binance, ceramic, filecoin, google-cloud, moralis, nft-port, polygon, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nft bingo

## Body

Overview Homepage Lootbox page Collection page My Account Mint NFT Tech Stack Inspiration In 2020, approximately 586.5 billion dollars were on advertising. Large companies like Google, Apple, Salesforce spend as much as 46% of their revenues on marketing. A 2021 report from Deloitte’s annual CMO survey shows on average the marketing budget is roughly 11.7% of total company budget. The top 3 industries with the most advertising spending are consumer packaged good, consumer services, and tech companies. For consumer goods and services, collectibles promotion is a popular marketing campaign. McDonald’s happy meal toys is the best example. This’s where NFT collections can come into play and create additional values for the traditional collectible promotion campaign by replacing tangible items with digital items on blockchain. What it does Companies and Creators Our Dapp allows companies/creators to upload images for their collections. Companies create prize pool to incentivize users to participate. Users who successfully collects all pieces in their collection could claim 50% of the prize pool. Consumers Users can buy lootbox of random pieces, or earn a piece of the collection by buying company’s product or using its services, just like the way McDonald’s happy meal toys are given out. Users are able to mint a piece of the collection as NFT, or the entire collection as a NFT, and put them up for sale, creating resale market on NFT platforms like Opensea. How we built it The solution consist of 4 parts: 1) Contracts are developed using HardHat 2) UI is built on NextJS 3) Sponsor Tech Components: Chainlink VRF is used to generate random numbers for image generation for lootbox purchase Polygon: Dapp is deployed to Polygon Testnet for speedy TNX IPFS: Images are stored on IPFS using web3.storage Alchemy: Used for blockchain node connection Moralis: Used to fetch NFTs from users’ wallet and show them on My Account/My Public Collage Google Cloud: Comments on Collection page is stored on Google Firebase NFT Port: API is used for NFT minting Binance: Dapp is deployed on Binance Smart Chain Ceramic Network: Used for storing user profile data 3Labs: 3D.connect is used to obtain DID(Digital ID) from MetaMask Challenges we ran into The most challenging part is how to structure/architect random number generation using Chainlink VRF. Accomplishments that we're proud of We have developed everything from scratch. During the hackathon we: created the solution architecture implemented the smart contracts developed UI What we learned how to use Chainlink VRF on contracts how to use Moralis Web API how to use Ceramic Network What's next for NFT Bingo Work on the following: Allow users to send NFT as gift to their friends Incorporate user-friendly logon such Magic or Dapper for blockchain newcomers Enhance creators UI/UX and add more features/flexibility for collection page Work on the “earn” section and provide more incentives for users to try out products/services (earn by leaving feedback or friend referral, etc) Allow creators to include option for donating a portion of their lootbox revenue shares to charities <div