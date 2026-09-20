---
slug: "don-t-touch-the-thermostat"
url: "https://devpost.com/software/don-t-touch-the-thermostat"
title: "Don't Touch the Thermostat"
hackathon: "Hack Reddit 2025"
organization: "reddit"
winner: true
words: 675
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/civic_government"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Don't Touch the Thermostat

> A skill-based opinion voting game for Reddit. Touch the thermostat while dad isn't looking

[Devpost](https://devpost.com/software/don-t-touch-the-thermostat) · hackathon [[Hack Reddit 2025]]

## Facets

**domain** [[civic_government]] [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]] [[web_dom]]

**stack** css, devvit, html, javascript, ts

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for don't touch the thermostat

## Body

title message from dad end screen dad watching you dad watching tv Inspiration People love to be right. Things like "actually being right" or "personal preference" matters very little in the face of any leverage they can get to prove themselves right. Inspired by classics like "Red light, green light" and "dancing while the teacher doesn't know", I made a skill-based opinion voting game where being right is a skill issue. For the theme, I used the old battle of "don't touch the thermostat" because my dad told me I couldn't touch the air conditioner button or turn on the light at the back of the car while driving and I guess I needed closure for that. What it does The game lets users post their own game of "Don't Touch the Thermostat" with their opinion on the line. Any user can participate in the game to either upvote or downvote the opinion. During the game, you can upvote/downvote as much as you want while dad is watching the TV. But, you have to be careful as your dad will chase you if he sees you touching the thermostat. Your votes are added to the pool of votes in the server, and if you become the top 3 contributor for upvoting/downvoting, you get to be on the leaderboard for that faction. How we built it The game was built using Devvit webview. I used css and html to build out the game logic and game scene, and used Redis for storing votes and leaderboard data. To draw the assets, I used clip studio paint, and I used pen and paper for designing the game. Challenges we ran into The biggest challenge was learning to use CSS and html on top of Devvit. Surprisingly Devvit was pretty easy to use, but finding ways to place the objects where I want with CSS and html was hard especially coming from game engines where coordinate positioning is the norm. Also, because I was new to using Devvit, I had to restart my project to use webview after 3 days of work because what I wanted to do required the additional control. Making that decision was hard because it hurt to start again. Accomplishments that we're proud of I gave myself 9 full days to make this whole thing, planned out what I would do on each day and set some stretch goals. I actually followed this schedule, met couple stretch goals, and I am submitting the project without pulling an allnighter. I feel good about getting the hang of guessing what I'm capable of in a certain amount of time. I'm especially proud of learning css and html (having it click) within the timeframe. It really gave me confidence in my ability to learn new tech things. What we learned On top of the new languages learned, I learned about what kind of games and experiences are possible using Devvit. While some ideas I had were definitely too big and complicated to be designed/coded/tested/polished in the timeframe of the jam. I might explore the Devvit documentation further to see if I can make a more permanent mmo webgame taking advantage of reddit's community layout. (something something mmo continental horse racing adventure game or browser games) On the art side, I learned that using tones (dots) and overlaying with a color can give a real nice feel for the texture in pixel art. I might use that in my later games and experiment more with it on my non-pixel arts too. What's next for Don't Touch the Thermostat Couple stretch goals I want to implement I want to give the option for image-based opinions (so users can put up an image of a waifu and vote on it or something) and I want to give the option for replacing the 'dad' in the game with their own character (like a waifu). Besides that, I might want couple days away from it to come back with a fresh pair of eyes to see if there's more places to polish <div