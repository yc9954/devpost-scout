---
slug: "bga"
url: "https://devpost.com/software/bga"
title: "Board Game Atlas"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 142
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "substrate/structured_db"
---

# Board Game Atlas

> Query Board Game Atlas to help suggest a boardgame, then find the best price for the top suggestion.

[Devpost](https://devpost.com/software/bga) · hackathon [[The Postman API Hack]]

## Facets

**substrate** [[structured_db]]

**stack** javascript, lodash, postman

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into

## Body

Inspiration Choosing the right boardgame to play is not always straightforward particularly if you have large or small groups, or have a limited time to play. Board Game Atlas has an extensive game database that can help find an appropriate game, and even find the online stores with the best prices. What it does Queries Board Game Atlas for the most popular games that match your criteria for player count and maximum game time. Shows the prices for online store for the first game. The game names and price information is written to the Postman console. How we built it Postman collection queries with some post-request scripts to write information to the console and store the game_id in the environment for the price query. Challenges we ran into This was my first time using lodash to work with the query responses. <div