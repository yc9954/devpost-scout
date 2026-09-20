---
slug: "shiro-share"
url: "https://devpost.com/software/shiro-share"
title: "Shiro Share"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 546
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Shiro Share

> A simple, fast and convenient instant file sharing platform. No web3 wallet necessary (you can use one if you have).

[Devpost](https://devpost.com/software/shiro-share) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[code_repository]] [[financial_record]] [[sensor_telemetry]]

**stack** chainlink, fleek, ipfs, magic.link, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- features
- details
- challenges and accomplishments
- what we learned
- services used
- what's next for shiro share
- relation to shiro storage

## Body

Dashboard Authentication My Files Pricing Architecture Inspiration Instant file sharing platforms are very popular in "web2". A quick google search for "instant file sharing" gives you many popular services. Decentralized alternatives for such services are needed. Storage platforms such as IPFS, filecoin, etc. have provided immense value to the ecosystem but they are quite hard to use for end users looking to quickly send a file. Even if they exist, such platforms built on web3 usually rely on the user having a sufficiently funded crypto wallet. What it does It's as simple as uploading a file and sharing the generated link. There's a free tier powered by Magic.link - no crypto wallets necessary. How we built it Behind the scenes, the magic.link, IPFS, a gasless transaction and a storage backend all work to store the file with no cost to the end user. Learn more about how it works here Features ✨ Easy to use : all you need to do is sign up, upload a file and share the link. 💾 Multiple storage backends : files are uploaded to any one of the storage providers including IPFS and web3.storage . Powered by Shiro Storage . 📖 Open : the entire codebase is open source with complete documentation. 🚮 Automatic garbage collection : using Chainlink Automation , files are cleaned up once they expire. 💰 Free : the free tier allows uploading files without any credit card or crypto wallet. Enabled by magic.link and OpenZeppelin Defender . 💸 Simple pricing : USD based pricing but charged in ETH/MATIC. Details The documentation has all details, including the architecture , FAQ and self-hosting guides . Challenges and accomplishments The two main challenges to usability were: Making it available without needing a crypto wallet. Solved by magic.link . Providing a free tier and absorbing the costs. Solved using OpenZeppelin Defender - Autotasks, Relayer and Forwarder. Learn more here . What we learned How to call a contract from another contract Other methods of making gasless, fee-less transactions Services used Note: these were all necessary to bring this project to fruition. Chainlink Automation: source code IPFS: deployment docs , storage provider web3.storage: storage provider Fleek: client deployment , docs deployment Quicknode: used as the main Eth node Polygon: we used Polygon Mumbai as our testnet for all contracts. Magic.link OpenZeppelin Forwarder: source code OpenZeppelin Autotask: source code OpenZeppelin Relay: source code Shiro Storage: source code . This is another project we built for the same hackathon - at first to power Shiro Share but we made it generic enough to be usable by anyone needing storage with a contract. What's next for Shiro Share Accept payment in any ERC20 token - currently only accepts ETH/MATIC Upload directories Encryption - currently all files are publicly available with the right CID. For private file sharing, the files must be encrypted with a shared key. We plan to encrypt it symmetrically and embed the key in the link, so that only people with the link can view the file. Relation to Shiro Storage While Shiro Share is built on Shiro Storage, they are completely different products with different use cases. Shiro Share is a simple app for anyone to share files whereas Shiro Storage is a generic storage platform for the web3. <div