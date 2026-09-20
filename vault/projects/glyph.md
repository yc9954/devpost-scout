---
slug: "glyph"
url: "https://devpost.com/software/glyph"
title: "Glyph"
hackathon: "NEAR MetaBUILD Hackathon"
organization: "NEAR Protocol"
winner: true
words: 530
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/media_journalism"
  - "user/developer"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Glyph

> Glyph is a wiki engine that allows its contributors to get rewarded, through a learn-to-earn and teach-to-earn model, powered by NEAR.

[Devpost](https://devpost.com/software/glyph) · hackathon [[NEAR MetaBUILD Hackathon]]

## Facets

**domain** [[developer_tools]] [[media_journalism]]
**user** [[developer]]
**substrate** [[financial_record]] [[video_visual]]

**stack** near, near-api-js, next.js, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for glyph

## Body

Inspiration The advent of the creator economy and web3 has shined a light on the exploitation of users in the modern web. They do not get rewarded for their data or their user generated content in an efficient way. Wikipedia, although a pioneer of free and open applications on the internet, suffers from many of these ills. Editors are not rewarded for their edits and the people that volunteer are mostly hobbyists. This is very exemplary but inevitably leads to a monopoly of information. Only a fraction of Wikipedia's users are editors,. Also, surprisingly, most articles today are maintained by marketers and journalists, depending on their agenda. Incentivizing more of the population to share what they know about the world is one way to stop such a monopoly on information. Glyph solves all these problems thanks to the new advancements made in blockchain technologies. With the power of web3, participants can easily sign in and contribute by just connecting a wallet, glyph users will be able to edit in a familiar way like using Notion without needing to know markup. Contributors will also be able to earn tokens and ownership for their contributions. What it does A wiki protocol that allows its contributors to get rewarded with tokens. Imagine if Wikipedia was on-chain? What would be different? A modern wiki editing experience. (see: Confluence , Notion & Mirror ). A new economic model powered by blockchain tech. The users. Editors/readers , who come to learn or contribute knowledge. Websites/Communities and DAOs , that want to crowdsource knowledge from their users. Publications and media outlets, for content creation. Editors have a chance to get rewarded for their contributions, while 3rd parties can mobilize their community (or our user base), and incentivize them to create and maintain public facing content. How we built it For the hackathon prototype we forked and improved on a Notion clone to build our front-end UX, on the back-end the articles are minted as NFTs on the NEAR testnet, the article JSON is also deployed to the Arweave mainnet (the Arweave transaction ID is in the NFT metadata). Challenges we ran into We managed to implement everything we defined for our prototype, although we had some trouble deploying images on Arweave. The NEAR developer experience is very comprehensible and painless. Accomplishments that we're proud of Deploying on testnet. Working with other developers from the ecosystem and community. We started working on the project about halfway through the hackathon and we managed to submit something in time. What we learned Learned about NEAR's unique NFT standard. Working with a team in different time zones efficiently (remote). Also learned a lot of Rust. What's next for Glyph Prototype (For the Hackathon) - It will be a basic article editing loop; connect wallet, edit, publish and mint token, disconnect wallet - deployed to the NEAR testnet (Done). Testnet - Prototype with more functionality, article NFT will be fractionalized to allow new editors ownership, also the utility token $NOUS will get minted when users participate in the platform (~3 months). Mainnet - Testnet application with more functionality, article monetization and and in-app marketplace for the article NFT tokens (~3 months). <div