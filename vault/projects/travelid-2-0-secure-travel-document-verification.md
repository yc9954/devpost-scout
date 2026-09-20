---
slug: "travelid-2-0-secure-travel-document-verification"
url: "https://devpost.com/software/travelid-2-0-secure-travel-document-verification"
title: "TravelID 2.0 - Secure Travel Document Verification"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 558
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# TravelID 2.0 - Secure Travel Document Verification

> TravelID 2.0 turns identity from papers into proof — a Polkadot-based platform for instant, tamper-proof, and private verification of travel documents anywhere in the world.

[Devpost](https://devpost.com/software/travelid-2-0-secure-travel-document-verification) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[provenance_signing]]
  <sub>weak: cross_origin_web</sub>
**domain** [[security_privacy]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** axum, polkadot.js, postgresql, react, rust, shadcn/ui, sqlx, subxt, tailwindcss, tokio, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for travelid 2.0 - secure travel document verification

## Body

main page (starting point) learn more page The Learn More page The documents page The Dashboard Inspiration Travel document verification is a common problem. Traveler's often need to prove document authenticity to authorities, hotels, and services, but current methods are fragmented and vulnerable to forgery. We wanted a solution that: Provides cryptographic proof of document authenticity Works without exposing sensitive document contents Uses decentralized infrastructure for trust Is accessible to anyone with a wallet Polkadot’s interoperability and security make it a good fit for a cross-chain verification system that can scale globally. What it does TravelID 2.0 is a decentralized document verification platform on Polkadot. Users can: Upload travel documents (passports, driver’s licenses, national IDs) via a web interface Generate cryptographic hashes (SHA-256) of documents Store hashes on-chain using Polkadot system remarks for immutable proof Verify authenticity by comparing document hashes with on-chain records Share verification via QR codes or links without exposing document contents The system verifies authenticity without storing or exposing document contents, protecting privacy while providing cryptographic proof. How we built it Backend (Rust) Axum for async HTTP Subxt for Polkadot/Substrate integration SQLx with PostgreSQL for metadata SHA-256 hashing for document integrity System remarks to store hashes on-chain Frontend (React + TypeScript) React 18 with TypeScript Polkadot.js for wallet integration (Polkadot.js, Talisman) shadcn/ui components TanStack Query for data fetching Zustand for state QR code generation for sharing Architecture Document upload: frontend sends file to backend Hash generation: backend computes SHA-256 Database storage: metadata stored in PostgreSQL Blockchain submission: hash submitted via Subxt as a system remark Verification: anyone can verify by comparing hashes The system uses Polkadot’s remark pallet to store hashes on-chain, providing immutable proof without custom pallets. Challenges we ran into Polkadot integration: learning Subxt and Polkadot’s transaction model, handling async operations and transaction finalization. it was tough especially finding explorers and my local txhash when it was successful Wallet connection: integrating multiple wallet extensions with different APIs Hash verification: designing a system that verifies without exposing document contents UX: making blockchain concepts accessible to non-technical users Performance: optimizing database queries and blockchain interactions for responsiveness Accomplishments that we're proud of Full-stack implementation: working backend and frontend with blockchain integration (Testnet/Localnet) Privacy-first design: verification without exposing document contents User experience: intuitive interface for document management and verification Real blockchain integration: actual transactions on Polkadot, not just mockups QR code sharing: easy verification sharing Modern tech stack: Rust backend and React frontend with TypeScript (could also use next but I had a template ready for this kind of stuff) What we learned Polkadot ecosystem: Subxt, transaction lifecycle, and remark pallet usage Rust async programming: Tokio, Axum, and async patterns Blockchain UX: simplifying complex concepts for end users Cryptographic hashing: SHA-256 for document integrity Full-stack development: integrating blockchain, database, and frontend Error handling: robust error management in distributed systems What's next for TravelID 2.0 - Secure Travel Document Verification Custom Polkadot pallet: replace system remarks with a dedicated pallet for better indexing and querying Multi-chain support: leverage Polkadot’s interoperability for cross-chain verification Document encryption: optional client-side encryption before hashing Mobile app: native iOS/Android apps or react native app (hopefully if i win) Batch verification: verify multiple documents at once API access: public API for third-party integrations Advanced features: document expiration tracking, revocation, and delegation International standards: compliance with W3C Verifiable Credentials and related standards <div