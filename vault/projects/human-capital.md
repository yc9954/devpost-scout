---
slug: "human-capital"
url: "https://devpost.com/software/human-capital"
title: "Human Capital"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 847
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Human Capital

> Time is money: literally. Sell your day away in 15-minute blocks. Highest bidder controls you, watches you, directs you. Blockchain auctions meet dystopian labor. Your time. Their terms.

[Devpost](https://devpost.com/software/human-capital) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]]
**substrate** [[code_repository]] [[structured_db]] [[video_visual]]

**stack** ai, chromadb, claude, livekit, next.js, sui

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for human capital

## Body

logo Inspiration "Time is money" is something we hear constantly—but what if we took it literally? We wanted to create a Black Mirror-style commentary on the gig economy, surveillance capitalism, and the commodification of human labor. The inspiration came from thinking: if your time really is money, shouldn't there be a marketplace for it? The result is intentionally dystopian, a parody that makes you uncomfortable while showcasing what's technically possible when you combine blockchain, real-time streaming, and AI surveillance. What it does Human Capital is a platform where you sell your time in 15-minute chunks via blockchain auction: Users broadcast themselves live and put their time up for auction Bidders place bids on time slots using Sui blockchain NFT auctions Winners gain complete control of the user's body for 15 minutes: Send commands via chat that appear as overlay instructions Watch via LiveKit real-time stream Direct the user to do whatever they want AI monitors everything - a vision-language model captures frames, analyzes compliance, and stores summaries Search your history - semantic search lets anyone query past activities ("Are they good at coding?" "Did they complete tasks?") It's surveillance capitalism meets gig economy meets blockchain, turned up to 11. How we built it Frontend: Next.js 16 + React 19 + TypeScript + Tailwind CSS v4 Real-time Infrastructure: LiveKit for low-latency video streaming and bidirectional communication Custom room architecture with hidden bot participants for AI monitoring Blockchain: Sui Network with custom Move smart contracts for time slot NFT auctions @mysten/dapp-kit for wallet integration On-chain bid validation and winner selection Fully decentralized, trustless architecture AI Pipeline: OpenAI GPT-4o (via OpenRouter) for real-time vision analysis Anthropic Claude for natural language processing and historical analysis ChromaDB Cloud vector database for storing activity summaries OpenAI embeddings (text-embedding-3-small) for semantic search Multi-stage processing: frame capture → batch summaries → chunk summaries → vector storage Off-chain oracle implementation for compliance scoring Data Flow: VLM bot joins stream → captures frames every 5s → analyzes with GPT-4o → batches summaries → stores in ChromaDB → enables natural language search of user history This is a data-intensive application —the system processed 7.52 GB/s of bandwidth at peak time during testing. Challenges we ran into Decentralization vs. AI control - Our biggest challenge was maintaining true decentralization. Initially, we wanted to put funds in escrow controlled by an AI oracle on-chain, but we realized that put too much power into the hands of the AI oracle and, more importantly, the people who controlled it. We decided to build a fully decentralized, entirely trustless system by moving the oracle off-chain and implementing it as more of a credit score mechanism. VLM frame capture at scale - Processing hundreds of frames per hour with GPT-4o vision was expensive and required careful batching strategies to stay within token limits LiveKit bot architecture - Getting a headless bot participant to join rooms, capture video frames reliably, and stay hidden from the UI took significant debugging Sui Move smart contracts - Learning Move's ownership model and implementing auction logic with proper time-based finalization was complex Real-time state synchronization - Keeping blockchain auction state, LiveKit room state, and UI state in sync across multiple users required careful React Query caching Semantic search quality - Tuning the ChromaDB collection and prompt engineering to return actually useful historical insights took iteration Accomplishments that we're proud of Fully trustless, decentralized architecture - no central authority controls funds or outcomes It actually works end-to-end - blockchain auctions → live streaming → AI surveillance → searchable history Multi-stage VLM pipeline that intelligently batches and summarizes to manage API costs Custom Sui Move contracts deployed and functioning on testnet Semantic search that genuinely understands natural language queries about user history Real-time winner control with command overlays and task compliance tracking The aesthetic - we committed fully to the dystopian bit and the UI reflects it Scale testing - we actually ran this for 6 hours and processed real production data What we learned Decentralization has real trade-offs - putting AI oracles on-chain creates centralization risks we hadn't initially considered Vision-language models are powerful but expensive - real-time video analysis at scale requires careful architecture Sui's Move language has a steep learning curve but elegant ownership semantics LiveKit is incredibly robust for real-time streaming when properly configured Vector databases like ChromaDB make semantic search surprisingly easy once you get embeddings right Hackathon projects can be satire AND technically impressive - the parody angle made it more interesting to build Data-intensive applications hit different - 7.52 GB/s hours taught us to respect bandwidth costs What's next for Human Capital Compliance scoring - aggregate AI analysis into reputation scores for users Task marketplace - let bidders post tasks in advance with bounties Multi-user mode - control multiple people simultaneously Mobile app - stream your human capital on the go Analytics dashboard - charts and graphs of your commodification Mainnet deployment - take this dystopia to production (kidding... mostly) Privacy mode - blur faces/sensitive info while maintaining surveillance (ironic, we know) Refined oracle mechanisms - explore hybrid on-chain/off-chain solutions for compliance verification <div