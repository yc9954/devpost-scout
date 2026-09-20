---
slug: "1bridge"
url: "https://devpost.com/software/1bridge"
title: "1Bridge"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 344
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# 1Bridge

> A bridge aggregator and cross-chain bridge transaction explorer

[Devpost](https://devpost.com/software/1bridge) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**substrate** [[financial_record]] [[web_dom]]

**stack** next, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

Bridge Aggregator home Bridge Aggregator Select blockchain Bridge Aggregator Select blockchain Bridge Aggregator Select token to bridge Bridge Aggregator Show compatible bridges Bridge Aggregator Transaction explorer home Bridge Aggregator Transaction explorer search result Inspiration 1Bridge began as a hackathon project, it was inspired by existing web3 projects like Uniswap and cross chain bridge providers like Celer, Multichain, Connext and the rest, the focus was more on sleek user interface and ease of use. What it does 1Bridge core functionality is to provide a single trustworthy web URL that links to a compatible cross chain bridge provider in a simple ease to navigate user interface. Imagine a single platform that caters for all your cross blockchain transfers, no need to remember too many bridging providers URLs, just this one is enough. You can think 1bridge as 1inch aggregator for cross blockchain asset transfers. Although we currently do not handle any transaction or request user to authenticate and authorize any transfers at the moment but only show compatible bridge provider when a user selects an origin chain, destination chain and token to bridge. How we built it 1Bridge project is made up of 2 subprojects,; Bridge aggregator Bridge transaction explorer Bridge Aggregator The bridge aggregator is basically made up of a widget which comprises 2 sets of modals one to select origin and destination blockchain and the other modal to select token to bridge. Bridge transaction explorer This is a simple user interface with search input and button, when a user enters a transaction hash from the cross chain transaction they sent, the UI sends a request to the multichain api to retrieve the transaction details if it was bridged with multichain else it will return no record. ***Only multichain bridge is supported at the moment and more to be added soon. Each of the modals have inputs that allows user to filter based name or symbols. When a user selects an origin blockchain, destination blockchain and token to bridge, the app searches for all supported bridge provider and redirects based on the user selection. <div