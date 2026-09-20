---
slug: "daily-dungeon"
url: "https://devpost.com/software/daily-dungeon"
title: "Daily Dungeon"
hackathon: "Reddit Games and Puzzles Hackathon"
organization: "reddit"
winner: true
words: 398
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/civic_government"
  - "domain/supply_logistics"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Daily Dungeon

> Similar to Twitch Plays Pokémon, it’s Reddit Plays Dungeons & Dragons! An entire subreddit acts as a single main character, and every day the top-upvoted comment decides that character’s next action

[Devpost](https://devpost.com/software/daily-dungeon) · hackathon [[Reddit Games and Puzzles Hackathon]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[civic_government]] [[supply_logistics]]
**substrate** [[structured_db]] [[video_visual]]

**stack** chatgpt, firebase, reddit, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- what's next for daily dungeon

## Body

Use the Reply with Dice Roll comment action to show others your daily roll! Inspiration I've been a Dungeon Master for Dungeons & Dragons games with my friends for years. Last year, I tried something called "Gwamp's Quest" on Reddit—a daily choose-your-own-adventure series in r/comics. It was received enthusiastically, and I realized this approach had more potential. Inspired by "Twitch Plays Pokémon," I wanted to bring that communal, democratic decision-making spirit to the world of tabletop role-playing. Enter Daily Dungeon , where the entire subreddit is the hero, guiding each day’s action through reddit comments. What it does Daily Dungeon transforms a subreddit into a single adventurer’s mind. Each day, a new scenario is presented—a perilous cavern to explore, a mysterious stranger to interrogate, or a treasure chest to open. The community votes through comments, and the top-voted comment becomes the hero’s next step. The result is a collaborative, emergent narrative where no single person controls the journey, but everyone contributes. Users also have a daily roll , where they roll a d20 (20-sided die) that accompanies their day's comment. This dice roll determines the success (or failure!) of their comment's action. There's also a comment menu action that users can select to have the app comment their daily dice roll in response to their own comments. How I built it I built Daily Dungeon using Reddit's native Interactive Post + Blocks UI. As such it integrates seamlessly into subreddits without a hitch, scaling to both mobile and desktop device sizes. It also supports both dark and light mode. The daily text is stored in a Firebase database instance that the app fetches when a post is created. Right now I have a ChatGPT instance that creates backup text for the next day's post automatically, but I'm personally curating the copy myself. What's next for Daily Dungeon First, I'd like to run Daily Dungeon in r/dungeonsanddragons or r/dnd. I think the game has so much potential for fun in either of these communities. Moving forward, I plan to enhance the experience with: A dedicated character stats page that updates daily, tracking health, abilities, and inventory. Daily images or illustrations to bring scenes and encounters to life visually. Additional voting methods beyond comments, such as polls or multiple-choice options, to streamline decision-making and encourage even broader participation. A Gwamp's Quest offshoot using the Daily Dungeon platform in r/comics <div