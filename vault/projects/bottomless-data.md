---
slug: "bottomless-data"
url: "https://devpost.com/software/bottomless-data"
title: "Aster"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 656
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# Aster

> A Decentralized Collective Micro-task App for Data

[Devpost](https://devpost.com/software/bottomless-data) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[finance_payments]] [[labor_employment]]
**user** [[educator_student]]
**substrate** [[financial_record]] [[web_dom]]

**stack** chainlink, firebase, node.js, polygon, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what's next for aster
- accomplishments that we're proud of

## Body

Our Team User Story Aster Infrastructure Client Dashboard Labeler Interface Inspiration We’re a group of college students fascinated by the idea of using technology for positive change. With blockchain, we’re able to build applications that are not only useful and sustainable, but also transparent and inclusive. Traditional data labeling applications are opaque and exclusive. There is no transparency in the workflow process to verify the demographics of the workers and fair payments to the workers. Usually, the third-party companies would take a large portion of the profits and leave only a small portion to the workers. By incorporating the blockchain technologies, Aster is able to eliminate the monopolizing third-party companies to provide fair payments to the workers, allow anyone from anywhere in the world to classify data at ease on their mobile phone, and provide clients the opportunities to collect transparent and multi-perspective labels. What it does Aster is a decentralized and collective micro-task application for data. Aster enabled transparent data labeling and instant crypto rewards. Aster allows clients to upload data and task description onto our secured backend and create a smart contract on Polygon Blockchain for each labeling task to incentivize users from all over the world to help classify data. Polygon network support low transaction fees to make these task creations and submissions affordable. The clients can view the real-time progress of their tasks on the Aster home dashboard website. We implemented Chainlink's Price Feed oracle to get the latest price of MATIC to provide better understanding and visualization of the rewards' worth to users. The task information and the rewards per task will be displayed on the Aster task page. The labelers can log onto Aster’s website to select any task they wish to work on. Once a task is completed, labelers receive instant crypto rewards as indicated on the task page. How we built it This project contains both web2.0 and web3.0 technologies. We use Firebase as Aster’s backend to securely store data for clients via NodeJS APIs. We implemented a factory design to allow clients create a new task contract for every data task they want to publish. All payment transactions are through the task smart contracts and are instant. The Aster server is a React website application that handles client’s task creations on the Polygon blockchain and labelers’ task selection and submission and instant crypto rewards which also interacts with MetaMask wallets. What's next for Aster Currently, we support only MATIC as the crypto payments. We would like to implement the functionalities to support more cryptocurrencies as payments by utilizing more Chainlink tools and support more data micro-tasks such as segmentation tasks and description tasks. Potentially, we could allow users to choose the form of crypto rewards they want to receive by implementing an in-app swap functionality. Moreover, we would also like to provide data analytics to our clients to help them better understand their data distribution and information. In order to make this project more decentralized and adapt fully to Web3.0, we are planning to implement Moralis technologies to replace the current Firebase backend and to utilize Filecoin protocol for decentralized data storage. To turn this project into a fully decentralized working solution, we would build a complete and healthy ecosystem for this project community. We need to include a reviewers community in the ecosystem to prevent frauds and ensure the quality of the micro-tasks. This can be done by implementing a decentralized reviewing mechanism on chain to incentivize users to fully support the mission of this project. Accomplishments that we're proud of We are an international team with each member living in a different time zone. We are beginners to blockchain technologies, so we are proud to be able to build a furnished blockchain MVP with a backend, frontend for users, and the smart contracts that interacts with Chainlink tools on Polygon in such a short amount of time on top of our school and work. <div