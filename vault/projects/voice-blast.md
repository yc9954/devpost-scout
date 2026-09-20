---
slug: "voice-blast"
url: "https://devpost.com/software/voice-blast"
title: "Voice Blast"
hackathon: "Alexa Skills Challenge: Beyond Voice"
organization: "Amazon"
winner: true
words: 809
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Voice Blast

> Compete against others in a game of celebrity guess who!

[Devpost](https://devpost.com/software/voice-blast) · hackathon [[Alexa Skills Challenge- Beyond Voice]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[finance_payments]]
**substrate** [[structured_db]] [[video_visual]] [[web_dom]]

**stack** amazon-dynamodb, apla, ask-sdk, node.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for voice blast?

## Body

Gordon Ramsay... correct! Splash screen Inspiration Our players love competition, we've seen videos of fans playing our skills, celebrating victory when they beat a "bot" player. So we wanted to enhance this by adding custom nicknames and real opponent rankings and an actual PVP experience. We thought about successful skills, and decided to base this on Voice of the Day , people love celebrities and guessing games so our plan was to create a brilliant mishmash of the two that will (hopefully) be a fan favourite! What it does The aim of the game is to guess celebrity voices as quickly as possible in a match of 5 questions against another player from around the world. Answer before the clip is over and get double points! If you win a match you get 5 points, if you draw, 2 points. The points you earn add up to a score on our global leader board. The skill uses some awesome audio beds, and sound clips. For example: let's say you draw the match, you might be played the clip... close but no cigar! You can spell out your own custom username, earn rankings and compete on our global leader board! How we built it We used APLA to manage the audio throughout the skill, one of the main benefits of using it was to avoid the 5 audio file limit, this let us get really creative with the audio sequences we serve the user. We developed the viewports using APL, some key points were scaling the celebrity images properly in every viewport using the best-fit on the scale property of an APL image component, to make sure they weren't stretched or blurred. A lot of development time went into gathering voice content, we mostly scoured YouTube videos, until we found a brilliant resource on a site called https://www.playphrase.me/#/search . This website allows you to search for specific phrases, returning video clips from a huge library of movies that contain that phrase! We took these clips and converted them to mp3's to use in Voice Blast. We used the ASK-SDK to manage our skill deployments, and hosted the audio files and imagery using S3 buckets. Challenges we ran into A challenge we faced was accurately calculating the time it takes for a player to respond, this is important since we award double points if you answer quickly. However, we found that timing with Alexa is very difficult, due to varying length of TTS and audio clips. These are the steps we took to solve this issue: create a function that takes an input of SSML, and converts to an mp3 file using Amazon Polly node library. use FFmpeg to concatenate this mp3 with other mp3's in the response. calculate the length in seconds of the newly created mp3 using the get-audio-duration node library. Using the time in seconds returned from this function, we calculate a date time stamp. If the user answers before this time stamp they get double points! Accomplishments that we're proud of We're proud of how we handled player matching. Since headless devices don't support real time multiplayer, we had to come up with a solution which simulates this in the best way possible. We created a system of "delayed player matching". Every time you answer a voice clip, your answer and answer speed are recorded against your user in our database. Then, when we randomly select a user for you to be paired against, we will look at their previous answer data. If the clip that is being played in your match is included in their answering data, then the skill will use their previously given answer. If the opponent hasn't answered the clip before, we look at their lifetime score and run a random number generator between 1 - 100. If the number produced is less than their expected score percentage, then they're given a correct answer. What We learned We learned that giving users free range of spelling out nicknames presents some UX issues, not only for slowing down the players introduction into the game, but also for other players since despite profanity filters - deviations of inappropriate usernames were getting through. We've now had to remove the feature of sharing opponents usernames and instead show a randomly generated username, even though you are technically still matched up against them! What's next for Voice Blast? We want to add more clips and content into the game, we've already seen some players with over 1000 points on the leader board, which means that they've played through 1000 celebrity voices, which is our question bank 5 times over! We're thinking of having a menu option which offers the user to select an "era" of celebrity, or even a sub genre for example "characters from cartoons". This would allow users from all generations to enjoy the game. <div