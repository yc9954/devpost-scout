---
slug: "reddit-football-prediction"
url: "https://devpost.com/software/reddit-football-prediction"
title: "Reddit Football Prediction"
hackathon: "AWS Deep Learning Challenge"
organization: "Amazon"
winner: true
words: 136
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# Reddit Football Prediction

> Predicting the result of football matches based on the top comment of the Pre Match Threads in the "RedDevils" subreddit.

[Devpost](https://devpost.com/software/reddit-football-prediction) · hackathon [[AWS Deep Learning Challenge]]

## Facets

**substrate** [[structured_db]]

**stack** habana, pytorch, transformers

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for reddit football prediction

## Body

logo training Inspiration I'm a big fan of the premier league, specifically, the red devils, Manchester United so I wanted to see whether fans in a subreddit can predict the result of match. What it does It is a fine tuned distilbert model for text classification trained on a Gaudi HPU. In this case we classify the top level comment in the Red Devils subreddit with the result as the target. How we built it Using Pytorch and transformers Challenges we ran into Curating the dataset. The dataset was small and I had to input the results of the games manually Accomplishments that we're proud of Developing a simple baseline model What we learned Using Habana for Pytorch What's next for Reddit Football Prediction Collect more data and perhaps use this model on Twitter data. <div