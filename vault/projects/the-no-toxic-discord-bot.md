---
slug: "the-no-toxic-discord-bot"
url: "https://devpost.com/software/the-no-toxic-discord-bot"
title: "The No Toxic Discord Bot"
hackathon: "HackSwift 2024"
organization: "hackswift"
winner: true
words: 319
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/structured_db"
---

# The No Toxic Discord Bot

> A Discord Bot that uses text classification AI to maintain community wellness in a Discord server.

[Devpost](https://devpost.com/software/the-no-toxic-discord-bot) · hackathon [[HackSwift 2024]]

## Facets

**substrate** [[structured_db]]

**stack** discord, discordjs, flask, huggingface, javascript, node.js, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for the no toxic discord bot

## Body

Inspiration As a result of more people using the internet, our world has become more connected then ever before. Expressing an idea or an opinion is now easier than ever. Unfortunately, this also allows for toxic messages to be easily spread across social media, which can mentally harm people in the form of cyberbullying. What it does We built the Non Toxic Discord bot in order to prevent the spread of hateful messages before it goes out of hand. By using AI text classification, it can moderate discord servers just as well as a human, 24/7, without any interruption. How we built it We trained a well-known sentimental analysis model called DistilBERT with numerous examples of both toxic and non-toxic messages found in the Wikipedia Toxic Comments dataset. After training the model, we integrated it with a DiscordJS bot using Flask, allowing for the discord bot to call the AI Model whenever a user sends a message in a discord server. Challenges we ran into Since it is our first time using AI, we struggled to understand how to use and train a model to classify text. However, after a long night of Stack Overflow pages and Google searches, we felt confident enough to effectively train DistilBERT to recognize toxic messages. Accomplishments that we're proud of We are proud of the discord bot that we made and we hope that even after this hackathon, it can make a lasting impact on the online community. What we learned We learned how to train an AI model and finetune it for our purpose, which is toxic message detection. We also learned how to create our very own discord bot and use it on a discord server. What's next for The No Toxic Discord Bot We hope that this bot can actually be used in large servers in order to protect their community members from potentially harmful or excessively toxic content. <div