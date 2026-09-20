---
slug: "drawit"
url: "https://devpost.com/software/drawit"
title: "Drawit"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 459
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Drawit

> Put your drawing skills to the test! An interactive Alexa Skill game for kids, family and friends!

[Devpost](https://devpost.com/software/drawit) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets

  <sub>weak: developer_tools</sub>
**substrate** [[structured_db]] [[web_dom]]

**stack** alexa-sdk, amazon-alexa, amazon-lambda, amazon-web-services, android, android-room, css3, echo-dot, html5, javascript, kotlin, lambda, node.js, postgresql

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for drawit

## Body

Inspiration We had a brainstorming and we knew we wanted to do something different – something innovative, interactive and fun. We asked ourselves if it wouldn't be great to connect voice and learn to draw. This evolved to an Alexa Skill game for kids. What it does Alexa will tell you instructions of which shapes to draw and every player has to individually draw them on a pice of paper. Whoever guesses the described object first, wins the round. The more rounds you win, the more chances you have to become the ultimate Drawit champion. How we built it We developed a custom Alexa Skill using Node.JS which is running on the Amazon Lambda web service. In addition, in order to be as flexible as possible with new objects, we're using a self-hosted web server (also based on Node.JS) to provide a backend with objects descriptions, which are stored in a Postgres database. In addition, we developed a native Android app as well as an (due to the review process, as of yet unreleased) native iOS app to optionally keep count of the players' or groups' scores. In order to keep data offline we use the Realm framework for iOS and the Room library for Android. In order to tease/market the Alexa Skill we also designed and developed a Website in plain HTML and CSS. Challenges we ran into The biggest challenge was a way to have the best possible experience when guessing the object. Having the Echo Buttons in mind all the time to buzz in, but not yet available, we hope we came up with a fair way of just letting the users decide for now, who the first one to guess right, is. The biggest challenge however, was creating the video to communicate the idea. It might sound easy to pitch your idea, it's harder to get it on tape than expected. Accomplishments that we're proud of Finishing all we planned on time and especially producing a Skill that we find really fun to play ourselves. What we learned How to create a video pitch where we've not had any experience. Visual design and development are quite easy tasks for us as we do it on a daily basis. Having to step out of the box to accomplish a proper video was fun to learn, even if we probably have more outtakes than most tv shows or movies. What's next for Drawit We hope that we get access to the Amazon Alexa Gadgets API so we can integrate the Echo Buttons. In addition, it's important to add way more objects so that it's less likely to guess the same objects over and over again. And of course we want to translate it to different languages. <div