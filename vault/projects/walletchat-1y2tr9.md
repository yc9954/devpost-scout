---
slug: "walletchat-1y2tr9"
url: "https://devpost.com/software/walletchat-1y2tr9"
title: "WalletChat"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 1026
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# WalletChat

> Wallet-to-wallet chat program, offering API integration as well. We use a mix of web2 and web3 for the backend, a standard REST API for message routing and IPFS to store the message data itself.

[Devpost](https://devpost.com/software/walletchat-1y2tr9) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[cross_origin_web]]
**substrate** [[geospatial]] [[structured_db]]

**stack** alchemyapi, go, infura, ipfs, mysql, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for walletchat

## Body

Sequence Wallet Integration - Connect Wallet Modal Sequence Wallet Connecting to Spheron Hosted Instance Spheron hosted walletchat main page after login, all messages on IPFS POAP integration and Polygon NFTs Inspiration Our inspiration was after seeing many people chatting in Discord across NFT projects trying to find owners of NFTs, sometimes for theft reasons, sometimes for trades, sometimes because they won a prize or giveaway but the NFT project owner could not reach them directly. Walletchat was born out of this use case! Since then we realized that was a fairly narrow use case and branched out to more use cases, including POAP integrations. What it does Wallet-to-wallet chat program, with focus on NFT context and workflow. Also aim to support an API that others can integrate if the front end does not meet the project needs. We support POAP and NFT based community chats, so you can chat wallet-to-wallet with your peers from a recent event or other holders of your favorite NFTs. We also wanted to do our best to use decentralized hosting services so we used Spheron, and also integrated Sequence Wallet which is very nice for quick spin up. We also incorporated IPFS, and setup a dedicated Infura gateway for maximum speed. Wallet-to-wallet chat: Chat with any address in any EVM chain. Networking in-event and post-event: We support POAP so you can chat wallet-to-wallet with your peers from a recent event such as hackathons. Community discovery and building: We support NFT-based community chats, so you can chat in a NFT contract context (e.g. Pudgy Penguins holders coming together to chat and interact). This is not restricted to OpenSea-listed NFT collections; it can be ground-up. For example, collectors who just minted an NFT of a new NFT contract in mint.fun can gather together, speculate or build community vibes without the typical Discord or Twitter setup. Options for connections: WalletChat is a webdapp in addition to being a chrome extension ( https://chrome.google.com/webstore/detail/walletchat/cagioajkfaodnmocikaceihiobbcnime?hl=en ). Connections through MetaMask, WalletConnect, Coinbase Wallet are supported. To make onboarding easier for web2 users, we use Sequence Wallet where users can sign up using an email address and password, or with Google, Facebook or Apple. How we built it We use React for the front end, and typical web2 REST API to route the messages and store some data in a MySQL db. The message contents are stored in IPFS, and we hope someday to use libp2p for message routing and peer discovery, once this becomes a bit faster so we can move to being more decentralized! We use Figma for prototyping and graphic assets, which are later translated into front-end code using React with Typescript. We use IPFS for storing of messages, REST API to route the IPFS hashes (which contains the messages), and a MySQL database to store them. To move towards decentralization, we hope someday to use libp2p for message routing and peer discovery, and build a way for users to backup and restore messages independent of dapp. Challenges we ran into We ran into some challenges being able to get all these changes made and testing while our team was on opposite ends of the world. But we made a few live versions of the product so we could deploy to one while leaving the other in tact, so we always had a working version live, and it allowed each of us to work without being forced to integrate changes we didn't make ourself without live support. Unlike typical hackathons, we developed the WalletChat webapp and Chrome extension while onboarding new users for testing. We discovered features requested frequently by users and implemented them. We also design the backend to be open so that others could integrate the API into their own UI. To make it easy to onboard web2 users, we integrated Sequence Wallet; users can sign up using an email address and password, or with Google, Facebook or Apple. Accomplishments that we're proud of We are proud of many things, but a nice clean UI/UX is one area we focused on, in addition to the backend designed in a way that others could integrate the API into their own UI. We are also proud that we were able to integrate Sequence Wallet which is super easy to spin up! Also we were able to deploy our UI on Spheron which is pretty cool that its decentralized! What we learned We learned a lot about IPFS and the differences between running nodes and using a third party dedicated gateway. We used Infura, as we didn't want to assume each client could run an IPFS node. In the guture it would be great to see the speed of IPFS increase to that of a dedicated service! What's next for WalletChat We hope to continue to build and get funded, integrate with a trusted platform or wallet dApp to make WalletChat and w2w messaging something that people in crypto come to think of as second nature! We are continuing to build and are looking for funding (find us at twitter.com/wallet_chat!). Support for other chains with significant volume : To support other chains such as Solana and Avalanche where WalletChat is useful to have as a social layer for their NFT communities. Notifications: Messaging apps are useless without notifications. As a first step, we did a Chrome extension which shows number of unread messages to users. EPNS or a similar communications layer would be the next step to ensure users get timely notifications to messages they are interested in, be it in the form of email, to their favourite chat apps like Discord or Telegram. Announcements and communications hub: A hub where NFT holders can vote, play, discuss, speculate in the main contract chat group, or spin off their own groups based on NFT holdings (token gating). And get the latest news and announcements on all projects they are interested in in a consolidated environment. Decentralization: We want to go fully decentralized, making it both possible for anyone to build on top of our layer, and to be censorship-resistant. Integrations: Partnerships and integrations into trusted platforms such as NFT marketplaces, or wallets such as Trust, Metamask, Argent. <div