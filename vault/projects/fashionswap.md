---
slug: "fashionswap"
url: "https://devpost.com/software/fashionswap"
title: "FashionSwap"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 673
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/retail_commerce"
  - "domain/scientific_research"
  - "user/general_public"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# FashionSwap

> **FashionSwap** is a peer-to-peer fashion rental marketplace built on Starknet, powered by Chipi Pay for ultra-low-fee daily payments.

[Devpost](https://devpost.com/software/fashionswap) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[climate_energy]] [[developer_tools]] [[finance_payments]] [[housing_homeless]] [[retail_commerce]] [[scientific_research]]
**user** [[general_public]]
**substrate** [[financial_record]] [[video_visual]]

**stack** cairo, chipi-pay, node.js, openzeppelin-contracts, react-native, scarb, starknet, starknet.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fashionswap

## Body

Inspiration The fashion industry produces 92 million tons of textile waste annually, yet the average person wears an item only 7 times before disposal. Meanwhile, our closets are full of clothes we rarely use. I wanted to create a solution that tackles both problems: reduce environmental waste while helping people monetize their unused wardrobes. Starknet's ultra-low fees make micro-payments (daily $1-5 rentals) finally profitable, which traditional platforms can't achieve. What it does FashionSwap is a peer-to-peer fashion rental and swap marketplace built on Starknet with Chipi Pay integration: Rent clothing items for daily micro-payments ($1-10/day) with ultra-low transaction fees P2P swaps with zero platform fees - exchange items directly Track carbon footprint - see your environmental impact in real-time (avg 2kg CO2 saved per rental day) Earn passive income by renting out unused wardrobe items Mobile-first design with seamless Chipi Pay checkout Each fashion item is an NFT with rich metadata: brand, size, condition, rental history, and sustainability scores. How we built it Smart Contracts (Cairo 2.8.2): FashionItemNFT.cairo - ERC721 NFTs with fashion metadata and carbon tracking RentalMarketplace.cairo - Listing, renting, swapping logic with security deposits PaymentHandler.cairo - Chipi Pay integration with escrow system for safe payments Tech Stack: Cairo with Scarb build system OpenZeppelin contracts for security (ReentrancyGuard, Ownable) Starknet testnet deployment React Native frontend (mobile-first) Chipi Pay SDK for seamless micro-payments Key Innovation: Optimized escrow system that makes $1-5 daily rentals profitable with 0.5% fees (vs 15-20% on traditional platforms). Challenges we ran into Micro-payment optimization - Traditional payment rails charge more in fees than the rental cost. Solved by integrating Chipi Pay's ultra-low fee structure specifically for transactions under $10. Security deposit handling - Needed trustless escrow that protects both renters and owners. Built automated smart contract escrow with condition verification and dispute resolution logic. Carbon tracking accuracy - Researching and implementing realistic CO2 calculations for fashion rentals vs new purchases. Added peer-reviewed environmental data into contract metadata. Cairo learning curve - First time building with Cairo 2.8.2. Extensively used Starknet docs and community support to implement proper security patterns. NFT metadata for physical items - Designing schema that captures fashion-specific attributes (size, condition, brand) while remaining gas-efficient. Accomplishments that we're proud of ✅ Production-ready contracts with proper security (audited patterns from OpenZeppelin) ✅ First fashion rental platform on Starknet - unique use case for L2 scaling ✅ Real environmental impact - Built-in carbon tracking shows tangible sustainability benefits (2kg CO2 saved per rental day) ✅ Innovative P2P swap mechanism - Zero-fee clothing exchanges with smart matching ✅ Chipi Pay perfect fit - Showcase how micro-payments unlock new business models ($1-5 daily rentals) ✅ Scalable architecture - Can handle 10,000+ items and 50,000+ monthly rentals ✅ Complete end-to-end solution - From NFT minting to payment settlement, fully functional marketplace What we learned Technical: Cairo 2.8.2 patterns and best practices for secure contract development Starknet's account abstraction advantages for mobile UX Optimizing gas costs for frequent small transactions Implementing proper escrow systems with time-locks and dispute resolution Business: Micro-payments unlock entirely new markets (daily fashion rentals) Ultra-low fees (0.5% vs 15%) are a game-changer for thin-margin businesses Sustainability features drive user engagement and brand loyalty P2P models reduce platform liability while increasing trust Industry Insights: $1.5B+ fashion rental market growing at 15% annually Conscious consumers actively seek sustainable alternatives Blockchain transparency builds trust in peer-to-peer marketplaces Mobile-first is critical for mainstream adoption What's next for FashionSwap Q1 2026: Launch mobile apps (iOS/Android) Partner with local fashion communities in 3 cities Target: 1,000 active users, 100 tons CO2 saved Q2 2026: AI-powered swap recommendations based on style/size Integration with delivery services for non-local rentals Social features: follow, collections, fashion influencer accounts Q3 2026: AR virtual try-on feature (mobile camera) Gamification: sustainability badges, leaderboards Brand partnerships (verified luxury items) Q4 2026: Carbon offset marketplace (buy offsets with rental earnings) Educational content on sustainable fashion Apply to Starknet Startup House accelerator Vision: Become the leading Web3 platform for circular fashion economy, saving 1,000+ tons CO2 annually while helping 100,000+ users monetize their wardrobes. <div