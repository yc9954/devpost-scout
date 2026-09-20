---
slug: "the-wizard-of-oz"
url: "https://devpost.com/software/the-wizard-of-oz"
title: "Wizard of Oz"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 579
team_size: 0
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Wizard of Oz

> Interactive role-playing game for kids that allows them to take the central role to find their way home to Kansas.

[Devpost](https://devpost.com/software/the-wizard-of-oz) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[education]] [[finance_payments]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** c#-asp.net-web-api

## How they structured the write-up

- inspiration
- what it does
- how to play
- how i built it
- challenges i ran into
- what's next

## Body

Inspiration I have a 12-year-old son (featured in the demo video) who is crazy about his Alexa device. My goal was to provide an entertaining game based on familiar elements that requires strong problem-solving skills and emphasizes the value in pursuing intelligence (brains), bravery (courage), and compassion (heart). The Alexa skill is based on L. Frank Baum's classic (public domain) book. What it does Wizard of Oz is an interactive role-playing game that allows students to use flexible, natural sentences to tell Alexa what they want to do in navigating their quest in the land of Oz. It's a true role-playing game, as young people think through problems in order to help others and advance their quest to find the Wizard, defeat the Wicked Witch of the West, and find their way back home. The game uses a rich assortment of voice actors and sound effects. How to play You give Alexa natural voice commands, normally a verb and object. E.g., "Pick up the hammer." "Talk to the Scarecrow." "Cut the rope with the scissors." "Use the oilcan." You can ask for help, and Alexa will read you a list of suggested commands that pertain to your current location in the game. If you really get stuck, you can say, "I need a hint" and you will be given a very strong clue about what to do next. The game keeps track of your progress as you go, in case you need to stop to take a break. You can also reset the game and play it from the beginning. The goal was to make the game challenging enough that young people have to make logical decisions using correctly phrased commands, but give them as much help as they need in case they can't figure out the right way to ask Alexa for something. The game is a simple story but it weaves in the kind of values we need more of in today's world. I made a downloadable PDF with a list of possible commands available at my website: https://daysfly.com/Gaming-Education/Gaming/Wizard-of-Oz How I built it ASP.NET Web API 2.0. The game is built on an engine I created to manage complex interactions (actions) involving agents (i.e., people and creatures who talk with you, follow you around, do things to help you, fight you, etc.), items, rooms, exits, and verbal expressions. This engine is controlled by scripting that I manage using a web interface I built. This allows me to dynamically change content, correct problems, and build complex interactions without needing to touch the underlying code. In other words, none of the content and interaction you're experiencing is hard-coded. It's flexible and expandable, making possible many more interactive adventures. Challenges I ran into (1) Using as much of Baum's book as I could to make it familiar but add in new challenges that enhance the story and make it an intuitive, puzzle-solving challenge. Knowing the story will prove to be helpful, but there are some twists and turns that will surprise you as well. (2) Accounting for a wide range of logical alternatives; this required a robust game engine to provide alternate paths to solve puzzles (e.g., what happens if the Tin Man is rusted and you don't have him with you when you go to talk to the Wizard?). What's next I'd love to gain support and funding to create a series of games that require problem-solving and reinforce values that we all want our kids to have. <div