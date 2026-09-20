---
slug: "gan-music-generator"
url: "https://devpost.com/software/gan-music-generator"
title: "GAN Music Generator"
hackathon: "AngelHacks 2.0"
winner: true
words: 359
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/video_visual"
---

# GAN Music Generator

> A Generative Adversarial Network trained on EDM MIDI files to create music.

[Devpost](https://devpost.com/software/gan-music-generator) · hackathon [[AngelHacks 2.0]]

## Facets

**substrate** [[video_visual]]

**stack** flstudio, python, shell, wordpress

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gan music generator

## Body

A Generated Adversarial Network, taken from https://towardsdatascience.com/generative-adversarial-networks-explained-34472718707a Inspiration We've always wanted to make an EDM music generator and decided to finally tackle it in this hackathon. What it does Running the MIDI generator will create new audio files, which can be edited in FL Studio to sound like a synthesizer. How we built it We first used the music21 python package to extract pitches and durations of notes in midi files. Pitches and durations of notes were used to make an image file, where pitches represented a pixel in the y space and durations represented 16th note in the x space. These images were fed into the GAN, which consists of two neural networks, one that attempts to classify "desirable" musical elements, and another that generates images. The image outputs from the model were then changed back into note data describing pitches and durations. These were processed into midi files and finally converted to mp3 files. Challenges we ran into At first, the model was generating terrifying audio. This issue was due to the threshold for a note during training being 50%. Raising the threshold fixed the problem and the outputs started sounding significantly more pleasant on the ears. Accomplishments that we're proud of This was the first hackathon for both of us and it was amazing to see a project like this come together in such a short period of time. What we learned We had minimal experience in python prior to the project and had also never trained a GAN before. During the course of this project, we increased our proficiency in python and learned how to train a GAN. We also learned that when setting something, especially for the first time, even if it seems right, it might not be. Trying different methods is important. What's next for GAN Music Generator A more accurate network and by extension, better generated songs, might arise from improving the quality of training data and increasing the number of variables taken in by the network. For example, instead of having just pitch and duration data for notes in given MIDI files, extracting other data such as loudness of notes. <div