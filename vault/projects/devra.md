---
slug: "devra"
url: "https://devpost.com/software/devra"
title: "Devra"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 846
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/developer"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Devra

> Devra is a decentralized marketplace that lets data owners securely encrypt, verify (AI), mint, and sell high-quality datasets as NFTs, buyers purchase access on-chain powered by Polkadot's Asset Hub.

[Devpost](https://devpost.com/software/devra) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]]
**user** [[developer]] [[researcher]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[structured_db]]

**stack** fastapi, metamask, nest.js, next.js, polkadot, python, react.js, solidity, tailwindcss, talisman, torchvision, transformers, typescript, vercel

## How they structured the write-up

- devra - decentralized data marketplace
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for devra

## Body

Logo Homepage Devra - Decentralized Data Marketplace Inspiration The inspiration for Devra came from witnessing the challenges faced by AI researchers and data scientists in accessing quality datasets. Traditional data marketplaces are plagued with issues, centralized control, lack of transparency, questionable data provenance, and unfair compensation for data providers. We asked ourselves: What if we could create a trustless marketplace where data ownership is verifiable, quality is AI-verified, and transactions are transparent? The rise of blockchain technology and the growing demand for ethical AI solutions converged into a single vision: democratize data trading while ensuring quality and authenticity using Polkadot. What it does Devra is a decentralized data marketplace built on Polkadot's Westend Asset Hub testnet that revolutionizes how datasets are bought, sold, and verified. Here's what makes it special: NFT-Based Ownership : Every dataset is minted as an NFT, providing immutable proof of ownership and provenance AI Verification : Our AI agent analyzes datasets for quality, completeness, and authenticity before they hit the marketplace Encrypted Storage : Datasets are encrypted and stored on IPFS via crust network, ensuring decentralization and security Smart Contract Trading : Trustless peer-to-peer transactions powered by Polkadot's Solidity smart contracts Dynamic Pricing : Sellers can list, update prices, or cancel listings—all on-chain Beautiful UX : A sleek, cyberpunk-inspired interface that makes blockchain feel accessible The workflow is simple yet powerful: Upload → Seller uploads dataset and metadata Verify → AI agent validates data quality and authenticity Mint → Dataset becomes an NFT with encrypted IPFS storage List → Seller sets price and lists on marketplace Buy → Buyers purchase with WND tokens Access → Smart contract handles decryption and delivery How we built it Building Devra was a full-stack blockchain adventure that pushed us to master multiple technologies: Frontend (Next.js 15 + React 19) Modern React with Server Components and App Router Framer Motion for smooth, eye-catching animations Tailwind CSS v4 for rapid, responsive styling Wagmi v2 + Viem for Ethereum wallet integration Custom hooks for contract interactions (mint, list, buy, cancel) Smart Contracts (Solidity) ERC-721 NFT standard for dataset ownership Integrated marketplace logic within the NFT contract Events for tracking listings, sales, and cancellations Secure price handling using OpenZeppelin libraries Blockchain Integration Deployed on Westend Asset Hub (Polkadot's EVM-compatible testnet) Used Remix IDE for contract development and testing MetaMask and Talisman wallet support Transaction tracking via Blockscout explorer AI Verification Pipeline Python-based AI agent for dataset analysis Checks for data quality metrics: ( Q = \frac{\text{valid_rows}}{\text{total_rows}} \times 100 ) Authenticity scoring using statistical analysis Integration with backend API for verification results Decentralized Storage IPFS via Crust for storing encrypted datasets Server-side encryption before upload Decryption keys managed by Custom backend Gateway fallbacks for reliable access Architecture ┌─────────────┐ │ Frontend │ (Next.js + Wagmi) └──────┬──────┘ │ ┌──────▼──────────────────────┐ │ Smart Contract (Solidity) │ │ - Mint NFT │ │ - List/Delist Dataset │ │ - Buy/Transfer │ └──────┬──────────────────────┘ │ ┌──────▼──────┐ ┌─────────┐ │ IPFS │◄────┤ AI Agent│ │ (Encrypted) │ │ Verify │ └─────────────┘ └─────────┘ Challenges we ran into We ran into a lot of challenges this where the few significant challenges we faced: Custom Wallet Connector for Talisman Wagmi doesn't have built-in Talisman support, so we had to create a custom connector: const getTalismanProvider = () => { if (typeof window === "undefined") return undefined; return (window as WindowWithTalisman).talisman?.ethereum; }; This required careful TypeScript typing and handling SSR edge cases. Contract Interaction Edge Cases Gas estimation failures when users had insufficient WND Race conditions when listing/buying simultaneously Stale data after transactions completed Deploying to Westend Asset Hub testnet using Remix polkadot IDE Accomplishments that we're proud of What we learned This project was a crash course in modern blockchain development: Technical Skills Smart Contract Security: Learned about reentrancy guards, access control, and safe math EVM Compatibility: Polkadot's Asset Hub runs a full EVM, making Solidity deployment seamless React 19 Patterns: Server Components, async components, and streaming Web3 UX: How to make blockchain interactions feel native and intuitive TypeScript Mastery: Strict typing for contracts, proper error handling, generic hooks Blockchain Concepts Gas Optimization: Every operation costs money, we optimized storage layout and function calls Event-Driven Architecture: Using contract events to update UI state Tokenomics: Designing pricing mechanisms and marketplace fees (even if we set them to 0%) Wallet Integration: Supporting multiple providers (MetaMask, Talisman) Soft Skills Problem Decomposition: Breaking down "build a data marketplace" into manageable chunks Debugging Persistence: Spent hours tracking down hydration bugs and build failures Documentation Reading: Learned to navigate Wagmi, Viem, Polkadot, and OpenZeppelin docs User Empathy: Realized blockchain UX needs to hide complexity, not flaunt it What's next for Devra Having established a strong foundation, our next steps will focus on deeper integration and optimization within the Polkadot ecosystem. Integrate Native Precompiles : Leveraging Polkadot's utility pallet for features like batchAll Optimize Marketplace : Making transactions even more secure and efficient for users and developers. Expand Ecosystem : Further empowering developers and data providers within the Polkadot network. Built with ❤️ by the Devra team Making data trading fair, transparent, and decentralized, one NFT at a time. <div