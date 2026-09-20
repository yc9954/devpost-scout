---
slug: "dear-marketplace"
url: "https://devpost.com/software/dear-marketplace"
title: "Deer Marketplace"
hackathon: "NEAR MetaBUILD III Hackathon"
organization: "NEAR Protocol"
winner: true
words: 814
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/structured_db"
---

# Deer Marketplace

> Buy & Sell Anything. Simple, Decentralized, and Secure Marketplace.

[Devpost](https://devpost.com/software/dear-marketplace) · hackathon [[NEAR MetaBUILD III Hackathon]]

## Facets

**domain** [[developer_tools]] [[finance_payments]]
  <sub>weak: civic_government</sub>
**user** [[developer]]
**substrate** [[structured_db]]

**stack** javascript, near, nextjs, rust, thegraph

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for deer marketplace

## Body

Example Store Voting Results for a Dispute Example Item for Sale UI for the Store Creation Form Inspiration The real value of blockchain : I'm not a big fan of the current trends of the blockchain, because most new web3 platforms don't really have a use in our day-to-day life. But I'm a big believer and a fan of the technology behind decentralization and the idea of building something and letting the community take care of the rest. Fairness in design : Typically, companies are designed to make the most money from users, and having a real fair platform is rare if not impossible. What I'm trying to offer in Deer is Fairness for all users and participants that cannot be influenced by profit. Creating New Opportunities : When building a DAO, we give people the power of choice. But what if we take it one step further, and let the community earn rewards by involving them in helping other users solve their problems. What it does Deer marketplace allows anyone to sell and buy anything securely, fairly, and transparently. Anyone can launch their online store in seconds, each store represents one smart contract that handles the escrow and cannot be manipulated in any way. The only fee currently is the storage cost for the smart contract. In case of a dispute between a buyer and a seller, both can call the Dispute Resolution smart contract, which basically lets each one provide his evidence and the community publicly vote for a resolution. Starting a dispute will cost the users a 20% fee on their item but it will go directly to the voters who helped them reach a resolution. How we built it Building Deer I didn't wanna rely on any centralized platform because of the complications of the cost, maintenance, and all the trouble that comes with it. Smart contracts This may change in the future, but here is a list of the smart contracts that currently handle all the core functionality and database of Deer: Store Factory : This contract is responsible for deploying and managing the stores' smart contracts. It also keeps track of the stores and the code versions. Store : This contract is responsible for managing the store's data and handling the escrow. Dispute : This contract is responsible for the dispute creation and resolution using votes and can be linked to any store. All smart contracts are written in Rust which I had to learn from scratch these 60 days. Indexer In addition to the smart contracts, we are using The Graph to index the data from the blockchain and make it available to the front end. This will allow us to have better control over how to store and fetch data, such as searching capabilities and stats tracking. Front-end The front end is built using Next.js and is currently hosted on Vercel until there is a better decentralized solution. The UI is designed for user experience and has the feeling that it kinda belongs to the near ecosystem with some minor similarities. Challenges we ran into The biggest challenge was time as I wanted to be part of this hackathon, but Deer is a pretty big project and needs a lot of effort for each part of it. However, the biggest chunk of the project is done and the only thing left now is to improve it and fix the hidden bugs to make it ready for Mainnet and make it a platform that people actually need and love. Accomplishments that we're proud of Learning Rust, that's my favorite coding language now. Also, proud of the UI design which was done by my friend. But I won't feel really accomplished unless Deer actually become a big part of the blockchain world and be used by others. What we learned I learned everything about Near, all the libraries, Rust... I learned how to rethink real-world problems using blockchain and community. What's next for Deer Marketplace The goal is simple: make Deer a product people need and love. But the road to that is going to be hard, especially for a solo developer but definitely worth pursuing. I'm planning to work full-time on this project if I win, If not, I'll keep working on it as a side project and apply to Near grants. In general, this is my plan for the future: Finalize the MVP of the platform with proper testing and quality insurance. Start a proper DAO for Deer and start getting other people involved using bounties. Get someone to spread the word, and handle social media and community. On the feature side, these are my planned features: A way of communication between seller and buyer without leaving the platform. Support push notifications to inform users about their orders. Each store should be able to have its own custom domain. More ability to customize the stores. <div