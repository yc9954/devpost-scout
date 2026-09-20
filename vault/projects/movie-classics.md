---
slug: "movie-classics"
url: "https://devpost.com/software/movie-classics"
title: "Movie Classics"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 412
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "user/general_public"
  - "substrate/document_pdf"
---

# Movie Classics

> Watch the best movies in the public domain

[Devpost](https://devpost.com/software/movie-classics) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**domain** [[civic_government]]
**user** [[general_public]]
**substrate** [[document_pdf]]

**stack** apl, lambda, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for movie classics

## Body

Plays on Echo Show Plays on Echo Spot Plays on Echo Dot Plays on Echo Fire Stick and Fire Cube Inspiration For movies to be in the public domain means that no government, company, organization or individual owns them. They are considered part of the public cultural heritage and may be freely watched and used by all. The main disadvantage of that is no one cares to market or distribute them since there is no monetary return. We believe that the free flow of creative work is of vital importance to transfer knowledge, educate and culture our young one and society. That's why we build Movie Classics. What it does Movie Classics is an Alexa skill that allows you to watch some of the best classical movies in the public domain on your Video-Enabled echo device. The skill will play a movie in random when you utter: "Alexa, ask Movie Classics to play something". If your echo device doesn't support video, no worries, The skill is smart enough to play a classical radio show from the "Golden Age" of American Radio. How I built it Once a decision has been made regarding what the skill will do and what it won't do, building and testing were easier. I always start with a list of the must-have features to produce an MVP (Minimal Viable Product). The first version was built, submitted to certification and passed. What really made me very excited is the number of unique users and skill activations (67 in a couple of days) without advertising it anywhere. The skill utilizes a Video Player, an Audio Player, and APL documents. Some of the media is hosted in S3 while some are loading directly from public repositories on the internet. Challenges I ran into There are not enough examples of APL and Audio Player skills. Error messages are not descriptive enough, which made the troubleshooting harder. Accomplishments that I'm proud of Making creative work in the public domain available to a new market. Publishing a first-of-a-kind skill. Learning APL. What I learned There are a lot of great movies in the public domain (check out 12 Angry Men and D.O.A.) APL There's a lot more to learn about Audio Players (that's my next project) What's next for Movie Classics Depending on the feedback I get from customers, I might add a list view where users can select what they want to watch. Add new media files. Automate the media upload process. <div