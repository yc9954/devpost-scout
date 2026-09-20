---
slug: "chainlink-fanzone"
url: "https://devpost.com/software/chainlink-fanzone"
title: "Community FanZone"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 983
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/web_dom"
---

# Community FanZone

> Build your own community or fan-zone with unique assets: NFT, FT, raffles and events. Use DAO voting, organize sweepstakes, share news and take advantage of the web3 world with a few clicks.

[Devpost](https://devpost.com/software/chainlink-fanzone) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]] [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[web_dom]]

**stack** chainlink, hardhat, openzeppelin, react, solidity, tailwind, wagmi, worldcoin

## How they structured the write-up

- inspiration (problem that project addresses)
- what it does (how we solve the problem)
- how we built it (which technologies was used)
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for web3 fanzone

## Body

Homepage Dashboard NFT Collection Fungible token DAO Voting Raffles Members Community settings Community public page Community NFT Inspiration (problem that project addresses) Web3 provide new ways for content distribution, transparency and democracy in our lives, it is next step in digital culture and interaction between different groups of people. In other side this technology is new and complicated for new users and makes it difficult to launch your own product in web3 space. As content owner (or community moderator) you can use existing marketplaces for your NFT collections, but there is a lot of limitations for next usage, content distributions and functional abilities. For example you can't manage distribution strategies, don't have ability to limit campaign (to be used only by your community), avoid multi-accounting (for free NFTs), get additional info about community (for example email addresses), can't check community activity, get NFT holders list. How about ability to launch your own fungible token, send airdrops, create DAO voting or raffles etc. To cover this limitations you can develop your own community website with web3 integration but it require a lot of time, money and your energy :) What it does (how we solve the problem) We provide solution to cover your needs - with Web3 FanZone you can create NFT collection, manage distribution strategies, get all activity information, limit NFT campaigns, launch fungible token, DAO voting, organize sweepstakes and extend your community audience. Only you will be the owner of your content and smart-contracts! You can create multiple communities and simply switch using our web-interface. All public communities listed in our website separated by category and allow anyone to see community content, distribution campaigns and DAO voting process. For raffles we use Chainlink VRF to get random winners from your community. Code examples in repository: smart-contract , frontend . DAO voting automated by Chainlink time-based automation that execute completed voting proposals. Code examples in repository: smart-contract . Our service is free and open source and you can use it to build your own custom solution in few days instead of weeks or months! Web3 FanZone can be used by sport, gaming teams, musicians, artists, singers and any groups of people by interest to bring new possibilities into our lives. Use Cases: Sport team can create NFT Series with player cards. Fans collect this NFT to support favorite team and participate in raffles for next match tickets. Gaming team can store the best gameplay moments as NFT, send token airdrops for your NFT holders. Media channels (radio, TV or individuals) can distribute the best materials as NFT, collect users list for future media sharing and offline campaigns. Musicians and artists can join web3 world, share creativity, art, find new fans and sell their digital assets. Now only you own your work! Teachers can create events for students and allow only local event participant to claim their assets, set a date range and limit distribution with an extensive set of rules. Events: you can create NFT-tickets and distribute to your audience (directly send to wallets or use one of our distribution campaigns). This functionality will be extended by "Burn NFT" option when you accept ticket on entrance. How we built it (which technologies was used) We use Solidity to develop factory smart-contracts that deploy smart-contracts based on settings that community owner provide using our web-interface. Frontend build on react with redux and wagmi hooks for connect and communication with blockchain. We use hardhat for smart-contracts with OpenZeppelin library to make our contracts upgradable and follow ERC-1155, ERC-20 and Governance standards. We use Chainlink VRF to get random numbers in specific range to define the list of raffle winners. Also we use Chainlink Automation to simplify and automate our DAO voting process by execution completed proposals. All media files stored in IPFS using nst.storage service that simplify this process and help to save ERC-1155 metadata file with media in one call. Also usage nft.storage speedup content delivery from IPFS that fills like usage regular web2 services for end users. When you allow free NFT minting and token claims, you want to avoid multi-accounting and delivery your content for real audience. Worldcoin proof of personhood solve this issue and allow execute specific action only once per real person. To test all functionality please use Mumbai network. Challenges we ran into How to develop factory smart-contracts. How to use wagmi for frontend (replace some parts multiple times to find the best solution). How to upload ERC-1155 metadata json into IPFS. How to develop DAO voting and use OpenZeppelin Governor. How to use Chainlink time-based automation. How to use Chainlink VRF to get random numbers. How to provide most efficient distribution campaigns. How to get community activity. How to send tokens airdrop. How to work with smart-contract size limitation (24kb). How to limit content to avoid multi-accounting (used proof of personhood). Accomplishments that we're proud of Simple user interface with powerful features. Community owner also own smart-contracts and all created content. Powerful functionality for NFT series: description, attributes, royalty. Automated DAO voting (using Chainlink time-based automation). Multiple distribution strategies for NFT and FT. Allow to create unlimited NFT series. Found a way how to get unique winners based on Chainlink VRF random numbers. It was the issue because I have limited range of addresses and user need to get some amount of this addresses as raffle winners. All public communities listed by category in our website. Ability to use different wallet connectors. What we learned I learn a lot of thinks, it is even hard to describe :) Most complicated parts was about factory smart-contracts, wagmi usag, DAO logic and Chainlink connection to this service. What's next for Web3 FanZone Testing and build community. Extend functionality for better social integration. Option for burn NFT by multisign (for example you can create NFT-tickets, distribute it and but on usage). Marketing. Launch on Polygon mainnet. Partnership with other projects. <div