---
slug: "daomix"
url: "https://devpost.com/software/daomix"
title: "DaoMix"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 469
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# DaoMix

> DaoMix is a privacy-as-a-service network that provides anonymous voting and messenging for all Polkadot parachains.

[Devpost](https://devpost.com/software/daomix) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[civic_government]]
**substrate** [[financial_record]] [[geospatial]]

**stack** nextjs, onion, rust, typescript

## How they structured the write-up

- what inspired us
- what we learned
- how it works
- how we built it
- challenges we faced
- where we are now

## Body

logo Features, Architecture, Data flow use cases sandbox What Inspired Us We noticed a gap: blockchain governance is transparent, but transparency can enable coercion. People should be able to vote and communicate without fear of retaliation. We set out to build anonymous voting and encrypted communication that works across Polkadot parachains. What We Learned Cryptography is hard, but doable. We implemented mixnets with X25519 key exchange and XChaCha20-Poly1305 encryption. Each layer had to be correct, or anonymity breaks. the mixer has a hybrid post-quantum mode that combines X25519 with ML-KEM (Kyber) for onion layers and transport hops. XCM is powerful but complex. Cross-chain communication required understanding barriers, origin conversion, and message routing. Getting the first cross-chain message working took time. Privacy needs multiple layers. On-chain anonymity isn’t enough if your IP address is exposed. We added transport mix—3-hop onion routing for RPC calls—to protect transaction submission. How It Works User Flow: Data Encryption, Hops, Sharding, and On-Chain Posting Vote Encryption & Storage User casts vote → Encrypt in 4 layers (Tally → Mix3 → Mix2 → Mix1) ↓Submit via Transport Mix (3-hop IP protection) ↓Store encrypted ballot on-chain Cross-Chain Job Submission Parachain submits MixJob via XCM → DaoChain validates → Creates job (status: Pending) Mixing Process (3 Hops with Sharding) Hop 1: Mix Node 1 Peels Layer 1, shuffles ballots, shards each ballot into k pieces Hop 2: Mix Node 2 Reconstructs ballots from shards, peels Layer 2, shuffles, shards again Hop 3: Mix Node 3 Reconstructs ballots, peels Layer 3, shuffles, returns final ciphertexts Final Decryption & Tally Orchestrator decrypts Layer 4 with Tally key ↓Extracts votes → Computes tally ↓Computes Merkle roots (input & output) for verification On-Chain Posting Submit tally + Merkle roots to DaoChain ↓Update MixJob status: Completed ↓Results stored on-chain, verifiable by anyone How We Built It We started with a single mix node and one vote. Once that worked, we added nodes and scaled up. The system has three parts: DaoChain parachain with voting and mixing pallets Mix-node network that shuffles encrypted ballots Transport mix that protects IP addresses during submission We used TypeScript for rapid iteration, with the logic ready to move on-chain once the runtime rebuilds. Challenges We Faced Dependency conflicts: A Rust dependency issue blocked runtime builds. We worked around it, but it slowed progress. WebSocket vs HTTP: Polkadot.js uses WebSocket subscriptions, while transport mix is HTTP-based. We built a hybrid that routes subscriptions directly and sends transactions through the mix. Orchestrator reliability: Automatic job processing needed careful state management to avoid stuck or duplicate jobs. Where We Are Now DaoMix works. You can create anonymous elections, cast unlinkable votes, publish encrypted content, and communicate across parachains with identity protection. It’s real cryptography on real blockchains, not a simulation. We’re building toward privacy-preserving governance that’s both verifiable and anonymous. <div