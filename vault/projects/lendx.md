---
slug: "lendx"
url: "https://devpost.com/software/lendx"
title: "LendX"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 660
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "user/small_business"
  - "substrate/financial_record"
---

# LendX

> Making SMB lending transparent and efficient with on-chain loan tracking on the XRP Ledger

[Devpost](https://devpost.com/software/lendx) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]] [[finance_payments]] [[immigration_refugee]]
**user** [[small_business]]
**substrate** [[financial_record]]

**stack** auth0, fastapi, python, ripple, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lendx

## Body

Inspiration Financial inclusion remains one of the world's greatest challenges, particularly in emerging markets where traditional banking systems fail to serve billions of people. We were inspired by the potential of decentralized finance (DeFi) to democratize access to credit, especially for small business owners and entrepreneurs in regions like Southeast Asia, Africa, and Latin America. The XRPL's focus on sustainability and low transaction costs made it the perfect blockchain foundation for building a lending platform that could genuinely serve underbanked communities without prohibitive fees. What it does LendX is a full-stack decentralized lending marketplace built on the XRP Ledger that connects lenders and borrowers through peer-to-peer transactions. The platform features: Dual-role dashboard where users can seamlessly switch between lender and borrower views Auth0 Google SSO integration for secure, familiar authentication Native XRPL wallet generation with direct blockchain integration (no third-party dependencies) DID-based identity system using verifiable credentials for borrower verification Lending pool creation where lenders can set custom rates, terms, and requirements Direct loan applications with transparent approval/rejection workflows Real-time transaction tracking with XRPL WebSocket subscriptions Multi-Purpose Token (MPT) support for representing loans as blockchain assets Escrow transactions for secure collateral handling Multi-signature account support for institutional lenders How we built it Our architecture combines a modern React frontend with a robust Python XRPL backend: Frontend (Next.js 14 + TypeScript): Built with App Router and server-side rendering for optimal performance Shadcn/ui component library with custom dark theme styling Direct XRPL.js integration for blockchain interactions Auth0 SDK for Google SSO authentication Zustand for efficient state management Real-time WebSocket connections for transaction updates Backend (Python + FastAPI): Custom XRPL client library built on top of xrpl-py Multi-Purpose Token (MPT) operations for loan tokenization Escrow transaction handling for secure loan collateral Multi-signature account management for institutional use Comprehensive exception handling and logging WebSocket subscription management for real-time updates XRPL Integration: Direct wallet generation replacing Xumm SDK dependency Transaction memoization for loan metadata storage Custom payment flows for lending pool creation and loan distribution Account subscription system for real-time balance updates Challenges we ran into XRPL MPT Documentation: Multi-Purpose Tokens are a relatively new XRPL feature with limited documentation, requiring deep diving into XRPL specifications and extensive testing Transaction Finality: Managing the asynchronous nature of blockchain transactions while providing immediate UI feedback required careful state management Wallet Integration: Replacing third-party wallet dependencies with native XRPL wallet generation while maintaining security best practices Real-time Updates: Implementing WebSocket subscriptions for live transaction monitoring without overwhelming the UI with updates DID Integration: Building a verifiable credentials system that integrates seamlessly with Auth0 authentication Accomplishments that we're proud of Complete end-to-end lending flow from pool creation to loan repayment working on XRPL testnet Professional-grade UI/UX that rivals traditional fintech applications Native XRPL integration without external wallet dependencies, reducing friction for users Comprehensive Python XRPL library with full test coverage for all lending operations Real-time transaction monitoring providing immediate feedback on blockchain state changes Scalable architecture supporting both individual and institutional lenders What we learned The power of XRPL's low transaction fees (fractions of a cent) makes microlending economically viable Multi-Purpose Tokens provide an elegant solution for representing complex financial instruments on-chain Building native blockchain integration significantly improves user experience compared to external wallet dependencies Verifiable credentials combined with traditional OAuth create a powerful identity verification system The importance of real-time feedback in financial applications - users need immediate confirmation of transaction status Python's xrpl-py library is incredibly robust for building production-grade blockchain applications What's next for LendX Mainnet deployment with integrated fiat on/off ramps for emerging market accessibility Credit scoring algorithm using on-chain transaction history and verifiable credentials Insurance pools to protect lenders against default risk Mobile-first PWA optimized for smartphone usage in emerging markets Multi-currency support for local currency lending pools Partnerships with microfinance institutions and business guilds for borrower verification Advanced analytics dashboard for lenders to track portfolio performance Automated loan repayment with scheduled payment systems Cross-border remittance integration for diaspora lending to home countries <div