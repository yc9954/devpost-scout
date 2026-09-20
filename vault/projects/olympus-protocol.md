---
slug: "olympus-protocol"
url: "https://devpost.com/software/olympus-protocol"
title: "Olympus Protocol"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 675
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# Olympus Protocol

> Activating web3 communities IRL through an augmented reality protocol

[Devpost](https://devpost.com/software/olympus-protocol) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]]

**stack** 8thwall, coinbase, coinbase-wallet, firebase, google-maps, ipfs, niantic, polygon, solidity, storj, thirdweb

## How they structured the write-up

- the game
- what it does
- how we built it
- what inspired us
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for olympus protocol

## Body

The Game Players compete to claim locations, landmarks, neighborhoods and entire cities for their web3 community. Claim - Claim a location by pinning an NFT from your wallet onto the location Collect - Earn $OLY for visiting locations and meeting up with friends Upgrade - Fortify your claimed location with a stronger fortress Vandalize - Compete to attack and take over other locations What it does Olympus is a generalized standard for pinning data to real world locations in the metaverse. Our infrastructure will provide application specific extensions that enable different use cases (ex. AR, real estate, events). Our developer SDK will provide rapid development APIs to easily build engaging AR experiences for web3 communities. Partnerships Part of our monetization strategy involves sponsored locations where IRL businesses can host giveaways. Instead of claiming $OLY tokens at this location, users can claim NFT's that can be exchanged for freebies at that business. Our first partnership is with Froth NYC https://www.instagram.com/frothnewyork/?hl=en - where users can claim a free coffee by collecting the Froth NFT at their lower east side location. How we built it Coinbase Wallet Coinbase Wallet is used to get the users wallet address and also authorize and validate transactions on the blockchain. In order to play our game, new users to web3 will need to create their first crypto wallet with Coinbase. Polygon Smart Contracts We created two custom smart contracts. One for minting 1 trillion $OLY reward tokens and one for in-game player interactions. The Player interactions are vandalize: takes X amount of tokens out of the players wallet to reduce a locations health points. , upgrade: takes X amount of tokens out of the players wallet to reduce a locations health points, claim: distributes $OLY token rewards to users for daily and multiplier bonuses. The user has to approve the transaction contract to transfer tokens. The contracts inherit the ERC-2771 context contract which enables gasless transactions. thirdweb SDK We are using thirdweb to deploy our contracts onto the Polygon L2 blockchain. We utilized the thirdweb SDK to facilitate our contract interactions and authorize wallets through their contract authorization script. This script provide a cookie to the user to validate their wallet once every 6 hours rather than requiring the user to re-validate for every transaction. We are using OpenZeppelin defender for their relay service, which is utilized to conduct gasless transacations on behalf of the user. Google Maps JavaScript API We are using the Google Maps React library to render an interactive view of AR locations. Backend APIs and Database (Firebase) We are utilizing Firebase to track metadata about each AR location. It is also used to pull information about how many tokens have been accrued at a location. This is called when players try to collect tokens from a location. IPFS and Storj We are using thirdweb deploy to pin the ABI to IPFS. In addition we are using Storj IPFS pinning to host in-game static assets. What inspired us We were inspired to use Niantic technologies, who are the creators behind Pokemon Go. We want people to get out into the real world and have fun, explore web3 communities in real time. Challenges we ran into Challenges we ran into were integrating web3 technologies into the AR experience. There is little documentation on this so we had to do a lot of hard-wiring to get it to work. Accomplishments that we're proud of We are proud of our video demo which we filmed together as friends in NYC. It was a super fun experience and we hope everyone has a laugh when they watch it! What we learned We learned that AR is still a space that needs a of exploration. We were excited to build this project to be pioneers for AR in web3. What's next for Olympus Protocol With Olympus, we are interested in building the game out further and deploying to mainnet Polygon. We want others to start to have fun and play our game. We are also interested in exploring an accelerator program with Snapchat. <div