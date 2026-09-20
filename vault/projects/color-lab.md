---
slug: "color-lab"
url: "https://devpost.com/software/color-lab"
title: "Color Lab"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 570
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
---

# Color Lab

> It's an Alexa Skill that teaches kids colors

[Devpost](https://devpost.com/software/color-lab) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]]

**stack** lambda, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for color lab

## Body

Press the purple color Press the yellow color Choose a game Press the red color Roll Call Touchscreen controls Now with touchscreen capability on compatible devices Inspiration After learning about Echo Buttons at re:Invent 2017, I was looking for a minimal viable product to use them in a skill. That Christmas, my son got all these toys related to learning colors. I've also been interested in STEM education for a long time. I started Progressive's STEM Progress program, which has helped reinforce STEM concepts in over a thousand classrooms. Anyway, I thought that would be a great way to use the echo buttons and released Color Lab during the first half of 2018. I learned about APL at re:Invent 2018. What it does Color Lab has two ways to play, with Echo Show or Echo Buttons and there are two games to play: Push the Colors and Hear the Colors. Hear the colors is best for earlier learners. When the child pushes the button, Alexa will tell them the colors. As soon as the button is pressed, new random colors are displayed on each button. When playing push the colors, children are rewarded for pushing the right color with an applause sound file. The colors jump around when the right one is pushed. Neither game tracks score; this is aimed at young kids and isn't meant to be competitive. How I built it It runs in Lambda. I started with the Color Button template. I then added more color sets and audio files for applause. Additional instincts were added for this functionality and utterances based upon what users have tried. Challenges I ran into Initially, I had some trouble understanding that the buttons completely bypassed the normal interface & timeout that the normal Alexa skills use. The color fidelity of the Echo Buttons could be better; darker colors are particularly hard to show on them so they have to be left out of the color patterns. While adding APL, I struggled with the APL AlexaHeader not allowing the font color to be changed. I wanted the screen to be bright and engaging so I didn't want to use the dark theme. I solved the problem by including a dark element behind the header and customizing the background for each device. Accomplishments that I'm proud of Color Lab had more 5 star ratings than the Echo Button Simon game for several months during 2018. Color Lab was featured on the Alexa Skills Review Podcast (now A Few Minutes in Voice ). What I learned APL is relatively easy, though the documents add quite a bit of actual code. The tools for APL are so much better than the tools for Echo Buttons were when they were new. What's next for Color Lab Additional Game Modes: Color Mixer: 3 buttons will be red, yellow, and blue. Pushing them will add that color to a 4th button. Pushing the 4th button will have alexa say the name of the color on that button. See the Color: Children would say a color and the device could show the color. This might extend the appeal of the skill because currently buttons are required. Color Quiz: Children will be asked what color different things are and they will answer by pushing the button with that color on it. Ability to select game by touching the device instead of providing an audio response to the skill <div