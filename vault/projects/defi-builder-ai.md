---
slug: "defi-builder-ai"
url: "https://devpost.com/software/defi-builder-ai"
title: "DeFi Builder"
hackathon: "Block Magic: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 649
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/structured_db"
---

# DeFi Builder

> The all-in-one AI Powered Solution for Web3 Smart Contract Security and Deployment.

[Devpost](https://devpost.com/software/defi-builder-ai) · hackathon [[Block Magic- A Chainlink Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** amazon-web-services, chainlink, docker, fastapi, figma, foundry, langchain, mongodb, next, openai, prisma, python, react, tailwind

## How they structured the write-up

- overview 📝
- what it does 🤔
- contract addresses 📑
- components 🧩
- process flow 🌊
- future of defi builder 🔮

## Body

Overview 📝 DeFi builder leverages Chainlink and Avalanche technologies to create an automated and decentralized smart contract auditing and deployment platform, with the potential to turn into a tool able to offer easy deployment of smart contracts and DeFi Applications for developers. What it Does 🤔 DeFi Builder integrates various technologies and services to ensure a seamless and efficient process for easy smart contract imports through github repos, auditing smart contracts through artifical intelligence, reviewing audits with security experts, managing vulnerabilities, and deploying contracts. The platform also leverages gamification in its features, incentivising developers to audit code, and security experts to review it. The project is structured into three folders each containing its parts: /auditor contains code for the AI Agent backend written in python. For more information on Auditor architecture, and how to run it, please visit AUDITOR.md . /contracts contains the contracts used in the project, i.e. the AuditRegistry which interacts with Chainlink Price Feed and AI Agent API through Chainlink Functions, and the AuditorsVault which is responsible for uploading embeddings for the AI Agent and return an uniqueness score of the finding. /app is a Next.js project that contains client-facing code and backend that glues together the calls to AI Agent so they are prepared for the Chainlink Function. Contract Addresses 📑 WrappedNative at 0x3e770515D6Ed2197817dF6eeB26853df4E739080 AuditorsVault at 0xbFcfaad9a78C0a05cf2ad7D43273DEDd35C4eB75 AuditRegistry at 0x2a5252c7EC0261fe5480d0B83A562540A8C34d27 All contracts are verified. Components 🧩 Developer : Registers with GitHub and selects the smart contracts to be audited. User : Deploys the contract on the desired blockchain. Auditor : Submits findings and reports vulnerabilities. Chainlink Functions : Used for various decentralized operations, such as requesting audits, uploading auditor feedback and calculating rewards. Avalanche Network : Utilized for storing audit records and managing tokens via ERC721 and ERC4626 standards. AI Auditor Agent (AWS EC2) : Performs the auditing by calling an inference API. Vulnerabilities Database (MongoDB Vector Search) : Stores embeddings and provides a uniqueness score for vulnerabilities. Process Flow 🌊 Registration and Selection : Developers register with GitHub and select the smart contracts to audit through the App (Audit Section). Audit Request : The audit request is sent along with a generation fee or bug bounty. The App sends a function request via Chainlink to the AI Auditor Agent hosted on AWS EC2. AI Auditing : The AI Auditor Agent processes the request by calling the inference API. The context and findings are uploaded to the Vulnerabilities Database, which returns a uniqueness score. Backend Processing : The App Backend receives the findings and stores them. A callback Chainlink function returns the URI for the audit report. Price Conversion and NFT Minting : Chainlink AVAX/USD Price Feed fetches the price and converts the fee to the native gas token. Another Chainlink function mints an NFT (ERC721) with the token metadata on Avalanche. Audit Registry and Vault : The audit details are stored in the Audit ERC721 Registry on Avalanche. The Auditors ERC4626 Vault on Avalanche handles the rewards and fee distribution. Deployment and Compilation : Users deploy the contract on their desired blockchain. The App (Deploy Section) communicates with the Compiler Service (AWS Lambda) to compile the contract and return artifacts. Reporting and Minting Shares : Auditors submit findings and report vulnerabilities through the App (Audit Section). A Chainlink callback function returns the number of shares to mint, rewarding the auditors via the ERC4626 Vault. Future of DeFi Builder 🔮 We are striving to turn DeFi Builder into the #1 spot for Web3 entrepreneurship, creating a bridge between non-tech entrepreneurs, developers and security experts, through our comprehensive tools. In order to achieve this, in the near future we are working on our first modules that will support both smart contract deployment, and frontend customization and deployment. In order to improve our Block Magic submission, post-hackathon we will focus on launching an Avalanche Subchain, that can support native gas tokens as rewards for platform users. <div