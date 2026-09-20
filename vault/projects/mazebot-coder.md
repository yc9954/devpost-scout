---
slug: "mazebot-coder"
url: "https://devpost.com/software/mazebot-coder"
title: "MazeBot - Coding Challenge Maze"
hackathon: "Facebook Hackathon: Messaging"
organization: "Facebook"
winner: true
words: 575
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "substrate/structured_db"
---

# MazeBot - Coding Challenge Maze

> Want to practice maze solving, and get some coding exercise at the same time? MazeBot delivers both!

[Devpost](https://devpost.com/software/mazebot-coder) · hackathon [[Facebook Hackathon- Messaging]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]]
**substrate** [[structured_db]]

**stack** amazon-dynamodb, amazon-web-services, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for mazebot coder

## Body

Inspiration My inspiration for MazeBot came from failing coding challenge interviews in the past. As a challenge to myself, I wanted to make these interviews part of my strengths in the future. I wanted to build a program that is simple to use and that I can help sharpen the mind when it comes to coding. I was able to learn a few extra tools that would assist me while creating this game. I wanted to build a bot that would incorporate my knowledge in data structures, algorithms, but also come up with a small daily brain exercise to keep my coding skills working constantly. Even though the challenge is simple, it helps the user by challenging them to think through each maze and get into the habit of solving problems constantly. What it does MazeBot generates a random maze (via emojis) to challenge the user. Once a maze is generated, the user must find a way to solve the maze. Using the messenger text field, the user will have to "code" a working solution by typing specific characters and a specific logic unique to the maze. The user can also use the loops and directions to solve the maze. How I built it The application was built with Messenger API and NodeJS. The Webhook is hosted using Heroku. AWS Dynamo-DB as a state management tool. A recursive backtracking algorithm was used to generate random mazes. Messenger button templates were used as a specific tool for generating mazes, this kept the maze generation as a postback payload instead of a message text. Quick Replies were used to show different parts of the application to assist the user in what they needed to solve the maze. Challenges I ran into Using the database asynchronously, and making it work properly with the Messenger's asynchronous nature was particularly challenging. Determining what is a valid "code" solution and what is not was specifically difficult. A combination of string parsing and regex was necessary to ensure the data being processed is clean and accurate. Accomplishments that I'm proud of The greatest accomplishment I was proud of was being able to build a working bot in less than a week while working with APIs I was not familiar with and simultaneously incorporating old technologies I already knew with it. What I learned I am a software developer! For the longest time, I was wondering if I can come up with something that did not involve tutorials, or code alongs. This experience taught me that I can thrive even though I am not familiar with the tools yet. I can learn and grow fast in areas that constantly challenge me, and I learned to be self-sufficient quickly. Now, I have confidence knowing I can build useful programs by myself, and if I was given the opportunity to works with a team of more knowledgeable engineers, I think I can progress even faster. What's next for MazeBot Coder I would like to add a timer to certain solutions. When the time limit is reached, the code gives you a hint. I would like to have a "give me the solution" quick reply, where the algorithm can solve the maze, and generate a solution for the user. Generate a more difficult maze, via a different algorithm. Incorporate a challenge mode, where you can challenge a friend to solve the maze you just solved. Incorporate a score database for keeping track of solved mazes. <div