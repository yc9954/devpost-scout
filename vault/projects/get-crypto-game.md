---
slug: "get-crypto-game"
url: "https://devpost.com/software/get-crypto-game"
title: "GetCrypto Game"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 637
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# GetCrypto Game

> This is a card game for newbies in the crypto space, created as a smart contract. It introduces the players to basic concepts around crypto and reinforces best practices for holding crypto.

[Devpost](https://devpost.com/software/get-crypto-game) · hackathon [[Cosmos HackAtom VI]]

## Facets

**mechanism** [[provenance_signing]]
**domain** [[developer_tools]]
**substrate** [[financial_record]] [[web_dom]]

**stack** pylons-sdk, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for get crypto game

## Body

Inspiration Its always the same: Your friends read some get rich quick story somewhere and ask you about how to invest in crypto, but as soon as you start talking about self custody and decentralization, they lose interest. There is no use to tell them that crypto is not about mooning, they just don't get it. How about you could just teach them by playing a game? What it does GetCrypto is a card game for newbies in the crypto space and can be played in groups of 2-6 players. It introduces the players to basic concepts around crypto currencies and reinforces best practices for holding your own crypto. The game is played with two types of cards: event cards and coin cards. The coin cards represent Bitcoin, Ethereum and 20 other altcoins and tokens. They also introduce the players to the concept of "shitcoin". The event cards let you pick up or lose coin cards and introduce topics around security, blockchain related jargon, use cases and community culture. For a complete description of the game mechanics, have a look here (links to the hackatom repo). How we built it For HackAtom VI we want to develop a digital version of the game, minted as NFT on the blockchain. We got the a point where we have an interactive demo, build with HTML / JS, that shows the game mechanics. We also deployed a few test cookbooks and recipes, but due to various reasons (see below, challenges) we couldn't get to a point where the UI is linked to the recipes. Challenges we ran into The initial deployment started using the Flutter SDK, as per (the really useful) presentation during the hackaton launch. Developing without a set of tools to sign transactions in code felt cumbersome and slow, so after deploying a cookbook and a recipe, I decided to build a react app, using CosmJs. And here came the biggest bottleneck: integrating ComsJs with React. The culprit seems to be in the crypto libraries, or support files. The Buffer that is used by ComsJs is not the same as the node package (or viceversa) and I couldn't make it work. I tried to refactor a few times, using the proto files, but to no avail. In the end I switched back to the Flutter test app + Pylons wallet as a signature device + pylons_dart_sdk, only to learn that the blockchain was halted due to a bug. Accomplishments that we're proud of After briefly meeting in person at a crypto meetup in Lisbon, we were able to create a remote team and work together on this one. This gives us confidence in the future steps related to this project (or, to be more precise, gives us confidence that there will be future steps for this project). The UI, the interactive prototype and the graphics, we like them a lot. We also formalized in code the basic structures and we have a good foundation for further development. What we learned We learned to communicate remote, working for a month for a project outside our work hours. From a tech point of view, I (Dragos), got accustomed with the cookbook / recipes ecosystem in Pylons. I see it like a very stripped down smart contract engine, which can be used in many ways. It seems very flexible and easy, while you get the gist of it. Should the tools were more consistent, I would have loved to actually build and interconnect those recipes. What's next for Get Crypto Game We hope to be able to launch a paper version of the game in Q1 2022, so you can play it with friends and family that don't feel comfortable with the digital version. For more info, please sign up to our newsletter or follow us on social media: https://www.getcryptogame.com/follow/ <div