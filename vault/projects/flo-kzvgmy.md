---
slug: "flo-kzvgmy"
url: "https://devpost.com/software/flo-kzvgmy"
title: "Flo"
hackathon: "Facebook Hackathon: AI"
organization: "Facebook"
winner: true
words: 438
team_size: 4
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "user/general_public"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# Flo

> Automate meeting notes and summarization with the help of our AI assistant, Julia

[Devpost](https://devpost.com/software/flo-kzvgmy) · hackathon [[Facebook Hackathon- AI]]

## Facets

**mechanism** [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**user** [[general_public]]
**substrate** [[structured_db]] [[transcript_audio]]

**stack** flask, postgresql, python, react, socket.io, sqlalchemy, wit.ai

## How they structured the write-up

- wit.ai app id
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flo

## Body

Login page Dashboard on going meeting End of meeting summary download Calendar Contacts page Profile page Wit.ai App ID 938304383356549 Inspiration Our inspiration came from trying different video conferencing applications ever since most of the world went remote due to Covid-19 and experiencing the different features each one has to offer and what we could add to make meetings easier, in our case eliminating secretaries while also accommodating people with different schedules. We discovered that instead of having someone watch a whole meeting recording, they could choose to read everything or just get an idea of what they missed out or if someone is busy with other activities, they can just use voice commands and run meetings. What it does Our application allows users to use voice commands by leveraging wit.ai speech feature, they can create group and individual video meetings either instantly or by scheduling it. At the end of a meeting, our application generates a meeting transcript as well as a summary of the whole meeting. How we built it We built the application using python flask for the back-end and react for the front-end and postgresql for the database. Our design was based on using WebRTC to implement multiple peer connection calls. We also wanted to make our application interactive and more user friendly by making our application accessible using natural speech voice commands and for this we used Wit.ai by Facebook. Challenges we ran into Learning wit.ai for the first time was a bit of a challenge for all of us and trying to figure out the best way to implement it in a product that is relevant for us and is also bound to be widely accepted by the public. Another challenge was having to implement certain features that were not readily supported by Wit.ai but we did come up with methods to resolve the issues. Accomplishments that we're proud of We are proud of the short space of time, two weeks, that we were able to work on our project from brainstorming ideas, coming up with one that has potential to be expanded further and building the application while working remotely. What we learned We learned the basics of using Wit.ai for voice recognition, transcribing speech and running intents What's next for Flo Our goal is to further train our application to be more effective when running voice commands as well as listening to conversations during the meeting so that we can produce accurate transcripts and summaries. We also plan on adding the annotations in multiple languages during a meeting so that our application can fully accommodate and connect different users. <div