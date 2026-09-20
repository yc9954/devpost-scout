---
slug: "near-visualizer"
url: "https://devpost.com/software/near-visualizer"
title: "NEAR Visualizer"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 270
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# NEAR Visualizer

> The visual blockchain explorer for NEAR

[Devpost](https://devpost.com/software/near-visualizer) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** near, next.js, postgresql, react

## How they structured the write-up

- intro
- technologies
- add new visualizations
- local development
- deploy
- explore other projects:

## Body

NEAR Visualizer Live Demo: https://near-visualizer.vercel.app/ The visual blockchain explorer for NEAR A submission for the NEAR Metabuid Hackathon Intro NEAR is a fast, scalable, carbon-neutral blockchain. With sharding, NEAR is capable of processing in the order of hundreds of thousands of transactions per second. How can developers, teams, and DAOs sort through millions of transactions to find trends and patterns? How can we understand NEAR data in context to create new features, Dapps or governance proposals? With NEAR Visualizer, you can understand key trends with just a glance. You can also explore your own account ID and any transactions on NEAR visually. Technologies NEAR Visualizer uses: The most up-to-date data via SWR and Server-side rendering Next.js Blockchain data from the NEAR indexer Industry-standard charts and UI via IBM's Carbon Design Framework , by using the Carbon Components & Carbon Charts React packages A responsive, custom-built UI on both mobile and desktop Add new visualizations NEAR visualizer is designed so that anyone can clone and adapt it to their needs with minimal effort. In fact, you can add a new visualization by modifying two main files, without touching the front-end code. Add a data query to queries.js Add the visualization settings and reference the query in config.json The new page will automatically popup on the side-nav. Local development Clone, run yarn install or npm install and then start the development server: npm run dev # or yarn dev Open http://localhost:3000 with your browser to see the result. Deploy The easiest way to deploy NEAR visualizer is via Vercel: https://github.com/karlxlee/near-visualizer https://near-visualizer.vercel.app/ Explore other projects: https://devpost.com/karlxlee https://gitcoin.co/karlxlee Previous hackathon wins: https://github.com/karlxlee/lunatic-score-calculator https://github.com/karlxlee/make-crypto-mobile-hackathon/tree/project/optics_dashboard <div