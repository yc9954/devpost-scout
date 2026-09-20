---
slug: "guess-my-name"
url: "https://devpost.com/software/guess-my-name"
title: "Guess My Name"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 618
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Guess My Name

> Laptops down and phones away, for this guessing game you can play all day!

[Devpost](https://devpost.com/software/guess-my-name) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets


**stack** amazon-alexa, jovo, node.js

## How they structured the write-up

- inspiration
- what it does
- multimodal
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for guess my name

## Body

Choose Category Screen - TV Choose Category Screen - Show Choose Category Screen - Spot In Game Screen - Show / TV In Game Screen - Spot Leaderboard Screen - Show / TV Leaderboard Screen - Spot Inspiration Laptops down and phones away, for this guessing game you can play all day! Fun for one, or for all the family, You’ll hear a series of clues, in a certain category. Your job is to guess, whom you think it may be, but you'll have to be quick, if you want to score highly! Shout out your answer, if you think you know. For example you'd say: "Alexa you're Marilyn Monroe!" There’s even a Lightning Round, if you’ve a competitive streak, See if you can be top of the leaderboard, we announce the winners each week! To see how you’re getting on, go to playguessmyname.com Or you can just play for fun; there’s plenty of categories to choose from! To get started with this game, say "Alexa, open Guess My Name!" What it does Guess My Name has 4 game modes: —LIGHTNING ROUND (daily)— You've 2 minutes to answer as many questions as you can! New questions released each day. Your aim is to get a highest score for the day, which is then added up over the week to give your regional leaderboard position. Winners announced in the skill on Mondays! Playing on an Echo Show/TV/Spot? Open Guess My Name then ask: "Alexa, show me the leaderboard!" Or you can check it at www.playguessmyname.com Don't like your username? Open Guess My Name then ask: "Alexa, change username" --PRACTISE MODE-- Play against yourself to build up your trivia knowledge in prep for the daily Lightning Round! --HEAD TO HEAD-- Play against a random opponent from somewhere in the world. See if you can beat their score! --MULTIPLAYER-- Challenge your family or housemates to a game! Multimodal Guess My Name is a fully multimodal skill and makes use of the Alexa Presentation Language in every interaction. We have 6 main screen layouts: Choose Mode Screen --> Select which game type you want to play. Choose Category Screen --> Select which category you want to play. Game Confirmation Screen --> Review your game information before beginning the game. In-Game Screen --> See the current scores as well as a clue for the current question! Leaderboard Screen --> View the international Guess My Name leaderboard across multiple regions and timeframes. Dynamically change the data that's displayed using either your voice or the touch controls. Each screen layout is fully responsive across the different Alexa device types such as FireTV, Echo Show, and Echo Spot. How we built it The Skill is built using the Alexa Skills Kit. The app logic is written in NodeJS using the Jovo framework. Challenges we ran into Building a Trivia Skill with over 1000 question answers leads to difficulties in maintaining a suitable level of recognition accuracy. We used multiple layered methods to ensure we have the maximum chance of correctly identifying a correct answer based on what the user says. Designing a leaderboard in APL was a new challenge for us. We had to ensure that it looked good across all device types and sizes. We also wanted to make the table layouts reusable so that we can implement this feature in other skills. Accomplishments that we're proud of To our knowledge this is the first leaderboard in an Alexa Skill where users can dynamically filter the data with their voice: "Show me the leaderboard in the US for this week" "What about last week" "Show me the international leaderboard for this month" What's next for Guess My Name More game modes, categories and features! <div