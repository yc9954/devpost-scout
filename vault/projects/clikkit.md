---
slug: "clikkit"
url: "https://devpost.com/software/clikkit"
title: "Clikkit"
hackathon: "Hack Reddit 2025"
organization: "reddit"
winner: true
words: 370
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/agriculture_food"
  - "user/frontline_worker"
---

# Clikkit

> a collaborative MMO clicker game based on Reddit platform

[Devpost](https://devpost.com/software/clikkit) · hackathon [[Hack Reddit 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[agriculture_food]]
**user** [[frontline_worker]]

**stack** blocks, css, devvit, javascript, redis, webviews

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clikkit

## Body

Inspiration The inspiration for Clikkit came from classic clicker games like Cookie Clicker, but with a social twist based on Reddit's community structure. We wanted to create a game that would bring subreddit users together through a shared, collaborative experience. What it does Clikkit is a massively multiplayer online clicker game that attaches to subreddits. Community members click on a shared kitty to increase their subreddit's score, competing against other communities (coming soon...) on Reddit. The game contains: Visual and sound effects Skill system where users can specialize as either "Farmers" (focusing on passive income for the community) or "Warlords" (enhancing their personal clicking power) Score multiplier which increases on every daily game reset Real-time updates allow users to see others' contributions almost instantly. How we built it Clikkit is using a lot of different parts of Devvit platform, such as Blocks, Web Views, Realtime, Schedulers and Redis for storing game data. Web View part of the game is based on Javascript and CSS Challenges we ran into Some of the key challenges we faced included: Understanding avalability of Redis in different contexts of Devvit Decisions on which path to take in gameplay mechanics was pretty hard, especially considering that we had a limited amount of time invested into this project, and Devvit Redis missing incrByFloat Creating and testing a design that works well on both desktop and mobile Accomplishments that we're proud of We're particularly proud of: Developing satisfying visual and interactive elements that make clicking feel rewarding Implementing a skill system that allows for different play styles Designing a system that works equally well on desktop and mobile devices Creating a game that's simple to understand but offers strategic depth What we learned How to effectively use Devvit's features for minimalistic real-time MMO game experiences Methods for creating engaging visual feedback with minimal as possible performance impact Approaches to creating responsive designs that work across different devices What's next for Clikkit Future plans, which we are currently thinking of: Implement a global leaderboard to track top-performing subreddits Listen to players feedback on possible gameplay improvements Develop achievement system based both on players and subreddit communities Add customization options for moderators to theme the game to their subreddit <div