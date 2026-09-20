---
slug: "callcenter-for-hipchat"
url: "https://devpost.com/software/callcenter-for-hipchat"
title: "CallCenter for HipChat"
hackathon: "Atlassian Codegeist: Add-on Hackathon"
organization: "Atlassian"
winner: true
words: 239
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "user/small_business"
---

# CallCenter for HipChat

> With full phone and voice-mail support directly in HipChat, your team will never miss an important customer call.

[Devpost](https://devpost.com/software/callcenter-for-hipchat) · hackathon [[Atlassian Codegeist- Add-on Hackathon]]

## Facets

**user** [[small_business]]

**stack** hipchat, javascript, memcached, nginx, node.js, twilio

## How they structured the write-up

- inspiration
- what it does
- how i built it
- accomplishments that i'm proud of
- what i learned

## Body

Inspiration As a small business, having a standing business phone number can be costly as well as a hassle to maintain. Especially since giving out your direct phone number isn't exactly what you might want to do. We set out to solve this with CallCenter for HipChat What it does CallCenter for HipChat integrates with Twilio and allows a HipChat room owner to assign one (or multiple) phone numbers to a room. When a call comes in, it can be answered from directly inside the room or be go to voicemail. A discussion can then be had in the room and everyone can collaborate about it. How I built it This was build using the new awesome HipChat Connect framework that allows more integration with the HipChat client as well as the Twilio rest api. Accomplishments that I'm proud of One of the bigger challenges that was run into was how to handle the "live" updating of the sidebar when it's displayed for a large audience while not causing a DoS attack on the service itself. We ended up creating a very protective caching layer within nginx that we're able to adjust as necessary. By doing this calls can appear in the sidebar "as live" items. What I learned A lot. HipChat Connect opens a lot of interesting opportunities and the biggest challenge is to figure out how to best make use of the tooling provided by it. <div