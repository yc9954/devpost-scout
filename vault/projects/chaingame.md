---
slug: "chaingame"
url: "https://devpost.com/software/chaingame"
title: "ChainGame"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 1126
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# ChainGame

> A No-code approach to Generate and Buy Dynamic + Upgradable NFTs for your Web3.0 Game

[Devpost](https://devpost.com/software/chaingame) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]
**substrate** [[structured_db]] [[web_dom]]

**stack** ccip-read, chainlink, cloudflare, ens, solidity, thorin

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chaingame

## Body

Creating NFTs Buying NFTs Interval-based NFTs Level-based NFTs Inspiration Web3.0 games are rising at a very fast pace but currently it's a big headache for new developers to create a Web3.0 game as it involves complex steps such as - Designing smart contracts Designing assets needed in the game Building the Game 's Frontend Making assets available in the form of NFTs But managing NFTs can get tedious for developers in some cases. For example - creating an NFT that updates everytime user's level gets increased could require some complex logic and time. Last month, I dived deep into Chainlink and it made me realise that it's possible to create a solution to all the problems mentioned above. With ChainGame, I wanted to build a one-stop application that allows web3.0 game developers to register their contracts and mint dynamic nfts. What it does Chaingame allows game developers to generate customizable and dynamic NFTs easily on the go. I classified NFTs into three types - Static - Metadata doesn't change. Level-based - This type could come into play if your game contains Upgradable-assets. For example - A Level 2 Weapon must look stronger than a Level 1 Weapon. Interval-based - Metadata changes at a certain interval. This type could come into play if your assets change with time. For example - A tree changes its appearance through the seasons. Apart from all this, the NFT and Contract data is stored offchain, which gets accessed using CCIP-read. This allows easy and gas-efficient data storage. Registering A Contract Developers must register their contract before generating NFTs. The contract data is stored Offchain on a cloudflare worker. The contract must be Chaingame Compatible . Your ERC720 minter contract must contain atleast two functions - mint and setTokenURI . You can customize DestinationMinter.sol as per your needs but make sure to not hinder with the specified functionalities Note - DestinationMinter.sol is considered to be your contract for this example. Static NFTs Generating - Developers create JSON metadata for the NFT and pin it to IPFS. Generate a Static NFT by following the instructions given on the website. The data goes to Chaingame.sol and then OffchainLookup gets reverted. Then, the data gets stored into the cloudflare worker using the request sent by the ccip-read protocol. Then the data gets signed by the cloudflare worker and the callback is called. The signature gets verified and then tokenPrice gets stored. Buying - The data goes to Chaingame.sol and then OffchainLookup gets reverted. Then, the data gets stored into the cloudflare worker using the request sent by the ccip-read protocol. Then the data gets signed by the cloudflare worker and the callback buyTokenWithSignature is called. User pays the NFT price. sendMessage from CCIPHandler.sol is called and the message is sent to DestinationMinter.sol . CCIP request gets fulfilled within 20 minutes and the NFT gets minted. Level Based NFTs Generating process is pretty much the same as that of Static NFTs except for the multiple metadata links provided by the developer. Buying - One extra step gets added after the fourth step - Token Data is stored into CCIPHandler.sol Upgrading - DestinationMinter.sol calls upgradeToken . CCIP Request is received in CCIPHandler.sol . sendMessage is called on AutomatedFunctions.sol which sends a request to cloudflare worker using Chainlink Functions. The data gets updated offchain. Token Update request is sent to DestinationMinter.sol , using CCIP, to update the tokenURI . Interval Based NFTs Generation process is the same as that of level-based nfts. Buying - Data is stored in AutomatedFunctions.sol instead of CCIPHandler.sol Updates - AutomatedFunctions.sol manages the upkeep that triggers time-based changes. Once performUpkeep is called, the offchain data gets updated using Chainlink functions. After offchain update, sendMessage is called on CCIPHandler.sol to update the tokenURI in DestinationMinter.sol How we built it Smart Contracts I used the following technologies to build the smart contracts - Solidity - I used Solidity to develop the Smart Contracts and deployed them on the Sepolia Testnet. Chainlink Functions - Chainlink Functions allow my smart contract to connect with the cloudflare worker so that the data can be updated with each token update. Chainlink CCIP - Chainlink CCIP acts as a bridge between Chaingame contract and the game contract. It sends the message to the game's contract to mint/modify NFTs. Chainlink Automation - Chainlink Automation helps in updating Interval-based NFTs. Once, perform upkeep is triggered, it updates the NFT metadata using Chainlink Functions and CCIP. README Frontend I built the frontend using Next.js and used Thorin as a UI design library. I used CCIP Read to interact with the smart contract functions which require OffchainLookup. README Worker I use Cloudflare as a gateway to interact with data. I used Kysely as the database for this project. Cloudflare has some good support for ENS, which helped me build the worker easily. README Challenges we ran into Considering the amount of challenges I ran into, it would be safe to say that this was the most challenging project I've ever done. When I started with the project, I ran into some errors with Chainlink CCIP. And it was really frustrating as even if I changed only one line of code, it would take 20 minutes to see if it's actually working or not. It was really testing my patience. That was due to the fulfillment time taken by CCIP. But somehow I managed to fix it. Initially, I planned to store the data On-chain but as the data grew, gas prices got significantly higher, which made me rethink my approach. Then I read about CCIP Read and realised that it is what I need. So, I integrated CCIP Read using a cloudflare worker into my project to make my smart contracts gas efficient. I planned to add much more things, but it went out of the scope for this project. Accomplishments that we're proud of Making a project that leverages multiple technologies at a time in such short timespan seems to be a big achievement for me. Tackling all the challenges without giving up is what I'm proud of. What we learned I just knew some basic solidity before starting this project. But while creating this project I learnt alot about Chainlink Technologies, EIP3668 and ENS. Apart from this, I learnt about ZK-proofs, Isolation forest and OpenAI too (to add more features into it after the hackathon). What's next for ChainGame My first task would be to work on the details in the frontend while creating a good UI using Thorin. I initially planned to add features such as Recoverable NFTs(using ZKP), AI-Generated Dynamic NFTs and Checking Anomalies in the Game Contracts using Isolation Forest. But they went out of the scope for this hackathon. So, I'll make sure to add everything I planned. <div