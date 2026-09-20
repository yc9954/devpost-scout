---
slug: "whisper-asset-transfer-leveraging-ccip-and-zk-proofs"
url: "https://devpost.com/software/whisper-asset-transfer-leveraging-ccip-and-zk-proofs"
title: "Whisper Asset Transfer: Leveraging CCIP and ZK Proofs"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 322
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "mechanism/voice_speech"
  - "substrate/financial_record"
---

# Whisper Asset Transfer: Leveraging CCIP and ZK Proofs

> A new era of Cross-chain Interoperability, representing a sophisticated method of transferring digital assets across different blockchain networks, leveraging CCIP and Zero Knowledge Proofs

[Devpost](https://devpost.com/software/whisper-asset-transfer-leveraging-ccip-and-zk-proofs) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[structural_withholding]] [[voice_speech]]
**substrate** [[financial_record]]

**stack** circom, node.js, snarkjs, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for whisper asset transfer

## Body

Architecture of Whisper Asset Transfer Solution Initiate Mint Burn Confidential Transaction Sender Circuit Confidential Transaction Receiver Circuit Confidential Transaction New Account - Zero Balance Circuit Inspiration ZK Proofs are taking center stage as the backbone behind ZK Rollups for Layer 2 solutions as well as other cases where constraints need to be maintained on private data What it does This project allowed us to explore how the Chainlink CCIP for transferring of assets between two blockchains could be extended to support Confidential Transactions through the use of ZK-Snarks How we built it We leveraged ZK-Snark circuits built with Circom to verify constraints that tokens are being properly maintained and also to help validate that the asset was correctly burned and minted on either end of the CCIP bridge Challenges we ran into Confidential Transactions has been referenced in literature dating back to 2017, but there is still a lack of a standard around how they should be used in smart contracts (although ERC1724 was proposed in 2019), and there is also a lack of implementations of this privacy preserving algorithm Accomplishments that we're proud of We are proud to confirm that privacy preserving transactions can be implemented through the CCIP bridge, and that it also adds value in that the Zero-Knowledge Proof can be used on each side of the CCIP bridge to validate that the token was correctly burned and minted on either side of the bridge What we learned Everything from understanding and gaining exposure to cross-chain/interoperability and ZKProofs all the way to learning how to create a more visually appealing demo. The team has varied levels of development and product experience but brought together our diverse skillsets to make it work and learn from each other through this solution What's next for Whisper Asset Transfer We identified a few limitations of the current implementation that could be improved in future revisions of the algorithm (refer to the PPTX) <div