---
slug: "hacka-link"
url: "https://devpost.com/software/hacka-link"
title: "Hacka.link"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 642
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "user/developer"
  - "user/legal_professional"
---

# Hacka.link

> Hacka.link is a dApp for organizing hackathons that provides full automation, security, transparency and fairness.

[Devpost](https://devpost.com/software/hacka-link) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**domain** [[civic_government]] [[developer_tools]]
**user** [[developer]] [[legal_professional]]

**stack** filecoin, hardhat, ipfs, moralis, react, solidity, typescript, web3

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i'm proud of
- what i learned
- what's next for hacka.link

## Body

How it all comes together :) Inspiration I was inspired mostly by Gitcoin, which is an awesome platform that's showing how the future of open source community may look like thanks to web3. What it does In short, Hacka.link is a dApp for organizing hackathons. As any dApp, it runs on blockchain and ensures full automation, security, transparency and fairness. How I built it I've had minimal experience with smart contracts and web3, so it was A LOT of learning. Luckily thanks to awesome community, great workshops, fantastic open source libraries and frameworks I was able to put it all together. I worked solo and took care of everything, including: system design UI design (well, it is what it is, I'm no designer) smart contract development using Hardhat deployment to Ethereum Kovan network frontend app using React, Moralis, Web3.Storage Chainlink Keepers setup Challenges we ran into I may have been a bit too ambitious in terms of scope, so the main problem was just time. Accomplishments that I'm proud of I'm extremely happy I managed to finish my project in time and I'm very proud of it - it's functional. Obviously there's a lot that still needs to be done to make it production ready, but I managed to finish what I set out to do, which feels awesome. Above all this has been a learning experience and I'm very proud of what I managed to do despite being a newbie in the web3 world. What I learned I learned a ton during this hackathon. My only previous experience with smart contracts and web3 was previous Chainlink hackathon, when I wasn't even able to finish my super simple project in time because of time constraints and being just overwhelmed. This time I had a bit more spare time, so I diligently watched the workshops and started working on my project early. My lesson for the future is to maybe not be so ambitious with the scope, work on something smaller :) What's next for Hacka.link While Hacka.link is functional, it is far from being production ready. There are numerous things to be done like proper test coverage, any bugfixes necessary, audits etc. before it could go live. I also have a list of some really cool ideas for features that I just didn't have the time to implement. Here's a sample of those ideas: Project idea hub - some people come into hackathons with an awesome idea, but no technical skills to execute. Some come in with developer background, but don't know what to submit. Hacka.link could provide mechanisms for voting on best ideas submitted by the community and semi-automatic teambuilding, with incentives for both developers and people who suggested best project ideas. Sponsors - currently the organizer provides funds for all prizes, as well as determines judges. In the future, hackathons could be open for sponsors who could set up their own prizes. Different prize types - currently the prizes have a simple "winner takes all" rule. There could be different types of prizes, for example pooled prize where each eligible submission wins a portion of the pool; or a tiered prize where first place winner gets x%, 2nd place y% etc. Community prizes - participants would vote on their favorite submissions, selecting "community prize winners". Possibly this would require using our own token to prevent sybil attacks. Multi chain - currently the dApp is deployed to Eth Kovan testnet only. It would be great to run on many chains, especially considering Ethereum mainnet is currently not a viable environment for such a dApp due to huge fees. IPFS for storage - currently only project description is saved to IPFS. Instead of just submitting a markdown file as a description, participants could actually submit all of their work (code, video explainer etc.) to IPFS. For more information, please visit https://hacka.link <div