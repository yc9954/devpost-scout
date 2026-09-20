---
slug: "waste2wealth-0o4tah"
url: "https://devpost.com/software/waste2wealth-0o4tah"
title: "Waste2Wealth"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 485
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Waste2Wealth

> Turn trash into cash: report litter, clean it up, get paid in Solana.

[Devpost](https://devpost.com/software/waste2wealth-0o4tah) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**domain** [[civic_government]] [[climate_energy]] [[developer_tools]] [[finance_payments]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]]

**stack** cloudinary, react-native, solana, supabase, world-u

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for waste2wealth

## Body

Inspiration Walking past the same pile of garbage for two weeks straight made us ask, why does nobody clean this? The answer was simple: there's no incentive. Existing apps like SeeClickFix have <5% completion rates. Reports go in, nothing comes out. We wanted to fix that with crypto rewards and community accountability. What it does Waste2Wealth is a mobile app where you earn Solana crypto for cleaning your city. Snap a photo of garbage → someone nearby claims it and cleans it → the community votes it's real → everyone gets paid automatically on-chain. Every photo is verified by Cloudinary AI. Every account is gated by World ID. No fakes. No bots. Just cleaner streets and real rewards. Reporter: 0.01 SOL · Cleaner: 0.10 SOL · Verifier: 0.005 SOL each How we built it React Native (Expo) : mobile-first, single codebase, no web companion Cloudinary AI Vision : natural language prompts verify every photo ( "Is there actual garbage here?" , "Has it been cleaned?" ) World ID (IDKit) : one real human = one account, cryptographically enforced Solana devnet : micro-payments with near-zero fees Supabase + PostGIS : real-time map pins and geo-based push notifications FastAPI : backend consensus engine, reward distribution, geofence routing Challenges we ran into World ID on React Native : IDKit's bridge API has changed multiple times across versions; required real-device testing before writing a single screen Cloudinary AI Vision quota : 2–3 API calls per report burns through the free trial fast; had to mock Vision in dev and save live calls for the demo Solana polyfills in Expo : @solana/web3.js needs 3 specific polyfills in index.js or the wallet silently fails on device with no error GPS drift indoors : had to loosen the proximity check from 50m → 200m for the hackathon venue Accomplishments that we're proud of Built a full 3-sided crypto economy in 36 hours that's actually cheat-proof Cloudinary AI Vision acts as a transparent trust layer : the AI's reasoning is published in-app, not hidden in a black box 5 distinct Cloudinary surfaces in one mobile app: AI Vision, Envision Clean, comparison slider, background removal, auto-tagged gallery Zero fake accounts possible: World ID makes the whole economy viable What we learned Crypto micro-payments only work at scale on Solana , Ethereum gas fees would exceed the reward itself The hardest part of any incentive system isn't the reward, it's the anti-cheat Cloudinary AI Vision answering questions in plain English is a fundamentally better trust story than any on-device ML model we could have shipped What's next for Waste2Wealth City partnerships : municipalities pay into the reward pool instead of spending $500M/year on cleanup crews Reputation leaderboards : top cleaners get featured, building civic identity World Chain deployment : move escrow on-chain for full decentralization Carbon credit integration : every verified cleanup generates a tokenized carbon offset, adding a second revenue stream for cleaners <div