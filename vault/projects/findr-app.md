---
slug: "findr-app"
url: "https://devpost.com/software/findr-app"
title: "FINDR app"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 816
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/deterministic_policy"
  - "domain/developer_tools"
  - "user/legal_professional"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# FINDR app

> FINDR app is an AI powered Dapp for restaurant goers, reviewers and anybody who is interested in gastronomy to come and gain accurate info on the restaurants in the vicinity.

[Devpost](https://devpost.com/software/findr-app) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[deterministic_policy]]
**domain** [[developer_tools]]
**user** [[legal_professional]]
**substrate** [[geospatial]] [[web_dom]]

**stack** hardhat, java, next.js, react, solidity, springboot

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for the findr app

## Body

logo AI reviewed Review list Maps and details interface Inspiration Reviews play an important role when we decide which restaurant to dine in. We know how easy it has become to write a fake/spam review using AI. This spoils the purpose of reviews. To tackle this problem we introduce FINDR through which you are able to stake a restaurant and write reviews while earning tokens yourself. Our application checks for the authenticity of the reviews which is our value proposition. What it does FINDR is a blockchain/AI-powered review app which gamifies the restaurant review process and offers incentives for restaurant goers, reviewers and anyone who are generally interested in this space. It mainly has 3 important roles User Users may go to the website, where they can look at the restaurants near them on Google Maps type interface and get authentic reviews for the restaurants they select. The frontend talks directly to the blockchain which secures the source of the reviews (as hashes), aggregates them on multiple dimensions such as ambience, food quality, waiting time for dishes etc and offers that as free basic info for the restaurants. Reviewer The reviewer will be incentivised to review the restaurant he recently visited because, if the quality of the review is good on multiple dimensions such as authenticity, the balance of positives and negatives, specificity of a dish etc, he/she will be rewarded with FINDR tokens in addition to the satisfaction of helping the people and perhaps the restaurant improve their quality of service. The main value added is that the AI filters the reviews, makes them palatable and perhaps spits out a final score. This information will be pushed using Chain Link Functions to the blockchain, where the aggregated information + some hash information will be stored. This information can be queried directly by the frontend. Staker Anyone can stake FINDR tokens for the restaurants they like on the website. The restaurants with bigger stakes on them will have a spotlight on the frontend therefore attracting more viewers. They will get to choose what counts as a good restaurant and later earn restaurant-specific benefits. This mechanism would gamify the problem at hand and allow a large pool of people to check out our ecosystem. How we built it We used chain link functions to make sure the reviews can be judged by an AI (Open AI API) as the users submit them. This makes the process trustless as the blockchain stores a hash of the executable file. (params, source-code and the judgement are therefore immutable) We implement a mechanism where users' reputation is based on the tokens they earned by reviewing and staking on the restaurants which inspires people to contribute back. Challenges we ran into Challenges faced in the AI segment First of all, predicting whether the text is AI generated is a hard problem. We had to find good thresholds and decide on a model to predict if the text was AI generated\Spam etc. After we were able to finetune the model to work for the restaurant reviews. We had our code written in Python but we observed that this is unusable with Chainlink Functions. So we had to re-write the whole code in Javascript. We ran into another problem, initially we were just thinking of using a single call to the api. But to replicate multiple call from Chainlink DOM we needed to set the parameters such that model results became semi-deterministic to get a consensus. Challenges faced with ChainLink Functions segment We initially misunderstood a bit. First, we thought, the only way to judge a review is to call the ChainLinkRequest with a URL, get a nested param back and use this in our solidity code. But the problem is AI responds with a rational number which cannot be exponentiated onchain (e^rational_number). So, we discovered ChainLink functions wherein we could execute our own code, but the result is still censorship-resistant and therefore solved our puzzle. Another instance is the gas limit on the ChainLink request cap at 300,000. We had a lot of ops post-request which kept on failing. After a lot of debugging, came upon this and the system is stable thereafter. Challenges faced with Programming languages We are all beginners in typescript/ react, so it was a nice experience to learn a few quirks about this. How to integrate google maps, blockchains and backend together one step at a time Collaboration We were working in 3 time zones each of which had a 6 hour gap. Bringing all the team members together could only be possible due to our group representatives' excellent coordination. Accomplishments that we're proud of -Able to show AI usage in a censorship-resistant way -Prototype a concept app just as we envisioned What's next for the FINDR app -Make the ecosystem more user friendly -AI censorship of unethical reviews -Stylometry on the users -Stake-slashing mechanism with reviews <div