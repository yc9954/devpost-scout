---
slug: "intotheverse-metaverse-land-sale-chainlink-moralis"
url: "https://devpost.com/software/intotheverse-metaverse-land-sale-chainlink-moralis"
title: "IntoTheVerse Metaverse Land Sale Chainlink-Moralis"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 867
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# IntoTheVerse Metaverse Land Sale Chainlink-Moralis

> We are building a demo for our upcoming land sale at IntoTheVerse metaverse, using Chainlink's keepers for triggering rewards based on calamities for estate owners, ChainlinkVRFs for random attributes

[Devpost](https://devpost.com/software/intotheverse-metaverse-land-sale-chainlink-moralis) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[agriculture_food]] [[civic_government]] [[finance_payments]] [[housing_homeless]]
**substrate** [[geospatial]] [[video_visual]]

**stack** blender, chainlink, chainlink-keepers, chainlinkvrf, ethers, ipfs, moralis, sketchfab, solidity, three.js, truffle, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- technologies and their use cases
- accomplishments that we're proud of
- what we learned
- what's next for intotheverse metaverse land sale chainlink-moralis

## Body

Inspiration We were inspired by Crypto Voxels, which uses three.js to create surreal metaverse experiences. So to prepare for our upcoming NFT land presale, we were determined to build something for the chainlink Spring hackathon this Spring, while making use of technologies, like VRFs, Keepers, Moralis and three.js What it does Virtual-Estate Sale for IntoTheVerse metaverse IntoTheVerse is planning a metaverse land sale, for November 2022. We spent our time learning the use cases of Chainlink's VRF and keepers to help in Land Sales for the metaverse. Scroll owners would be able to own Virtual Estate inside the metaverse in return for various incentives. We use Chainlink Keepers to keep track of external events like high yield in our virtual token farms to reward users with the ERC-20 VRS tokens depending upon yield in the farms. This incentive is only given to token owners. Each random NFT (house) minted has random attributes powered by Chainlink VRFs, which will be used to decide the rates for leasing the property, in the future. Our Smart Contracts have been deployed to Ethereum(Rinkeby), Polygon Mumbai Testent, and Binance Smart Chain Testnet. Moralis runs nodes for Ethereum, Polygon, and Binance for our metaverse. IPFS for storing token metadata and minting tokens with a unique token URI. The front end is built on Three JS and smart contract interactions are made possible through Moralis web3 and ethers APIs Smart Contracts deployed NFTEsate.sol Rinkeby: https://rinkeby.etherscan.io/address/0x0eE04B101157c22fAA35BbEBaa67193ca33B6741 Polygon: https://mumbai.polygonscan.com/address/0x8F6b17B1425c1A8a5D2014eb2FdEDcd39beFF860 BSC: https://testnet.bscscan.com/address/0x84a4E9C645778039e221365Fc17E953a46542c57 CityEconomy.sol Rinkeby: https://rinkeby.etherscan.io/address/0x853b198031D94d10136798Ab0CB265a312561bC1 Polygon: https://mumbai.polygonscan.com/address/0xfC7B6c91c903cdEb5F8F1Fc89207A7B14b521076 BSC: https://testnet.bscscan.com/address/0x0038311685adEF9A92aB2b15Ee901397448919ca NativeToken.sol Rinkeby: https://rinkeby.etherscan.io/address/0xcc8e2B231D266B42f947ff31666657B04eE6b77A Polygon: https://mumbai.polygonscan.com/address/0xA5f0C434135Bc31F35B2Ebbc511b523835e51a32 BSC: https://testnet.bscscan.com/address/0x495cd33714C17f5ea3dDf231F1b7aC45f91aa31d ScreenShots 1 NFT minted 5 NFTs minted How we built it We use Chainlink Keepers to keep track of external events like high yield in our virtual token farms to reward users with the ERC-20 VRS tokens depending upon yield in the farms. This incentive is only given to token owners. Each random NFT (house) minted has random attributes powered by Chainlink VRFs, which will be used to decide the rates for leasing the property, in the future. Our Smart Contracts have been deployed to Ethereum(Rinkeby), Polygon Mumbai Testent, and Binance Smart Chain Testnet. Moralis runs nodes for Ethereum, Polygon, and Binance for our metaverse. IPFS for storing token metadata and minting tokens with a unique token URI. The front end is built on Three JS and smart contract interactions are made possible through Moralis web3 and ethers APIs 3D models are created in Blender. Challenges we ran into Learning about making 3D models, lighting, and camera angles for the same. Learning Moralis and using their APIs to read and write smart contracts Exploring Chainlink Keepers to trigger events based on certain actions. Technologies and their use cases IPFS - The virtual land is represented as NFT which can be viewed on NFT marketplaces to show the NFTs image and property on these marketplaces we store metadata of an NFT on IPFS. The NFTs are interest-bearing NFT they have random attributes through which the share of the airdrop is calculated. Chainlink VRF - To keep airdrop fair on the NFTs the random property is derived from Chainlink VRF. In future scope the virtual land would be inside the phaser/unity game this is an MVP. With the use of VRF, we are building an algorithm that would determine the share of airdrops in a particular city with respect to chains id's such as 4 - Rinkeby, 8001 - Polygon, 97 - BSC. Chainlink Keeper - Keeper is used to trigger the smart contract functions for airdrop and random city economy. Truffle - The smart contracts are deployed using truffle and @truffle/hdwallet-provider is used to connect wallet for gas payments of smart contract deployment. Threejs - The virtual land representation is done through threejs. Metamask - The MVP is built to be operated on a web browser so we use Metamask's wallet extension to trigger smart contract changes etc. Moralis - Moralis has been the crux of the project to interact/read from the smart contract. We are also aiming to store virtual land data like coordinates, lease amount, and rent per month on the Moralis server. Web3 - To keep development hassle-free some part of the smart contract is rendered through web3.js Solidity - The entire blockchain functionalities (smart contracts) are developed through Solidity. Accomplishments that we're proud of Although we are still working on the Chainlink rewards triggering mechanisms based on the yield in farms available, we are still happy with the way we set out to develop the project in a short period of time. With the use of Chainlink Keepers and VRFs, we can now better secure our project by listening to events on-chain. What we learned We learnt to build on Moralis for the first time and integrate Chainlink Keepers and VRFs on Rinkeby, Polygon, and BSC testnets, Use of threejs library and rendering and working with 3D objects. What's next for IntoTheVerse Metaverse Land Sale Chainlink-Moralis Scrolls would be sold to genesis metaverse landowners and then they would be able to mint land inside the metaverse by burning their scroll NFT. Owners would be given periodic rewards for owning land inside the metaverse and access to various exclusive rewards and voting power, token-gated access to certain parts. <div