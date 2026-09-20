---
slug: "blockreg"
url: "https://devpost.com/software/blockreg"
title: "Blockreg"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 725
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/finance_payments"
  - "domain/transportation"
  - "substrate/financial_record"
---

# Blockreg

> Blockreg is an event registration/ticketing platform built on the Ethereum blockchain.

[Devpost](https://devpost.com/software/blockreg) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[finance_payments]] [[transportation]]
**substrate** [[financial_record]]

**stack** amazon-web-services, chainlink, ethereum, keychain, linkpool, python, react-native, social-networks-software, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blockreg

## Body

Inspiration I'm interested in exploring the idea of digital identification, but I don't think we're quite at the point where it's safe to post sensitive personal information on-chain -- once it's out there, it's out there forever. Event registration presents an opportunity to develop best practices around storing semi-secure data (a person's work email, for example) without the risk of permanent life-altering damage. It lowers the barrier of entry for people who might otherwise be skeptical about digital identity by presenting a practical use case that's ephemeral and pragmatic. What it does You can create events and register for them. How we built it The contracts are in solidity, the front end is a react native app. Because big blocks of string data (like a hackathon description, for example) are so expensive to store on-chain, I used Chainlink to create a bridge to IPFS. The app submits all the data to the contract, and the expensive parts are offloaded to IPFS, and the CID that's created is stored on-chain with the inexpensive uints. The IPFS connection and badge createion are AWS Lambda functions. We could allow the front-end to store the data on IPFS and simply pass that CID into the contract at creation, but this flow is preferable for a number of reasons: Data validation: this allows my contract to do things like validate identity against an API, or implement content policies (banned word lists for example). It's an extensible solution. Data integrity: if my contract builds the JSON objects on IPFS, I know they fit the standard. If anyone could submit a CID to my contract, I wouldn't know what's in it. Front-end agnostic: Don't like my app? That's fine, write your own -- but the technical requirements of the blockreg infrastructure are still guaranteed because they're enforced at the contract level instead of the in the client. The other beauty to this is that the costs are fixed -- if we want to add accommodation information, survey questions, attendee bios, keynote schedules etc. etc, the cost of hosting all of that doesn't change because it gets offloaded to IPFS. Challenges we ran into Well I've never written a smart contract before this, so step 1 was learn the language. Also, I would say that the documentation around external adapters and chainlink nodes is not fantastic -- it wasn't until I found out about NAAS on linkpool (through the discord) that it really opened up. Overall, testing chainlink isn't great because you can't do it locally. It adds a fair amount of time to each iteration to deploy and test everything on a testnet. I would say if there was one piece of the infrastructure I'd like to see improved, it's that. Accomplishments that we're proud of I generalized my chainlink IPFS code into a module called Storable, kind of like Ownable. It allows you to add data offloading to any contract. Also, I really like my pseudo-linked list implementation in the Registrations contract to make moving through the huge registrations array fast and efficient. What we learned So, so much. I have a decent grasp on solidity I think -- not an expert, but I have a feel for the language and patterns. Also, it wasn't until I started working in the ecosystem that I truly began to understand the power of decentralization. Ten years ago I built a registration platform and so much of my job was running servers and dealing with traffic surges. At one point our payment processor froze all our money and stopped accepting payments (Paypal man, they suck). Now I built a registration platform that has literally zero servers and no payment processor. That's insane. What's next for Blockreg I'm pretty stoked on this project. Not exaggerating, I probably put 140 hours into this, and I'd love to see if anyone else thinks there's a there there. I'm going to keep working on it (though at a slower pace -- I haven't slept in a week). I'd be very interested in an incubator or accelerator if the project gains any steam. Events seem like a great market for crypto adoption -- what if all concert tickets are sold in doge? What if Coachella was sold in Solana? At 50k transactions/second they could sell out in 3 seconds, and there are no servers to crash during registration. <div