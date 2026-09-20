---
slug: "chatur"
url: "https://devpost.com/software/chatur"
title: "Chatur"
hackathon: "Hack The League Chapter 2"
organization: "Hack The League"
winner: true
words: 272
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# Chatur

> Generate Human Like text using chatGPT with various prompts.

[Devpost](https://devpost.com/software/chatur) · hackathon [[Hack The League Chapter 2]]

## Facets

**substrate** [[geospatial]]

**stack** chatgpt, headlessui, nextjs, openapi, react, tailwindcss, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chatur

## Body

Default Home Page Generating text using one of the prompts Summary of a site using one of the prompts Inspiration ChatGPT often gives us wrong results because we don't use proper prompts when asking ChatGPT anything. We have Gathered some high quality prompts from certain categories which will produce high quality results. What it does Chatur is a Web App which gives you human like text based on certain predefined prompts which are integrated into the application. Before deciding to include them, we investigated various tools, such as AIPRM, and tested a number of high-quality prompts. End users find it simpler to produce high-quality results without having to worry about prompts themselves. How we built it We created the entire application in NextJS, and we created the API using the NextJS API directory, which eliminated the need to create a separate backend server. To fully utilise Vercel's infrastructure, we used NextJS' Edge Runtime. The edge functions made our API calls extremely quick. Challenges we ran into It was new because we had never used OpenAI before. We also encountered a GPT 3.5 Turbo token size error because we were consistently exceeding the maximum size of 4,096 tokens. To fix it, we decreased the token size in our configuration. Accomplishments that we're proud of We had never participated in a Hackathon before so it was an accomplishment for us to build the entire project in the span of 48 hours. What we learned We learnt about OpenAI, Edge Runtime and NextJS API Routes. What's next for Chatur We will add more high quality prompts in the future and keep on improving it. <div