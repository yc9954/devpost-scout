---
slug: "zkbadge"
url: "https://devpost.com/software/zkbadge"
title: "zkbadge"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 882
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "mechanism/structural_withholding"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "user/developer"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# zkbadge

> Privacy-Preserving Age-Gated Content & Features with Zero-Knowledge Proofs on Starknet

[Devpost](https://devpost.com/software/zkbadge) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[revocation_withdrawal]] [[structural_withholding]]
**domain** [[agriculture_food]] [[civic_government]] [[developer_tools]] [[finance_payments]] [[scientific_research]] [[security_privacy]]
**user** [[developer]] [[educator_student]]
**substrate** [[sensor_telemetry]]

**stack** cairo, noir, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for zkbadge

## Body

ZkBadge Inspiration The inspiration for ZkBadge stems from the growing tension between regulatory demands for age verification in digital services and the core Web3 principle of user privacy. Traditional age-gating methods—such as uploading government IDs or sharing birthdates—expose sensitive personal data to centralized platforms, leading to privacy breaches and eroding trust. Projects like Google's 2025 integration of zero-knowledge proofs (ZKPs) into Wallet for privacy-focused age checks and zkMe's zkKYC for decentralized identity verification highlighted the potential of ZKPs to solve this. We saw an opportunity to extend this to a creator-driven marketplace on Starknet, where users could prove eligibility for age-restricted content (e.g., premium courses, NFTs, or dApps) without revealing personal details, while enabling monetization and community governance. Drawing from blockchain-based age verification systems like Segpay's privacy-friendly solutions and Concordium's protocol-level ZKPs, ZkBadge aims to make compliant, privacy-preserving access control accessible to Web3 creators and users. What it does ZkBadge is a Starknet-based protocol for privacy-preserving age-gated features and content. Creators publish "features" (e.g., 18+ tutorials, exclusive drops, or gated communities) with minimum age requirements and optional ERC20 payments. Users generate ZK proofs using a Noir circuit to demonstrate: Valid certificate ownership (via Poseidon2 hashing) Age eligibility (e.g., ≥18 without revealing birth year) Uniqueness (via nullifiers to prevent replay attacks) The system verifies Honk proofs on-chain, handles payments, tracks access/votes, and allows creators to withdraw funds. Key features include certificate revocation, trusted issuer management, and community voting for feature quality. It supports any ERC20 token, ensuring multi-chain compatibility while maintaining TVL tracking for protocol economics. How we built it We architected ZkBadge as a full-stack dApp: ZK Circuit (Noir) : Defined a circuit for certificate hashing, age checks, and nullifier generation. Used Poseidon2 for efficient hashing and public inputs for on-chain verification. Smart Contracts (Cairo 2.0/Starknet) : Implemented the core IZkBadgeImpl contract with storage for features, certificates, and nullifiers. Integrated Garaga for UltraHonk verifier generation and library calls for proof validation. Added ERC20 dispatcher for payments. Proof Pipeline (Barretenberg) : Automated proof generation with bb prove (UltraHonk scheme) and VK extraction. Makefile targets handle building, execution, and artifact copying. Frontend (Bun/Vite + React) : Built a responsive UI for creators (publish features) and users (generate proofs, access/vote). Integrated Starknet.js for wallet connections and proof submission. DevOps : Used Starknet devnet for testing, with Makefile orchestration for installs (Bun, Noir, Barretenberg), deployments ( sncast ), and E2E flows. Environment configs handle accounts and RPCs. Deployment flow: Compile circuit → Generate VK/verifier → Declare/deploy contracts → Copy artifacts to frontend. Challenges we ran into ZK Integration Complexity : Barretenberg and Garaga tooling was nascent; we faced version mismatches (e.g., RPC 0.8 vs. 0.7 in devnet) and type errors in Cairo (e.g., ClassHash vs. StorageBase unboxing). Proof deserialization required careful handling of public inputs. Package Manager Conflicts : Bun/Vite setups clashed with Yarn/Corepack, causing "unenv/mock/empty" resolution errors. Fixed by disabling Corepack and adding polyfills for Node builtins. Starknet Ecosystem Maturity : asdf tool management failed for starknet-devnet (version not set), and Makefile targets needed robust error handling for accounts.json parsing. RPC incompatibilities halted deployments until client updates. Privacy-Compliance Balance : Ensuring nullifiers prevented replays without on-chain data leaks, while keeping gas costs low for library calls. These hurdles took ~40% of development time but strengthened our grasp of Starknet's ZK-native capabilities. Accomplishments that we're proud of End-to-End ZK Flow : Successfully integrated Noir circuits with Starknet's Honk verifier, achieving sub-second proof generation and on-chain validation—proving age without revealing any PII. Multi-Token Marketplace : Built a flexible creator economy with ERC20-agnostic payments, TVL tracking, and creator withdrawals, all while enforcing ZK access controls. Privacy-First Design : Implemented global nullifiers and revocable certificates, aligning with FATF-compliant projects like zkMe and IOTA's tokenized KYC, but tailored for content creators. Developer-Friendly Pipeline : Created a comprehensive Makefile for one-command setups (e.g., make deploy-all ), making ZkBadge reproducible and hackathon-ready. We're especially proud of the seamless user experience: prove once, access forever, with zero data exposure. What we learned ZK Tooling Evolution : Starknet's UltraHonk and Garaga simplify proof verification but require precise version alignment; future devs should prioritize RPC 0.8 compatibility early. Ecosystem Interoperability : Mixing tools (Bun, asdf, npm) demands strict lockfile management—stick to one manager per layer (Bun for frontend, Scarb for contracts). Privacy Engineering : ZKPs excel at selective disclosure but amplify the need for robust nullifiers; we learned to balance on-chain storage costs with off-chain proof efficiency. Web3 UX Priorities : Compliance doesn't have to kill decentralization—reusable credentials (inspired by Togggle's KYC) enhance adoption, but frontend proof generation must be intuitive to avoid drop-off. Overall, building ZkBadge deepened our appreciation for Starknet's ZK-native advantages over Ethereum L2s. What's next for zkbadge Mainnet Launch & Integrations : Deploy on Starknet mainnet, partner with DeFi/NFT platforms for real-world age-gating (e.g., 18+ yield farms). Advanced ZK Features : Add batch proofs for multi-user access, cross-chain support via bridges, and biometric certificate issuance. SDK & Tools : Release a JS SDK for easy proof generation and a creator dashboard for analytics/voting insights. Expansion : Evolve to full zkKYC for broader compliance (e.g., geo-fencing, credit scoring) while exploring AI-assisted circuit optimization. Community & Governance : Launch a DAO for feature curation, with ZK-voting to maintain decentralization. ZkBadge is just the start—aiming to power privacy-compliant Web3 experiences at scale! 🚀 <div