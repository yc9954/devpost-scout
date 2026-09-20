---
slug: "softoken"
url: "https://devpost.com/software/softoken"
title: "SofToken"
hackathon: "dAppAthon "
organization: "Spheron "
winner: true
words: 903
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# SofToken

> A Secure & Efficient Solution for Software Licensing and Royalty using NFTs

[Devpost](https://devpost.com/software/softoken) · hackathon [[dAppAthon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]] [[video_visual]]

**stack** chainlink, filecoin, ipfs, mantle, polybase, push, solidity

## How they structured the write-up

- secure & efficient solution for open source software licenses.
- ⚒️ working of softoken
- ✨features
- ⚙️ tech stack
- 🔍 future scope
- 🗒️smart contract deployment
- 😫challenges we faced
- 👩‍💻 team members

## Body

Explore, Find and Filter NFTs NFT Details Profile Details Page Create NFT Notifications Tab Flowchart 🗄️ SofToken Secure & Efficient solution for Open Source Software Licenses. SofToken is a blockchain-based application that allows users to Mint a NFT for their software. Other users have a option to subscribe to the minted NFT and use it to build their own software. Different types of restrictions can be applied to the usage of a software before it is minted. ⚒️ Working of SofToken User creates his/her profile. The details are stored on IPFS & Polybase. User can Follow other people. User can mint NFT for his software having a option on which type of NFT he/she wants to mint. 3 ways to Mint NFT :- properietary executable : Only the executable file of the software minted (NFT A) is shared with User 2 User 2 cannot mint his own NFT B using NFT software A. Reusable & Modifiable (without Royalty): Code files are shared with the user User can mint his own NFT B using the software as a dependent NFT A. None of the total amount User 2 receives from his subscribers is given to User 1. Reusable & Modifiable (With Royalty): Code files are shared with the user User can mint his own NFT B using the software as a dependent NFT A. 10% of the total amount User 2 receives from his subscribers is given to User 1 as royalty fee. User can Filter out NFT Softwares based on Price, Ratings etc. User can give his own rating to the software. Live Price of the NFT is determined by the Ratings it gets. The rating is passed through Aggregator function which calculates the price of the NFT off the chain. (No gas consumed) User can subscribe to the NFT software. Once subscribed user can :- chat with the owner of the NFT software. Group chat with other subscribers to the same NFT software. Notifications are sent to the user on receiving messages. ✨Features Live Chart Demographics of top NFT softwares. Dymanic Price changes in NFT based on Ratings Mint NFT in 3 ways. Live 1-1 and Group chat with people. IPFS and Polybase Storage. Filter NFT's based on needs Notification sent to users. ⚙️ Tech Stack NextJS - Frontend Solidity - Smart Contract Mantle - Deployment of Contract. This helped us make the marketplace scalable, improve the user experience by improving the speed of minting tokens and also reducing the gas fees. Polygon - Deployment of Chainlink Functions Contract. This helped us push the computation for computing cost of an NFT based on user review dynamically off-the-chain, using Chainlink Functions. Polybase - Storing User and NFT details - the "backbone" of the project. This helped us literally gamify our marketplace experience. Be it introducing some small features like following other users, or storing the NFT metadata off-the-chain, our project was dependent on Polybase for everything. Polybase allowed us to design the schema the way we wanted, and implement a database system system just like we did in Web2 seamlessly. Push Protocol - this was the cherry on the top for improving the UX. Push Chat for 1-1 Chat: Buyers of an NFT could directly approach the owner/developer of the NFT for discussions. Push Group Chat: All the buyers of an NFT would be automatically added to a group chat for discussions regarding the software. This helps to not just license a software through an NFT, but also provide a community-like experience, thereby increasing the scope of the project immensely. Push Notifications: All the notifications from the personal/group chats, and new NFT creations from the users one has followed can be viewed as notifications. Chainlink Functions - Implementing Aggregator function off the chain. Although on a Beta release, the Chainlink Functions feature promises of an unlimited number of possibilities, allowing us to scale and expedite the DApps considerably. Filecoin/IPFS - Storing ZIP files of software, User Profile, Cover Images 🔍 Future Scope Implement TheGraph for fetching the live rates of the NFT's. Mobile Application for chart demographics. Categorizing NFT softwares into different domains. Integrate Push Notifs with TheGraph subgraph 🗒️Smart Contract Deployment Deployment Network - Mantle Testnet Contract Address: 0x744b61418D77d4C4AA953cD36403D353F7Cd947e Mantle Testnet Explorer Link: Link 😫Challenges we faced One of the challenges faced during the integration of push chat in NFTWare was related to the creation of groups by the NFT owners. The buyers needed to be added to these groups, but this was not possible directly because the NFT buyers could not add themselves to groups they were not already a part of. To solve this challenge, the development team came up with a solution that involved triggering an automatic message from the buyers to the NFT owners. The NFT owners could then verify these messages on direct messages (DMs) and subsequently add the buyers to the respective groups themselves. Overall, this approach allowed for a streamlined and secure process of adding buyers to the appropriate groups, ensuring that only authorized users could access the chat feature. Another major issue we faced was regarding the use Polybase. Referencing records of 2 collections was not the same as in Firebase, and the queries were rather more laborious than expected. However, it wasn't inconvenient, but it took some time to figure out how we'd relate 2 records of different collections. 👩‍💻 Team members Sarvagnya Purohit Harsh Nag Ananya Bangera Chaitya Vora Smit Sekhadia <div