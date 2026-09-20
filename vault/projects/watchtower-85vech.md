---
slug: "watchtower-85vech"
url: "https://devpost.com/software/watchtower-85vech"
title: "WatchTower"
hackathon: "Chirp Developer Challenge"
organization: "Twitter"
winner: true
words: 598
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/media_journalism"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "user/developer"
  - "user/general_public"
  - "user/researcher"
  - "substrate/structured_db"
---

# WatchTower

> Block violent, extremist, and hate speech tweets from your Twitter feed.

[Devpost](https://devpost.com/software/watchtower-85vech) · hackathon [[Chirp Developer Challenge]]

## Facets

**domain** [[media_journalism]] [[mental_health]] [[security_privacy]]
**user** [[developer]] [[general_public]] [[researcher]]
**substrate** [[structured_db]]

**stack** gradio, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for watchtower

## Body

WatchTower Splash Screen Logo WatchTower FavIcon and Small Logo WatchTower Introduction Tab WatchTower Getting Started Tab Inspiration The inspiration for watchtower came two fold; first from my PhD research into identifying and predicting ideologically motivated cyber crime and secondly from my intertest in building tools to support users. WatchTower builds off these areas by providing a platform for Twitter users to perform mass-blocking of violent extremist users. What it does WatchTower is backed by a machine learning model (with additional models in the works). Each machine learning model has been trained off a dataset of users that fall into one of many unfavorable activities (i.e. hate speech, violent extremism, misinformation, etc). The current model that backs Watchtower is Pinpoint, Pinpoint is a machine learning model trained of violent extremist content found on the Parler social network and is used to identify violent extremism from text posts. Using these models Twitter users can set their preferences (i.e. block violent extremist accounts with a 80% confidence or block hate speech accounts with a 50% confidence, etc) and WatchTower will block users it has identified as falling into the configured preferences. How I built it WatchTower was build by myself, James Stevenson, and builds off a machine learning model, Pinpoint , that I developed as part of my PhD research into violent extremism. Pinpoint in turn builds off the research by Nouh et.al. that uses machine learning models to identifying Islamic extremism. WatchTower in turn utilizes Pinpoint (and future, to be developed, models) by providing a simple user interface and Twitter integration that allows Twitter users to harness the capability of Pinpoint and perform mass blocking of users and posts that could impact their mental health or emotional state. Challenges I ran into WatchTower was created as a side project outside of my 9-5 and outside of my part-time PhD. That being the case, developing WatchTower was a challenge of time management as well as the obvious technical challenges. My work experience comes from software engineering and security research, however, as my first web user interface WatchTower came with several hurdles and iterations when integrating the core Python code with a web UI. As mentioned previously, WatchTower builds upon Pinpoint a random forest binary classifier machine learning model for identifying violent extremism. This model's creation did not come without it's own challenges and blockers. The primary of which was in acquiring a dataset of violent extremist messages to train the dataset off - a mix of StormFront and Parler posts were used for this in the end. Accomplishments that I'm proud of As this whole project have been solely developed by myself I'm quite proud of it in it's entirety. It's rough around the edges, but has a lot of room to grow and I can see it either becoming a stand along tool or integrating it into one of the many other tools out there designed to protect users from undesirable behavior on the platform. What I learned My background comes from working as a Java software engineer and a a vulnerability researcher working on the Android OS. Neither of these two skillsets can be applied to what WatchTower and Pinpoint have become - I've learnt so much during this process, from developing machine learning models, creating web front ends, and using the Twitter API. What's next for WatchTower WatchTower is rough around the edges and needs quite a bit of work before it's ready to be used by everyday users. I'm always up for feedback if you have any ideas for where WatchTower can be taken moving forward. <div