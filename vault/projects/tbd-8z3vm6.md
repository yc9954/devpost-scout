---
slug: "tbd-8z3vm6"
url: "https://devpost.com/software/tbd-8z3vm6"
title: "ZK Bitcoin Battleship"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 881
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# ZK Bitcoin Battleship

> Bitcoin-staked Battleship on Starknet. ZK proofs for privacy, on-chain game engine for fairness. Deposit BTC, battle in real-time, winner takes all.

[Devpost](https://devpost.com/software/tbd-8z3vm6) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[structural_withholding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[financial_record]]

**stack** cairo, noir, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zk bitcoin battleship

## Body

Staking interface (WBTC approval + staking) Login screen using Cartridge Controller Login screen for Xverse wallet Transaction approval on Xverse Missed shot notification and prompt for zk proof generation Game wallet powered by Cartridge showing 1514 sats (WBTC) Successful shot notification and prompt for zk proof generation Defeat screen after losing a match Victory screen after winning a match Inspiration We wanted to build a fully on-chain version of Battleship: a game where board positions must remain hidden while hits and misses are provably fair. This is the perfect use case for zero-knowledge proofs: players can prove their shots are valid without revealing their ship placements. But we also wanted the stakes to be real. Not worthless tokens, but Bitcoin, the most trusted cryptocurrency. The challenge was to combine ZK cryptography with cross-chain composability (Bitcoin to Starknet) and real-time multiplayer gameplay, all on Layer 2. What it does ZK Bitcoin Battleship is a production-ready multiplayer Battleship game where: Players stake 1,000 sats (0.00001 BTC) in WBTC per game Winner takes all: 2,000 sats automatically distributed on-chain All game logic enforced by Starknet smart contracts, leveraging the Dojo Engine Bitcoin deposits via Xverse wallet, automatically swapped to WBTC using Atomiq protocol Real-time multiplayer with gRPC subscriptions and HTTP polling fallback Complete ZK proof implementation (Noir circuits + Garaga verifiers). Note: Due to UX constraints (proof generation taking too long), this feature was not included in the demo. Critical Privacy Feature : Board configurations are NEVER written to the blockchain, not during setup, not during gameplay, and not at the end. Only cryptographic commitments (hashes) and shot results (hit/miss) are stored on-chain. Ship positions remain private throughout the entire game. Live at: zkbattleship.fun How we built it Smart Contracts : 7 Cairo contract systems using Dojo's ECS architecture, deployed on Starknet Sepolia Frontend : React + Vite with Cartridge Controller for seamless wallet integration Zero-Knowledge Architecture : Players commit to their board via Poseidon2 hash (stored on-chain) Actual board layout stays client-side (localStorage + session recovery) Two Noir circuits (BoardCommit validates 5-ship placement, ShotResult proves hit/miss) with Garaga-generated Cairo verifiers Complete implementation with 21/21 tests passing, using mock verification for UX while proof generation takes too long for real-time gameplay When activated, defenders prove "this shot is a HIT/MISS" without revealing any other ship positions Cross-Chain : Atomiq SDK integration for BTC to WBTC swaps, Xverse wallet for PSBT-based Bitcoin transactions Infrastructure : Vercel frontend, Torii indexer on AWS EC2 with Nginx + SSL Challenges we ran into Atomiq Token Discovery : Initial BTC to WBTC swaps failed with "No intermediary found." After extensive debugging and reaching out to the Atomiq community on Telegram, we discovered that Atomiq supports a WBTC token used by Vesu lending protocol on Sepolia. Switching to this specific token resolved the issue. RPC Provider Incompatibility : Atomiq worked locally but failed on Vercel with the same error. Root cause: Cartridge RPC doesn't support block_id: "pending" for starknet_call . Switched to Alchemy RPC. gRPC Streaming Reliability : Subscriptions died after 60 seconds with ERR_INCOMPLETE_CHUNKED_ENCODING . Fixed by increasing Nginx timeouts to 3600s, disabling buffering, and implementing HTTP polling as backup. Blockchain Race Conditions : "WRONG_SHOOTER" and "NOT_YOUR_TURN" errors when players acted quickly. Implemented exponential backoff retry logic to handle blockchain propagation delays. ZK Proof Performance : Complete implementation works but proof generation takes too long for real-time multiplayer gameplay. Chose to ship with mock verification for instant UX and leave real ZKPs for a future enhancement, once we solve the performance issue. Accomplishments that we're proud of Production Deployment : Live at zkbattleship.fun with successful remote multiplayer testing across different locations. Complete ZK Implementation : 21/21 Noir circuit tests passing, Garaga Cairo verifiers generated (1.2MB contracts ready to deploy), full offline proof pipeline working. This is production-quality ZK just waiting for performance to catch up. Proper Privacy Architecture : Board configurations never touch the blockchain, only commitments and results are stored on-chain. Demonstrates correct ZK design principles. Real Bitcoin Integration : BTC Testnet3 deposits, Atomiq cross-chain swaps, WBTC staking with automatic escrow settlement. Technical Depth : Resilient real-time multiplayer (gRPC + HTTP polling), V3 transactions with resource bounds, account abstraction, board persistence across sessions, comprehensive error handling. Documentation : 28 markdown files organized in docs/ covering our complete debugging journey, production deployment guide with 8 critical fixes, and pre-deployment checklist. What we learned Technical : Not all RPC providers implement the same features. gRPC alone isn't always reliable, should run HTTP polling as backup. ZKP proving performance is the real bottleneck, not circuit implementation. Proper cryptographic architecture keeps sensitive data off-chain, using commitments for integrity. Ecosystem : Dojo is production-ready for on-chain games. Cartridge Controller provides game-optimized UX with session keys. Atomiq enables true cross-chain composability. Community support (Atomiq Telegram, Dojo Discord, Garaga maintainers) was crucial for overcoming blockers. Product : Real stakes change player behavior - 0.00001 BTC feels different than worthless tokens. UX beats cryptographic purity, instant mock verification is better than slow real ZK proofs for multiplayer gaming. Documentation is a product, our debugging journey helps future developers. What's next for ZK Bitcoin Battleship Immediate : Complete mainnet deployment (contracts + Bitcoin mainnet integration), activate zero-knowledge proofs when performance issues are solved. Short-term : Lightning Network integration for instant deposits, mobile support with responsive design. <div