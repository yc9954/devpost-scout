---
slug: "pic-motion"
url: "https://devpost.com/software/pic-motion"
title: "pic motion"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 141
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/video_visual"
---

# pic motion

> Create deep fakes with a photo and a reference video. Based on first-order-model by AliaksandrSiarohin.

[Devpost](https://devpost.com/software/pic-motion) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[video_visual]]

**stack** docker, flask, gcp, postman, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for pic motion

## Body

Inspiration I wanted to create something fun with AI so I decided on a a deep fake API. Also saw some stuff on twitter where Justin pinkney's toonify was combined with first order motion, so it was more reason to make it accessible What it does Animate selfie photos by mirroring a 15secs short video like. tiktok videos and the likes How we built it Created Flask endpoint based on pytorch model of [first-order-motion-model]( https://github.com/AliaksandrSiarohin/first-order-models . Deployed docker container of endpoint to Google Compute engine Challenges we ran into Figuring flask and container deployments. CORS restrictions. Cloud and desktop agents in postman. Accomplishments that we're proud of It works What we learned Postman workspace. Collections. CORS and patience What's next for pic motion Support for. longer videos. Support for links apart from. local files for the image and video reference. <div