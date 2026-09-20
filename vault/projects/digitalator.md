---
slug: "digitalator"
url: "https://devpost.com/software/digitalator"
title: "QuickBase Digitalator"
hackathon: "Quick Base Virtual Hackathon"
organization: "Quickbase"
winner: true
words: 282
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# QuickBase Digitalator

> As the use of hand-filled forms for COVID consents and contact tracing, Digitalator inserts the data from those hand-filed forms into Quickbase data, by leveraging machine learning and computer vision

[Devpost](https://devpost.com/software/digitalator) · hackathon [[Quick Base Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[video_visual]]

**stack** api, computer-vision, javascript, machine-learning, netlify, quickbase, rest

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- what i learned
- what's next for digitalator

## Body

Inspiration Quickbase no code database, is amazing in collecting and sorting data. but as we've seen with covid and the increasing need for collecting consents and information for contact tracing, there's still huge data collected out there in the form of handwritten forms. To be able to search and analyze the data in the forms we need to digitize them in a timely and cost effective manner. What it does Digitalator was created to digitize hand written forms using machine learning and computer vision, and the robust Quickbase API. We feel that this combination of Machine Learning and no code database like Quickbase will save many organizations a lot of time and money during crisis time and during normal times. How I built it Using QuickBase REST API in addition to computer vision Challenges I ran into Limitation related to the size of image uploaded What I learned As with any technology there are limits to the accuracy and size of image files it can analyze. What's next for Digitalator We plan for the Digitalator to become an extension that the users can add to their Quickbase apps and pipelines, this is why in the design we tried to avoid hard coding values, we read the field title from the form directly and map it as the key in real time. and then map the hand written part as the value. For the extension we plan to have the user map the values which are returned from reading the document to the correct table and fields once for each type of form the user plan to scan. As we continue to work on those we hope that you enjoy the Digitalator. <div