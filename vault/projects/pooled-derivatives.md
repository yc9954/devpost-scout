---
slug: "pooled-derivatives"
url: "https://devpost.com/software/pooled-derivatives"
title: "Pooled Derivatives"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 184
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/sensor_telemetry"
---

# Pooled Derivatives

> On chain derivatives that are based on pools. Settlement functions and underlying price feeds give a wide range of possibilities while a hedging mechanism ensure exposure stays symmetric.

[Devpost](https://devpost.com/software/pooled-derivatives) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**substrate** [[sensor_telemetry]]

**stack** brownie, chainlink, oracles, python, solidity

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i am proud of
- what we learned
- what's next for pooled derivatives

## Body

Overview Inspiration Try to provide on chain derivatives that behave the same way as conventional derivatives but are settled on chain and are based on a pool instead of counter-parties. What it does Its a smart contract that redistributes funds according to a settlement function based on a a price feed. A hedging mechanism ensures that long and short side are equal in size such that the exposure remains stable. The concept allows for a wide variety of settlement functions and underlying price feeds. E.g. you build on chain derivatives on conventional stocks with this. How I built it Using brownie, solidity and chainlink data feeds. Challenges we ran into This is my first solidity project so there quite a few challenges with regard to mastering the language. Accomplishments that I am proud of To bring the concept from an idea into code What we learned Smart contracts have some fundamentally different characteristics. Its challenging to get your idea to to work as you intended in some situations. What's next for Pooled Derivatives Path depended settlement functions, settlement cycles and gas consumption optimization <div