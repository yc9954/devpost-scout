---
slug: "starkcloak"
url: "https://devpost.com/software/starkcloak"
title: "StarkCloak"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 576
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "substrate/code_repository"
---

# StarkCloak

> Make wallets private again,Make decentralisation great again

[Devpost](https://devpost.com/software/starkcloak) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
  <sub>weak: realtime_stream, structural_withholding</sub>
**substrate** [[code_repository]]
  <sub>weak: financial_record</sub>

**stack** cairo, merkle-trees, node.js, react, starkli

## Body

Landing Deposit Withdraw hash hash pitch 1 pitch 2 pitch 3 StarkCloak: Make wallets private again! Inspiration In the world of blockchain, transparency is a double-edged sword. Every on-chain interaction — every swap, bridge, and transfer — adds a traceable layer to your digital identity . When we explored the ecosystem of wallet trackers and indexers , it became clear how exposed users really are. Even if you move to a new wallet, your transaction graph can be reconstructed — revealing links between your old and new addresses. We drew inspiration from projects like RailGun , which pioneered privacy on Ethereum, but found that existing mixers on Starknet were either incomplete, lacked full decentralization, or relied on trusted setups. So we asked ourselves: Can we design a trustless privacy layer native to Starknet — one that allows users to truly escape their digital footprint while preserving their tokens, identity, and value? That question led to StarkCloak . Problem Centralized DEXs like Binance link your KYC data directly to your wallets. Wallet trackers and indexers reveal your holdings, transfers, and interactions in real time. On-chain transparency means your wallet graph can be easily deanonymized. Even moving to a “new” wallet doesn’t help — your transfer path betrays your identity. There was no way to escape your digital footprint within Starknet while remaining on-chain and trustless. Solution — StarkCloak StarkCloak is a trustless, privacy-preserving mixer for Starknet that lets users break their on-chain linkages. It allows any wallet to: Deposit tokens (ERC20) with a hidden commitment . Later withdraw to a new wallet — unlinkable to the original depositor. Our system ensures complete privacy while remaining verifiable, auditable, and fully on-chain . How We Built It The flow was designed for verifiable privacy without trusted setup : User generates secrets: (secret,nullifier) Computes: commitment = Poseidon(secret, nullifier) Deposit phase: User approves Mixer to spend ERC20 tokens. Calls deposit(commitment, amount) . Contract pulls tokens, stores the commitment, and emits a Deposit event. Merkle tree update: Backend / TEE listens for deposits. Builds an unsorted-leaf Merkle tree with pairwise-sorted hashing. Calls update_root(new_root) on-chain as the owner. Withdrawal phase: User (or another wallet) requests a Merkle proof for their commitment. Calls withdraw(merkle_proof, secret, nullifier, recipient, amount) . The contract: Recomputes ( \text{commitment} = Poseidon(\text{secret}, \text{nullifier}) ) Verifies the proof. Checks nullifier not spent. Transfers tokens to the new wallet, ensuring unlinkability. This architecture ensures no centralized intermediary can link deposits and withdrawals — privacy is enforced by math, not trust. What We Learned How to combine Starknet’s Cairo VM with zero-knowledge-based privacy flows . Efficient Merkle tree management using sorted internal hashing to avoid path collisions. The intricacies of Poseidon hashing and commitment verification on L2. Handling cross-contract ERC20 approvals securely within Starknet’s account abstraction model. We also gained a deeper appreciation of the trade-offs between off-chain computation (TEE) and on-chain verification for scalability and trustlessness. Challenges We Faced Tree synchronization: Ensuring Merkle roots between backend and on-chain state remain consistent. Proof generation latency: Optimizing zk-proof verification time within Starknet’s execution model. Cross-contract allowance management: Dealing with non-standard ERC20 implementations on Starknet. Frontend anonymity: Designing UX for a privacy app without exposing user identity via API calls. Conclusion With StarkCloak , we bring privacy-as-a-right to Starknet — enabling users to transact, trade, and move assets freely without carrying their digital footprint forward. A future where you can be both visible on-chain and invisible in identity — that’s the world StarkCloak envisions. <div