---
slug: "block-fabric-uplsq3"
url: "https://devpost.com/software/block-fabric-uplsq3"
title: "Block Fabric"
hackathon: "TRON Grand Hackathon - HackaTRON Season 6"
organization: "TRON DAO"
winner: true
words: 1181
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Block Fabric

> Block Fabric is an all-in-one platform for creating, deploying and managing smart contracts

[Devpost](https://devpost.com/software/block-fabric-uplsq3) · hackathon [[TRON Grand Hackathon - HackaTRON Season 6]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[security_privacy]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** amazon-web-services, nextjs, node.js, react, typescript, vercel

## How they structured the write-up

- block fabric is an all-in-one platform for building, deploying and managing smart contracts
- inspiration
- about the project
- features
- business model
- technical details
- project roadmap
- screenshots

## Body

AI model selection Smart contract deployments overview App creation selection Analytics dashboard Smart contracts code overview Smart contract creation wizard Block Fabric is an all-in-one platform for building, deploying and managing smart contracts Project Goal : We want to make it simpler for anyone to bring their Dapp ideas to life. By providing an easy to use platform to create, deploy, manage, and monitor smart contracts. Project Test Instructions Visit https://www.blockfabric.dev Click on the "Live Demo" button. Your temporary unique account is created, explore and make changes as you wish. Inspiration Our question: "How can we make the power of blockchain technology and smart contracts accessible to everyone, regardless of their technical proficiency?" The inspiration for Block Fabric comes from the understanding that blockchain technology holds vast potential to improve various aspects of our digital lives. Yet, this potential remains largely untapped because of the technical complexity associated with creating and managing decentralized applications (dApps). We wanted to provide a solution that didn't just cater to expert developers, but also to non-technical visionaries who have great ideas but lack the coding skills to translate those ideas into functional dApps. This led us to the conception of Block Fabric - a platform designed to enable anyone to easily create, deploy, manage, and gain useful insights into their smart contracts. About the Project Block Fabric is an all-in-one platform for creating, deploying and managing smart contracts on TRON and various blockchains. It enables straightforward creation, deployment, management, and analysis of smart contracts for both beginners and expert blockchain engineers. The platform is built with advanced and yet easy to use features including GitHub integration, no-code templates, analytics, AI code review and security analysis, storage and a holistic overview of your smart contracts What's New in Season 6 GitHub Integration : You can now link your GitHub repository and directly build and launch your smart contracts. **AI Code Review *: Choose from over 10 industry leading AI models to review your smart contract code for improvements and recommended practices directly on the Block Fabric platform. **AI Security Analysis *: Automatically scans your source code for security vulnerabilities and risks. Interactive Demo : See and interact with sample apps on Block Fabric without the need to login. Each demo is a temporary account unique to you so you are welcome to create or make any changes as you please. (credits to @fulldecent for the feedback in S5 on allowing users to see the app in action without login) Overall Polishing & Refinement : Over 15 improvements were made in the platform including UX uplift on several areas, rename app functionality, introducing additional info in app settings and sidebar, and bug fixes. BlockFabric Manifest File : Introducing a standardized blockfabric.json file that accompanies smart contract code, detailing how to build and deploy the contract. It includes essential information such as the contract's name, description, author, inputs, and dependencies. Rebranding under Comexias Labs * Supported AI models: Anthropic Claude 3 Sonnet, Anthropic Claude 3 Haiku, Anthropic Claude 2.1, Meta Llama 3, Meta Llama 2 70B, Amazon Titan Text G1 - Express, Mistral AI Mixtral 8x7B Instruct, Mistral AI Mistral 7B Instruct, Cohere Command, Cohere Command Light, AI21 Labs Jurassic-2 Mid Features AI Code Review & Security Analysis Automatically scans your smart contract code for improvement and security vulnerability. No Code Smart Contract Templates Build and deploy your contracts from a growing collection of Community Contributed preset templates you can use and customize, no coding required. GitHub Integration Link your GitHub repo and build and deploy directly from smart contract codes in your repository. Import Existing Smart Contracts Easily import contracts that you already have active on the blockchain. App Manager Create and organize apps and smart contracts in a unified interface which gives you a holistic view of your apps. Built-in Compiler and Deployer Compile your smart contracts and deploy them to testnet and mainnet with a button click, directly on the platform. Analytics & Insights See insights and understand how people interact with your dapp. Storage Browser Browse and organize your decentralized files directly on Block Fabric. (Powered by BNB Greenfield) Note: Greenfield, like IPFS, is a standalone storage solution and can be used by apps on different chains, like TRON Interactive Demo See and interact with sample apps on Block Fabric without the need to login. Each demo is a temporary account unique to you so you are welcome to create or make any changes as you please. Multiple Blockchain Support Blockchain: TRON, BNB Smart Chain, Fantom, Areon Storage Provider: BNB Greenfield, IPFS (Coming soon) Business Model Summary: Free and publicly available While we aim to keep the majority of features free so anyone can experience and use BlockFabric, we plan to introduce a freemium model in the future to sustain the project's development. The platform will still remain free for basic use. We are in a development and growth stage and will put off monetization for now. Technical Details Architecture Overview Web Application & APIs The frontend Web Application is developed in React using the NextJS framework. The authentication, analytics and core APIs are developed in NodeJS. These applications are hosted on Vercel . Artificial Intelligence (AI) Block Fabric's AI capabilities lives on a completely separate stack from the main application/ Hosted entirely on AWS and powered by AWS Bedrock, the AI service consist of a custom developed streaming enabled lambda function that intelligently maps requests from Block Fabric into various AI models on Bedrock, adjusting inference parameters as required depending on the selected model. Compiler Solidity Compiler (Solc) is used for compiling Solidity code into Contract Application Binary Image (ABI) and byte code. Contract Interactions/Deployments TronWeb and Web3Js libraries are used for all contract interactions, including deployments. Block Explorers We rely on data from block explorers such as TronScan API to power our analytics dashboard. Off-chain Database The offchain database is used for various operations of the application and is hosted on Google Firebase using the Firestore service. Decentralized Storage BNB Greenfield is the decentralized storage used on Block Fabric. Note: Greenfield, like IPFS, is a standalone storage solution and can be used by apps on different chains, like TRON Project Roadmap Q1/Q2 2024 (TRON Hackathon S6) GitHub Integration AI Code Review AI Security Analysis Interactive Demo Overall Polishing & Refinement BlockFabric Manifest File Rebranding under Comexias Labs See "What's New in Season 6" above for more details Q4 2023 Setting up hygraph CMS for docs site and foundation for learning center Launch documentation site with coverage Deep research on generative AI models and use cases for Block Fabric Q3 2023 (TRON Hackathon S5) Open-sourced contract templates for community contribution Analytics and insights dashboard Contract Functions with interactions/execution Ability to import existing contracts on the blockchain Integration with Greenfield decentralized storage Overall UI/UX improvement Promote to Open Beta stage Submission to TRON Hackathon S5 Q2 2023 Project inception, early planning and prototyping POC available with minimum features: Create and manage apps Build contract from templates Deploy contract to mainnet or testnet View Code, ABI and ByteCode View Functions, without interaction suport Screenshots <div