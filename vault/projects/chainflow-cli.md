---
slug: "chainflow-cli"
url: "https://devpost.com/software/chainflow-cli"
title: "ChainFlow CLI"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 216
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/financial_record"
---

# ChainFlow CLI

> ChainFlow CLI is an adapter that allows Chainlink Automation to communitace with the Flow Bloackain.

[Devpost](https://devpost.com/software/chainflow-cli) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** cadence, chainlink, flow, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chainflow cli

## Body

Inspiration I was inspired to create an adapter that would make it possible to make use of Chainlink Automation on the Flow Blockchain since it is yet to be supported. What it does ChainFlow CLI creates a project scaffold that can then be edited and configured around the based adaptor functionality to allow your Cadence Smart Contracts to be automated with Chainlink Automation. How we built it The project was built mainly in Node js, Solidity and Cadence. The CLI creates a project with compatible contracts which would then be edited. Once the contracts are deployed the developer can create automations on Mumbai, and connect the events raised to a Flow transaction adapter. Challenges we ran into It was mostly challenging to implement the authorization because FCL only allows for in browser authentication, so transactions had to be built on the commandline, which caused high memory usage due to multple upkeeps which spawned multiple terminal instances. Accomplishments that we're proud of I was able to put together a proof of concept which I will continue to work on post hackathon. What we learned It was my first time working with the FLow Blockchain and I really enjoyed Cadence, it reminds me of a typed version of Python. What's next for ChainFlow CLI Build, build, build! <div