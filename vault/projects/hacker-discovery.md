---
slug: "hacker-discovery"
url: "https://devpost.com/software/hacker-discovery"
title: "Hacker Discovery"
hackathon: "Hack Devpost - The hackathon"
organization: "Devpost, Inc."
winner: true
words: 402
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "domain/legal_justice"
  - "user/developer"
---

# Hacker Discovery

> Hackathons are about, among other things, growing your network! By leveraging Devpost's social logins, Hacker Discovery offers a simple way to find friends, coworkers and colleagues from other sites

[Devpost](https://devpost.com/software/hacker-discovery) · hackathon [[Hack Devpost - The hackathon]]

## Facets

**domain** [[legal_justice]]
**user** [[developer]]
  <sub>weak: video_visual, web_dom</sub>

**stack** css3, html5, miro

## How they structured the write-up

- inspiration
- what it does
- how can it be built
- what's next for hacker discovery

## Body

Hacker Discovery image inside Devpost website. Includes first and second degree contacts Updated profile with "Manage social networks" option and already configured networks. Hacker Discovery thumbnail Inspiration I'm an introvert And while some hackathons provide a space to meet people, it would be much easier if I could easily find hackers I already know! It's usually hard to approach people about hackathons in friends circles, university, or work. But what if someone else in my circle is in the same position as me? We need to know. What it does "Hacker Discovery" aims to help address one of Devpost's pillars: "Grow your network" . By leveraging the existing APIs in all the social login platforms supported, we can easily cross-reference users already registered in Devpost, or even invite them! Once connected, all the tools are already in place for following each other, sharing past projects, and building new teams for upcoming hackathons. How can it be built The best part of this idea is that all the required dependencies are already available. Data ingestion Apart from just email, currently, Devpost supports social login with Github, Facebook, Google, and LinkedIn. All these sites provide APIs to retrieve information related to the user's network: Github API : List followers of the authenticated user Facebook Graph API : Retrieve user friends Google People API : Read contacts LinkedIn - Microsoft Contacts API : Retrieve address book While only one of the sites can be chosen a login method, allowing the user to set up other social sites will improve Hacker Discovery searches and suggestions. Graph representation Here is a fun opportunity for Devpost engineers to model a rich graph. Each user needs to be linked with its identities across the registered profiles. Search and discovery Once the graph is built, Devpost should be able to easily suggest other registered hackers that are part of your circles (such as Facebook friends or LinkedIn contacts). There are multiple product decisions to be made at this point, but one of the main ones is asking users if they effectively want to be discovered : let's keep in mind that the key purpose of social login is to, well, log in. Being searched should be, in my opinion, an opt-in feature. What's next for Hacker Discovery Let's build this thing. Integrations are fun! Oh, there might also be some legal details I'm intentionally leaving outside of the slicing. <div