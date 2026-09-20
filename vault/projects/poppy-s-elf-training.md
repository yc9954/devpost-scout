---
slug: "poppy-s-elf-training"
url: "https://devpost.com/software/poppy-s-elf-training"
title: "Poppy's Elf Training"
hackathon: "Alexa Skills Challenge: Kids"
organization: "Amazon"
winner: true
words: 389
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
---

# Poppy's Elf Training

> An educational, interactive story for kids. Help Poppy complete her 3-day elf training course in the North Pole.

[Devpost](https://devpost.com/software/poppy-s-elf-training) · hackathon [[Alexa Skills Challenge- Kids]]

## Facets

  <sub>weak: geospatial, web_dom</sub>

**stack** alexa-skills-kit, aws-lambda, javascript

## Body

Description Join Poppy the Elf as she completes the three-day Certified Elf Training Program in the North Pole! Over the course of 3 segments, listeners will travel with Poppy to the mail room, bakery, and toy factory, where they will answer math and phonics questions that will help Poppy advance in her training. This interactive experience integrates learning with the magic of Christmas! Special appearances by Poppy’s elf friends and Santa Claus himself make this a perfect skill for ages 5-8. Inspiration We wanted to create a skill that took advantage of the audio-only format of the Echo and Echo Dot. We use character voiceovers, sound effects, and music to help create a story that activates kids' imaginations. Our other main goal was to emphasize contextual learning, by incorporating phonics and math questions into the framework of the story. What it does Each Alexa session corresponds to one day of elf training. During each day of training, we follow Poppy to various locations around the North Pole and help her with the task of the day by solving three problems. The path is linear, and every time we open up for user input, each option is clearly stated, resulting in a clear and directed user experience. At any point the user can ask for help. After we complete three sessions, we are prompted to accompany Poppy to her Elf Graduation, where the user has the opportunity to meet Santa and tell him what they want for Christmas. How we built it The first step was creating the content -- the story and the questions -- which we collaborated on over the course of several weeks. Once the content was written, we built a "skeleton" version of the app, using the built-in Alexa voice instead of recorded audio. This helped with the mapping of the overall structure. We then recorded the voiceovers, added music and sound effects, and replaced the text with URLs to our audio files, hosted on S3. What's next for Poppy's Elf Training Since it's a seasonal skill, we have plenty of opportunity to evaluate user feedback and add new content. In particular, adding new questions or changing existing questions is something we can do without disrupting the story. Eventually, we'd like to have many possible questions during each session, to help keep the experience fresh. <div