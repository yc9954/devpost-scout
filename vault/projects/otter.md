---
slug: "otter"
url: "https://devpost.com/software/otter"
title: "Otter"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 834
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Otter

> Decentralizing how humans communicate using SUI

[Devpost](https://devpost.com/software/otter) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[privacy_tech]] [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]] [[video_visual]]

**stack** css, dapp, fetch.ai, lucide, move, node.js, postgresql, radix, react, smart-contracts, sui, supabase, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for otter

## Body

Inspiration The Web3 ecosystem is powerful but fragmented. Traders use one platform, communities gather on another (like Discord or Telegram), and blockchain insights require a third tool. We were inspired to create a single, comprehensive platform that unifies these critical functions. Our goal was to build a "super-app" on the Sui blockchain where users can trade, communicate securely, govern communities, and gain AI-powered insights, all in one place. What it does Otter is a comprehensive decentralized platform on Sui that combines intelligent trading, community building, and AI insights. Copy Trading : Allows users to follow and automatically replicate the trading strategies of expert traders with customizable risk settings. Community DAOs : Enables the creation and management of token-gated communities (DAOs) with built-in governance and member management. AI Agents : Integrates Fetch.ai and Google GenAI, allowing users to query in natural language for trading insights, community recommendations, and real-time blockchain guidance. Secure Messaging : Features end-to-end encrypted messaging for private communication between users and within communities, built on the Sui Messaging protocol. Real-Time Activity Stream : A live feed of on-chain activities, including swaps, NFT mints, transfers, and smart contract calls, allowing users to monitor the pulse of the network. How we built it We built Otter using a modern, comprehensive tech stack to handle the demands of a real-time, decentralized application. Blockchain: We used the Sui blockchain , leveraging the Sui SDK , Sui dApp Kit for wallet connections, and native protocols like Sui Messaging and Sui Walrus (decentralized storage). Our smart contracts for copy trading and DAOs are written in Move . Frontend: A responsive UI built with React 18 and TypeScript , styled with Tailwind CSS , and routed with React Router . AI & Data: We integrated Fetch.ai for autonomous AI agents and Google GenAI for LLM-powered chat. React Query was crucial for managing server state and caching blockchain data. Backend & Database: A Node.js/Express.js API server handles off-chain logic, with Supabase (PostgreSQL) used for user profiles, community metadata, and data aggregation. Challenges we ran into Real-time Data: Building the activity stream was a major challenge. We had to implement efficient polling ( useTransactionPolling ) and data aggregation to provide a live feed of on-chain transactions without overwhelming the frontend or our API. Complex State Management: Juggling blockchain state (wallet connections, contract data), server state (Supabase data), and local UI state was complex. React Query was essential in managing this. ZKLogin & Sponsored Transaction: Trying to use Enoki for ZKlogin and to sponsor transactions on our app for a seamless user experience had a larger learning curve than expected especially when dealing with oauth providers like Google and .build functions. Secure Messaging: Implementing end-to-end encryption with session key management using the new Sui Messaging protocol required a deep dive into its documentation to ensure a secure, seamless user experience. Document transfer on chain: Utilizing Walrus to employ file uploads such as images, videos, and other documents with the messaging SDK was rather difficult and required understanding of the Walrus docs. Accomplishments that we're proud of A Unified Platform: We are incredibly proud of successfully integrating five distinct, complex features (copy trading, DAOs, AI chat, messaging, and a real-time stream) into a single, cohesive application. The AI Agent: The Otter AI Chat, powered by Fetch.ai and Google GenAI, is a standout feature. It can understand natural language queries and provide genuinely helpful trading strategies and ecosystem guidance. On-Chain + Off-Chain Synergy: We created a robust architecture that skillfully balances on-chain smart contracts (for trust-minimized trading and governance) with an efficient off-chain backend (for data aggregation and user experience), all powered by Supabase. Polished UX: Despite the underlying complexity, we delivered a clean, responsive, and accessible UI with features like dark mode and a mobile-first design, thanks to Tailwind and Radix UI. What we learned Deep Dive into Sui: This project was a massive learning experience in the Sui ecosystem. We gained deep, hands-on expertise with the Sui SDK, the dApp Kit, and especially the newer protocols like Sui Messaging and Walrus. Practical AI Application: We learned how to move beyond simple AI chat prompts and integrate LLMs (Google GenAI) and autonomous agents (Fetch.ai) to perform complex, data-driven tasks related to blockchain activity. Real-Time Data Architectures: We learned the challenges and best practices for handling real-time data feeds from a blockchain, using a combination of smart contract events, API polling, and frontend state management with React Query. What's next for Otter Mainnet Deployment: Our immediate next step is to complete audits on our smart contracts and deploy Otter to the Sui mainnet. Expanded AI Capabilities: We plan to enhance our AI agents to allow for autonomous actions, such as executing trades based on user-defined strategies or providing proactive alerts. Mobile App: To truly be a "super-app," we aim to develop native mobile applications for iOS and Android. Advanced DAO Tooling: We want to add more sophisticated governance modules, such as treasury management and integration with other DeFi protocols, for our community DAOs. <div