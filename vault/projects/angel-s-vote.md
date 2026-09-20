---
slug: "angel-s-vote"
url: "https://devpost.com/software/angel-s-vote"
title: "AngelVote"
hackathon: "AngelHacks 2.0"
winner: true
words: 424
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/privacy_tech"
  - "mechanism/provenance_signing"
  - "domain/civic_government"
  - "substrate/structured_db"
---

# AngelVote

> Voter convenience, voter fairness, voter confidence and voter turnout. We will help you secure your vote online with a variety of authentication methods to ensure fair, balanced and secure elections.

[Devpost](https://devpost.com/software/angel-s-vote) · hackathon [[AngelHacks 2.0]]

## Facets

**mechanism** [[privacy_tech]] [[provenance_signing]]
**domain** [[civic_government]]
**substrate** [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** blockchain, cloud-functions, css3, figma, firebase, firestore, gcp, html, javascript, mongodb, nextjs, react, twilio

## How they structured the write-up

- inspiration
- what it does
- key features
- how we built it
- challenges we ran into
- what we learned
- accomplishments that we're proud of
- what's next for angel's vote

## Body

Inspiration We were deeply inspired by the recent events of the US election. With such sophisticated a new technologies of the 21st century we thought elections could be done better in a way no one could dispute. As electronic voting schemes are becoming popular in the last decade, and they are still unsolved. E-voting schemes bring problems mainly regarding security, credibility, transparency, reliability, and functionality. What it does As an effort to bring transparency, fairness, and truth to elections, we decided to build AngelVote, a platform to facilitate decentralized voting. Transparency of the whole process and the voters’ security and privacy thanks to homomorphic encryption. It is fully utilized by blockchain and all processes can be handled within it. After the start of the voting, the platform behaves as fully independent and decentralized without possibilities to affect the voting process. The data are fully transparent, but the identity of voters is secured. Key Features Elections Election operators dashboard to create Simple, Multichoice and Ranked voting elections Specify if voting is open to public or limited QR Code Voting Invites to vote BlockChain Secured Voting Voting OAuth Authenticated Voter Registry Facial Capture and Recognition Signatures Capture and Recognition Mobile OTP verification Vote Casting Page that adds your vote to the block chain Block chain visual of where your vote is in the block chain Viewing Block chain visual of the entire block chain for each election Live view of election results Count down of the current election time remaining How we built it NextJS like crazy and React. Using the NextJS serverless functions hosted on Vercel connected to serverless functions on Google Cloud to do blockchain ops and connect to Mongo. Firestore, firebase storage for local caching and firebase auth. Challenges we ran into Prettier whitespace change merge conflicts CORS on Google Cloud Functions SSG tries to parse all paths but we have a backend that's too complicated and inconsistent data What we learned We were inspired by the NextJS workshop and really used all of the deeper functionality that we had never tried out before like SSR and SSG We also applied a whole lot of tailwind we learned at a workshop Both the Computational modeling workshop and machine learning workshop helped us create our backend with blockchain and facial/signature recognition models Accomplishments that we're proud of Biggest app we've ever made What's next for Angel's Vote Fix up all our missing UI We could allow CSV to upload to support larger voter lists Voter registration page vs auto registration on first vote <div