---
slug: "pharo-acmm"
url: "https://devpost.com/software/pharo-acmm"
title: "Pharo ACMM"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 939
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/finance_payments"
  - "substrate/sensor_telemetry"
---

# Pharo ACMM

> Providing liquidity for volatile events on and off chain. Automated cover market maker.

[Devpost](https://devpost.com/software/pharo-acmm) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[civic_government]] [[finance_payments]]
**substrate** [[sensor_telemetry]]

**stack** ant, chainlink, css, fastapi, numpy, python, react, recharts, scipy, shib, solidity, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pharo acmm

## Body

Eye of Ra Inspiration It’s been over six months since Pharo placed in the April Chainlink Hackathon , and we’re excited to participate once again! Chainlink is unique in its ability to validate off-chain data, and we’re looking forward to building Pharo markets around services like currency pairs and weather data . Each new market is a custom contract that utilizes Chainlink Adapters to bring the data on-chain, and Chainlink Keepers to monitor that feed and trigger the Pharo event. We developed this concept during the April hack, and we're excited to build a working version as our submission for this November hack. We recently completed our Thorchain Discord Experiment and are excited to expand into Mumbai testing with SHIB volatility cover as our hack project. What it does Since the last hack we've proven our Wisdom of the Crowds approach works, and the python code powering our WoC algorithm we've wrapped as an API service. Having this API to begin the hack enabled us to build our first market: SHIB Volatility Cover , which we'll be submitting as our project. To launch SHIB Volatility Cover on Mumbai we're asking users the question: "By when will SHIB have dropped by 15% or more? . Users are required to answer this question, as well as their minimum coverage requirement, to enter the market and be eligible for Pharo Rewards. The Pharo API calculates the wisdom of crowds and provides users a Quote, Pharo Staking records users' market positions, and Pharo Anubis settles payments. Since this is testnet, rewards will be a share of $25K in PHRO token rewards. How we built it We can break our hack development into three parts: 1) UI/UX 2) Adapter & Keeper Data Triggers 3) UI - Contract - Algorithm Integration UI/UX The front-end is built with react, ant-design, tailwind css. The dynamic data population of the graphs in the advanced view of the buy cover page is achieved by using react-hooks and react recharts module. The UI is responsive thanks to tailwind css. Data Trigger Integration We entered the Chainlink hack with the Pharo Wisdom of Crowds algorithm complete, but there are always integration issues. Using the python FastAPI package allowed us to quickly iterate new data, structures, endpoints, and general flow of the algorithm’s answers to compliment the front-end UX and adapter-keeper contracts. Challenges we ran into Time vs space user estimates The Pharo Wisdom of Crowds Algorithm is an MVP focused on time series data, which worked great with our Thorchain test which asked, “How long until Thorchain is hacked again?” It seemed a natural extension to apply the same approach to sports bettering and ask, “How many more points will the Raiders score than the Cowboys?” Unfortunately this is not a time based question, the event can only be triggered at the end of the game, so we pivoted to SHIB volatility cover , which required an intense few days of collaboration with our advisors. We chose SHIB for many of the same reasons sports was appealing: large existing market and a clear use case. Distilling these reasons took days of hypothesis testing. Unavailable data in sports feeds In addition to the time-series issue with sports bettering, the Chainlink sports feeds don’t currently provide a “Game Over” flag. We began looking into creating our own, but the effort would have distracted us from our main objective of launching on Mumbai. The Pharo API: UX simplification w/ quotes and rewards As a new member to the team it took Fahim time to grok the Pharo application and logic of the apis. Insurance and cover is usually determined BEFORE users get involved, but Pharo quotes and rewards vary as users enter the market, as the Wisdom of Crowds matures, and reflecting this in an intuitive interface was a challenge. We had to guide users through the rate estimate decision process by showing where the market is, where it will be if they’re right, and what they get for taking the risk. Charting Wisdom of Crowds The Wisdom of Crowds needs to be reflected in an intuitive interface, and finding the right charting module for react was a trial and error process. While we started with D3js, however Recharts was the option with the least amount of development required to achieve our UX goal. Accomplishments that we're proud of Pivoting from Sports Bettering to SHIB price volatility Building a custom price feed for SHIB Populating front-end graphs with swagger-hub API data. Custom Adapter-Keeper contracts What we learned How to know when a Pharo event trigger question is Time parallel vs Time series Examine your data and formulate a plan before starting the data graph Pharo event trigger precision is limited by gas required by the keeper network. Better auto-payment architecture for scaling Pharo markets beyond SHIB What's next for Pharo ACMM Pharo has been steadily progressing and we’re proud to be launching on the Mumbai testnet! We’ll first be testing with the assumption that Liquidity Providers have already staked in our SHIB market, so after testing by opening buying cover to our thousands of discord members, we’ll expand to dynamically adding liquidity as well. We’re minting Pharo NFTs! This will be in parallel with our Mumbai testing, and these aren’t just any NFT; in addition to governance staking capability, we’re including the very special property of staking these NFTs to collect a dividend percentage from all Pharo markets, giving them intrinsic value within the Pharo ecosystem. Once Pharo is tested and NFTs are minted, we’ll officially launch Pharo with our TGE! From there, it’s all about building profitable relationships with Market Makers :) <div