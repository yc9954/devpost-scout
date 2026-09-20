---
slug: "bulls-cows"
url: "https://devpost.com/software/bulls-cows"
title: "Bulls & Cows"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 418
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/document_pdf"
---

# Bulls & Cows

> Bulls & Cows is a code breaking mind game. The game helps you enhance your logical thinking and problem solving skill

[Devpost](https://devpost.com/software/bulls-cows) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**substrate** [[document_pdf]]

**stack** alexa-presentation-language, amazon-alexa, amazon-dynamodb, amazon-web-services, apl, aws-lambda, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for bulls & cows

## Body

Inspiration Bulls and Cows is the game that I used to play to help me build my own logic and improve my problem solving skills, and these are the skills which are most required in engineering. First I thought of bringing this game to voice and released the first version of the application. Then I realized that if the user does not note down all his responses on a notebook which playing it through voice, it becomes next to impossible for a user to solve it. To Solve this problem, I thought of adding and new prompt for the voice users and a display functionality of to the application. With the display functionality I am able to show user their previous responses, which help them understand the game better and also makes it easy for them. What it does Bulls and Cows is a Voice based game in which the user will have to guess Alexa's secret code. At the start of the game Alexa will think of a 4-Digit number and will keep that a secret. Now the user will make a guess. Based on the user's guess, Alexa will tell user the number of bulls and cows in the application. User will keep on guessing the number until they are able to find out the Secret Alexa Code. How I built it I used APL Authoring tool to create the APL docs and data sources. For creating the application, I used Alexa Skills Kit to create the frontend of the application and my own custom Python code hosted on AWS Lambda for the backend. Challenges I ran into Biggest challenge in developing the application for me was designing the APL documents. I took me a while to understand how things work. Accomplishments that I'm proud of This skill has one of the best interaction models for an Alexa Skill. I have tried my best to handle all the possible utterances that a user can say. The context of the conversation is always maintained. You say anything, anytime, everything is handles gracefully. What I learned Alexa Presentation Language Code Alexa Presentation Language Design Alexa Context Management What's next for Bulls & Cows I am thinking of adding levels [ 2,3,4,5 Digits] for the user so that people can begin from the basics and then move on to the advanced levels. Guessing a 4 digit number correctly is not easy for most of the users. The display functionality helps but does not cater the needs of everyone. <div