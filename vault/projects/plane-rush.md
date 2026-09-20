---
slug: "plane-rush"
url: "https://devpost.com/software/plane-rush"
title: "Plane Rush"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 580
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Plane Rush

> Plane Rush is a game based on NFTs that runs on the Polygon network in the Ethereum blockchain and is powered by decentralized Chainlink Oracles.

[Devpost](https://devpost.com/software/plane-rush) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**substrate** [[video_visual]] [[web_dom]]

**stack** alchemyapi, chainlink, ethereum, filecoin, ganache, ipfs, metamask, nft, nft.storage, openzeppelin, phaser.js, polygon, polygonscan, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for plane rush

## Body

Landing page Game NFT Marketplace Home page for showing the NFTs connected to the wallet, navigation to the game and the NFT Marketplace Inspiration All our team members are big game enthusiasts. There are a lot of games even in the NFT space but a lot of those games are too heavy on the machine. So, we decided to come up with a game idea that is seemingly simple, fun and at the same time, offers great rewards to its users. Hence, we used this Hackathon as a space to explore and build our idea together as a team. What it does The game involves a pilot driving a plane moves through the accelerating obstacles coming towards him. The NFT here is the Pilot and the Plane combined. The Pilot can move in any direction(up, left, right, or down) to pass through these obstacles and gets 10 points whenever he successfully moves through each one of them. The game ends whenever the Pilot hits an obstacle. Every Plane has an Airspeed that represents how fast it can move through those obstacles. The NFTs that have higher Airspeeds will be able to perform better with respect to the obstacles as they keep accelerating forever. This is the incentive model for the users to buy the Plans with a better Airspeed. Users will be rewarded with new Randomized characters which have a speed corresponding to the score achieved in the game with a certain amount of randomization to it whenever the user achieves a new checkpoint. The NFTs are generated in the backend and the images of these NFTs are completely Random. How we built it This uses React.js for the frontend website and web3.js for interacting with the blockchain network. Chainlink is used to bring in the NFT's metadata on-chain through its API calls. The NFT (character) metadata and images are stored in nft.storage (IPFS) The game is built using Phaser.js. The smart contract is deployed to the Polygon Mumbai testnet. Challenges we ran into We as a team were not very experienced in game development, and it took us a lot of time to figure out many basic things in Phaser.js. Furthermore, randomizing the image/character for the NFT was a hurdle. We overcame it by building a custom API. We used image blending of different components to create a random plane. Getting the IPFS hash into the smart contract using chainlink was a toiling assignment. We overcame it by creating 2 different endpoints in the Custom API which split up the IPFS Hash into 2 parts. From the smart contract, we made 2 API calls to fetch the IPFS Hash as only 32 bytes of data can be retrieved using Chainlink Oracles for a single GET request whereas the IPFS base32 hash had 59 characters. Rate limiting of public IPFS gateways also caused us a lot of confusion. Accomplishments that we're proud of We are very proud to be able to build a complete and presentable decentralized game and marketplace of our own. What we learned We learned a lot about Chainlink We explored IPFS We also got to know about the intricacies of game development We learned about react optimizations to limit the re-loading of heavy resources What's next for Plane Rush Improving the marketplace to allow for better searching/sorting of NFTs. Reducing various IPFS rate limiting issues. Adding various new fun elements to the game. Improving character minting logic. Better UI/UX Deployment to the main net (hopefully) <div