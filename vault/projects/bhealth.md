---
slug: "bhealth"
url: "https://devpost.com/software/bhealth"
title: "BHealth"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 325
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "domain/security_privacy"
  - "user/patient_family"
  - "substrate/financial_record"
  - "substrate/structured_db"
---

# BHealth

> Secure and private health data.

[Devpost](https://devpost.com/software/bhealth) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[health_clinical]] [[security_privacy]]
**user** [[patient_family]]
**substrate** [[financial_record]] [[structured_db]]

**stack** chainlink, javascript, node.js, postgresql, python, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bhealth

## Body

Inspiration According to HippaJournal, Between 2009 and 2020, 3,705 healthcare data breaches of 500 or more records have been reported to the HHS’ Office for Civil Rights. Those breaches have resulted in the loss, theft, exposure, or impermissible disclosure of 268,189,693 healthcare records. That equates to more than 81.72% of the population of the United States. In 2018, healthcare data breaches of 500 or more records were being reported at a rate of around 1 per day. In December 2020, that rate had doubled. The average number of breaches per day for 2020 was 1.76. Blockchain technology can transform healthcare by increasing the security, privacy of health data while eliminating bureaucracy, data breaches, inefficiencies, improving quality of care and democratizing patient data. In addition, patients receive cryptographic identities in the form of public and private key pairs. Public keys are stored in the blockchain and are suitable for securing and verifying transactions. Furthermore, smart contracts, Filecoin's OrbitDB and Chainlink's extrnal-adapter ensuring the preservation of privacy and confidentiality. What it does Give patients full control of their data. How we built it Our project brings healthcare data from standard databases - such as PostgreSQL - to the on-chain space, by leveraging the use of Chainlink API features. Initially, this data will be stored on IPFS and FileCoin's OrbidDB. This way, we can guarantee the security and privacy of the data, giving more control to the patient, as he can see at any time who has access to it. Challenges we ran into Most of the development time was spent figuring out how OrbitDB because it's a new technology, Accomplishments that we're proud of Created an API from OrbitDB that can send data to a chainlink node. What we learned There are infinite possibilities to what can be achieved with blockchain technology What's next for BHealth More privacy by introducing Zero Knowledege proof, lot of improvements and features need to be done on the smart contract. <div