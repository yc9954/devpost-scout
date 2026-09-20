---
slug: "nairobi"
url: "https://devpost.com/software/nairobi"
title: "Nairobi"
hackathon: "EthCC Hack 2022"
organization: "EthCC"
winner: true
words: 477
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Nairobi

> Nairobi is a deployment tool that sets up and deploys contracts without exposing private keys. Smart contract deployers can execute deployment easier and safer by writing scripts.

[Devpost](https://devpost.com/software/nairobi) · hackathon [[EthCC Hack 2022]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]] [[web_dom]]

**stack** etherjs, gnosis-safe, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nairobi

## Body

Logo Inspiration The smart contracts are getting more complicated in the future. This also means the deployment of smart contracts is getting more complicated. Not only deploy multiple contracts, but you need to do a lot of setup work for the different contracts. Most of the tools now could also do some deployment, but they ask you need to expose your key in the file. It is dangerous, and in some cases, it doesn't work. For example, most service will manage their vault by using MutliSig contracts like Gnosis-Safe. We want to improve this problem and save the time of smart contract engineers. What it does We built a frontend website that developers could use to execute the scripts and send tx by Metamask. Because Metamask is the wallet, most people use and support it. And Metamask also supports hardware wallets like Ledger. We also built a step system to track and execute the scripts written by developers. The developer could execute their script step by step; it all show on the website. You don't need to execute the successful step; just re-execute the failed step. And don't worry about the data generated in the execution of the successful step; you could store it in the cache and use it again. We also support Gnosis-safe so developers can write the script and send Gnosis-Safe transactions. Because we think the most of cases to manage vault is Gnosis-Safe + hardware wallet. It also shows in our demo video how to interact with Gnosis. We use ether.js to write scripts because Hardhat supports Ethers. Developers don't need to learn another package to write the deploy scripts. It is the same with writing the unit tests. How we built it We use react + Ether.js + Gnosis-Safe library to build the whole project and improve the flow of deployment, we want to save the time and get safer for the deployment of smart contracts. Challenges we ran into There are some challenges when we working on it. The biggest challenge is we want to see the problem from the smart contract developer to improve the flow as much as possible. That is a lot of thinking on this issue; what do we need to improve it? Accomplishments that we're proud of We built a nice website and a step executing system. Also, support the Gnosis-Safe in our platform. It is happy to see it come true. What we learned We learned to build a project from user experience, not just implement the function we want. Keep search the answer. What's next for Nairobi We want Nairobi to become the Web3 CI/CD tool. There is a big potential in web3 Dapp. Surely, service becomes more complicated, and we need more tools to help developers to develop amazing projects. We gonna provide more of the CI/CD function, configuration, and so on. <div