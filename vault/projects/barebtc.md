---
slug: "barebtc"
url: "https://devpost.com/software/barebtc"
title: "BareBtc"
hackathon: "Bitcoin 2025 Official Hackathon"
organization: "Bitcoin++"
winner: true
words: 637
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/accessibility"
  - "domain/finance_payments"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# BareBtc

> “Let your Bitcoin history speak for your future.” Undercollateralized credit. Powered by sBTC. Designed for hyperbitcoinization and built for the entrepreneurs of the world.

[Devpost](https://devpost.com/software/barebtc) · hackathon [[Bitcoin 2025 Official Hackathon]]

## Facets

**domain** [[accessibility]] [[finance_payments]]
**user** [[small_business]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[web_dom]]

**stack** clarity, nextjs, react

## How they structured the write-up

- 🚀 inspiration
- 🛠️ how we built it
- 📚 what we learned
- ⚠️ challenges we faced
- 🔧 improvements & next steps

## Body

🚀 Inspiration In many parts of the world especially across Africa access to credit remains a major barrier to economic growth. Small businesses and everyday individuals often can't get loans without high collateral, credit history, or bank access. Meanwhile, Bitcoin adoption is rising , but its use is mostly limited to holding or remittance not active economic utility. We asked: What if people could borrow using their sBTC/BTC reputation without selling or locking up their BTC? That question led us to build an undercollateralized lending protocol powered by sBTC designed for global users, but especially impactful for African entrepreneurs. Our goal: To accelerate hyperbitcoinization by turning Bitcoin into not just sound money but a productive economic layer that enables borrowing, lending, and building. 🛠️ How We Built It Our project is powered by sBTC , which gives us the programmability of smart contracts while staying anchored to the Bitcoin ecosystem. Here's how it works: Credit Score Engine : We calculate a user’s credit score using: On-chain activity specifically average sBTC balances across the last 3 months. Repayment history from prior loans. The on-chain activity score is the core of the trust model . For the hackathon, we intentionally made it lightweight to emphasize concept clarity focusing on average balances rather than complex behavioral metrics. This means, for example, that a new user who suddenly receives a large amount of sBTC won't be able to get a loan immediately, they’ll need to wait until the next Stacks block to be eligible. This small delay helps ensure that only sustained activity earns trust, preventing abuse of the system. Borrowing Limit Logic : Users cannot borrow more than their average sBTC balance over the last 3 months a simple but effective signal of financial consistency. Smart Contract Lending Pool : Loans are issued and repaid via smart contracts using sBTC, enabling decentralized execution, risk management, and yield generation for lenders. Frontend Interface : A clean web interface allows users to connect wallets, view their credit score, and request or repay loans. The interface was built with a mobile-first approach , ensuring usability on smartphones— especially important in emerging markets , and in anticipation of Leather's upcoming mobile wallet release . It was also made accessible , with features including proper ARIA roles , semantic HTML , focusable regions , screen-reader-friendly labels , and live status updates for dynamic content. These help ensure an inclusive experience for all users, including those using assistive technologies. 📚 What We Learned The fundamentals of blockchain and decentralized finance (DeFi) How to work with Bitcoin Layer 2 solutions like sBTC The importance of building inclusive, real-world financial tools that support the broader mission of hyperbitcoinization ⚠️ Challenges We Faced This was our first hackathon and our first time learning about blockchain technology , so the learning curve was somewhat steep. While working with Stacks, Clarity and sBTC, we noticed that the documentation wasn't always fully up-to-date with the latest implementations , but overall it was helpful and gave us a solid foundation to build on. 🔧 Improvements & Next Steps Currently, the on-chain activity score is calculated based on a user’s average sBTC balance over the past three months . This approach is simple and effective for now, but there’s room for improvement: Integrating transaction frequency and volume into the score Using reputation staking or social graph metrics to strengthen trust Introducing risk-adjusted loan tiers based on evolving on-chain behavior Creating an oracle or reputation network to decentralize credit scoring further By refining this system, we can create a more accurate, fair, and resilient credit layer crucial infrastructure for a truly hyperbitcoinized world. We believe this project is a step toward hyperbitcoinization , where Bitcoin becomes not just a store of value, but the foundation of a decentralized global economy accessible to anyone, anywhere. <div