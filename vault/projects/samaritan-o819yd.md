---
slug: "samaritan-o819yd"
url: "https://devpost.com/software/samaritan-o819yd"
title: "SamaritanOS: A DID-based Web3 Cloud Access Layer"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 311
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/revocation_withdrawal"
  - "mechanism/simulation_digital_twin"
  - "substrate/financial_record"
---

# SamaritanOS: A DID-based Web3 Cloud Access Layer

> SamaritanOS describes a living vessel (a “means to an end”) made up of 1s and 0s, which can be accessed by any on-chain account, whose state is created and shaped uniquely by its users’ interactions

[Devpost](https://devpost.com/software/samaritan-o819yd) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**mechanism** [[realtime_stream]] [[revocation_withdrawal]] [[simulation_digital_twin]]
**substrate** [[financial_record]]

**stack** c, css3, html5, javascript, node.js, rust, substrate

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for samaritan

## Body

Inspiration This project was inspired by the many scandals and misuse of power by big corporations. What it does It gives you the power to control your online data and activities however you want. How we built it SamaritanOS is still in its early stage undergoing its idealization testing phase. It is currently being lightly built with its client as a simulated terminal on a browser and a node-js server. This encourages quick-testing and speed of changing ideas and implementation paths. It currently utilizes JavaScript, node-js and Substrate. We built a terminal on a browser simulating a native terminal. This terminal stands as the SamaritanOS in that it accepts commands and delivers it to the node-js server running in the background. We then made the server query the chain, communicate with other decentralized protocols, and deliver whatever state change or information to the terminal and back to the user. Challenges we ran into Currently, there's been no major one. Accomplishments that we're proud of Being able make state changes on-chain and on decentralized protocols/networks through the terminal in real-time was really cool. What we learned Among other things, we learnt more about governance on substrate chains. What's next for Samaritan Short term goals Build native access to the Crust storage layer inside the OS (the terminal and server) Provide applications and Samaritans alike with their own DIDs using the Kilt protocol Add an application to a Samaritan state and build a minimal structure for the app to access the Samaritan state. Revoke access to an application by submitting a transaction. The web prototype is still in the first wave(there are three waves) which is yet to be complete. The second wave would focus on getting things correctly and loose coupling a lot of things. Then the third wave would focus on robustness. After the web MVP, we then go native. <div