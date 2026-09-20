---
slug: "storymation-yvef2p"
url: "https://devpost.com/software/storymation-yvef2p"
title: "StoryMation"
hackathon: "Hack the North 2023"
organization: "Techyon"
winner: true
words: 363
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "substrate/video_visual"
---

# StoryMation

> Story to Animation in seconds!

[Devpost](https://devpost.com/software/storymation-yvef2p) · hackathon [[Hack the North 2023]]

## Facets

**substrate** [[video_visual]]

**stack** cohere, dall-e, node.js, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of

## Body

Inspiration We were inspired to create such a project since we are all big fans of 2D content, yet have no way of actually animating 2D movies. Hence, the idea for StoryMation was born! What it does Given a text prompt, our platform converts it into a fully-featured 2D animation, complete with music, lots of action, and amazing-looking sprites! And the best part? This isn't achieved by calling some image generation API to generate a video for our movie; instead, we call on such APIs to create lots of 2D sprites per scene, and then leverage the power of LLMs (CoHere) to move those sprites around in a fluid and dynamic matter! How we built it On the frontend we used React and Tailwind, whereas on the backend we used Node JS and Express. However, for the actual movie generation, we used a massive, complex pipeline of AI-APIs. We first use Cohere to split the provided story plot into a set of scenes. We then use another Cohere API call to generate a list of characters, and a lot of their attributes, such as their type, description (for image gen), and most importantly, Actions. Each "Action" consists of a transformation (translation/rotation) in some way, and by interpolating between different "Actions" for each character, we can integrate them seamlessly into a 2D animation. This framework for moving, rotating and scaling ALL sprites using LLMs like Cohere is what makes this project truly stand out. Had we used an Image Generation API like SDXL to simply generate a set of frames for our "video", we would have ended up with a janky stop-motion video. However, we used Cohere in a creative way, to decide where and when each character should move, scale, rotate, etc. thus ending up with a very smooth and human-like final 2D animation. Challenges we ran into Since our project is very heavily reliant on BETA parts of Cohere for many parts of its pipeline, getting Cohere to fit everything into the strict JSON prompts we had provided, despite the fine-tuning, was often quite difficult. Accomplishments that we're proud of In the end, we were able to accomplish what we wanted! <div