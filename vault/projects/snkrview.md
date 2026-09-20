---
slug: "snkrview"
url: "https://devpost.com/software/snkrview"
title: "SNKRView"
hackathon: "Hack the North 2021"
organization: "Techyon"
winner: true
words: 430
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# SNKRView

> The ultimate fashion tool

[Devpost](https://devpost.com/software/snkrview) · hackathon [[Hack the North 2021]]

## Facets

**domain** [[education]]
**substrate** [[structured_db]] [[video_visual]]

**stack** colab, rune, swift, tensorflow, xcode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for snkrview

## Body

Inspiration We all tell a story with our clothing. Whether our garments represent a cultural significance or simply a style that we enjoy, we share a side of ourselves with the world around us. Every story that reaches its peak is built from the bottom up; Our stories begin with our sneakers . Fashion is about an exchange of what we hold dear, and as we've all known since elementary school, sharing is caring. We built this app to better facilitate the exchange of sneaker info so we can all up our shoe game. What it does By taking a photo or selecting a gallery photo of a shoe, SNKRView uses machine learning to detect the model of the sneaker. Currently, our application supports Jordan's only; fear not , the list of supported shoes will grow substantially within the next few weeks. How we built it This project was split up into several parts: We first scraped Bing for images of Jordan's 1-12s, and compiled these images into datasets. We then trained a pre-processed TensorFlow Lite model on this dataset, which we used as a component of a Rune pipeline to accept images and output a prediction of the sneaker. We then designed an IOS application on XCode using Swift and then proceeded to deploy the encoded Rune pipeline onto Flutter which we then integrated into our IOS code. Challenges we ran into There were many difficulties along the way. The biggest would probably be the lack of sleep. Apart from the obvious, we had difficulties creating a dataset that was expansive enough to allow the model to reach a certain level of accuracy, yet small enough to not have the model spend precious hours in training. We also had some difficulties creating the pipeline, as we were not initially familiar with Rune's infrastructure. Finally, we had issues deploying our Rune pipeline onto Flutter to be used in our IOS application. Accomplishments that we're proud of Creating our first mobile app. MACHINE LEARNING THINGS! Using Rune. We are pretty proud of ourselves. What we learned We learned a lot . Tensorflow, Rune, Swift, XCode, and the occasional terminal command. We learned more about transfer learning, as well as the process of mobile development. I think it's safe to say that I am going to dream in code tonight. What's next for SNKRView Big things. We plan to slowly train our model to recognize more shoes until it spans every single sneaker ever made. Or, maybe just Nike shoes in the near future. We've got a long way to go! <div