---
slug: "scientia-dao"
url: "https://devpost.com/software/scientia-dao"
title: "Scientia DAO"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 1247
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/researcher"
  - "substrate/web_dom"
---

# Scientia DAO

> Scientia DAO is the first DAO Community for Scientists & Researchers. Researchers from around the world can become a DAO member and share their researches, studies and a lot more!

[Devpost](https://devpost.com/software/scientia-dao) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[civic_government]] [[developer_tools]]
**user** [[researcher]]
**substrate** [[web_dom]]

**stack** alchemyapi, chainlink, css3, ethers.js, hardhat, html5, ipfs, javascript, next, polygon, rainbowkit, react, wagmi.js, web3.storage

## How they structured the write-up

- inspiration
- what it does
- how we built it
- sponsor technologies used
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for scientia dao?

## Body

Landing page Scientia DAO DAO features DAO joining steps Publish research page Request for grants section Contribution and Powered By section Future Plans for Scientia DAO Process of Joining the DAO Process of Publishing a Research Process of applying for Grants Inspiration We wanted to build a project for the research and scientific community and provide them with a platform where they can share their work and collaborate with other fellow researchers from around the globe. This project is one of it's kind and no such good platform exists yet in web3, this Space is not even explored much. We came up with the idea of Scientia DAO through which we can help bring the scientific community in a single place and contribute our best as a general audience to help them keep exploring the wonderful world of research & science. What it does The platform allows researchers & scientists to become a DAO member by submitting a request, the entry proposal is then sent to DAO dashboard where all the members can see it and approve the entry through voting. Once the request is approved, a DAO member NFT is minted, and now any member can publish their research to IPFS through the /publish page. After a research is published, anyone on the internet can visit the /explore page and read it along with other published researches. In the DAO dashboard section, members also have an option to request for grants by submitting a grant proposal which can be approved by other members through voting. The platform also offers the general audience to contribute to research by paying any amount of their choice, after someone contributes they are minted a contributor NFT. The amount collected by the means of contributors is used to pay for the grants that are requested by members to start a new research. NOTE Website is compatible with all kind of devices and is flexible to use on any device , even Smart Phones . The wallet can be connected too with help of Mobile wallet. How we built it We are a team of four members who built this project from scratch. We divided our work on the basis of our skill set. Kushagra Sarathe - Worked on designing and building the frontend of this project. Dhruv Agarwal - Worked on integration, writing & improving smart-contracts for this project. Aditya Gupta - Worked on backend & writing smart contracts. Nils Giebing - Worked on backend & writing smart contracts. We used NextJs , CSS & JavaScript to build the frontend for this project. Our backend is powered by: Polygon : For deploying contracts on the Polygon Blockchain. IPFS/web3.storage : For decentralized storage of all the data and querying the data from IPFS. Chainlink - Keepers used to close the voting system in Member and Grants Request. Spheron : For decentralized hosting. Smart Contracts are written in Solidity, tested well and managed in the best possible way by the team members working on the contracts part. Deployed on Polygon Testnet with Hardhat and Alchemy as a node provider. The integration is done with Javascript , Wagmi.js , Ethers.js . Rainbow-Kit is used for the Connect Wallet component . Wagmi.js & Ethers.js are used for interaction with Polygon chain from frontend application and the contract management. All components are created in ES6 JS. NFTs are minted on Polygon Testnet. The NFTs are completely Soul-Bound tokens , non transferrable and can only be burnt and minted. The Member NFT is used for token gating on the website. The Contributor NFT is a token of appreciation, for contribution to the DAO. Collection link: MemberNFT , Contributor NFT Sponsor Technologies used Web3.Storage is used for storing all sort of Data including user profile, grants request and researches on IPFS , done with the help of the SDK provided and stored in JSON format. The querying of the data is done with CID Gateway links and then rendered in Frontend. The CIDs are stored in contract to avoid data tampering. Video Explanation Refer these components for more info : StoreMembers , StoreResearch , StoreRequests , StoreContent Chainlink Keepers are being used to end the voting for members entry request and grants request. Created 2 Time based trigger upkeeps for Members Contract and Grants Contract. These upkeeps runs once in 2 days and close all the open requests if so available in the contract . This is done in order to remove all discrepancies related to one person control. Video Explantation Member Contract Upkeep , Grants Contract Upkeep Spheron - Hosting of website on decentralized storage , IPFS(FileCoin) . Live link for project: Spheron Challenges we ran into We enjoyed every minute building this project, apart from the times we faced errors. 😅 Some issues that we ran into while building this platform: Deciding how to take new member entry. Since this platform is research and scientific community focused, we wanted to keep the membership to only genuine people. To avoid any type of spams, we decided to go with the voting option. Keeping the UX simple. The project idea was quite new, and we couldn't find many resources regarding how we should be implementing the whole idea. We decided to keep navigation flow simple so that anyone can easily navigate through the application. Managing multiple contracts (5) for a single platform together at the same time and integrating them in frontend. We faced issues in retrieving data from IPFS & contracts in the proper format , but later it was resolved. Integrating the contracts and creating components for each task was really a big task for us. We made over 15 components to add the actually functionality, handled well by all the team members. Accomplishments that we're proud of The best accomplishment was to bring an idea to life. To be able to make a platform that allows great researchers and scientists to showcase their work to the world To make the platforms so simple for anyone to understand, even with no technical knowledge of web3. To create a DAO that even supports the researchers in their researches by providing grants. To provide Soul Bound tokens (NFTs) for the members and contributors. What we learned How to make plans as a team and delegate tasks and work collaboratively. Every person in the team as a learned a lot from each others ,backend and frontend. Brain storming an idea and actually implement that into a project. How to build such a big scale project from scratch in under a period of 2-3 weeks. How to make Soul-Bound tokens for the DAO membership. Token gating of website for the DAO member specific section. Detailed use of Web3.storage package. Querying the data from IPFS & contract and rendering the same in the respective sections. What's next for Scientia DAO? Next we want to add more features to the platform like: Collaborate & contribution feature for DAO Members by which members can collaborate on new researches and contribute to published research with their knowledge. Milestone feature for grants so that the grants that are approved by members would be divided into milestones and the amount for next milestone would only be released after the previous milestone has been finished and approved by all the members. Build a token and governance system for the DAO. Add organization support to DAO through which organizations can also join the DAO and share their work (e.g. Polygon publish their researches on Scientia DAO 🤩). <div