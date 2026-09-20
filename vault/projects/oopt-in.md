---
slug: "oopt-in"
url: "https://devpost.com/software/oopt-in"
title: "Allocation Engine / opt.in"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 289
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Allocation Engine / opt.in

> Endow, Vote, and Spend in network - supporting real earth value in the cosmoverse.

[Devpost](https://devpost.com/software/oopt-in) · hackathon [[Cosmos HackAtom VI]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[civic_government]] [[developer_tools]] [[supply_logistics]]
**substrate** [[document_pdf]] [[financial_record]]

**stack** golang, javascript, preact, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for oopt.in

## Body

GIF quick silent gif of the allocation ui in action diagram of the over all planned scheme linear flow (legend for the diagram) Inspiration pylon gateway, regen network, global ecovillage network What it does facilitates principle secure investments (endowments) investor engagement by allocating resources within the network of earth value producers investor incentivization via rewards offered by the network of earth value producers How we built it For this hackathon we focussed on the Allocation Engine, which will be the technical centerpiece for oopt.in, but also serves as a standalone open source contribution to the core cosmos modules. Challenges we ran into Building proto files in both go and ts and wiring them together using typescript, while trying to minimize boilerplate. We wanted to build a streamer directly from Osmosis pool rewards, but the Cosmos sdk isn't ready for it yet (cross chain accounts and hooks are both needed), so we spun off another submission that did 70% of what we wish could happen via modules and smart contracts directly in the Osmosis UI: https://devpost.com/software/osmosis-semi-auto-compound Accomplishments that we're proud of simple ui architecture that uses material design library and offline-first transaction handling fully working integration with keplr and a local chain with a new custom module. What we learned proto files can be used to generate useful strongly typed go and typescript files that are reasonably managable to wire up front end ui with blockchain "backend" What's next for oopt.in we applied for a regen grant, so hopefully we'll get funding to continue manifesting: integration with governance protocols implement streamers and add more types of streamers community engagement consider inclusion in the Cosmos SDK more advanced allocator voting structures as outlined in the opt.in section of the pdf <div