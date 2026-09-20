---
slug: "auto-stackoverflow-search-bot"
url: "https://devpost.com/software/auto-stackoverflow-search-bot"
title: "Auto Stackoverflow Search Bot"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 175
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
---

# Auto Stackoverflow Search Bot

> A Bot to Help Developers to Debug Quickly & Easily !

[Devpost](https://devpost.com/software/auto-stackoverflow-search-bot) · hackathon [[The Postman API Hack]]

## Facets

**domain** [[developer_tools]]
**user** [[developer]]

**stack** flask, postman, python

## How they structured the write-up

- what we learned
- what's next for auto stackoverflow search bot

## Body

Introduction A slack app to help developers in the quick error debugging by auto searching. Post an Error in a specified slack channel & return the top results from Stackoverflow.com with links. Setup: Create a new environment with following variables. stackExUrl ( https://api.stackexchange.com/2.2 ) SlashServerUrl (deploy this Flask code) slackWebhookUrl SlashServerUrl : Create a new slack app & Slash command. Give the Endpoint IP, port while creating the slash command. refer here sample endpoint using python-flask SlackWebhookUrl : Slack allows you to generate incoming webhooks for your team using which you can send a message to a specific channel or user. Go to Slack to learn more about how you can generate one. Once you have all these three, you can add them to the attached environment and your collection is ready for use. A sample look something like this: A VSCode extension/ Jupyter extension of this will be helpful. What we learned postman features, slack bot integrations, jupyter extensions What's next for Auto Stackoverflow Search Bot Converting to Jupyter & VS code extensions <div