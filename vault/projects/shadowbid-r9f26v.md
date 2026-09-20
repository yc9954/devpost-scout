---
slug: "shadowbid-r9f26v"
url: "https://devpost.com/software/shadowbid-r9f26v"
title: "ShadowBid"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 717
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# ShadowBid

> ShadowBid is a fully functional sealed-bid auction protocol deployed on Solana Devnet that demonstrates how confidential computing primitives solve real DeFi problems around information asymmetry.

[Devpost](https://devpost.com/software/shadowbid-r9f26v) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[privacy_tech]] [[provenance_signing]]
  <sub>weak: realtime_stream</sub>
**domain** [[developer_tools]]
**substrate** [[financial_record]]
  <sub>weak: code_repository</sub>

**stack** anchor, inco-javascript-sdk, nextjs, rust, tailwind, typescript

## Body

The Inspiration I've seen front-running and bid sniping in on-chain auctions. Validators can see pending bids, and competitors can snipe at the last second. Commit-reveal schemes help but add complexity and still leak information during reveals. When I learned about Inco Lightning's confidential computing on Solana, I saw a path to sealed-bid auctions where bids stay encrypted throughout. The idea: use homomorphic operations to compare encrypted bids without decryption, revealing only the winner's amount at settlement. What I Learned This project required learning several new concepts: Homomorphic encryption on-chain : Inco Lightning's e_ge and e_select let us compare and select encrypted values without decryption. This enables winner determination entirely in encrypted space. TEE attestation : Inco's Trusted Execution Environment provides cryptographic proofs for decryption. The is_validsignature CPI verifies that a decrypted value came from the TEE, enabling trustless settlement without a trusted third party. Solana program design : I structured the auction as a state machine with PDAs for auctions and bids. The permissionless determine_winner instruction allows anyone to process bids, reducing reliance on a single actor. Client-side encryption flow : The @inco/solana-sdk handles encryption/decryption, but integrating it with Solana transactions—especially attested decryption with Ed25519 verification instructions—required careful sequencing. How I Built It Phase 1: Smart contract architecture I started with the Anchor program, defining Auction and Bid accounts as PDAs. The auction state machine ( Open → Closed → WinnerDetermined → Settled ) ensures correct transitions. The place_bid instruction uses Inco's new_euint128 CPI to convert client-encrypted ciphertext into an on-chain handle. This handle is stored in the bid account, no plaintext values on-chain. Phase 2: Encrypted winner determination The hardest part was determine_winner . I iterate through bids and compare each against the current highest using e_ge . If higher, e_select updates the highest bid handle and leader. All comparisons happen in encrypted space, so no bid values are exposed. I added a processed flag to prevent double-counting and track bids_processed to know when all bids are compared. Phase 3: Selective disclosure and settlement After finalization, finalize_winner calls Inco's allow to grant the winner decryption permission for their bid handle. Only the winner can decrypt. For settlement, the winner calls decrypt() from the SDK, which returns the plaintext and a TEE attestation signature. The settle_auction instruction verifies this via is_validsignature before transferring SOL, ensuring the decrypted amount is authentic. Phase 4: Frontend integration The Next.js frontend uses the Inco SDK for encryption before place_bid and attested decryption before settle_auction . Wallet integration via Solana Wallet Adapter handles transaction signing, and React Query manages auction state and real-time updates. Challenges Faced Challenge 1: Understanding encrypted handle types Early on, I stored ciphertext directly. Inco Lightning uses handles (128-bit identifiers) that reference encrypted values in the TEE. Switching to handles required refactoring the bid storage structure and understanding how handles persist across transactions. Challenge 2: Attested decryption verification The settle_auction instruction needs Ed25519 verification instructions from the SDK. These must be included in the transaction's instruction list, which required careful account ordering and instruction construction. Debugging failed verifications took time until I understood the exact format expected by is_validsignature . Challenge 3: Permissionless winner determination I wanted anyone to process bids, but needed to prevent double-processing. The processed flag solved this, but I also had to ensure the auction state transitions correctly and that finalize_winner can only be called after all bids are processed. Challenge 4: Client-side encryption timing Encryption happens client-side before transaction construction. If encryption fails or takes too long, the user experience degrades. I added error handling and loading states, and optimized the encryption flow to minimize delays. Challenge 5: Testing encrypted operations Testing homomorphic operations is harder than plaintext logic. I couldn't easily log intermediate values. I built test cases that verify state changes (like current_leader updates) rather than encrypted values directly, and used the Inco SDK's decryption capabilities in tests to verify correctness. The Result ShadowBid demonstrates that confidential computing can solve real DeFi problems. By keeping bids encrypted throughout the auction lifecycle, we eliminate front-running, bid sniping, and collusion while maintaining decentralization and trustlessness through TEE attestation. The protocol is fully functional on Solana Devnet, with a complete frontend for auction creation, bidding, and settlement. It shows how Inco Lightning's primitives enable new DeFi applications that weren't possible on transparent blockchains. <div