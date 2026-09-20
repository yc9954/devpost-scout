---
slug: "bunny-notes"
url: "https://devpost.com/software/bunny-notes"
title: "Bunny Notes -A Gift Card and Cash Note Protocol"
hackathon: "TRON Grand Hackathon - Season 3"
organization: "TRON DAO"
winner: true
words: 724
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/revocation_withdrawal"
  - "mechanism/structural_withholding"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "user/general_public"
  - "user/small_business"
  - "substrate/document_pdf"
  - "substrate/financial_record"
---

# Bunny Notes -A Gift Card and Cash Note Protocol

> A simple to use decentralized Cryptographic Note protocol that works with Zero-Knowledge Proofs and allows creating Gift Cards and Cash Notes that can be transferred offline or spent

[Devpost](https://devpost.com/software/bunny-notes) · hackathon [[TRON Grand Hackathon - Season 3]]

## Facets

**mechanism** [[on_device_local]] [[revocation_withdrawal]] [[structural_withholding]]
**domain** [[finance_payments]] [[retail_commerce]]
**user** [[general_public]] [[small_business]]
**substrate** [[document_pdf]] [[financial_record]]
  <sub>weak: video_visual</sub>

**stack** circom, ethers.js, express.js, node.js, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bunny notes -a gift card and cash note protocol

## Body

The front page of Bunny Notes application Bunny Notes Logo Visual Explanation of the Bunny Notes protocol, prototype images Inspiration The project was inspired by the simplicity of spending money with pay pass payments every day and I wondered how to implement instant payments with scanning a QR code that is as safe as single use virtual credit cards where the merchant cannot spend more than a set value for protection. I have always adored zero-knowledge proof technology and inspired by the notes used in tornado cash I implemented a similar technology without anonymizing or mixing features. What it does You can create a cryptographic note and deposit value into a smart contract to back the note with the value. The notes can be downloaded as PDF files that can be printed and contain a QR code. This value can be only withdrawn by the owner of the note using a zkSnark that is submitted in the transaction to the network. There are multiple tokens that can be used (ERC20 and variations) and the deposits can be withdrawn 2 ways. Either as a gift card that withdraws the full value 2 As a cash note which allows the user to choose to transfer just a fraction of the value to another user's address while receiving back the rest as change, just like when we pay with a larger note and get change back! How we built it The application uses Circom Circuits at it's heart for ZKP, with solidity Smart Contracts that handle the deposit of value and the value withdraw logic and the zkp verification. The front end is a React app with material design, using ethers.js and snark.js for creating proofs and interacting with the network. There is also a relaying server (express js running in a VPS) that allows gasless payments. It accepts zkSnarks on it's restful API and submits transactions on behalf of users. The zkp can be only generated knowing the contents of the note which never leaves the browser and so the transactions using the proof can be uploaded by anyone. Malicious relayers are never able to alter the transaction thanks to some checks implemented in the proof verification of the zero knowledge proof's circuit! Challenges we ran into The project was originally developed for the Tron network however due to the smart contract limitation time limit (80ms max to run a function) the ZKSnarks could not be verified (Timeout error) and so the project moved to Bittorrent Chain, where it works perfectly now! Accomplishments that we're proud of I have accomplished gasless payments using zero-knowledge proofs, offline transactions using gift cards and instant payments using scanable PDF notes. Users can now use instant payments on the go while never exposing their main wallet balance to a merchant or help onboard new users to the network by giving out gift cards! What we learned I have learned a lot about zero-knowledge proofs and the internal hashing functions, originally planned to use a pedersen hash but then later migrated to poseidon hash which gets the job done much better. What's next for Bunny Notes -A Gift Card and Cash Note Protocol I wrote a detailed post on the forums about the future of bunny notes. The plan is to abstract away the use of metamask completely and use credit card payments for creating gift cards in the future to support greater adoption. This is already implemented in the smart contract side (relayer can purchase gift cards on behalf of addresses) however implementing it will require some liquidity, so in the future I plan to introduce Liquidity Providing and also a custodial or smart contract wallet solution for users to help completely abstract away the wallet for everyday users and allow crypto ownership using notes and payments with just scanning QR codes. I also plan to introduce ecosystem integrations to provide other projects with zkp based note front ends, so for example a betting or staking application could use notes instead of wallets where the users just save the note and use it when they want to withdraw their money. This is possible to do for big projects too like AAVE without special support from their team. It's also possible to create a crypto note based gasless DEX in the future with this technology, and it's on the table. <div