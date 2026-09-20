---
slug: "the-werewolves-game"
url: "https://devpost.com/software/the-werewolves-game"
title: "The Werewolves Game"
hackathon: "Alexa Skills Challenge: Beyond Voice"
organization: "Amazon"
winner: true
words: 932
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# The Werewolves Game

> During several nights, a town is haunted by werewolves. The villagers must be brave and try to catch them all before it's too late, being able to avoid that the town loses its last villagers...

[Devpost](https://devpost.com/software/the-werewolves-game) · hackathon [[Alexa Skills Challenge- Beyond Voice]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[video_visual]] [[web_dom]]

**stack** amazon-alexa, amazon-dynamodb, amazon-web-services, apl, apla, creativity, dynamic-entities, love, serverless, web-development, websockets

## How they structured the write-up

- the werewolves game
- what the skill does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for the werewolves game

## Body

Werewolf Villager Enter website and town Turn the virtual cards over Go to sleep Wolves wake up Dead question Dead player Timer to detect the werewolves Player blamed and locked up The Werewolves Game The Werewolves Game is an interactive and multiplayer audio game in which you will immerse yourself in a really great adventure, diving into the game with Alexa using multiple images and sound effects thanks to features like APL and APLA. During several nights, a town is haunted by werewolves. The villagers must be brave and try to catch them all before it's too late and thus being able to avoid that the town loses its last villagers... All this adventure takes place in a particular town determined by Alexa. You will need to virtually enter this town using your mobile phones to dive into a fantastic story. Will villagers be able to find all the werewolves before the last night? And the wolves,... will you be able to kill all the villagers without being captured? What the Skill does With an Internet-connected device (such a mobile phone or computer), families, friends and colleagues can go to HOMRESLOBO.ES website and start the game invoking the Alexa Skill and following Alexa's instructions. Alexa will say a room/town name to enter in (as well as display it in APL-enabled devices). You need at least 4 players to enter the room with different usernames using their own devices. Say Alexa when you're ready. After the game starts, pay attention to your screens because you are going to receive a CARD you must CLICK to reveal you character in the game and know if you are a VILLAGER or a WEREWOLF. You must keep this information in secret. If you are a werewolf, every turn you must select who will be your victim in the form that will appear in your screen. The villagers will try to lock up every werewolf by saying "Alexa, it was Clara" or "Alexa, we blame Clara". The lynched player reveals his/her role and is out of the game. A turn begins when Alexa says "Let's go to sleep" so that all players must close their eyes. When Alexa says "Wolves wake up", those players who receive the card of a wolf in their screens must open their eyes. When Alexa says "Wolves chose a victim", the wolves must select a victim in the form that appears in their screens. When Alexa says "Wolves go to sleep" wolves must close their eyes like the rest of the players. When Alexa says "Everybody wake up... Are you ready to know who is dead?" all players can open their eyes and answer Alexa to know who was the victim selected by the wolves that night. Now it’s time to catch the werewolves! How I built it I’ve combined multiple technologies and tools to create this immersive and interactive Alexa Game Skill: Alexa Presentation Language (APL) Alexa Presentation Language for Audio (APLA) Customized Interactions with Dynamic Entities Speech Synthesis Markup Language (SSML) Alexa Skills Kit Sound Library i18n for Skill and web Internationalization (english & spanish): both the Skill and the web content change dynamically with the locale Software development: Visual Studio Code, Node.js, JavaScript, HTML5, CSS3, Bootstrap Deployment in AWS: Serverless Framework, Amazon API Gateway for REST and WebSocket interfaces, Lambda Functions, DynamoDB for data persistence, S3 and Route53 Visual design: Canva and Figma Challenges I ran into I've dealt with a series of obstacles related to the inexperience in different technologies and tools that made my way a little more tricky. It was the first time for me to use the serverless side of AWS in its entirety. I had experience in building code for Alexa Skills with Lambda functions and also in persisting data with DynamoDB, but it was completely new for me to work with API Gateway and the Serverless Framework to easily deploy the complete final solution. Even more challenging, I needed to use API Gateway for two different purposes, expose not only a REST API but also a WebSocket API. WebSockets were not as familiar to me as an HTTP client-server architecture. So, I needed to build up a solution which was unfamiliar to me and deploy it with tools that were not familiar either. However, if I wanted to create such an interactive audio game using not only Alexa but also players' smartphones, I should face the obstacles to reach my goal. Accomplishments that I'm proud of I'm absolutely proud of having built up a complete solution "from zero to hero" using so many different technologies and tools, even if they were unfamiliar to me. What I learned The most important knowledge I have acquired with this challenge is that if you want to build something new and different, you may need to apply lots of effort, but it will worth it. According to tech terms: I have learned about serverless philosophy and I have applied it using AWS and Serverless Framework I have worked for the first time with a WebSocket-based communication system using Amazon API Gateway I have also used for the first time both the APLA combining speech an audio not only in sequence but also in parallel and Dynamic Entities for customized interactions in order to make the usernames inserted in the web page understandable to Alexa What's next for The Werewolves Game The future of this Skill involves: Translating the game into multiple other languages such as French or German Adding new characters to the game, not only villagers or werewolves Enriching the audio experience with Alexa Emotions <div