---
slug: "web3-meetup"
url: "https://devpost.com/software/web3-meetup"
title: "Open Meetup"
hackathon: "Polygon BUIDL IT : Summer 2022"
organization: "Polygon"
winner: true
words: 405
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/financial_record"
---

# Open Meetup

> Organize a meetup and earn from participants' social interactions.

[Devpost](https://devpost.com/software/web3-meetup) · hackathon [[Polygon BUIDL IT - Summer 2022]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[financial_record]]

**stack** arweave, express.js, openzeppelin, polygon, react, relay, solidity, web3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for web3 meetup

## Body

UI (as user) UI (as organizer) Meetup Page (Rebranding / Not implemented yet) Leave a comment (Rebranding / Not implemented yet) User profile page (Rebranding / Not implemented yet) User profile page / Activity (Rebranding / Not implemented yet) Inspiration In the past, I organized some Meetups for javascript enthusiasts. They were once a week and every meetup took me at least 4 hours to organize. I had no income from these events so when the platform Meetup.com started to charge me after the free period I decided to stop this activity. The idea of this project is to allow Meetup organizers to have reimbursement for their activity via meetup participants' social interactions and to give also to the participants a way to earn something. What it does As a Meetup organization (one or more organizers) you can create new online Meetups adding some information about the event and a streaming link (via huddle01 ). As an active Meetup participant , you can interact with the organizers by asking questions or liking others' questions (by paying a micro fee). If other participants like your question you can earn from it. As a passive Meetup participant , you can participate freely, and if you want you can leave a "tip" when the event ends. More info here How we built it This project is based on Polygon chain for the transaction part (paid social interactions) and on Arweave chain for the content part (meetup data etc). All the code is open source and is released on Github (it’s a work in progress) The app is fully decentralized, we created a Node.js API as a Gateway to interact with Polygon (via open zeppelin Defender ) and with Arweave . Challenges we ran into So far the main challenge was to avoid DB centralization. We tested different solutions till we ended up using Arweave to store JSON. The next big challenge will be user identification (maybe with Ceramic Self.ID or Polygon ID ???) Accomplishments that we're proud of This one is my first Web3 project so I’m proud of it. I’d like to create some build blocks for more micro-social Web3 projects. What's next for Web3 Meetup complete the API part by adding Queue for meetups and organizations creation (half done) redesign the UX and UI (Sofia just joined the project and is working on the user experience ) create a DAO and structure a business model <div