---
slug: "knn3-data-job-management-panel"
url: "https://devpost.com/software/knn3-data-job-management-panel"
title: "KNN3 Data Job Management Panel"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 572
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/supply_logistics"
  - "user/developer"
  - "substrate/financial_record"
---

# KNN3 Data Job Management Panel

> Allows developers to execute a job that can process off-chain data and deliver results to smart contract with scheduling through smart contract. The configuration is done in a user-friendly interface.

[Devpost](https://devpost.com/software/knn3-data-job-management-panel) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**domain** [[developer_tools]] [[supply_logistics]]
**user** [[developer]]
**substrate** [[financial_record]]
  <sub>weak: web_dom</sub>

**stack** chainlink-automation, chianlink-any-api, css, html, javascript, pagerank, postgresql, scss, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for knn3 data job management panel

## Body

Problem to solve What the panel offer Panel design Future plan Demo process Inspiration Currently, it is difficult for developers to process on-chain and off-chain data directly through smart contracts. First, smart contracts have limited data processing capabilities. Second, delivery data to smart contracts via oracle requires enhancements on data service flexibility. Third, the processing jobs need to be managed without heavy coding and accessible user interfaces in a decentralized approach. What it does KNN3 proposes a service that allows developers to execute a job that can process off-chain data and deliver results to smart contract with scheduling through smart contract. The configuration can be done easily in a user-friendly interface. 1. Integrated : One stop for on-chain and off-chain data fetching, processing, and delivery with Chainlink tool set API service deployed on Chainlink Node Job scheduling and triggered via Chainlink Automation Result delivered to smart contract directly with ChainlinkClient 2. Computation capability : range from raw data fetching, to data aggregation, to pre-processed models 3. Light-coded : User friendly interface, customized script constructed as individual job at the back-end for easy deployment How we built it 1. An integrated panel Data Preparation With a job instance created, users can select the data sources that they are interested in which are available in KNN3 data warehouse. Data Processing Users can decide how they want the data to be processed, including raw data, customized aggregation through SQL, ready to use algorithms, and customized algorithms. Data Delivery Through the interface, users can configure the frequency of data delivery and where they want the data to be stored. They are provided with the options of decentralized file storage (IPFS, Arweave), cloud storage (S3, TiDB), and smart contracts. 2. Smart Contract scheduling with Chainlink Automation If users want the job to be executed with customized schedules, they can configure the parameters easily from the panel interface by some dropdown lists. The job panel will register their job schedules in Chainlink automation with a simple button click. 3. Smart Contract Data delivery and storage with Chainlink Any API With job service registered in Chainlink Node, it will listen to the data delivery smart contract based on ChainlinkClient. When the data delivery smart contract is triggered by Chainlink Automation, the job in Chainlink Node will be executed and send result to data delivery smart contract through Chainlink Oracle. Challenges we ran into Balance between simplified user experience of UI and complicated on-chain and off-chain communication process How to minimize user coding through the entire process Accomplishments that we're proud of Job scheduling with Chainlink Automation through API without going to multiple user interface Hybrid smart contract concept realized by integrating Chainlink Node, Oracle, Client, and Automation What we learned A clear understanding of how Chainlink tool sets work and how they can help enhance on-chain and off-chain data processing and delivery More flexible and configurable job management process is in demand What's next for KNN3 Data Job Management Panel Integrated minimize cross platform work smart contract deployment within the panel Computation capability allow customized aggregation through SQL customized ML model deployment on-demand triggering for Transactional Processing jobs periodical job registration & keeping for Analytical Processing jobs Role-controlled account management access key generated based on role with specific capability dashboard to track key usage and resource usage Scalable optimal performance with resource management strategy instances allocated to each account with demanded resource open for quota increase per request <div