---
slug: "curisapphire"
url: "https://devpost.com/software/curisapphire"
title: "CuriSapphire"
hackathon: "Privacy4Web3 Hackathon"
organization: "Oasis Foundation"
winner: true
words: 339
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/health_clinical"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/financial_record"
---

# CuriSapphire

> Your Health, Your Data, Your Control 🛂

[Devpost](https://devpost.com/software/curisapphire) · hackathon [[Privacy4Web3 Hackathon]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[health_clinical]]
**user** [[patient_family]] [[researcher]]
**substrate** [[financial_record]]

**stack** ethers, react.js, sapphire, solidity, viem, wagmi, zk-snarks

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for curisapphire

## Body

Inspiration The inspiration also comes from the potential of technologies like Sapphire and Zero-Knowledge Proofs (ZKPs). These technologies offer a transformative path toward preserving privacy while enabling the fruitful use of data. Also, the need to revolutionize the way we handle health data and empower individuals with control over their own information fueled this idea. What it does CuriSapphire empowers user privacy by leveraging the Sapphire paratime and Zero Knowledge Proofs. Giving your healthcare provider the access to your medical history might seem like giving away too much private information, so Curi-Sapphire utilizes Zero Knowledge Proofs (ZKPs) to prove medical statements to healthcare provider so that they can take informed decisions and patient privacy is not compromised. Similarly, giving out details such as date of prescription issue, etc. to pharmacies is prevented by using Zero Knowledge Proofs (ZKPs) to prove to the pharmacy that a prescription is still valid. Not all medicines require a prescription, so we have used an AI model to decode medicine purchaser's intent and extract medicine information from it and keep an order ready. Tokenized data opens use-cases where data providers can benefit financially through their data. People like medical researchers are constantly looking for medical data for their research purpose and data analysis. They can get access to anonymized data by providing financial incentives to data providers. This helps CuriSapphire assist in creating a responsible data economy. How we built it We have used a gasless proxy contract (Proxy.sol), which implements an on-chain signer, for smooth and gasless user onboarding on our platform. zk-SNARK Proofs are implemented using snarkjs and circom libraries. Data tokenization is implemented by the Tokenization.sol smart contract Wallet and contract integration is done through wagmi, viem and ethers.js Challenges we ran into Deployment: It was not possible in time because of ZKP files Accomplishments that we're proud of Using the power of ZKPs with Sapphire What we learned A great deal about patient privacy and data economy What's next for CuriSapphire Adding more ZKP use-cases and enhancing privacy further. <div