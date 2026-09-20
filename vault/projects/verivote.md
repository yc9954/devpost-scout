---
slug: "verivote"
url: "https://devpost.com/software/verivote"
title: "VeriVote"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 559
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "user/researcher"
  - "substrate/structured_db"
---

# VeriVote

> Turn every laptop or handheld device into a ballot machine with Verivote. The world’s first face recognition app for securing elections.

[Devpost](https://devpost.com/software/verivote) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]]
**user** [[researcher]]
**substrate** [[structured_db]]

**stack** dash, flask, opencv, python, quickbase, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for verivote

## Body

Verivote Making Elections Safer Value Proposition How Verivote Works Inspiration I am from a country of 200 million people. A country where corruption is a value and suffering a virtue. Election rigging through ballot box stealing, stuffing and thuggery are the order of the day. As a result of that, a country of 200 milion has been held captive by an insidious, unlawful group of about 1000 persons who currently inhabit the top seats in state agencies such as the executive, judiciary and legislative branches of our government. The people try as they may, cannot rise up and vote these people out due to the tactics they employ which i mentioned above. This idea was born from pain, shame and fear. On the 20th October 2020, the Nigerian state authorized its military and police personnel to shoot at unarmed protesters at the Lekki Toll Gate. You may not have heard of this but i am sure you have seen the #EndSars protest. That is what this was borne from, a deep frustration with the democrative electoral process and how it drives the disenfranchisement of people across the globe. What it does Verivote is a convolutional neural network built upon the dash/flask framework which when trained on a group of different faces, is able to detect and recognize an individuals face, pull up their bio-information, figure out which states they are eligible to vote in and feed them the relevant choices all from the quickbase api so they are verified and can vote only for candidates in states they are eligible to vote in. How I built it Verivote is built upon python, flask, dash and keras using imagenet weights, adam as my momentum optimizer. It has 9 classes in its output layer. Challenges I ran into I am barely 7 months in to machine learning so this was a very ambitious project for a self-taught data scientist in training like myself. Especially, considering i have only been signed on for this hackathon project for 2 weeks(seriously). I ran into issues tuning the model to fit the faces due to not having a massive dataset of pictures and people around me to give me pictures, i had to settle with an average of about 150 pictures per class on average, which is extremely small. Accomplishments that I'm proud of Seeing this project come to life like it has. I honestly didn't know what to expect considering the short turnaround, but I hope you guys like it. My goal here is not to build a perfect product, but to kickstart the conversation around computer vision, face recognition technology and its potential for securing elections and turning every handheld device intoa ballot machine. What I learned This is only the second neural net i can say i have actively setup and utilized. While i know this is basically just transfer learning and i am really not doing much, i can't help but feel some sense of ownership and excitement about the future of the electoral process. Elections are integral to societal stability and development, i hope i can play my part in entrenching, free and fair elections and disrupting corruption. What's next for VeriVote Petitioning the Nigerian Independent Electoral commission to transfer their voter information database to quickbase and employ computer vision, this amazing technology to secure the future of Nigerians. <div