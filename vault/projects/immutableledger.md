---
slug: "immutableledger"
url: "https://devpost.com/software/immutableledger"
title: "immunomic"
hackathon: "Chainlink Fall 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 425
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/code_repository"
  - "substrate/financial_record"
  - "substrate/regulation_legal_text"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# immunomic

> A real-time immutable ledger on the blockchain

[Devpost](https://devpost.com/software/immutableledger) · hackathon [[Chainlink Fall 2022 Hackathon]]

## Facets

**mechanism** [[provenance_signing]] [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[code_repository]] [[financial_record]] [[regulation_legal_text]] [[sensor_telemetry]] [[web_dom]]

**stack** chainlink, ethers, javascript, lambda, node.js, paypal, polygon, quicknode, react, solidity, tailwindcss

## How they structured the write-up

- inspiration
- what it does
- how we build it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for immunomic

## Body

immunomic_title immunomic_stack immunomic_architecture immunomic Inspiration Financial statement manipulation is a type of accounting fraud that remains an ongoing problem. The manipulation of financial statements to commit fraud against investors or skirt regulation is a real and ongoing problem, costing billions of dollars annually. Managers/Organisations may "cook the books" in order to qualify for certain advantages that rely on certain financial performance metrics being met or Crowdfunding platforms raise funds for campaigns and may underreport them to users by diverting the funds. Often people who contribute/donate to campaigns run on crowdfunding platforms are unaware of how the funds are being used: who are the exact people who have access to the funds, and where they are spending the money? What it does immunomic is a DAO we created to solve the issue of lack of transparency and trust in crowdfunding platforms. Our solution connects the bank accounts of the campaigns being run to a chainlink node, which writes all the bank transactions on an immutable ledger (blockchain), that in turn emits the transaction so that web2 app detects and records the transaction to display it to users on Dashboard. Github Repos : Backend Frontend How we build it Frontend: We used React JS , Tailwind CSS for UI and ethers library to fetch details from contract. External Adapter: We used Nodejs server and Paypal-sdk for fetching payment details from paypal. Blockchain : Smart Contract: We used Solidity for writing smart contracts. Development: Remix to write, compile in local system. Deployment: Hardhat to deploy to testnet and verify the contract. Chain: Polygon Mumbai to deploy smart contracts on testnet. RPC URL : We used Quick Node polygon RPC url to connect to the mumbai chain. Chainlink: Oracle: We used Operator.sol for Oracle requests. Bridge: We used Bridge for connecting external adapter to the chainlink job. Job: Used to get data from external adapter and pass it to oracle. Others: We used Paypal for transactions, AWS Lambda function as a webhook url for paypal. Challenges we ran into There has been a lot of challenges encountered in solidity, and finding a solution has been challenging. Accomplishments that we're proud of Despite having no prior knowledge of the chain link ecosystem, we have built a Dapp using it. What we learned While working on this project, we have learned how to send off chain data to on chain in a more secure and decentralized manner. What's next for immunomic The Immunomic system is currently built using PayPal. More banks and financial institutions should be added in the future. <div