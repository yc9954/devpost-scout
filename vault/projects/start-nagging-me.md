---
slug: "start-nagging-me"
url: "https://devpost.com/software/start-nagging-me"
title: "Start nagging me"
hackathon: "Alexa Skills Challenge: Life Hacks"
organization: "Amazon"
winner: true
words: 458
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/developer"
---

# Start nagging me

> Trouble motivating yourself? Say Alexa, start nagging me and she will nag you every minute in a tailored and fun way!

[Devpost](https://devpost.com/software/start-nagging-me) · hackathon [[Alexa Skills Challenge- Life Hacks]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** amazon-web-services, aws-lambda, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for start nagging me

## Body

Inspiration The built in Alexa timer feature is one of the most popular use cases for the device. I've used it a few times to deal with procrastination, but I felt it was lacking those key nagging phrases that really get one going. The other issue was that it didn't repeatedly nag over and over, which is key to good nagging. So I decided to build a comprehensively annoying nagging skill called 'Start Nagging Me'. What it does Just yell out "Alexa, start nagging me" and she will ask you what you want to be nagged about, and then ask you for how long. If you chose 'Washing the dishes' as your task then Alexa will give you some tailored motivational words about washing the dishes every minute and tell you how much time you have left. She emulates that nagging person in your life that has a knack for getting you moving. How I built it This is built using AWS Lambda for request handling logic and uses AWS S3 as storage to help identify return users and not bore them with lengthy skill introductions. The skill makes use of the SSML pause feature by chaining pauses together to create a minute of silence between nags. Challenges I ran into Alexa Skills can be launched by saying 'Start ', so I took advantage of that by using 'nagging me' as my invocation word. Unfortunately an intent can not be tied to a 'Start' type of invocation. So I was unable to make it work like so.. "Alexa, start nagging me to wash the dishes". Alternatives could have been using an invocation name like 'Nag bot' and say "Alexa, ask Nag bot to nag me about washing the dishes", but that is a mouthful, so I've just opted for a sleek VUI to set up the nag. Also, it isn't possible to keep the skill running much more than 10 minutes without user interaction, so I had to build a refresh prompt into the VUI to keep the nags going if they had chosen a time period over ten minutes. Accomplishments that I'm proud of The skill is quite popular, there is definitely an interest in this type of skill. I was able to get a few hundred sessions of usage data and customer feedback to help optimize the skill prior to final submission. What I learned There is a notifications capability coming out for developers where users can opt in to get notified. This would expand my skill in the future as I could create periodic nags that don't require the skill to be running in the foreground. What's next for Start nagging me Let customers save their favorite nag which automatically starts with the skill. <div