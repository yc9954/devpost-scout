---
slug: "3card"
url: "https://devpost.com/software/3card"
title: "3card"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 631
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/finance_payments"
  - "user/general_public"
  - "substrate/financial_record"
---

# 3card

> A social platform thats cover all you need in web3

[Devpost](https://devpost.com/software/3card) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[finance_payments]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** amazon-web-services, amplify, dynamodb, graphql, nextjs, react, s3, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for 3card
- contact us

## Body

Message Card of the day Post NFT Post Home Profile Inspiration Existing social media have separated social graphs, which means different apps will have to bootstrap their user base. Given the effort of growing the social graph is so huge, aggressively monetizing the user base will be the next step for the popular app. However, the merit of web3 makes shared social graphs possible. As a Twitter and crypto lover, I always want to build a social platform designed for crypto people and have a great user experience just like Twitter. Thus, we bring this idea into an experimental project built on top of Lens protocol, a composable, decentralized social graph. Just like Twitter, people can post their creative minds, build communities, and meet others. The difference is that creativity is rewarded directly, communities are more crypto-focused, and the platform recommends others with your on-chain activities. What's more, people can even sell their NFT through posting. In short, this is a project by crypto degen for crypto degen. WAGMI. What it does On 3card, a user can: Sign in with their web3 wallet and create a profile. Browse the latest and hottest post feed as well as the newest update for web3 projects gather from 500+ RSS feeds. Post, comment, and repost interesting thoughts and earn from their post. Browse profile with posts, comments, reposts, NFTs, and transactions on the same page. Get the most relevant user card recommended by on-chain activities every day to make news friend Search users by name, handle, or address, and send messages to them directly. Browse and join communities. Make a P2P NFT sale by posting. How we built it Frontend (Next.js + Tailwind CSS) Backend (Next.js + AWS amplify) Storage (IPFS + AWS Dynamo DB + AWS S3) API - (Lens graphql + Appsync graphql +Etherscan API + Coingecko API) News feed - (RSS + AWS lambda) NFT Trading - (Seaport) Challenges we ran into Integrating multiple data sources - we have many data sources, such as Lens social graph, news feeds, user messages, on-chain data, etc. It's a hassle to understand all of them, structure them, and make a readable display. Managing complex application state - as the project is a social platform and there are many data involved, the complex user interaction and frequently updating data make state management of the application a hard task. Unfamiliar tech stack - We learned basically everything from scratch in this hackathon, including Lens protocol, Next.js, AWS, and Tailwind CSS. Limited manpower and short time frame - we only have 3 teammates, and two of them are having full-time jobs. Accomplishments that we're proud of We successfully build the project that integrated both web2 and web3 technology with great UI/UX in less than 3 weeks. What we learned How to design a serverless infrastructure. How to design a seamless consumer-facing app How to work asynchronously What's next for 3card We hope we can launch our beta version and serve more users afterward. What we are going to do next: Improve the recommendation system/ advanced filter and make it pluggable - users can choose different kinds of ML models to have different feeds experience. Complete P2P asset trading - add different trading patterns and fine-tune the UX. Improve user experience - add media content, markdown editor, tags, mentions, and improve message experience. Add P2P lending market - use social graphs & on-chain data to calculate interest rates, make POST-TO-BORROW (LEND) available, and design credit scores. Mobile version - add IOS/Andriod version NFT P2P trading post google chrome extension - Add a google chrome extension to make upgrade any web2 social media post function. Contact us If you have any feedback or idea, feel free to find me on: Twitter: https://twitter.com/billionxdev Email: jeffreylin0723@gmail.com Discord: jeffrey0723#3551 Telegram: @jeff0723 <div