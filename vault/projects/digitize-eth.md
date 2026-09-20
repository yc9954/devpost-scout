---
slug: "digitize-eth"
url: "https://devpost.com/software/digitize-eth"
title: "Bl0ckify"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 584
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Bl0ckify

> Transforming Tangible Treasures into Digital Assets with NFT Magic

[Devpost](https://devpost.com/software/digitize-eth) · hackathon [[Hack the North 2023]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]

**stack** cockroachdb, eas, ethereum, ethers, evm, l2, mumbai, nextjs, polygon, react, thirdweb, typescript

## How they structured the write-up

- inspiration 💡
- what it does 🤖
- how we built it 👷🏻‍♂️
- challenges we ran into 🏃🏻‍♂️🏃🏻‍♂️💨💨
- accomplishments that we're proud of 🌄
- what we learned 👨🏻‍🎓
- what's next for digitize.eth 👀👀👀

## Body

GIF Overview Your Collection Marketplace Inspiration 💡 Buying, selling, and trading physical collectibles can be a rather tedious task, and this has become even more apparent with the recent surge of NFTs (Non-Fungible Tokens). The global market for physical collectibles was estimated to be worth $372 billion in 2020. People have an innate inclination to collect, driving the acquisition of items such as art, games, sports memorabilia, toys, and more. However, considering the world's rapid shift towards the digital realm, there arises a question about the sustainability of this market in its current form. At its current pace, it seems inevitable that people may lose interest in physical collectibles, gravitating towards digital alternatives due to the speed and convenience of digital transactions. Nevertheless, we are here with a mission to rekindle the passion for physical collectibles. What it does 🤖 Our platform empowers users to transform their physical collectibles into digital assets. This not only preserves the value of their physical items but also facilitates easy buying, selling, and trading. We have the capability to digitize various collectibles with verifiable authenticity, including graded sports/trading cards, sneakers, and more. How we built it 👷🏻‍♂️ To construct our platform, we utilized NEXT.js for both frontend and backend development. Additionally, we harnessed the power of the thirdweb SDK for deploying, minting, and trading NFTs. Our NFTs are deployed on the Ethereum L2 Mumbai testnet. MUMBAI_DIGITIZE_ETH_ADDRESS = 0x6A80AD071932ba92fe43968DD3CaCBa989C3253f MUMBAI_MARKETPLACE_ADDRESS = [0xedd39cAD84b3Be541f630CD1F5595d67bC243E78](https://thirdweb.com/mumbai/0xedd39cAD84b3Be541f630CD1F5595d67bC243E78) Furthermore, we incorporated the Ethereum Attestation Service to verify asset ownership and perform KYC (Know Your Customer) checks on users. SEPOLIA_KYC_SCHEMA = 0x95f11b78d560f88d50fcc41090791bb7a7505b6b12bbecf419bfa549b0934f6d SEPOLIA_KYC_TX_ID = 0x18d53b53e90d7cb9b37b2f8ae0d757d1b298baae3b5767008e2985a5894d6d2c SEPOLIA_MINT_NFT_SCHEMA = 0x480a518609c381a44ca0c616157464a7d066fed748e1b9f55d54b6d51bcb53d2 SEPOLIA_MINT_NFT_TX_ID = 0x0358a9a9cae12ffe10513e8d06c174b1d43c5e10c3270035476d10afd9738334 We also made use of CockroachDB and Prisma to manage our database. Finally, to view all NFTs in 3D 😎, we built a separate platform that's soon-to-be integrated into our app. We scrape the internet to generate all card details and metadata and render it as a .glb file that can be seen in 3D! Challenges we ran into 🏃🏻‍♂️🏃🏻‍♂️💨💨 Our journey in the blockchain space was met with several challenges, as we were relatively new to this domain. Integrating various SDKs proved to be a formidable task. Initially, we deployed our NFTs on Sepolia, but encountered difficulties in fetching data. We suspect that thirdweb does not fully support Sepolia. Ultimately, we made a successful transition to the Mumbai network. We also faced issues with the PSA card website, as it went offline temporarily, preventing us from scraping data to populate our applications. Accomplishments that we're proud of 🌄 As a team consisting of individuals new to blockchain technology, and even first-time deployers of smart contracts and NFT minting, we take pride in successfully integrating web3 SDKs into our application. Moreover, users can view their prized possessions in 3-D! Overall, we're proud that we managed to deliver a functional minimum viable product within a short time frame. 🎇🎇 What we learned 👨🏻‍🎓 Through this experience, we learned the value of teamwork and the importance of addressing challenges head-on. In moments of uncertainty, we found effective solutions through open discussions. Overall, we have gained confidence in our ability to deliver exceptional products as a team.Lastly, we learned to have fun and build things that matter to us. What's next for digitize.eth 👀👀👀 Our future plans include further enhancements such as: Populating our platform with a range of supported NFTs for physical assets. Take a leap of faith and deploy on Mainnet Deploy our NFTs on other chains, eg Solana. Live-demo: https://bl0ckify.tech Github: https://github.com/idrak888/digitize-eth/tree/main + https://github.com/zakariya23/hackathon <div