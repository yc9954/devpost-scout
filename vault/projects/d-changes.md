---
slug: "d-changes"
url: "https://devpost.com/software/d-changes"
title: "metamob"
hackathon: "Supernova "
organization: "DFINITY Foundation"
winner: true
words: 881
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/provenance_signing"
  - "domain/civic_government"
  - "domain/climate_energy"
  - "domain/education"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# metamob

> Create, donate, vote, sign and fund extraordinary mobilizations!

[Devpost](https://devpost.com/software/d-changes) · hackathon [[Supernova]]

## Facets

**mechanism** [[provenance_signing]]
  <sub>weak: cross_origin_web</sub>
**domain** [[civic_government]] [[climate_energy]] [[education]]
**substrate** [[financial_record]] [[video_visual]]

**stack** bulma, motoko, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what has been done
- what's next for metamob

## Body

Front page Campaigns page Signatures campaign Signatures list Places page (globe view) Places page (list view) Donations campaign Fundraising campaign Voting campaign My profile page My fundraisings page Admin page Inspiration Our inspiration was helping people change the world they live in. Be it a campaign targeted at tens of million users or just changing something that has to be fixed on their school, Metamob can help them accomplish their plans and dreams! What it does Metamob is a decentralized web3 app, running on the Internet Computer, that lets any user start mobilizations by creating campaigns of four different kinds: donations, votes, signatures and fundraising. Using metamob users can create campaigns to face real world problems like climate change, wars, oppression, inequality, or even to fix specific issues on his school or his condo, for example. Thanks to the Internet Computer and its 100% on-chain apps, metamob doesn’t depend on web hosts and can’t be controlled or censured by governments. In later stages, the app will be released as open-source and a DAO (Decentralized Autonomous Organization) will be created to decide how its treasury will be allocated, who should be the moderators, etc. No single individual should own the app. How we built it The backend is 100% Motoko and depends on the Internet Identity and Ledger canisters. It also support querying canisters that implement the DIP20 and DIP721 interfaces. The front-end was developed in Typescript with React 18, SASS, Bulma, YUP and the React components React Context, react-router, react-query, react-markdown, react-globe.gl, etc. Challenges we ran into To be able to do free searches and complex ordering and filtering on the data stored, I had to implement a B+tree and Suffix tree algorithms in pure Motoko. Accomplishments that we're proud of Authentication & authorization Users only have to authenticate on the Internet Identity to have full access to the app There are three user roles: administrator, moderator and ordinary user Multiple kinds of campaigns Four kind of campaigns are supported: signatures, donations, votes and fundraising Donations and fundraising will automatically transfer funds to the creator’s wallet. Vote campaigns can invoke external canister methods, allowing them to be used by DAO’s User defined places/spaces Users can create their own places to better organize campaigns Places can be restricted by email lists, DIP20 (tokens) and DIP721 (NFT) balances Rewards Users that help moderating abusive content are rewarded with the metamob token (MMT) The internal DB (called mo-table) Implemented using B+Tree and Suffix tree to allow complex queries with fast retrieving Source-code at: https://github.com/av1ctor/mo-table What we learned Motoko in general and its core libraries. How to use the Internet Identity, both on localhost and in production. How to transfer ICP's and DIP20 tokens between users. How to interact with DIP20 (tokens) and DIP721 (NFT's) interfaces. What has been done Users Users can sign in, log in, logout, edit their profiles, see the lists of campaigns, places, signatures, donations, votes and fundings they created User roles are checked on every update action on entities Update actions on places/spaces are checked when there is a restriction like email lists, DIP20 or DIP721 balances Campaigns Users can search (by partial name, by category, by place or any combination of them), sort by what is hot or by date, create, edit and delete campaigns Users can create, update and delete updates to their campaigns, closing them manually if desired Campaigns that reach goals are automatically finished and, depending on the kind, the funds are transferred to the creator or an external canister method is invoked Expired campaigns are automatically closed and the users are refunded when the goal is not reached Users can promote campaigns, boosting them with ICP's Places/spaces Users can search (by partial name, by kind or by both), sort by name or be date, create, edit and delete places Votes, signatures, donations and fundings Users can create, edit and delete their votes, signatures, donations and fundings Administration/moderation Admins and moderators can ban users, view and assign reports, edit any campaign, place, vote, signature, donation, funding and update reported by users Admins can create, edit and delete categories and places What's next for metamob DAO (Decentralized Autonomous Organization) Assign all control to a DAO that will decide how the treasury will be allocated, who will be the moderators, etc Users will have to stake the metamob token (MMT) to be able to vote All propositions will be posted on the DAO’s place created in metamob Token rewards Moderators, creators and users should be rewarded too with MMT’s depending on their participation POAP NFT (Proof of Attendance Protocol) Users that participated on a campaign should receive a POAP NFT when it finished Multiple languages The app should support multiple languages to allow users from non English-speaking countries to participate Logs Logs of any update action done by any user should be stored for at least 30 days to allow audits Image uploading Users should be able to upload images to be used as avatars and as campaign covers Places tree Places should be organized as a tree, allowing fast retrieving of all campaigns created on child places Missing pages Create the missing pages, including the Categories page and the ones displayed at the footer section Tests Create integration and unit tests Please try it out: https://wbpm2-ciaaa-aaaan-qajta-cai.ic0.app/ <div