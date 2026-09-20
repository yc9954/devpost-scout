---
slug: "adar"
url: "https://devpost.com/software/adar"
title: "ADAR"
hackathon: "Hack the North 2019"
winner: true
words: 312
team_size: 4
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/video_visual"
---

# ADAR

> Real-time personalized AR ads

[Devpost](https://devpost.com/software/adar) · hackathon [[Hack the North 2019]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[video_visual]]

**stack** facebook-login-api, ibm-watson, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for adar

## Body

Inspiration The inspiration behind this project was the growing relevance of targeted ads on social media platforms, such as Facebook. Mobile applications, such as Pokemon Go inspired the augmented reality aspect, with which we hope to increase the level of interaction with each user. What it does By utilizing the cell phone's camera, our mobile application scans it's field of view for the symbols of certain brands, such as Tim Hortons or McDonalds. Upon finding one such symbol, an augmented reality ad is triggered for the brand. It takes into account the time of the day, weather, and preferences of the user, which is pulled from Facebook. Afterwards, if the user makes a purchase, then a Facebook chatbot messages them, following up and ensuring that they enjoyed their purchase. How I built it The mobile application was built with Unity and C#. It worked with the back-end REST API, which was built in Python, using the Flask framework. In order to interact with our MongoDB instance, we used PyMongo. Lastly, in order to pull and analyze user data, we used the Facebook and IBM APIs respectively. Challenges I ran into We had a decent amount of issues with Unity, since it involved ensuring the components were dynamic. We also had trouble using the Facebook and IBM APIs. Accomplishments that I'm proud of We're proud of the fact that we were able to complete a functioning Augmented Reality mobile application over 36 hours. What I learned We learned a lot of augmented reality development in Unity. Also, we learned about the different kinds of APIs that Facebook offers. What's next for ADAR We hope to have a fully functioning operations user interface, allowing companies to use Kibana or Grifana to easily access and manipulate the data. Furthermore, we'd like to focus on creating a new library solution, rather than further utilize Unity. <div