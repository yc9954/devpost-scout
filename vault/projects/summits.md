---
slug: "summits"
url: "https://devpost.com/software/summits"
title: "summits"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 425
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
---

# summits

> Represent community activity as a network of interconnected projects on-chain. Incentivize contribution to the commons.

[Devpost](https://devpost.com/software/summits) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]

**stack** near-sdk, rust, typescript, vue

## How they structured the write-up

- born from a lack of meaning
- a dapp for project networks
- governance token
- rust, ts and vue.js under the hood
- roadmap
- links to the open source repositories on github
- live demo

## Body

Summits Summits is a dApp that represents community activity as a network of interconnected projects onchain. A governance token incentivizes contribution to the commons. #networkedOKRs Born from a lack of meaning 5 Years ago I was working in consulting and I found that it wasn't obvious for employees to understand how their work contributes to the overall direction or vision of the company. My motivation suffered from this and I came up with the idea of visualizing what a company is doing as a network of projects: all the way from the company vision to the simple tasks of junior employees. This would... make it easier for people to find places where they want to contribute make their work more efficient as it is more aligned with the sourrounding projects enable project value calculation Not only companies but also individuals or communities can use this system to coordinate their efforts. In the past years I got more and more involved with decentral technologies and in my imagination the project graph idea fused with the possibilities of blockchain technology. A dApp for project networks Summits is a dApp that allows users to create projects and interconnections between these projects. Running projects that are valuable for the community is incentivized by a governance token system. Projects (or goals, endeavours, enterprises, ...) are the nodes of the network. Edges between those nodes express contribution of value. E.g. if you want to climb a challenging mountain (node A), some training beforehand (node B) would contribute to your chance of success (flow from B to A). Governance token There will be a governance token that can be deposited with projects. Depositing tokens gives the project an intrinisc value. Also, flows shift some value towards the contributing project. From time to time tokens are distributed among the projects proportional to their current value. Rust, TS and Vue.js under the hood The smart contract is written in rust using near-sdk. The web-UI is written in Typescript using Vue.js. I use kurtosis for setting up a full fledged localnet NEAR environment. Roadmap Update smart contracts to follow the factory pattern Indexer using NEAR Indexer Framework (work started) realtime updates over WebSockets (actix-web) project search engine project value calculation Governance token Links to the open source repositories on GitHub Note that "blockchain-only" is the relevant branch in each repo. web-UI code smart contract code Live demo I will deploy the contract on testnet and publicly serve the web-UI, so that you can go and try it out! \ https://mprnc.dynv6.net/ (runs best on Chrome.) <div