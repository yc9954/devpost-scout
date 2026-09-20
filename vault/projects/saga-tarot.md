---
slug: "saga-tarot"
url: "https://devpost.com/software/saga-tarot"
title: "Saga Tarot"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 781
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/developer"
  - "substrate/financial_record"
---

# Saga Tarot

> Open source tarot ecosystem on the IC. Nobody owns Tarot. Everybody owns Web3.

[Devpost](https://devpost.com/software/saga-tarot) · hackathon [[Supernova]]

## Facets

**mechanism** [[provenance_signing]] [[vision_ocr]]
**domain** [[developer_tools]] [[finance_payments]] [[transportation]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** cap, dab, ext, motoko, react, three, typescript, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for saga tarot

## Body

Inspiration Tarot is a bustling community of people who enjoy the art, social aspects, and creative self insight that this card-based "divination" practice has to offer. It's a semi mystical practice that's been around for hundreds of years and is going strong to this day. I love what MTG Arena and Hearthstone have done to create a beautiful digital experience out of a "traditional game" based on physical cards, and this project started with the intention of doing the same thing with tarot. After discovering the Internet Computer, I realized that the web3 infrastructure it offers could take the project to a new level, and that there are latent similarities between the tarot and web3 communities. Tarot is a naturally decentralized space, with thousands of artists creating tens of thousands of unique decks, and meritocratic and open ideals pervade. What it does Saga's initial purpose is to bring a delightful, faithful digital tarot experience to existing tarot fans, and to do it in a way that enables and encourages open contribution and participation at all levels. We do this by first establishing the groundwork for interoperable tarot goods and services (NFTs and dApps) as a suite of open source software and SDKs. There are several components of this ecosystem that we have developed on IC mainnet: The Bazaar : A launchpad protocol and secondary NFT marketplace that's dedicated to tarot. The Tarot Directory : A DAB standard NFT registry that provides developers with an authoritative list of all available tarot NFTs in a single call. Open Tarot SDK : A typescript SDK available on npm providing a plug-and-play api to connect wallets, discover available NFTs or tokens owned by the user, query provenance, mint/buy/sell NFTs, query assets, and so on. Tarot Table : A a simple dApp built using the SDK, allowing users to use any decks they own to do tarot readings. Legends NFTs : Illustrating a full deck of tarot cards is a time consuming process, so in addition to our NFTs which act as a fully functional deck of tarot cards, we developed this series of collectible NFTs. Each Legends token is good for one or more full decks once illustration is complete, and the full deck inherits the unique card trim from the collectible that spawns it. Legends NFTs have some unique features enabled by IC, such as static, animated and interactive views that are encoded in the same canister as the token ledger itself. How we built it Our stack is Motoko and Typescript, with React and Threejs for our 3D interactive components. We operate a fleet of canisters dedicated to various functions: the launchpad canister, a fleet of Legends NFT canisters, a fleet of tarot deck canisters. Our frontends can be deployed to the IC, but we have preferred other solutions that can offer just-in-time edge-cached rendering. One perk of flexible deployment targets is that we can decentralize our frontends using the IC at the drop of a hat if it is required. We have relied heavily on the EXT standard in developing our own legends and tarot deck NFT canisters, as well as much of the work done by Psychedelic DAO to provide standards and common infrastructure for our NFT projects (CAP provenance, DAB directories, etc.) We developed custom NFT generation tools and a novel open source minting protocol . Challenges we ran into ICP Payments Payments processing with ICP has been a significant learning process for the community, and for us. Having found a few ways that do not work, we eventually developed a protocol based on per-principal deposit accounts held by our launchpad canister, which allows us to perform atomic "single client message" or "fire and forget" purchases. Accomplishments that we're proud of Novel Fire-And-Forget ICP Payment Protocol ICP purchase protocols often relied on the client performing multiple calls in order to complete a transaction. For example, a client would have to perform separate message executions to 1) indicate intent to purchase an NFT, 2) transfer ICP, 3) notify the purchase handler of the ICP transfer. This is a fairly simple flow, but mishandling it is easy for a dApp to do. This can result in incomplete transactions that must be recovered and mean headaches or lost ICP for end users. User controlled deposit accounts within the payments canister allow clients to instead "fire and forget" a single message to purchase some goods with ICP, which will atomically fail or succeed. What we learned What's next for Saga Tarot Illustration for our first complete deck will finish later this summer. We will keep building better tarot experiences, and eventually begin translating knowledge gained into new niches in the IC and Web3. <div