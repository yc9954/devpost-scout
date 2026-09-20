---
slug: "bloinx-opyq7d"
url: "https://devpost.com/software/bloinx-opyq7d"
title: "Bloinx"
hackathon: "Celo's Make Crypto Mobile Hackathon"
organization: "Celo"
winner: true
words: 550
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "substrate/financial_record"
---

# Bloinx

> A dapp that helps users to create reliable savings communities known as "tandas" or "chit funds" by using smart contracts, in a transparent, verifiable, and trustworthy environment.

[Devpost](https://devpost.com/software/bloinx-opyq7d) · hackathon [[Celo-s Make Crypto Mobile Hackathon]]

## Facets

**mechanism** [[revocation_withdrawal]]
  <sub>weak: cross_origin_web</sub>
**domain** [[finance_payments]] [[labor_employment]]
**substrate** [[financial_record]]

**stack** react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bloinx

## Body

Login page(working dapp on Alfajores) Customized saving round creation (working dapp on Alfajores) Registration page (working dapp on Alfajores) Dashboard (working dapp on Alfajores) Inspiration Studies from the International labor organization show that more than 60 per cent of the world’s employed population are in the informal economy and are concentrated in developing and underdeveloped countries. Since financial institutions require proof of income to give credit, the 2 billion informal workers around the world are imposed high interest rates or get excluded. Rotating saving and credit associations(RoSCAs) compensate some of the financial needs of the informally employed population. They are groups of people that agree to make periodic payments and each period one participant gets the bag, the first ones to get the bag get an interest free loan and the last use it to save creating a microfinancial system from a trusted network. Variations of this system have been used for many years in countries from Latin America, Asia and Africa. The saving circles usually rely on one person who organizes the list with the order, keeps record of the payments, reminds people to pay and sometimes receives payments and distributes the bag. This person is very organized and trusted by everyone but needs to perform many activities so the saving circle is succesful. What it does Bloinx is an application where users will be able to create and join saving circles from their computer or phone. Since it will run on blockchain, payments and withdrawals will be done remotely and all of the transactions will be permanently recorded to get a reputation record. Bloinx will perform most of the aministrator's tasks making saving with your friends easier! How we built it Through our platform, the users will be able to easily create a customized smart contract with the number of participant and saving amount that best suits their needs. The smart contracts were developed in Solidity and the frontend with react. The saving round smart contract receives the payments and only allows the person in turn to withdraw keeping the funds save in a self managed way. Challenges we ran into During user testing we discovered that the usage of the native token(CELO) for the saving rounds is confusing for non crypto users so the need for a stablecoin integration at this stage became critical. We fast tracked the cUSD integration and testing and now have deployed the new version on Alfajores with the cUSD currency integration. Accomplishments that we're proud of We launched our dapp on Alfajores November 22th and as of the 24th we have 40 users on the pilot program. With this pilot we are testing the smart contract functionality, usability of the frontend and fee proposal. Also we can share this awards and programs: We are currently part of the blockchain cohort of the UNICEF Innovation Fund developing solutions promoting financial inclusion. link We won the Finastra's Hack to the Future 3 link Also we are currently part of the Creative Destruction Lab Blockchain Cohort. link What we learned We found that the smart contract logic needs to be replicated on the frontend to prevent users to execute functions that would revert and cause frustration. What's next for Bloinx Q1 of 2022: Mainet Launch and Valora integration Q2 of 2022: Reputation token launch <div