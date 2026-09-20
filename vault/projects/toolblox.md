---
slug: "toolblox"
url: "https://devpost.com/software/toolblox"
title: "Toolblox"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 665
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/regulation_legal_text"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Toolblox

> No-code blockchain app maker. Turn any business process into a smart contract.

[Devpost](https://devpost.com/software/toolblox) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**domain** [[finance_payments]] [[retail_commerce]]
**substrate** [[document_pdf]] [[financial_record]] [[regulation_legal_text]] [[video_visual]] [[web_dom]]

**stack** .net, azure, blazor, css, ethers, functions, ipfs, metamask, node.js, polygon, pwa, solidity, typescript, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for toolblox

## Body

Flow gallery Object properties Editing states and transitions Real estate flow in action Mobile view Inspiration One could say no-one is really using blockchain - yes we have DeFi, and NFT's but for most people blockchain is not useful in their daily lives. Our aim is to change that - make blockchain useful to every person and company on the planet. Idea is to go after small and medium size businesses (99.9% of all businesses) who have limited IT capability and know-how - and help them translate their business flows into a smart contract. What we have found during creating hackathon examples is that when you put a business process on chain magic happens: a regular sync-based data flow (exchanging documents with partners, sending invoices to customers) becomes a deep conversion about shared items with payments baked in. New blockchain technologies with fast settle times and cheap transactions (like Polygon) together with clearer regulation (EU wide MICA for example) all help with the transition. What it does Provides a no-code workflow builder to define a workflow Creates smart contract (e.g. Solidity) code from this definition Compiles code into bytecode Deploys to blockchain Generates Web and Mobile UI for interacting with the smart contract (similar to ERC721). Additional features: Upload images and documents to IPFS (Web3.Storage) Show QR code and deep link to open items. Work offline or not being logged in. Add roles and addresses into roles. Create account and authenticate with Auth0 to use backend services How we built it Project started earlier in the year, so some things were already done: Solidity compiler wrapper (solc wrapper) in node.js Model schema (C# classes) + simple UI for parts of the schema Generate 'Spec' format from Model. This is a custom super-simple text format for serializing workflows. Done during the hackathon time: Metamask and Polygon integration for storing smart contracts and working with them IPFS Web3.Storage integration for storing documents and images of items in the workflow. Service which wraps Web3.Storage was done to be 1:1 similar to Web3.Storage HTTP API - to make it possible for each user to use their own API Key and endpoint if needed. User experience and flow designer : splitting design, HTML, Typescript, CSS for web page, app layout, workflow designer and flow usage. Responsive to both web and mobile sizes. Progressive web app in Blazor - users can create workflows offline - no backend needed. They can then store items in local browser storage or export as 'Spec' format and store it wherever. Backend service done using Azure Functions and Table Storage. Authentication with Auth0 in order to use backend service users need to be authenticated. Added QR code to open deepl links to items in workflows Challenges we ran into Flow designer itself was a big challenge. How do you create a visual representation of workflow without complex arrows and elaborate swimlanes? The idea is to be able to glance at the workflow at any point during using the app - to see where are you and what are the next steps in the process. Kind of like breadcrumbs or steps in a shopping cart (shipping, billing, etc). We used external help (good folks at www.linkedin.com/company/boilingbrains ) to tackle this challenge - they helped with mockups and story board. Metamask was very unstable at times and lots of effort was put in to hold the link stable (retries, error checks etc). Probably the instability was due to overcrowded RPC endpoints. Accomplishments that we're proud of Everything works end to end Truly offline capable - ready for the world beyond Web2. Although more work is needed (additional config settings) one can use the app to design a workflow offline, export to human readable format, use local storage and in the future deploy to local Blockchain node, compile with local 'solc' compiler and connect to local Web3.Storage endpoint. What's next for Toolblox Will be adding various features (subflows, versioning, auditing) and approaching companies to create first real use-cases. <div