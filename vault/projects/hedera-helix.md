---
slug: "hedera-helix"
url: "https://devpost.com/software/hedera-helix"
title: "Hedera Helix"
hackathon: "Hedera22: Hello Smart Contracts"
organization: "Hedera"
winner: true
words: 484
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Hedera Helix

> Help the environment with Hedera Helix for Heroes.

[Devpost](https://devpost.com/software/hedera-helix) · hackathon [[Hedera22- Hello Smart Contracts]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[education]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[video_visual]]

**stack** blockchain, git, hedera, node.js, nuxt, solidity, vue

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i’ve learned and what i’m proud of
- what’s next

## Body

Demo sign-in page Store account overview page Store account search page User account overview page User account item detail page Inspiration The inspiration for this challenge came from observing my neighbors (mostly students) throwing away piles and piles of good furniture when they move out. I try to throw away and buy as little as possible and I wanted to inspire people to buy and sell more items second hand and/or to use their bought items for a longer period of time and make people more aware of how each of their choices have impact on the environment. What it does A smart contract is attached to each product in Helix. This contract contains a deposit that you pay when you buy the product. The deposit reflects the environmental impact of the materials in the product and the impact of the transportation from the production country to the store. Up to 60% of the deposit will be returned to you over time or after you sell it, 30% of the deposit is transferred to the person who buys the item second hand and 10% is donated to an environmental charity. How I built it The front-end is build with Vue and Nuxt. The smart contracts are written in Solidity. To make the app more efficient, all data retrieved from the Hedera network is stored in a Vuex store such that most data is retrieved only once while using the app. Static data is also encoded and combined in a single string to reduce the amount of queries needed. Challenges I ran into The main challenge I ran into was storing and retrieving data efficiently, to reduce gas fees and to ensure a smooth user experience. Furthermore, I needed to keep track of which smart contracts were created from the app. I solved this by creating another smart contract that maps user IDs to their smart contract IDs. What I’ve learned and what I’m proud of During this hackathon I learned to write smart contracts, I learned Solidity and learned to use Hedera SDK services. I’m also proud that I could use my recently learned UX and front-end skills to create a clean user interface for the dApp, which is optimized for use on mobile devices. This was also the first time in my life that I participated in a hackathon and without this hackathon I probably wouldn’t have been able to learn all these things in such a short amount of time. What’s next Making the app fully production-ready by replacing the demo data, such as accounts and images, with real data. Making a stronger (physical) connection between the product and the smart contract (using QR code, RFID, …), which also creates opportunities for garbage collection services. Making the deposit more accurate (e.g. tracking the amount of energy that is being used in different product supply chains and including the corresponding C02 emission) <div