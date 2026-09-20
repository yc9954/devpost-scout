---
slug: "vernari-protocol"
url: "https://devpost.com/software/vernari-protocol"
title: "Vernari Protocol"
hackathon: "Chainlink Spring 2023 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 323
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/retail_commerce"
  - "user/general_public"
  - "substrate/financial_record"
---

# Vernari Protocol

> Web3 E-Commerce security platform for businesses allowing for automated escrow accounts which unlock based on shipping information. Peace of mind for users and yield earning opportunities for sellers.

[Devpost](https://devpost.com/software/vernari-protocol) · hackathon [[Chainlink Spring 2023 Hackathon]]

## Facets

**domain** [[retail_commerce]]
**user** [[general_public]]
**substrate** [[financial_record]]

**stack** chainlink, foundry, nextjs, react, solidity, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vernari protocol

## Body

Inspiration This inspiration for this came from the uneasy feeling with buying items with crypto and never knowing if I will ever get my package. Having a trust less system where transactions of goods can happen with verifiable off-chain data seems like a perfect tool for e-commerce businesses that want more user adaption. What it does Vernari means 'One who protects' in old Norse. The protocol aims to be a trust less middleman between consumers and sellers. The protocol plugs into existing e-commerce platforms and stores the revenue in escrow vaults which are then unlocked when tracking information is verified delivered to the individual. This allows for more piece of mind for users knowing that e-commerce stores wont run off with their money. On the seller side, stores can now earn yield on their escrow'd money which when unlocked by delivery can still be kept there earning yield. How we built it The protocol was build using Foundry/Solidity on the contract side and React/Nextjs on the front end. Chainlink Automation along with the new Chainlink Functions product was used heavily with bringing off chain shipping data into the contracts. Challenges we ran into The largest hurdle with making a scale-able product and incorporating Chainlink Functions into the mix. Password and data encryption was also a hurdle since store owners need to manage both Automation/Functions subscriptions. Accomplishments that we're proud of Most proud of getting the new Chainlink Functions up and running and integrated into the contracts. What we learned Learned a lot about Chainlink Functions since its a brand new product, and how powerful of a tool it is. What's next for Vernari Protocol Next for Vernari is getting the UI/UX more beefed up and getting it integrated into a smaller marketplace to start off with. Also, allowing for more assets to be incorporated into the platform which stores can earn yield from. Creating different yield strategies that stores can choose from. <div