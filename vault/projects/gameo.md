---
slug: "gameo"
url: "https://devpost.com/software/gameo"
title: "Gameo"
hackathon: "2020 Facebook Developer Circles Community Challenge"
organization: "Facebook"
winner: true
words: 334
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Gameo

> There's a Game for Everyone

[Devpost](https://devpost.com/software/gameo) · hackathon [[2020 Facebook Developer Circles Community Challenge]]

## Facets

**substrate** [[structured_db]] [[web_dom]]

**stack** flask, javascript, python, pytorch, rawg, react, redux, twitch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gameo

## Body

Inspiration Games are a form of entertainment and pleasure to many of us. According to a market study, the global video game industry is valued at USD 151.06 billion in 2019 and is expected to grow at a Compound Annual Growth Rate (CAGR) of 12.9% from 2020 to 2027. This means that there will be more selection of games for us. For gamers and for people who are not familiar with video games, it can be daunting to find and choose a game that they will enjoy. Gameo aims to become the number 1 game recommendation engine for anyone to use. At Gameo, we believe that there is a game for anyone. Whether or not you have played video games before, Gameo will have a game for you. What it does Main Features See trending games based on how popular it is on Twitch View a personalized recommendation list of games based on games rated Add games to your library and wish list Games that are rated will have a rating of 1-10, which will be used to train the model Modify the number of recommendations given in the settings page How we built it Resources Gameo uses the following resources: Twitch API, which allows Gameo to fetch the newest and trending games. Official documentation can be found here. RAWG API, which allows Gameo to access detailed information for each game. Official documentation can be found here. Metacritic Game Dataset and Metacritic User Comments Dataset, which are used for training the model can be found here. Tech Stack Languages: Python, JavaScript, HTML, CSS Frameworks: ReactJS, Python Flask Database: MongoDB APIs/Other: Twitch API, RAWG API, Firebase Authentication Challenges we ran into Learning and integrating PyTorch into our Flask and React App Accomplishments that we're proud of A fully working Game Recommendation Platform for anyone! What we learned Reommendation engine algorithms and how they work What's next for Gameo Improving the current recommendation algorithm and filtering games through its metadata such as platform and genres. <div