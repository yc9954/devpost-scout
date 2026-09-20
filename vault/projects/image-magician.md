---
slug: "image-magician"
url: "https://devpost.com/software/image-magician"
title: "Image Magician"
hackathon: "Reddit Mod Tools and Migrated Apps Hackathon"
organization: "reddit"
winner: true
words: 343
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# Image Magician

> A port of the MAGIC_EYE_BOT repost moderation bot to the new devvit platform.

[Devpost](https://devpost.com/software/image-magician) · hackathon [[Reddit Mod Tools and Migrated Apps Hackathon]]

## Facets

**substrate** [[video_visual]]

**stack** jimp, redis, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that i'm proud of
- what i learned
- what's next for image magician

## Body

Settings page Inspiration I've always been inspired by kinship with my fellow moderators, people who I see working so tirelessly to make communities run. Years ago a friendly mod reached out to see if I could widen my repost detector to include their subreddit, and from that point it grew into a full project to help other moderators run their subreddits efficiently. What it does It detects image/video reposts, and more importantly helps moderators deal with the situation. How I built it The original bot had years of feature requests and feedback. This was a port of those features, but also a reimagining with the learnings of what didn't work as well as it could have. This was not an AI port, as improving the existing bot was part of the goal. While some code was written with my scant free tokens, AI mainly helped with understanding the devvit platform. Challenges we ran into Time! Due to personal reasons I could only start on this in the last week so late nights were involved, but it was a fun challenge to get it done. Accomplishments that I'm proud of The Redis data limit that stumped me initially, as I wanted this to be a contained bot that doesn't rely on external services. The problem: If image hashes (A4B920E3F5C7D816) have randomly differing characters, how can you find close matches without extracting all of the hashes? I realized I could solve this by splitting the hash into small segments and creating a custom index. The key knowledge was understanding the relationship between the segment size and hamming distance it would allow matches from. tl;dr the bot is very efficient at storing and retrieving data. What I learned The devvit team has done an amazing job with this platform. Hats off to them, it's quite fun to develop on. What's next for Image Magician I'll be reaching out to all of the MAGIC_EYE_BOT users to migrate, and for the first time in a while taking new feature requests (of which there is no shortage of). <div