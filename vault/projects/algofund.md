---
slug: "algofund"
url: "https://devpost.com/software/algofund"
title: "AlgoFund"
hackathon: "Hack the North 2019"
winner: true
words: 353
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/financial_record"
---

# AlgoFund

> A decentralized bounties platform on Algorand

[Devpost](https://devpost.com/software/algofund) · hackathon [[Hack the North 2019]]

## Facets

**domain** [[developer_tools]] [[labor_employment]]
**user** [[developer]]
**substrate** [[financial_record]]
  <sub>weak: web_dom</sub>

**stack** algorand, css, flask, html, javascript, python, react, surveymonkey

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into

## Body

GitHub OAuth (before linking with Algorand mnemonic) Bounty explorer Create bounty interface Inspiration Each one of us loves programming. We love going to hackathons, using new tech, and combining it all together to build something cool. Oftentimes, we're building with open source software: React, Express.js, Tensorflow, you name it. Unfortunately, these (and any other open source project) have bugs and feature requests that end up piling onto the repo page, with many buried, never to be fixed. Encountering these issues is already super inconvenient for hackers like us, but imagine the headache caused for companies using the open source platform in production. As much as we all love software, very few developers use their precious time to contribute to open source - especially to fix issues that they themselves aren't personally facing. This is why we created AlgoFund (a pun on "I'll go fund"), a decentralized bounties platform that allows anyone to attach a bounty to any GitHub issue - giving a reward to the developer who successfully solves and merges a solution. What it does AlgoFund is a fully featured bounties platform. Users fund and explore active bounties through our React web app by signing in with Github and associating an Algorand wallet (through mneumonic). Bounties are pulled directly from the blockchain into a fully responsive, non-blockchainy user interface that's both fast and easy to use. All bounties are linked to real Github issues, which get automatically updated as potential workers apply and start working on a bounty. How we built it AlgoFund is built using the versatile notes field built into Algorand's transactions. The backend for managing the Github issues is built using Flask and Python. All of this is tied together with a React front end. Challenges we ran into The Algorand API ran into a few issues at the beginning, but those were quickly resolved. Still, using a new platform like this is never a breeze so we're happy we pulled it off! Additionally, designing all the user and data flows was tricky. We also integrated user feedback with Surveymonkey! Also GitHub kept banning our test accounts >:(( <div