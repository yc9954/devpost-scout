---
slug: "project-frhdw3zgtabu"
url: "https://devpost.com/software/project-frhdw3zgtabu"
title: "ChainSmith"
hackathon: "Theta Network 2023 Hackathon"
organization: "Theta Labs"
winner: true
words: 363
team_size: 0
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# ChainSmith

> A comprehensive management tool for the streamlined creation and deployment of subchains on the Theta Network.

[Devpost](https://devpost.com/software/project-frhdw3zgtabu) · hackathon [[Theta Network 2023 Hackathon]]

## Facets

**mechanism** [[benchmark_measured]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[structured_db]]

**stack** javascript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for …

## Body

Welcome to ChainSmith, a Product of FuelFoundry. Inspiration In response to the numerous requests from projects seeking our expertise in deploying a Theta Metachain subchain, we decided to enhance our approach. Our commitment was to develop an intuitive Metachain management system that eradicates repetitive tasks and simplifies the deployment process. What It Does Our project empowers users to create, manage, and maintain a subchain without requiring comprehensive knowledge of the underlying infrastructure. It functions as an independent ledger, where once a component is designed, it's mostly immutable to maintain data resilience and integrity. How We Built It We opted for a node-express-nunjucks-sqlite stack, primarily because the Metachain SDK is written in Javascript. This selection allowed us to leverage the existing SDK on the backend without having to rewrite it in a different language. For managing and executing commands on remote (virtual) machines, we used ssh2. Challenges We Ran Into Initially, we planned to use Ansible for node management due to its capability to install packages and deploy programs across multiple machines simultaneously. However, its lack of support for Windows led us to opt for node-ssh2, writing our custom bash commands to install and deploy nodes. While MariaDB is typically our preferred database, its need for configuration and Docker deployment led us to choose SQLite, enabling a local file to act as the database. Additionally, while we've automated remote node deployment for Windows 10 running Node 19.9.0 and Ubuntu 22.04.02 minimal installation, varying performance may occur on different Linux versions. Accomplishments That We're Proud Of - Integrating Theta.JS and Theta Metachain SDK - Implementing military-grade AES-256-GCM encryption - Devising an engaging project name - Constructing a user-friendly Theta Metachain Wizard What We Learned Throughout the project, we encountered issues that further enhanced our knowledge and understanding. We've had prior experience building a subchain on a testnet, and this project presented an opportunity to deepen that knowledge. What's Next for … Our roadmap includes deploying multiple nodes, a recovery mode, and mainnet integration upon the release of the requisite documents. We also look forward to receiving feedback from potential users to understand their needs better, enabling us to further improve and refine our product. <div