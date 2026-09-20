---
slug: "reservoir-levels"
url: "https://devpost.com/software/reservoir-levels"
title: "Reservoir Levels"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 447
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Reservoir Levels

> Reservoir Levels gamifies the process of water conservation.

[Devpost](https://devpost.com/software/reservoir-levels) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**substrate** [[document_pdf]] [[web_dom]]

**stack** chainlink, ethers.js, express.js, hardhat, javascript, next.js, react, soldiity, tailwind.css

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for reservoir levels

## Body

Inspiration My inspiration for Reservoir Levels was the droughts in California. I decided to look more closely and found out that the water levels in our reservoirs were consistently below their historical averages. What it does Reservoir Levels is meant to gamify water conservation. Users are divided into water districts based on where they live. If the reservoir levels in a water district are above their historical averages then the users will receive a payout in Ether. How we built it I build the frontend using React and Tailwind css. I build a solidity smart contract to handle the logic. I used Chainlink keepers in order to periodically get the reservoir levels (daily), calculate payouts (seasonally), and update historical averages (yearly). I used Chainlink api calls in order to call a water levels api to get the reservoir levels. The reservoir data given by the State of California is done vie a legacy system with no public api! In order to get around this I took the data from their website ( https://cdec.water.ca.gov/cgi-progs/products/rescond.pdf ) and made my own api that I could call the data from. Challenges we ran into One challenge I ran into was learning how to use the Chainlink api call service and Chainlink keepers. I found the videos by Chainlink on Youtube super helpful! Another challenge was figuring out how to get the data I needed into the smart contract. Because the reservoir data provided by the State of California is a legacy system with no public api, I needed to build my own. Accomplishments that we're proud of I am super proud of my smart contract and frontend. I put a lot of work into learning about Chainlink keepers and API calls in order to make the project. I think the frontend I made is able to communicate the reservoir levels clearly to users and gamify the process of conserving water. The smart contract is working and is ready to be tested with real users. What we learned I learned so much about Chainlink and what it means to build a hybrid smart contract! I learned about Chainlink keepers and how to call api's with Chainlink. I've come away really impressed by how Chainlink allows blockchain to be used in the real world. What's next for Reservoir Levels We will partner with the State of California in order to build an official reservoir data api. We would then look to test out the project in a water district with real users. In the future we would like to pay our users in an ERC20 token representing water rather than ETH. We are looking forward to making a difference in conserving water! <div