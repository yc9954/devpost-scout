---
slug: "podship"
url: "https://devpost.com/software/podship"
title: "PodShip"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 389
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# PodShip

> A Decentralized Podcast Sharing & Streaming Platform.

[Devpost](https://devpost.com/software/podship) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** chainlink, filecoin, hardhat, ipfs, javascript, metamask, next.js, openzepplin, polygon, quicknode, solidity, thegraph, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for podship

## Body

Home Page Upload Page Single Podcast Page Tipping Feature Supporters & Winner Page Powered by section Explore Page Inspiration Podcasters create so much value in our lives with their podcasts but in return, many of the podcasters don't get enough benefits especially financially. In fact, some of the podcast channels have negative cash flows. Users, who provide their valuable time to the platforms, don’t get many benefits from it instead Web2 platforms don’t respect their Users’ Data & Privacy. PodShip's main goal is to support Podcasters & Give Users Full Data privacy What it does PodShip empowers Podcasters to upload their podcasts over a decentralized Internet and mint it as an NFT. Podcasters then can sell their Podcasts NFTs using PodShip thru Auctions. PodShip provides Podcasters & Users with an easy, fast & reliable Value-For-Value framework. With the help of that framework, Podcasters can receive seamless and direct tips from their fans using the Tipping Functionality. PodShip also incentives the users with SupporterNFTs based on their engagements (every week a winner will be selected among the supporters). How we built it The Dapp front-end is built using Next.js . We used Hardhat for Smart Contracts development and deployment. We are storing Podcast NFTs metadata on IPFS/Filecoin using NFT.storage. As PodShip allows tips as low as $1, we used Chainlink Price & Data Feeds there to make sure that no one sends tips lower than $1.We are using Chainlink's VRF , to make sure that SupporterNFTs winners are selected with full fairness. We are also using Chainlink Automation (upKeeps) services, so that selection & giveaway of the SupportersNFTs are done automatically. It's built on Polygon , an eco-friendly blockchain. For the lighting-fast API/RPC Endpoint, we are using QuickNode . we are using subgraphs from the TheGraph protocol to index data entities from the blockchain. Accomplishments that we're proud of We are really glad that we were able to complete the PodShip's MVP in a month and deployed the dapp on the Polygon testnet & also published a live demo. What we learned Chainlink's Awesome Services and NFT.storage easy to use SDK What's next for PodShip Add Upvotes feature Gasless Transactions Improve UI/UX Mobile Application Mainnet Deployment on the Polygon Network Follow us on Twitter @PodShipNFT Note: PodShip Project is on 3 GitHub Repos. Smart-Contracts Repo Front-End Repo SubGraphs Repo <div