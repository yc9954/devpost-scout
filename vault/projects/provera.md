---
slug: "provera"
url: "https://devpost.com/software/provera"
title: "AutoTrust AI Escrow"
hackathon: "MNEE Hackathon: Programmable Money for Agents, Commerce, and Automated Finance"
organization: "MNEE, LLC"
winner: true
words: 413
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/developer"
  - "user/small_business"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# AutoTrust AI Escrow

> A web app based on the MNEE blockchain that acts as a bridge between developers and employers by integrating the MNEE typescript SDK and ETH smart contracts.

[Devpost](https://devpost.com/software/provera) · hackathon [[MNEE Hackathon- Programmable Money for Agents- Commerce- and Automated Finance]]

## Facets

**domain** [[developer_tools]] [[finance_payments]] [[health_clinical]]
**user** [[developer]] [[small_business]]
**substrate** [[structured_db]] [[web_dom]]

**stack** express.js, firebase, gemini, next.js, node.js, solidity, tailwind, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for autotrust ai escrow

## Body

Inspiration What inspired me in building this project was the need to automate payments when developers bid for jobs as freelancers. I wanted a system whereby anyone could get paid without even having contact with the other party. What it does It basically acts as a bridge (ESCROW) between Employers and Developers. It allows an employer to create a task and simply wait for a developer to execute it. More of a fiverr that’s automated. The AI system then verifies the developer’s submission before the employer releases it. The developer is also kept safe due to the dispute automation that releases coins when a dispute has been lodged. It will release the coins as long as the developer has met the criteria of the submission requirements. If an employer isn’t satisfied with the work, he/she has the option of lodging a dispute before the AI automatically releases the coin to the developer. How we built it I first crested a next.js project and designed the landing page before completing the employer and developer page. I setup a new firebase project and added a web app before configuring the database rules, allowed origins and the likes. I then proceeded with the backend which I build in typescript. The first was setting up the server before the major endpoints then configuring the MNEE typescript SDK and CLI. Also has had to create a developer account and API key in order to interact with MNEE. The last thing one the list was designing the smart contract and deployment. I therefore got Gemini api key and updated the variables of both the frontend and backend. This is the CA of the contract deployed using the MNEE CA address as a constructor: 0x9181e6E152d9e77F0642650312E002827367E316 Challenges we ran into Getting the faucet via the MNEE CLI was really hard. I kept on running into 400 error timeout codes while requesting sandbox tokens. I also had a hard time making it a dual system that supports two major blockchains. I had to deploy the smart contract severally. Accomplishments that we're proud of I’m proud of finally deploying to production with a live url that works with wallet extensions enabled for MNEE and ETH. What we learned I learned how to use the MNEE CLI and how to properly diagnose server related issues when dealing with escrows onchain. What's next for AutoTrust AI Escrow We’ll definitely be looking at deployment to the main stream, onboarding of more users, and major upgrades. <div