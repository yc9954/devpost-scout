---
slug: "warisan"
url: "https://devpost.com/software/warisan"
title: "WARISAN"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 736
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# WARISAN

> The Intangible Heritage Ledger

[Devpost](https://devpost.com/software/warisan) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**domain** [[developer_tools]]
**substrate** [[financial_record]]

**stack** javascript, next, rust, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for warisan

## Body

Thumbnail WARISAN: The Intangible Heritage Ledger Inspiration We are facing a global crisis of vanishing cultures. Inspired by UNESCO's work on intangible heritage and the ASEAN summit's themes of "Inclusivity and Sustainability," we saw a critical problem: current preservation models are neither. They are not inclusive of the Culture Bearers (the elders, storytellers, and craftspeople) and are not economically sustainable, treating preservation as a cost, not an asset. We found a Malay proverb that became our guiding principle: "Tak kenal maka tak cinta" —"You cannot love what you do not know." We are building WARISAN to ensure future generations can know. What it does WARISAN is a purpose-built blockchain designed to answer one question: How do we transform cultural preservation from a cost center into a sustainable economic activity? It's a decentralized "proof-of-preservation" system. Instead of relying on sporadic grants, WARISAN creates a new economy where: Elders are compensated with the native $WARIS token for sharing their knowledge. Documentarians are rewarded for ethically recording and submitting heritage. Communities maintain sovereignty with the power to approve, restrict, or veto content related to their culture. We are creating a permanent, immutable, and living ledger that provides economic value back to the communities where the heritage originates. How we built it A simple smart contract couldn't achieve this. We needed a sovereign, purpose-built chain, which is why we chose the Polkadot SDK and the Substrate framework. Custom Logic: Substrate allowed us to build custom, base-layer logic. Our core innovation, pallet-preservation , is the chain. It defines the "Proof-of-Preservation" mechanism that manages the entire lifecycle of a submission, its verification, and the automated reward distribution. This is impossible on a standard smart contract platform. Parachain Model: By building as a Polkadot parachain, WARISAN operates as an independent Layer-1 with its own tokenomics ($WARIS), avoiding high gas fees and creating a sustainable micro-economy. Decentralized Storage: Our system uses IPFS for decentralized, immutable storage of the cultural data (audio/video). The blockchain stores the unchangeable proof—the metadata, the consent, and the verification. Sovereign Governance: The entire system is governed by a multi-stakeholder community of Culture Bearers, Documentarians, Validators, and Community Councils, who have ultimate sovereignty over their content. Challenges we ran into Designing Equitable Tokenomics: Our biggest challenge was designing a model that wasn't extractive. We had to ensure the primary value flowed to the Culture Bearers, not just to token holders or validators. This led to the multi-stakeholder reward split and the Community Council funds. Balancing Sovereignty and Decentralization: We had to balance the decentralized ideal of "code is law" with the absolute need for cultural sovereignty. We solved this by giving Community Councils a special veto power that can override protocol decisions for content related to their community. Substrate Learning Curve: The Polkadot SDK is incredibly powerful, but implementing custom logic in the pallet-preservation module within a tight timeframe was a significant technical challenge. Accomplishments that we're proud of A Novel "Proof-of-Preservation" Model: We designed a complete, well-thought-out economic and governance model that directly links token inflation to the verified preservation of cultural heritage. A Working Custom Pallet: We successfully implemented the core logic for pallet-preservation in Substrate, proving our concept is technically feasible. Human-Centric Design: We are most proud that our whitepaper and architecture are built around the humans at the center of this problem—the Culture Bearers. The system is designed to empower them, not just extract their "data." What we learned Aligning Incentives is Key: We learned that the most powerful application of blockchain isn't just to store data, but to create novel economic incentives that can solve real-world problems. Substrate is the Right Tool: For complex, purpose-built systems, the power of the Polkadot SDK is unmatched. You can build logic at the "chain-level" that a smart contract could never achieve. Tokenomics is Governance: The way you design your token flow is your governance. We learned to think of tokenomics not just as finance, but as the encoding of our project's values. What's next for WARISAN Our hackathon project is the foundation. The next steps are: Launch Testnet: Get the pallet-preservation module onto a public testnet. Onboard Genesis Validators: Begin recruiting the first expert Cultural Validators. Pilot with Communities: Partner with 3-5 cultural organizations in the ASEAN region to run the first pilot preservation projects. Develop the UI/App: Build the user-friendly web portal and mobile app for field documentarians and Culture Bearers to interact with the chain easily. <div