---
slug: "link-become-human"
url: "https://devpost.com/software/link-become-human"
title: "Link: Become Human"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 336
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
---

# Link: Become Human

> Dynamic NFT that utilizes Chainlink VRF, Chainlink Functions, and Chainlink Automation. It leverages the Gitcoin Passport's humanity score to show an android's transformation into a human in the NFT.

[Devpost](https://devpost.com/software/link-become-human) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]

**stack** avalanche, chainlink, ens, thegraph, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for link: become human

## Body

Hero UI OpenSea Dynamic NFT Unity Integration Technical Detail Inspiration I want to create a system on the blockchain that visualizes a 'humanity score'. What it does Dynamic NFT that utilizes Chainlink VRF, Chainlink Functions, and Chainlink Automation. It leverages the Gitcoin Passport's humanity score to show an android's transformation into a human within the NFT. How we built it Dynamic NFT State The humanity score affects the growth of the android. The random seed value affects accessories like hats and eyeglasses. Unity for Dynamic NFT Dynamic NFTs are rendered using Unity and WebGL. Unity fetches data from The Graph and updates the state dynamically. The web app and Opensea display the same Unity dynamic NFT using an iframe. Data Integration Diagram Gitcoin Passport as a source for humanity scores. Chainlink Functions for integrating humanity scores into NFT smart contracts. Chainlink Automation to automate the data fetching process. Chainlink VRF for generating random seed values. The Graph for data aggregation purposes. ENS for managing identity data, such as names and avatars. Chainlink Integration The details of Chainlink integration are maintained here. https://github.com/taijusanagi/link-become-human/blob/main/Docs/Chainlink-Integration.md Avalanche Integration The dynamic NFT is deployed Avalanche C-Chain Fuji Testnet. https://testnet.snowtrace.io/address/0x98d80C7a5338fD211544f1f807D19F9191264Ce0#code-43113 Opensea supports Avalanche C-Chain Fuji Testnet and the asset page is here. https://testnets.opensea.io/assets/avalanche-fuji/0x98d80C7a5338fD211544f1f807D19F9191264Ce0/1098112484341563293955512077999730492067707 The Graph Integration The Graph is used in a Unity C# script for data aggregation. https://github.com/taijusanagi/link-become-human/blob/main/Assets/Scripts/GameManager.cs#L122 The following subgraphs are integrated. https://api.studio.thegraph.com/proxy/60667/linkbecomehuman/v0.0.1/graphql (New) https://api.thegraph.com/subgraphs/name/ensdomains/ens/graphql (Existing one for ENS) ENS Integration The ENS name is fetched by The Graph and displayed in the dynamic NFT. The ENS avatar is fetched by Rainbow Kit SDK. Challenges we ran into Using some of the Chainlink modules was a new experience for me, so it took time to learn how to use them. Accomplishments that we're proud of I have implemented Chainlink Functions, Chainlink VRF, and Chainlink Automation, and have also demonstrated a working dynamic NFT. What we learned Relevant Chainlink modules Unity Development The Graph Integration What's next for Link: Become Human Add more accessory for random ness Make it production <div