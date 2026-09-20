---
slug: "pirate-maths"
url: "https://devpost.com/software/pirate-maths"
title: "Pirate Maths"
hackathon: "Alexa Skills Challenge: Beyond Voice"
organization: "Amazon"
winner: true
words: 629
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "substrate/video_visual"
---

# Pirate Maths

> Answer the times-table questions to help the pirates find the hidden treasure in this swashbuckling game for children aged 5-10!

[Devpost](https://devpost.com/software/pirate-maths) · hackathon [[Alexa Skills Challenge- Beyond Voice]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** amazon-alexa, amazon-web-services, litexa

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for pirate maths

## Body

Inspiration Pirate Maths started life as a simple game to help my 5-year-old son practise and learn his times tables while he was off school during lockdown. I wanted to make a genuinely immersive audio game with real voices, sound effects and pirate treasure! What it does In each game, you travel with the pirates around Skull Island, answering times table questions to help them find the buried treasure. Each time you answer a question correctly, you uncover some more treasure. You can choose a particular times table to practise, or a challenge game with a mixture of different questions. There are many different locations on the island, and you visit four during each game. There are also two pirates (one male, one female) and lots of different types of treasure to uncover. How I built it Pirate Maths was built using the Litexa framework, which allows developers to quickly design and prototype conversational games and skills for Alexa. Litexa programs can be mixed with Javascript to provide more complex functionality. The original game was written before APL for audio (APLA) was released, and used a very large number of recorded voice samples, pre-mixed offline with sound effects. This is a very time-consuming process if you want to add a lot of variety to a game. APLA allows developers to send voice and sound effects to Alexa and mix them on-the-fly. This meant that I could allow the player to visit different parts of the island, with different background sound effects without the need to re-mix a large number of audio files in advance. APLA also allows 'gapless' sequences of audio. I used this to join together speech seamlessly, which meant that I could reduce the number of speech samples used for the maths questions from literally hundreds to just 48. Challenges I ran into The original version of Pirate Maths involved shooting cannons to sink other pirate ships. Unfortunately, this version didn't pass certification due to being unsuitable for children! I had to redesign the game from scratch to make it suitable, and instead of shooting ships, players now use their maths skills to help the pirates dig for treasure. However, this has allowed me to add much more variety to the game. Rather than being stuck on a ship, you are able to discover and explore new locations throughout your adventure. The game has been updated several times thanks to feedback from beta testers. Accomplishments that I'm proud of I think I've succeeded in making the game feel genuinely immersive, through the use of voices and sound effects. Some audio responses involve recorded speech, and three or four different samples to build up a soundscape that I hope helps young players to imagine that they are really part of the game. Although the game does show images and simple animations on devices with screens, I think the game succeeds in working just as well on the huge number of devices without screens. What I learned The original version of the game was written using Litexa, but the framework doesn't support APL Audio yet. This meant having to use Javascript to considerably extend the capabilities of the skill. I learned a lot about ways of building up data structures which supported mixing of audio samples . I also decided to create all of the graphics used on devices with screens myself. This is the first time that I've created artwork for a published game. What's next for Pirate Maths My son is already asking which other parts of the island the pirates haven't been to yet, and he wants to explore more. I'd really like to expand the game into an ongoing adventure, with new locations being added on a regular basis, and perhaps even one-off quests. <div