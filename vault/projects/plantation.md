---
slug: "plantation"
url: "https://devpost.com/software/plantation"
title: "Plantation"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 316
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Plantation

> Gamefi and more

[Devpost](https://devpost.com/software/plantation) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**substrate** [[video_visual]]
  <sub>weak: geospatial</sub>

**stack** ipfs, javascript, nftport, polygon, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for plantation

## Body

Growing fruit Fruit market Dead plant Map and your plants Inspiration Virtual pets: Tamagotchi + Digital property: Decentraland + Play to earn: Axie Infinity + Virtual farming: Farmville + Yield farming What it does We built an on-chain mobile-friendly virtual yield farming game on Polygon using Chainlink VRF to provide entropy for fair distribution of game items. There is a NFT minter using NFTPort saving data on IPFS. There is an internal decentralized exchange (DEX) to trade earned items for MATIC (custom wrapped version) and dynamically price your yield. How we built it Solidity (multiple versions) for game contracts and multiple ERC721 and ERC20 token contracts. The game can be played entirely on chain through calling contract functions (e.g. on Etherscan). Big thanks to scaffold-eth for the boilerplate. Chainlink VRF is used to call back our contract with randomness which is used to set various traits of our plants so players can't know what kind of seed they get ahead of time. Contracts are currently deployed on Polygon (Mumbai). Decentralized exchange contract (Sushiswap/Uniswap) is deployed for trading the fruit tokens that you earn in the game. NFTPort is used to mint snapshot NFTs of game items on Polygon. We store the NFT's image on IPFS using NFTPort. GitHub Pages serves the frontend. Challenges we ran into Setting up a mock of Chainlink VRF. But most challenging was retaining team members throughout the hackathon as many members had to leave. Accomplishments that we're proud of The game is working on a public blockchain and hosted online and works well on mobile (via Metamask). The game is fast and fun to play. There is an in-game decentralized exchange for the fruit tokens that are yielded. What we learned Chainlink + VRF. How to deal with Polygon. What's next for Plantation Finish up some yield farming features, get more artwork, expand to more chains and integrate more assets. <div