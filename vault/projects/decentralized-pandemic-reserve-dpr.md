---
slug: "decentralized-pandemic-reserve-dpr"
url: "https://devpost.com/software/decentralized-pandemic-reserve-dpr"
title: "Decentralized Pandemic Reserve (DPR)"
hackathon: "COVIDathon - Decentralized AI Hackathon"
organization: "SingularityNet"
winner: true
words: 603
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/realtime_stream"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/supply_logistics"
  - "user/developer"
---

# Decentralized Pandemic Reserve (DPR)

> DPR is an R-value backed DAO matching individual and manufacturer resources with the areas most in need. We're solving pandemics with data driven consensus and governance.

[Devpost](https://devpost.com/software/decentralized-pandemic-reserve-dpr) · hackathon [[COVIDathon - Decentralized AI Hackathon]]

## Facets

**mechanism** [[privacy_tech]] [[realtime_stream]]
**domain** [[civic_government]] [[health_clinical]] [[supply_logistics]]
**user** [[developer]]

**stack** aragon, dao, juypter, ocean, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for decentralized pandemic reserve (dpr)

## Body

DPR Logo Voting on Need using R-Value Inspiration As hospitals and essential businesses compete for necessary supplies, the identification of need is skewed by racial, political, and socio-economic biases. Policies are being driven by short-sighted and inaccurate data with little understanding of the virus’’s real-time effective reproductive number, leaving communities left scrambling for an effective plan of action. We are inspired by the DAO's ability to function without hierarchical management, removing biases and hopefully giving a voice back to people instead of skewed policy leaders during a time of global crisis. What it does The Decentralized Pandemic Reserve (DPR) aims to create an autonomous supply chain consortium that matches individual and manufacturer resources with the areas most in need. Our end-to-end solution solves issues with data storage, data retrieval, data validity, supply chain, and governance. By using a predictive model to identify the coronavirus’s real-time, effective reproduction number, training that model with A DAO supported by decentralized voters and assessing proposals of hospitals or entities in need of resources against data models of activity (healthcare.gov/covid or healthdata.org/covid) to deliver supply. How we built it PySyft is a Python library for secure and private Deep Learning. PySyft decouples private data from model training, using Federated Learning , Differential Privacy , and Encrypted Computation (like Multi-Party Computation (MPC) and Homomorphic Encryption (HE)) within the main Deep Learning frameworks like PyTorch and TensorFlow. We deployed the jupyter notebook, and used PySyft , OpenMined and PyGrid to implement Differential Privacy and Federated Learning on the model. For the DAO component, we utilized Aragon and it's smart contracts for ease of deployment, token functions, and voting mechanism. A React front end ties together the data component, a DAO component, and R values and other data from jupyter notebook and the OCEAN protocol. Challenges we ran into Initially, we were too consumed with figuring out the supply chain component, but quickly realized we could leverage cohorts such as https://make4covid.co/ and others across the globe to handle supplies and manufacturing production to meet demand. Since they are a growing coalition of designers, engineers and manufacturers, we could shift our project to focusing on distribution and areas of greatest need. Accomplishments that we're proud of We were able to stream line the data being used to understand COVID from the daily amount of reported cases to the coronavirus’s real-time, effective reproduction number, or its actual ability to spread at a particular time. By using this data we are able to continuously train the model with a DAO putting the power of choice back into the hands of the people. A modified voting mechanism with informed data points informs the community about relevant information such as supply recipient, location, (R) infection rate, and reputation. What we learned We learned that people are afraid and feel powerless as decisions are being made that they have little say or control over. We also learned that our project is modular and can be replicated to solve for more than just this use case. We have a centrally build a decentralized and global data science department. What's next for Decentralized Pandemic Reserve (DPR) We hope to gain feedback and insight from the Devpost community and continue building our project as we believe it will have long-term scalable impact. We believe DPR has the potential to decentralize voting, force decision making and price transparency and build the data economy of the future. It can be used for a variety of supply chains, but more importantly, it will eventually with enough training, reduces the amount of human bias and mode from the decision chain. [presentation] https://docs.google.com/presentation/d/1JOKOpt5lD0M9_JQbWPOhPo9YH1qLv3inADb9C5DItlQ/edit?usp=sharing ) <div