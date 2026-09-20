---
slug: "aigency"
url: "https://devpost.com/software/aigency"
title: "Aigency"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 434
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/agriculture_food"
  - "substrate/web_dom"
---

# Aigency

> Aigency is a NEAR AI-compatible caching CDN and orchestration engine with a scheduler, shared memory, and usage metering that seamlessly integrates community-built AI agents into any existing website.

[Devpost](https://devpost.com/software/aigency) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[agriculture_food]]
**substrate** [[web_dom]]

**stack** docker, facebook/bart-large-cnn, graphile, helm, kubernetes-(k3s), langchain-js, llama-v3p1-70b-instruct, near-ai, near-bos, nest.js, nltk, openai-gpt-3.5-turbo, openai-text-embedding-3-small, openfaas

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aigency

## Body

cover wtf architecture running agents embedded into the website storing scrapped content Fake Detector Agent on NEAR AI More application ideas The greater vision Thank you! Inspiration When you have a trillion agents, it becomes a pain for the average user to manually select the best one for their workflow. Collecting contexts and making them available to agents for every single agent call is also a pain. On the Web it is also essential to have a smart cache for faster delivery and cheaper agent calls. All in all, we need meaningful automation to make all those trillions of agents work smoothly for users. Fortunately, it seems possible to automate agent selection and orchestration based only on user goals (such as earning money, staying informed, avoiding abuse), site purposes (such as betting, social networking, or media outlet), and agent descriptions. Mutable Web technology provides seamless agent integration into the user workflow and context harvesting for agent calls. Automatic agent orchestration and seamless integration everywhere is Aigency's vision. What it does Aigency is a NEAR AI-compatible caching CDN and orchestration engine with a scheduler, shared memory, and usage metering that seamlessly integrates community-built AI agents into any existing website. Users are intended to pay-per-use and earn-for-contribution. How we built it Frontend: NEAR BOS on Mutable Web, TypeScript, React Backend: NEAR AI, LangChain JS, OpenAI text-embedding-3-small, Kubernetes (k3s), OpenFaaS, Helm, Docker, TypeScript, Nest.js, Graphile, PostgreSQL, TypeORM Associative Summarizer Agent: facebook/bart-large-cnn, pgvector, Python Crawler Agent: puppeteer, TypeScript Fake Detector Agent on Aigency: OpenAI gpt-3.5-turbo, Python Fake Detector Agent on NEAR AI: NEAR AI, llama-v3p1-70b-instruct, Python Sentiment Analysis Agent: NLTK VADER, Python Challenges we ran into NEAR deprecated BOS as a whole instead of fixing it (which is possible!), and now it is slowly eroding. NEAR AI API calls are slow. We have reported some NEAR AI Bugs: https://github.com/nearai/nearai/issues/962 https://github.com/nearai/nearai/issues/963 Accomplishments that we're proud of It works as an early MVP. Aigency seems to be a great business case: closer to end customers, more efficient UX and delivery, flexible enough to host different applications and adopt the best AI services. Mutable Web has proven its usefulness once again. What we learned Technicals: NEAR AI, LangChain JS, OpenFaaS, pgvector. Container management in Kubernetes using HTTP API. Business: great business cases for AI + Mutable Web. What's next for Aigency Business: validate business cases we have found. Technicals: Finish two ways Aigency Telegram integration for human assisted orchestration. We have it already running in the early-stage, but we need to spend more time on it. Automate AIAgent selection based on user goals. Refine usage metering and introduce costs/reward calculation. <div