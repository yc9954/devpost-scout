---
slug: "verxio-protocol"
url: "https://devpost.com/software/verxio-protocol"
title: "Spacetar"
hackathon: "Privacy4Web3 Hackathon"
organization: "Oasis Foundation"
winner: true
words: 512
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/general_public"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# Spacetar

> Spacetar is a socialFI forum dApp that allows users to earn reward tokens by actively participating and engaging in the community.

[Devpost](https://devpost.com/software/verxio-protocol) · hackathon [[Privacy4Web3 Hackathon]]

## Facets

**user** [[general_public]]
**substrate** [[code_repository]] [[financial_record]]

**stack** javascript, oasis-sapphire-hardhat, oasis-sapphire-paratime, openai, rainbowkit, solidity, typescript, wagmi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for spacetar

## Body

Homepage Dashboard Page Forum Page Inspiration Spacetar is a groundbreaking SocialFi platform on Sapphire, a blockchain renowned for its speed and secure privacy. Inspired by the vision of connecting people and finance, Spacetar offers a universe of possibilities where community-driven innovation, trust, and financial empowerment converge. What it does Spacetar is a socialFI forum dApp that allows users to earn reward tokens by actively participating and engaging in the community. User's earned rewards can be swapped for any erc20 tokens on Sapphire and also rewards can be staked and locked to earn more interest and incentives. How we built it We built Spacetar using Solidity for the contract creation, Hardhat for the contract deployment, Oasis Sapphire Hardhat in our config file to initialize encryption of our contract, Javascript and Typescript for building out the frontend architecture, then Wagmi and Rainbowkit was used for the frontend integration. Challenges we ran into The major challenge initially was encrypting the transaction calls when made from the frontend. Oasis-Sapphire-Paratime currently supports ethers but the version of Wagmi we used uses View instead. Initially, transactions were open but after we figured out the cause of the challenge we dived deep into the View documentation and wrapped sapphire around the publicClient we were creating. Accomplishments that we're proud of We're immensely proud of Spacetar's achievements, including: Creating a thriving community-driven ecosystem that fosters innovation. Establishing secure and user-friendly financial pathways for our users. Promoting financial inclusion by connecting diverse users worldwide. Seamlessly integrating with the Sapphire blockchain for top-tier performance. Our accomplishments stand as a testament to our commitment to revolutionizing the socialFI and DeFi landscape and empowering individuals in the ever-expanding Spacetar cosmos. What we learned We learned in practicals how the encryption and privacy algorithm works exactly when building on Sapphire both for the hardhat side and the client side of the dApp. What's next for Spacetar Spacetar represents more than a socialFI decentralized application; it's a movement. In the future, we envision further enhancing the platform: Expanded Features: Our smart contract still has a lot of features that we'll continuously refine and expand on based on user feedback and evolving needs, ensuring it remains a cutting-edge and responsive platform. Also, we would be building out an admin section of the dApp so as to moderate things as the community grows. Decentralized Exchange : We would be working to integrate DEX into Spacetar so that users can be able to swap their reward tokens, stake their tokens, or gift reward tokens to other community members. Research and Innovation: Currently the '@oasisprotocol/sapphire-paratime'; only supports ethers so we would need to integrate support for views as we scale Spacetar. AI Chatbot: We are also working on leveraging OpenAI GPT-4 to integrate an AI chatbot assistance that will help the users navigate through the dApp as we expand our features. Anonymous Transfers: We are also working on integrating stealth addresses so users can receive crypto without revealing their wallet address which is their identity on the blockchain. This feature is heavily inspired by Vitalik's article on stealth addresses <div