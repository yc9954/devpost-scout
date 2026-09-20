---
slug: "sleepinfo"
url: "https://devpost.com/software/sleepinfo"
title: "SleepInfo"
hackathon: "Junction 2016"
winner: true
words: 281
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
---

# SleepInfo

> Ask Alexa about your last nights' sleep, or for motivation to get up!

[Devpost](https://devpost.com/software/sleepinfo) · hackathon [[Junction 2016]]

## Facets


**stack** alexa, oura

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for sleepinfo

## Body

Inspiration We all know how hard it can be to get up from our comfy bed. Maybe we would like to know how efficient our sleep was on the previous night. Well, we created Sleepinfo to help achieve these goals and ultimately make your sleep better and more efficient with a sense of humour. What it does Sleepinfo is helping you monitoring your sleep data super easily, just by asking Alexa, whether you're still in bed, or out and about. It can also give you tips for improving your sleep if it sees your sleep quality decreasing. It can even motivate you to get up if you're having trouble in the morning. How we built it We have used an AWS Lambda instance that was linked to the Alexa API. The users' Oura accounts are easily linked to their Amazon accounts using oauth and Oura's sign in screen in the Alexa app. Using the obtained token our lambda instance queries the Oura API for the users' sleep data. Accomplishments that we're proud of SleepInfo is a really seamless way to get info about your sleep, that can really help you improve the users' sleep, since it takes less effort on their part. This is something we would love to use, which is part of why we created it. What we learned We have never used the Amazon Echo or the Oura ring, so this was a good chance for us to dive into some new technologies. What's next for SleepInfo We want to extend the information that it provides to you, have it control lightbulbs in the house, and playing soundscapes that are fine-tuned to provide the perfect wake-up experience. <div