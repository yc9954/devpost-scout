---
slug: "dupe-defend"
url: "https://devpost.com/software/dupe-defend"
title: "Dupe Defender"
hackathon: "Constellation: A Chainlink Hackathon"
organization: "Chainlink"
winner: true
words: 341
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
---

# Dupe Defender

> Defend your creator rights seamlessly by using Chainlink Functions, Polygon ID Verifiable credentials and Account Abstraction from Alchemy

[Devpost](https://devpost.com/software/dupe-defend) · hackathon [[Constellation- A Chainlink Hackathon]]

## Facets

**domain** [[developer_tools]]

**stack** alchemyapi, ethers, forge, solidity, typescript, viem

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dupe defend

## Body

Homepage Flow Wallet Info Inspiration We felt like that there is a lot of content that is fake and there will be a genuine need to identify the original from the noise, our experience in web3 says that a lot of times there is friction in using a new application, so we wanted to make something that is easy for people to use that allows creators to verify that their content is theirs. What it does Allows a youtube content creator to add a verifiable credential of their youtube video content using account abstraction on the polygon iden3 platform How we built it We used chainlink functions + polygon id + web3 auth and for the account abstraction we used Alchemy's light account Challenges we ran into On the AA part, ran into some issues with biconomy sdk, so switched to Alchemy. On the polygon identity, the examples are catered more towards offchain identity and had to dig through github to get an idea on how to do the integration. Accomplishments that we're proud of We are able to abstract away all the details of how things work to the user. We think that by doing so the users who are content creators have an easy time to validate their work and the usage of these applications will increase. Thereby, reducing fake online content. The app is already fully functional and ready to deploy to mainnet. What we learned We learnt about polygon id and Chainlink functions, how AA and paymasters, bundlers etc work. What's next for Dupe Defend We want to create a good polygon schema for this sort of onchain social media data verification and it feels like it is just the beginning. We want to make the claim like a github badge so that the content creators can upload to their youtube videos to show verified content. Need to evaluate the security model and check where we may have gaps We intend to finance the AA operation by asking for subscriptions from premium or heavy usage users. <div