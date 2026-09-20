---
slug: "bot-calling-bot"
url: "https://devpost.com/software/bot-calling-bot"
title: "Bot Calling Bot"
hackathon: "Power Up Automation"
organization: "UiPath"
winner: true
words: 246
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/housing_homeless"
  - "substrate/financial_record"
---

# Bot Calling Bot

> It is a UiPath bot manager framework aims to function as a workload manager for robots

[Devpost](https://devpost.com/software/bot-calling-bot) · hackathon [[Power Up Automation]]

## Facets

**domain** [[housing_homeless]]
**substrate** [[financial_record]]

**stack** uipath-orchestrator-api, uipath-studio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bot calling bot

## Body

Inspiration Manage and distribute workload between robots for efficient utilization of all available robots is either tedious or not viable with Uipath built-in capability What it does UiPath Bot calling Bot framework aims to function as a workload manager for robots by distributing transactions across available robots even across multiple tenants and orchestrators How we built it We have used UiPath Orchestrator APIs to build the framework. A new transaction for a process is triggered by creating a transaction item in the master queue. A master robot runs non-stop as back-end process checking for requests in master queue. The master bot check the back-end configuration to find out robots which are configured for the corresponding process and dispatch the transaction and wakes up a robot based on its availability. Challenges we ran into Although Uipath Orchestrator API are well documented, it took some time to explore and choose apt API call for the job in hand. Managing adn dispatching queue items, bots and enabling the framework work across multiple orchestrator/tenant came out as bit more challenging than we expected. Accomplishments that we're proud of Proud to make the framework work the way we intended What we learned We have learned the power of collaboration, team spirit, innovative thinking & problem solving. This project also help us in understanding the importance of well defined plan and time management What's next for Bot calling Bot Looking forward to demonstrate the capabilities of the framework with our customers <div