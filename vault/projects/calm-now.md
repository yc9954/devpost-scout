---
slug: "calm-now"
url: "https://devpost.com/software/calm-now"
title: "Calm Now"
hackathon: "Alexa Skills Challenge: Life Hacks"
organization: "Amazon"
winner: true
words: 531
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
---

# Calm Now

> Whether its anger or sadness, this Alexa skill will teach a kiddo techniques to calm down.

[Devpost](https://devpost.com/software/calm-now) · hackathon [[Alexa Skills Challenge- Life Hacks]]

## Facets

**mechanism** [[simulation_digital_twin]]

**stack** amazon-alexa, amazon-web-services, javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i’m proud of
- what i learned
- what’s next for calm now

## Body

Inspiration Watching your kid so sad or so angry can bring about all kinds of different emotions as an adult. Sometimes you feel really bad for them and just want to comfort them while other times you feel pretty mad yourself and not in a very comforting mood. I wanted to build a skill that would provide a fun and productive way for kids to deal with their intense emotions, something that would teach them coping skills that they could eventually employ even without Alexa around. I originally created a version of this skill as a mobile app for the phone, but decided it would also be helpful as an Alexa Skill. What it does After launching Calm Now, it will go through three different (randomly chosen) calming techniques. The techniques start with a more active one, when a kiddo would be the most upset, and progressively get calmer. After the three techniques, there is an option to go through three more techniques or just be done. How I built it I used AWS Lambda to host my javascript with an audio file stored in S3. I use session data to track which calming techniques have already been done, so that there aren’t repeats during a session. I don’t persist any data after that. Challenges I ran into Truthfully thinking up different and unique calming techniques proved challenging. I have included some techniques that actually involve stopping the skill and going to listen to music or reading a book. I toyed with not including them, but I think they are really good calming strategies so decided to leave them in but make sure they come up at the end of the set of three. Also, there is still an option to keep going. Another challenge was in figuring out how much time to allow someone to do a task such as taking deep breaths or going and getting water. It will really depend how accessible those things are as to whether enough time was allocated or not. Accomplishments that I’m proud of This was the first Alexa skill I ever created back in October. I updated it for this challenge to do a series of three instead of just one technique at a time. I just remember last October, not knowing anything about Alexa, deciding that I was going to learn and build something. It was really empowering. What I learned Originally when I built this skill I learned everything from just how to build a basic Alexa skill, to working in lambda to using the Alexa simulator. This latest round I had to learn how to use the updated simulator but otherwise felt pretty comfortable. What’s next for Calm Now It was originally built to target both adults and kids, but I changed it to be just a kid focused skill. It will be interesting to get feedback on the updates and let those dictate some changes, but I’d love to add in more calming techniques as well as something that can customize the experience more to the specific kid (i.e. which techniques they like the best, different types of techniques depending on the level of upset they are). <div