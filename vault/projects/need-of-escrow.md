---
slug: "need-of-escrow"
url: "https://devpost.com/software/need-of-escrow"
title: "AI Agents for Need Of Escrow"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 523
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# AI Agents for Need Of Escrow

> AI-powered enhancements for an online collaboration platform to improve compliance and streamline dispute resolution.

[Devpost](https://devpost.com/software/need-of-escrow) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**domain** [[finance_payments]]
**substrate** [[regulation_legal_text]] [[sensor_telemetry]] [[web_dom]]

**stack** amazon-web-services, apigateway, cdk, jest, lambda, next.js, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for need of escrow
- api usage instructions

## Body

dispute resolution on Need of Escrow platform dispute resolution API compliance validation on Need of Escrow platform compliance validation API Inspiration I've created Need of Escrow project in past and I always wanted to integrate AI for certain needs like task name and description validation with compliance rules. Dispute resolution may also be complicated, so, having Ai assistant is beneficial here. What it does The project itself consists of 3 parts - two Ai Agents(compliance validator and dispute resolver), AWS Api on top of them for convenient usage and the third piece is integration it into Need of Escrow project. How we built it Easily :) Not sure what to add here. I use simple Ai Agents with specific prompts. These prompts return text plus some json message when needed. Then I put AWS Api Gateway on top of near ai api and I've integrated this Api into Need of Escrow project which is written with the usage of Next.JS framework. Challenges we ran into I can't name any. The development was pretty straightforward. There was one bug on near ai side where I couldn't put long enough description in meta file for my Ai Agent but after talking to people in tg channel I found the root cause. Someone from near ai team has created a bug for that. Accomplishments that we're proud of I am glad that Need of Escrow has integration with AI now. If I understand correctly the AI agent is isolated from outer world which means it's safe to post private data to it like task description which might be under NDA. What we learned I've learned that it's pretty easy to spin up Ai agent on near. Ai agent can do many more things than just natural language processing. Although, I see no sense at this moment in using anything other than NLP capabilities for Need of Escrow project. What's next for Need Of Escrow I am not sure with the payment model. Probably, I'll need to investigate whether Ai Agents are free to use on Near or not. If they will be not free in future then I have to understand how Nescrow Admins(special user role who can use Ai Agents on the website) can pay for usage of Ai agents. Api usage instructions Validate compliance: URL: https://pk8p4z13td.execute-api.eu-central-1.amazonaws.com/prod/validate-compliance Method: POST Body: { "taskName": "I need a drug diller", "taskDescription": "I am looking for somebody who can help me with distributing drugs" } Dispute resolution: URL: https://pk8p4z13td.execute-api.eu-central-1.amazonaws.com/prod/resolve-dispute Method: POST Body: { "taskName": "integrate datadog with my microfrontend", "taskDescription": "Integrate datadog into microfrontend application which is built on top of AWS lambdas. Keep in mind that lambda is written in typescript and it uses apollo server for handling graphql requests and express framework for handling http/https.", "ownerComment": "Contractor didn't manage to add lambda metrics. Only logs are present in datadog", "contractorComment": "I've done everything is mentioned in the task description" } Dispute clarification: URL: https://pk8p4z13td.execute-api.eu-central-1.amazonaws.com/prod/clarify-dispute Method: POST Body: { "message": "how to know which bugs contractor needs to fix?", "threadId": "thread_f916c4931ba3474392d96dd5" } List messages: URL: https://pk8p4z13td.execute-api.eu-central-1.amazonaws.com/prod/messages/thread_f916c4931ba3474392d96dd5 Method: GET Use your thread_id in the url instead of mine. <div