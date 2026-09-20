---
slug: "running-clothes"
url: "https://devpost.com/software/running-clothes"
title: "Running Clothes"
hackathon: "Amazon Alexa Skills Challenge: Multimodal"
organization: "Amazon"
winner: true
words: 452
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Running Clothes

> Wondering what to wear on your next run? This skill takes the guesswork out of gearing up for your next run.

[Devpost](https://devpost.com/software/running-clothes) · hackathon [[Amazon Alexa Skills Challenge- Multimodal]]

## Facets

**mechanism** [[benchmark_measured]]
**substrate** [[code_repository]] [[video_visual]]

**stack** amazon-alexa, javascript, node.js

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for running clothes

## Body

Thank You / End screen example 3 output screen Opening screen example 1 output screen Gender example 2 output screen Inspiration 11 years ago, I spectated my first marathon in Virginia Beach, VA and I was completely awe-struck by the dedication and commitment to a healthy lifestyle of the marathon runners. For me, running a marathon was just a pipe dream as I had never run further than my mailbox. Fast forward to today, I have now completed 3 full marathons, 9 half marathons, and logged over 1,100 running miles in 2018. As someone who ran over 1,100 miles outdoors last year, I've found that being properly layered and dressed for outdoor runs is essential. I've learned about running apparel, and proper layering for my runs. I found myself obsessively checking the weather, and then checking a formula in my head to select my running clothes for each run. Isn't there an easier way? What if I created a skill that took the guesswork out of getting dressed for each run? What it does Running Clothes advisor, pulls weather information including, temperature, wind speed, humidity, and conditions, and then runs it through my algorithm to create a personalized running clothes recommendation. How I built it I am using the OpenWeather API and pulling temperature, wind speed, humidity, and conditions by the user's zip code. I started with the basic Alexa dialog management template and combined it with the API information. I watched the Amazon webinars on APL and reviewed the technical documentation to add APL screens to my skill. Challenges I ran into My original plan was to create an APL screen for every scenario, and every dialog turn in my skill. Unfortunately, I found that I could not combine slot filling with APL screens as it is not supported yet. screenshot here Accomplishments that I'm proud of I completed the New York City Marathon (26.2 miles) on November 4, 2018. Or are you asking about my Alexa experience? I was featured on the Alexa Skill home page from November 30 to December 6, 2018 for my skill, Cork Ornaments. What I learned Listen to user feedback. I did not include the weather API in the initial release of the skill, and it was the most requested feedback I received. As a part of the APL upgrade, I also added Weather API. I learned that I couldn't combine dialog directives with APL screens. I learned that invoking an intent from a user touch wrapper is not yet supported. I creatively found a workaround by adding a new way to trigger my intent. What's next for Running Clothes I'd love to expand my skill for countries outside the US and other languages. <div