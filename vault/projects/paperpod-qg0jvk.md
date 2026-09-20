---
slug: "paperpod-qg0jvk"
url: "https://devpost.com/software/paperpod-qg0jvk"
title: "PaperPod"
hackathon: "EducateHacks 2024"
organization: "EducateHacks"
winner: true
words: 477
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/scientific_research"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# PaperPod

> Listen to your favourite research papers like never before!

[Devpost](https://devpost.com/software/paperpod-qg0jvk) · hackathon [[EducateHacks 2024]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
**domain** [[scientific_research]]
**substrate** [[document_pdf]] [[structured_db]] [[web_dom]]

**stack** fastapi, nextjs, pinecone, python, redis, supabase, tailwind

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for paperpod

## Body

Podcast Page Search Page Semantic Search ssh instance + fast api backend Inspiration Visit here - website If you're coming from a research background, you must have stumbled upon Google Scholar's messy UI, scrolled on websites blocked by paywalls, or prompted to download the research paper. Introducing PaperPod , a platform to explore and listen to your favorite research papers on the go. Create content from the papers you read and share it with the world. We believe that research papers are the most fun piece of content you can read and therefore we are excited to bring this to you. What it does Our platform is the go-to platform for accessing and understanding research papers. We provide a fascinating interface for users to search for papers and return a list of papers with their abstracts and a direct pdf link to view directly on the app. Since research papers are generally difficult to understand, we have added an exclusive custom trained chatbot to chat with the papers and understand them better. Not only this, We've worked to introduce podcasts feature where you can create short podcasts using AI that talks about the highlights in the paper and also asks questions related to it! How we built it We used Next.js for the frontend and FastAPI for the backend. We also used Pinecone for semantic search and Whisper for generating podcasts. We used Redis PubSub to integrate the queueing system and save the generated podcasts in the database. We also used Kinde's secure authentication to secure the app. We're using Supabase as our database client. Challenges we ran into We faced quite a lot of challenges in building this project during the hackathon. Integrating FastAPI with a Next.js client running with TypeScript type support. Adding Kinde's secure authentication into the app. Embedding PDF using Pinecone and using their namespaces to embed papers on the arxiv library. Podcasts are heavy generation process and we had to use Redis PubSub to use their queueing system and save the generated podcasts in the database. This is a very heavy process and we had to optimize it. We had to use Whisper model to generate the podcasts and it was a bit of a challenge to get it working with Redis PubSub. Accomplishments that we're proud of We are proud to have implemented the idea we thought of at the beginning of the hackathon. It was our first time working with Redis PubSub and it was a great learning experience and integrating it into our FastAPI backend. What we learned Learnt so many new tools over the weekend like Next.js integration w/ FastAPI and Open AI Worked on Whisper model bugs as well Built a simple yet elegant UI using Next.js Embedding PDFs into the app Integrating Pinecone for semantic search What's next for paperpod Work on a bookmark feature <div