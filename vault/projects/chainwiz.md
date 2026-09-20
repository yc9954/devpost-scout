---
slug: "chainwiz"
url: "https://devpost.com/software/chainwiz"
title: "Oriviz"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 468
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/general_public"
  - "substrate/financial_record"
---

# Oriviz

> End-to-end debugger for your Chainlink pipeline.

[Devpost](https://devpost.com/software/chainwiz) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[general_public]]
**substrate** [[financial_record]]

**stack** gcp, nextjs, node.js, react, solidity, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for oriviz

## Body

Get a summary of the Chainlink stack Test the E2E connection with one click Update variables across the entire pipeline Inspiration For blockchain applications to be mainstream and address powerful real-world use-cases, contract developers will need the ability to access multiple sources of off-chain data. Understanding how Chainlink oracles work and adapting them for individual purposes requires a developer to be familiar with three different pieces of the stack - the Chainlink node infrastructure, the Oracle contract and the consumer contract. This can be intimidating and time-consuming, with a developer trying to manage multiple contract address, jobIds, funding different addresses etc across multiple tabs and multiple platforms. This makes debugging and visualization of the entire pipelines difficult, thereby slowing down time-to-market and increasing effort. What it does Oriviz provides a way for a developer to visualize, test and debug Chainlink transactions in a single view. Developers can change parameters across any of the three pieces of the stack - the node, oracle contract and/or the consumer contract - and have the corresponding variables change accordingly. Oriviz also allows the user to test the entire flow with a single button click and see the hierarchy of events and transaction calls as they are made. How we built it The first goal was problem validation. By traversing through some of the discord channels (like external adapters), I found that a few problems were recurrently faced by developers: getting the contract addresses mixed up trouble getting hold of test tokens / testnet eth, unfunded nodes trouble debugging the connection between the contract and the node and inability to verify if the node was listening to events correctly I built this prototype using NextJS, web3.js and React. Mostly a UI-focused application, understanding the way the events were fired, the control flow and the fulfilment of the requests was pivotal. I also used react-mui and tailwind for fast prototyping. Note: Most functionality is currently based on the testnet standard contracts and hardcoded to capture the essence of the complete app. Challenges we ran into Understanding the Chainlink stack and transaction cycle Getting the local infrastructure setup. The initial idea was to have this as an interface for a completely local end-to-end setup. However, I had trouble getting the chainlink node to work with a development node like Hardhat. Accomplishments that we're proud of Problem Validation and talking to users The data structure to capture all the related components information together Visualization of the events being fired sequentially What we learned This project gave me better, more in-depth understanding of how the Chainlink ecosystem works. What's next for Oriviz Two main features planned next for Oriviz Allow for in-place custom deployments for consumer contract, chainlink nodes (with jobs and adapters) and oracle contracts. Allow for interaction with a fully local setup with Hardhat <div