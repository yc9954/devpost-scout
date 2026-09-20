---
slug: "moonbridge"
url: "https://devpost.com/software/moonbridge"
title: "Moonbridge"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 860
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Moonbridge

> The ultimate Moonbeam bridge and explorer. Bridge multichain assets and see your transactions all in one place.

[Devpost](https://devpost.com/software/moonbridge) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]] [[web_dom]]

**stack** abi, cicd, digitalocean, ethers, graphql, python, react, rest, smartcontract, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for moonbridge

## Body

Moonbridge Landing Page Bridge Aggregator Bridge Transaction Explorer Transaction Details Moonbridge Inspiration The blockchain ecosystem has been growing at an incredible speed. As individuals, we have been fascinated by the Polkadot ecosystem and how it has been expanding in an exponential way. One project that caught our attention is Moonbeam. Since its launch in January of 2022, we have been involved in getting to know more about it and its uses as a next generation blockchain. After several weeks of learning Web3 basics, UI and UX design, front end and back end programming; we knew that we had to take part in a blockchain Hackathon, and show our skills and how we can contribute to expanding the uses of Web3. The Polkadot Hackathon was the perfect candidate for us to develop a working Web3 & Tooling project with an intuitive interface that leads to great user experiences. What it does Moonbridge is a Web3 web based dApp that is both a bridge aggregator and a cross-chain bridge transaction explorer. It has a variety of bridge options for bridging funds to and from other EVM-based chains. Some of these blockchains include Ethereum, Binance Smart Chain, Avalanche, Optimism, etc. The protocols available for these transactions are Synapse and Multichain. Users are able to bridge assets in a straightforward way because of its intuitive design. Some features include selecting the maximum amount of an asset to be bridged, an alert for when a transaction has been submitted and a direct link to the transaction details on the explorer. The explorer lets users take a look at the status of their cross chain transfers. The transaction can be entered into the search bar in order to look for a specific transaction. The data displayed includes the transaction hash, coin type, value, the origin and the receiving chain, the address, date, protocol, and if the status was successful or is still pending. The transaction hash is a link to the local explorer of the network the user sent the tokens from or to. It also includes features such as the live price of GLMR, the number of bridge transactions, yearly volume and the average bridging time. How we built it To build this project we had to understand how the bridges we were going to implement worked and how their applications were built. After that, we started building our application in React and interacting with the contracts of the bridges we implemented using ethers. We created a simple backend by using functions in DigitalOcean which helped us reduce the amount of development time and focus on the code instead of the infrastructure. After the backend was done, we focused on the front end to provide a simple and reliable UI for the user to bridge their assets and explore their transactions in a seamless way. To deploy the webiste we used Firebase with CI/CD to keep the website up and running and see changes almost instantly when published. Challenges we ran into When implementing API calls to the bridges, we had some issues when using their endpoints since they do not allow calls from other webpages. Also we have faced some roadblocks with the format of the transactions since every bridge represents the data in their own format. The same happened with the smart contracts when we tried to interact with them but realized each one could have different addresses and methods. We also encountered some problems while styling elements within React, so we made a thorough research into this framework. We had to prioritize all the tasks we wanted to do to be able to deliver a functional product that we want to keep developing and growing. Accomplishments that we're proud of When we decided to participate in The Polkadot Hackathon one of our main goals was to create a product with value for the Polkadot and Moonbeam ecosystem. Today we can proudly say that we have achieved the goal of creating a functional and user friendly Bridge Aggregator and a built-in Transaction Explorer. Last but not least, we are proud of contributing to the enhancement and growth of the Polkadot ecosystem. What we learned As software engineers, one of our main learning goals was to acquire more experience in blockchain development and Web3. We also developed our front-end skills because we used React to develop our web application. Our CSS knowledge was greatly improved, as our user interface was designed in order to be used intuitively by anyone. We also learned an important lesson which is teamwork. Each team member contributed with their personal skills so that we could develop the web application that we have delivered. What's next for Moonbridge As a team, we became fascinated with our development and creation of Moonbridge. Since the beginning, we had in mind many features that we knew we wanted to implement, maybe not now, but in the future. We plan to continue adding bridges to further expand the amount of users taking advantage of the Moonbeam network by building and transacting on it. We use Substrate indirectly by using Moonbeam but in the future we want to include XCM transactions on the application. <div