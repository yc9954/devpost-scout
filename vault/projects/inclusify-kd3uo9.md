---
slug: "inclusify-kd3uo9"
url: "https://devpost.com/software/inclusify-kd3uo9"
title: "Inclusify"
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 328
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/accessibility"
  - "substrate/video_visual"
---

# Inclusify

> A Hack The North project which attempts to bring inclusiveness to the ever growing world of communication.

[Devpost](https://devpost.com/software/inclusify-kd3uo9) · hackathon [[Hack the North 2021]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[accessibility]]
**substrate** [[video_visual]]

**stack** azure, computer-vision, css, express.js, figma, gcp, google-cloud, hootsuite-api, html5, javascript, languagetool, node.js, oauth, postman

## How they structured the write-up

- inspiration
- what it does
- challenges we ran into
- accomplishments that we're proud of
- what's next for inclusify

## Body

Inclusify: Increasing social media inclusivity, one post at a time Login Page Upload your picture and caption Review of how to make your post more inclusive Post the final reviewed post to Twitter, Instagram, and Facebook Image and caption posted to Twitter by Hootsuite! Inspiration Online communication is growing very rapidly, with some countries quintupling users every 5 years. With such a large online base, it is imperative to ensure a comfortable and inclusive environment for different cultures, and people with accessibility needs. Unfortunately, social media inclusivity is not growing nearly as rapidly as online communication. This causes a few groups to not be as connected with the trends and happenings of today's social media. What it does Inclusify hopes to improve communication for users of different cultures, users with accessibility needs in today's connected world. It does so by accepting a user photo and caption. It then uses Azure ComputerVision API to give an image description, removes emojis if there are more than one, lowercases uppercase words, and uses LanguageTool API to camelcase hashtags with multiple words. It then returns this suggested caption back to the user, who can then post the image and caption to Twitter, Instagram, and Facebook using the HootSuite API. Challenges we ran into Authentication with OAuth 2.0 using GET REST API was something completely new to us. Despite facing many challenges with OAuth, we were able to finally figure it out. Accomplishments that we're proud of User authentication with OAuth was a challenging but rewarding task. Most of us were relatively new to JavaScript, particularly async functions. After several attempts, we all got the hang of it. Making a good looking frontend was also a proud moment! What's next for Inclusify We are planning to include features like video captioning for supporting inclusive video, flagging captions which may be offensive to a group, and automated suggestions for when to post. Furthermore, we are also planning to make the app more robust. <div