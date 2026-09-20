---
slug: "permanent-voting-with-fractional-vote-delegation"
url: "https://devpost.com/software/permanent-voting-with-fractional-vote-delegation"
title: "Permanent Voting with fractional vote delegation"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 326
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "substrate/web_dom"
---

# Permanent Voting with fractional vote delegation

> Imagine no term limits for elected officials. Imagine them having to prove themselves again competitors every two weeks. By actually achieving something. That is a core inspiration for this project.

[Devpost](https://devpost.com/software/permanent-voting-with-fractional-vote-delegation) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]]
**substrate** [[web_dom]]

**stack** chainlink, express.js, orbitdb, react, solidity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for permanent voting with fractional vote delegation

## Body

Inspiration https://lex-kravetski.livejournal.com/626412.html (In Russian, author is not me) In short idea is to allow permanent voting for elected officials or for policies. They have to remain in place for as long as they have the majority's support. Technologies nowadays allow to implement direct democracy, but for the amount of the potential decisions people could make some voting power delegation would still be nice. An ability to have multiple delegates and sensible algorithm for counting votes would be very much appreciated in my opinion What it does The project combines on-chain voter registry and off-chain delegation graph. They are both connected with frontend application that allows user to interact with both of them. Users can choose delegates for themselves and cast and re-cast votes. The system can display results based on delegation graph and voter registry. How we built it Lots of googling, reading the docs and good old-fashioned trial and error Challenges we ran into I have working experience with only React frontends, so Creating a SmartContract, connecting to contract using web3 libraries, figuring out how to incorporate IPFS via using orbitdb were very real challenges. Also I always have trouble limiting scope of my ideas and often end up with incomplete projects. Accomplishments that we're proud of Most of all I am very proud of making a complete working demo. Incorporating a bunch of new technologies that I was unfamiliar with. I think that idea has a lot of potential and I've built a great core which would allow to extend and expand this project in the future. What we learned A bunch of new technologies. How to prioritize working functionality over ambitious ideas. That implementing an leaves you with more ideas that you would wish to implement, not less. What's next for Permanent Voting with fractional vote delegation Nicer UI Ability to create proposals and have discussions on them Figuring out how to work with user's Identity Assigning voting rights ...a lot more <div