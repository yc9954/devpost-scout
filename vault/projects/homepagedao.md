---
slug: "homepagedao"
url: "https://devpost.com/software/homepagedao"
title: "HomepageDAO"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 599
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/education"
  - "user/educator_student"
  - "substrate/financial_record"
  - "substrate/web_dom"
---

# HomepageDAO

> The first decentralized community-governed, editable homepage.

[Devpost](https://devpost.com/software/homepagedao) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]] [[education]]
**user** [[educator_student]]
**substrate** [[financial_record]] [[web_dom]]

**stack** alchemyapi, chainlink, dart, flutter, ipfs, javascript, nftport, polygon

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for homepagedao

## Body

Inspiration We were inspired to create a community-driven solution for the plague of inactive discord and subreddit moderators in online community spaces. We watched our own UW subreddit fall victim to terrible admins. Originally, the subreddit was a flourishing community of 31,000 people. Over time, inactive centralized moderators ignored calls for the transfer of ownership or increased management. Now, the subreddit swings between inactivity and chaos, leaving students without a voice in their own community. HomepageDao offers a way for people to join together in a fun and accessible way, without the risks of centralized management. What it does HomepageDAO is a community governed, editable homepage. Through ownership of a DaoBao token, members can propose and vote on everything from displayed content to background color– without the need of a moderator or admin. In order to join the community, you stake an amount of wMATIC to receive a DaoBao token. Once you’ve become a stakeholder, you can submit proposals for modules and setting changes. If a proposal passes the editable quorum requirement through a majority vote, congratulations! Your change will be displayed on the website, without the need for admin approval. Finally, we wanted to really lean into the fun– so every time you vote on a proposal, you’re entered into a lottery for DaoBao prizes. Using Chainlink VRF, a winner is chosen and their prizes could include special community NFTs, DaoBao tokens, or even native MATIC. How we built it We built HomepageDao by producing two smart contracts on the Polygon network. The DAO logic is controlled by Main.Sol, and Token.Sol which controls the ERC-20 challenges. The frontend is fully developed in Flutter/Dart. The technologies used include Alchemy for less latency, Polygon for cheaper transactions fees, NFTPort for appreciating lottery winners with NFTs, Chainlink to choose DAO winners randomly verified, and IPFS/Moralis to upload all the data. Challenges we ran into The largest challenge was finding an architecture that allowed us to not repeat voting functions for each type of proposal. Having large arrays made the smart contract far too storage-intensive. To get around this, we created an array of struct of the string ids for each proposal. Each string ID mapped to a struct of Type proposal that held identifying information for the proposal. We solved the repeating function issue by including an “indicator”, which acted as an enum with all possible states for proposal types. The indicator differentiated different types of proposals through one attribute of data stored in its stuct, rather than an actual function call. This solution allowed us to change settings and pass the threshold or quorum indicator without needing massive amounts of storage. Accomplishments that we're proud of Being able to use Chainlink VRF alone is a huge accomplishment. However, we’re extremely proud of figuring out how to use the VRF to incentivize voting within a DAO. The applications of this are endless. What we learned We learned so much about smart contract architecture and using Chainlink VRF. The problem-solving behind smart contract architecture was also an amazing learning experience. In addition, we learned how to work as a team and incorporate many aspects of the blockchain into our project. What's next for HomepageDAO Our mission is to make DAO’s community-oriented and fun. We believe in the power of a community, led by members that can point directly to where their voice mattered. Each button, each post, every color selected by a democratic system. As we continue to build and grow the DaoBao community, we hope to offer a space that truly represents the people within it– however that may look. <div