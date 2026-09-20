---
slug: "helppier-k5lbru"
url: "https://devpost.com/software/helppier-k5lbru"
title: "helppier"
hackathon: "Hack the North 2020++"
winner: true
words: 655
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# helppier

> Neighbours helping neighbours through gamified volunteering.

[Devpost](https://devpost.com/software/helppier-k5lbru) · hackathon [[Hack the North 2020-]]

## Facets

**mechanism** [[cross_origin_web]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]] [[structured_db]] [[web_dom]]

**stack** azure, blockchain, cockroach.db, css3, express.js, figma, flask, html5, javascript, node.js, python, react

## How they structured the write-up

- the team
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

The Team We are team Magic4, a multidisciplinary international team that spans across 3 continents and time zones. Amine - back-end dev from Scotland, Glasgow Tele - back-end dev from Lagos, Nigeria Janice - UX designer from Toronto, Canada James - full-stack dev from Vancouver, Canada Inspiration Inspired by the newly born solidarity within the communities across the world during COVID, we were inspired to develop an application which would reinforce those bonds. We aimed to develop an application which would contribute into a better society, therefore we built upon the goals set by the U.N. for a prosperous world through volunteering . Helper x Happier = Helppier What it does Helppier's goal is to encourage a new social norm of volunteering in peoples’ daily routines in their local neighbourhoods. Research has shown that while over 90% of people want to volunteer, only 1 out of 4 Americans actually do. Main barriers to volunteering include lack of time and inflexible volunteering hours. With these pain points in mind, Helppier facilitates neighbours helping neighbours through gamified volunteering with key features including: 1) Volunteering to help people in their neighbourhood - such as grabbing groceries for their 70 year old neighbour, or walking their neighbour’s dog 2) Requesting for help based on location - a streamlined place to send requests for volunteers 3) Earning rewards using the web-app’s cryptocurrency, Karma Coins, to redeem gift cards and donations for charity How we built it In order to build a decentralized network where we can have our own cryptocurrency, and used Microsoft Azure which provides a blockchain service. We used Solidity to create and deploy our smart contract and called our coin “Karma Coin”. Karma Coin is built upon the ERC-20 token standard. To interact with our network, we used web3 and created a Restful API using Express which provides methods to perform a transfer of Karma Coin as well as retrieve the balance for a given user. This Restful API is used by our backend infrastructure which is built using Python, Flask and CockroachDB. All this information is retrieved through API calls made by the frontend which was built using React and designed on Figma. Challenges we ran into While the developers of the team have experience with Python, React and databases like MongoDB, this was the first time they had contact with the blockchain and CockroachDB. Amine spent some time to familiarise himself on Saturday with how the blockchain worked and how he could create a cryptocurrency for our app, especially given that we had no prior experience in the domain. At first, he struggled to understand how he could create wallets and whether he needed to use a Microsoft Azure API to create and add new members to the consortium. However, he later realised through the use of the Chrome extension Metamask, that it wasn’t necessary. He looked at potentially using the Metamask API to interact with his deployed network, however, he found out about web3 and learned how to use it with Javascript. Meanwhile, Tele spent some time learning how to use CockroachDB and struggled to efficiently process geographical coordinates in the database until he found out about Geoalchemy, an extension to work with spatial data. Finally, as the frontend development was led by James, he had a lot of flows to implement from the wireframes and prototypes made by Janice the UX designer. Accomplishments that we're proud of We are extremely proud to have been able to deploy our own cryptocurrency in the short time span we had. Thanks to the team effort led by each individual, we were able to realize a steady progress across the tech stack. In addition, Janice had her first experience with HTML/CSS in a real world project by working closely with James. We are also proud of how well we worked together as a team across 3 different time zones and how much fun we had together. <div