---
slug: "parsedia"
url: "https://devpost.com/software/parsedia"
title: "Parsedia"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 317
team_size: 2
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
---

# Parsedia

> Decentralized social media platform giving users back control over their content and making social media advertising fair for everyone.

[Devpost](https://devpost.com/software/parsedia) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets


**stack** javascript, node.js, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for parsedia

## Body

Inspiration Currently social media platforms give no control for the users over their content, take most of the profits from advertising and often don't open-source their algorithms. We wanted to give users back control over their content, transparency and rewards for their attention. What it does Full functionality was supposed to be social media platform which would be connected to lens social graph, have communities where owners of any NFTs collection could get value from owning it by connecting with other owners of that connection and fair decentralized ads with the ability for users to earn rewards by seeing ads that would be shown while using the dapp, users could decide to share earnings with creators they follow. How we built it We connected our project to lens social graph to provide user with social media features like ability to create a profile, follow see feed and other users. We wrote Ad control contract to which verified dapp can call to get ads to show to users, submit information about which users saw ads and randomly select users to show the ads for. We wrote community and community factory smart contracts which let users join communities if they own nft and create their own custom communities. 4.We used react for the frontend. Challenges we ran into Initially we didn't fully read into all of the features lens offered so we wasted a lot of time coding stuff that we didn't really need. We didn't fully connect everything and complete project because of that. Accomplishments that we're proud of We connected to and used chain link oracle, connected some parts of lens, added dark mode. What we learned We should have created Graphql endpoint and used apollo client and we should have done it from the start. We had to start from lens protocol. What's next for Parsedia We need to finish the connecting lens and contracts. <div