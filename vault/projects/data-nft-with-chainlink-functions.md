---
slug: "data-nft-with-chainlink-functions"
url: "https://devpost.com/software/data-nft-with-chainlink-functions"
title: "Data NFT with Chainlink Functions"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 395
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# Data NFT with Chainlink Functions

> Data NFT with Chainlink Functions

[Devpost](https://devpost.com/software/data-nft-with-chainlink-functions) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**substrate** [[structured_db]]

**stack** chainlink, ipfs, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for data nft with chainlink functions

## Body

Data NFT for Dataset Licensing What is a Data NFT? Design Details Solution Overview Inspiration We were inspired by the growing need to securely manage data ownership and access in the era of big data and machine learning, while ensuring the rightful owners are rewarded. By leveraging blockchain technology, Data NFTs address the challenges associated with data ownership and licensing. What it does DataNFT for Dataset Licensing is a platform that allows dataset owners to tokenize their data and grant access to users via NFTs. Owners of DataNFTs can issue licenses, which allows them to define the scope, duration, and conditions of data usage, ensuring that their intellectual property rights are protected. Data NFTs provide a mechanism to create licensing agreements and enable data owners to generate revenue through licensing fees. How we built it The smart contracts are written in Solidity using Chainlink Functions for data validation and metadata generation on IPFS. The contracts follow the ERC-721 standard, using Openzeppelin's contract library. The smart contract is deployed on the Ethereum Sepolia Testnet: 0x70bc8584313e2a854a321e68f6854ec767d69131 Challenges we ran into Seeing that Chainlink Functions is currently still in BETA, things get changed frequently and as a result our team also has to refactor our code. Another challenge we faced is since the contracts implement Chainlink Functions, only addresses on their whitelist can use this feature. The javascript code we send to the DON also has some limitations, such as prohibiting the use of external javascript modules. Accomplishments that we're proud of We successfully developed a platform that allows for secure data licensing using NFTs. Our solution is not only decentralized and transparent but also ensures dataset owners are properly rewarded for their work. What we learned We learned about the intricacies of data licensing, NFTs, and the potential applications of blockchain technology in the data ecosystem. We also gained valuable experience in developing smart contracts and integrating with decentralized storage solutions. What's next for Data NFT with Chainlink Functions We plan to expand the platform's functionality by integrating more data sources and types, developing advanced licensing models, and exploring partnerships with data marketplaces to increase adoption and reach. Also development datatokens, so data owners can monetize their licenses. Eventually, we would like to support multiple chains and mainnet deployments. Since Chainlink Functions is still in BETA, we will follow the progress closely to make this happen. <div