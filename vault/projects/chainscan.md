---
slug: "chainscan"
url: "https://devpost.com/software/chainscan"
title: "Chainscan"
hackathon: "Polkadot Hackathon: North America Edition"
organization: "AngelHack"
winner: true
words: 321
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "substrate/financial_record"
---

# Chainscan

> Explore on-chain data via an intuitive interface.

[Devpost](https://devpost.com/software/chainscan) · hackathon [[Polkadot Hackathon- North America Edition]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[media_journalism]]
**substrate** [[financial_record]]

**stack** bootstrap, javascript, netlify, react, subsquid

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chainscan

## Body

Home_screen_desktop Event_screen_mobile Inspiration Chainscan was inspired by Subsquid 's onchain-data indexing framework which provides archives that are quite useful when one needs to run fast queries for historical blockchain data. We needed to leverage those publicly available archives to provide a way to explore data for each network on the archive registry. The UI design and layout was inspired by Subscan . What it does Chainscan provides a UI interface to explore on-chain data for any network listed on Subsquid Archive Registry . It fetches data from the GraphQL backend provided by each archive and displays them in a searchable format. Among others, it provides a way to view events and transactions in a given block, both by height and block hash; and also filter events by their name. A user can also see transactions by the signer address. How we built it Chainscan was built with React (using CRA ). We applied Bootstrap classes for styling. We wrote a custom hook to make GraphQL queries to retrieve chain data from the archive of each chain, whether from the Registry or a locally running archive. React's Context API is used to persist the current archive data across the app. We hosted the project on Netlify which provided free CI/CD pipeline and hosting. Challenges we ran into It was difficult to provide pagination for the lists (blocks, events, transactions) because the Archive GraphQL backend doesn't provide that feature. It is only available on Squid GraphQL backends. Finding a team mate especially one that specializes in UI/UX was difficult. Subscan design and layout was adopted as a last resort. Accomplishments that we're proud of Being able to put together the project with all the required features in a short time was a great feat. What we learned We learned more about web3, Substrate and the Polkadot/Kusama ecosystem. What's next for Chainscan To develop it further into a full-fledged explorer for Substrate chains. <div