---
slug: "tokertize"
url: "https://devpost.com/software/tokertize"
title: "Tokertize"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 1359
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Tokertize

> Fund your projects by selling ad revenue as a tradable NFT

[Devpost](https://devpost.com/software/tokertize) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[finance_payments]] [[supply_logistics]]
**substrate** [[document_pdf]] [[video_visual]] [[web_dom]]

**stack** alchemyapi, chainlink, docker, mongodb, moralis, node.js, polygon, solidity, truffle, vue, web3

## How they structured the write-up

- inspiration
- what it does
- how we built the mvp
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tokertize
- full project description
- contracts used
- contact

## Body

Tokertize Logo Inspiration The core idea to bridge NFTs and DeFi was generated during the early 2021 NFT hype, when numerous articles reported on large purchases of numerous NFTs that had all kind of digital products as an underlying, extending the craze from digital artwork to sport clips, Twitter posts and many more. In an attempt to understand the economic value of such NFTs non could be identified, instead the value was set to be whatever the market was willing to pay. Hence, it begs the first question: What would the same person pay for an NFT that had an actual monetary underlying? After conducting a feasibility study for an innovative use case to tokenize (ERC-721) YouTube videos with the idea to redirect ad-based revenue streams to new owners, a few significant barriers were identified which led to the adjustment to design such infrastructure for website owners who monetize their websites with an ad network in order to earn a passive income. However, the underlying product is not limited to websites and videos only, but also social media accounts, digital billboards, apps etc. Simply put anything that can be considered as inventory for advertisement placement. Further research revealed the possibility to create a new type of digital asset, which similar to mortgages in the U.S., could be securitized. This realization begs the second question: Can such NFTs be securitized as a new type of asset-backed security, opening up a new market? First conversations with financial institutions confirm their interest, yet would require a more detailed description of the business model and the asset, especially when it comes to the technical execution. Consequently, the aim of the Chainlink Fall 2021 Hackathon is to create a minimum viable product (MVP) to show a possible technical solution for the core functions of the intended business case and to establish a basis upon which further business-related decisions can be made. What it does Our use case implies the business model of an NFT platform that can dock to any existing ad network, both legacy and crypto-native ones, based on the plug and play principle. The innovative feature of the platform grants users, who monetized their digital products with the ad network, the possibility to tokenize (ERC-721) and sell future ad-based revenue streams. So far we have focused on one digital product (website) and one monetization method (ad unit). In the long run, we seek to expand our service portfolio. Through this type of tokenization, we effectively will create a new type of NFT - the first NFT with an actual financial underlying and dynamic properties. In the near future, these NFTs will be listed on a native NFT marketplace that seeks to facilitate NFT trading by providing the infrastructure of a secondary market. How we built the MVP Our tech stack for the MVP is Node.js for the API, Vue for the frontend, MongoDb for storage and Solidity for the smart contract. When creating an ad or registering a site to mint in our website, we store the data for that object in MongoDb. This object includes the ad text, ad link, ad image etc. The user then mints an ERC-721 token with an id that corresponds to an id in the document we have stored in MongoDb. When minting an ad, the minting process will include an amount of ETH that will be used to pay for ad impressions / clicks that the ad generates. In our API we have a scheduled job that fetches the ads and sites both from MongoDb and our smart contract. It then hydrates a memory cache object with a dictionary of all the ads with a non-zero balance, and all the sites that are minted. The site owners will place an iframe tag code block on their page with an url containing the id of their site token. When a GET request to view this ad lands in our API we look up the site data in our memory cache dictionary and select a random ad from the memory cache object to render and send that back. This results in the iframe being populated with a random ad with a non-zero balance of ETH each time the site is loaded. We also register the views for both the site and the ad in another memory cache dictionary. The rendered ad includes a link to our API with url parameters containing both the id of the site containing the ad box and the id of the ad. When someone clicks an ad we take these parameters from the url and register an ad click for both the site and the ad in our memory cache dictionary. Then we send a redirect response to the url from the ad object. Using in-memory lookups makes this very fast, and the end user will perceive the click as just pointing straight to the target page. We also have a IP filter that store the IP's where the ad views and ad clicks are coming from, and if we see the same IP within 5 minutes we will not register the impression into the statistics document. This is simply to avoid click-fraud. The ads are still rendered and clicks redirected. At a given interval we scrape the statistics from the memory cache and save it into MongoDb along with a timestamp of the scrape. This allows us to query statistics and provide endpoints for historic view and click statistics for both ads and sites. The smart contract uses Chainlink to poll our API for this statistics data, and calculates the payment flows according to this. Balances on ad tokens are subtracted and balances of sites are incremented according to how many clicks they have at the current time compared to last time their statistics were polled. The contract then provides calls for the site owners to withdraw earnings that their sites generated and for ad owners to supply funds to their ads. The smart contract implements the ERC-721 interface and thus allows the tokens to be listed on a marketplace and be sold. The API and frontend is Dockerized and the workload should allow scaling. Challenges we ran into Compatibility aspect of the NFT platform with crypto-native ad networks that have no stable coin solutions as well as legacy ad networks that pay out in fiat. this would require a tailored solution with a future financial partner (on & off ramp for fiat <> crypto, stable coins, other coins etc.) If we cannot reach compatibility/collaborations with ad networks the way we envision, we aim to design our own ad network or have a whitelabel solution. However, this will require extra time and expertise. A lot of ad networks don't have an API The securitization aspect requires leading banks to collaborate, connection has to be established. Accomplishments that we're proud of Formed a team and spread the passion for the project Converted thoughts into code Achieved the desired outcome for our MVP target Build friendships that will last beyond the Hackathon Completely built a transparent payment system and tracking for ad payment per click using chainlink on-chain/off-chain API integration. Offering a platform for both parties(advertisers and website owners) to get benefited mutually. What we learned We could narrow down the way to go forward with our project as the exact formulation of the business case was not clear from the start modifying the product architecture to make it plug n play with different types of digital assets types and integrable with existing ad systems. What's next for Tokertize Q4 21 – Q1 22 - Secure funding > Establish business & team > Whitepaper > Strategic partnerships with financial institutions Q1 22 – Q2 22 - Build out business case with focus on websites > Collaboration with ad networks > Pilot project Q2 22 – Q3 22 - Platform goes live > Marketing & Sales Q3 22 – Q4 23 - Expand services for other digital products and platforms Full project description Notion - Project Description Contracts Used 0xcCa094bf5F8D385B06f7835737563C24a13df469 -- webBaseNFT -- wTKTZ 0x1800DB78a312c04d8408263b5fed9bf0cd46a899 -- adBaseNFT -- aTKTZ 0x41985fb1EAdA74D597dC1a203b64c35120018cbf -- payment Contract Contact Waldi - boos.waldemar@gmail.com Sid - sidduHERE@protonmail.com Fred - studiefredfredrik@gmail.com <div