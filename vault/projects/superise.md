---
slug: "superise"
url: "https://devpost.com/software/superise"
title: "Superise"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 656
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "substrate/web_dom"
---

# Superise

> Crypto & NFT giveaways like it's 2077.

[Devpost](https://devpost.com/software/superise) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[developer_tools]]
**substrate** [[web_dom]]

**stack** graph, near-api-js, near-sdk-rs, react, rust

## How they structured the write-up

- inspiration
- try it out
- what it does
- how we built it
- the graph integration (for sponsor challenge)
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for superise

## Body

Cover Home page - Giveaways Finished giveaway box (Winners) Ongoing giveaway box (not joined) Ongoing giveaway box (joined) User account page Create giveaway - Add prizes - Import NFT prize from Paras Create giveaway step 1 - Add prizes Create giveaway step 2 - Set requirements and countdown clock Create giveaway step 2 - Customize tweet template Verify participant's status Inspiration With the popularity of NFT and Crypto projects, there are many fake NFT giveaways on Twitter and it also costs too much energy to host a Twitter giveaway campaign. So we decide to build a tool to make giveaways more transparent and automated. It's called Superise Try it out Homepage: superise.xyz Join a giveaway box: Giveaway #39 GitHub: https://github.com/superise-is-near (You might need a network proxy service if you open the website from mainland China in order to load content from NEAR rpc) What it does Anyone can deposit their NEAR assets (FT/NFT) to our website to create a giveaway box. A giveaway box has a whitelist function, only the account in the whitelist could participate in the giveaway. Additional integration for Twitter Giveaway: Giveaway Creators can specify requirements for joining a giveaway box. For example: follow an account, retweet, and like a tweet. The participant must meet all the requirements before joining the giveaway box. Superise will do the requirements verification automatically through Twitter API. How we built it Write smart contract with near-sdk-rs and write Frontend with near-api-js . Use nep141 's interfaces to check the ft balance of users and transfer ft between users. Use nep181 's interfaces to find the nfts owned by the user in Paras or Mintbase . Use nep171 's interfaces to transfer nfts between users. Use Twitter api to tweet and check whether the requirements specified by the creator are met. Use the Graph to indexes data that is logged in contract methods. Use Figma, GitHub, Notion, Discord to collaborate together as a remote team. The Graph integration (For sponsor challenge) Allow user to query the giveaway they created, joined, whitelisted and won. Add the record and activity, any user could check where their assets come from and go to Users could easily check the distribution of the prizes Users could find data of the deleted giveaways in the Graph which are no longer stored in the contract to save storage cost. The sub-graph could work properly now, but because of the crash of the Graph recently, we won't replace the data source from the smart contract to the Graph until the Graph for NEAR testnet works again. Challenges we ran into The information related to Twitter is off the chain, and we have to be careful when exchanging data between on-chain environment and off-chain environment. It's quiet difficult to make our contract to satisfy nep145 standard. It requires a lot of effort to design an extensible solution to migrate existing data when upgrading contract. Accomplishments that we're proud of We make the crypto giveaways transparent and automated. We build a user-friendly product for both giveaway hosts and participants. We meet internet friends and then work together on this app. What we learned It's the first time we build dApp based on the NEAR. We learned a lot of NEAR's concepts and standards. Many of NEAR's designs are elegant, and it prompted us to think more and deep about dapp development, for example: How to build contract by near-sdk-rs How to interact with other contracts (eg: Paras, Ref) How to use near-api-js How to index data with the Graph What's next for Superise The next step is to do more testing and go to the mainnet. And besides giveaway tool there are a lot of aspects in building and launching a crypto project, eg: Incubation: minting, marketing, ido(initial digital offering), etc Application: trading, renting, mystery box, etc We're not limited to a giveaway tool. Our goal is to provide more tools for building and launching crypto projects. <div