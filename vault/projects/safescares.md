---
slug: "safescares"
url: "https://devpost.com/software/safescares"
title: "SafeScares"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 327
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/media_journalism"
---

# SafeScares

> Enjoy a personalized horror experience without the fear of encountering unsettling content.

[Devpost](https://devpost.com/software/safescares) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**domain** [[media_journalism]]

**stack** partyrock

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for safescares

## Body

Inspiration I watch horror movies with friends every Halloween. As the person who has seen the most horror movies, I'm usually tasked with recommending films. However, balancing my friends' triggers and comfort levels without spoiling the movies for myself became increasingly difficult. With no one else to consult, the research process grew lengthy and cumbersome. There had to be a way to streamline this process. What it does SafeScares is a spoiler-free horror movie recommender app that allows users to input their scare level, specify triggers to avoid, and describe what they're interested in - whether it's a particular mood, setting, or theme - for personalized recommendations. The app provides a curated selection of horror movies tailored to each user's comfort level and preferences. Users can then chat with the app to narrow recommendations or inquire about potential triggers in the recommendations. How we built it PartyRock Challenges we ran into I initially used Claude to generate recommendations, but no matter the prompt, Claude's recommendations kept including movies with the mentioned triggers. It even included movies referenced in the description. I tried increasing the specificity of the prompts and providing more explicit instructions, but nothing worked. It wasn't until I switched to Llama that the recommendations improved. Accomplishments that we're proud of It was pretty satisfying to build something I would use regularly in under a day. What we learned Fact-checking proved essential due to Claude providing recommendations that were redundant and contained triggering content Design and copy played a crucial role in clarifying the app's purpose as a horror movie recommender for triggers and scare thresholds Utilizing explicit and specific prompts notably enhanced recommendation results What's next for SafeScares I think there is a wide application for recommendations based on safety. SafeScares could move beyond horror movie recommendations to include any content, such as shows and books. Additionally, it could serve as a tool for parents to filter out works containing content they find inappropriate. <div