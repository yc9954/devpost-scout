---
slug: "xplore-suezr3"
url: "https://devpost.com/software/xplore-suezr3"
title: "Xplore"
hackathon: "Global PyTorch Summer Hackathon"
organization: "Facebook"
winner: true
words: 387
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Xplore

> XPlore is a tool designed for understanding, analyzing and annotating medical images like Xrays ,MRIs, CT scans. The intended audience are both data scientists and medical professionals.

[Devpost](https://devpost.com/software/xplore-suezr3) · hackathon [[Global PyTorch Summer Hackathon]]

## Facets

**user** [[researcher]]
**substrate** [[structured_db]] [[video_visual]]

**stack** dicom, docker, fastai, images, medical, pytorch, vue

## How they structured the write-up

- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what's next for xplore
- demo
- code

## Body

UI Home We can examine by applying image filters. What it does XPlore is a tool designed for understanding, analyzing and annotating medical images like Xrays ,MRIs, CT scans. The intended audience are both data scientists and medical professionals. Typically medical images are stored in DICOM format. Our tool can read both meta data and images from dicom files and render them appropriately. Lets consider two different user cases. From datascientist perspective. As datascients we want to understand how our model is performing. For example we want to look at different images and see what our model predicts. We often do this by sampling few images and visualize them in jupyter notebooks. This is a slow and tedious process .So we examine very few images. We designed the tool to easily load any dataset and the corresponding model. After adding the dataset we can quickly see all the images in our dataset and understand how our model is performing. We can also check images that are similar to the image we are analyzing. Often this gives us a clue about our model behaviour like overfitting or any inheriten biass it learnt etc. Once the model is debugged, we want to deploy it and share it with medical professionals for the review. From medical professional perspective. Let’s say you are looking at an X-Ray and deciding if it has pneumothorax or not. Some X-Rays are easier to analyze and some are tricky. Normally we look at similar X-Rays and decide on that. Some times it is easier if we apply various image filters. Each filter highlights some aspects of the image. How I built it The UI is written in vue js. The backend is implemented using fastapi. The models are built on pytorch and fastai. The files are indexed using faiss library. Challenges I ran into Time :) Accomplishments that I'm proud of It provides an easy and fast way to visualize the medical datasets. There is no opensource tool i am aware of that does this. What's next for Xplore Adding more features like annotations and adding support for model additions using UI. Now some of the operations needs to be done using UI and some needs to be done using command line. I would like to unify these. Demo http://148.251.87.118:8080 Code https://github.com/sairahul/xplore-ui https://github.com/sairahul/xplore-backend https://github.com/sairahul/notebooks/blob/master/Siamese_Network_with_Triplet_Loss.ipynb <div