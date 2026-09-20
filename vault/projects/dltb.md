---
slug: "dltb"
url: "https://devpost.com/software/dltb"
title: "dltb"
hackathon: "AWS Deep Learning Challenge"
organization: "Amazon"
winner: true
words: 130
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "substrate/video_visual"
---

# dltb

> Using UNET for lung x-ray image segmentation. This is developed as an accompaniment of a TB classification model.

[Devpost](https://devpost.com/software/dltb) · hackathon [[AWS Deep Learning Challenge]]

## Facets

**domain** [[health_clinical]]
**substrate** [[video_visual]]

**stack** amazon-web-services, python, pytorch

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dltb

## Body

Inspiration Trying to develop an open-source tuberculosis solution for anyone who wants to use it. What it does Acts as part of a pipeline, where once an image is diagnosed as having TB an extra step is to also provide a segmentation mask for the x-ray image. How we built it Challenges we ran into Getting it to train on HPUs was a bit challenging I always seem to break something, including my entire VM. The solution was mainly to destroy the instance and recreate it again and everything would be working as intended then after a few hours same cycle. Accomplishments that we're proud of Actually getting the model to train. What we learned Implementing Unet's, first time doing it. What's next for dltb Build a QT interface <div