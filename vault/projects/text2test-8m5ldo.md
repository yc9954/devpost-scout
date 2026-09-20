---
slug: "text2test-8m5ldo"
url: "https://devpost.com/software/text2test-8m5ldo"
title: "Text2Test"
hackathon: "Azure AI Hackathon"
organization: "Microsoft"
winner: true
words: 192
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/transportation"
  - "user/developer"
  - "user/frontline_worker"
---

# Text2Test

> This project aims to create test automation based on user input texts. Nowadays all test tools needs to input application specific commands.

[Devpost](https://devpost.com/software/text2test-8m5ldo) · hackathon [[Azure AI Hackathon]]

## Facets

**domain** [[transportation]]
**user** [[developer]] [[frontline_worker]]

**stack** asp.net, azure, core, luis

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for text2test

## Body

Inspiration We have a lot of test automation tool alternatives either open source or paid ones. Some of them has also test case recorder which tracks user’s interactions with application. Even if we have test recorder none of them perfect. After test recordings they needs to be validate and corrections and it is time consuming process If we get some test automation cases in advance , it would be perfect for a test engineer that no need create automation from scratch What it does It converts user typing to test automation codes by using LUIS Service. How we built it Text2Test uses Asp.Net Core for interaction and real magic goes under LUIS service. When we input as a test case like free format, it sends our human language corpus to service and returns back to intents. it parses these intents and converts to actual selenium web driver code Challenges we ran into Choosing right Machine Learning method. Accomplishments that we're proud of Interaction human language with AI What we learned Machine Learning Methods, LUIS What's next for Text2Test Adding more code language support and also add different test automation language support. <div