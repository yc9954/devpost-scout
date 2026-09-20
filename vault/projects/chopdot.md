---
slug: "chopdot"
url: "https://devpost.com/software/chopdot"
title: "ChopDot"
hackathon: "Build Resilient Apps with Polkadot Cloud"
organization: "POLKADOT"
winner: true
words: 836
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/structural_withholding"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# ChopDot

> ChopDot is a Polkadot-native group expense app that lets friends create pots, track costs, and settle in DOT in seconds, local-first, non-custodial, and built for real-world groups.

[Devpost](https://devpost.com/software/chopdot) · hackathon [[Build Resilient Apps with Polkadot Cloud]]

## Facets

**mechanism** [[provenance_signing]] [[structural_withholding]]
**domain** [[finance_payments]] [[retail_commerce]]
**user** [[small_business]]
**substrate** [[financial_record]] [[video_visual]]

**stack** api, crust, css, ipfs, network, polkadot.js, postgresql, react, shadcn/ui, supabase, tailwind, typescript, vercel, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chopdot

## Body

Pots Screen Pot Dashboard Pots Overview Settle Overview Settlement Conformation Settlement Screen Pots w/ DOT Inspiration Group money is always messier than it should be. Trips, hackathons, shared flats, pop-up cities – someone pays, screenshots get lost, and three weeks later nobody remembers who actually covered what. We wanted a tool that feels as simple as Splitwise, but is built on rails that are transparent, sovereign, and can’t just disappear with our data. Polkadot’s vision for user sovereignty and the upcoming Polkadot App inspired us to ask: what would a local-first , Web3-native “group money layer” look like if it was actually nice to use? What it does ChopDot is a group expense app built on Polkadot. Create a pot for a trip, hackathon team, or shared flat. Add expenses and see who’s in the red or in the green. When you’re ready, settle with fast on-chain DOT transfers on Polkadot Asset Hub. Log in with Polkadot.js, SubWallet, Talisman, WalletConnect , or email via Supabase. Keep pots and expenses local-first in the browser, with an option to export receipts to IPFS/Crust for decentralized, verifiable proofs. Use a clean, mobile-friendly UI with dark/light mode and a landing-page ready experience at chopdot.xyz. Today’s focus is: make it dead simple for a real-world group to see “who owes what” and close the loop with a real on-chain settlement. How we built it On the frontend we used React + TypeScript with Vite , Tailwind CSS , and shadcn/ui for a fast, modern UI. We designed it mobile-first but kept it fully responsive for desktop. For auth and simple user profiles we used Supabase (email/password and “wallet-as-email” bridging). Pots and expenses currently live in a local-first data layer in the browser so the app feels snappy and resilient even with flaky connectivity. For the chain integration we used @polkadot/api to talk to Polkadot Asset Hub and perform DOT settlements using balances.transferKeepAlive . Wallets connect via Polkadot.js extension , SubWallet , Talisman , and WalletConnect . We also wired an export path for receipts to IPFS/Crust , so we can demonstrate how group proofs could live in decentralized storage beyond ChopDot itself. The whole thing is deployed on Vercel with a separate landing page (chopdot.xyz) and app (app.chopdot.xyz). Challenges we ran into Wallet UX: Supporting multiple Polkadot wallets plus WalletConnect while keeping the login screen simple took iteration. We had to balance “power user” flows with people who have never seen a Polkadot wallet before. Local-first vs shared data: We wanted local-first resilience but also multi-device sync. Designing the data layer so it can later move to Supabase/Postgres without rewriting everything was non-trivial. On-chain vs UX: Exposing real chain interactions (fees, addresses, confirmations) without overwhelming users was tricky. We had to design copy and flows that feel friendly but still honest about what’s happening on Polkadot. Timeboxing scope: It was tempting to jump straight into stablecoins, escrow contracts, and DeFi yields. Staying disciplined and shipping a solid “group pot + DOT settlement” core took effort. Accomplishments that we're proud of A fully working, multi-wallet login + DOT settlement flow on Polkadot Asset Hub. A polished, production-feeling UI that people can actually play with today at app.chopdot.xyz. A local-first architecture that already feels good offline and is ready to grow into a shared backend. A clear “live today vs. next up” roadmap that lines up with Polkadot’s own direction (Polkadot App onboarding, Asset Hub stablecoins, and future smart-contract features). An export path to IPFS/Crust that shows how receipts and proofs can outlive any single app. What we learned How to use Polkadot’s JS API with Asset Hub in a way that feels like a normal app, not a blockchain demo. How much UX work it takes to make Web3 flows feel as simple as Web2 (especially around wallets and fees). The power of local-first thinking : keeping data close to the user first, and only then syncing or uploading. How Polkadot’s upcoming upgrades (asynchronous backing, elastic scaling, Polkadot App) open space for simple, user-facing apps instead of just infrastructure projects. What's next for ChopDot Shared backend data: Move pots/expenses/members from local storage to Supabase/Postgres with realtime sync, so groups can share pots across devices and invitations persist. Polkadot App onboarding: Integrate with the upcoming Polkadot App gifting/identity rails so a new user can create a wallet, receive DOT, and join a ChopDot pot in one guided flow. Stable savings & DeFi yields: Add support for stablecoins on Asset Hub (e.g. USDT/USDC) and plug into parachains like Acala so groups can park shared funds in yield strategies before they settle. Smart-contract escrow & merchant flows: Explore Ink!/PolkaVM contracts for event deposits, QR-based merchant payments, and trustless “ChopPay” style payouts. Full Crust/IPFS audit trail: Index receipts and pot snapshots through Crust so any member (or even an external auditor) can independently verify the history of a group’s expenses. ChopDot is our attempt to make group money coordination effortless, transparent, and sovereign – starting with DOT pots today, and growing alongside Polkadot’s next chapter. <div