---
slug: "dtelecom"
url: "https://devpost.com/software/dtelecom"
title: "dTelecom"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 332
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# dTelecom

> Web3 CPaaS - Decentralized Communications Platform as a Service. Infrastructure for audio/video conferences powered by community. 4x cheaper, safer, reliable.

[Devpost](https://devpost.com/software/dtelecom) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** golang, javascript, near, pion, rust, webrtc

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dtelecom

## Body

Problem & Solution What is dTelecom Use Cases Adding a b2b Client Run a Node Web3 Meeting powered by dTelecom Inspiration It was an idea since 2018 to building telecom services on top of blockchain. Current services in telecom mostly created and maintained by single company. It's not clear how they store and manage clients data. Reliability and security couldn't be guarantee using this approach. Same time customers has limited ways to request some features or even bug fixes. Using modern blockchain with fast and cheap transactions and modern open-source software for distributed WebRTC SFU we are building a decentralized Communications Platform as a Service supported by community (DAO). What it does It's a b2b SaaS. Developers can integrate dTelecom SDK into services to add real-time audio/video communications and pay only for minutes spent. There are different companies providing such services like Twilio or Vonage. Main difference is in infrastructure. Conferences use decentralized network of nodes maintained by independent mainers. How we built it We built MVP using NEAR blockchain and ion-sfu project. There 4 parts: 1) smart contract - provide secure billing between miners and clients 2) frontend - provides interfaces for clients and miners to manage deposits and staking 3) node software - miners run on their servers to provide services for WebRTC conferences 4) client software - frontend and backend for web conferences Challenges we ran into All challenges were resolved using chat or office hours. The main challenge was to make it in time. Accomplishments that we're proud of Finally we have working MVP in mainnet. What we learned Rust. How to build on NEAR - it's really much more simple comparing with another blockchains. What's next for dTelecom We have a large list of TODO. 1) Marketing - we need our first customers 2) Community - we need our first miners 3) Technical debt - a lot of things And later we are planning to add more different services like: instant messaging VPN VoIP calls etc <div