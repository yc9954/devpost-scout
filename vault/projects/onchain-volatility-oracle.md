---
slug: "onchain-volatility-oracle"
url: "https://devpost.com/software/onchain-volatility-oracle"
title: "Swaapvol"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 317
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/sensor_telemetry"
---

# Swaapvol

> An oracle designed to compute the volatility between 2 crypto assets while limiting gas computation costs

[Devpost](https://devpost.com/software/onchain-volatility-oracle) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**substrate** [[sensor_telemetry]]

**stack** javascript, metamask, remix, solidity, trufle

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for swaapvol

## Body

Inspiration We were inspired by the fact that a lot of financial products (e.g., option pricing) or investment decisions (hedging strategies) rely on volatility. Furthermore, we are running a bigger project, a DeX that is impermanent-loss resistant, that needs this module to work. We decided to build this module for everybody to take advantage of building protocols that use volatility in their design. What it does Swaapvol aims to provide an on-chain volatility oracle for any pair of assets individually available as a Chainlink data feed. It is running on Ethereum (Kovan), Polygon (Mumbai), Avalanche (Fufi), Harmony (Testnet) and BSC (Testnet). How we built it To estimate the percentage rate of return (RoR) and volatility of a given pair of assets (e.g. BTC/ETH), we consider here the simplest stochastic model: "Black & Scholes". In that context, this asset is modeled according to a geometric brownian motion and its continuous rate of return follows a log-normal distribution. As a matter of computation efficiency we use here the average and standard deviation of the historical RoR - in lieu of the log returns - as an approximation of the percentage RoR/volatility, and following the Hull's result. Challenges we ran into Our biggest challenge was to identify the right statistical approach to model volatility while ensuring the best computation efficiency for the module. Accomplishments that we're proud of We managed to identify a method which limits the computations and enables us to run in an efficient manner. What we learned We improved our knowledge of geometric brownian movement and how to translate statistical approach into efficient Solidity code. What's next for Swaapvol Swaapvol's computational efficiency will be further improved in a second version of the tool. Swaapvol will be integrated into the first version of Swaap protocol, which is going to be launched end of Q1 2022. Swaap is an impermanent loss resistant DeX, able to handle multiple assets. <div