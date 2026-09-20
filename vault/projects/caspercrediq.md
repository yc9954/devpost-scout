---
slug: "caspercrediq"
url: "https://devpost.com/software/caspercrediq"
title: "CasperCredIQ"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 736
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/document_pdf"
---

# CasperCredIQ

> AI-Gated On-Chain Credentials for Fraud-Resistant Digital Trust

[Devpost](https://devpost.com/software/caspercrediq) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[revocation_withdrawal]]
  <sub>weak: cross_origin_web, structural_withholding</sub>
**domain** [[finance_payments]] [[labor_employment]]
  <sub>weak: developer_tools, immigration_refugee</sub>
  <sub>weak: developer, legal_professional</sub>
**substrate** [[document_pdf]]
  <sub>weak: financial_record, sensor_telemetry, structured_db</sub>

**stack** caper, ipfs, next.js, node.js, pinata, rust, typescript, wasm

## Body

Landing Page Dashboard AI Form Filled AI Verification Issue Verify Request Revoke Audit logs Inspiration Credential fraud, fake certificates, and delayed access revocation are everywhere from education and hiring to healthcare and governance. Existing systems either rely on centralized databases that can be altered or breached, or on blockchain credentials that permanently store unverified data. We were inspired by a simple question: What if credentials were not just verifiable, but justified before they ever existed? CasperCredIQ was built to combine the decision-making strength of AI with the enforcement guarantees of blockchain so trust is evaluated before it is made permanent. What it does CasperCredIQ is an AI-gated, blockchain-secured credential infrastructure. Before any credential is issued: AI evaluates whether the request is legitimate Issuers receive a confidence score and justification Only validated credentials are minted on-chain Once issued: Credentials are cryptographically verifiable Instantly revocable across all systems Time-bound with automatic expiry Fully auditable via immutable on-chain logs The result is a trust system that prevents fraud at the source, not after damage is done. How we built it CasperCredIQ follows a dual-trust architecture: 1) AI Verification Layer Integrated Google Gemini 2.5 Flash Analyzes credential requests, documents, and domain signals Produces a 0–100 confidence score with reasoning 2) Blockchain Enforcement Layer Smart contracts deployed on Casper Network using Odra Role-based access control (Viewer / Issuer / Auditor) Credential hashes stored on-chain, data on encrypted IPFS Instant revocation and millisecond-precision expiry 3) Application Layer Web dashboard for submitting, approving, issuing, and verifying credential Real-time verification in under 100ms Immutable audit trail of every action Challenges we ran into Balancing AI autonomy vs human control Ensuring AI assists decisions without becoming a black box required explainable scoring and issuer override logic. Designing instant revocation Most credential systems fail here. Implementing near-real-time invalidation while maintaining decentralization was non-trivial. Security vs demo accessibility Access-controlled smart contracts are safer but harder to demo. We had to clearly document this for reviewers. Avoiding PII exposure Ensuring no sensitive data ever touched the blockchain required careful hashing and storage design. Accomplishments that we're proud of Built a working, deployed prototype with real smart contracts Achieved instant revocation across all verifications Implemented AI-first decision gating, not AI as a gimmick Designed a fully auditable, privacy-preserving credential flow Created infrastructure usable across education, hiring, healthcare, and governance What we learned Blockchain alone cannot solve trust input validation matters AI must be explainable to be usable in security-critical systems Revocation speed is as important as verification accuracy Infrastructure projects need strong documentation to communicate value clearly What's next for CasperCredIQ Short term (3–6 months): Mobile credential scanner with QR verification Biometric confirmation before credential usage Multi-chain compatibility (Ethereum / Polygon) Long term (1–2 years): Zero-knowledge selective disclosure ML-driven fraud pattern learning Decentralized credential marketplace Cross-border compliance partnerships CasperCredIQ aims to become the trust layer for the next generation of digital credentials—where every credential is provably earned, transparently issued, and instantly revocable. Testing Instructions (Judges & Reviewers) Access setup required (intentional security feature) CasperCredIQ uses role-based access control to prevent unauthorized credential issuance. To test full functionality, Issuer access is required . Step 1: Share Your Casper Public Key Install the Casper Wallet browser extension Create or import a wallet Copy your public key (starts with 01 or 02 ) Share it with me via: GitHub Issues (CasperCredIQ) Email: ritigya00003@gmail.com Platform messaging (Devpost / DoraHacks) Step 2: Access Levels Level 0: No access (default) Level 1: Viewer (public data only) Level 2: Issuer (required for testing) Level 3: Auditor Level 4: Owner (admin only) Step 3: Test the Full Flow Submit a credential request Review AI confidence score & justification Approve and issue credential on-chain Verify credential instantly Revoke credential and observe real-time invalidation View immutable audit logs Expected Results AI confidence score: 60–95% IPFS upload: <2 seconds Blockchain confirmation: ~30 seconds Verification latency: <100ms Note: Access control is a security design choice, not a limitation. It ensures only authorized issuers can mint or revoke credentials. Track FinTech & Blockchain – Innovative applications in finance, crypto, secure transactions, or decentralized systems. CasperCredIQ is a next-generation digital trust infrastructure that combines AI-driven verification with blockchain-enforced credentials. It enables fraud-resistant issuance, instant revocation, and cryptographic verification of digital credentials making it ideal for financial compliance, identity verification, and decentralized governance use cases. Solo Project This project was designed and built entirely by me as a solo developer for Frostbyte Hackathon. <div