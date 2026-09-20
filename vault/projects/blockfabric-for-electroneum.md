---
slug: "blockfabric-for-electroneum"
url: "https://devpost.com/software/blockfabric-for-electroneum"
title: "BlockFabric for Electroneum"
hackathon: "Electroneum Hackathon 2025"
organization: "Electroneum"
winner: true
words: 825
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# BlockFabric for Electroneum

> BlockFabric is an all-in-one development studio for building, deploying and managing smart contracts

[Devpost](https://devpost.com/software/blockfabric-for-electroneum) · hackathon [[Electroneum Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** amazon-web-services, nextjs, react, vercel

## How they structured the write-up

- blockfabric is an all-in-one development studio for building, deploying and managing smart contracts
- about the project
- community feedback
- features
- business model
- technical details
- open source
- screenshots

## Body

BlockFabric is an all-in-one development studio for building, deploying and managing smart contracts Project Goal: We want to make it easy for anyone to bring their Dapp ideas to life, by providing a simple to use platform to build and manage smart contracts. Project Test Instructions Visit https://www.blockfabric.dev Click on the "Live Demo" button. Your temporary unique account is created, explore and make changes as you wish. Inspiration The inspiration for BlockFabric comes from the understanding that blockchain technology holds vast potential to improve various aspects of our digital lives. Yet, this potential remains largely untapped because of the technical complexity associated with creating and managing decentralized applications (dApps). We wanted to provide a solution that didn't just cater to expert developers, but also to non-technical visionaries who have great ideas but lack the coding skills to translate those ideas into functional dApps. This led us to the conception of BlockFabric - a platform designed to enable anyone to easily create, deploy, manage, and gain useful insights into their smart contracts. About the Project BlockFabric is web based all-in-one contracts development studio for creating, deploying and managing smart contracts on Electroneum and various blockchains. It enables straightforward creation, deployment, management, and analysis of smart contracts for both beginners and expert blockchain engineers. The platform is built with advanced and yet easy to use features including GitHub integration, no-code templates, analytics, AI code review and security analysis, storage and a holistic overview of your smart contracts Community Feedback We have introduced two important features based on recent community feedback: Demo mode which lets users explore the app without having to connect their wallet and deploy actual contracts. Create contracts from AI, this is a new and experimental feature that we are developing. On our roadmap is to also include the auto contract code verification feature. Features AI Code Generator (NEW) Leverage generative AI to create your smart contracts. This is an experimental feature. AI Code Review & Security Analysis Automatically scans your smart contract code for improvement and security vulnerability. Comprehensive Documentation BlockFabric offers extensive documentation to help developers get started and build on the platform. No Code Smart Contract Templates Build and deploy your contracts from a growing collection of Community Contributed preset templates you can use and customize, no coding required. GitHub Integration Link your GitHub repo and build and deploy directly from smart contract codes in your repository. Import Existing Smart Contracts Easily import contracts that you already have active on the blockchain. App Manager Create and organize apps and smart contracts in a unified interface which gives you a holistic view of your apps. Built-in Compiler and Deployer Compile your smart contracts and deploy them to testnet and mainnet with a button click, directly on the platform. Analytics & Insights See insights and understand how people interact with your dapp. Storage Browser Browse and organize your decentralized files directly on BlockFabric. (Powered by BNB Greenfield) Note: Greenfield, like IPFS, is a standalone storage solution and can be used by apps on different chains Interactive Demo See and interact with sample apps on BlockFabric without the need to login. Each demo is a temporary account unique to you so you are welcome to create or make any changes as you please. Multiple Blockchain Support Blockchain: Electroneum, TRON, BNB Smart Chain, Fantom, Areon Storage Provider: BNB Greenfield, IPFS (Coming soon) Coming Soon Contract verification Contract API Business Model Summary: Free and publicly available While we strive to keep the majority of features free so anyone can experience and use BlockFabric, we plan to introduce a freemium model in the future to sustain the project's development. The platform will still remain free for basic use. Technical Details Architecture Overview Web Application & APIs The frontend Web Application is developed in React using the NextJS framework. The authentication, analytics and core APIs are developed in NodeJS. These applications are hosted on Vercel . Artificial Intelligence (AI) BlockFabric AI capabilities is powered by AWS and consist of a custom developed streaming API that intelligently maps requests from BlockFabric into various AI models on Amazon Bedrock, adjusting inference parameters as required depending on the selected model. Compiler Solidity Compiler (Solc) is used for compiling Solidity code into Contract Application Binary Image (ABI) and byte code. Contract Interactions/Deployments Web3.js is the library we use for all contract interactions, including deployments. Block Explorers We rely on data from block explorers such as Electroneum Block Explorer API to power our analytics dashboard. Off-chain Database The offchain database is used for various operations of the application and is hosted on Google Firebase using the Firestore service. Decentralized Storage BNB Greenfield is the decentralized storage used on BlockFabric. Note: Greenfield, like IPFS, is a standalone storage solution and can be used by apps on different chains Open Source We've open-sourced the smart contract templates for BlockFabric to support the community. However, the core application code that powers the platform remains private. Screenshots <div