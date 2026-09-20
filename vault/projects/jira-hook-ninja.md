---
slug: "jira-hook-ninja"
url: "https://devpost.com/software/jira-hook-ninja"
title: "Jira Hook Ninja"
hackathon: "Codegeist 2021"
organization: "Atlassian"
winner: true
words: 561
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/housing_homeless"
---

# Jira Hook Ninja

> The all-in-one no-code solution to integrate ANY webhook-supported application into Jira for creating tickets. This is, the first Integration Platform As A Service tailored made for Jira

[Devpost](https://devpost.com/software/jira-hook-ninja) · hackathon [[Codegeist 2021]]

## Facets

**domain** [[housing_homeless]]

**stack** forge, javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for jira hook ninja

## Body

Inspiration In my company after many years of dealing with complex developing pipelines and various ecosystems where many applications need to communicate over webhooks with Jira to ensure automated reporting (bugs, stories, tasks, and epics), we and many others always end up abandoning the task of automating it and resorting to doing it manually. This is because not every application/tool has an integration app in the Jira Marketplace, and even if it has an integration app, most of the time you lack control over what to do, you get a webhook and it creates a ticket with minimal to none possibility of running your own logic. So you have 2 options, either you build a layer between the reporting application/tool and Jira, and you have to deal with code, maintenance, and infrastructure cost. Or you rent an integration platform (IPaaS) hoping they have a robust enough system to run your logic, and BTW, this IPaaS tend to be very expensive and cost prohibited especially for small startups. Either way, by the end of the day you feel like you had to move mountains just to handle simple automation. What if we can take the best of both worlds? to have an interface layer powerful enough to run any logic you might think of without having to learn a new programming language or even having to use one! and without having to host it and maintained it. If this sounds amazing to you, JIRA HOOK NINJA is for you 🤩 What it does Jira Hook Ninja allows you to create infinite webhooks listeners and attach to them what we call flows. A flow is a small application created using visual scripting, that works by dragging and dropping blocks that describe the application in terms that make sense for humans, so even non-technical people can develop a complex logic. When you receive a webhook, the associated flow is executed, and your logic determines if it needs to create a ticket on Jira and how it should be configured. The robust visual scripting engine in Jira Hook Ninja will allow you to tackle virtually any type of preprocessing you need, thanks to its vast library of blocks available to you, from simple math operators to cryptographic functions. How we built it Using Forge, the cloud app development platform from Atlassian. Backed with NodeJS code, and some great open source libraries, many of them adapted to run smoothly in the Forge cloud engine. Challenges we ran into The first experience with Forge, and like with many other firsts, at the beginning was a bit frightening, but after a few days of tinkering with it, I got the hang of it and learn to appreciate how much easier is to develop a Forge application rather than a self-hosted one. The need to maintain consistency between a flow running in the browser and the same flow running in the Forge cloud means that the same base code needed to be used in the frontend engine and in the backend engine, creating rather complicated challenges due to complexity. What's next for Jira Hook Ninja Better documentation system, so block functionalities can be easier to understand. More blocks; String manipulators, Logic operators (AND, OR, ....), and others. Third-party integration blocks, that will allow services to be integrated directly into flows (Google Analytics, Salesforce, ...) Official release in Marketplace <div