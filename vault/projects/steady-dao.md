---
slug: "steady-dao"
url: "https://devpost.com/software/steady-dao"
title: "Steady DAO"
hackathon: "Chainlink Fall Hackathon 2021"
organization: "Chainlink"
winner: true
words: 302
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
---

# Steady DAO

> Steady DAO is a play to earn dApp & game with UFO, create a simple synthetic that is free from liquidation. Based on any Chainlink price feed anyone can create a Steady and a Leveraged Token(Elixir).

[Devpost](https://devpost.com/software/steady-dao) · hackathon [[Chainlink Fall Hackathon 2021]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: video_visual</sub>

**stack** chainlink, gamemaker, moralis, polygon, solidity, ufo

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for steady dao

## Body

GIF Welcome screen logo GIF in-game screenshot Inspiration Inspiration for Steady DAO came from trying to do a simple easy to use leveraged and stable pair for HODLERS. Most leveraged tokens have a liquidation event, we wanted to create something really simple. What it does The problem it solves is that if I am HODLer and I want to keep the X% of my asset at its current market value in the underlying itself without bothering about the volatility there is no certain way to do it. The Steady DAO project ** splits and merges tokens ** , basically creating a stable asset and a leveraged asset for any asset that has a ** chainlink price feed ** . eg. GOLD tokens, SAND etc. There is no liquidation event, so only split and hold assets that you trust :-) . The Elixir's (leveraged tokens) do not have a liquidation event nor a rebase mechanism. They simply float based on market dynamics. How we built it We used gamemaker studio to create a gamified interface, we used moralis for login and event notifications, chainlink keepers, feed and api calls. We managed to integrate the UFO token by adding in a two way swap between UFO and Steady DAO tokens. Challenges we ran into Gamemaker studio and integration with Moralis and Websockets. Converting code into a factory form and integration. We also could not figure out the UFO documentation on polygon and chainlink api's were missing in polygon as well. Accomplishments that we're proud of The game interface, the hours spent on writing tests and making sure the project works well. What we learned Math, Integration of games and economics, usage of chainlink to make it all link up together. What's next for Steady DAO Production in February! Steady DAO token mint ! <div