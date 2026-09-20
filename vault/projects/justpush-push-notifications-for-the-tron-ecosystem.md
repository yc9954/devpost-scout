---
slug: "justpush-push-notifications-for-the-tron-ecosystem"
url: "https://devpost.com/software/justpush-push-notifications-for-the-tron-ecosystem"
title: "JustPush - Push notifications for the TRON Ecosystem"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 826
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "user/developer"
---

# JustPush - Push notifications for the TRON Ecosystem

> JustPush is a communication protocol that enables notifications for dapps wallets and services.

[Devpost](https://devpost.com/software/justpush-push-notifications-for-the-tron-ecosystem) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** react, solidity, tron, typescript

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- what is next for justpush

## Body

JustPush Push notifications for the TRON ecosystem This is a completely new hackathon project built for Tron Grand Hackathon Season 3. Inspiration Notifications are a key feature of any modern web2.0 application. They are used to inform users about important events, such as new messages, new followers, new posts, etc. In the blockchain space, notifications are not as common as they are in web2.0 applications. This is mainly due to the fact that there is no standard way to send notifications. This is a huge problem, as it prevents developers from building applications that are as good as their web2.0 counterparts. In Ethereum, the epns project is trying to solve this problem. Last year, it raised $10.1M in funding from the likes of Coinbase Ventures, Pantera Capital, and others. In Solana, Dialect is trying to solve this problem. And they raised $4.3M in funding recently. In the TRON ecosystem, there is no such project. And we believe that this is gap that needs to be filled. What it does JustPush brings notification capabilities to the TRON ecosystem. The protocol consists of several components. All these components were implemented in the hackathon timeframe after Sep20, 2022 Smart contracts [ github.com/justpush-protocol/contracts ] JustPush node [ github.com/justpush-protocol/node ] JustPush SDK [ github.com/justpush-protocol/sdk ] Dapp [ github.com/justpush-protocol/frontend ] Telegram Bot [ github.com/justpush-protocol/telegram-bot ] Discord Bot [ github.com/justpush-protocol/discord-bot ] JustPush makes the building of notification-enabled blockchain applications easy. It provides a set of tools such as Smart contracts SDKs, APIS, and a Dapp that allow developers to build notification-enabled applications in a matter of minutes. These notifications are tied to a wallet address. JustPush is built in a composability-first way. This means the method the end users receive notifications can be easily changed. These can be mobile push notifications, email, SMS, telegram, discord, etc. We have built a telegram bot and discord bot that can be used to receive notifications. But the list of supported methods can be easily extended. The process of integrating JustPush into a Dapp or service is as follows. The following guide also introduces concepts and design decisions behind JustPush. Step 01: Create a Group What are groups? https://docs.justpush.app/concepts/groups A Group is anyone who activates themselves as a service on the protocol to send notifications to its users. Any service that wants to send notifications to their users can create a Group.Typically dApps in the Tron ecosystem will create a Group to send notifications to their users. How to create a Group? https://docs.justpush.app/developer-guides/create-group There are several ways to create a group. The easiest way is to use the JustPush Dapp. Step 02: Ask users to subscribe to your group Why do they need to subscribe? Imagine if anyone could send notifications to anyone. This would be a huge spam problem. JustPush solves this problem by requiring users to subscribe to a group before they can receive notifications from that group. How to ask users to subscribe? https://docs.justpush.app/developer-guides/subscribe-to-groups Users can subscribe to a group using the JustPush Dapp. But you can also ask them to subscribe to your group using your own UI by using the JustPush SDK. You can also make your users subscribe to your group on -chain by calling JustPush smart contracts directly. Step 03: Send notifications https://docs.justpush.app/developer-guides/sending-notifications What are the types of notifications? There are two types of notifications. Broadcast and Direct . Broadcast notifications are sent to all users who have subscribed to a group. Direct notifications are sent to a specific user. How to send notifications? Group owners can send notifications to their users using the JustPush Dapp. This can be also done by using the JustPush SDK or by calling JustPush smart contracts directly. Step 04: Recieve notifications Subscribed users can receive notifications in a variety of ways. With the SDK, you can show notifications in your own UI, mobile app, service, etc. For the scope of this hackathon, we have built a telegram bot and a discord bot that can be used to receive notifications. But the list of supported methods can be easily extended. Challenges we ran into This is a big project with a lot of moving parts. All of these parts were built from scratch in the short hackathon timeframe. The biggest challenge is the short timeframe. As a one-person team, I had to do a lot of things in parallel. Accomplishments that we're proud of The initial plan was to build a simple MVP. But ended up building a fully functional protocol that's on mainnet with a Dapp, SDKs, and bots. It is still not perfect. But it is a very good start. What is next for JustPush Building a community around JustPush is the next step. We need to get more developers to use JustPush. And we need to get more users to subscribe to groups. Bringing already established services to JustPush is also a big priority. We need more ways to recieve notifications. We need to build a mobile app, a browser extension. <div