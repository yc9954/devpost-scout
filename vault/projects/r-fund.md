---
slug: "r-fund"
url: "https://devpost.com/software/r-fund"
title: "PeerFund"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 546
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# PeerFund

> A decentralized peer-to-peer lending platform built on the XRP Ledger (XRPL), enabling university students and individuals to lend and borrow funds with transparent, blockchain-backed transactions.

[Devpost](https://devpost.com/software/r-fund) · hackathon [[Cal Hacks 12.0]]

## Facets

**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[financial_record]] [[geospatial]] [[structured_db]]

**stack** blockchain, firebase, nextjs, xrpl

## How they structured the write-up

- inspiration
- what it does
- how it’s built
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for peerfund

## Body

Pay back money Contribute money to the Pool Landing page Signing into PeerFund with edu email Borrower Dashboard Lender Dashboard Inspiration College students often struggle to access fair credit — traditional banks deny small loans and payday lenders trap people in predatory cycles. Meanwhile, plenty of students have savings sitting idle, earning near zero interest. We asked ourselves: What if we let students support each other directly — safely, transparently, and with real financial upside? PeerFund enables a win-win system where students can fund each other using a secure blockchain, eliminating middlemen and complexity. ⸻ What It Does PeerFund is a peer-to-peer lending platform built on the XRP Ledger that: ✅ Allows students to lend money and earn interest ✅ Enables borrowers to request loans with predictable repayment schedules ✅ Uses XRPL blockchain transactions for transparency + trust ✅ Automates matching between lenders and borrowers ✅ Tracks user credit reputation over time Every payment — funding, disbursement, repayment, and payout — is recorded on-chain with structured memos for auditability. ⸻ How It’s Built Frontend • Next.js 14 + React + MUI for a clean, animated UI • React Query for realtime data and mutation flows Backend • Next.js API Routes (serverless) • Firebase Auth + Firestore for user and loan data Blockchain • XRPL.js with on-chain payments for: • Funding commitments (user-signed) • Loan disbursements (server-signed) • Loan repayments (user-signed) • Lender payouts (server-signed) • Secure collector wallet for automated settlement • Memos used to synchronize blockchain + database state We also created a detailed matching system architecture for future automation: • Automated loan funding (matcher cron) • Expired reservation cleanup • Payout distribution to lenders • Default detection and risk scoring ⸻ Challenges We Ran Into • Crafting a complete blockchain flow without smart contracts • Making on-chain/off-chain states idempotent and reconcilable • Wallet integration UX (reducing friction for new crypto users) • Designing a fair matching engine with all-or-nothing funding • Coordinating funding → disbursement → repayment → payout without race conditions • Finishing a complex financial system under hackathon time pressure ⏳ ⸻ Accomplishments That We’re Proud Of • We built a real lending marketplace, not just a prototype UI • Every financial event flows through the XRP Ledger • Fully functional lender and borrower dashboards • Secure wallet-linked authentication • Dynamic interest rates with clean visual design • Production-grade specs for matching + distribution pipelines • A polished user experience in just 36 hours ⸻ What We Learned • How to combine server-signed + user-signed XRPL transactions • Designing reversible financial systems is non-trivial • Hustling UX polish while building blockchain infra is… ambitious 😅 • The power of structured memos for traceable financial history • The importance of idempotency when listening to blockchain events • How to design an economic system that is fair and automated ⸻ What’s Next for PeerFund 🔜 Deploy smart matching scheduler to automate loan funding 🔜 Smart distribution system for lender payouts 🔜 Live wallet connection (Xaman + Crossmark integrations) 🔜 Offer identity-based credit scoring 🔜 Expand to more schools and verified student networks 🔜 Mobile-first app + QR-powered deep linking 🔜 Eventually support mainnet deployment with real liquidity pools Our long-term vision: A trustless micro-finance network where students fund their future — together. ⸻ <div