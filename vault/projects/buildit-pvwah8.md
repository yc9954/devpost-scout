---
slug: "buildit-pvwah8"
url: "https://devpost.com/software/buildit-pvwah8"
title: "BuildIt"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 864
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# BuildIt

> It is a metaverse project. It provides users with the ability to own virtual land within a map, place items on the land they own, and even sell the land to other users.

[Devpost](https://devpost.com/software/buildit-pvwah8) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**user** [[legal_professional]]
**substrate** [[financial_record]] [[geospatial]]

**stack** chainlink, csharp, ethereum, fantom, metamask, polygon, sepolia, solidity, thirdweb, unity

## How they structured the write-up

- smart contracts ( sepolia )
- smart contracts ( mantle testnet )
- table of contents
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for buildit

## Body

BuildIt is a metaverse project developed for the hackathon. It provides users with the ability to own virtual land within a map, place items on the land they own, and even sell the land to other users. The land is represented as ERC721 tokens, while the items are represented as ERC1155 tokens. All interactions within the metaverse are secured by smart contracts. Smart Contracts ( Sepolia ) Map.sol : 0x04b3B698D378EBeF564804B933D6CC803ac2aEa3 Utils.sol : 0x3717c0A441189d828fFE2bdEc97485098CB1Dda2 Faucet.sol : 0xC07DdbA94611C33882612b8031b2a6AfB65ca545 Marketplace.sol : 0x2e4dDe518EB8B63C47D388aa129386d9ca110a45 Smart Contracts ( Mantle Testnet ) Map.sol : 0x9f85f13F5FFb3b1dcb7B318F1712b6f42A4CFFd4 Utils.sol : 0x8e539DfdA07e5Bb63F6768eaDb800F01FC25C336 Faucet.sol : 0x69A46a7b195eb6C89454C41dE3e5Bd96C694D8FB Marketplace.sol : 0xcB82Ac8Ad0cd14DD4d6f6397B66Bf11dA538F12A Table of Contents Inspiration What It Does How We Built It Challenges We Ran Into Accomplishments That We're Proud Of What We Learned What's Next for BuildIt Inspiration The inspiration behind BuildIt comes from the desire to create an immersive metaverse experience where users can explore, own, and customize virtual land. We wanted to empower users to express their creativity and engage with a virtual world where they have control over their own unique space. What It Does BuildIt allows users to: Own virtual land within a map represented as ERC721 tokens. Place items on their owned land, such as buildings, roads, and other structures, represented as ERC1155 tokens. Sell their land to other users, transferring ownership and associated items. Connect their wallets (e.g., Metamask, Coinbase, WalletConnect) to interact with the metaverse. When a user connects their wallet, the game fetches data from the smart contracts and highlights the portion of the map that the user owns. Users can then click the "Edit" button to place or remove items on their land. They have the option to cancel or confirm the changes, which updates the items in the appropriate locations. Smart contract checks ensure that users can only interact with the land they own. In addition, BuildIt includes a marketplace where users can sell their land through direct listings or auctions. Chainlink automation can be utilized for auction listings, and if the chain supports Chainlink price feeds, the land can be sold in USD. The marketplace provides an easy and secure way for users to trade their land. How We Built It BuildIt was built using the following technologies and tools: Unity: The game was developed using Unity and built for Webgl. Smart Contracts: Four smart contracts were developed using Foundry and Hardhat: Map Contract: Responsible for the Lands in the Map, implemented as an ERC721 contract. Utils Contract: Represents the items that can be placed on the land, implemented as an ERC1155 contract. Faucet Contract: Allows users to obtain items for free initially. It is funded to provide items for judges and other participants. Marketplace Contract: Facilitates land sales through direct listings and auctions. Map Size: The map size is determined in the smart contract, allowing the deployment of multiple maps with different sizes. The current deployment consists of a map with a size of 15 by 15 tiles, where each land is a 5 by 5 tile. Item Minting: Three items are minted in the Utils contract: road, house, and special item. Wallet Integration: Users can connect their wallets, such as Metamask, Coinbase, and WalletConnect, to interact with the metaverse. Gasless Transactions: All smart contracts implement ERC2771Context, enabling users to perform gasless transactions when the relayer is funded. Challenges We Ran Into During the development of BuildIt, we encountered several challenges, including: Integrating Unity with the Ethereum blockchain and ensuring secure and efficient interactions between the game and smart contracts. Implementing ERC721 and ERC1155 token standards and handling the transfer of ownership between users and their land/items. Optimizing gas usage and transaction costs in smart contract deployments. Developing a user-friendly interface and seamless wallet integration for a smooth user experience. Accomplishments That We're Proud Of Throughout the development process, we achieved several accomplishments that we're proud of, including: Successfully integrating the Unity game engine with the Blockchain and smart contracts. Creating a metaverse where users can own virtual land and customize it with various items. Implementing a marketplace where users can buy and sell land securely through direct listings and auctions. Enabling gasless transactions for users by implementing ERC2771Context in all smart contracts. Conducting comprehensive testing, including fuzz testing, to ensure the stability and reliability of the application. What We Learned The development of BuildIt provided us with valuable learning experiences, including: Gaining in-depth knowledge of integrating smart contracts with Unity. Understanding the intricacies of token standards like ERC721 and ERC1155. Optimizing gas usage and transaction costs in smart contract deployments. Enhancing user experience through seamless wallet integration and fetching data from smart contracts. What's Next for BuildIt BuildIt is an ongoing project, and we have exciting plans for its future: Adding multiple maps with different sizes to expand the metaverse and accommodate more users. Conducting further research on gasless transactions to reduce transaction costs and improve user experience. Exploring cross-chain integrations to enable interoperability with other blockchain platforms. Enhancing the variety of items and customizations available to users. Engaging with the community to gather feedback and implement new features based on user suggestions. We are dedicated to continuously improving and expanding BuildIt to create a vibrant and immersive metaverse experience for all users. <div