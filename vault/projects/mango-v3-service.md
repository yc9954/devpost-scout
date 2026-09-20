---
slug: "mango-v3-service"
url: "https://devpost.com/software/mango-v3-service"
title: "mango-v3-service"
hackathon: "IGNITION | A Global Solana Hackathon"
organization: "Solana Capital"
winner: true
words: 344
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/security_privacy"
  - "user/general_public"
  - "substrate/financial_record"
---

# mango-v3-service

> Bring your existing trading tools adapted for centralized exchanges to trade on mango markets version 3 by using the REST API and sample clients provided by this project!

[Devpost](https://devpost.com/software/mango-v3-service) · hackathon [[IGNITION - A Global Solana Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[security_privacy]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** express.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mango-v3-service

## Body

tl;dr demos mango-service-v3 curl example demo mango-service-v3 python client example demo Inspiration Quite often different trading venues offer different mutually exclusive opportunities. To exploit all opportunities using consistently similar systems traders prefer adapting their existing tooling to work with newer venues. Mango markets is a very popular decentralized exchange with support for providing cross collateral based leveraged trading. So far mango markets has a very sleek UI and a python client with solana specifics to trade on it. Yet, it lacks a more simpler interaction medium like a REST and WEBSOCKET API which lets experienced traders bring their existing tools written in their programming language of choice to trade on this. This project aims to solve this. What it does Provides an easy to consume REST and WEBSOCKET API for trading on mango markets version 3. And in addition a simple python client and some examples. How we built it The project is built using typescript and expressjs and uses the official mango typescript client underneath. This was a conscious choice since the mango typescript client would always be a first class citizen because of its use in the official mango web app and would be continued to support and maintain by the core team. Challenges we ran into One of the long term goals is to have latency to perform various operations similar or lower than centralized exchanges. This requires a lot of careful optimizations like pre-loading required state, batching of instructions into solana transactions, etc. case by case basis. Accomplishments that we're proud of An MVP which serves all the basic operations required to build more sophisticated programs e.g. a marketmaker. What we learned From a lot of user feedback gathered, it became obvious that users want support for placing many exotic orders e.g. splitting a order into smaller chunks at various price points. What's next for mango-v3-service This is just the start, there are bunch of advanced features e.g. order types, optimizations, integrations. In addition I would also like to build more complex examples e.g. a more advanced market maker <div