---
slug: "hyperdapp"
url: "https://devpost.com/software/hyperdapp"
title: "HyperDapp"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 355
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/web_dom"
---

# HyperDapp

> HyperDapp is a browser developer tool that empowers anyone to instantly create & deploy verifiable front-ends for dApps.

[Devpost](https://devpost.com/software/hyperdapp) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** etherjs, ipfs, moralis, polygonscan, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for hyperdapp

## Body

Code Editor Dashboard IPFS upload Embedded into iframe Inspiration Smart Contract developers don't want to deal with front-end technologies, libraries or SDKs. They want to focus on the smart contract side and be able to prototype a UI for testing purposes quickly. It is hard for web2 developers to onboard into web3 because of the wide range of libraries/SDKs they need to learn. They want a simple tool that can run directly from the browser without installing and learning any libraries. Building front-ends for dApps is challenging because developers must integrate web3 logic, such as wallet connections or smart contract interactions, into the front-ends. Developers have to deal with complex and fragmented tech stacks. Often, they have to overcome a steep learning curve to understand and use numerous SDKs or libraries. What it does HyperDapp turns the process of building dApps front-ends into a seamless workflow. A key component of HyperDapp is a browser-based code editor capable of auto-generating code snippets. With live previews, testing and debugging smart contract interactions and prototyping UIs has never been easier. With a click of a button, the code for generating the front-ends is deployed to decentralized storage such as IPFS. After deploying it, the user gets a unique URL that can be shared among end users, testers, and teammates. This URL can also be embedded into any website through an iframe. How we built it During the Hackathon, we added support for Polygon and Mumbai chains. We added chain support to our interpreter engine and the ability to fetch verified contracts ABI from polygonscan Challenges we ran into We had to think about the architecture of our code to support multiple chains. Accomplishments that we're proud of Thanks to the hackathon, we quickly added support to other EVM chains. We are now supporting Ethereum, Polygon, Binance, Avalanche, Fantom, and Arbitrum. What we learned Handling switching chains within a dApp Deploying data to IPFS based on different chain What's next for HyperDapp Deploying the HyperDapp decentralized code registry to Polygon Composability: developing a search mechanism for users to lookup for existing front-ends and be able to fork them <div