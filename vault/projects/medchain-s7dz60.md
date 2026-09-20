---
slug: "medchain-s7dz60"
url: "https://devpost.com/software/medchain-s7dz60"
title: "MedChain"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 856
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# MedChain

> MedChain: A blockchain-powered app for secure, verifiable prescriptions. Built on Base with smart contracts and IPFS to eliminate fraud and streamline doctor–pharmacist workflows.

[Devpost](https://devpost.com/software/medchain-s7dz60) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[privacy_tech]] [[provenance_signing]] [[realtime_stream]] [[revocation_withdrawal]]
**domain** [[finance_payments]] [[health_clinical]] [[security_privacy]]
**user** [[clinician]] [[patient_family]]
**substrate** [[document_pdf]] [[financial_record]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** base, coinbase, html, javascript, react, reka, solidity, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for medchain

## Body

Opium Statistic MedChain Ethereum Addresses: Shang: 0x053Efe0AffA694e3d1CB82795117a8a9135cb9a7 Eric: 0x600fc3eaa9f16ff5e6f8148405a9214232708f7e Sachin: 0x6ad9ed6bc06689f21293ad928644eeaa786e05a7 Arnav: 0x437c51f303c3E80E4E8Ef39c495B33b825FB4336 MedChain: Blockchain-Powered Prescription Management Inspiration Every day, nearly 200 Americans die from opioid overdoses — many from legally obtained prescriptions. Behind those numbers lies a broken system: doctors, pharmacists, and patients operating in silos, with no unified way to verify prescriptions or detect duplicate fills across states. During our initial research, we spoke with a board certified doctor who described the reality on the frontlines — duplicate opioid prescriptions, inconsistent access to patient records, and an overwhelming amount of inconsistency in prescription platforms across the country. Each U.S. state maintains its own Prescription Drug Monitoring Program (PDMP) , yet these systems don’t talk to each other. This fragmented design costs billions in fraud and, more importantly, thousands of preventable deaths each year. We realized that the true problem isn’t data — it’s trust . What if every verified doctor and pharmacist shared a single, tamper-proof ledger for prescriptions, one that no patient could exploit and no state bureaucracy could delay? That question led to MedChain — a decentralized prescription management system designed not just to streamline healthcare, but to save lives . What it does MedChain transforms how prescriptions are created, shared, and verified across the healthcare ecosystem without a centralized database or server. For Doctors Issue digitally signed prescriptions that are stored immutably on-chain. Automatically generate a patient-specific QR code for seamless sharing and later verification. Track issued prescriptions, view statuses, and revoke them if necessary. For Pharmacists Scan a patient’s QR code to instantly verify the authenticity of a prescription using cryptographic validation. Dispense the medication and record the transaction on the blockchain for transparent tracking. For Patients No wallet, no gas. Patients authenticate with Base Accounts using passkeys (WebAuthn) — no seed phrases required. All on-chain actions are executed through abstracted accounts on Base; gas fees are sponsored via our paymaster so patients never pay gas. View active prescriptions, dosages, and refill details via a simple QR flow and receive real-time updates when medications are dispensed or canceled. All data is encrypted to preserve privacy. For Admins Decentralized credentialing system allows only verified healthcare professionals to issue prescriptions. Soul-Bound Tokens (SBTs) represent verified identities, with multi-signature governance ensuring secure and auditable actions. In essence, MedChain eliminates prescription fraud and paperwork bottlenecks while preserving the doctor–pharmacist–patient trust loop. How we built it We built MedChain as a fully decentralized dApp with no traditional backend or centralized database. Every interaction occurs on the blockchain or decentralized storage. Frontend: Next.js 15 (App Router) and OnChainKit for wallet connection, decentralized identity, and passkey UX. Accounts & UX: Base Accounts (smart accounts) with account abstraction enable passkey sign-in and gasless transactions via a paymaster; users don’t need a traditional wallet. Blockchain: All prescriptions and credentials are stored on the Base L2. Smart Contracts: Foundry-based contracts for the Prescription Registry and Credential SBT logic. Data Storage: Sensitive prescription details (encrypted) on IPFS via Pinata. Web3 Libraries: Wagmi and Viem for Ethereum interactions and transaction lifecycle. Architecture: Entirely client-side — the blockchain acts as the backend, providing both state and verification logic. The result is a secure, scalable architecture that treats the blockchain itself as the database, with walletless, gasless participation for end users. Challenges we ran into Eliminating the backend required a complete rethinking of traditional CRUD operations and caching strategies. Protecting patient privacy on a public ledger meant implementing robust end-to-end encryption before uploading data to IPFS. Creating a credential layer for healthcare providers using Soul-Bound Tokens involved careful contract design and governance logic. Designing a walletless, gasless flow required integrating Base Accounts, passkeys, and a paymaster — including session policies and sponsorship limits — while keeping the UX simple for non-crypto users. Accomplishments that we’re proud of Built a completely backend-less healthcare platform that runs entirely on Base blockchain. Implemented end-to-end prescription verification with cryptographic signing, QR-based sharing, and on-chain auditability. Developed a decentralized credential system using Soul-Bound Tokens to represent verified medical professionals. Delivered a walletless, gasless UX using Base Accounts + passkeys and account abstraction — no seed phrases, no gas fees for patients. What we learned This project taught us that trust is the ultimate currency in healthcare, and blockchain is uniquely positioned to protect it. We learned how to design for both decentralization and usability, balancing cryptographic rigor with human-centered design. We also deepened our understanding of Layer-2 scalability, multi-signature governance, account abstraction, and decentralized identity models like SBTs. What’s next for MedChain Regulatory Integration: Collaborate with healthcare compliance bodies to align MedChain with HIPAA and FDA digital health standards. Cross-Chain Expansion: Extend to multi-chain ecosystems for interoperability with electronic health record systems. AI-Assisted Insights: Integrate on-chain analytics to detect prescription trends or potential over-prescription patterns. Real-World Pilots: Partner with clinics and pharmacies to test blockchain-based prescription issuance in controlled environments. AA Operations: Mature our paymaster policies (rate limits, spend caps) and session keys for scalable, secure gas sponsorship. MedChain’s long-term vision is to become the trust layer for digital healthcare records, ensuring that prescriptions are secure, verifiable, and universally accessible — walletless and gasless — powered by Base. <div