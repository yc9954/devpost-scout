---
slug: "polkashield-og8vky"
url: "https://devpost.com/software/polkashield-og8vky"
title: "PolkaShield"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 526
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "substrate/structured_db"
---

# PolkaShield

> Turn any Web2 app into a tamper-proof, portable, user-owned identity + permissions system on Polkadot.

[Devpost](https://devpost.com/software/polkashield-og8vky) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]]
**substrate** [[structured_db]]

**stack** rust, substrate

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

Inspiration Every Web2 application, from school portals to admin dashboards to platforms, relies on a centralized access-control model, often reduced to a single database flag like is_admin = true. That tiny line silently governs permissions, authority, and trust. But because it lives inside a private server, it creates a dangerous single point of failure. If the database goes down, gets corrupted, or is compromised, the entire access-control system collapses. I kept asking myself: What if permissions were user-owned instead of server-owned? What if they were tamper-proof, verifiable, and portable across applications? When I discovered the Polkadot SDK’s modular blockchain design, the solution became obvious. We could decentralize access control itself, not as another token or DeFi concept, but as real infrastructure to make Web2 more resilient and secure. That spark is what led to PolkaShield. What it does PolkaShield introduces a decentralized, cryptographically verifiable access-control layer for Web2 applications. It includes: A custom Polkadot chain that stores roles, permissions, and audit logs A dashboard where admins can create roles and assign permissions A public API gateway that lets Web2 apps verify access using a simple call like: /verify-access?user=<address>&role=editor A demo “Editor Portal” that shows how permissions unlock or restrict actions in real time Users own their permissions through wallet signatures, and developers get a reliable, tamper-proof way to manage access. How we built it PolkaShield is composed of four coordinated components: 1. Custom Polkadot Blockchain (Rust + Substrate) We created: A Roles Pallet to define system roles A Permissions Pallet linking accounts to roles An Audit Pallet providing immutable logs 2. Dashboard (Next.js + Polkadot.js API) A clean UI for: Connecting wallets Creating roles Assigning roles Viewing logs 3. API Gateway (Node.js / TypeScript) A lightweight microservice that: Connects to the chain Verifies whether a user has the required role Returns boolean responses for Web2 apps 4. Web2 Demo App A simple interface demonstrating real-world usage: “Edit Page” unlocks only if the user has the correct role ## Challenges we ran into Understanding Substrate pallet boundaries and proper runtime configuration Handling RPC metadata and wallet integration, especially around Polkadot.js extension behavior Rust borrow checker issues inside pallets Designing a minimal yet extensible role/permission data model Time constraints while building a full chain + UI + API + demo end-to-end ## Accomplishments that we're proud of Building a fully functional custom blockchain runtime in the hackathon timeframe Designing a real Web2 → Web3 bridge that any developer can integrate Creating an end-to-end permission system from on-chain pallets to dashboard to Web2 demo Writing clean, modular documentation across ADRs, PRDs, and runbooks Delivering a concept that solves a real problem beyond crypto speculation ## What we learned How to design and implement Substrate runtime pallets The importance of wallet UX, especially for non-Web3-native users ## What's next for PolkaShield Add ZK-based private permissions, so roles can be proven without revealing identity Add delegated authority, enabling role inheritance or approval flows Deploy as a parachain for better performance and shared security Build SDKs for Web2 frameworks (React, Laravel, Django, Node) Add organizations and multi-admin governance Launch a production-grade version used by real Web2 apps across Africa and beyond <div