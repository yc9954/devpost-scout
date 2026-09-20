---
slug: "internet-computer-services"
url: "https://devpost.com/software/internet-computer-services"
title: "Internet Computer Services"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 530
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Internet Computer Services

> Build, ship and manage dapps faster on internet computer

[Devpost](https://devpost.com/software/internet-computer-services) · hackathon [[Supernova]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** motoko, node.js, postgresql, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for internet computer services

## Body

Dashboard Canister Management Create Canister Marketplace Inspiration It takes time for a developer to embrace new technology. Learning a new language to understand cutting-edge technological paradigms can sometimes be intimidating. We want to simplify developers' lives in the IC ecosystem and give them the tools and technology to build, ship and manage dApps faster on IC. What it does At its core Internet Computer Services ( ICS ) provides easy creation and management of atomic units in IC called Canisters . But the realm of ICS expands to the scale at which AWS / GCP offers services in Web2. ICS aims to provide small, independent, developer-owned services that will become building blocks of dApps. 100% on-chain deployed queue service, secret manager etc., are some of the services ICS aims to provide and continuously add more as the community requires. Apart from these services, ICS aims at providing 1-click deployment of dApps available in the marketplace, minting of NFTs, token generation for any new project, and provisioning on-chain BTC and ETH wallets with few simple clicks. ICS will support many more upcoming native integrations in the future, like SNS. How we built it We have written some of the core functionalities in Motoko and have deployed those core modules on IC. We call them ICS-Management Canisters. The rest of the implementation is developed in the traditional stack with javascript talking to ICS-Management canisters via agent-js. Challenges we ran into During our implementation, we realized requests for key functionalities like creating a canister could not be sent from outside of IC. It has to be a call from another canister. This discovery introduced a bit of lag to our development process, and we had to re-design our architecture. Accomplishments that we're proud of We are proud of achieving core canister management functionalities like Canister creation, deletion, starting/stopping a canister, topping up a canister with more cycles, and Installing WASM with installing/reinstalling/upgrading modes directly from UI. We are also proud to introduce a registry that developers can use to store WASM binaries and deploy them when needed. One of the very promising features of ICS is ICS Marketplace . ICS marketplace allows developers to submit their dApp. And then anyone without technical knowledge can 1-click deploy these dApps for their use. ICS Marketplace is a revolutionary use case for speedy adoption of IC and, at the very same time, incentivizing developers for dApps development. What we learned Every day of development in IC is a new learning opportunity. One may know how a blockchain works, but IC is a decentralized computer. With so many new native integrations and dApps coming on IC, we are sure to learn many new things, especially the ones we have not even seen in early web3 tech like ETH. What's next for Internet Computer Services Internet Computer Services will keep adding new services and onboarding developers at a significantly faster pace. We know time-to-market is critical for any startup and dApp, and we want to accelerate the development of dApps by helping our fellow developers. Moreover, ICS will soon be looking to raise more money to hire like-minded developers who want to create a product for developers. <div