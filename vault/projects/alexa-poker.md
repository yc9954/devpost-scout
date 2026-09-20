---
slug: "alexa-poker"
url: "https://devpost.com/software/alexa-poker"
title: "AutoPoker: Poker for Alexa"
hackathon: "Amazon Alexa Skills Challenge"
organization: "Amazon"
winner: true
words: 480
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# AutoPoker: Poker for Alexa

> AutoPoker! Play poker with your friends without having to deal with the hassle of dealing cards

[Devpost](https://devpost.com/software/alexa-poker) · hackathon [[Amazon Alexa Skills Challenge]]

## Facets

**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[web_dom]]

**stack** alexa, amazon-alexa, amazon-web-services, jquery, lambda, node.js, s3

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for autopoker

## Body

Inspiration I'm interesting in pushing the limits of what hardware can do by enabling new types of interactions between the user and the hardware. In this case, I'm expanding Alexa's capability by providing a website that multiple users can interact with in order to expand the functionality of what a skill can do. What it does When playing poker, one player always has to be the dealer. The exception to this rule is when it's played in a casino format, where a dedicated person deals the cards and doesn't participate in the game. This skill aims to replicate that kind of scenario by enabling Alexa to perform the job of a dealer. Players can play a hands-off game of poker by instructing Alexa what their actions are. "Alexa, I fold". "Alexa, bet twenty". Each player can view the field, chips, their cards, and more by using their smartphone. The game works like this: A user tells Alexa to start a new game. Alexa will announce a room code for players to enter on their smartphone. When everyone is in, the user tells Alexa to begin the game. Alexa then handles dealing the cards and prompting the players for their next action. Players will one by one tell Alexa what they intend to do (bet, call, pass, fold, etc). How I built it I built it using a suite of AWS. For the skill itself, I obviously used lambda. For the database, I used S3. For the website hosting, I also used S3. For the website backend, I used Lambda. I also used other services for minor parts, like KMS for managing my credentials, and API gateway for exposing the lambda service. Challenges I ran into I built this entire skill on my own, as a student, in the middle of a semester, while overloading 20 credits. It was very difficult to find time to consistently work on this. In addition, the game logic itself turned out more complex than I anticipated, and managing all the game logic so that it's concurrent between what Alexa knows and what the player see's on the phone was difficult. Also, setting up the system so that it's reasonably secure was tough. Accomplishments that I'm proud of Citing the last part, "I built this entire skill on my own, as a student, in the middle of a semester, while overloading 20 credits." I'm happy I managed to finish it. Also, I managed to host it using only free-tiers of AWS, so that's cool. What's next for AutoPoker The gameplay is far from complete. There are certain important mechanics that I didn't have time to implement that I hope to add in the near future. In addition, I have plans for expanding it from local multiplayer, to online multiplayer, where you'll be connected with other users with their own Alexa devices playing around the world. <div