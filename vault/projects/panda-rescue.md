---
slug: "panda-rescue"
url: "https://devpost.com/software/panda-rescue"
title: "Panda Rescue"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 573
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/runtime_tool_creation"
  - "domain/education"
  - "domain/security_privacy"
  - "user/government_staff"
---

# Panda Rescue

> The voice based panda adventure game.

[Devpost](https://devpost.com/software/panda-rescue) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets

**mechanism** [[runtime_tool_creation]]
**domain** [[education]] [[security_privacy]]
**user** [[government_staff]]

**stack** alexa, amazon-alexa, jovo, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for panda rescue

## Body

The Panda Wilderness School Newborn Panda 1 week old Panda 1 month old Panda 2 month old panda 3 month old Panda 4 month old Panda 5 month old Panda 7 month old Panda 10 month old Panda 14 month old Panda 18 month old Panda 2 year old Panda Inspiration The inspiration behind Panda Rescue was to create fun and immersive, but also educational experience for kids on Alexa. What it does Panda Rescue is an an educational story game for young children about the importance of conservation projects for vulnerable species, like the Giant Panda. Children will love the amazing sound effects as they play the character of a young volunteer who has just been accepted into the Panda Wilderness School, which is a Conservation and Research Center for the Giant Panda, in Wolong, China. The center has just rescued an orphaned baby panda from the forest and children play the assigned carer. The aim of the game is to teach the baby panda important life skills, so it can be released back into the wild when it's grown up. Children will be faced with a series of choices spread across 10 levels, meeting different characters along the way. They complete the game if the chief sanctuary officer decides their panda is healthy and skilled enough to attend the graduation ceremony and be released back into the wild. Once you've completed the game you can check your score and position on the leaderboard by going to: www.pandarescuegame.com How we built it The Skill is built using the Alexa Skills Kit. The app logic is written in NodeJS using the Jovo framework. The audio is generated using AWS Polly along with custom audio files and animal noises. Challenges we ran into We wanted kids to have as much of a personalised experience as possible, so we decided to allow them to name their baby panda. However this gave us the challenge that we could not use pre-recorded audio files, as the panda name used for each child would be different. For this reason we decided to dynamically generate the audio files as the child is playing the game. We do this using AWS Polly to generate the speech and then overlay the background audio files and sound effects over the top. Accomplishments that we're proud of We're proud that we were able to build depth into the game by having 10 distinct levels that follow the Panda over the course of it's early life, all the way to being released back into the wild. Each level is different and we hope this will give kids a truly immersive experience. What we learned One thing we learned was that initially we made the game a bit too hard! Most kids weren't able to get to the end of level 10 and successfully release the panda back into the wild. We've since made it easier to complete all the levels so that more kids get the full experience and feeling of pride when they complete the game - but we still keep a scoring system so they can see how well they've done on our leaderboard: www.pandarescuegame.com What's next for Panda Rescue We're continuing to test out the game with as many kids as we can. One thing we're thinking about adding is a separate skill that allows kids to practice their panda trivia with friends and family - stay tuned for this! <div