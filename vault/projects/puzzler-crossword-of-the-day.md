---
slug: "puzzler-crossword-of-the-day"
url: "https://devpost.com/software/puzzler-crossword-of-the-day"
title: "Puzzler - Crossword of the Day"
hackathon: "Alexa Skills Challenge: In-Skill Purchasing"
organization: "Amazon"
winner: true
words: 914
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# Puzzler - Crossword of the Day

> Crossword fans can get their daily puzzle fix.

[Devpost](https://devpost.com/software/puzzler-crossword-of-the-day) · hackathon [[Alexa Skills Challenge- In-Skill Purchasing]]

## Facets

  <sub>weak: runtime_tool_creation</sub>
  <sub>weak: developer_tools</sub>
**substrate** [[structured_db]]
  <sub>weak: geospatial, sensor_telemetry, video_visual</sub>

**stack** alexa-skills-kit, amazon-web-services, azure, c#, lambda, node.js, sql

## Body

Dynamic APL Driven Crossword with Scrolling Clues Panel Main Menu Puzzler - Intro Screen Upsell Inspiration We had found that users of our skills are the same audience of people who play crosswords, we give people such as those who struggle with written puzzles or the visually impaired the ability to solve crosswords. What it does Players can solve crosswords using their voice, Alexa will read you the clue and then you will be given some time to think about the answer, you can Interrupt at any time with "Alexa, clue answer " . There is a high scores system which tracks your fastest time to complete a puzzle. All players have access to these utterances: "Skip" "More time" "How many clues have i answered?" "Repeat" "Help" "What is the word of the day" "What can I buy" We give free users a new 5 by 5 crossword every day to solve, we select a crossword from our data set based on the day of the year. Alexa will then ask you the clues from the crossword, for example "Break out of an egg, 5 letters". The user just has to shout out the answer to the clue. How I built it To create the structure of the project we used the Alexa Skills Kit CLI. We used Amazons S3 storage for all our in-game assets such as images and audio. We used an SQL server database to store our user settings. We used a voice over artist to be the "host" and then used Alexa to handle our dynamic speech content such as asking questions. We give free users a new 5 by 5 crossword every day to solve, we select a particular crossword from our data set based on the day of the year - Alexa will then ask you the clues from the crossword, for example "Break out of an egg, 5 letters". The user just has to shout out the answer to the clue. ⭐ In Skill Product ⭐ The ISP for this skill is called Puzzler Premium, which is a subscription costing £2.99/$2.99 a month, premium users get an extra 50 crosswords per month which are 9 x 9 in size, as well as their daily crossword. They also get unlimited hints on a clue (free players are capped at 2 hints) as well as access to additional intents: "what’s the answer?" - to hear the answer to the clue "solve the crossword" - to solve the entire crossword Challenges I ran into Due to the vast amount of answers in our interaction model, we found that there was a lot of times where an utterance would be confused for something else. For example, "Hatch" vs "Patch". This would mean that in some instances a player could never get an answer right. We created a Fuzzy matching algorithm which was modelled around using the Levenshtein distance . The algorithm will take two strings: the correct answer and the user utterance, calculate the "distance" (the similarity of the strings) and then return a % match, if the % match was high enough then we would assume the user meant the correct answer. We found that for smaller words we needed to have a more aggressive algorithm, since an 80% match on a 3-letter word would always be the entire word! Accomplishments that I'm proud of We are especially proud of the way we developed the APL for this skill. We dynamically generate a crossword grid based off our data set. We start off by drawing a grid in APL and then map certain values to each square in the grid, here's an example of the way a clue data is processed to use with APL: { "id": 1, "start": 1, "dir": 0, "num": 1, "answer": "BAP", "clue": "Bread bun", "clueDisplay": "Bread bun", "answerLength": "3"}, From this we can extrapolate that: The clue starts from square 1 (start: 1) Has a number 1 in square 1: (num: 1) Is in the across direction (dir:0) Goes to square 3 (answerLength: 3) We repeat this process for all the clues, leaving us an array of values which can be mapped to the structure of the grid, leaving us the correct crossword view. What I learned We have learnt how to hone our upsell process. When we handed the skill to our testing team, we discovered the upsell process to be quite abrasive, because of this, we have developed an algorithm to calculate placement and frequency of the upsell offers based on metrics calculated from our player data. We found that lots of users natural speech for solving crosswords is different to how we anticipated, for example, people wouldn't just say "Answer", they would instead say "Is the answer to five across 'Answer'?", this has allowed us to think about in more depth for future skills, and create a wider range of potential utterances for a given intent. What's next for Puzzler - Crossword of the Day We are looking into using the API offered by DashBot, this will allow us to track things such as user drop off and abandonment, top messages and intents as well as conversation paths, this will help us optimise our flow to ensure that our players are having the best experience. We'd also like to implement a global leader board using the GameOn SDK powered by Amazon, this will allow for a wide range of competitions and global leader boards so players can compete against each other. <div