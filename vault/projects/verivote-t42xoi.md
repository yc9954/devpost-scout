---
slug: "verivote-t42xoi"
url: "https://devpost.com/software/verivote-t42xoi"
title: "VeriVote"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 379
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
---

# VeriVote

> Empowering democracy through QED Zero-Knowledge Proofs in order to improve, secure, and bring transparency one vote at a time!

[Devpost](https://devpost.com/software/verivote-t42xoi) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[structural_withholding]] [[vision_ocr]]
**domain** [[civic_government]]

**stack** json, python, rust

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for verivote

## Body

Inspiration Voting systems fail to adopt new technology and address systematic concerns. Blockchain, having the ability to create transparency and decentralize centralized powers, seemed like a plausible solution to this issue. Seeing the QED workshop and its utilization of ZKPs, we knew that would be a great opportunity to create a scalable, decentralized, and extremely secure voting platform. What it does This platform uses the QED protocol as a backend to verify state changes to proposals that are part of VeriVote using ZKPs. This means that users in the network are empowered with the ability to vote on policies and verify the legitimacy of the election/system. How we built it We used the QED Protocol coded in Rust to create a series of functions that allow users to vote and propose on different policies posed on our platform. We specifically created functions on the server side that helped list proposals, vote on them, and finalize them. To help run our application, we created a Python client and found ways to execute API calls from our server. Challenges we ran into Our team did not have as much exposure to ZKPs which resulted in us spending the majority of the hackathon learning and building levels of abstraction for the protocol. This was a significant challenge but through cross-collaboration and help from online resources, we were able to learn and create a product we're proud of! Accomplishments that we're proud of We're proud of creating a back-end that uses QED and works with Rust to create ZKPs with the potential for real application. Our team adapted to using a new language and learned more about a field that is constantly developing. What we learned Our team learned more about zero-knowledge proofs, contemporary solutions that are being implemented to address the Blockchain trilemma, and how to code a robust back-end in Rust. We plan on learning and diving more into open-source projects related to ZKPs and decentralized applications. What's next for VeriVote Our next steps include: Adding a delegation feature that allows people to delegate their votes to certain proposals/users in the network Implement a front end to make the application more functional/accessible (i.e. votes sidebar) Create a means of robust authentication to ensure that people on the network are unique. <div