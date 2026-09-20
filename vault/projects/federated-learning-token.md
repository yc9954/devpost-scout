---
slug: "federated-learning-token"
url: "https://devpost.com/software/federated-learning-token"
title: "Federated Learning Token"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 278
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "domain/civic_government"
---

# Federated Learning Token

> Smart contract ecosystem that provides secure, decentralized, anonymous federated learning. It allows training machine learning models on data without their exposure to the internet.

[Devpost](https://devpost.com/software/federated-learning-token) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[privacy_tech]]
**domain** [[civic_government]]

**stack** brownie, chainlink, ipfs, python, solidity

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for federated learning token

## Body

Inspiration I have been interested in machine learning for many years. This year I just started studying PhD at NUS working on a project related to federated learning. I saw a bunch of papers talking about federated learning on a blockchain, but I didn't see any running project. The other thing is that the entities are often worried about: Trusting central server that it will steal their data or not share the results with them Difficulties of setting up and hosting the infrastructure How to make a fair deal with other companies so non of them will screw the others My project is trying to solve all these issues. What it does This project provides contracts for managing federated learning. The main contract is called Project. Right now you can build and deploy the contracts. Then connect the nodes (using some demo data for now). After that, you can create a training plan (define model using scikit-learn) and let the nodes execute it. Challenges we ran into Voting for the malicious parties is a tricky issue and the rewards and penalties must be well set in order to make it work properly. We are still balancing this part. Accomplishments that we're proud of It actually runs! What we learned IPFS and Filecoin might sound complicated at first, but it is really awesome technology! What's next for Federated Learning Token A lot! We want to start by running federated learning competitions, where people could compete in creating the best machine learning models in federated learning scenario and receive prizes for participation. Creating a marketplace where projects could sell their pre-trained models. Improving security using Chainlink keepers. And more <div