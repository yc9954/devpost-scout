---
slug: "darchive-128hoy"
url: "https://devpost.com/software/darchive-128hoy"
title: "dArchive"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 731
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/media_journalism"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# dArchive

> dArchive (Decentralized Archive) is a decentralized application to create an archive of web pages that can always be accessed online even if the original page disappears.

[Devpost](https://devpost.com/software/darchive-128hoy) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[media_journalism]]
**substrate** [[financial_record]] [[video_visual]] [[web_dom]]

**stack** filecoin, heroku, ipfs, javascript, next.js, nft.storage, polygon, rainbowkit, spheron, typescript, vercel, wagmi, web3.storage

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for darchive

## Body

Home page Archive page Search page Support page FAQ page About page Inspiration I wanted to create an archive of web pages to create a time capsule for web pages. A popular solution already exists called archive.today but it's not decentralized so I wanted to create a web3 version of it so that the saved webpages are stored on decentralized storage providers like IPFS and Filecoin and also deploy it to the decentralized cloud using Spheron and using the fast, scalable, flexible and cost-effective solution called Polygon. What it does It allows a user to save a webpage HTML, screenshot, and metadata to the decentralized storage providers like IPFS and Filecoin, and the content identifier of the folder, title, and URL is emitted as an event and indexed using the graph for querying and filtering. The user can search the stored webpages based on different filters and can view and download the saved webpages and screenshots. This can be useful if you want to take a 'snapshot' of a page that could change soon: price list, job offer, real estate listing, drunk blog post, etc. Users can support the project by donating to the project using polygon MATIC which can be used for paying for storage, hosting, indexing, and meta transactions to let other users save their webpages without paying fees. How I built it Sponsor Technologies Used: Web3.storage , nft.storage and Spheron . I used different web3 technologies like Polygon blockchain, web3.storage , nft.storage , IPFS , Filecoin , Spheron , Alchemy, and the graph to build this project. Single page HTML, screenshot, and metadata are captured using a process involving puppeteer (browser automation) using single-file-cli . Then, web3.storage is used to store the webpage HTML, screenshot, and metadata regarding the webpage in the IPFS & Filecoin storage providers. nft.storage is also used to store the SoulBound supporter NFT metadata and image. The smart contract is deployed to the polygon blockchain and it is used to emit the content identifier, title, and URL as an event. Then, the smart contract is indexed using the subgraph which let us create the decentralized API to query the stored webpages. Spheron is used for deploying the dApp to the decentralized cloud easily. The Alchemy RPC node is used to interact with the polygon blockchain. I wrote smart contracts with solidity and Hardhat (containing ethers.js, Alchemy RPC node, and more) as a development environment to test and deploy it to polygon testnet. I used Next.js, Chakra UI, and Typescript to build the frontend, and the Wallet connection was facilitated using Rainbowkit which uses wagmi.sh under the hood. Challenges I ran into The challenge I ran into was to get the HTML and screenshot of the webpage and store and access it. Then, I used single-file-cli which uses puppeteer (browser automation) to open the webpage and save its web content as a single HTML file and also save the screenshot and the metadata like URL and title of the webpage. Accomplishments that I am proud of I am proud of what I am able to accomplish today. I Created a decentralized web3 version of archive.today Added meta transactions to the smart contract to let other users save their web pages without paying fees. Made the dApp easier to save a webpage to archive and query for it. What I learned I learned a lot during building this project. I Learned and Integrated different technologies to build this project. I learned: How to make use of different services like web3.storage, IPFS, Filecoin, Spheron, Alchemy, the graph, and polygon in unison to build this project. How to make use of SoulBound NFTs for the supporters of the project. Thinking and Working on the different aspects of the project and overcoming the challenges I ran into. Exploring different ways to deploy the project using Spheron, Vercel, Heroku, etc. What's next for dArchive There is always room for improvement so I want to make the following improvements to the project moving forward. Add a time-based search feature to search the webpages by saved timestamp. Optimize the front end to make it faster and more user-friendly. Optimize the flow for capturing the HTML and screenshots of the webpage. Deploy the code for getting the HTML and screenshot to better infrastructure and plans for adjusting the request timeout. Explore ways to make use of SoulBound NFTs minted for the supporters. <div