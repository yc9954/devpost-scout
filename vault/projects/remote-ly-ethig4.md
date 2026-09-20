---
slug: "remote-ly-ethig4"
url: "https://devpost.com/software/remote-ly-ethig4"
title: "Remote.ly"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 347
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/video_visual"
---

# Remote.ly

> More digital transformation, less Covid 19 Exposure. Organizations can leverage QB to: share requisites, forms to fill and easy video conference provisioning if in person presence was required

[Devpost](https://devpost.com/software/remote-ly-ethig4) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**substrate** [[document_pdf]] [[financial_record]] [[video_visual]]

**stack** angular.js, java, jitsi, micronaut

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for remote.ly

## Body

Inspiration Recently I've had to visit the consulate of birth country to get some documents issued. I had to fill several paper forms, close to 16 pages of information. In Covid19 times, the room seemed to be getting smaller and smaller. Kids were hungry but we couldn't leave, or risk loosing our spot. If I were given the forms beforehand, I could have filled these forms at home and reduce the time we needed to remain in the room with other persons (even with masks) Also getting information on the requisites for my transactions required a bit of back and forth. Then remove mask for photo, a small interview and we were finally out, after 137 minutes after we arrived, because we had to wait. The actual process probably took 25 minutes. So what if we could make it easy to automate this. What it does Reduces the risk of contracting Covid19 by reducing the time users and providers, need to interact with each other and other persons: Allows providers to digitalize transactions, share requisites and forms that are required to complete each. Provides easy video conferencing provisioning when 'in person' can be substituted by a video conference. All this information is provided to users to explore, download any forms they need to fill, upload them back for review. How I built it I used a QB application, to store the information necessary to organize the information related to Transactions, their requisites, the persons doing those transactions. Also used QB to send notification to users and providers when certain events happen. I am using a java microservice to allow the user facing UI to interact with QB REST APi. Challenges I ran into I am using Jitsi Meet self hosted video conference server to power that part of the solution. It was somewhat difficult to make it work inside QB (a problem with nested iframes, which prevented Jitsi from detecting camera and microphone) Accomplishments that I'm proud of Learning QB (almost not an accomplishment, because it is really intuitive). What I learned What's next for Remote.ly <div