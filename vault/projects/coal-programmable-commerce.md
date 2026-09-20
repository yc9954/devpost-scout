---
slug: "coal-programmable-commerce"
url: "https://devpost.com/software/coal-programmable-commerce"
title: "Coal - Programmable Commerce"
hackathon: "MNEE Hackathon: Programmable Money for Agents, Commerce, and Automated Finance"
organization: "MNEE, LLC"
winner: true
words: 572
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "user/developer"
  - "user/small_business"
  - "substrate/financial_record"
---

# Coal - Programmable Commerce

> Coal is the programmable commerce layer for the MNEE ecosystem. Accept stablecoin payments, automate revenue splits, and integrate via a single API, no smart contracts required.

[Devpost](https://devpost.com/software/coal-programmable-commerce) · hackathon [[MNEE Hackathon- Programmable Money for Agents- Commerce- and Automated Finance]]

## Facets

  <sub>weak: cross_origin_web, realtime_stream</sub>
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]] [[retail_commerce]]
**user** [[developer]] [[small_business]]
**substrate** [[financial_record]]
  <sub>weak: geospatial, structured_db, video_visual</sub>

**stack** alchemyapi, better-auth, framer-motion, iconsax, mnee-sdk, next.js, postgresql, prisma, tailwind-css, typescript, uploadthing, vercel, viem, wagmi

## How they structured the write-up

- additional info

## Body

Inspiration Crypto payments are often stuck in two extremes: raw wallet transfers that lack metadata and context, or complex smart contract protocols that are expensive to deploy, audit, and use. We wanted to build the "Stripe" experience for the MNEE stablecoin, empowering developers to accept payments, handle complex revenue splits (e.g., platforms taking a fee), and manage products without writing a single line of Solidity. We saw competitors building "bridges" (like Gravity), focusing on accepting any token. We decided to focus on programmability and business logic , building a bank for developers rather than just a pipe for assets. What it does Coal is a comprehensive payment infrastructure that bridges Web2 commerce with MNEE settlement: Programmable Checkouts : Create transient checkout sessions via API with defined amounts, strict expiry, and custom metadata. Automatic Revenue Splits : Define splits in your API payload. When a user pays, Coal handles the logic to route funds to the merchant, the platform, and other stakeholders instantly. Merchant Console : A full dashboard to manage Products, API Keys, and view real-time Transaction analytics. No-Code Payment Links : Generate shareable links for products or flexible donations in seconds. Robust Verification : A background reliability system that monitors the blockchain for transaction finality, ensuring no payment is ever missed even if the user closes their tab. How we built it We architected Coal as a high-performance Backend-for-Frontend system: Frontend : Built with Next.js 16 (App Router) and React 19 , styled with Tailwind CSS . We utilized Framer Motion to create a premium, "glass-morphic" aesthetic that feels alive processing data. Backend & API : A separate Next.js service acts as our secure API gateway. It handles API Key authentication, communicates with our PostgreSQL database (via Prisma ORM ), and manages the checkout lifecycle. Blockchain Integration : We utilized the MNEE SDK , Wagmi , and Viem for wallet connections and deeply integrated RPC calls to verify transactions on-chain. Assets : We used UploadThing for seamless product image hosting. Challenges we ran into The biggest challenge was the state mismatch between Web2 (HTTP request/response) and Web3 (Async Blockchain state). Users would often pay and immediately close the tab before our frontend could confirm the transaction hash. We solved this by implementing an "optimistic" verification flow and a background "sweeper" worker. We also had to solve cross-origin cookie issues between our separate frontend and backend deployments, which required a carefully tuned middleware and CORS configuration. Accomplishments that we're proud of The "Splits" Logic : Successfully enabling multi-party payouts in a single checkout flow without a smart contract. The UX : Achieving a checkout experience that feels as fast and polished as a Web2 standard like Stripe Link. Reliability : Hitting 100% payment detection in our stress tests thanks to the background worker. What we learned We learned that the power of stablecoins like MNEE isn't just in "sending money"—it's in the metadata and programmability you can wrap around that transaction. By treating the blockchain as the settlement layer and our API as the logic layer, we unlocked a much better developer experience. Built with Next.js, TypeScript, Tailwind CSS, Prisma, PostgreSQL, Wagmi, Viem, MNEE SDK, UploadThing, Vercel, Framer Motion, Better Auth, Iconsax. Additional Info Try it out : https://www.usecoal.xyz Public Repo : https://github.com/emmanuel39hanks/coal-mnee-submission Updates (if applicable) This is a fresh submission built entirely during the hackathon. We implemented the Core API, Merchant Console, Checkout UI, and Background Verification system from scratch. <div