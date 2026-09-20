---
slug: "dance-with-ar"
url: "https://devpost.com/software/dance-with-ar"
title: "Dance With AR"
hackathon: "Facebook Hackathon: AI"
organization: "Facebook"
winner: true
words: 288
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
---

# Dance With AR

> Exercise the fun way with "Dance With AR"! Choose your favorite genre and summon an AR dance teacher that will listen to your commands and teach you the dance moves.

[Devpost](https://devpost.com/software/dance-with-ar) · hackathon [[Facebook Hackathon- AI]]

## Facets

**domain** [[education]]
**user** [[educator_student]]

**stack** c#, mixamo, unity, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how i built it
- what's next for dance with ar

## Body

Choose Genre Starting Screen AR Scene Inspiration Dancing is one of the cheapest and most fun ways of exercising. I wanted to build an app that would close down the barriers that would prevent people from enjoying dancing. This app acts as a middle ground between video dance tutorials and in-person class: it provides a cheap and accessible alternative to an in-person class while also maintaining the interactivity between the teacher and the dancers. What it does Dancing with AR allows the user to select a music genre and then creates an augmented reality dance teacher that would teach the user how to follow the dance moves. The user can then interact with the dance teacher simply by talking to the app: ask the dance teacher to start dancing, slow down, stop, or turn around, and the teacher would do it for you! How I built it I used Unity for building the scenes and for putting everything together. After training and building the intents in Wit.ai, I used Wit3D to take the user voice input and to convert it into text. After fetching the Wit.ai response, I parsed it to retrieve the user intent and to play the dancer animation accordingly. What's next for Dance With AR The current version only has a basic dance move for each genre. Inside each genre, I would like to add several dances with several dance moves so that the user can learn the whole dance using the app. It would be great if I can incorporate motion capture to make trendy, up-to-date dances available. Another improvement would be to make the interaction between the user and the character more conversational by adding a speech response to the AR character. <div