---
slug: "umpire"
url: "https://devpost.com/software/umpire"
title: "Umpire"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 443
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Umpire

> Umpire is a low-code backend solution for building hybrid dApps

[Devpost](https://devpost.com/software/umpire) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]] [[sensor_telemetry]]

**stack** chainlink, hardhat, nextjs, polygon, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for umpire

## Body

Inspiration In recent years, many low-code or even no-code services have emerged for web2 applications. We think we're still not at a stage where no-code is viable for web3, but it's time to start making the space more approachable! What it does Umpire allows developers and power-users to quickly deploy "Umpire jobs", which are essentially micro-backends for hybrid web3 dApps. A job consists of: inputs - any number of variables provided by Chainlink data feeds, as well as constants like Pi or Euler number, and variables like "current timestamp" trigger - a formula using input variables and an arithmetic formula positive action - a custom smart contract function that is called as soon as the formula defined in the trigger is evaluated as true negative action - called if the trigger does not fire before a predefined deadline, think of it as a timeout. This simple concept combined with Chainlink Automation and hyper-reliable data feeds powered by Chainlink DONs can power all kinds of applications, such as: custom DeFi strategies, including stop-orders etc. prediction markets betting basic parametric insurance How we built it The system consists of two major components: the resolver (currently in V2) responsible for evaluating user-defined formulas; the registry, which manages all the jobs, serves as a hub for Chainlink Automation calls, fetches data from the feeds, etc. The system is currently deployed to Polygon Mumbai testnet. We have decided to build on Polygon due to quick and reliable transactions and low fees, which makes it a blockchain of choice for many developers - and our tool is mostly aimed at developers. Challenges we ran into Formula evaluation on-chain can be costly, but with Chainlink Automation optimizations it should not be a problem. The biggest challenge was, as always, time scarcity, we wish we had more time to implement more features we envisioned. Accomplishments that we're proud of We believe it's a really cool idea and hopefully, once it matures, it will help a lot of developers and users build toward a truth-based society! What we learned As always, this has been a learning experience. We learned a ton about the intricacies of blockchain development, as well as Chainlink Services, especially how to properly utilize Chainlink Automation. We can't wait to see what we'll be able to build once we enter a cross-chain era with CCIP! What's next for Umpire We have a lot of ideas in our backlog, the most important one would be to improve UX when building formulas. The next goal would be to actually get it production-ready! If you have any constructive criticism, or feedback, or want to contribute, please let us know! https://github.com/web3bits/umpire https://umpire.vercel.app/ <div