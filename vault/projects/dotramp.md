---
slug: "dotramp"
url: "https://devpost.com/software/dotramp"
title: "DotRamp"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 611
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/regulation_legal_text"
---

# DotRamp

> Using Mpesa or local currency, Dot Ramp enables users to on- and off-ramp DOT and other tokens on Polkadot. It expands easy Web3 access and is quick, safe, and a plug-in infrastructure for other apps.

[Devpost](https://devpost.com/software/dotramp) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[provenance_signing]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]] [[retail_commerce]]
**user** [[developer]] [[small_business]]
**substrate** [[financial_record]] [[regulation_legal_text]]

**stack** ink, nextjs, node.js, paseo, polkadot

## How they structured the write-up

- inspiration
- what it does
- how it was built
- minimal wallet knowledge needed
- challenges faced
- achievements & milestones
- key learnings
- roadmap and milestones

## Body

Main view Inspiration Dot Ramp was born from real-world demand for simple, safe conversion between fiat and crypto, in an environment where technical barriers, compliance risks, and manual processes slow adoption. The goal: create an infrastructure enabling payments and onramps/offramps that anyone can use, regardless of blockchain expertise. What It Does Dot Ramp offers fiat-to-crypto and crypto-to-fiat exchange infrastructure. The platform focuses on Kenya with M-Pesa integration, supporting DOT and stablecoins. Each milestone reduces friction through fast settlements (often under 30 seconds), direct bank or mobile wallet payouts, and seamless integration for B2C and third-party applications. How It Was Built Dot Ramp’s modular system is designed for deep integration with Polkadot-compatible wallets. It uses a secure backend and local payment integrations to handle wallet authentication, transaction signing, and settlement, while abstracting the underlying blockchain complexity. By leveraging the official Polkadot.js API stack, the platform ensures compatibility across a range of wallets, including Talisman, Polkadot.js, SubWallet, and others, so users can interact smoothly with their preferred wallet. Each step prioritizes compliance, user trust, and reliability, ensuring fast, secure, and familiar transaction experiences for all users.[web:68][web:71] Minimal Wallet Knowledge Needed Users only need basic familiarity with the supported wallets. This includes knowing how to connect their wallet (for example, Talisman, Polkadot.js, SubWallet, Nova, or others), access their wallet address, and confirm or approve transactions. All advanced blockchain operations, like cryptographic signing or private key management, are handled by Dot Ramp’s user interface and wallet integrations, allowing users to transact with confidence and ease, even if they are not blockchain experts. Challenges Faced Making advanced blockchain processes invisible to mainstream users through wallet support, seamless payment rails, and a familiar user experience. Navigating changing financial regulations and embedding compliance requirements such as KYC, AML, and reporting directly into the platform’s architecture. Designing scalable networks for business and developer integrations, enabling partners to build quickly atop the protocol. Achievements & Milestones Instant Conversion: Achieved near-instant fiat-crypto swaps with M-Pesa via decentralized networks. Embedded Compliance: Integrated KYC, attestation, and regulatory reporting for safety. Crypto-Free UX: Delivered user experiences that hide technical details—users need minimal wallet knowledge. Integration Ecosystem: Enabled apps and businesses to easily add fiat/crypto exchange support through APIs, smart contract interfaces, or direct protocol connections. Zero-Fee Experience: Reached the milestone of zero sender fees, providing competitive rates and flexible fee models. Global Expansion: Built support for multi-currency, multi-chain, and new digital asset protocols. Key Learnings Accessibility drives adoption: simplifying user flows, payment options, and compliance is essential. Reliable infrastructure, rapid settlement, and a transparent user experience are crucial for real-world Web3 growth. Roadmap and Milestones Immediate (V1) Complete system development for fiat-to-crypto and crypto-to-fiat transactions. Integrate local payment methods (M-Pesa for Kenya). Seamlessly connect with Polkadot-compatible wallets (Talisman, Polkadot.js, SubWallet, Nova, etc.). Provide intuitive user flows, requiring only minimal wallet knowledge for interaction. Conduct comprehensive functionality and user experience testing on the Paseo testnet (which supports the Passet Hub, Polkadot's dedicated asset hub for pre-mainnet deployment and QA) Deploy Dot Ramp to the Polkadot mainnet, specifically targeting the Asset Hub parachain for cost-efficient and standardized asset operations within the broader Polkadot ecosystem Medium-Term Broaden payment rails to include Nigeria, Uganda, Tanzania, and Rwanda, integrating mobile money and instant payment systems to expand regional reach. Expand protocol decentralization with multiple aggregators, permissionless participation, and unified full-stack nodes. Strengthen compliance and KYC/AML integrations for multi-jurisdiction support. Harden the system through audits and advanced security reviews. Long-Term / Advanced Launch cross-chain swaps and unlock advanced DeFi features using Asset Hub’s cross-chain capabilities. Release merchant tools for advanced crypto acceptance and robust transaction management. Invest in education and community programs to build user awareness and facilitate adoption. <div