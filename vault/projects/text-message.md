---
slug: "text-message"
url: "https://devpost.com/software/text-message"
title: "Text Message"
hackathon: "Cloud Native Hackathon"
organization: "WeMakeDevs"
winner: true
words: 148
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
---

# Text Message

> Converts WhatsApp voice messages into text messages using symbl.ai audio api.

[Devpost](https://devpost.com/software/text-message) · hackathon [[Cloud Native Hackathon]]

## Facets


**stack** flask, symbl.ai, twilio

## How they structured the write-up

- what it does
- how we built it

## Body

What it does Imagine you are in a situation where you can't listen to the voice message in WhatsApp for a couple of reasons like just you don't have any access to earphones to listen in public areas or just you don't have time to sit through a 4 min voice message. At that time Text message will solve this problem by converting voice messages into text messages using Symbl.ai Audio API . The user has to forward the voice message to symbl.ai bot and that voice message is sent to backend server through WhatsApp business API and then it is sent to symbl.ai audio API. Finally, the generated text is sent to that phone as a text message. How we built it we build our solution using the following technologies: 1) Flask for backend server. 2) Twilio for WhatsApp Business API. 3) Symbl.ai for Audio API <div