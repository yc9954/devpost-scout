---
slug: "unremarkable-project"
url: "https://devpost.com/software/unremarkable-project"
title: "Unremarkable project IXO wallet"
hackathon: "Cosmos HackAtom VI "
organization: "Cosmos"
winner: true
words: 439
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Unremarkable project IXO wallet

> Unremarkable project is building a web3-native operating system and hardware for the future of personal computing. We integrated the IXO wallet into the tablet. 1-2 weeks battery life, visible in sun.

[Devpost](https://devpost.com/software/unremarkable-project) · hackathon [[Cosmos HackAtom VI]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[education]] [[finance_payments]]
**substrate** [[financial_record]] [[video_visual]]

**stack** dart, flutter, javascript, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for unremarkable project

## Body

Inspiration We want to take the power back from Web2 monopolies and hand it back to users by empowering them with sovereign tools. To achieve this, we've built a Web3-native operating system and we're designing hardware to deeply integrate with the software to provide the first true alternative to the Apple/Google duopoly. We wanted to integrated the ixo project to enable to our users to participate in the Internet of Impact. What it does See for yourself in the photos/videos :) But in summary, the device itself is a kindle-ipad hybrid. Think of an ipad with a kindle screen that refreshes at the same speed as an ipad screen. Think of an ipad with the long battery life of a kindle. Think of an ipad with an open operating system that integrates Web3 primitives and enables self-sovereignty and exit from the centralized internet. Crucially the novel screen technology allows use in the field - visible in direct sunlight & 1-2 week battery life even in the bright sun. The combination of long battery life, offline first architecture, durability to drops, and visibility in direct sunlight makes it hardware suited for outdoor classrooms and the developing world. How we built it We forked the ixo Keysafe extension and made it compatible with our device/OS. Challenges we ran into The desktop "pop-up" nature of the Keysafe extension presented a challenge. We also had rendering issues that made it challenging to use & work on mobile. Accomplishments that we're proud of Keysafe installed, wallet created, running, and signing transactions on the app-uat.ixo.world on a mobile device. Mobile wallet extension integrations are rare, novel, and mostly lacking: .. we feel proud to bring the ability of extensible wallets to mobile devices! Crypto has mostly been stuck to the desktop. What we learned We learnt about integrating Cosmos-based wallets into our OS, and translating desktop technologies to mobile, and figuring out the primitives and flows of the IXO SDK & webapps. What's next for Unremarkable project This is just a proof of concept and we have many ideas on how to evolve from here. We will iterate on this integration, polish off the UI/UX, make changes to our fork to optimize the rendering size, and eventually include the IXO Keysafe wallet as one of the default wallets on our device. Deeper integrations can include smoother UX for micropayments, DID authentication & signing, claims etc. User Story: Rahul in Kashmir, India is 6 years old and is learning to read using digital books on the Unremarkable tablet while in his outdoor classroom, and uses the inbuilt IXO wallet with his DID to sign claims. <div