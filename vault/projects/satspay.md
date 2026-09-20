---
slug: "satspay"
url: "https://devpost.com/software/satspay"
title: "SatsPay"
hackathon: "Bitcoin 2025 Official Hackathon"
organization: "Bitcoin++"
winner: true
words: 406
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/small_business"
---

# SatsPay

> SatsPay is a Bitcoin-powered Buy Now, Pay Later platform that lets users unlock the spending power of their sBTC without selling it by borrowing USD against locked sBTC.

[Devpost](https://devpost.com/software/satspay) · hackathon [[Bitcoin 2025 Official Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[small_business]]

**stack** clarity, hiro, nextjs, stacks

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for satspay

## Body

Logo Inspiration We were inspired by the financial principle of not selling appreciating assets to cover short-term needs. In the fiat world, people borrow against real estate or stocks — so why shouldn’t Bitcoiners be able to do the same? We realized there’s a huge gap in the current Web3 ecosystem: no truly intuitive BNPL platform built around non-custodial Bitcoin-backed lending. SatsPay bridges that gap. What it does SatsPay is a modern Buy Now, Pay Later platform powered by Bitcoin. Users can shop online and use their sBTC as collateral to make purchases — without selling it. The platform approves purchases instantly, locks the necessary collateral, and sets a flexible repayment schedule. Merchants get paid upfront, users keep their BTC exposure, and repayments are handled seamlessly through smart contracts. How we built it Frontend: Built with Next.js and Tailwind CSS for a clean, responsive UI across web and mobile. Smart Contracts: Developed using Clarity, deployed on Stacks testnet. BTC Collateral: Leveraged sBTC as the core mechanism to lock Bitcoin as collateral while enabling seamless contract interactions. Wallet Integration: Integrated with Stacks Connect (Testnet). BNPL Logic: Implemented time-based repayment tracking, liquidation logic for overdue loans, and interest-rate calculation using oracles. Challenges we ran into Smart contracts on Bitcoin: Building on Bitcoin with smart contract capabilities was new territory. Tools like Hiro documentation and LearnWeb3 helped. sBTC Collateralization: Designing a trustless and transparent collateralization model was non-trivial, especially to prevent under-collateralization. UX complexity: Balancing technical complexity with a user-friendly design — especially on mobile — was a constant challenge. Accomplishments that we're proud of Built a prototype of a Bitcoin-native BNPL app. -Designed a slick, intuitive interface users loved testing. Integrated non-custodial wallet flows with real-time sBTC lockups and repayment logic. Bridged the user experience gap between DeFi and real-world shopping. What we learned Bitcoin L2s are the future. Designing for real-world use cases forces better architecture and UX decisions. Non-custodial financial products can be just as seamless as traditional fintech — with the right abstraction layers. Building in Web3 is 20% coding, 80% debugging weird behavior in wallets, SDKs, and node interactions. What's next for SatsPay Launch a closed beta with curated merchants to test out real-world usage. Integrate dynamic credit scoring based on wallet history and reputation. Add support for other Bitcoin L2s and more collateral types. Explore partnerships with on-chain retail aggregators and NFT marketplaces. Secure audit and pursue regulatory compliance for broader adoption. <div