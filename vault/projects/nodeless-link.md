---
slug: "nodeless-link"
url: "https://devpost.com/software/nodeless-link"
title: "nodeless.link"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 767
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
---

# nodeless.link

> Trigger serverless function or no-code automation from your smart contract simply, easily and cheaply - with Chainlink!

[Devpost](https://devpost.com/software/nodeless-link) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]]
  <sub>weak: financial_record</sub>

**stack** chainlink, react, solidity, typescript, xano

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nodeless.link

## Body

Create oracles for free and review them at a glance. We take care of the gas fees for all callbacks Pre-created templates that include the correct addresses to make integrating an oracle in a smart contract easy Templates for webhooks that know how to connect with Nodeless so that the developer can focus on the question they want to answer! We created a NPM Package @nodelesslink/core to make integrating a serverless webhook easy! Review recent requests made over your jobs at a glance, including links to the transactions We used the Xano support for Ethers.js to enable low-code, gasless blockchain integration Back-end built with no-code to allow us focus on solving a complicated problem Xano function stacks define our logic at the endpoints for both the app and webhooks using the service Inspiration Serverless technology allows us to serve more people with less infrastructure. It decreases the technical burden of deployment and drops costs of ownership. For minutes of work and pennies - less! - one can have a webhook. Chainlink Nodes can be big and expensive to operate. Shared services like Automation, VRF and Price Feeds allow people to take advantage of many of the common advantages of off-chain work, but the use of external adapters for compute over data applications remained challenging. Spinning up a node on AWS would drive a bill of over $100/month. Applying serverless technology to the distributed oracle problem lets us gut the costs from the system and make setting up arbitrary, interesting off-chain actions and information sources easy and affordable for a new generation of hybrid applications. What it does Nodeless.link allows developers to connect their smart contracts with webhooks in the cloud using Chainlink Oracle contracts. The system provides a form for describing which chain they want the external action to fire on, as well as parameters that allow for testing the serverless oracle. These parameters also help fill out template code that the user can copy-and-paste to fill out a first pass at both their consuming contract and their cloud-native oracle process. We manage the economics via LINK payment to the common oracle contracts. This also guarantees service levels because we use verified contracts built from the Chainlink Oracle repository. How we built it We built Nodeless using serverless and nocode technology to complement modern web3 on-chain contracts. The off-chain state and primary API is built in Xano , a no-code backend platform. We make good use of their recent addition of ethers.js support for communication with the chain. Using No-code for more of the routing and state management significantly cuts down on the code. We use the new Moralis Stream API to listen for on-chain events. This API was relatively easy to use and meant we did not have to deploy listener nodes on our own - a service-ful approach! We use a Netlify function in the middle to connect the Moralis feed with Xano to afford verification of the Moralis signature to ensure data integrity. The front-end dapp hosted on app.nodeless.link is built as a React SPA on Tailwind components. We integrate ethers for wallet-based authentication with the Xano back-end. The dapp also includes highlighted code previews to make development much easier. Finally, we added a small intro/marketing site hosted on umso to keep in the no-code vein. Challenges we ran into Pulling apart the Chainlink request through ABI encoding of the struct and CBOR encoding of the request parameters was a cool technical challenge that made us smarter about efficient conveyance of arbitrary data structures. Also, working with more chains pushed us into more issues of reliability. Props to Polygon whose mainnet and testnet kept working with reliability! Accomplishments that we're proud of Making a full service that makes it easy to link on-chain with off-chain resources could be a game changer for people making interesting products on EVM networks. Radically cutting the costs of off-chain services makes it easy for independent developers to explore more use cases. We can't wait to see what people build! What we learned So much! Making serverless functions work in more contexts. Using Xano to bridge code with no-code Using netlify functions for very fast deployment of new experiments Trying out new and strange oracle use cases - like sending an email! What's next for nodeless.link The opportunities for novel oracular use cases are many. We can't wait to work with the Chainlink community and fellow L2 developers to help more dapps connect with leading edge cloud-based resources for either data sources or expressing the will of the chain. Thank you so much for this opportunity! @rhdeck @akshay-rakheja <div