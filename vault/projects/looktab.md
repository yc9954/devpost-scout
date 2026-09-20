---
slug: "looktab"
url: "https://devpost.com/software/looktab"
title: "LOOKTAB"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 897
team_size: 6
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/web_dom"
---

# LOOKTAB

> LOOKTAB🖐 is the first AR-based mobile DApp on Near. We connect market owners and their customers with NFT Reward Program!

[Devpost](https://devpost.com/software/looktab) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[web_dom]]

**stack** android, kotlin, near, rust, typescript, wallet-selector

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for looktab

## Body

LOOKTAB: the first AR-based mobile DApp on Near. Inspiration Do you know Pokemon Go is the longest users' average time-spending app in the world? We're inspired by success of AR application like Pokemon Go to increase offline-based digital user experience. With Blockchain/Web3, We found new AR-based mobile application can give another WOW moment to users. What it does 1. AR-based offline information aggregator LOOKTAB is an AR-based mobile DApp for offline store owners and their potential customers and gives our users a fun and exciting experience with NFT Reward Program! With AR, offline space can show much more information. If you feel hard to imagine, Please watch HYPER-REALITY which describes futuristic offline experience with AR. LOOKTAB breaks limitation of offline space to give great user-experience with our mobile DApp. Users can find their local information by strolling around cities with their mobile device and get reward as form of NFTs from store owners. 2. NFT Reward Program We're aiming to help users seamlessly onboard our DApp and concept of web3. NFTs are the most powerful tools to start the journey of Web3 for users like Reddit NFTs did. Moreover, Gamification factors can increase users' engagement with offline stores. Users can use NFTs as a role of reward, including the concept of coupons or badges as proof of membership. Users can check these NFTs with mobile in-app Near Wallet and redeem them quickly. Furthermore, Store owners can make their own NFT Reward Program with our solution. It would be getting used to ordinary people since Starbucks also launched the NFT-based Loyalty Program . How we built it LOOKTAB has 2 main parts: LOOKTAB Mobile DApp On the user interface level, we created a mobile DApp using Android that enables users to manage their Near Wallet and NFT Reward. Users can get NFT Rewards from Airdrop and redeem them in offline stores. Store owners can check their ownership of reward from their wallet id. Users can get additional incentives when they contribute to LOOKTAB ecosystem by reviewing some stores and adding useful information. LOOKTAB NFT Maker Store owners are not used to technical side of NFTs, so we made a NFT Maker which helps store owners to make their own NFT Reward without any technical knowledge. Store owners can make their Near wallet in NFT Maker Site and mint NFT Rewards before doing airdrop with it. We deployed our own Rust-based NFT smart contract on near, which is from paras's smart contract. website Challenges we ran into At first time, we architected to use Multi Token based on NEP-245 for NFT Reward Program because it's easier and more efficient to handle airdrop logic by batch-transfer. However, NEP171 based NFT is also very user-friendly because Near protocol offers a lot of tutorials and materials to refer. Moreover its infrastructure is very stable and fast. Accomplishments that we're proud of Coming with no background in web3, developing for Mobile DApp on Near was pretty easy. We expected that developing a Mobile DApp would be the most challenging part of the process, and we were surprised to realize it wasn't hard! We used near-api-kotlin to interact with our smart contract. There is just a few Mobile focused DApp in Near Ecosystem, and we made production-level reference to develop mobile DApp to interact with Near Smart Contract. For Mass Adoption of Users, UI/UX is significant. In Web3, Wallet Onboarding is one of the most critical parts while users use the app. We tried to make our Dapp simple and easy to use for anyone who needs to learn more about Web3 and Blockchain. So we adopted wallet-selector in our NFT Maker, which helps users seamlessly log in by using their wallet. We hope this will be a new standard to increase user experience. What we learned Siena As someone who loves the Web3 ecosystem, I am honored to be working on my first project with Near Protocol. As an Android developer, it was very interesting to be able to embed a wallet. It was an honor to be able to directly edit the near-api-kotlin sdk! Next time, I want to make a contract myself and carry out an even cooler project!! It was so much fun! Jungdong It was meaningful time to learn how to design Near Smart Contract and contribute Near Ecosystem by increasing User Experience! Sewon I learned how to write, test and compile Near smart contracts with Rust. Accomplishments that we're proud of I'm proud that I was able to build such a large project that can help solving business problems based on Near. Also every functions works nicely Youngmin It seems that it provided customized information that users need when offline, which is difficult to easily obtain information, and at the same time, it seemed that users with low understanding of web3 could easily access it with interest through the app. It was such a beneficial experience to grow the project quickly through this NEAR MetaBUILD III Hackathon. In addition, all the team members participated passionately, so I was able to enjoy the project. What's next for LOOKTAB Develop Semi-Fungible Token Standard to optimize NFT Reward Program Build Admin dashboard to analyze and track airdrop results for Store Owners Make partnerships with some local stores to make their own NFT Reward Program together Optimize AR functionalities by development of our own SDK Fundraising for scaling our application globally <div