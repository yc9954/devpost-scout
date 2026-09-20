---
slug: "truecount"
url: "https://devpost.com/software/truecount"
title: "TrueCount"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 713
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# TrueCount

> Voting outcomes often face backlash. That’s why trust matters. TrueCount keeps every vote secure and permanently recorded on an open ledger, ensuring every choice is counted correctly.

[Devpost](https://devpost.com/software/truecount) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[civic_government]] [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[financial_record]]

**stack** hardhat, rainbowkit, react, solidity, typescript, wagmi

## How they structured the write-up

- inspiration
- what it does
- key features:
- how we built it
- challenges
- what we're proud of
- what we learned
- the future

## Body

Inspiration One of our teammates experienced a moment in student body government where a candidate's votes were reduced by half because a moderator believed she violated a subjective rule. The issue wasn't just the penalty — it was how easily one person's judgment could undermine trust in the entire process. TrueCount was born to fix this. By moving voting on-chain, we eliminate human bias and create a system where trust is placed in code , not moderators. What It Does TrueCount: A Decentralized, Phase-Based Voting System TrueCount is a commit–reveal voting system for communities that need fairness, transparency, and verifiable results. No moderators. No tampering. Every vote is private to remove bias, later revealed and then permanently auditable on-chain. Built on Ethereum using a commit–reveal–finalize flow: 1. Poll Creation Anyone can create a poll with custom options and configurable commit/reveal durations. Smart contracts enforce deadlines and rules without a central authority. 2. Commit Phase Voters pick an option. A random 32-byte salt is generated client-side. The frontend computes a hash: solidity keccak256(encodePacked(option, salt, voter, pollId)) The commitment is submitted on-chain — keeping the actual vote hidden. 3. Reveal Phase Voters resubmit their chosen option along with the salt. The contract verifies the commitment matches the reveal. Invalid reveals are automatically rejected. 4. Finalize Phase Once the reveal window closes, anyone can finalize the poll. The tallies are locked and publicly accessible forever. Key Features: 🔐 Wallet Integration - Seamless connection with RainbowKit and wagmi 📊 Customizable Polls - Flexible options with configurable time windows 🤝 Privacy-First - Votes remain hidden during the commit phase 🔍 Cryptographic Verification - Mathematical proof of vote integrity ✅ Permanent Transparency - Results locked on-chain forever 🎨 Intuitive UX - Real-time phase indicators, countdown timers, and comprehensive error handling How We Built It Smart Contract Architecture: Solidity contracts implementing the commit-reveal scheme with automatic phase transitions Hardhat development environment for testing, compilation, and deployment Ignition deployment modules for consistent contract deployment Frontend Technology: React + TypeScript for type-safe, component-based UI development wagmi + RainbowKit for Web3 wallet connectivity viem for efficient blockchain interactions and transaction handling TailwindCSS for responsive, modern styling Development Workflow: Local Hardhat node for rapid iteration and testing Comprehensive error handling for both on-chain and off-chain failures Client-side salt generation and secure storage using localStorage Real-time phase detection with automatic UI updates Security Considerations: Cryptographic commitments prevent vote manipulation Salt generation ensures vote privacy until the reveal phase to counter voter bias Smart contract validation prevents invalid or duplicate reveals Time-locked phases prevent premature or late submissions Challenges The toughest challenge was balancing vote privacy with decentralization — two contradicting ideas. On the one hand, we wanted an open and transparent system. On the other hand, exposing votes too early could create bias and influence voters mid-election. By using cryptographic salts, we achieve the perfect balance between privacy and transparency . Additionally, setting up faucets and managing wallet keys for testing and building our product was a new experience that required some time and practice. What We're Proud of We're incredibly proud that True Count isn't just a technical demo—it's a solution with genuine real-world impact. By eliminating central authorities, True Count replaces institutional trust with mathematical certainty through transparent, verifiable code. What excites us most is the system's universal scalability. The same cryptographic guarantees that secure a student body election work equally well for community decisions, corporate governance, or international organizations like the UN. Fair voting shouldn't depend on the scale of the election—it should be mathematically guaranteed at every level. What We Learned We learned how to balance privacy with transparency, work with smart contracts, manage wallets and faucets, and design a system that scales from small groups to global communities. The Future Near Roadmap: Layer 2 Deployment - Deploy to Optimism, Arbitrum, or Base for reduced gas costs and faster transactions Enhanced Security - Add multi-signature poll creation for high-stakes community votes Mobile Optimization - Responsive design improvements and mobile wallet integration testing More Decorative Options - Banners, colours, widgets to enhance user experience Long-term Vision: Cross-chain Compatibility - Enable voting on one blockchain with verification on another Governance Framework Integration - Full DAO tooling integration with popular governance platforms Institutional Adoption - Partner with educational institutions, non-profits, and community organizations <div