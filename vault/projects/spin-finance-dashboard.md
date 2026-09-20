---
slug: "spin-finance-dashboard"
url: "https://devpost.com/software/spin-finance-dashboard"
title: "Spin Finance Dashboard"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 451
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Spin Finance Dashboard

> Explore Spin Finance spot metrics on NEAR

[Devpost](https://devpost.com/software/spin-finance-dashboard) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**substrate** [[sensor_telemetry]] [[web_dom]]

**stack** near, next.js, postgresql, react, spin

## How they structured the write-up

- technologies
- metrics
- spin finance dashboard api
- adapting the project
- local development
- deploy
- explore other projects:

## Body

Spin Finance Dashboard Live Demo: https://spin-finance-dashboard.vercel.app/ Explore Spin Finance spot metrics on NEAR Spin Finance's spot markets are live on NEAR testnet, but there are no dedicated analytics to track its usage. Traders, investors and other stakeholders want to monitor Spin's performance using charts and metrics. Spin Finance Dashboard draws back the curtain and brings those metrics to the forefront. Technologies Spin Finance Dashboard uses: Instant server-rendered pages + incremental static regeneration using the lastest data via Next.js Latest blockchain data from the NEAR indexer Industry-standard charts and UI via IBM's Carbon Design Framework , by using the Carbon Components & Carbon Charts React packages A responsive, custom-built UI on both mobile and desktop Metrics Volume of orders placed (in USDC) 1 Volume of orders placed per market (in USDC) 1 Number of users Number of orders 1 Note that volume of orders placed is the sum of all ask and bid orders (both market and limit orders) placed by users in a given time period. It does not take into account the removal of orders ( drop_order ). Spin Finance Dashboard API Spin Finance Dashboard exposes API endpoints that anyone can use to obtain key metrics and data. All endpoints require the ?lastHours url parameter (e.g. lastHours=48 ) Additionally, you may specify a groupBy parameter (e.g. groupBy=hour or groupBy=day ) Endpoints: /api/orderCount /api/userCount /volume 1 For /volume endpoint, you can specify an optional marketId parameter which will filter for a specifc market (e.g. marketId=1 filters for NEAR/USDC only) For /volume endpoint, omitting marketId returns data categorized for each market pair. Alternatively, marketId=all returns data summed and aggregated over all markets /api/orders is a data-heavy endpoint and is available for local development only Adapting the project As Spin Finance adds new markets and deploys to mainnet, Spin Finance Dashboard should be able to adapt with ease. Adding new markets Append the market id and market pair name in config.json in the root of the project Changing the Spin spot contract Change the account id in config.json Switching to mainnet Change the account id to the mainnet spot contract in config.json Change the indexer_uri to the mainnet indexer in config.json Adding a new metric Create a new endpoint file in /pages/api for the metric. Fetch the data in this file. Call the API function and process the data in /dashboard/Data.js Use the data in a graph in dashboard/UI.js Local development Clone, run yarn install or npm install and then start the development server: npm run dev # or yarn dev Open http://localhost:3000 with your browser to see the result. Deploy The easiest way to deploy Spin Finance Dashboard is via Vercel: Explore other projects: https://devpost.com/karlxlee https://gitcoin.co/karlxlee Previous hackathon wins: https://github.com/karlxlee/lunatic-score-calculator https://github.com/karlxlee/make-crypto-mobile-hackathon/tree/project/optics_dashboard <div