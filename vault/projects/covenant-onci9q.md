---
slug: "covenant-onci9q"
url: "https://devpost.com/software/covenant-onci9q"
title: "Covenant"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 590
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "user/legal_professional"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Covenant

> Put your money where your goals are. Complete your commitments to earn it back, or watch it go to a cause you really don’t want to fund. Blockchain-verified accountability, powered by AI.

[Devpost](https://devpost.com/software/covenant-onci9q) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[developer_tools]]
**user** [[legal_professional]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[video_visual]]

**stack** blockchain, ethereum, next.js, reka

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for covenant

## Body

Inspiration We noticed that staying accountable to personal goals is hard. Reminders, to-do lists, and habit apps all rely on self-discipline alone. But people behave differently when real stakes are involved. We wanted to build a system that combines motivation through commitment with the transparency and fairness of blockchain. The result is Covenant: a decentralized way to make promises you’ll actually keep. What it does Covenant lets users create commitments to complete a goal by a deadline, with real money on the line. You lock funds in an Ethereum smart contract. You set a beneficiary wallet, a friend, charity, or even an “anti-charity,” to receive the stake if you fail. When you complete your task, you upload a verification video. The video is analyzed by Reka’s multimodal Video Q&A API, which checks for presence of the required actions, and your face. If the model verifies success, the smart contract releases your stake back to you. Otherwise, the funds go to the beneficiary. It’s accountability made autonomous. No judges, no excuses, just code and proof. How we built it Frontend: Next.js web app for covenant creation, wallet connection, and video upload. Blockchain: Solidity smart contracts deployed on Ethereum testnet using Hardhat. Verification backend: Next.js API routes that upload videos to Reka’s video indexing endpoint and call its Video Q&A API for commitment verification. Integration: WalletConnect + Wagmi for on-chain interactions, and secure server-side Reka API calls for video processing. Challenges we ran into Multi-stage video uploads: We had to design a pipeline that passed each uploaded video from the frontend, through a Next.js API route, to Reka’s upload endpoint using FormData, ensuring the file persisted correctly across each layer. Smart contract integration: Getting our Solidity contracts to deploy and communicate smoothly with the frontend required debugging ABI mismatches and transaction confirmation issues. Syncing AI verification with on-chain logic: Coordinating Reka’s verification responses with blockchain state changes demanded careful timing and error handling. Merging separate components: Integrating independently built blockchain, AI, and frontend modules into a unified app took close coordination and a lot of testing. Accomplishments that we're proud of Built a working end-to-end system that connects AI-based proof-of-work with Ethereum smart contracts in under 48 hours. Successfully verified real videos through Reka Video Q&A and used that verification to trigger blockchain contract actions. Created a user experience that feels fun and motivating while demonstrating real Web3 accountability infrastructure. What we learned How to combine AI verification with on-chain logic to create meaningful, human-centered dApps. The nuances of multipart uploads and serverless video handling in Next.js. Practical experience using Reka’s multimodal models beyond standard text or image tasks. That incentives, both social and financial, can make technology a powerful force for personal growth. What's next for Covenant Refining AI verification: Improve fairness and accuracy by fine-tuning prompts, using multimodal reasoning (video + audio + text), and introducing confidence thresholds before funds are released. Social accountability layer: Add friends, group challenges, and public covenant feeds to create social pressure and community-driven motivation. Mobile app: Build a lightweight mobile app for recording and uploading verification videos directly from your phone, streamlining the entire covenant flow. Gamification: Add progress tracking, streaks, and rewards for consistent goal completion to make accountability fun. Expanded blockchain support: Deploy on faster, cheaper chains like Base or Polygon, and integrate stablecoins for easier on-ramping. Covenant marketplace: Let users browse and sponsor other people’s covenants, turning accountability into a social investment ecosystem. Privacy-preserving verification: Explore zero-knowledge proof methods so users can prove goal completion without revealing sensitive video details. <div