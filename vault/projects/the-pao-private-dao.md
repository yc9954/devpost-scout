---
slug: "the-pao-private-dao"
url: "https://devpost.com/software/the-pao-private-dao"
title: "The PAO (Private DAO)"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 700
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/structural_withholding"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/financial_record"
---

# The PAO (Private DAO)

> Private fundraising protocol for Web3 startups (DAOs)

[Devpost](https://devpost.com/software/the-pao-private-dao) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**mechanism** [[privacy_tech]] [[structural_withholding]]
**domain** [[civic_government]] [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[financial_record]]

**stack** chainlink-automation, circom, express.js, hardhat, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the pao (private dao)

## Body

Inspiration Our team members share their backgrounds as blockchain developers and cryptography engineers. We have always stood for the decentralization mission of Web3 communities and we believe the development of DAO models is an essential process. That's why we came up with a protocol with many ideas to build a new framework of DAOs for this hackathon - the Private DAO. What it does The protocol addresses the privacy issue for investors, encompassing both the privacy of the amount of money they have invested and the privacy of voting on project operations through proposals. Our approach offers the advantage of facilitating the operation of a DAO (Decentralized Autonomous Organization) for investors who have made financial contributions in a convenient manner (with just one transaction), while ensuring privacy for all investment decisions. The concept originates from a practical need: I want to invest in Company A, but I don't want anyone to know how many shares I have or how I vote on the company's operations. How we built it There are two main stages: Research & Proposal In the first stage, we research existing work, both PoCs and running applications, on private DAOs. From what we learned, we propose a design for our Private DAO model, which is based on three core techniques: Distributed Key Generation for Threshold encryption Homomorphic Elgamal encryption Zero-knowledge Proof Implementation & Evaluation And in the second stage, we managed to successfully build a PoC for our proposed design, including: Smart contracts system for mentioned techniques ZKP circuits in circom Web application for users to interact with the protocol Web server to support the web app and listening to events. Fully automated workflows with the help of Chainlink Automation Challenges we ran into First of all, this project generates a huge workload for our members in a month. The research & proposal stage took us a while to finalize a decent proposal that we believe could really solve the privacy problem for investments in DAOs. Then at the second stage, due to a rich set of requirements, there is so much work to do to implement all the features we want in smart contracts and ZKP circuits. Also, much of our time was dedicated to testing and optimizing the smart contract systems. That's why we could not focus too much on the web application and some features in our protocol haven't been enabled and integrated into the web app. We will continue after the hackathon event to deliver a decent web app for the protocol. Accomplishments that we're proud of We are proud of the result of our hard work - a framework for anyone to create a DAO and raise funds from investors, which ensures: Functionality - Investors can fund, then make decisions (through voting) for what a DAO can do with the fund raised. Privacy - Investors fully preserve their privacy in the funding and voting processes. Autonomous - All actions that do not require a specific role in the system are automated with Chainlink Automation (Chainlink Keepers). We are confident that there are no running protocols manage to meet all the requirements specified in our protocol at a reasonable cost for users. What we learned Throughout a month with lots of work to do, we have learned a lot of lessons in developing DAOs and ZKP on EVM: which are the standard behaviors and why people implement DAOs that way, how to optimize gas cost, etc. and we also discovered interesting applications and services provided by Chainlink. We found the Chainlink Automation is extremely useful for the autonomous protocol on Web3, especially DAO. We will take a closer look at other services from Chainlink for potential ideas to improve our protocol. What's next for The PAO (Private DAO) While it was a tight-scheduled month, we still have much work and many ideas for the PAO (Private DAO) protocol. We aim to make this a platform where startups can raise funds as DAOs but with strategies similar to traditional startups. It means that our smart contract system should cover common investment strategies, i.e. convertible loans, future equity shares, etc. Also, there are a lot of technical ideas to improve the protocol as well. <div