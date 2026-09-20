---
slug: "out-the-door-ux0wig"
url: "https://devpost.com/software/out-the-door-ux0wig"
title: "Out The Door"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 408
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
---

# Out The Door

> No more hectic mornings! Alexa helps your little ones have fun while completing their morning routine.

[Devpost](https://devpost.com/software/out-the-door-ux0wig) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]

**stack** amazon-web-services, lambda, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for out the door

## Body

Inspiration Mornings with kids can get hectic when you have to be somewhere on time. When Alexa joined our family we realized the kids love interacting with her, and we were curious to see if she has more authority over them than their parents. She does. What it does Out the Door helps kids complete their morning tasks in a fun and engaging way. It helps parents focus on what’s really important in the morning and and saving their energy for hugs and fun instead of having to repeatedly nudge their kids to brush their teeth. How we built it Interaction Model - Using Alexa developer IM builder, The services are implemented using node.js AWS Lambda function, alexa-sdk library Challenges we ran into This was our first Alexa skill so we ran into a few challenges. Conversation design We ran into some problems with the ui. Alexa didn’t always understand what the kids were saying, so we had to select easily pronounceable words for them (we replaced “ready” with “go” for example). Another problem was that we couldn’t just have the kids tell Alexa when they are done with each mission because the skill quits after 16 seconds, so we built a workaround with music playing in the background and Alexa asking them every 30 seconds or so if they are done. Also, we wanted to keep the skill simple, but to engage kids. We used speechcons, sound effects, and a basic story line where every day there’s a different creature you have to beat. And of course we used superpowers because everyone loves them. tech challenges handling states and sessions, cards - delay display of card parts, learn the new API and concept, testing the skill with voice. Accomplishments that we're proud of We got happy kids out the door in ten minutes and made it to work on time! What we learned On the technical part, we learned the API mainly with official skill tutorials. The test simulator was particularly helpful What's next for Out The Door Since every family has different routines, our next step is to add a feature that lets parents control their missions and the desired time for each mission. We also want to add new story lines to keep the skill interesting over time. Additionally, this skill was designed to motivate one child. We would love to craft this as a a fun morning challenge for siblings and parents too! <div