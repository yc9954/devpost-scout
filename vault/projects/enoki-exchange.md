---
slug: "enoki-exchange"
url: "https://devpost.com/software/enoki-exchange"
title: "Enoki DEX"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 911
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "domain/media_journalism"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/geospatial"
---

# Enoki DEX

> Completely Async and Scalable DEX: Swap, Earn, and be a Market Maker

[Devpost](https://devpost.com/software/enoki-exchange) · hackathon [[Supernova]]

## Facets

**domain** [[developer_tools]] [[labor_employment]] [[media_journalism]]
**user** [[developer]]
**substrate** [[financial_record]] [[geospatial]]

**stack** internet-computer, react, rust

## How they structured the write-up

- inspiration
- try it out
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for enoki dex

## Body

Swap Provide Liquidity Trade and Make Markets Inspiration Having both worked in Fintech, we had an idea of what we wanted in a Decentralized Exchange. When we heard about the scalability and asynchronous nature of the Internet Computer, something that sets it apart from other blockchain systems, we decided to imagine what an exchange with multiple asynchronous actors would look like. We arrived on a model with one central exchange with multiple "brokers" around it, and Enoki was born. Try it out Well, this is a long, technical post, and we hate to ramble. TL;DR: scroll to the bottom links and try out our dApp. What it does In short, Enoki is a Decentralized Exchange that allows users to swap tokens, provide liquidity, trade using limit orders, and act as a market maker. A user signs up to the exchange and is assigned a broker. The user can submit limit orders to the broker, which are then executed by the exchange after a synchronization round. Users can also lock liquidity into a Liquidity Pool. Brokers have access to this liquidity, which is available for swapping at prices determined by the bid-ask curve of the limit orders in the exchange. This way, users are also able to instantly swap tokens with any broker, without having to wait for any exchange synchronization. As an additional incentive for market makers, users who submit limit orders that are posted to the order book (they create a market) receive 0.03% in rebates when their order is matched. How we built it We had Rust experience but had never built an Internet Computer canister. However, we were quickly up to speed after attending the excellent Supernova developer workshops. We used Rust to code the canisters, and React to code the frontend. After several iterations we now have: a central exchange canister in charge of synchronizing state and executing limit orders. many broker canisters in charge of taking limit orders, distributing order payouts, and immediately executing swaps. a liquidity pool canister in charge of keeping track of liquidity. a liquidity pool worker canister where users actually deposit their liquidity. It has an anti-spam mechanism to ensure the exchange canister can constantly and reliably communicate with the liquidity pool canister. Challenges we ran into We aim to create a truly scalable DEX that simply adds and removes broker canisters as user activity changes. We met our first obstacle when we realized that existing token standards are not yet scalable. They depend on a single canister for processing transactions, and this canister can get clogged up after a sudden influx of transactions. Since we wanted the core of our project to be truly scalable, we designed our own proof-of-concept token standard. The Enoki Token has a sharded data structure that allows for scalable token transfers. Another challenge we ran into deals with market maker incentives. Because the liquidity pool (and the returns for liquidity providers) relies so heavily on bid-ask curves set by market makers, it became essential to set the right incentives for market makers to operate at the right prices. We therefore added multiple measures to ensure market makers cannot manipulate this bid-ask curve, such as being able to cancel limit orders only after a synchronization round. We also plan to penalize bad market making (for example, not giving rebates for setting bids/asks that do not have a large enough bid-ask spread, as proven by either historic or future price volatility) and use these funds to reward good market making. Accomplishments that we're proud of In a month we have created a complete version of our DEX, which includes swapping, a liquidity pool, limit orders, and an automated market maker bot. It is fully deployed and running with test tokens. We also take pride in designing a good looking dApp. We aim for a simple and user-friendly UI, and we think we have achieved that with our design - it's clean, and it makes you want to trade some tokens. What we learned On the programming side, we learned that we can actually put our Rust hobby to good use. And we brushed up on our css. A lot. We were also impressed at how fast and easily we can deploy a complete dApp on the Internet Computer, including all the hosting. We thought surge.sh was the coolest thing we had ever seen, but now dfx deploy --network ic enoki_exchange and us are best buds. What's next for Enoki DEX We have a lot of work in the pipeline. First, when there is community consensus on a standardized token standard, we want to migrate our token to fully support it. We also want to discuss our sharded token model for scalability with the community. Second, after extensive testing we will release a version of Enoki DEX with real wrapped tokens, probably starting with ICP, Cycles (XTC), and possibly BTC pending Bitcoin integration. We also have a lot of extra features we want to add to our dApp: ability to scale up and down automatically, depending on user activity. use tokens collected as fees, converted to cycles, to power the dApp. ability for users to migrate to less utilized (and therefore faster) shards/brokers. move a lot of the state to an archive canister that uses a distributed big-map to store data. And add transaction history for the token (using PubSub mechanism). for the our sharded token, establish paid priority shards, for example for the exchange and liquidity pools. <div