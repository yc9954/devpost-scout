---
slug: "shard-2kvsch"
url: "https://devpost.com/software/shard-2kvsch"
title: "Shard"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 1483
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/on_device_local"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/accessibility"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Shard

> Do you have a laptop? You're potentially losing on making at least $10/day side income with Shard. Introducing Shard to make use of unutilized resources from 1.5 billion devices globally.

[Devpost](https://devpost.com/software/shard-2kvsch) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[benchmark_measured]] [[on_device_local]] [[privacy_tech]] [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[accessibility]] [[climate_energy]] [[developer_tools]] [[finance_payments]] [[labor_employment]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** swift, typescript

## How they structured the write-up

- for job submitters (via web interface)
- for computing providers (via macos app)
- key features
- tech stack
- development highlights
- blockchain & cryptography
- native macos development
- distributed systems design
- full-stack integration
- performance optimization
- short-term (next 3 months)
- long-term vision
- technical improvements

## Body

🌟 Inspiration The inspiration for Shard came from observing two key problems in the modern computing landscape: Wasted Computing Power : Millions of high-performance Macs sit idle for hours each day, their powerful Apple Silicon chips underutilized while consuming electricity. Centralized AI Infrastructure : Running AI inference and compute-intensive tasks typically requires expensive cloud infrastructure or centralized services, creating bottlenecks and single points of failure. I asked myself: What if I could create a decentralized marketplace where anyone could contribute their idle computing power and earn cryptocurrency, while others could access distributed compute resources at a fraction of traditional cloud costs? The name "Shard" reflects the core innovation—breaking large computational jobs into tiny micro-task fragments that can be processed independently across a distributed network, similar to how blockchain shards distribute data and computation. 🛠️ What It Does Shard is a decentralized compute network built on the Sui blockchain that transforms idle Mac computers into a distributed supercomputer. Here's how it works: For Job Submitters (via Web Interface) Submit Computational Tasks : Upload a CSV file with 100 sentences for AI content moderation or provide parameters for Monte Carlo simulations Automatic Fragmentation : The system breaks your job into tiny independent fragments (1 sentence per fragment) Privacy-First Encryption : Each fragment is encrypted using Sui Seal threshold encryption Decentralized Storage : Encrypted data is stored on Sui Walrus (decentralized blob storage) On-Chain Job Posting : The job and all fragments are published to the Sui blockchain with USDC bounties (0.01 USDC per fragment) Real-Time Progress : Watch as workers around the world claim and process your fragments Automatic Result Aggregation : Get your completed results delivered in the original order For Computing Providers (via macOS App) Beautiful System Monitor : Track CPU, GPU, and memory usage in a Robinhood-like interface One-Click Worker : Click "Start Worker" to begin earning USDC AI-Powered Chat : Built-in Gemma 3-4B chatbot for local AI assistance Auto-Discovery : The app polls the blockchain for available work Secure Processing : Downloads encrypted fragments, decrypts locally using Seal Local AI Inference : Runs Gemma AI model to classify content (safe/unsafe) Upload Results : Encrypts and uploads results to Walrus, submits completion on-chain Instant Payment : Receives 0.01 USDC per completed fragment (sponsored transaction—zero gas fees) Multi-Worker Support : Spawn multiple worker windows to process tasks in parallel Key Features Zero Gas Fees for Workers : All transactions are sponsored by job creators Privacy-Preserving : Workers never see raw sensitive data—only encrypted fragments Fault-Tolerant : Uncompleted fragments are automatically re-queued Native Performance : Leverages Apple Silicon's Metal acceleration for AI inference Real-Time Transparency : Both submitters and workers see live progress updates 🏗️ How I Built It I built Shard solo over 15 hours during the hackathon, integrating cutting-edge blockchain technologies with native macOS development. Tech Stack Frontend (Next.js 14 + React + TypeScript) UI Framework : shadcn/ui components with Tailwind CSS for a minimalist, dark-mode-first design Animations : Framer Motion for smooth transitions and progress indicators Real-Time Updates : Polling-based live fragment status tracking Features : Job submission portal, AI inference configuration, Monte Carlo simulation setup Backend (Node.js + Express + TypeScript) API Server : RESTful endpoints for job management, fragment lifecycle, and wallet queries Sui Integration : @mysten/sui SDK for blockchain interactions and USDC transfers Walrus Client : Custom implementation for uploading/downloading encrypted blobs Seal Encryption : @mysten/seal SDK for threshold encryption with session keys Job Orchestration : Automatic fragmentation, encryption, and on-chain publishing macOS App (SwiftUI + Combine) System Monitoring : Real-time CPU/GPU/Memory tracking using IOKit and Mach APIs AI Integration : Embedded llama.cpp server running Gemma 3-4B-it-q4_0.gguf model Metal Acceleration : Native Apple Silicon GPU support for AI inference Worker Engine : Multi-threaded fragment discovery, claiming, processing, and completion Multi-Window Architecture : Spawn independent worker windows for parallel processing Live Dashboard : Beautiful glassmorphic UI with animated charts (inspired by Apple's design language) Blockchain (Sui + Move) Sui Network : Testnet deployment for job and fragment state management Smart Contracts : Move modules for access control policies (Seal) Walrus Storage : Decentralized blob storage with erasure coding Seal Encryption : Threshold encryption with programmable access control Sponsored Transactions : Job creators pay all gas fees for workers Development Highlights 1. Micro-Task Fragment Protocol I designed a novel fragmentation system where each sentence becomes an independent TaskFragment with: Unique fragment ID and job ID Encrypted data blob stored on Walrus USDC bounty (0.01 per fragment) Status lifecycle: pending → claimed → completed 2. Sui Seal Integration I implemented end-to-end encryption using Seal's threshold encryption: Generated session keys with TTL for time-limited access Created Move access policy contracts ( seal_approve ) Encrypted fragments using AES256GCM Workers decrypt using session keys without exposing raw data 3. llama.cpp Embedding I bundled the Gemma AI model and llama-server binary directly into the macOS app: Built static llama-server to avoid dynamic library issues Spawned server as subprocess with Metal GPU acceleration Implemented streaming HTTP client for real-time inference Created beautiful chat UI with gradient avatars and suggestion chips 4. Multi-Worker Architecture I built a sophisticated worker management system: @Environment(\.openWindow) for spawning new worker windows Shared WorkerService instances with independent worker IDs Competitive claiming (first worker to claim gets the fragment) Real-time USDC balance tracking across all workers 5. Production Deployment Frontend : Deployed to Vercel ( https://shard-alpha.vercel.app ) Backend : Deployed to Vercel with Cloudflare Tunnel for local testing CORS : Dynamic subdomain support for *.trycloudflare.com Config Management : Centralized API URLs for easy environment switching 🎓 What I Learned Blockchain & Cryptography Sui Blockchain : I dove deep into the Sui ecosystem, learning about Move smart contracts, sponsored transactions, and how to structure on-chain state for a compute marketplace. Sui Walrus : I implemented decentralized storage for both job inputs and results, learning how erasure coding provides redundancy without centralized servers. Sui Seal : I mastered threshold encryption and programmable access control, enabling workers to decrypt job data without ever exposing it to centralized parties. BCS Encoding : I learned about Sui's Binary Canonical Serialization for efficient data encoding. Native macOS Development I built a production-grade SwiftUI application with real-time system monitoring (CPU, GPU, Memory). I integrated llama.cpp and Gemma 3-4B for local AI inference using Apple Silicon's Metal acceleration. I learned advanced Swift concepts: Combine framework, @Published properties, URLSession streaming, and multi-window architecture. I mastered IOKit for low-level hardware metrics and Mach APIs for system-level monitoring. Distributed Systems Design I implemented a micro-task fragment protocol where jobs are broken into independent units that can be processed in parallel. I designed fault-tolerant execution with fragment re-queuing if workers go offline. I built a polling-based worker discovery system that scales to multiple simultaneous workers. I learned about eventual consistency and how to handle race conditions in distributed claiming. Full-Stack Integration I connected React/Next.js frontend → Express.js backend → Sui blockchain → macOS worker app in a seamless end-to-end flow. I implemented real-time progress tracking with polling-based live fragment status updates. I managed CORS, API design, environment configuration, and production deployment. I debugged complex multi-component issues (e.g., USDC transfers, fragment completion, UI state synchronization). Performance Optimization I optimized SwiftUI rendering by removing continuous animations and using .drawingGroup() for Metal acceleration. I reduced CPU usage from 50% to <5% by simplifying chart rendering and using efficient update intervals. I implemented smart batching for blockchain queries to minimize network overhead. 🚀 What's Next for Shard Short-Term (Next 3 Months) Mainnet Launch : Deploy to Sui mainnet with real USDC incentives More Task Types : Support image processing, video transcoding, and scientific simulations Advanced Reputation System : Track worker reliability and completion rates with on-chain NFTs Mobile Support : Build iOS/Android worker apps to expand the provider network Job Verification : Implement cryptographic proofs of correct computation Long-Term Vision Cross-Chain Support : Integrate with Ethereum, Solana, and other L1s for broader adoption Specialized Hardware : Support GPU-intensive tasks (3D rendering, AI training) with CUDA/ROCm Enterprise Partnerships : Offer B2B solutions for companies needing distributed compute DAO Governance : Community-driven protocol upgrades and fee structures Carbon Credits : Reward providers for using renewable energy sources Technical Improvements WebSocket Real-Time Updates : Replace polling with push notifications for instant updates Smart Contract Upgrades : On-chain fragment verification and slashing for malicious workers Result Validation : Implement consensus mechanisms (multiple workers verify the same fragment) Benchmarking System : Automatically test worker capabilities and assign appropriate tasks Dynamic Pricing : Market-driven bounty pricing based on task complexity and demand 🎯 Conclusion Shard demonstrates that it's possible to build a fully functional decentralized compute network in a single weekend. By leveraging Sui's innovative blockchain architecture, Walrus's decentralized storage, and Seal's privacy-preserving encryption, I created a platform that turns idle Macs into a global supercomputer—while ensuring privacy, fault tolerance, and instant micropayments. This is just the beginning. The future of computing is decentralized, and Shard is proof that we can build it today. <div