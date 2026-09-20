---
slug: "lucid-ai-95nerk"
url: "https://devpost.com/software/lucid-ai-95nerk"
title: "Lucid.ai"
hackathon: "Hack the North 2022"
organization: "Techyon"
winner: true
words: 288
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Lucid.ai

> Let's turn that book into a movie. Text to movie, directed by AI.

[Devpost](https://devpost.com/software/lucid-ai-95nerk) · hackathon [[Hack the North 2022]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**substrate** [[code_repository]] [[video_visual]]

**stack** amazon-web-services, deforum, flask, openai-gpt-3, pytorch, react, stable-diffusion, tortoisetts, youtube

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lucid.ai

## Body

Home Page Video Player What it does Paste in a text and it will identify the key scenes before turning it into a narrated movie. Favourite book, historical battle, or rant about work. Anything and everything, if you can read it, Lucid.ai can dream it. How we built it Once you hit generate on the home UI, our frontend sends your text and video preferences to the backend, which uses our custom algorithm to cut up the text into key scenes. The backend then uses multithreading to make three simultaneous API calls. First, a call to GPT-3 to condense the chunks into image prompts to be fed into a Stable Diffusion/Deforum AI image generation model. Second, a sentiment keyword analysis using GPT-3, which is then fed to the Youtube API for a fitting background song. Finally, a call to TortoiseTTS generates a convincing narration of your text. Collected back at the front-end, you end up with a movie, all from a simple text. Challenges we ran into Our main challenge was computing power. With no access to industry-grade GPU power, we were limited to running our models on personal laptop GPUs. External computing power also limited payload sizes, forcing us to find roundabout ways to communicate our data to the front-end. Accomplishments that we're proud of Extremely resilient commitment to the project, despite repeated technical setbacks Fast on-our-feet thinking when things don't go to plan A well-laid out front-end development plan What we learned AWS S3 Cloud Storage TortoiseTTS Learn how to dockerize large open source codebase What's next for Lucid.ai More complex camera motions beyond simple panning More frequent frame generation Real-time frame generation alongside video watching Parallel cloud computing to handle rendering at faster speeds <div