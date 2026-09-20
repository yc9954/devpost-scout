---
slug: "vself"
url: "https://devpost.com/software/vself"
title: "vSelf"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 606
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/financial_record"
---

# vSelf

> vSelf is an Identity-as-a-Service project enhanced by NFT-based gamification. We guarantee full ownership of personal data and bring benefits of the blockchain world to enterprise data management.

[Devpost](https://devpost.com/software/vself) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[financial_record]]
  <sub>weak: web_dom</sub>

**stack** firebase, javascript, nextjs, react, rust, typescript, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it

## Body

Mobile app: Home screen Mobile app: Start check-in for quest or event Mobile app: Authorize at quest or event Mobile app: Get reward - NFT Mobile app: See collection of NFTs in the app Mobile app: Achievements Website: QR code for event or quest Web app: Set up NFT reward Web app: Set up NFT reward Inspiration During the pandemics, we saw expensive and flawed Covid-19 infrastructure: it was built to manage users' sensitive data and credentials, however, mostly did not meet modern standards for development. People were forced to share excessive personal data across non-secure channels. At the same time, businesses were pushed to collect their clients’ data without any benefits in exchange. We saw a pattern across different business processes for data governance that could be automated much more efficiently using a single platform. It inspired us to create the vSelf project - Web3 wallet for digital identity with rewards for data sharing. What it does In this demo, we focus on a simple scenario for reward-driven authentication for events and meetups. We have built a mobile app that engages with the users, guiding them through the activities of the events and immediately rewarding with NFTs: Events can set up quests for participants, providing unique NFT collections as rewards. Users can check in to the events via the app and collect NFTs to their NEAR wallet by participating in different activities. In profile, users can choose which data to disclose and see their collection and achievements. Besides, we have a web app that serves as a back-office for event content and settings. How we built it Previously ( title , we've presented to the NEAR community a simpler prototype that demonstrated the main functions for the mobile app. It generated a random collection of NFTs that served as a reward for scanning any QR-code. Since then, we made several improvements, adjusting the platform for the complete user story. vSelf includes: User-facing mobile app built with Unity (iOs, Android) Web application to manage and analyze collected data and set up the rewards and other smart contract settings (Next.js based) Cloud infrastructure and backend code: smart contracts + serverless functions (written in Rust and Node.js) ## Challenges we ran into When we started, we found out that implementing wallet functionality in Unity is pretty challenging for us at this point (and struggled with its SDK for NEAR). So we decided to augment our architecture and introduce an intermediary API service hosted in our cloud and sign transactions on behalf of the Unity app. ## Accomplishments that we're proud of It seems like it works :) We have developed a scalable and forward compatible cloud setup, iterated and brainstormed on our overall architecture and design decisions. Also, we have gained some skills as a team which is always valuable. ## What we learned We’ve had a great first-hand experience with development tools, as well as writing using recent releases of Rust SDK. A lot of boilerplates were designed by our devs, and we definitely feel more comfortable with NEAR tech than before. ## What's next for vSelf Next, we see a bit more general event management system, which is also includes token economy component. We are working to be mainnet ready and add new features, becoming more cloud-agnostic by bringing on powers of IPFS and GUN.db projects. We see NFT as first experiments in the field of verifiable credentials, so we are looking forward to building a more generic data-sharing solution. Big thanks to NEAR community for support and warmth. Shout-out to Human Guild and many other community members who were supporting us along the way. <div