---
slug: "futureproof-pes1vn"
url: "https://devpost.com/software/futureproof-pes1vn"
title: "Sovseal(Lockdrop)"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 699
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
---

# Sovseal(Lockdrop)

> Zero-knowledge state permanence for humans, and local-first vector memory (MCP) for AI agents.

[Devpost](https://devpost.com/software/futureproof-pes1vn) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]] [[structural_withholding]]
**domain** [[developer_tools]]
  <sub>weak: agriculture_food, civic_government, legal_justice</sub>
**user** [[developer]]
**substrate** [[structured_db]]

**stack** ether-js, foundry, ipfs, lancedb, local-llm, metamask, model-context-protocol, next-js, pallet-revive, passet-hub, polkadot, react, solidity, sqlite

## How they structured the write-up

- what it does
- how we built it

## Body

Inspiration Imagine recording a message for your child to receive on their 18th birthday. Or leaving final words for loved ones. Or preserving family stories for future generations. These are the most intimate, precious moments of our lives. Now imagine that message being: Sold to AI training companies without your consent Analyzed by algorithms to build psychological profiles Accessed by corporations for targeted advertising Seized by governments through legal orders Lost forever when the company shuts down This is the reality of centralized digital storage in the age of AI. We're living through a gold rush where our most personal data - our voices, our faces, our stories - is being harvested to train AI models worth billions. Companies promise privacy, but their terms of service tell a different story. Your "private" messages become training data. Your memories become commodities. I asked myself: What if we could send messages to the future where even I, the developer, cannot access them? Where no company can sell them? Where no AI can train on them? This question led me down a rabbit hole of cryptography, blockchain consensus, and decentralized storage. The answer became Lockdrop. ⚡ The Next Chapter: Agentic State Continuity (MCP) During our final integration phases, we realized a profound truth: AI agents suffer from the exact same fragility and privacy violations as humans. Currently, developers building AI agents are forced to send highly sensitive agent memory and user context to centralized cloud vector databases (like Zep or Mem0). This introduces massive 500ms+ latency and exposes highly confidential user data to third parties. We decided to solve this. We took our battle-tested cryptographic infrastructure and expanded it. Sovseal is now the ultimate Agentic State Continuity Infrastructure. We built and shipped a Zero-Knowledge, Local-First MCP (Model Context Protocol) Server that lets AI agents remember everything entirely on your own machine. The Math is Simple: Want to decrypt early? Break AES-256 encryption (computationally impossible - would take 3.67 × 10^51 years) Want to change the unlock time? Control 51% of Polkadot's validator stake (economically impossible) Want to keep your AI agents secure? Run our local vector server (0 cloud data leaks) The Vision is Profound: In a world where AI companies scrape everything, where privacy is a marketing term, where your data is the product - Sovseal offers something radical: true digital sovereignty . For humans, and for the AI assistants that serve them. Guaranteed by mathematics, not corporate promises. What it does Sovseal provides two distinct layers of state permanence: 1. Human Memory Layer (Lockdrop) Create time-locked audio/video messages with mathematical privacy guarantees. Record or upload a video message. Set an unlock date. Specify a recipient's wallet address. The media is encrypted entirely client-side using Web Crypto API and pushed to IPFS via Storacha Network, with metadata stored on Passet Hub. 2. AI Agent Memory Layer (Local MCP Server) A high-performance Model Context Protocol (MCP) server that gives Claude Desktop, Cursor, or your custom agents local-first semantic memory. Zero Cloud Leakage: All vector embedding math is run locally. Micro-Second Latency: Retrieves contextual memory in < 10ms using local vector lookup. Zero Server Costs: Run indefinitely on your own local hardware for $0 . How we built it Tech Stack: Frontend & App: Next.js 14 + TypeScript (strict mode) + Tailwind CSS AI Memory Server: Model Context Protocol (MCP) + LanceDB (local vector storage) + Transformers.js (on-device embeddings) Blockchain: Solidity 0.8.20 on Passet Hub testnet via pallet-revive (PolkaVM) Contract Address: 0xeD0fDD2be363590800F86ec8562Dde951654668F (Passet Hub Testnet) RPC: ethers.js v6 for Ethereum-compatible JSON-RPC Storage: Storacha Network (IPFS with email-based UCAN auth) Crypto: Web Crypto API (AES-256-GCM, RSA-OAEP) Wallets: Talisman & MetaMask via EIP-1193 Key Implementation - On-Device AI Embedding & Vector Store: // packages/mcp-server/src/local/db.ts import { connect } from '@lancedb/lancedb'; import { pipeline } from '@xenova/transformers'; export class LocalMemoryStore { private db: any; private embedder: any; async init() { this.db = await connect('~/.sovseal/db'); // Run embedding model entirely on the local machine this.embedder = await pipeline('feature-extraction', 'Xenova/all-MiniLM-L6-v2'); } async storeMemory(content: string, metadata: object) { const output = await this.embedder(content, { pooling: 'mean', normalize: true }); const vector = Array.from(output.data); const table = await this.db.openTable('agent_memories'); await table.add([{ vector, content, timestamp: Date.now(), ...metadata }]); } } <div