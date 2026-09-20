---
slug: "mighty-trivia-a-guessing-game-for-kids"
url: "https://devpost.com/software/mighty-trivia-a-guessing-game-for-kids"
title: "Mighty Trivia - a guessing game for kids"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 565
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Mighty Trivia - a guessing game for kids

> Alexa pretends to be something and you have to guess what it is based on her hints. It also has a global leaderboard.

[Devpost](https://devpost.com/software/mighty-trivia-a-guessing-game-for-kids) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets


**stack** alexa-skills-kit, api-gateway, javascript, lambda, node.js, s3

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for mighty trivia - a guessing game for kids

## Body

Global leaderboard at mightytrivia.com Inspiration A lot of the trivia and guessing games I had looked at had pretty complicated voice-user-interfaces (VUIs). My aim was to build a guessing game skill that was straight to the point and intuitive. What it does Mighty Trivia is a guessing game for kids. Alexa pretends to be an object, place, person or animal and you have to guess based on the hints provided. There are three difficulty levels and lots of random questions. Basically Alexa will pretend to be an object, person, place or animal and you can either ask for another hint or have a guess based on the hints provided. You only get five hints per question and you get two attempts to guess the answer per question. Scoring is based on the speed at which the answer is guessed correctly (incorporating the number of hints and elapsed time) and the difficulty level of the question. The game is over when the user runs out of guesses or the questions within the difficulty level have been exhausted. You will progress from the easy to moderate difficulty when your score passes 1000, and you will progress from moderate to hard difficulty when your score passes 1500. The hard level will continue until all questions are exhausted. The top scores (only the scores) are displayed for 24hrs on a global leaderboard at mightytrivia.com . Why is it educational It helps children learn useful facts about various things. It can also assist as a memory booster because kids can progress through the challenge faster if they remember a previous answer when it comes up again. Why is it engaging It is engaging because customers get a score for every question as they progress through the difficulty levels. If they score high enough, their total score is posted for 24hrs on a global leaderboard, promoting healthy competition across the entire customer base. Why is it entertaining It entertains by invoking kids' competitive spirit. Having limited attempts and limited hints, kids have to decide whether to guess or get a hint. They also know that if they get another hint, their score for that question will be much lower. It also provides exciting sounds and randomised voice responses during the gameplay. How I built it I built the core Alexa skill using the Alexa Skills Kit, AWS Lambda and AWS S3. The leaderboard is hosted in AWS Route53 and delivered via AWS CloudFront and AWS API Gateway. Challenges I ran into Testing was difficult as my son quickly got used to the gameplay, so I didn't get fresh ears / feedback on the skill until it was live on Christmas Eve 2017. Accomplishments that I'm proud of The skill had really good uptake over the Christmas period, picking up about 50-70 new customers per day and generating over 15,000 customer utterances in a week. This enabled me to analyze usage data and improve the skill. What I learned The data model is key for enabling scaleable content and functionality. Also, using SSML to add sound is worth the effort as it provides nice polish to a skill. What's next for Mighty Trivia - a guessing game for kids More SSML and more questions to be added over time. Will definitely look at tagging themes to the questions to enhance contextual engagement during seasonal events such as Easter, Christmas, Thanksgiving etc. <div