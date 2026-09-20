---
slug: "mediversal"
url: "https://devpost.com/software/mediversal"
title: "Mediversal"
hackathon: "Empower Hacks 2.0"
organization: "Project: Empower"
winner: true
words: 446
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/mental_health"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Mediversal

> Mediversal is an innovative app focused on revolutionizing mental health and self-care through ultra-personalized meditation audios and videos.

[Devpost](https://devpost.com/software/mediversal) · hackathon [[Empower Hacks 2.0]]

## Facets

**domain** [[mental_health]]
**substrate** [[structured_db]] [[web_dom]]

**stack** firebase, flask, javascript, openai, pycharm, python, smptblib

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mediversal

## Body

Inspiration In today's world, mental health resources are often behind a paywall barrier. This especially affects first-generation, low-income individuals who need them the most but can't afford them. This inspired me to create Mediversal, a free and publicly available customized meditation app that allows these groups to garner tailored and specific, rather than generalized, mental-health support. The name "Mediversal" is a combination of "Meditation" and "Universal." Mediversal aims to make mental health support universal for all, not just limited to a specific group or person. What it does Mediversal allows users to create customized meditation audios and videos through the "Meditation Generator" page. Here, users fill out a form with four required variables: description (the topic of the session), duration, meditation theme (background music and video clip), and preferred narration voice. Each generated session is saved to the "Generated Content" page, allowing users to easily refer back to their personalized meditation sessions. How we built it This application was built using the Framework Flask, Bootstrap5, Jinja, Python, JavaScript, variousAPIs (OpenAI, ffmpeg, etc). I also used Firebase’s Storage and Realtime Database in order to store the links and audio urls created such that I'd be able to reference them later on. Challenges we ran into Deploying my website onto a hosting server proved to be quite difficult for me. Unfortunately, the data files produced by my application exceeded that of the DATA Quota. Because of this and the time constraint of the Hackathon, I chose to simply show the demo working on my laptop solely. Accomplishments that we're proud of I'm especially proud of how I was able to successfully utilize both the OpenAI API and the ffmpeg API in order to create a customized finalized video and audio. Especially within a Flask application, a Framework that I've never worked with before. Additionally, being able to reference the data stored within my Firebase Realtime Database was quite rewarding as it was the key to the concept of getting the 'Generated Content' page to work. Finally, I'm also proud of the fact that I was able to complete the project in time and get it to work properly. I worked as a solo person, meaning I had a lot on my plate to complete. What we learned This was my first time working with the likes of Flask and Firebase. They're both extremely helpful in their own right. Learning how to set up Authentication, Storage, and Databases in Firebase in this project will allow me to implement it into other projects too. What's next for Mediversal Future plans for Mediversal include developing a mobile app, partnering with mental health organizations, and including feedback mechanisms and community features. <div