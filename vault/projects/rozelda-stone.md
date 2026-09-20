---
slug: "rozelda-stone"
url: "https://devpost.com/software/rozelda-stone"
title: "Rozelda Stone"
hackathon: "Pygames"
organization: "Microsoft"
winner: true
words: 280
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "user/educator_student"
---

# Rozelda Stone

> Zelda x Rosetta Stone x Typing game

[Devpost](https://devpost.com/software/rozelda-stone) · hackathon [[Pygames]]

## Facets

  <sub>weak: education, finance_payments</sub>
**user** [[educator_student]]
  <sub>weak: geospatial</sub>

**stack** gtts, pygame, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what i learned

## Body

Foreword: Just to be clear, I only hacked this together over one weekend and built on top of an existing project which I followed the youtube tutorial for the game logic, graphics, and music; so most of the credit goes to them (see readme). I did the least amount to get the Minimum Viable Product. The features I implemented were: Typing mandarin characters to attack Mastery for repetitions && Hint system Changed controls -> UpLeftDownRight -> ESDF to keep left pointer finger on f: ready to type Audio outputs chinese as you get a new challenge word to type Setup: git clone https://github.com/quanconnect/RozeldaStone cd code python3 -m venv venv source venv/bin/activate pip install requirements.txt python3 main.py Controls: (all keyboard) up: e down: d left: s right: f ctrl: magic attack Current limitations: As a MacOS guy: the game lacks windows & linux language support Needs to type fast, otherwise would need to slow the frames down FPS= to make it easier typing impedes movement,aim && viceversa Need to preconfigure chinese traditional within "MacOS language input" before playing Future goals: support other languages remote datastore: for leaderboards, translations (eg redis+dynamodb) multiplayer PvP* is a stretch goal support DLC/mods on user generated maps (builders), user generated translations/storylines (teachers) Inspiration Language learning without immersion is difficult. What it does Gamifies learning languages with audio pronunciation How I built it Keeping the mindset of an extendable engine for future languages & user generated content. Challenges I ran into plenty see current limitations Accomplishments that we're proud of Doesn't segfault & crash upon voice translation What I learned Learning foreign languages with time pressure is fun & hard Gamifying the process keeps me engaged <div