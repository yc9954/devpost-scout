---
slug: "ripplerelief"
url: "https://devpost.com/software/ripplerelief"
title: "RippleRelief"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 830
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "domain/security_privacy"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# RippleRelief

> Every donation, tracked and trusted.

[Devpost](https://devpost.com/software/ripplerelief) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[disaster_emergency]] [[finance_payments]] [[retail_commerce]] [[security_privacy]]
**user** [[small_business]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** flask, javascript, node.js, python, react-native, ripple, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ripplerelief

## Body

Donor Dashboard Donor Stripe Payment Donor Payment Completed Recipient Checkout NGO Dashboard Biometric Face Verification Systems Design Inspiration When disasters strike, billions in aid are pledged, but much of it never reaches the people who need it most. Funds are delayed, misused, or lost in bureaucracy. As a team, we asked: What if every donor could see their impact, and every recipient could trust the system delivering it? This inspired us to build RippleRelief, a transparent aid ecosystem powered by the XRP Ledger (XRPL) . What it does RippleRelief is a web app that connects donors, NGOs, recipients, and merchants in a transparent aid ecosystem: Donors contribute funds to a pooled XRPL wallet. NGOs issue digital vouchers (IOUs) directly on XRPL. Recipients receive those vouchers as QR/SMS codes. Merchants redeem vouchers instantly for stablecoins/XRP. The web app includes a donor dashboard (to track impact), NGO interface (to issue and manage vouchers), and merchant portal (to scan and redeem vouchers). Every step is recorded on XRPL, making the flow auditable and tamper-proof. How we built it Frontend: RippleRelief is a React web app built with Next.js + Tailwind CSS for a responsive, mobile-first interface. We designed separate flows for donors, NGOs, merchants, and recipients, all integrated into one ecosystem. Backend: A Flask server acts as the core API, handling requests from the frontend, connecting to XRPL via the xrpl-py SDK, and managing identity + fraud logic. Blockchain Integration: We used the XRP Ledger (XRPL) for donation tracking, decentralized identifiers (DIDs), and instant settlement. Every transfer is transparent and auditable. Face ID Wallets: Recipients access aid through Face Recognition wallets. We generate encrypted facial embeddings with liveness checks and bind them to wallet keys, ensuring passwordless, fraud-resistant authentication. Payments: Integrated Stripe so donors can give in fiat (credit card, bank, etc.), while each donation is mirrored on XRPL as a transparent, traceable transaction. Database: Chose Supabase for user management, transaction logs, NGO/merchant registries, and fraud detection. Supabase gave us a Postgres backend plus built-in authentication and real-time APIs. Challenges we ran into Biometric wallet access: Implementing Face ID–secured wallets required balancing security vs. privacy. We had to learn about embeddings, liveness checks, and how to keep biometric data off-chain. System integration: Connecting donors, NGOs, recipients, and merchants meant building multiple flows (web app ↔ server ↔ XRPL ↔ Stripe). Ensuring they worked together under hackathon time pressure was a major challenge. Low-tech accessibility: Designing for disaster zones meant building with constraints in mind — intermittent internet, older devices, and non-technical users. Keeping the app simple but secure was harder than expected. Accomplishments that we're proud of Learnt how to build on-chain. It was all of our first times building something with a cryptocurrency! Face ID–secured wallets: Implemented biometric login for recipients, mapping facial features into embeddings for secure, passwordless access to their aid. End-to-end XRPL integration: Built donor → NGO → recipient → merchant flows entirely on the XRP - Ledger, enabling real-time, auditable aid distribution. Hybrid payments: Connected Stripe with XRPL so a fiat donation could be mirrored on-chain as a traceable transaction. What we learned XRPL fundamentals: We learned how to work with the XRP Ledger — from issuing tokens and DIDs to integrating it with traditional payment systems like Stripe — and how it enables transparent, low-cost financial flows. Ecosystem thinking: Instead of designing a single app, we built an ecosystem connecting donors, NGOs, recipients, and merchants. That shift taught us how system design, user flows, and communication between services (web app ↔ server ↔ DB ↔ ledger) all tie together. Biometric identity: We explored face embeddings, liveness checks, and privacy-preserving storage methods, which gave us experience in balancing security and usability for vulnerable populations. Human-centered design: Building for low-tech users in disaster contexts taught us to simplify interfaces, reduce friction, and make design decisions that don’t require people to abandon their existing technology. Fintech + blockchain fusion: We discovered how traditional rails (Stripe) and decentralized rails (XRPL) can complement each other, letting donors transact in fiat but still watch their impact transparently on-chain. Collaboration under pressure: Coordinating system engineering, identity flows, and UI design in such a short time reinforced the importance of communication and iteration in a hackathon setting. What's next for RippleRelief Pilot program with NGOs: Launch a small-scale test deployment with real donors, recipients, and merchants to validate usability and flows. Fraud prevention & compliance: Auto fraud detection using anomaly detection on XRPL transactions. Production-ready Face ID wallets: Improve biometric login with advanced liveness detection, privacy-preserving embeddings, and fallback mechanisms for low-tech users. Donor transparency dashboard: Richer reporting with impact metrics (e.g., meals delivered, aid redeemed) tied directly to transactions on XRPL. Deeper XRPL features: Incorporate NFTs as impact certificates, stablecoin flows for price stability, and escrows for conditional payouts. Low-tech accessibility: Expand SMS/USSD wallet access for disaster zones with limited smartphones or internet. Scaling the ecosystem: From pilot → regional rollout → global network where every aid dollar is traceable, secure, and accountable. <div