---
slug: "my-rewards"
url: "https://devpost.com/software/my-rewards"
title: "My Rewards - Alexa Skill"
hackathon: "Alexa Skills Challenge: In-Skill Purchasing"
organization: "Amazon"
winner: true
words: 452
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "substrate/geospatial"
---

# My Rewards - Alexa Skill

> An Alexa skill to reward kids for good behavior

[Devpost](https://devpost.com/software/my-rewards) · hackathon [[Alexa Skills Challenge- In-Skill Purchasing]]

## Facets

**mechanism** [[on_device_local]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** amazon-dynamodb, amazon-lambda, amazon-web-services, express.js, node.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for my rewards

## Body

My Rewards Inspiration After building http://eFamilyBoard.com I decided to purchase an Alexa Show (2nd gen) for comparison. eFamilyBoard has a few nicer features but over all the Alexa is much more powerful and scalable. One heavily used feature was the sticker board on eFamilyBoard that didn't have a comparable skill on Alexa. As a result, I decided to build My Rewards skill to replace it. What it does It allows families and teachers to reward kids for good behavior. The user ultimately decides what to do with the rewards. Personally, our kids earn $5 after they've earned 10 total rewards, then they start over. The user can add recipients and give multiple rewards at a time. For example, "Alexa give John 5 stickers" or "Alexa take away 2 stickers from John". And if you don't know what reward type of reward to give or take away you can always simply say "rewards" in the place of the type of reward (e.g. football, sticker, heart, unicorn, truck, cookie, doughnut, etc). How I built it I built it with the ASK CLI and Visual Studio Code. I started with the sample hello world app and refactored it to utilize typescript, express, and ngrok to run locally. I also used mocha with chai for unit tests that run and must pass before I can deploy to AWS. Challenges I ran into I learned to get stated by taking a course on Udemy but they didn't use typescript and deployed to AWS for every change. That would take FOREVER to debug and build efficiently. I setup a simple express app and use ngrok to route calls to my local machine. This allows me to talk to my Alexa and debug by stepping through the code in VS Code. Accomplishments that I'm proud of Project setup, local debugging with typescript, and tests with 90%+ code coverage. Not only does it work for voice but it also supports display templates to show the user what rewards each participant has earned. I was going to add ISP down the road but decided to do it from the start and it ended up being easier than expected. For being my first Alexa app I think the app works extremely well and my kids started to utilize it with no learning curve. What I learned Being my first Alexa app I learned a TON. From how to simply use Alexa (still learning tricks) to how to interact with voice commands. I've also never used DynamoDB but the Alexa SDK made that super easy. What's next for My Rewards Add support for more languages. My family has been using it for development but exited to see what others think of it. <div