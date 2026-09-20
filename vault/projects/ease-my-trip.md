---
slug: "ease-my-trip"
url: "https://devpost.com/software/ease-my-trip"
title: "Ease my trip. The new way to plan your next trip !!"
hackathon: "Alexa Skills Challenge: Alexa Conversations"
organization: "Amazon"
winner: true
words: 483
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
---

# Ease my trip. The new way to plan your next trip !!

> Create a fully customized day by day itinerary for free, just using Voice commands !!

[Devpost](https://devpost.com/software/ease-my-trip) · hackathon [[Alexa Skills Challenge- Alexa Conversations]]

## Facets

**mechanism** [[voice_speech]]

**stack** alexaskillkit, amazon-alexa, amazon-dynamodb, amazon-web-services, amazonalexa, apl, awslambda, dynamodb, googlesheet, googlesheets, lambda, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for ease my trip

## Body

Inspiration COVID19 is killing all the fun we can have in travelling and visiting places. But now we are seeing fewer cases of COVID19, everyone has started making plans. I was having a cup of coffee with my wife and just randomly asked Alexa. "Alexa, what are the best places to visit in Dubai?" and I was left with very limited options. Could not even check the weather for the month I am travelling, type of activities and how long will it take to visit each place. I needed some kind of app to help me make an itinerary for my trip to Dubai considering all the parameters. And what would make it an outstanding application if I can get it all these done just by using voice commands and send the final plan to my email that too using voice command. That is when i decided to work on this idea and make it a reality. What it does "Easy trip planner" helps a user plan a trip for any destination. User has to provide destination and travel dates in different ways. Once provided, Alexa shares a customized day to day plan for the mentioned dates. Alexa shares a list of activity considering time of day, type of activity and time duration for activities. Users can swipe through dates and activities. If user does not like any activity, they can check the "Activities to do" section and swap the activity. Once plan is prepared as per user's requirements, it is sent over to user via email How I built it We are currently using Google sheets and AWS dynamodb as backend. This skill delivers the best experience on display devices such as Echo show. Skil is built in Node.js language with code deployed on AWS lambda. Challenges I ran into Making a trip based on time is the most critical part. Allowing users to swap activity was very critical considering time limits. Working with intents and conversations parallelly was very challenging. Code builds failed so many times. Accomplishments that I'm proud of First of all, I have finally what I was searching for. I am very happy that people can plan their trip using Alexa devices. Our future development cycles include integration with Flight booking APIs and Ticket info/buy APIs. What I learned Making conversations like humans is very difficult. To some extent, we can design it but practical implementation is very complex. What's next for Ease my trip We are in talks with "Inspirock" and "Tiqets" teams for content collaboration. We finally made deal with “Tiqets” platform for ticketing platform integration and content API integration. Because of time crunch we can not implement it right now for competition but now it will be implemented in second phase of skill with more features and more places to visit. We will integrate Flight search & booking features, activity reviews & place reviews. <div