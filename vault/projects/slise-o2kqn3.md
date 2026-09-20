---
slug: "slise-o2kqn3"
url: "https://devpost.com/software/slise-o2kqn3"
title: "Slise"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 399
team_size: 5
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Slise

> We help Web3 creators to collect and analyze their user data (social + on-chain activity) to know their audience better and do better marketing

[Devpost](https://devpost.com/software/slise-o2kqn3) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**user** [[general_public]]
**substrate** [[structured_db]] [[web_dom]]

**stack** amazon-web-services, axios, bitquery, etherspot, github, heroku, javascript, moralis, mui, nftport, node.js, polygonscan, postgresql, redis

## How they structured the write-up

- the problem
- our solution
- tech stack
- what's next for slise

## Body

The problem Despite all the publicity of on-chain data, the marketing in web3 projects is surprisingly uninformed and is built on intuition and common practices. Because of that, creators waste their time and budget on growth efforts that do not return the expected results. Particularly painful it is for token-based projects in the growth stage when the token is not yet on the market. Today, creators can just guess who will be their future holders and have no ways to reach them, even if they know individual wallets. There are tons of tools that provide a market overview for traders (like Similarweb in web2). Yet, there is still very little available for creators to deeply analyze their own token-based projects and marketing performance (like Google Analytics or Mixpanel in web2) that we connect to the wild nature of the bull market where growth was primarily speculative and explosive. Our solution We've built a Mint list collection and analytics tool for web3 creators to give them control over their marketing and growth. Right now, we concentrate on the pre-mint (growth) stage and allow creators to collect and analyze user data (social + on-chain activity) to understand their personas, learn where to find them, and do 10x more precise targeting. We use proprietary ML algorithms to surface insights on their future holders, connect their web3 and web2 identities, find new opportunities for collaborations, create lookalike audiences for targeting, filter bots, and connect multi-wallet accounts. See how it works in the demo video! Tech stack The Slise project was developed and uses a variety of APIs and algorithms to build analytics on collections and wallets. We used Node.js + TypeScript as the main backend language and also: PostgreSQL as the main database with Prisma ORM, Redis for caching, and AWS S3 for file storage. Deploying to Heroku as a container. Github for version control Frontend app was made using JavaScript, Next.js, MUI, HTML & CSS, deploying to Vercel. We used apex charts for dashboards, axios for communication with backend, and localstorage as frontend storage. To work with the blockchain, we use native web3.js, Bitquery, Moralis, NFT Port, and Polygonscan API. We use etherspot.io as the main provider for EVM networks. What's next for Slise We are happy to announce that we were accepted to the upcoming Alliance cohort which means we will continue building our app with funding and experienced mentors! <div