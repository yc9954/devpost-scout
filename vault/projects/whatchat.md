---
slug: "whatchat"
url: "https://devpost.com/software/whatchat"
title: "WhatChat"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 270
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/voice_speech"
  - "substrate/transcript_audio"
---

# WhatChat

> Conversational analysis for Whatsapp chats.

[Devpost](https://devpost.com/software/whatchat) · hackathon [[Cloud Native Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[voice_speech]]
**substrate** [[transcript_audio]]

**stack** alan, bulma, django, python, symblai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for whatchat

## Body

Inspiration A lot of businesses in Africa have begun to use chat apps, such as Whatsapp, to talk to customers. This leads to tons of chats and sometimes the ball being dropped as somebody misses something in a chat. What it does This application allows users to upload text transcripts from WhatsApp and run conversational analysis on them. It picks up important information that may be needed by a business, such as follow ups, action items, topics and questions. How we built it I built this application using Django and python with Bulma for the frontend styling. I integrated it with Symbl.ai for the conversational analysis and Alan for voice commands. Challenges we ran into The biggest challenge I had was time I have not completed the application. The following are a few challenges I currently have: The styling is not complete throughout the whole site. I found out that the response objects from the symbl ai conversation aren't JSON serialisable Saving all conversation information in Django is not complete Alan integration has not been completed yet I have not deployed it. Accomplishments that we're proud of I'm proud of getting the application running. I'm proud of getting social login working and Symbl integration done. What we learned I learned how to do social logins for GitHub in Django. I learned how to add symbl ai to a Django project. What's next for WhatChat I would like to complete the following features: Upload multiple WhatsApp chats Add telegram chats Complete dashboard styling as well as login page Add Facebook, Twitter and gmail social logins Add more Alan voice commands <div