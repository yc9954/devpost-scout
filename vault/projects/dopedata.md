---
slug: "dopedata"
url: "https://devpost.com/software/dopedata"
title: "Mycelium"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 204
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
---

# Mycelium

> Mycelium powers precision farming with distributed sensors networks and a community of growers to increase crop yields, quality, and profitability.

[Devpost](https://devpost.com/software/dopedata) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[sensor_fusion]]
**domain** [[agriculture_food]]

**stack** ceramic, chainlink, gljs, ipfs, mapbox, nextjs, nextui, node.js, openweather, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mycelium

## Body

Browser interface for the Mycelium network. Inspiration Like the fungal filaments that connect and nourish the forest, Mycelium powers smarter agriculture with distributed environmental sensing for better harvests. What it does Mycelium is a distributed sensor network built with Web3 technologies such as IPFS and Ceramic. Through the Mycelium network, compatible devices provide real-time, actionable data to enable users to respond dynamically to changing environmental conditions and to optimize production. How we built it We used embedded devices to drive data to Ceramic and IPFS along with a custom oracle service and Ethereum smart contract to populate the UI. Challenges we ran into We attempted to use Chainlink for AccuWeather and Openweather data but were not able to find public nodes for the feeds. We built adapters for those APIs, and ran a node locally. In the future, we would like to deploy the node and keeper infrastructure for driving UI updates. Accomplishments that we're proud of We're proud that we were able to explore a diverse range of technologies and that we were able successfully integrate them into this project. What we learned Teamwork and the dopamine high of successful hard work. What's next for Mycelium Mycelium is going to spread everywhere. <div