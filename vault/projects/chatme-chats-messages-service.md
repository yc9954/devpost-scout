---
slug: "chatme-chats-messages-service"
url: "https://devpost.com/software/chatme-chats-messages-service"
title: "ChatMe - Chats & Messages service"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 965
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ChatMe - Chats & Messages service

> All-in-One solution for NEAR blockchain: direct messages, channels, public and private chats, simple integration for any project in NEAR ecosystem. ChatMe is something like decentralised telegram :)

[Devpost](https://devpost.com/software/chatme-chats-messages-service) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**substrate** [[code_repository]] [[financial_record]] [[video_visual]] [[web_dom]]

**stack** ipfs, near, nft.storage, react, rust, thegraph

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chatme - chats & messages service

## Body

Homepage Dashboard Group Chat Direct messages (with privacy mode enabled) Send NEAR tokens Create group/channel Send first message to some account Technical details ChatMe widget integration in our NFT game Inspiration Communication is very important part of every community and ecosystem. The chatMe story started when I use popular NEAR applications and realised that it could be great to send message directly to a NEAR wallet address (NFT holder offer, in-game direct message or project feedback). The next phase started when we were developing clans in our game on NEAR and community requested an internal chat for each clan. All this ideas and requests inspired me to develop service that combines direct messages, public/private groups and broadcast channels. This idea was extended when I started working on this project: how about media files, encryption of private messages (all blockchain transactions is publicly available), sending tokens or avoiding spam... all this have been successfully implemented! Also, I found a way to avoid saving messages in the smart contract storage that make it much cheaper and don't increase the size of smart-contract by sending any message! I use smart-contract logs and collect messages using The Graph indexer. The main idea of our service is to provide our features for any project and account in the NEAR ecosystem, build decentralised messenger (anyone can call our smart-contract to send messages, create and manage communities etc.) and combine all chats and conversations in one place - our web application. What it does ChatMe is decentralised chats and messages system that combine the best user experience, blockchain security, fast and cheap transactions with new web3 possibilities. All our features is open-source and documented to simplify any integration and future updates. We provide chats & messages service for all projects and accounts in NEAR ecosystem. Main features: Send direct messages: text, likes, media files, reply to message, spam reports, send NEAR tokens and private mode (encrypted messages). Create and manage public and private groups, broadcast channels. Integrate NEAR Social profiles to get more details about each NEAR Account. Control of spam and malicious messages. 3 types of user accounts for extend functionality. List of all public groups & channels with ability to join this community. Ability to integrate any project: widget and documentation that describe how to use our smart-contract and service. Use Cases examples: Direct messages. NFT marketplace can implement private messages to send proposals for NFT holders. Private Group for DAO, guilds, clans or other communities. When you create DAO, your contract can call our service to create internal chat for participants. Only DAO members can add new messages. Public Group for communication with your audience. Add public comments into your article, NFT or service. Any NEAR account can join and add new messages. Public Channel to share news, announces or updates. Add announces into your website to show latest updates (can be created manually or automatically through your smart-contract calls on migrate). Store your immutable contract data as messages. Most interesting and non-standard usage: if you need to store huge amount of immutable data in blockchain, you can use our smart-contract. Just create private group and send your data as messages into this group. All data will be available trough The Graph schema in few seconds. How we built it Create new project using "npx create-near-app", rebuild react structure to use Context, add templates and start work on smart-contract logic. After basic setup and few commits I setup The Graph indexer and test ability to send messages using smart-contract logs. When all ideas was confirmed I continue adding functionality: direct messages, groups, integrate NEAR Social profiles, spam reports and user Accounts. Each day I update UI/UX components, allow to send media files, implement messages encoding, export/import private keys that used for encoding, reply for messages, update dashboard, show list of all public groups and channels to give ability to extend public communities. Added unit tests for smart-contract and upload to NEAR testnet. Start work on documentation to describe integration all features for other NEAR projects. Completed first version of chatMe widget that allow implement chat/channel functionality inside any react project: github repository . Continue work on documentation updates: documentation and pitch deck . Challenges we ran into How to store messages to avoid contract storage grow. How to minimise Gas usage. How to minimise spam messages. How to create private encoded conversation between two users. How to combine all chats & conversations in one list of latest chats. How to integrate NEAR Social. How to send media files: use IPFS (nft.storage). How to develop simple system that any project or user can use. How to provide the best user experience for chats and conversations. NOTE: I used IPFS, that's why images can load with small delay. NOTE: For now library that I use for encoding (@nearfoundation/near-js-encryption-box) marked as "experimental library", that's why I add next message in dashboard: For private conversations, you can use "Private Mode", but we recommend not to send any personal/sensitive content. Accomplishments that we're proud of Small Gas usage (~7 TGas per message). Fast message delivery (3-5 seconds). NEAR Social integration. Private mode (encoded messages). Send NEAR tokens in direct conversation. Connected multiple wallet providers. Spam protection and rules to minimise spam. Different user account levels that extend functionality. Also account can be Verified to avoid any locks (only for NEAR team and popular projects). What we learned Learn a lot of thinks, most complicated was: creating simple UI/UX, The Graph usage and private mode for encrypted messages. What's next for ChatMe - Chats & Messages service Testing and launch on mainnet. Ability to send any NEP-141 token in NEAR ecosystem. Ability to setup email notification about new messages. Partnership and share abilities with NEAR projects. Marketing. Develop new widgets. Improve documentation. Performance optimisation. <div