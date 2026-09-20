---
slug: "promptreality"
url: "https://devpost.com/software/promptreality"
title: "PromptReality"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 549
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/supply_logistics"
  - "substrate/video_visual"
---

# PromptReality

> A platform for creating AI experiences in Mixed Reality

[Devpost](https://devpost.com/software/promptreality) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**domain** [[supply_logistics]]
**substrate** [[video_visual]]
  <sub>weak: financial_record</sub>

**stack** chainlik, javascript, next.js, polygon, python, solidity, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for promptreality

## Body

CCIP Transaction Inspiration With the modern trend in AI, there are a lot of people who can use generation AI to create artistic images but what if you were able to render them in reality and interact with them? What it does Artists can use our application to demonstrate their creativity by selecting an AI model and prompting it with a creative prompt which is hashed and stored secretly, this prompt creates a generation which is validated on a chain and mints an NFT with this validated URI and hashed prompt which can be traded on the marketplace. Users on the web app can log in with their email and can simply pin any of the assets on-chain from their inventory that they chose to render and interact with in the Mixed Reality. Using the client app users need to log in with their same email and the app fetches the user's pinned asset from the contract deployed on Polygon Amoy. API stores every user's email and corresponding wallet address so the user only needs to provide their email on the client app. How we built it Technologies: This project combines a smart contract with a mixed reality application through a connecting API and a web app from where users can express their art through prompting. Polygon Amoy: For deploying smart contracts for trading MR models and pinning assets. 0x55dbA48D5B0c279160Af3C26EbD58619bA948CAC Avalanche Fuji: Shown as a CCIP receiver exhibits all the features of the platform. 0x2f30921869dc2Cd6cD48373ef1E7c752958B990E Scroll Sepolia: For deploying smart contracts for trading MR models and pinning assets. 0x51390fB1C9ec18B6a0b7047815E0F224DD99A49F Chainlink: Data-feeds for fetching price from Matic to USD, API Functions for calling generation API from inside smart contract and CCIP for bridging NFTs from Polygon Amoy to Avalanche Fuji. CCIP tx Chainlink Functions tx AI Models: They get options to either choose Meshy AI for 3d models or DallE for 2d models. Web app: Every time a user requests a model generation, our API securely calls the selected AI model and responds to our connecting API with the generation. Smart Contract: At this same moment, model NFT is minted and the call moves to the chainlink function for verifying the latest generation at our API endpoint for the calling user. Once verified, it sets the NFT URI to the latest generation. AR app: Now, the user upon launching their AR applications will be logging in with the same email as the web app and this will read the user's synced pin asset on the contract and render it in reality where users can interact with it. Challenges we ran into Ensuring a running combination of APIs, Smart-contracts, Web-app and AR-app along with Chainlink features was a troubling task. Accomplishments that we're proud of We were able to pull off the project in the hackathon timeline by using 3 chainlink features. We built a properly functioning MVP with Smart contracts, APIs, web-app client and mobile-app client. What we learned We learned a lot in AR space about creating mixed reality applications and along with that to make sure that the API backend was able to perfectly communicate with the Smart contract, Web-app and Client-app was a challenge as well. What's next for PromptReality We'll try to introduce more artistic features where users can interact better with their generated assets. <div