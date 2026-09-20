---
slug: "nearmint"
url: "https://devpost.com/software/nearmint"
title: "NearMint"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 475
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/financial_record"
---

# NearMint

> NearMint is the first Web3 pawn shop that tokenizes physical collectibles, turning a $500B illiquid market into liquid assets, with seamless fiat onboarding via ChipiPay for LatAm users.

[Devpost](https://devpost.com/software/nearmint) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[finance_payments]]
  <sub>weak: government_staff</sub>
**substrate** [[financial_record]]

**stack** account-abstraction, cairo, chipi-stack, chipipay-sdk, clerk, css, figma, git, github, javascript, next.js, node.js, react, restful

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nearmint

## Body

Logo NearMint: Revolutionizing Collectibles Liquidity in LATAM Inspiration NearMint emerged from observing three critical problems in LATAM: the lack of trust in traditional pawn shops due to opaque pricing and questionable authentication practices, the difficult access to credit for the massive unbanked population, and the poor liquidity in physical collectibles markets where valuable assets remain illiquid for extended periods. We saw the opportunity to solve these interconnected financial challenges through blockchain innovation. What it does NearMint tokenizes physical collectibles with real backing . Through our platform, collectors can send their physical items to our secure Vaults and receive RWA tokens that represent verifiable ownership. Investors gain diversified access to the collectibles market and earn yield by lending to collectors. The system automatically handles RWA generation, migration, and elimination based on client needs, with Cairo smart contracts ensuring complete transparency in pricing and authentication for massive LATAM onboarding, where users can participate completely without knowing they're onchain . How we built it We built NearMint leveraging Starknet's unique capabilities : Native account abstraction for frictionless user experience Ultra-low fees for economic viability Inherited Ethereum security We developed Cairo smart contracts that handle RWA tokenization, digital custody, and lending mechanisms. ChipiPay SDK integration enables instant LATAM onboarding using familiar payment methods. We implemented a virtual Vault system with authentication and custody protocols, connected to smart contracts that update RWA states in real-time. The multicall architecture optimizes batch transactions, while paymasters eliminate gas fee friction for end users. Challenges we ran into The main challenge was balancing UX simplicity with the inherent complexity of physical collectibles custody. We had to design robust authentication protocols that inviolably connect physical items with digital tokens. Another significant challenge was integrating ChipiPay SDK while maintaining complete blockchain abstraction for non-technical users. Accomplishments that we're proud of We achieved a solution that genuinely democratizes liquidity access for LATAM collectors, leveraging Starknet's world-class infrastructure. Our ChipiPay integration completely eliminates technical barriers - users can tokenize collectibles using familiar payment methods without directly interacting with wallets or crypto concepts. The Cairo smart contracts we developed automatically handle complex cases like: Ownership fractionalization Yield distribution Lending mechanisms Most importantly, we created a sustainable business model with multiple revenue streams that benefits both collectors and investors. What we learned We learned that true Web3 mass adoption in LATAM requires complete abstraction of technical complexity, not just simplification. Account Abstraction is fundamental to this. We also discovered that the RWA market needs solid bridges between physical and digital assets - not just purely digital representations. What's next for NearMint Our post-hackathon roadmap includes: Expanding to physical Vault ecosystems in other major LATAM cities, starting with Mexico City, Bogotá, and São Paulo Integrating decentralized oracles for dynamic collectibles pricing Implementing advanced DeFi features like yield farming with RWA tokens Building partnerships with traditional auction houses and financial institutions <div