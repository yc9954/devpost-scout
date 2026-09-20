---
slug: "adapter-js"
url: "https://devpost.com/software/adapter-js"
title: "Adapter.js"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 773
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Adapter.js

> An external adapter for securely executing custom JavaScript. Fetch data via HTTP requests with optional private headers. Use custom JavaScript to process fetched data & return it on-chain.

[Devpost](https://devpost.com/software/adapter-js) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[structured_db]] [[web_dom]]

**stack** chainlink, google-cloud-functions, hardhat, ipfs, moralis, node.js, polygon, web3.storage

## How they structured the write-up

- overview
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for adapter.js

## Body

Adapter.js External Adapter Call Simulator Overview of Adapter.js Adapter.js logo Check it out at AdapterJS.link Overview An external adapter for executing JavaScript Fetch data from APIs or websites Upload headers to access authenticated APIs without exposing private keys Execute custom JavaScript code to process fetched data Send custom code in a Chainlink request as a string or upload larger JavaScript files to IPFS Simulate external adapter requests using the external adapter web app at AdapterJS.link Use the simulator to automatically generate Solidity code to make an Adapter.js request on-chain Built so any node operator can host an independent instance of Adapter.js themselves to achieve decentralization Inspiration Chainlink external adapters are extremely powerful, but can be time consuming for developers to create. Even after developers create an adapter, they then need to get a node operator to host their adapter, or set up a Chainlink node and host it themselves. Additionally, in order to be truly decentralized, separate instances of the developer’s external adapter must be hosted on multiple independent Chainlink nodes so developers do not need to rely on a single point of failure. This requires developers to get multiple node operators to host their adapter each time they want to make a decentralized Chainlink request with custom functionality. What it does Adapter.js is a Chainlink service which makes it easier for developers to add custom functionality to Chainlink requests. It is an external adapter which can fetch data from any API or website, then securely process data using custom JavaScript before returning the results on-chain. In a Chainlink request to Adapter.js, users can provide custom code as a string or reference a JavaScript file hosted on IPFS. In addition, Adapter.js can securely access web resources which require authentication by allowing users to upload headers containing private keys to the external adapter’s database. These custom headers are encrypted and are only able to be used in requests initiated by an approved smart contract. Adapter.js is open source and is being developed such that any Chainlink node operator can run their own independent instances of the external adapter. This means, as more Chainlink nodes support Adapter.js, developers no longer need to rely on nodes which have agreed to host the developer’s own custom external adapter. Developers would instead be able to make a custom requests to any node which hosts an instance of Adapter.js. This also makes it easier for developers to verify resulting data in a decentralized manner. Developers can then make requests to many nodes which host an instance of Adapter.js; then consensus can be reached on-chain by comparing the results provided by each node. How I built it Adapter.js was built using Node.js and is currently deployed to Google Cloud Functions which allows for limitless scalability when executing user provided code. If a user chooses to upload code to IPFS, it is stored and retrieved using Web3.Storage. If a user uploads private headers, they are securely stored on Google Cloud Storage. The Chainlink node where Adapter.js is currently available is connected to the Polygon network using a Moralis RPC node. Challenges I ran into The most difficult part of building Adapter.js was security. Executing user-provided exposes many security risks. This required finding a sandbox which could execute Node.js code and verifying the sandbox had no known security flaws. Another security challenge was securely storing and accessing uploaded headers to be used in HTTP requests. This was made easier by Google Cloud Storage which provides built in security tools such as data encryption. Accomplishments that I am proud of I am proud that I created a robust piece of technology that developers can actually use. In fact, I have already been contacted by multiple developers who would like to use Adapter.js in their own projects! What I learned Prior to this hackathon, I had no experience with using Chainlink and limited experience working with Node.js. However, by the end of the competition, I became competent using Node.js and gained a deep understanding of Chainlink's capabilities. In addition, I learned how to use Google Cloud Platform. What's next for Adapter.js Currently, Adapter.js is only hosted on one Chainlink node for the Mumbai Polygon testnet, however it has been built in such that any node operator can host Adapter.js themselves. The next steps for Adapter.js will be to create new Chainlink nodes that host the adapter for all Chainlink-supported blockchains. Concurrently, the goal is to encourage many independent Chainlink nodes to host their own instances of Adapter.js in order to achieve decentralization. Eventually, developers should be able to send requests to any node in a huge pool of nodes which all support Adapter.js. <div