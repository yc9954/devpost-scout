---
slug: "the-great-expedition"
url: "https://devpost.com/software/the-great-expedition"
title: "The Great Expedition"
hackathon: "Alexa Skills Challenge: Alexa Conversations"
organization: "Amazon"
winner: true
words: 577
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# The Great Expedition

> Can you explore the far corners of the world and find long-lost artifacts, rare animals and priceless works of art? But beware, dangers lurk at every corner

[Devpost](https://devpost.com/software/the-great-expedition) · hackathon [[Alexa Skills Challenge- Alexa Conversations]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** alexa, amazon-alexa, amazon-web-services, node.js

## How they structured the write-up

- tl;dr
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for the great expedition

## Body

First step of an expedition Note that bringing the tool box unlocked a new option Potential result of an expedition tl;dr The Great Expedition is essentially a set of non-linear adventures in an persistent environment, meaning that every expedition is something like a “Choose your own adventure game” but the choice you make influence future games. In addition, you have a pool of characters and items, from which you select a subset for each expedition which can open up even more options. Successful expeditions can provide you with new items, characters or even new regions. Alexa Conversations makes the selection of region, characters and items much easier than traditional Intent based Dialog Management. Inspiration Even as a child, I found 'choose your own adventure' books fascinating. I remember trying to reverse-engineer a particularly hard puzzle by going through each and every section. With The Great Expedition I wanted to bring that feeling of exploration and progress to Alexa. The beta release of Alexa Conversations finally made it possible to build a robust and user-friendly way of selecting items, characters and location. What it does In ' The Great Expedition ' you start in London at the turn of the century. The Royal Exploration Society has tasked you to find long lost artifacts, rare animals and priceless works of art. You will need to mount expeditions to far corners of the world. Fortunately for you, you have already some competent companions and helpful items at your disposal. However, you cannot take everything with you on an expedition at the beginning. Your points in leadership determine how many companions you can take with you. The same goes for knowledge and your items. Lastly, there is morale which determines how long you can motivate your crew on an expedition. Should morale drop to 0, your crew will mutiny. Expeditions are essentially 'Choose your own adventure stories'. Meaning, during your expeditions you often have multiple options and you will need to decide which to pursue. Note that different characters and items might unlock new options. Successful expeditions can unlock new characters, items, and even new locations. Returning rare animals and treasures will also earn prestige with the Royal Exploration Society. How I built it ' The Great Expedition ' is an Alexa-hosted node.js skill using DynamoDB for persistence. Challenges I ran into As a software developer, I initially found it difficult to use the developer console to create and annotate dialogs, response, utterances etc. But after a while, it became actually easy and enjoyable due to the validation and pre-selecting of variables and options among other things. Accomplishments that I'm proud of Submitting a working and hopefully enjoyable skill. I was very proud, the first time my Alexa Conversions Dialog finally worked using context carryover, list items and corrections What I learned Time-management and focusing on the core idea. Designing and developing the skill as a single person meant that I needed to focus on the core experience in order to deliver something valuable at the deadline. See the next paragraph ;) What's next for The Great Expedition Regarding the content, I have a lot of ideas in my head about new locations, expeditions, characters and items. Technically, I would like to polish the presentation using more APL features, e.g. adding a morale tracker and enabling character/item selection via on-screen buttons. In addition, I would really like to play around with APL for audio to add effects or background sounds. <div