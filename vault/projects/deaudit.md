---
slug: "deaudit"
url: "https://devpost.com/software/deaudit"
title: "DeAudit"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 833
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "domain/security_privacy"
  - "user/developer"
  - "user/legal_professional"
---

# DeAudit

> A decentralized audit marketplace built on Polygon.

[Devpost](https://devpost.com/software/deaudit) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[finance_payments]] [[security_privacy]]
**user** [[developer]] [[legal_professional]]

**stack** chainlink, chakraui, ipfs, nextjs, sass, vercel, vrf

## How they structured the write-up

- inspiration
- how deaudit works
- tools we used to build it
- challenges we ran into
- what we learned
- what's next for deaudit

## Body

decentralized auditing prove your worth as a security auditor landing page audit profile page user profile page DeAudit - A decentralized Audit marketplace on Polygon Inspiration Owing to the immutable nature of blockchain technology, it is impossible to update the code after its deployment. Placing smart contracts without adequate audits could lead to undesirable situations like differences in the contract's intended performance, gas leakage, etc. 47% of the web3 hacks in the first half of 2022 were due to contract vulnerabilities. Only 52% of the exploited web3 projects were audited. Helps earn users/investors' trust for the product and the idea. Auditing isn't an easy process. Auditing wait times on top audit firms are 9-12 months and are expensive. We need something that is more participative and allows for new and yet-unproven security auditors. This is the motivation behind building DeAudit, a decentralized audit marketplace that turns the auditing process into a prediction marketplace. How DeAudit works 1. Select a jury A jury is usually a reputed security engineer. This jury doesn’t do the audit itself but only signs off a reported vulnerability as a real bug. There are 5 jury members selected for every audit. They control a 3/5 multisig that approves a detected bug once it is reported by an auditor. They receive 5% of the total audit spend. 2. The contract is deployed for auditing The contract must be deployed on-chain to make the code immutable. 3. Pools are created Once the contract is deployed, 2 betting pools are created. Called NoBugs and YesBugs - representing a betting pool that says there are no severe bugs in this contract v/s yes there are bugs in this contract. 4. Pools are equally funded To kick start the marketplace, the person requesting the audit must fund both pools. 5. Auditors audit and fund pools A security auditor looks at the deployed contract and judges whether there are bugs in this contract or not. If they’re confident there are no severe bugs; they may add money to the NoBugs pool. 6. Money starts streaming from YesBugs to NoBugs Until a bug has been reported, the money from the YesBugs pool starts streaming to NoBugs pool, so the YesBugs pool will be exhausted in 30 days. 7a. Bug report If a security engineer finds a bug, they may report it to the jury. The jury will vote with their signature on whether the bug is severe. If the jury accepts the bug as a severe bug, the NoBugs pool is liquidated, and all the money from NoBugs pool is distributed to the people who funded the YesBugs pool. This distribution happens proportionally to When the funder puts money in the YesBugs pool (earlier you make a bet, more is your reward if true) Amount put in as the bet (larger your bet that there are bugs, the more the reward) 5% goes to the jury members equally 7b. No bugs reported If the size of NoBugs pool is greater than 95% of the summation of the pools, the NoBugs pool can be liquidated. All the people who bet that there are no bugs are rewarded by the same ratios presented in 7a. Tools we used to build it Smart contracts were written in Solidity , using Hardhat as the dev environment. Frontend dApp uses Next.js , ChakraUI , Sass , RainbowKit and wagmi.sh . The backend is an express server using Supabase to store data. Challenges we ran into We faced several hurdles while designing and writing the smart contract, integrating it with our frontend, and striking a balance between decentralization and a centralized server. Ultimately, we chose to keep critical data on-chain while entrusting an off-chain server to store additional data. We faced a lot of compile time errors with Solidity while dealing with in-memory arrays and returning data from mappings. Issues on the front end regarding which type of rendering to choose for NextJS for optimization, interacting with write functions and events of the contract, etc, were also some challenges. What we learned In the process of building DeAudit, we learned a lot. Smart contract design, Solidity, dealing with Oracles (Chainlink VRF and Keepers), distributed storage of files (IPFS), decentralized infrastructure (Spheron). We had a lot of fun building it. What's next for DeAudit We've planned a lot of changes and improvements to DeAudit. If the no bugs reported is the pool that won, an NFT is created with the amount of money that was liquidated and the ENS of people on the jury. Specify some background checks for approving a user as a jury member and not allowing anyone to do so randomly. Create a DAO which votes on approving Jury members based on their security profiles. Migrate our frontend DApp to TypeScript . Explore storing additional data (stored in a centralized server for now) to be kept on IPFS. Migrate to foundry for our dev environment. Built @ Polygon BUIDLIT Summer 2022, by @ameya-deshmukh, @priyansh71 & @arihantbansal. Idea Credits madhavanmalolan.eth <div