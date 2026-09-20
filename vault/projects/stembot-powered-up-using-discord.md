---
slug: "stembot-powered-up-using-discord"
url: "https://devpost.com/software/stembot-powered-up-using-discord"
title: "StemBOT powered up using Discord"
hackathon: "HackSwift 2024"
organization: "hackswift"
winner: true
words: 478
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/educator_student"
---

# StemBOT powered up using Discord

> STEM Bot is a revolutionary Discord bot designed to enhance your learning experience through interactive quizzes as a virtual study partner and educate you on a wide range of topics.

[Devpost](https://devpost.com/software/stembot-powered-up-using-discord) · hackathon [[HackSwift 2024]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[educator_student]]

**stack** discord, python, replit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for stembot powered up using discord

## Body

Architecture of the Stem Bot Inspiration Kahoot in school seems to be very educative while competing with friends. This bot is a simple text-based and helps make learning fun. What it does Bot is an educational bot that the user can comunicate to with a simple message "hello". It will respond back with an introduction. Here are some of the features: - User can pick different topics for the quiz - User can see real time scores (after each question) - User can skip if they don't know the answer. - User can also see final score after the quiz is over We used discord bot API and implemented backend code that reads the input from discord channel and finally compares the answers against the JSON format in memory using replit platform. Using various constructs part of python we implemented skip and scoring features to the bot. How we built it We built this bot using Discord and Replit. Discord is our User Interface (UI) and Replit is where we put the backend logic. For the backend, we wrote the code in python. Challenges we ran into We were not familiar with github platforms. Discord API setup was also challenging. Watching videos helped us and got hand-on. Thanks to Youtube channels that makes students lives easier these days if we effectively plan. JSON is the data structure we chose to store the questions in various subjects. Coming up with the simplest design was challenging with subjects in mind. The bot is an event driven program So, we had to make sure the user's state is preserved across multiple questions. Setting up mentorship sessions for students was challenging ; It was made possible through ADPlist a mentorship platform. Accomplishments that we're proud of We're proud to have developed a versatile tool that can be easily integrated into any Discord server, empowering users to engage in educational quizzes on a variety of subjects. This was our first time ever creating a Discord Bot and we successfully were able to run it. We also customized the bot so users can input a subject of their choice, and the bot quizzes them accordingly, fostering learning and engagement within the server. What we learned We learned to navigate through platforms such as Discord, Github, and Replit to create our bot. We also learned more in software development, by learning new ways to implement features into the bot by implementing backend code in Python. We learned how to add our bot to any Discord Server and how to manage bugs in the program. What's next for StemBOT powered up using Discord For now the StemBOT only has two subjects (with six questions each) programmed into it. In future, we would like to - Extend it by adding more subjects and questions. - Make it more fun and more gamelike - example: introduce leaderboard. <div