---
slug: "growr"
url: "https://devpost.com/software/growr"
title: "Growr"
hackathon: "Hack to the Future 4"
organization: "Finastra"
winner: true
words: 802
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/general_public"
  - "user/small_business"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Growr

> Fair loans through self-sovereign profile and decentralized risk management

[Devpost](https://devpost.com/software/growr) · hackathon [[Hack to the Future 4]]

## Facets

**domain** [[finance_payments]] [[retail_commerce]]
**user** [[general_public]] [[small_business]]
**substrate** [[code_repository]] [[video_visual]]

**stack** blockchain, finastra, fusionfabric.cloud, graphql, hardhat, mongodb, next.js, node.js, react.js, rif-data-vault, rif-identity, rsk, solidity, ssi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for growr

## Body

Growr SSFI App (Demo): How it works Growr Protocol App (Demo): How it works Inspiration Financial health is an important factor in our daily life. However, bad financial health is plaguing the world. More than half of the global population is living paycheck-to-paycheck without any savings (link) . In addition, almost 2 billion adults in the world do not have access to financial services (link) or if they do, they fall prey to financial sharks and receive loans at a very high interest rate. Moreover, there are still 72 countries where women from specific social groups do not have the right to open a bank account or obtain credit (link) . At the same time, even people who have savings in cash or in a bank account are also impacted. On the one hand, macroeconomic events, such as high inflation, are literally “eating their money” and on the other hand, they are not able to acknowledge the disruptive change that is happening to the financial system. Today, most financial service providers do not solve those problems. They are clueless about people's real-life problems, needs and aspirations. There's a complete disconnect between the person and the provider. Banks, and even more so non-banking lenders, have a negative image especially with younger generation, who, as a result, are more likely to go to the dentist than visit a bank. What it does We propose the Growr protocol as a bridge to a new global financial environment. The Growr protocol advances financial inclusion by enabling borrowers to receive fair & instant unsecured loans based on a self-sovereign identity. Growr protocol addresses the problems stated above with the following elements: Growr core protocol – a decentralized smart contract ecosystem for funding and consuming loans on top of the RSK blockchain, with open access for everyone. Self-sovereign financial identity (SSFI) – a digital identity, based on W3C's DID and VC standards, owned and managed by the user. Protocol access via web and mobile applications - a simple and secure way for consumers and merchants to easily apply and obtain fair loans. Credit risk assessment – a framework for establishing trust using a combination of alternative approaches such as on-chain activity, trusted off-chain sources, peer vouching, and others. Growr DAO - a future decentralized autonomous organization for protocol governance and fair compensation of protocol contributors. How we built it We conceptualized the idea and developed a first PoC in early December 2021. Since then, we continued with detailed solution design and we initiated a development of second PoC. Hack-to-the-future hackathon gave us motivation to accelerate our effort and during the submission period we managed to develop: Core Protocol . Solidity smart contracts system for decentralized lending, running on RSK-Testnet. Includes: PondFactory : 0x3d56294133C83C1c887Cb6C0CC35AdF81593a0f1 VerificationRegistry : 0x29Fa7b0eBA146176d39531f564751DE3E9583080 xUSD token: 0xAb32F4D4b0A57C0B0F1e1600B8B89896d3a886eC DOC token: 0x250aBdF81b3BAcbe896a23C61B0C89C796A77d91 WRBTC token: 0x3844d4FCa7371E20A779E64857220baE05130b00 SSFI . A unique global decentralized identity, based on DID and VC WEB3 standards, that is intended to store various protocol-specific verifiable credentials. The SSFI leverages RIF Identity framework. User's data is stored user-centric cloud storage and can be restored on different devices, using Web3 wallet. Demo Protocol App . A demo web app for creation of ponds with different eligibility criteria and funding those ponds. Demo SSFI App . A demo web app for providing the borrowers with easy access to the protocol mechanics. It covers onboarding of borrowers, loan application, loan release and repayment. Credential issuing service . A backend service that provide end-users with verifiable credentials based on data retrieved from external data sources. Credential verification service . A backed service that verifies presented credentials. Integration with Consumer bank API for extraction of risk assessment for the verifiable credentials Integration with Credential storage service (data vault) for storing user data. Challenges we ran into Designing and development of decentralized lending protocol is a complex task with many challenges. Some of our biggest challenges were: Designing and implementing smart contracts on RSK chain Putting all services and applications to work together Accomplishments that we're proud of Converting our vision into detailed protocol specification Launching a protocol on RSK TestNet Proving some key concepts (eg. decentralized identity, verifiable credentials) with demo application and services What we learned How to design, develop and deploy smart contracts on RSK How to use RIF Identity to issue, store and verify credentials How to use RIF Data Vault to store and restore data How to host and present documentation repository using Github Pages What's next for Growr Extend the PoC with protocol dashboard, lightning payments integration, financial health gamification, additional VC schemas and data sources Test the develop protocol components with real users Develop further protocol components and features following the protocol specification Local MVP launch in El Salvador Regional expansion with investors and partners (crypto funds, microlenders, telecoms, merchants/retailers in LatAm and potentially SEE) <div