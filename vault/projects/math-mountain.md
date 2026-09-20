---
slug: "math-mountain"
url: "https://devpost.com/software/math-mountain"
title: "Math Mountain"
hackathon: "Alexa Skills Challenge: Beyond Voice"
organization: "Amazon"
winner: true
words: 862
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "domain/labor_employment"
  - "substrate/document_pdf"
---

# Math Mountain

> A math climbing challenge - can you make it to the top?

[Devpost](https://devpost.com/software/math-mountain) · hackathon [[Alexa Skills Challenge- Beyond Voice]]

## Facets

**domain** [[labor_employment]]
**substrate** [[document_pdf]]
  <sub>weak: structured_db</sub>

**stack** apl, google-spreadsheets, voiceflow

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for math mountain

## Body

Gameplay View You Win! Math Mountain Skill Icon Inspiration The idea for Math Mountain first came to me in early March after reading the Hobbit. I thought the theme of climbing a mountain would make for a fun Alexa Skill, so I put together an outline for a game that would increase in difficulty and reflect the sounds of nature & hiking. Originally the game was going to be voice only. However that plan changed by mid March when everyone went into lockdown due to Covid-19. With my extra time at home, I dove into learning more about APL. While things have been stressful & odd this year, my extra time off has given me the chance to fine-tune the user experience - both in sound & visuals - and really make Math Mountain what it is today. What it does The rules are fairly simple - answer 7 math questions correctly in a row to reach the summit of Math Mountain. The game starts off easy, and gets harder the higher you climb. If you get a question wrong you can use a lifeline. You're given 3 free lifelines to help with your journey, and you can purchase additional lifelines through two ISP products: the Starter Pack (3 extra lifelines) and the Mega Pack (10 extra lifelines). The game also includes a monthly leaderboard. When you makes it to the top of Math Mountain you will start a win streak. The game uses APL for Audio to enhance the soundscape. Certain dialogue, such as Alexa explaining the rules, asking a question, congratulating the winner, etc. includes background music & sound effects to a create a higher quality/ immersive experience. The addition of APL-A (using birds chirping, flowing streams, wind, thunder, etc.) has improved the gameplay and strengthened the sense of climbing a mountain. How I built it The game is built on Voiceflow. I used the APL Authoring tool for editing & testing my APL documents. For the animations, I used this amazing library of APL transitions: https://github.com/arjun-g/apl-transitions The live leaderboard & questions (categorized by difficulty on a scale of 1-7) are stored in google sheets. All other assets are stored in s3. Challenges I ran into There were a lot. I've created skills using APL before, but nothing this intricate. This is the first time I've used animations and APL for Audio, so naturally there were a few frustrating moments. Most of my challenges were minor, such as fixing APL mistakes, volume adjustments, random missing text reprompts, etc. the list could go on & on. I think my biggest challenge was making sure every element (dialogue, SFX, layout, etc.) within the game served a purpose. It's relatively easy to add fun animations or epic background music, but for a high quality experience it requires a great deal of planning, decision making, and a whole lot of testing. Accomplishments that I'm proud of I'm really proud of the time and effort I've put into this game. This is by far the most time I've spent on a single Alexa skill, and it's been well worth it. I love that so many people are using the leaderboard and enjoying the game on a daily basis. Someone said this game is a great way for kids to break up the monotony of virtual learning. So I'm really proud to have provided a relaxing/educational game that kids and families can enjoy during these difficult & weird times. What I learned I learned a lot more about APL. I've wanted to add APL for Audio to Math Mountain for a while now, but this competition was the motivation I needed to learn how. There is a lot of awesome documentation out there, and I have to say, there are some incredible people in the voice community that are doing some amazing things with APL. When I've needed help or advice, there is always someone more than happy to share their knowledge. It's incredible. I also learned the importance of quality beta testing. I had several people test and improve the user experience. Through several iterations, Math Mountain turned into something cooler than I initially thought possible. What's next for Math Mountain I'm planning on adding another ISP product called the "Super Mega Pack," which will include 25 additional lifelines. This product will be helpful for the hardcore gamers who are trying to rank high on the leaderboard. I'll be adding TouchWrappers in the near future too. Voiceflow user events are in beta (and still working out the kinks). I have all of my APL docs with TouchWrappers 100% ready to go, I'm just waiting for a few bugs to be worked out. With the addition of APL touch, you can press a button to start the game, use lifelines, see ranking, etc. And based on some user feedback, I'm planning on adding more challenging options for advanced players. The game will probably have tiers, where you can choose from easy, medium, or hard. I definitely will continue improving the quality of the questions, and I'm seriously considering hiring a writer to help. My goal over time is to keep elevating the Math Mountain experience. <div