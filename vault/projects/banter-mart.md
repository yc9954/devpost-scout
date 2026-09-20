---
slug: "banter-mart"
url: "https://devpost.com/software/banter-mart"
title: "Banter Mart"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 656
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Banter Mart

> Humans swipe, agents type.

[Devpost](https://devpost.com/software/banter-mart) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]] [[realtime_stream]]
**domain** [[finance_payments]]
**user** [[developer]]
**substrate** [[geospatial]] [[video_visual]] [[web_dom]]

**stack** css, gemini, react, supabase, supabase-edge-functions, viem, vite, world, world-minikit, worldcoin-agentkit, worldid

## How they structured the write-up

- inspiration
- banter mart
- how it works
- why we built with world id
- tech stack
- challenges
- what's next for banter mart

## Body

Inspiration Online marketplaces in 2026: Bots are everywhere. Agreeing on price is cumbersome and time consuming. It is not a fun user experience for buyers or sellers. We believe agentic commerce has the potential to help both sides. Platforms must create trustworthy agents and invent new and lean interfaces for the handoff between human and agent. Banter Mart Using Tools for Humanity's Mini App Kit and proof of human verification we provide a secure marketplace. With a simple swipe, buyers choose cool products. Sellers focus on curating amazing offerings. Human backed agents take over the boring part. They negotiate, finalize and process payments for deals. How it works The sellers uploads a listing with name, photo, category and details of the product The buyer swipes left on products they don't want their agent to pursue. If they swipe right their agents start to negotiate prices in real time using pricing anchors, offer dynamics, and market comps. A proposed deal is brought to buyer and seller. Per one click they explicitly approve or decline . No money ever moves without a human decision. Why we built with World ID World shines as the number of humans in a network grows and the cost of proof of personhood must be kept low. Since sellers don't have the resources to handle verification large scale World's lean proof logic was ideal. World also enabled us to pay seamlessly through agents in USDC via MiniKit Pay Every buyer and seller is a World ID–verified real human . The level of trust brought by world app draws sellers who need to adapt to the beginning of agentic commerce. Tech Stack Frontend -React 18.3.1 + Vite 5: mobile-first, app-like feel with Tinder-inspired swipe -React Router DOM 6: client-side routing across Discover, Sell, Profile, and ListingDetail -@worldcoin/minikit-js: wallet-based sign-in (MiniKit.walletAuth), Orb-verified World ID status, and USDC payments initiated from inside World App. -@supabase/supabase-js (browser client): direct reads on listings, negotiations, negotiation messages and image uploads Backend -Google Gemini 2.0 Flash: the negotiation reasoning model, called from the Edge Functions with a strict JSON schema (action, price, message, reasoning, summary). Deterministic step-down fallback to less powerful models kicks in on quota errors. See supabase/functions/_shared/gemini.ts lines 210–220, 419–552. -World App + MiniKit: USDC payment commands are issued from the client and verified on-chain. Authoritative identity is the walletAddress returned from walletAuth, which is what the backend keys negotiations on (buyer_wallet, seller_wallet). -Supabase Postgres, Realtime, Storage, Edge Functions (Deno) Challenges - Getting the AI to stay in bounds. LLMs want to be helpful and agreeable — which means without strict prompting they'd just accept any counter immediately. We had to engineer the system prompt carefully, for example with hard JSON schema enforcement. - Keeping humans in control without adding friction. Users need to feel like the AI is a tool they wield, not an autonomous agent spending their money. The one click Approve & Pay , was non-negotiable. Getting that flow to feel natural rather than annoying took iteration. - Realtime sync between two parties. Supabase Realtime made the live message feed possible, but managing subscriptions cleanly buyers subscribing to negotiation updates, sellers subscribing to new messages on their listings without memory leaks or stale closures in React required careful cleanup logic. - World App constraints. Building inside a MiniKit mini-app means the entire experience lives in a sandboxed WebView. MiniKit.isInstalled() gating, wallet auth nonces, and USDC payment flows all had to be tested against the actual World App environment rather than a standard browser. - Making the UI minimalistic and fun to use for buyers What's next for Banter Mart Smarter discovery: Personalized recommendations based on user swipes, behavior, and past negotiations. Seller insights: Give sellers visibility into how agents interact with their listings and what drives conversions. Stronger negotiation agents: Improve pricing strategy, reasoning, and adaptability in real-time conversations. User-trained agents: Let users shape agents to match their personality and decision style (“AI twin”). <div