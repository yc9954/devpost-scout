---
slug: "oryn-fi"
url: "https://devpost.com/software/oryn-fi"
title: "OneSat"
hackathon: "Starknet Re{Solve} Hackathon"
organization: "Starknet Foundation"
winner: true
words: 559
team_size: 6
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "substrate/structured_db"
---

# OneSat

> One click, one Sat, one journey to yield.

[Devpost](https://devpost.com/software/oryn-fi) · hackathon [[Starknet Re-Solve- Hackathon]]

## Facets

**domain** [[civic_government]] [[developer_tools]]
**substrate** [[structured_db]]

**stack** atomiq, cairo, next.js, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for onesat

## Body

One click, one Sat, one journey to yield Portfolio Page Earning Page Landing page History Page Detailed Earning Pool page Status Modal for Single Click Bitcoin yield. Inspiration There's a clear desire to make Bitcoin productive rather than letting it sit idle. Many users face friction: wrapping, bridging, moving between chains, etc. OneSat wants to reduce that friction (i.e. "no wrapping, no hassle"). The idea is: a seamless, one-click experience from native BTC to yield generation. What it does OneSat is a platform that allows users to deposit native BTC (either via on-chain or via Lightning) and immediately begin earning yield, all in a very streamlined fashion. Here's how it works: Deposit Native BTC — you send BTC (on-chain or Lightning) to OneSat One-Click Bridge — behind the scenes, it handles conversion into Starknet-compatible WBTC (Wrapped BTC) Automatic Yield — the platform deploys that capital into trusted Starknet protocols (the site mentions names like Troves, Endur, Vesu) Withdraw Anytime — users can redeem their yields / withdraw as needed So effectively, OneSat abstracts away the complexity of bridging, wrapping, deploying into yield strategies; users just "click & earn." How we built it We built OneSat using Next.js, typescript, solidity and rust for a clean, responsive, and performant application. The application supports multiple wallets, with a primary focus on Xverse Wallet for both Bitcoin and Starknet connectivity, ensuring seamless user authentication and signing. On the backend, we implemented a Rust-based service connected to an SQL database to handle deposits, user session management, and protocol interactions securely and efficiently. Each user deposit is assigned a unique deposit address (UDA), enabling precise tracking and attribution of funds. We integrated the Atomiq SDK to abstract and perform swaps between native Bitcoin and Starknet-compatible assets, enabling one-click conversions behind the scenes. Yield generation is powered by integrating existing trusted Starknet protocols (like Troves, Endur, and Vesu), automatically deploying user capital for optimized returns. This architecture allowed us to deliver a smooth, end-to-end pipeline — from native BTC deposits to automated yield — all with minimal friction and maximum transparency. Accomplishments that we're proud of Successfully enabling a one-click pipeline from native BTC → yield via Starknet (i.e. removing much of the user friction) Choosing a composable architecture: instead of reinventing yield protocols, leveraging existing trusted ones (Troves, Endur, Vesu) Delivering a UI / UX that is simple (Deposit → Bridge → Yield → Withdraw) and presenting it clearly on the site What we learned Even though bridging, wrapping, yield strategies are "solved" in parts, the biggest value is in abstracting UX friction — users will prefer simple flows Integration with multiple protocols is nontrivial; you must deeply understand each protocol's mechanics, risks, and constraints The interface between Bitcoin (especially Lightning) and smart contract chains (Starknet here) is a key frontier — there is real value in bridging the gap cleanly What's next for OneSat Expand Protocol Integrations — more yield protocols beyond Troves / Endur / Vesu; perhaps also cross-chain yield sources Optimize Efficiency & Gas / Fees — make bridging, wrapping, yield deployment cost and latency minimal Governance / DAO integration — user voting, protocol direction, fee model Support more chains / BTC variants — expand to other L2s or sidechains and Lightning Audit & Security Hardening — before going live with real funds, it's essential to get audits, bug bounties, etc. <div