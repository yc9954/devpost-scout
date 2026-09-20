---
slug: "paradao"
url: "https://devpost.com/software/paradao"
title: "ParaDAO"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 911
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/financial_record"
---

# ParaDAO

> ParaDAO provides tools for communities with the same passion / shared interests to come together to organise amongst themselves to achieve a common goal.

[Devpost](https://devpost.com/software/paradao) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[civic_government]] [[developer_tools]] [[health_clinical]]
**user** [[patient_family]]
**substrate** [[financial_record]]

**stack** cumulus, docker, ink, polkadotjs, react, rust, substrate, typescript, zeitgeist

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for paradao
- try it out!

## Body

Prediction Market ParaDAO homepage DAO details Dao with prediction market ‼️ Update 15th July: currently we are experiencing CORS policy change for https://ipfs.zeigeist.pm/api/v0/* and our domain has been blocked. https://paradao.space is not able to create / fetch PM in the DAO, we are trying to contact Zeigeist to solve this issue. Inspiration We are inspired by creators / organisers who dedicate their time, possibly outside of their normal job, to provide valuable content to many people. We would like to build tools to help them to have more direct support with their fans and community members. During the pandemic, the things that are the most important, really came into focus. Artists, are the fabric of life, and we want to make it easier to show support, and let them keep doing what they do. The idea of donating your staking profits seemed like a no brainer. Every little bit counts. New technology brings so much potential, as to what is possible, and we are excited to help it evolve in the right way. Going to meetups to meet like minded people is a great service, and countless people have incredible experiences, meet new friends, and discover their next passions because of them. Unfortunately organizing them cause bring lots of headaches. Allowing members to vote of potential activities, locations, gives power to the members, and more incentive to pay the fee to join. Allocation of these funds, allows for even better events, and paying the organizers, even if its just a coffee or beer, to show your appreciation. Another natural fit. What it does ParaDAO provides tools for communities with the same passion / shared interests to come together to organise amongst themselves to achieve a common goal. By creating a no code platform to create DAOs, we hope to inspire new communities to adopt, and inspire in new directions. Not only can communities create proposals, and have members vote on the issues that matter. With the power of predictive markets, it takes everything to a whole new level. By using the probability of real world events, DAOs can make even better decisions, like never before. With the relay chain, we can teleport assets in from other chains, bringing a new freedom across chains, and allowing a global reach. We have only began to touch on this, but we cannot wait to think of new implementations of contracts that thrive with this new flexibility. How we built it Blood, heat wave induced sweat, and tears. with some good old fashioned lack of sleep sprinkled on top. also, we used docker,, substrate, ipfs, polkadot, zetgeist, ink!, react, typescript, POLKDADOTjs, tailwind css, vite, husky Challenges we ran into There were several challenges that we faced. Relay Chain teleporting assets: we had to understand the different filters to allow our Parachain to recieve assets Ink! is new all all of us and we had to understand what primitives we can use and how the underlying storage works Zeitgeist parachain, we attempted to connect Zeigeist parachain to our relay chain so that we can call create prediction market directly with XCM, but we were only able to get it to produce the first block. local setup, needed to create docker containers and scripts to actually be able to run the relay and parachain locally documentation reorganization and changing while studying them, did not make life easier Accomplishments that we're proud of We are very proud of us being able to create DAOs, store and retrieve data on IPFS, and implement a voting system. The user interface was also a challenge as we had to connect to two different chains and use different SDK. It was fun to learn more about polkadot, and how game changing the XCM will be. We were able to just touch on the tip of the iceberg as to what is and will be possible, and cannot wait to keep discovering. What we learned Quite a bit! First of all, Ink! is nice to work with. polkadotjs has so much magic, so really enjoyed reading Zeitgeist documentations. so much potential. We also learnt quite a bit on XCM and how to add extension to the pallet-contract and in general how to configure xcm-pallet. What's next for ParaDAO We would like to deploy our contracts on a Ink! supporting parachain. This will allow us to focus less on infrastructure and provide UI. We would also like to support content providers with staking options for their DAO so that it is easy for them to have some passive income. We would love in integrate the prediction market with the proposals / DAO itself, however, this is 2 different transactions and repeated on chain data. Therefore we would like to integrate with an indexer to serve prediction market info with the DAO. Currently, we do not have this infrastructure. Try it out! Please fund yourself with paradao parachain tokens (to create, join, propose and vote) with wss:://paradao.space/paradao Also fund youself with Zeitgeist dev tokens (to create prediction market and buy OST) with wss://paradao.space/zg Head over to paradao.space 🚀 Note: the Paradao Parachain has a block time of 12 seconds, please be patient Note: if you made the proposal, your vote has been counted and you cannot use the same account to vote again Note: Currently the Prediction Market is stored in localStorage (please see Next steps regarding indexer for this). So you can test our PM buying feature if you create a market yourself. <div