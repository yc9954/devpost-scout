---
slug: "c-lee"
url: "https://devpost.com/software/c-lee"
title: "c-lee"
hackathon: "HackZurich 2021"
organization: "HackZurich"
winner: true
words: 189
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/media_journalism"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# c-lee

> C-lee allows people to watch funny internet content while recording theirselfes by video. Our AI predicts how real or fake the laughter is. By that we can make social media more authentic and real.

[Devpost](https://devpost.com/software/c-lee) · hackathon [[HackZurich 2021]]

## Facets

**domain** [[media_journalism]]
**substrate** [[structured_db]] [[video_visual]]

**stack** keras, python, react, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what's next for c-lee

## Body

Inspiration Real laughing is a great indicator of our amusement. In order to assess the quality of social media content, it would be great to analyze the user's emotions. What it does Our web application allows users to watch funny internet content in a special way. While watching, our application can record the user's reactions by video. A deep learning model predicts how real or fake our laughing was. How we built it We created a large image-based dataset extracted from TikTok videos and we labelled them manually. Using that data, we trained a deep learning model with Python, TensorFlow, and Keras. We integrated that into a web application that runs even on smartphones and tablets. Challenges we ran into Deep Learning models need a huge data basis and very long time to train. It was difficult to develop an architecture that archives a high accuracy with the limited amount of data that we could annotate manually. What's next for c-lee We would like to further improve our deep learning model and integrate it into a social media app that some of us are currently developing: syly.app . <div