---
slug: "xcm-explorer"
url: "https://devpost.com/software/xcm-explorer"
title: "XCM Explorer"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 246
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# XCM Explorer

> Cross-Chain Messaging Passing (XCMP) is one of the key features of Polkadot/Kusama ecosystem. This tool, hopefully, can make it easier to track messages across Kusama and its parachains.

[Devpost](https://devpost.com/software/xcm-explorer) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**substrate** [[financial_record]] [[structured_db]]

**stack** react, subquery, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for xcm explorer

## Body

Inspiration Currently, tracking transactions across chains is not easy. This issue is addressed by XCM Explorer. What it does It allows users to list all cross-chain transactions for a given address on Kusama, Moonriver, Karura and Basilisk. Both hex and SS58 style addresses are supported. The information for both sender and recipient is only available for the supported chains, that is why many transactions show only one part (sent or received) part of XCM. How we built it We used SubQuery to index the four chains. UI is build with React/TypeScript. Messages between chains are linked by the message hashes. GraphQL queries are made from the UI to fetch two related pieces of XCM across four databases. Challenges we ran into The information available for different type of messages (HRMP, DMP an UMP for those in the know) is not consistent. For example, the message hash which is used inside parachains themselves readily available or not available at all. Accomplishments that we're proud of We manages index and link all the related parts of XCM on four chains despite the challenge above. What we learned It is difficult to make a generic tool for a something so versatile and flexible as XCM format. What's next for XCM Explorer The parsing of information can be significantly improved, as for now, most of the information is just given in JSON format. And, of course, more chains should be indexed to make this tool useful for many users. <div