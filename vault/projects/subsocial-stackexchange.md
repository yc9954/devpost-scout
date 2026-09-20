---
slug: "subsocial-stackexchange"
url: "https://devpost.com/software/subsocial-stackexchange"
title: "Subsocial Substrate StackExchange"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 478
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/web_dom"
---

# Subsocial Substrate StackExchange

> A decentralized forum for developers Q&A regarding substrate development, made on top of Subsocial parachain

[Devpost](https://devpost.com/software/subsocial-stackexchange) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[web_dom]]

**stack** next, polkadot-js, subquery, subsocial, subsocial-sdk, talisman, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for subsocial substrate stackexchange

## Body

Home Page Ask Question Page Question List Page Question Detail Page Profile Page Edit Profile Page Followers Page Inspiration This project is inspired by subsocial bounty for this hackaton, which is decentralized Substrate StackExchange . What it does Create a forum between substrate developers to help each other. All the posts, replies, answers are saved in IPFS and Subsocial Parachain , which made the connections you made in here (following/followers) are portable in another social app made on top of subsocial. It also becomes easier to tip other person, for example, tipping the one that helps you by answering your question. How we built it This project is made using next js with typescript . Majority of the web3 interaction is made using subsocial SDK and wallet connection using talisman-connect . There is also indexing service made by subquery for reputation system. Challenges we ran into This is the first time I made an app that connects to parachains, so learning the wallet connection and subsocial SDK is quite a hurdle, especially digging the documentations for both of them. Some features are also not specified inside the documentation, which makes me have to research and dig deeper into the extrinsics of existing subsocial app. The other thing is running indexing service. I have not much experience in infrastructure like aws, so learning ec2, docker, etc to run indexing service is a hard thing for me. Accomplishments that we're proud of The best accomplishments is that I am able to connect subsocial SDK, and also polkadot api (to get balances of each listed parachain) inside react-query with full typescript support, making development after that much easier in term of caching, getting data, mutation, and invalidating queries. This makes the web page updates accordingly after any mutation is done. I have also able to have a ec2 server running subquery indexing service to have a reputation system running in the main website. What we learned I learned connections to polkadot api with RPCs, connection to wallet using talisman, and most importantly connection to subsocial chain using their SDK. I also learned to dig into block explorer and extrinsics inside parachain, learn how to see and interact with them inside the polkadot js wallet. AWS EC2, docker, and managing networking inside the EC2 is quite a challenge for me that I have to learn in this project. Other thing unrelated to web3, learned about slate which is customizable textarea. What's next for Subsocial Substrate StackExchange Currently because of the limitation of time, many features are not implemented yet. Here are some of them that I think of currently: SSR content for better SEO. Better reputation system. Connection to subsocial offchain (or subsquid or subquery), to show better filtering of content (e.g. search question, filter by tags, etc.) More tokens inside tipping list Responsive design Better text area customization and feature <div