---
slug: "ringle"
url: "https://devpost.com/software/ringle"
title: "Ringle"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 663
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# Ringle

> Platform to expand the NFT ecosystem (NFT AMM, VRF Game)

[Devpost](https://devpost.com/software/ringle) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** avalanche, chainlink, javascript, metamask, metis, nextjs, polygon, scroll, solidity, typescript, zksync

## How they structured the write-up

- inspiration 💡
- what it does ✨
- how we built it 🛠️
- 📕 challenges we ran into
- accomplishments that we're proud of 🎡
- what we learned ⚙️
- what's next for ringle 🤔

## Body

Dashboard Buy NFT Sell NFT VRF Game NFT AMM Liquidity Ringle: NFT Automated Market Maker (AMM) Trading Platform Inspiration 💡 The rapid evolution of decentralized finance (DeFi) has brought significant attention to the potential of NFTs (Non-Fungible Tokens). However, the NFT market faces challenges such as liquidity, price discovery, and providing a seamless trading experience. Inspired by the principles of Automated Market Makers (AMM) and the need to integrate robust financial tools, we set out to create Ringle, a platform that addresses these challenges and enhances the trading experience for NFTs. What it Does ✨ Ringle creates liquidity pools for asset pairs (NFTs and other base tokens), utilizing the AMM (Automated Market Maker) model and the Constant Product formula (xy = k) . This ensures high liquidity for NFT trading. Providing Liquidity to Asset Pairs: In an NFT AMM, providing liquidity to asset pairs makes the trading experience smoother and more reliable. Liquidity providers earn a share of the transaction fees, encouraging more users to provide liquidity. This increased liquidity helps stabilize prices. Buying and Selling NFTs: Users can sell NFTs through ERC-721 tokens and buy fractionalized tokens of NFTs through ERC-20 tokens. Guessing Game with Chainlink VRF: New traders can engage in a simple game, ‘Guess and Claim Free NFT.’ Leveraging Chainlink VRF, the game generates a fully random and fair number, giving users a chance to win free NFTs. Chainlink automation enhances our platform's functionality by distributing free NFTs, improving the customer experience. If you are a new trader at Ringle, why not try and test your luck? Guess the correct number and get a chance to win FREE NFTs. 😉 How We Built It 🛠️ Backend (Smart Contracts): For writing & deploying Solidity code, we used the Foundry toolkit (i.e. forge) and Remix. Frontend: We used SDKs like Ethers.js and NextJS to create the UI designs. Chainlink Integration - Chainlink Automation, Chainlink VRF Blockchain networks for Deployment - Sepolia Testnet, Polygon Cardona (zkEVM) Testnet, Scroll 📕 Challenges We Ran Into Backend Challenges: Our project relies on numerous libraries, leading to oversized contracts that caused a lot of deployment issues. We tackled this by modularizing the project into 4 contracts, which turned into a new challenge of connecting them together. Frontend Challenges: Integrating the smart contracts with the frontend was a complex task, but it provided an opportunity to explore and learn new libraries (SDKs) that streamlined the development process. Initially, understanding and implementing Chainlink VRF Service was difficult, by thorough documentation review and careful adjustments, this effort paid off by enhancing our platform's functionality and reliability. Accomplishments That We're Proud Of 🎡 Successful Deployment: Fully deployed Ringle on multiple blockchain networks, ensuring broad accessibility. Innovative Features: Developed unique features like NFT wrapping and fractionalization, enhancing liquidity and tradability of high-value NFTs. Seamless User Experience: Achieved a user-friendly interface that simplifies complex DeFi and NFT interactions. Security Integration: Implemented robust security measures, leveraging Defender for automation and security in DeFi operations. What We Learned ⚙️ How to write large smart contracts with best practices and how to deploy them on various different blockchain networks. 2 Creating a user-friendly interface significantly enhances user adoption and satisfaction. Interoperability between blockchains is essential for expanding the user base and liquidity. How to develop and utilize the services of Chainlink VRF and Chainlink Automation What's Next for Ringle 🤔 Expanded Cross-Chain Functionality: Further enhance cross-chain trading capabilities to include more blockchain networks through Chainlink CCIP. Chainlink Price Feeds: Currently we are using AMM to decide the prices of our NFTs, in future we would like to integrate Chainlink data feeds and then comparing the prices for providing the best possible price to our NFTs. This can highly increase reliability of our platform. NFT Staking : Developing NFT staking mechanisms to attract more users. Community Involvement: Increase community engagement and participation through governance tokens and decentralized decision-making. Advanced Analytics: Integrate advanced analytics tools to provide users with deeper insights into NFT market trends and performance. <div