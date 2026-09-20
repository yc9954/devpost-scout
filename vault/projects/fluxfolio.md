---
slug: "fluxfolio"
url: "https://devpost.com/software/fluxfolio"
title: "Fluxfolio"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 308
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "substrate/structured_db"
---

# Fluxfolio

> Trustless portfolio management solution leveraging MPC-based proxy contracts for secure gating of NEAR intent signing permissions.

[Devpost](https://devpost.com/software/fluxfolio) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**domain** [[labor_employment]]
**substrate** [[structured_db]]

**stack** cloudflare, nextjs, prisma, rust, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for fluxfolio

## Body

Before Balance After Balance Inspiration As both NEAR Intents and AI agents get more traction, we thought it would be a good idea to build a trustless agent assigning protocol where funds cannot be stolen. Generally with portfolio managers, you give the agent authority over your funds and they can turn around and rug you quite easily. With Fluxfolio, this is not the case. What It Does Our solution allows a NEAR intents deposit address to be derived via an MPC key that is controlled by a proxy contract. By using this model, we can re-construct NEAR intent messages on the contract layer so we can scan for any malicious intents from the agents. We also wrapped everything in a NextJS app that talks to a DB and allows users to sign up using a simple passkey model. How We Built It We developed Fluxfolio using Rust for the smart contracts, a NextJS app for the frontend, prisma for the database, and finally cloudflare workers to perform the CRON jobs. The smart contract is a proxy to the MPC network and accepts NEAR intent messages to then be signed if the permissions allow. What's Next for Fluxfolio Looking ahead, we want to turn the smart contract into a general purpose AI agent security protocol that is much more customizable. The contracts could become the backbone for major AI agent portfolio interactions due to the removal of trust in the equation. We can make the contract general purpose and allow a much more fine-grained control where users can set things like: time-locks maximum swap amounts certain token conditions limit orders Once the contract is built to be more general purpose, we can move to expand the frontend and allow for a smarter portfolio manager that can manage complex positions, follow social trends, interact via twitter and telegram etc.. <div