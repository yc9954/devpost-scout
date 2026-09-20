---
slug: "passa"
url: "https://devpost.com/software/passa"
title: "Passapay"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 706
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# Passapay

> Founded in 2025, Passapay emerged from a simple observation: event ticketing was broken. Fraud, scalping, and poor user experiences plagued the industry. We knew there had to be a better way.

[Devpost](https://devpost.com/software/passa) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]] [[immigration_refugee]]
**substrate** [[financial_record]] [[structured_db]]

**stack** metamask, mongodb, moonbase, typescript

## How they structured the write-up

- what inspired this project
- the build journey
- challenges faced
- what's next
- why this matters

## Body

PassaPay - Project Story What Inspired This Project The music industry in Africa has always been vibrant, but getting paid as an artist? That's a different story. We've seen talented musicians wait months for payment after a gig, dealing with middlemen, unclear contracts, and sometimes getting nothing at all. Promoters aren't always the bad guys, they face their own challenges with payment transparency and trust issues. We wanted to build something that could actually help. Not another platform that promises the world but delivers complexity. Just a straightforward way for promoters to pay artists, with everything recorded on-chain so there's no "the payment got lost" excuses. The Build Journey Starting Point We began with the core problem: how do you make crypto payments feel as simple as sending money to a friend? The answer wasn't just about the blockchain tech, it was about the interface. If my non-technical friends couldn't figure it out in 30 seconds, it wasn't good enough. Technical Stack The project runs on: Next.js 15 for the frontend (because server components are genuinely useful) Polkadot SDK for blockchain integration Smart contracts on Moonbase Alpha testnet for escrow payments MongoDB for off-chain data (user profiles, transaction history) MetaMask for wallet connections Key Features Built For Promoters: Dashboard showing real-time balance from the blockchain Artist search and payment system Smart contract integration for secure payments with 2.5% platform fee Transaction history pulled directly from the database For Artists: Claim pending payments from smart contracts View earnings and transaction history Profile management The Payment Flow: Promoter creates payment through smart contract Funds locked in escrow with 7-day claim window Artist claims payment (gets 97.5% after platform fee) Everything recorded on-chain and in database for quick lookups What we Learned Blockchain isn't scary, but it's particular: We spent way too long debugging why transactions weren't showing up, only to realize we were comparing addresses with different cases (0xABC vs 0xabc). Now we normalize everything to lowercase. Small lesson, big impact. Mobile-first actually means mobile-first: The dashboard looked great on my laptop. On my phone? Horizontal scrolling nightmare. We had to rebuild the entire layout system, adding proper overflow handling and responsive breakpoints. Now it works on a 320px screen. Type safety saves time: TypeScript kept yelling at me about the Transaction type being defined in multiple places. We ignored it for a while, then spent an hour fixing type conflicts. Created one shared type definition, problem solved. Should've listened earlier. Challenges Faced The MetaMask Connection Dance Getting MetaMask to connect reliably was harder than expected. Sometimes it would connect, sometimes it wouldn't. Sometimes it would connect but not return the account. We ended up building a custom hook that handles all the edge cases and stores the connection state properly. Smart Contract Events Reading events from the smart contract to get the payment ID was tricky. The event logs come back as hex strings, and you need to know exactly which topic contains what data. Took us a few tries to get the PaymentCreated event parsing right. Database vs Blockchain Deciding what goes on-chain vs what stays in the database was interesting. Payments? On-chain. User profiles? Database. Transaction history? Both blockchain for truth, database for speed. The trick was keeping them in sync without making everything slow. Type Conflicts TypeScript was throwing errors about "two different types with this name exist" for the Transaction interface. Turns out we had defined it separately in four different files. We created a shared types folder and imported from there. What's Next The platform works, but there's room to grow: Add support for multiple currencies (USDC, DOT) Implement dispute resolution for contested payments Build a rating system for both artists and promoters Add automated payment scheduling for recurring gigs Mobile app using React Native Why This Matters In many African countries, traditional banking is slow and expensive for cross-border payments. Crypto can actually solve this, not as a speculative investment, but as a tool. PassaPay shows that blockchain payments can be simple enough for everyday use. The goal isn't to replace everything with crypto. It's to give artists and promoters a better option when they need it. One that's transparent, fast, and doesn't require trusting a middleman with your money. <div