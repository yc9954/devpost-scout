---
slug: "metatalk"
url: "https://devpost.com/software/metatalk"
title: "MetaTalk"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 660
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/security_privacy"
  - "user/small_business"
---

# MetaTalk

> Opensource Decentralized Communication Protocol

[Devpost](https://devpost.com/software/metatalk) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[security_privacy]]
**user** [[small_business]]

**stack** php, react, solidity

## How they structured the write-up

- so, metatalk. pitch me!

## Body

So, MetaTalk. Pitch me! Did you see the film “Ready Player One”? Oasis Metaverse looks like the future of gaming. But it had one fatal flaw - it was developed and maintained by a single Mega (Meta?) company. Huge companies are slow and inefficient in most cases. And also they tend to ignore users when it related to money. Try to ask some giant to do not monetize your personal data. Let's imagine something opposite - Metaverse, which will unite thousands of independent games in a single experience. Such a Metaverse would eat “Oasis” for breakfast. Single Gaming Metaverse will need to be Decentralized and it will need Decentralized Communication Protocol, which I am trying to build. OMG, one more decentralized messenger. Really? No, we already have way too much messengers and I am not trying to build one more :) As a freelancer - I already use email, telegram, viber, whatsup, slack, Microsoft Teams, discord, facebook messages, linkedin messages, upwork messages, jira comments, github comments and a few dozens of less popular tools for communications. That's already ridiculous, but in the Metaverse with thousands of independent games it will become even worth. So, I am trying to build an open source communication protocol - which can be used by anybody. Call it what you want. Ok, so you are going to use crypto wallets for user identification and blockchain for messages storage? Yes and No. Yes, I am using crypto wallets for identification, because it's an existing and stable technology with a big user base and a lot of benefits. Messages are signed using crypto wallets, but no, I do not try to put messages into the blockchain - it's inefficient and it will produce a lot of hard to solve problems. What about NEAR Sharding? It looks like an ideal tool for this use case. Unfortunately, no. Blockchain is just not working for storing messages because of different reasons. Few of them - most users do not want to pay for each message and you can't send big files over the blockchain. Anyway, you want to use my wallet for signing messages. Which will mean that I will need to either sign each message OR provide my secret key to some software. I don't like both ways. There is a third way - you may authorize some new keys to send messages on your behalf and share them with sender software. How will it work. You register at “DecentralizedFacebook” and you want to send messages from it to your friends DecentralizedFacebook generate new wallet and you authorize it with your main key You may send signed messages from DecentralizedFacebook And “NEAR” blockchain has built-in functionality for this. Hm.. Sounds interesting, but it looks over complicated. I would prefer to use “OldFacebook” instead and not bother with keys etc. There are few serious benefits. For example, what will you do if some hacker steals your “OldFacebook” account and sends messages to your friends? Also in future Metaverse there will be a lot of “indy games” with weak security. And some of them will be hacked for sure. It means that hackers will definitely be able to exploit that and send messages to your friends. That's why we need a more sophisticated “communication protocol”. In MetaTalk you will just deactivate the compromised key and all messages will be marked as unverified. Ok, so where will you store messages? There will be special nodes - Storage Nodes. They will provide api access for messages access / message sending. How will you protect users from sending SPAM? When user will add new contact - some NEAR tokens will be locked in a smart contract. If target user will not accept request - that tokens will be lost. Whats next? Well, not sure. I am going to polish base functionality and try to find some existing games, which will integrate it into their games. At this stage - its a prototype only. <div