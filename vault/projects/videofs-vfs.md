---
slug: "videofs-vfs"
url: "https://devpost.com/software/videofs-vfs"
title: "VideoFS (VFS)"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 980
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "mechanism/vision_ocr"
  - "domain/labor_employment"
---

# VideoFS (VFS)

> Decentralised content and managment services. Giving creators the freedom to switch between platforms in a click, remain uncensored forever no matter what and choose how they get paid!!

[Devpost](https://devpost.com/software/videofs-vfs) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

**mechanism** [[revocation_withdrawal]] [[vision_ocr]]
**domain** [[labor_employment]]

**stack** ipfs, nestjs, typescript, vue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for videofs (vfs)

## Body

Purpose of video fs Inspiration Recently i noticed saving videos offline on youtube in good quality (720P and 1080P) now needs premium. While i understand companies need to make money and youtube is not wrong. But It got me thinking how companies change their policies and agremments overtime without considering their user base and then the content creators are also locked into the platform and there is no easy choice for both. There is also no easy way where creators could choose which type of monetisation stratagey ( pay per miniute etc ) they want. Uploading same video on many platform's is also cumbersome. There is also all forms of imperfect ai and powerful entities censoring a certian type of content or content owner, maybe sometimes even threatening them with lawsuits etc. Looking at all this one might say orgs nowdays have soo much power over what people can do on their platforms but it doesn't have to be this way. If creators could leave platforms ,users would follow suit and people may have more say in the end. To address all these issues i made VideoFS Its a decentralised storage for pointers that point to videos uploaded on IPFS which allows user to grant access to their content to any platform they want and till they want. Making it seamless to integrate with platforms they choose join. What it does It allows user to upload content once and share it on many places( different platforms like youtube ) with a click or two. It allows user's profile (could be anonymous but linked to some web3 identity) to be attached to their channel and content thanks to IPFS Cids It allows users to revoke access of their content on platforms if they are not happy with platform in any way possible Allows users to get paid in web3 native ways from get go Allow users to have a choice over which platforms monetisation stratgey they prefer, their policies, t&ncs etc etc. Allows users to issue tokens natively tied to their account and channel to their loyal viewers and in best paragmatic ways. No need to wait for platforms to implment smart contract support etc How we built it We first found a way to attach profile of users to their channel and videos (all decentralised and verifiable) and provide them freedom to be anonymous if they want but at same time assoicated to some form of web3 identity like hedera accountID. Then we built a video uploading and processing functionality (transcoding, thumbails etc) that uploads the videos to IPFS and also links user's profile and channel identity with that video Then we integrated Hedera topics to make sure the pointers to these videos and identities is never ever censored and stays decoupled from api gateway for persistence purposes and real ownership. We made a platform layer (incomplete) which will allow users to provide access to view and manage their content from 3rd party platforms like say youtube ( should the user want other awesome features from these awesome platforms in future like advanced AI processed video etc) . The final change will always need user's permission before modification unless they allow for more permissions for a vendor in api gateway Challenges we ran into Most of the days were spent researching about other projects and what meaningful use cases could be built over them and that lead to lack of sight till the aderline kicked in and at that point we only had 7 days left.. This time constraint lead me to sprint for 7 days since im alone in my team. And this was one of the biggest challange for me which does show its mark in some places Next we had issues getting a async architecture built for video uploads and processing (that to with resume support) but i wasn't going to be satisfied with mediocre implmentation and it took quite some time We had hard time coming up with ideas and interfaces to implment this whole paradim of IPFS based identities and signatures and what not and connecting them to hedera account keys and topics Accomplishments that we're proud of Even with this huge time constraint im very proud that i was able to pull through this to at least 90% of my expectation. New Ways to attach and verify ownership of content based on signatures and IPFS objects. I choose rigirous implmentation for certain things which i was doing first time like resumable server and video processing etc and got really frustated, having to go back to pen and pair repeteadly but in the end it turned out to be really well done and async in nature. I like how well the whole application works now and is soo much maintainable apart from some shady interfaces here and there. Also the whole project is in typescript and highly rigrious NestJS for server which has made a huge project a breeze for me for most part. What im not proud of is not being able to make the platform layer more demonstrable and the show real power of it. What we learned About IPFS and Web3.Storage About hedera smart contracts API gateways like this (VideoFS) might be a confluence between web2 and web3 in one of the most scalable ways possible To not sprint in a marathon but save energy and make progress consitently What's next for VideoFS (VFS) More finished and complete platform/vendor layer. Add encryption and key managment to prevent user's content from being watched without permission by unauthorized entities over internet More ways to get users paid without much hassle from platforms More types of Smart Contracts for users to choose from for tokens etc Fix Rough edges and make it industry capable. Looking for more people interested in such type of ideas Look for possible entities interested in funding such idea further <div