---
slug: "notic3"
url: "https://devpost.com/software/notic3"
title: "Notic3."
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 543
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
---

# Notic3.

> The blockchain solution for content creators offering a decentralized platform for creators and users, powered by Sui.

[Devpost](https://devpost.com/software/notic3) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** move, next.js, sui, tailwindcss, typescript, walrus

## How they structured the write-up

- overview
- inspiration
- our approach
- key features
- conclusion

## Body

Featured Creators Content Creator Page Notic3 – A Decentralized Solution for Content Creators Overview Notic3 is a decentralized platform designed to empower content creators, offering a blockchain-based alternative to platforms like Patreon (and that one unholy platform). Our mission is to eliminate intermediaries, giving creators direct access to their supporters while ensuring secure, transparent, and tamper-proof data. Built fully on-chain, Notic3 exemplifies the spirit of decentralization by providing trustless interactions and immutable records. While many blockchain-based projects use off-chain solutions to sidestep technical challenges, our team committed to going all-in on decentralization. This approach presented unique obstacles, but it also set us apart, reinforcing our belief in the transformative potential of blockchain for creative industries. Inspiration Blockchain technology offers more than just financial innovation—it provides a new way to manage ownership, access, and rewards. Inspired by these capabilities, we wanted to build something that could give content creators control over their work and revenue streams without relying on centralized platforms that charge high fees or control the distribution of content. While the Web3 space has already seen some early experiments in creator tools, many platforms are still hybrids—leveraging blockchain partially but retaining centralized components. We wanted to explore what would happen if we stayed true to the core ethos of decentralization. Notic3 was born from that idea: a fully on-chain platform that doesn't compromise on its principles. Our Approach We chose to build Notic3 entirely on-chain to guarantee transparency, immutability, and censorship resistance. This meant every interaction—from subscription payments to content access—would be recorded directly on the blockchain (available to the general public). This decision came with trade-offs: Secure data storage: Managing private files like videos or audio on-chain is insecure if unencrypted, so we had to creatively manage metadata to ensure users are truly accessing content they own. Novelty of Move and Sui: The Move programming language, native to blockchains like Aptos and Sui, was completely new to our team. Learning it on the fly was one of the biggest challenges we faced, in addition to learning about the Sui SDK. Smart Contract Design: Writing complex smart contracts to handle subscription models, creator payouts, and access permissions directly on-chain was difficult. Key Features Subscription-based Payments: Creators can set up recurring subscriptions that allow supporters to access premium content. Payments are processed seamlessly on-chain, ensuring transparency and immediate distribution of funds. Web3 Storage: Everything about our app is in the chain, including the file storage. We utilized Sui's newest Data Storage solution, Walrus, to store encrypted files on the chain using blobs allowing creators to leverage the chain for distribution of their content. Conclusion Working on Notic3 has been an incredible experience. We took on ambitious challenges, and despite the difficulties, we believe we succeeded in delivering a powerful product. Along the way, we learned new technologies, embraced decentralized principles, and grew both as developers and as a team. Notic3 is proof of what can be achieved when you stay true to your mission, even when easier paths are available. We are excited to continue developing the platform beyond the hackathon and see how it can empower creators around the world. Thank you for the opportunity to present Notic3, and we look forward to feedback and collaboration as we continue this journey! <div