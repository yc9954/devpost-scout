---
slug: "cryptodo-ai"
url: "https://devpost.com/software/cryptodo-ai"
title: "CryptoDo AI"
hackathon: "Fantom Hackathon Q2 2023"
organization: "Fantom Foundation"
winner: true
words: 401
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# CryptoDo AI

> AI-based no-code dapp builder

[Devpost](https://devpost.com/software/cryptodo-ai) · hackathon [[Fantom Hackathon Q2 2023]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** amazon-web-services, gpt-4, node.js, react, solidity

## How they structured the write-up

- inspiration
- how it works

## Body

CryptoDo-AI interface CryptoDo-AI is a next-generation smart contract builder powered by GPT-4 API Inspiration CryptoDo AI The project's aim is to provide the best service for non-technical users to generate custom decentralized applications (dApps). GPT-4 is currently the most advanced language model, and it excels at writing Solidity smart contracts. However, generating quality results requires crafting a well-structured, technically sound prompt for the AI. Furthermore, the code output from GPT-4 requires validation, compilation, deployment, and verification in a blockchain explorer before it can become a functional product. This process presents significant challenges to users lacking programming expertise. CryptoDo-AI solution is to create a service where non-technical users can construct and deploy any smart contract via a user-friendly drag-and-drop interface, without interacting directly with code or needing to write a prompt. How it works The user chooses a basic contract type from dozens of options offered by our service. The user selects additional features for their dApp and drags them into their project. If necessary, the user can add their functions through a separate text prompt. Based on the user's choices and pre-created templates, our service generates a technically sound prompt for GPT-4. We interact with the AI via the API and receive a response in the form of a code file. We make a second request to the AI for double-checking, auditing, and refactoring the received code. On the backend, we attempt to compile the Solidity code and report any compilation errors to the GPT-4 model. The ready and compilable contract is deployed by our service to the testnet, with the user's approval. The user receives a link to the verified smart contract on the testnet and instructions for testing. If testing is successful, the user can deploy the smart contract to the main blockchain network through our service in one click. We understand that this method is not perfect and comes with inherent risks. However, we implement several stages of technical checks and manual tests before deploying the contract to the mainnet, drastically reducing potential issues. Despite this, we alert users to the need for external verification and the potential risks of the created solution. While it's not yet an ideal product, we believe that the rapid advancements in AI technology will soon begin to replace developers in the market. Our goal is to provide people with a flawless and convenient tool for interacting with this amazing technology https://ai.cryptodo.app/ <div