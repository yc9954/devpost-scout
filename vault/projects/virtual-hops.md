---
slug: "virtual-hops"
url: "https://devpost.com/software/virtual-hops"
title: "Virtual Hops"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 378
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/transportation"
  - "substrate/geospatial"
---

# Virtual Hops

> Virtual Hops enables users to see the cheapest / most optimal path between 2 CCIP compatible networks and transfer tokens between them. Effectively acting as a load balancer for CCIP lanes.

[Devpost](https://devpost.com/software/virtual-hops) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[transportation]]
**substrate** [[geospatial]]

**stack** foundry, javascript, react, solidity

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for virtual hops

## Body

What it does Virtual Hops allows users to find the cheapest path between 2 CCIP-enabled networks. The direct route is not always the cheapest route. This project can also double as a load balancer for the CCIP network to ensure each CCIP lane has similar amounts of traffic and avoids congestion on certain popular lanes. How we built it We built it using Solidity + Foundry with a React JS frontend. Foundry gave us the necessary tools to test out smart contracts well and easily deploy them to numerous chains and write scripts to interact with them. the project consists of 2 components, on-chain and off-chain component. On-chain : Smart contracts that route tokens to certain chains, based on the input HOP data that is provided by the frontend. Off-chain : react js frontend that is able to run the A* algorithm based on the CCIP fee feedback that is fetched from the CCIP routers. Challenges we ran into We ran into many problems encoding and decoding the necessary data into the CCIP transfers to communicate the data across chain and successfully parse on the destination chain. We fixed this through lots of trial and error! We also ran into issues with our heuristic for our A* algorithm where we got unexpected results, but after some debugging we got it working very well! Accomplishments that we're proud of We are very proud of the fact we could build a weighted graph in real time using the CCIP fees from the routers and we can accurately formulate the optimal path between different chains. We believe this project is solving a real problem and will hopefully inspire others to solve similar problems too! What we learned We learned more in depth about CCIP and how to build a system that impacts the user in a positive way. We all really enjoyed working on this as a team and having a cool project to show for all of the hard work. We hope you enjoy interacting with it as much as we did building it. What's next for Virtual Hops Next steps is to keep improving, keep building, keep entering into hackathons and enjoying all of the innovation in the web3 space! Keep networking and sharing the knowledge with others. <div