---
slug: "coffee-club"
url: "https://devpost.com/software/coffee-club"
title: "Coffee Club"
hackathon: "Alexa Skills Challenge: Alexa Conversations"
organization: "Amazon"
winner: true
words: 480
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "substrate/video_visual"
---

# Coffee Club

> Coffee Club is a productivity skill that manages a "coffee club" for friends and co-workers, taking the guesswork out of ordering the right coffee for everyone.

[Devpost](https://devpost.com/software/coffee-club) · hackathon [[Alexa Skills Challenge- Alexa Conversations]]

## Facets

**domain** [[labor_employment]]
**substrate** [[video_visual]]

**stack** alexa, amazon-web-services, javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for coffee club

## Body

Video title page Inspiration I chose a coffee club for the Amazon Alexa Conversations Challenge because it requires something to be configured, and that's a perfect fit for Alexa Conversations. In this case, customers use a conversation to configure both the club initially, then another conversation to configure each individual coffee order. What it does The skill uses Alexa Conversations to gather information about people's coffee preferences, and stored them for later use. You only need to add a member once, and you can delete them at any time. Later, you can start a "coffee run". In the real world, this is where you say "who'd like a coffee?". Different people will say Yes on different days, so the actual coffee order is different each time. The skill lets you specify a list of up to five club members who can be included. (If you need more you can always create a second coffee run!) From the names you specify, the skill looks them up in persistent storage (the club), and adds details for each person to your coffee run (the order). It posts the resulting order to a skill card in your mobile app so that you can take it with you, or screenshot it and send it to someone else. How I built it I built the skill as an Alexa-hosted Skill in Node.js. This was my first Alexa-hosted skill so I had to learn about that as well as the new (beta) Alexa Conversations. Challenges I ran into Alexa Conversations is brand new, and in beta. So I struggled with the all-new UI at times, and the fact that it's a black box service, so it's not always clear what's gone wrong. In most cases I was able to work through this using the Alexa team's examples, but in some cases I had to start fresh. In fact Coffee Club was my backup idea - my original plan was a far more ambitious skill using several external APIs, but the complexity of my dialogs proved too much for me, or Alexa Conversations in its beta state, or both. Accomplishments that I'm proud of Turning round this Alexa Conversations skill in just a few days after spending two weeks struggling with a far more complex one (which I still plan to publish after the challenge). What I learned Ask for help - the Alexa team is very responsive, but so are all the other participants. I help as much as possible, and appreciate the leg up when others help me! What's next for Coffee Club I plan to add more options for drinks - I've really only scratched the surface. So additions like you'd find in a coffee shop would be on the list. But for Alexa Conversations I will add lost more things you can say to the skill to make for a more natural conversation. <div