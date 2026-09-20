---
slug: "betvex"
url: "https://devpost.com/software/betvex"
title: "betVEX"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 741
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "mechanism/structural_withholding"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# betVEX

> betVEX - Community Powered Esports Betting Application. Users are a part of the platform, stakers of $VEX are distributed rewards from the betting contract. Easy onboarding + good odds (low overhead)

[Devpost](https://devpost.com/software/betvex) · hackathon [[-REDACTED- Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]] [[structural_withholding]]
**domain** [[civic_government]] [[finance_payments]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** chain-signatures, javascript, near, near-api-js, nextjs, rust, typescript, wallet-selector

## How they structured the write-up

- problem statement
- solution
- scope
- project goals and future plans

## Body

betVEX Problem statement The current esports betting market is very inefficient due to a lack of competition, which leads to fees as high as 8%. Many platforms are just a money grab extension to an existing traditional betting website with frequent fund lockups and withdrawal delays of 3-5 days Solution betVEX is a next-generation Community-Powered Esports Betting Application that aims to combat these issues in the space. With lower overhead due to autonomous code and a custom parimutuel betting system betVEX can offer vastly lower fees than its competitors undercutting the competition. Instead of all rewards going back to the company, betVEX community members become a part of the platform and share its profit with a revolutionary staking system . With DAO governance the community is a part of VEX and can decide how treasury funds are used to improve the platform and decide how it evolves by, for example, voting on a proposal to change the fees (coming soon). Niche bets coming soon with polymarket-like betting mechanics along with copy betting for enhanced community dynamics. Smart use of account abstraction and relayers handles gas fees and blockchain complexity in the background, keeping the user experience smooth and simple. Esports fans are proven to be fast adopters of new technology making this the perfect market to build in. Scope We are a pre-existing project but have significantly enhanced our platform during this hackathon by modularizing our core components into open source reusable libraries and reference implementations to be used by the community. Building upon our existing betting system and frontend, as part of REDACTED we have: Implemented a unique profit sharing staking system that takes $USDC rewards from matches with profit, swaps them to native $VEX tokens with anti-slippage mechanisms and redistributes these rewards to $VEX stakers . For loss coverage, we utilize a dynamic $USDC* insurance pool with overflow protection through proportional $VEX staker liquidation. Created a frictionless onboarding flow leveraging account abstraction and meta transactions , where users receive a VEX account with zero gas fees , requiring only $USDC or $VEX for betting and staking operations. Vastly improved the frontend that shows current matches, allows users to bet on them, shows the users current bets and allows them to claim them once they are resolved, allows users to interact with the staking system to stake, unstake, and claim rewards, and redistribute rewards for all stakers to enhance decentralization of the platform. We also added a swap in app and a USDC faucet on testnet so users never have to leave the app. Created a database to load images and data for matches to show on the frontend. Upgraded open source onboarding library by developing a flexible self-custody solution that enables applications to seamlessly integrate password-based private key encryption and hierarchical sub-account recovery - all through a customizable plug-and-play library built on near-api-js. Created an example of non-custodial account recovery via chain signatures that anyone can build on top of. Created a reference implementation of a ref finance swap in a contract that outputs the amount swapped, for others to add to their DeFi projects. Project goals and future plans We look to offer the best esports betting experience on the market by leveraging the best of web3 through a web2 onboarding experience and become the number one esports betting application in users by 2027. Betting on esports within crypto is a proven market opportunity with Unikrn reaching a 289m valuation in 2018, even without the ability to onboard the non-crypto native. With NEAR's amazing onboarding through meta transactions, account model, and chain abstraction and a thriving experienced team, we can top this. In the future, we plan to: Add a stake weighted DAO to allow for community governance of the platform. Add verifiable data , match odds, and resolutions are currently done in a centralized manner, we plan to use zk or an oracle to verify these. Implement proper account recovery / account login so users can log in with a username, password, or email through zkemail and chain signatures. Launch VES as an omni token and allow anyone to bet from any chain with chain abstraction. Add niche bets with polymarket-like betting mechanics. Add copy betting to allow users to follow the bets of others without having to sign themselves through chain signatures. On the business side: Our main goal is to raise funds in early 2025. A full roadmap can be found on our website <div