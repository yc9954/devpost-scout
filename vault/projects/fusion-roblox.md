---
slug: "fusion-roblox"
url: "https://devpost.com/software/fusion-roblox"
title: "Fusion Roblox"
hackathon: "Hack to the Future 4"
organization: "Finastra"
winner: true
words: 560
team_size: 6
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/document_pdf"
---

# Fusion Roblox

> Metaverse: Bring Financial Services to the Game Industry & Youth Financial Literacy

[Devpost](https://devpost.com/software/fusion-roblox) · hackathon [[Hack to the Future 4]]

## Facets

**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[document_pdf]]

**stack** accountbalancesapi(b2c), expertpropartnerapi, fusionfabric.cloud, html5, httprequest, javascript, lua, oauth2, robloxstudio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fusion roblox

## Body

Metaverse: Bring Financial Services to the Game Industry & Youth Financial Literacy Bank Account Scenario Mortgage Lead Scenario Crypto>NFT Inspiration People interact in metaverses today People buy and trade at metaverses Where people interact, where people trade, banking follows. We don't know what banking in the metaverse will look like, but we know it will happen. Ideas, hacks, and proof of concepts need to be developed to see what works. The Metaverse we chose in our POC is Roblox for following reasons: • Roblox has over 43.2 million daily active users worldwide • Majority of users are young • Brands like attracting a young audience, as the audience can grow with them • Teaching financial literacy to our youth is crucial. What it does Use case 1 : At Roblox, we build a Virtual Mortgage Brokerage and have a character broker in the game collecting the information from a player, then send the lead to Finastra’s ExpertPro Mortgage Origination system with a new client profile created. In return, the ExperPro API sends back the Client Profile Id along with the Finastra branded message to Roblox player. A document checklist for a typical mortgage application will be emailed to the player for their financial awareness. Use case 2 : We’ve also extended our POC to consume “Create Current or Saving Account” (B2C) API in Finastra’s FusionFabric.Cloud to GET Roblox player’s Account Balances-Similarly, via sending Roblox’s Http request to this API, a player can interact with virtual bank teller in the game and have an immersive experience of “in-person” banking: verify bank account info and check account balances. How we built it 1.Finastra's ExpertPro Mortgage lead scenario: 2.FusionFabric.Cloud> GET Account Balances(B2C) scenario: . Challenges we ran into We had trouble figuring out how to get the authorization token for AccountBalances API at Fusion Fabric.Cloud , The Dev team worked round the clock to tackle it --Our big thanks here to Radu and Sankar from FFDC Support team for their timely help! Accomplishments that we're proud of • From a business perspective, our POC demonstrated an innovative business model of “Embedded Finance” through bringing financial services to the Game industry at Metaverse. Brands like attracting a young audience, that can grow with them. The 10-year-old that deposits their weekly allowance may need a student loan and ultimately a mortgage. • For social impact, our POC has provided a feasible channel for youth Financial Literacy by integrating into a popular metaverse: Roblox has a traction already designed to wrap it’s technical arms around children – we'll bring them into a world where they learn and become an early adopter client of our processes. • From a technology perspective, Evolution from Green Screen Interface to Web Interface to Metaverse interface needs more experimentation as demonstrated in our POC. What we learned • Understand Roblox’s Http Service • Understand more about the FFDC's role in Finastra's strategy • Concept of Youth Financial Inclusion & Embedded Finance What's next for Fusion Roblox • We will explore ExpertPro APIs further to include “Mortgage Quote/Loan Pre-approval” use case where a “lender response” can be sent back to Mortgage lead/Roblox player • We also plan to include Crypto/NFT in our POC by consuming the latest API in FusionFabric.Cloud: Our special thanks to Richard Audette for his input and Trevor Pinkney for the original concept on which inspired this hack. <div