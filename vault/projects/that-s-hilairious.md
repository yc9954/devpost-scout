---
slug: "that-s-hilairious"
url: "https://devpost.com/software/that-s-hilairious"
title: "that's hilAIrious!"
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 435
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "user/educator_student"
  - "user/legal_professional"
---

# that's hilAIrious!

> Who's the funniest? We'll let AI be the judge.

[Devpost](https://devpost.com/software/that-s-hilairious) · hackathon [[Hack the North 2021]]

## Facets

**mechanism** [[realtime_stream]]
**user** [[educator_student]] [[legal_professional]]

**stack** express.js, face-api, heroku, node.js, react, socket.io, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for that's hilairious!

## Body

Inspiration The pandemic has forced many of us to rethink how we socialize and interact with friends, family, and coworkers. Fun, lively in-person gatherings have been replaced with a plethora of online party games - but what many of these games lack is the ability to create human connections and a sense of community. Our idea: to bring all our faces together (virtually) and put laughter at the centre of our game. What it does that's hilAIrious is an online party game where friends can tell jokes and win points for how much they make their friends laugh, based on our algorithm which uses Face API. Players can join individual rooms, where they'll be able to see and chat with other players. Once the game is started, each player will have a turn to respond to a prompt, after which their response is revealed to the room and our algorithm calculates the player's score based on how much the others were laughing. At the end of the game, players can compare scores and see who was the funniest in the group! How we built it Our game uses a Express.js backend server and a React frontend. Twilio is used to stream video and audio between the players, while Socket.io allows the backend and clients to communicate in order for game mechanics to proceed in real time. We use Face API, a library built on top of TensorFlow.js, to analyze how much each player is laughing and generate a score from that. Challenges we ran into Fine-tuning the Socket.io communication between the server and clients was difficult and a bit tedious. Also, it was our first time deploying a React/Express.js together to Heroku, and we ran into issues configuring the repo to have our app built properly and without timeouts. Twilio was also completely new to us which gave us a new challenge, and the great documentation and intro tutorials were incredibly helpful. Accomplishments that we're proud of Creating an algorithm using Face API to calculate a score for each player Implementing Twilio successfully to stream audio and video Using Socket.io for realtime communication Creating and deploying a React/Express.js app to Heroku Our UI and animations What we learned How to use the Twilio video platform How to create a React app incorporating Twilio and Socket.io Using a TensorFlow.js library What's next for that's hilAIrious! Adding new gamemodes like a try not to laugh challenge, where players can suggest videos for the room to watch Displaying more feedback in the UI such as AR filters or highlighting to indicate which players are laughing the most <div