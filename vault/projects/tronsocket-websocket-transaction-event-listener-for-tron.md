---
slug: "tronsocket-websocket-transaction-event-listener-for-tron"
url: "https://devpost.com/software/tronsocket-websocket-transaction-event-listener-for-tron"
title: "TronSocket - WebSocket Transaction Event Listener for Tron"
hackathon: "TRON Grand Hackathon - HackaTRON Season 7"
organization: "TRON DAO"
winner: true
words: 742
team_size: 2
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

# TronSocket - WebSocket Transaction Event Listener for Tron

> With TronSocket you can listen to events, transactions and block flows on the Tron Blockchain network in the most cost-effective and optimal way without creating your own Tron Blockchain Full-Node.

[Devpost](https://devpost.com/software/tronsocket-websocket-transaction-event-listener-for-tron) · hackathon [[TRON Grand Hackathon - HackaTRON Season 7]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** java, mongodb, nestjs, ngnix, node.js, socket.io, typescript, vue, zeromq

## How they structured the write-up

- inspiration
- what is tronsocket?
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tronsocket - websocket transaction event listener for tron

## Body

Review Page Tokens Dashboard Subscription Usage History Inspiration For my open source project MultipleChain and my WordPress plugin CryptoPay, I needed to listen to events on the Tron network. But I realized that Tron doesn't have a built-in WebSocket support. So the only way to listen to events in a standard way was to install a Tron Full-Node. Since setting up a full node is the only way to to listen the blockchain, this may be a difficult task for developers who don't own a server that fulfills Tron Mainnet's system requirements. This is why TronSocket was born, I asked the question, why don't we build our own Full-Node, enable event listener and offer it as a service? What is TronSocket? TronSocket is a service where you can connect to our services and listen for Tron blockchain events, either directly with the SDK or using a pure WebSocket structure as we illustrate in our documentation. TronSocket consists of 2 parts: Dashboard and Socket Server. In order to interact with WebSockets on the Tron network, you need to create a TronSocket account and subscribe to one of the plans. Then, you need to create a token on the dashboard. Now you are ready to listen to transactions and events on the Tron blockchain. Also, using TronSocket SDK for your TypeScript projects, you can easily listen to the blockchain without diving into WebSocket technology. Therefore, we can call TronSocket a standalone development environment for Tron developers. How we built it First we decided on the technologies we would use in our project, and then the first thing we did was to build the Nile Testnet node on Ubuntu. After that, we used NestJS (Express based), Socket.IO, VueJS, Nginx, Docker technologies to develop a structure that can offer this as a service. We also needed a interactive dashboard that our users can manage their tokens and subscriptions, and also a landing page to attract developers into TronSocket. Last step was the development of SDK. TronSocket SDK allows developers to interact with TronSocket WebSocket server without actually dealing with WebSockets. TronSocket SDK is written with Typescript, and it's completely open-source. Technologies we've used Vue3 Nest.js MongoDB Socket.io Docker nginx Challenges we ran into I tried the first Tron Node installation process on Windows and it didn't work, then I switched to WSL and it didn't work again, but luckily I had Dual Boot Ubuntu and I switched there and tried the installation process but I was getting errors again. So I contacted the Tron developers and they told me to install Java JDK 8 because I was getting errors with the others. I switched to Java JDK 8 and then I created and ran the Node configurations with their instructions. It was a really challenging process, even though it looks simple when I explain it here. Likewise, I had a hard time trying to download and extract the Mainnet Snapshot to our main server, because I tried to download it directly and extract it later. However, the space was insufficient and I wasted a lot of time, I extracted it later while downloading it with wget and pipline. Since it was my first time developing with NestJS, it took me a while to understand its module, service, controller structure. Accomplishments that we're proud of In this process, I used a lot of new technologies and learned a lot. I developed using NestJS for the first time. Likewise, my teammate used VueJS for the first time, we pushed ourselves a lot in this process, but I believe we succeeded. I also think we've created an affordable product that really solves a problem and can help Tron developers. What we learned In this process, I learned unmanaged server setup and deployment processes from the beginning to the end. For the first time, I started a project completely from scratch with nginx. We developed with NestJS and VueJS for the first time and learned new frameworks. I also learned how to deal with overloading processes and created simple queuing systems. What's next for TronSocket - WebSocket Transaction Event Listener for Tron In the future, we're planning to expend our service with a broader endpoint support, as well as a extra methods for our SDK. TronSocket currently works fine for events. Currently TronSocket v1 is live and we have started designing the existing RPC service. In addition to Event Listener, we aim to provide data service directly via RPC. <div