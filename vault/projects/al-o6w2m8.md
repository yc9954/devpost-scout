---
slug: "al-o6w2m8"
url: "https://devpost.com/software/al-o6w2m8"
title: "AL"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 273
team_size: 0
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/supply_logistics"
  - "substrate/web_dom"
---

# AL

> AL makes financial planning easier, by offering a more natural way to interact with your financial data; through voice & chat.

[Devpost](https://devpost.com/software/al-o6w2m8) · hackathon [[Azure AI Hackathon]]

## Facets

**domain** [[education]] [[finance_payments]] [[supply_logistics]]
**substrate** [[web_dom]]

**stack** azure, nextjs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for al

## Body

AL Chat AL chat actions AL home page AL home page (dark mode) Inspiration For a long time I have struggled to keep a budget; even when I know its value towards financial freedom. I am not alone in this, so I set out to find and build tools to help with getting better at finances in general (literacy, planning and management). AL, is a manifestation of my hope to get better at this and hopefully help others who find themselves struggling too. What it does AL connects to your various accounts; bank, mobile wallets, subscriptions, utility e.t.c and provides a voice/chat interface to manage amounts in and out of these accounts. That's the long term plan, for now the interaction is a little lacking but we will get there. How we built it The bot logic is built using Bot framework composer , leveraging Azure cognitive services for some intelligent handling of conversation. To interact with the bot, I built a website for AL which supports chat and voice (coming soon). Challenges we ran into Configuring bot framework composer to deploy bot logic to Azure took some doing. Getting LUIS to help with nitty gritty dialog details proved challenging. Accomplishments that we're proud of Deploying bot service on Azure Building the website for AL What we learned To build a useful conversations bot, a majority of the time ought be spent in the design and testing. A low-code platform like bot framework composer helps with reasoning through the myriad of paths a conversation might take. What's next for AL Improve bot's chat functionality to support more actions Get voice chat working <div