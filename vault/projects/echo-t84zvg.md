---
slug: "echo-t84zvg"
url: "https://devpost.com/software/echo-t84zvg"
title: "Echo"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 251
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
---

# Echo

> Echo is a YouTube comment sentiment analyzer that helps creators quickly understand audience reactions by classifying comments as positive, negative, or neutral.

[Devpost](https://devpost.com/software/echo-t84zvg) · hackathon [[DSH Hacks V1]]

## Facets


**stack** fastapi, python, react, vader

## How they structured the write-up

- about the project

## Body

About the Project I built Echo , a YouTube comment sentiment analyzer, because I was interested in how raw audience feedback could be turned into something more meaningful and measurable. On platforms like YouTube, creators often receive hundreds of comments, and while those comments contain valuable opinions, they can be difficult to sort through manually. I wanted to create a tool that could simplify that process and show overall audience reaction in a clear way. Through this project, I learned more about natural language processing , sentiment classification, and how text data can be cleaned and analyzed. I also gained experience working with APIs, handling user input, and designing a project that turns unstructured data into useful insights. To build the project, I used the YouTube Data API to collect comments from videos, then processed the text and ran it through a sentiment analysis workflow that labeled comments as positive, negative, or neutral. From there, I summarized the results so a user could quickly understand how viewers responded. In simple terms, the sentiment score can be thought of as: $$ \text{Sentiment Ratio} = \frac{\text{Positive Comments}}{\text{Total Comments}} $$ One of the biggest challenges was handling the messiness of real comments. Many comments include slang, emojis, sarcasm, spam, or very short phrases that are difficult for a model to interpret correctly. Another challenge was making sure the project remained simple and understandable while still producing meaningful results. Overall, this project helped me better understand the connection between data, language, and decision making. <div