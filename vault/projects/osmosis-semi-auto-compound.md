---
slug: "osmosis-semi-auto-compound"
url: "https://devpost.com/software/osmosis-semi-auto-compound"
title: "Osmosis (Semi-)Auto Compound"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 448
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/transportation"
  - "substrate/code_repository"
---

# Osmosis (Semi-)Auto Compound

> Automate osmosis pool compounding as much as possible

[Devpost](https://devpost.com/software/osmosis-semi-auto-compound) · hackathon [[Cosmos HackAtom VI]]

## Facets

**domain** [[developer_tools]] [[transportation]]
**substrate** [[code_repository]]

**stack** javascript, keplr, osmosis, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for osmosis auto-compound
- how to try it out

## Body

Inspiration We (used to) have to do the same tedious process every day: deposit staking rewards (e.g. REGEN) Swap half to other currency for equal pool share Join pool Bond LP tokens What it does First, we aimed for a fully auto-compounding smart contract, but soon figured it was not possible without Comsos' soon-to-come Interchain accounts. So we opted to go as far as we could and implement a semi-automatic wizard seamlessly into the osmosis UI. It offers two modes: All-in Take whatever you have of both curriencies, swap (if necessary) so that liquidity is balanced. Select input You select a certain amount of a specific currency, and it will swap half of it to create balanced liquidity (there's also a toggle that allows using available balance of the other currency to reduce or skip swap). In both modes after establishing balanced liquidity, it will then automatically join pool & bond resulting LP tokens . How we built it I forked the osmosis-frontend repo and implemented it while trying to stay close to the existing codebase & building the UI in a way that looks & feels like Osmosis. Then I tried mocking up UI and using existing osmosis functions to perform on-chain actions. When that resulted in a working PoC, I took the time to fully rework UX and flow to accomodate most Personas/Intentions I could think of, and to make the process as seamless as possible. I also made sure relevant choices are persisted in LocalStorage so that the UX is even better Challenges we ran into As mentioned, we failed to implement our initial vision as it requires Cosmos' interchain accounts, which are not ready yet. It also took some time to find my way around the osmosis codebase. Accomplishments that we're proud of Good UX and integration with Osmosis UI, good fault-tolerance & a quick semi-automated process. Smart IBC balances detection. I loved the UX after redesigning & the going the last mile of saving relevant choices in LocalStorage took the seamless feeling of smart automation to another level. I also added some improvements & utils to the Osmosis code, and feel confident to contribute outside of a hackathon context. What we learned Agoric & IBC is waaay harder than it sounds the functionality we dream of is not there yet, but coming soon adapting an existing project is fun What's next for Osmosis auto-compound Get PR merged into osmosis-frontend When Interchain accounts are ready - go all the way! How to try it out Open the deployed app link Connect your Keplr wallet Deposit some assets to osmosis via "assets" tab Open a pool's page Click the "Autobond" button on the top <div