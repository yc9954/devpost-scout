---
slug: "ghosty"
url: "https://devpost.com/software/ghosty"
title: "Ghosty"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 771
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "domain/security_privacy"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Ghosty

> A messaging platform for NEAR users to simply and instantly messaging across wallet-to-wallet on the NEAR network.

[Devpost](https://devpost.com/software/ghosty) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[privacy_tech]] [[realtime_stream]]
**domain** [[security_privacy]]
**substrate** [[financial_record]] [[structured_db]] [[video_visual]]

**stack** chakraui, express.js, google-cloud, heroku, javascript, mongodb, near-api-js, nextjs, node.js, socket.io, tailwindcss, vercel, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ghosty

## Body

Ghosty Homepage Login Near Wallet First User Login Ghosty Room Chat Set Nickname Address Mobile Homepage Mobile Responsive Add User Address Mobile Responsive Chat List Emojis Inspiration Do we feel how important communication is, when we communicate everything feels close and warm, one of which is on Web3 where we sometimes need to communicate between addresses of other users connected to this blockchain network, therefore the idea came to our mind✨ And the reason why I'm named Ghosty, because in the blockchain world we don't know and there are lots of wallet addresses that I define as blockchain ghosts👻 There are several important points why Ghosty was created: On the blockchain, users are restricted from communicating directly from wallet to wallet of other address. Between user address can give each other offers or cooperation in a project via chat between wallet-to-wallet. Warns about exposure to smart contract vulnerabilities. What it does Ghosty app is built using socket.io for real-time communication between wallet-to-wallet. Socket.IO is an event-driven library for real-time web applications. It enables real-time, bi-directional communication between web clients and servers. Ghosty App Flow: The user will be directed to the NEAR wallet for the login authentication process --> At this stage Ghosty will store address data in the form of the accountId property into MongoDB which is obtained from the NEAR login authentication process. When successfully logged in, the user will be immediately directed to the chat page --> The chat page in question is the CHAT ROOM INTERFACE User adds the user address in the Add Address modal --> In this process the user will search for the NEAR user address by calling nodeUrl with the following property: jsonrpc: '2.0', id: 'dontcare', method: 'query', params: { request_type: 'view_account', finality: 'final', account_id: <wallet_address>, } if the value sent is the same and the user adds it, the accountId will be post to database alias: <accountId> In this process the user can send a message in the form of text, images, and also emojis that have been provided by Ghosty. --> All these processes are done with the help of socket.io for real-time wallet-to-wallet communication. Login with NEAR Wallet Add wallet addres Let's Talk!👻 How we built it Frontend: Frontend application uses the React library with the Next.js Framework, using near-api-js for interact NEAR Blockchain, TailwindCSS⚡️ChakraUI for styling. Backend: Javascript compiler uses NodeJs with Express Framework + event-driven uses Socket.io for real time web application and is hosted on Heroku for the Back-End. MongoDB for storing data. Some other libraries using Zustand for state-management. Challenges we ran into I learned from several variants, modules, libraries and several frameworks to create a real-time chat application by integrating NEAR Blockchain as a login authentication process. The most challenging is how the user can always receive data instantly without recursive sent by the user's address with socket.io, then there are still several challenges in the future in developing Ghosty, one of which is end-to-end encryption, and how chat can be stored on-chain. Accomplishments that we're proud of Chat application that utilizes NEAR Wallet for the authentication login process which of course can make it easier for user addresses to communicate between wallet-to-wallet. Many useful and productive features for the future such as extensions, and also buy or sell an NFT. An elegant UI design by taking a monochrome theme that is pleasing to the eye and comfortable for every user who is communicating. Ghosty has provided an emoji feature and can also send pictures. What we learned At some points that we have done, of course, there is a huge potential for business opportunities when we try to make a project by linking it to the Blockchain, without me realizing that business ideas are very expensive and valuable. This is a very valuable experience for me in participating in MetaBUILD to build and participate in the NEAR Protocol network, where my curiosity is getting higher to explore the world of Blockchain especially wanting to develop and execute the Ghosty feature in the future. What's next for Ghosty Of course in the future I will integrate features that are still in the development stage such as end-to-end encryption, dark mode, and chrome extension. Improve team. Automated unit test creation. Create group chats as well as global ones by dividing them into multiple servers. Design a business model (already have several options). Create NFT avatars / emojis which can later be used to change profile photos and can share stickers via chat. Can make NFT transactions by integrating them into several NFT projects or marketplaces that run on the NEAR ecosystem. Let's Talk with Ghosty👻 <div