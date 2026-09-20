---
slug: "second-x"
url: "https://devpost.com/software/second-x"
title: "Second X"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 292
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/general_public"
---

# Second X

> NEAR's secondary market for NFTs.

[Devpost](https://devpost.com/software/second-x) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[general_public]]

**stack** javascript, rust

## How they structured the write-up

- video chapters
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for second x
- must be signed in to experience app fully

## Body

Mobile Layouts Home Screen Token Page Contract Page Video Chapters Main Submission Demo (3 min limit) Mobile and Design (1 min) Code Overview (1.5 min) Inspiration NEAR needs an open secondary marketplace for NFTs. Like OpenSea, but for NEAR NFTs. What it does SecondX is an NFT marketplace that allows anyone to place an offer on any standard NEAR NFT. How we built it We started with some boilerplate code from NEAR Examples and docs. We made a Rust contract and added lots of tests using testnet and JavaScript. We created a server that uses the public indexer (sparingly) and creates static files for market data and analytics. We store this on GitHub temporarily right now. Clients can fetch this data and combined with NEAR RPC calls they have a great experience. We plan to transition the indexer piece to something more robust post hackathon. Finally, our frontend was designed by the amazing Pimentel and can be statically hosted. Challenges we ran into Callbacks and state updates/reversions/panics. Indexer design. Access patterns for the market data, stats and summaries. Accomplishments that we're proud of Our contract, indexer and frontend. Basically the whole project. What we learned A lot about NEAR SDK, more Rust and async cross contract calls. What's next for Second X We plan to raise into a DAO that will manage the development, costs and control of things like fees. We are also interested in adding some DeFi functionality with the NEAR held in contract during the offer period. For example, swap NEAR for stNEAR automatically, and then back again when someone needs to be paid. Must be signed in to experience app fully Please sign in with testnet wallet to try the app fully and bid or buy NFTs! <div