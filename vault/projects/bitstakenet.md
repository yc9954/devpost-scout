---
slug: "bitstakenet"
url: "https://devpost.com/software/bitstakenet"
title: "BitStakeNet"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 528
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# BitStakeNet

> BitStakeNet is a Starknet solution that enable Bitcoin users to bring their bitcoin into startknet and back. With bitcoin in their wallet, they are able to stake it so that they can claim rewards.

[Devpost](https://devpost.com/software/bitstakenet) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[revocation_withdrawal]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[financial_record]] [[geospatial]]

**stack** atomiq, cairo, cavos, nestjs, node.js, postgresql, prisma, react, starknet, typescript

## How they structured the write-up

- inspiration
- 🔧 how i built it
- 🏗️ technical stack
- 📘 what i learned
- challenges faced
- conclusion

## Body

BitStakeNet Logo BitStakeNet - A secure Bitcoin-Starknet Solution Inspiration The project was inspired by the need for secure and seamless transfer of bitcoin into Starknet and back — especially when handling sensitive operations like deposits, staking, and withdrawals. I wanted to build something that merges DeFi functionality with real-world usability , where users can manage their StarkNet or Bitcoin-based assets as easily as using a traditional banking app — but with self-custody and 2FA protection . 🔧 How I Built It The frontend is built with React + TypeScript , styled using TailwindCSS for clean and responsive UI design. The backend is built with NestJs, Prisma, Typescript, and PostgreSQL, Cavos SDK, Atomiq SDK with secure argon2 algorithm for password hashing before storage. The web3 contract is built using Cairo programming language with functions to maintain various states through storage maps Each major feature — Deposit , Stake , Unstake , Swap , and Withdraw — is modularized into independent components, all connected through a secure API layer. 💡 Key Features Deposits & Withdrawals: Handled via authenticated API calls to the backend ( /auth/deposit , /auth/vault/withdraw ), with blockchain operations executed through the Cavos API for StarkNet. Staking & Unstaking: Communicates with the backend ( /auth/vault/stake and /auth/vault/unstake ) using JWT authorization tokens. Lightning Swap: Bridges Bitcoin L1 → StarkNet L2 , displaying invoices as QR codes and polling for status updates until completion. 2FA Protection: Before executing any sensitive transaction, a TwoFAModal prompts the user to enter their TOTP code. The code is verified via /transactions/validate-2fa , and only if successful does the action proceed. Toast Notifications: Integrated with react-hot-toast for real-time feedback during all asynchronous actions. 🏗️ Technical Stack Frontend: React, TypeScript, TailwindCSS, Cavos SDK Security: JWT Auth + TOTP (2FA) Blockchain Integration: Starknet smart contract using Cairo language Lightning Payments: Invoice generation + QR display UI Enhancements: react-hot-toast , reusable modal components Backend: Node.js/Nest.js, PostgreSQL, Prisma, Cavos SDK, Atomiq SDK 📘 What I Learned How to integrate multi-step secure transaction flows with TOTP-based verification. The importance of frontend state management and graceful loading/error handling . Implementing real-time updates via polling for swap status. Structuring API layers for consistent authentication and error feedback . How to make financial dApps feel familiar , bridging Web3 UX/account abstraction with Web2 reliability. Challenges Faced 2FA Integration Flow Getting the timing right — prompting for a TOTP code before executing API calls — required restructuring logic across all transaction components. Error Handling & UX Feedback Making sure errors from both the backend and blockchain layer were properly surfaced to the user via toasts and logs. Async Transactions & Polling Managing long-running swap operations without blocking the UI was tricky. The solution involved careful use of setInterval and clearInterval references. Token and State Management Ensuring that JWT tokens were safely retrieved from localStorage and handled consistently across routes. Conclusion This project taught me the balance between user experience and security in DeFi applications. By combining 2FA protection, modular React architecture, and seamless blockchain interactions , the app achieves both trust and usability — two things that rarely coexist in Web3 platforms but has been made simpler with Starknet's native account abstraction. <div