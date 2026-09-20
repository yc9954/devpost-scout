---
slug: "narrative-trails-letterbox"
url: "https://devpost.com/software/narrative-trails-letterbox"
title: "Narrative Trails - Letterbox"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 1110
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# Narrative Trails - Letterbox

> Get out and explore in the real world, remember your adventures on the blockchain. Our dApp uses RMRK multi-resource NFTs to add a digital component to the outdoor arts activity known as letterboxing

[Devpost](https://devpost.com/software/narrative-trails-letterbox) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**substrate** [[geospatial]]

**stack** fleek, hardhat, ipfs, javascript, moonriver, react, rmrk, solidity, web3-react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for narrative trails - letterbox

## Body

Inspiration Our inspiration originates from two sources. First, the amazing work of infrastructure builders in the Polkadot ecosystem who are creating a base layer with the potential to support many use cases. Our belief is that the infrastructure being developed will enable more small and mid-sized enterprises to adopt meaningful uses of this technology. Our second source of inspiration was one of the founder's family road-trip, which included some experimentation with the activity known as linkletterboxing. Our broadest, long-term vision is to create blockchain enhanced travel experiences under the name Narrative Trails, but we needed a way to build our skills, as well as test various required components of our bigger vision. With those needs in mind, we decided to create a letterboxing dApp for the hackathon. What it does Our dApp creates NFTs to enhance the letterboxing experience. Particularly for those who plant letterboxes and may not always get to see the stamps that are collected by the letterbox before they are destroyed or damaged by weather, or accidentally discarded by well intentioned passers by. For those not familiar with letterboxing, essentially our dApp will enable the minting of NFTs to serve as a user’s stamp, as well as NFTs to serve as letterboxes. In the real world, an individual will follow clues to find a letterbox that is hidden (outside in the world). Upon discovering the letterbox, the finder will use the stamp inside to mark their own notebook, while leaving their own stamp in the letterboxes’ logbook. Much like in the real world, multi-resource NFTs allow for letterbox NFTs to collect stamps, and for users to collect the letterbox stamps in their own NFT. Unlike the real world version, a letterbox planter using the dApp gets to see the stamps immediately after being found, and the logbooks are not lost if their box is waterlogged or otherwise destroyed. In addition, real world letterboxers only get to enjoy the other stamps a letterbox has gathered while they are physically at the letterbox. In the dApp, once a letterbox is found and collected (added to the stamp NFT of the user) they can view the stamps the box contains at any time. How we built it Our aim is to launch the dApp on Moonriver. We have built our contract using the RMRK EVM code and our current test site is on Moonbase Alpha. Fleek has been used for metadata storage and the React front-end deployment. When launched, we also plan to use Moonsafe multi-sig so that our dApp can be held by the Narrative Trails DAO (in progress). It should be noted that the RMRK EVM implementation is actively in development. Based on advice from members of the RMRK team (big thanks to Cicada on RMRK Implementers Telegram for being accessible and providing some really helpful answers), we used the dev branch, working throughout with the version available when our contract writing began. There have been a lot of changes to the RMRK code since that time, and we do plan to re-work our contract before launch to get up to date. Our test site is very open (did not activate all modifiers to restrict function calls) and we will also update that, but leaving it open allows us to experiment with different interactions more freely as we work out user experience details. Challenges we ran into We are a two person team, and neither of us had any experience working with blockchains (we have used them, but never built anything on-chain). Our work was divided into two areas: contract and deployment, and front-end, storage and hosting. Over the course of the hackathon, we learned a tremendous amount about the web3 tech stack. We attempted to use Crust, but were unable to deploy our front-end while using the Crust javascript library. Given the time constraints, we set that specific goal aside temporarily to move forward. It took us some time to work through the mechanics of front-end, wallet, contract interactions - details like having Metamask persist, understanding how to divide logic between contract and javascript, etc were challenges that pushed us to learn. Accomplishments that we're proud of Tom tackled all things front-end which, coming from a web2 background, meant learning a lot more about IPFS and other decentralized aspects of the tech stack. In addition, he learned a great deal about interacting with EVM smart contracts and wallets. Also gained a deeper understanding of front end development. Shawn comes from a background in Human Resources and non-profit administration. He comes with the longer term vision for Narrative Trails, and a few ideas for experiments to grow toward that goal including the Letterboxing dApp. In this project, he took on writing the smart contract. With limited programming experience, he had to learn everything from the basic setup of development environment, to writing solidity and later (basic, for testing) javascript, and reading RMRK EVM code to understand the concepts of a multiresource token. There’s a lot to learn, and programming is certainly an exercise in humility, but the hackathon has been a significant learning experience for Shawn. As you can imagine, some of Tom’s time went to explaining javascript or front-end concepts to Shawn. What we learned Tom tackled all things front-end which, coming from a web2 background, meant learning a lot more about IPFS and other decentralized aspects of the tech stack. In addition, he learned a great deal about interacting with EVM smart contracts and wallets. Also gained a deeper understanding of front end development. Shawn comes from a background in Human Resources and non-profit administration. He comes with the longer term vision for Narrative Trails, and a few ideas for experiments to grow toward that goal including the Letterboxing dApp. In this project, he took on writing the smart contract. With limited programming experience, he had to learn everything from the basic setup of development environment, to writing solidity and later (basic, for testing) javascript, and reading RMRK EVM code to understand the concepts of a multiresource token. There’s a lot to learn, and programming is certainly an exercise in humility, but the hackathon has been a significant learning experience for Shawn. As you can imagine, some of Tom’s time went to explaining javascript or front-end concepts to Shawn. What's next for Narrative Trails - Letterbox Tom and Shawn intend to continue to work on the project and launch the Letterboxing dApp on Moonriver, experiment with a DAO for Narrative Trails, and generally continue to explore web3. Several features are in progress, such as mapping of boxes, and we continue our search for other creatives (eg designer) to help us make it a terrific experience. <div