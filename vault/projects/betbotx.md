---
slug: "betbotx"
url: "https://devpost.com/software/betbotx"
title: "BetBotX"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 696
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# BetBotX

> BetBotX: Social betting platform on Twitter—wager on sports and crypto with blockchain-secured markets, real-time accurate resolution, and transparent payouts. Join the future of social betting!

[Devpost](https://devpost.com/software/betbotx) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[financial_record]] [[web_dom]]

**stack** github-actions, google-cloud, python, react, tweepy, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned

## Body

BetBotX Inspiration I was inspired by the freedom of creating my own bet ideas from platforms like Kalshi. The idea of formulating unique, personalized wagers and having them securely executed on a blockchain captivated me. I envisioned a platform that merged the spontaneity of Twitter with the transparency of decentralized finance—a place where anyone could bet on sports, crypto, and more, all through simple tweet commands. What It Does BetBotX is a Twitter-native betting platform that allows users to: Create Markets: Launch betting markets on various events (sports, crypto, and more) with a simple tweet command, with direct integration to a web app for authentication. Place Bets: Wager on the outcomes directly from Twitter using straightforward commands, , with direct integration to a web app for signing. View Market Information: View all currently active markets, specific information for a particular market, and all bets made by a specific address, all from Twitter. Automatic Resolution & Payouts: An off-chain oracle fetches real-world data from sources like The Odds API and CoinGecko to resolve markets automatically, ensuring transparent payouts via the NEAR blockchain. Web Dashboard: A user-friendly web app displays active markets, odds, and pool details, allowing users to track their bets in real time. How I Built It Smart Contract Development: I built and deployed a NEAR smart contract using TypeScript (via near-sdk-js) to manage market creation, bet placement, and resolution with automated payouts. Twitter Agent: Using Python and Tweepy, I developed a Twitter bot that listens for user mentions, parses bet commands, interacts with the smart contract, and responds to user's tweets. Off-Chain Oracle: I created an off-chain oracle service that polls external APIs (like The Odds API for sports and CoinGecko for crypto) to fetch real-world outcomes and trigger the resolution of markets automatically and accurately. Web Dashboard: A basic web app (built with React) was developed to display active markets, odds, and pool information, offering users an intuitive interface to monitor their bets. Additionally, the web app directly enables authentication and signing for the create markets and place bet functionality, through URL-trigger responses to twitter mentions. Challenges I Ran Into Twitter API Limitations: This was the major limitation since the free tier of Twitter’s API imposed really strict limits on the number of mentions that could be read and tweets that could be posted. This required careful scheduling and optimization of the bot’s polling mechanism, but it's difficult to optimize for the number of tweets posted since it's limited to 17/day. NEAR Authentication/Transactions: There was no feasible way to securely keep all the betting functionality solely on Twitter due to the complexities of authenticating NEAR accounts and signing transactions for bet placements. To address this, I separated out the components—maximizing what could be handled directly on Twitter while offloading the secure transaction signing and authentication to a dedicated web app. This hybrid approach lets users initiate actions on Twitter, and then seamlessly complete their transactions via the web interface through specific URL responses populated with all the necessary data in the queries. External Data Integration: Building a reliable off-chain oracle to accurately fetch and interpret data from multiple APIs, each with its own data format, was complex and required creative problem-solving. Accomplishments That I'm Proud Of Seamless Integration: Successfully merging Twitter interactions with blockchain technology, the oracle service, and the React web app to allow bets to be created, managed, and resolved directly via tweets. Decentralized Transparency: Leveraging NEAR’s blockchain for secure, trustless betting and automated payouts, ensuring a transparent process. Innovative User Experience: Creating a platform that transforms everyday Twitter activity into dynamic, engaging betting opportunities. Robust Off-Chain Oracle: Developing an oracle service that bridges real-world data and on-chain logic, ensuring markets are resolved accurately. What I Learned BetBotX has been a journey of innovation and technical growth. Through this project, I learned how to: Develop and deploy secure smart contracts on the NEAR blockchain. Navigate and overcome the limitations of the Twitter API. Build an effective off-chain oracle that integrates external data into decentralized applications. Combine multiple cutting-edge technologies—from social media to blockchain—to create a cohesive and user-friendly platform. BetBotX just shows that the possibilities for decentralized, social applications are endless. <div