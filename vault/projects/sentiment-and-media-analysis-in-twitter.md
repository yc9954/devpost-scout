---
slug: "sentiment-and-media-analysis-in-twitter"
url: "https://devpost.com/software/sentiment-and-media-analysis-in-twitter"
title: "Sentiment and media analysis in Twitter"
hackathon: "The Postman API Hack"
organization: "Postman"
winner: true
words: 224
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/video_visual"
---

# Sentiment and media analysis in Twitter

> Twitter sentiment analysis allows you to keep track of what’s being said about your product or service on social media, and can help you detect angry customers or positive mentions.

[Devpost](https://devpost.com/software/sentiment-and-media-analysis-in-twitter) · hackathon [[The Postman API Hack]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[video_visual]]

**stack** azure, javascript, postman, slack, teams

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Inspiration I wanted to build solution that help developers to use AI services and automate the way team can receive insights from social media in teams chats like Microsoft Teams and Slack using Postman Collections and Monitors. What it does Retrieves 100 recent tweets along with images based on provided query. Describes what is on the images using Microsoft Azure Computer Vision service. Detects in what language these tweets are written using Microsoft Azure Language Detection service. Retrieves sentiment of tweets using Microsoft Azure Text Analysis service. Combines result in a report. Sends report to Slack channel via webhook. Sends report to Microsoft Teams channel via webhook connector. How we built it Using Postman Collections, Pre-request scripts, Tests, Workflows, and Postman Monitor. Challenges we ran into At one point I wanted to use Postman Visualization of API Data ( https://www.postman.com/api-visualizer/ ) for visualization, but it seems that it's not supported when running collections. Some of the API require multiple calls to process the data. That's why I've used a combination of pre-request scripts and tests with workflows to mitigate that. When using free tiers of Microsoft Azure Cognitive Services some of the requests need to be throttled. Accomplishments that we're proud of Fully automated twitter sentiment reports in Microsoft Teams and Slack What we learned Postman Collections Pre-request scripts Tests Workflows Postman Monitor <div