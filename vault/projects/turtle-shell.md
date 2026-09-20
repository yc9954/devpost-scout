---
slug: "turtle-shell"
url: "https://devpost.com/software/turtle-shell"
title: "Turtle Shell"
hackathon: "Web5: Building the Decentralized Web"
organization: "TBD"
winner: true
words: 353
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/revocation_withdrawal"
  - "domain/developer_tools"
  - "user/developer"
---

# Turtle Shell

> A Portable Personal Data Management Tool which allows us to own, manage and view all our data regardless of its type. We call it Turtle Shell. It combines all our digital life under one Shell.

[Devpost](https://devpost.com/software/turtle-shell) · hackathon [[Web5- Building the Decentralized Web]]

## Facets

**mechanism** [[cross_origin_web]] [[revocation_withdrawal]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** dwn, express.js, extensions, node.js, plaid, sqlite, vcs, vue, web5

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for turtle shell

## Body

Inspiration Back in 2011, Columbia University Prof. Eben Moglen created the Freedom Box Server which is meant to be a highly portable server that stores one's data. This inspired a group of youngster to develop Diaspora, a Facebook-like decentralized Social Network. Years forward, TBD and DIF's spec outlined the same vision as Prof. Moglen. A user managed software that can allow us all to take control of our digital lives. What it does Allows users to manage multiple DWNs into one umbrella. Data is organized in Profiles and Partitions. Each profile with its own DWN. Identity Verification is a core feature and allows the re-usability of Identity for any type of Use Case: Health, Finance, Travel, Govt, etc.. Data is shared with 3rd parties though a browser extension that is fully permissioned by the user. At any point the user can revoke access if so they desire it. How we built it We're a team of one developer and one UX designer. We iterated and consulted with various experts to make sure our idea is sound and we are on the right track. We also took advantage that there's no existing Web-based wallet that allows of the management of one's DWN's. Challenges we ran into The biggest obstacles are mainly linked to the JavaScript ecosystem: 3rd party dependencies, Polyfill issues, CJM modules vs ESM. Also due to the nature of Web5's tech preview, things do change quite often. Accomplishments that we're proud of We're very happy with our vision and our team of mentors validated it. We want as many users to manage their own DWNs using our tool. What we learned We delved deep into the internals of Web5 and the DWN SDK JS. In addition we became more confident with UI development What's next for Turtle Shell We would love to offer this tool to TBD as their recommended Web-based wallet. We will develop an Electron version of it. We're planning for this platform to be an umbrella for all Web5 d-apps. Our intention is to leverage this tool for a particular Use Case which we cannot reveal just yet! <div