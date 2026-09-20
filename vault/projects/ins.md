---
slug: "ins"
url: "https://devpost.com/software/ins"
title: "AIRNFT"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 674
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# AIRNFT

> AIRNFT is an interactive nft service that aids the creator in bringing interactive nfts to the market: be it games, 3d models, interactive animations etc.

[Devpost](https://devpost.com/software/ins) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[geospatial]] [[video_visual]]

**stack** ethers, filecoin, hardhat, ipfs, moralis, nextjs, react, solidity, tailwindcss, web3.storage, web3uikit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for airnft

## Body

AIRNFT logo Pacman NFT Flappy Bird NFT Home Page Explore Page Create Page Profile Page Inspiration We wanted to let users experience NFTs which were more than just PFPs. AIRNFTs started as an idea of having a browser game itself as an NFT and slowly evolved into a need for a platform that allowed users to create their customizable game collections/interactive media, from which new games/digital media would be minted. Chainlink VRF proved to be instrumental in our project since it allowed us to introduce a randomized aspect to the NFTs that would be generated from each collection. What it does An AIR NFT is an augmented interactive reality NFT where users get to interact with it and the experience is uniquely defined on-chain. The interaction is created by modifying layers of NFTs where the metadata is configured on-chain. Using our platform SDKs creators can easily launch AIRNFT collections in seconds. We’ve kept if very simple for creators to launch AIR NFTs. This is how you proceed to launch one: Firstly the user chooses between experiences, for example, the collection would be an Art or Gaming experience. We are are also going to add AR/VR experiences in future Then the user continues to configure the UI Design and the Game Mechanics with further deploying the game assets to IPFS for a truly decentralized solution. They can also customize the metadata according to the collection needs. Once you deploy the collection, your NFT mint is Live for users to buy the tokens. How we built it The smart contract makes use of Chainlink VRF and inserts random values into the game file variables. This helps generate random interactive NFTs. The game itself will be a folder containing files pertaining to the game. On the frontend, we used NextJS, tailwindcss, Moralis, MoralisDB (to store contracts created for each user), web3uikit (for our connect button and NFT components) and web3.storage (for generating image and game folder ipfs cid). The game folder and image preview will be uploaded and its ipfs cid will be generated using the web3.storage library and used for creating a new instance of our collection smart contract. Once the collection smart contract is created, its NFTs can be minted by simply specifying collection contract address and metadata values that would be unique to the NFTs. For more info on our project or smart contract, please refer to our github or verifed smart contract on polygonscan . IPFS metadata of an AIRNFT: { "name":"Augmented Interactive Reality Experiences", "description":"Interactive. Randomized. Customizable", "image":"ipfs://bafkreic5ch6hvbdbefka74vurdlibwy6vjrdncr7efxdhwharswxp4yjti", "animation_url":"ipfs://bafybeigcykqlrl3r33gd5xu6yei3zxeqsdhqtonu4whjvolh5wg4jzwfgu/?uniqueParam=2520785061168210647646832395485437475681982032876320291291606201981714983730?tokenId=1", "attributes":[ { "trait_type":"color", "value":"orange" } ] } Challenges we ran into Integrating the chainlink VRF generated random number into our game and using that to generate the randomized NFT was definitely a challenge. We had some trouble generating the preview image and game folder ipfs cid and using that for our smart contract interaction. web3.storage allowed us to easily do just that with just their API key and javascript library. Storage for NFTs is crucial for interactive-media based NFTs, especially games. Accomplishments that we're proud of Successfully consume random number by Chainlink VRF into game files, enabling their randomization. Successfully able to create a new collection contract from the frontend with user-defined arguments. Successfully able to mint NFT from an existing collection, also with user-specified unique metadata. What we learned What seemed like a stretch for a hackathon idea is no longer so. Our team had to tackle new challenges in the course of the project development. Chainlink Spring 2022 Hackathon helped us gain invaluable skills over the course of a month and pushed us to ship something that we would be proud of. What's next for AIRNFT We are excited to add more features into AIRNFT and build it out to a fully functional platform dedicated towards launching interactive NFT collections. A road map for AIRNFTs: SDKs for launching NFT Experiences in Web & Mobile with JS libraries like ReactJS, ThreeJS etc. 2022 Q3 Alpha Launch with Marketplace 2022 Q4 Integrate AR/VR Metaverse Game using Unity3D 2023 Q1 Governance Token Launch🎉 <div