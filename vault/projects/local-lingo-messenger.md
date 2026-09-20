---
slug: "local-lingo-messenger"
url: "https://devpost.com/software/local-lingo-messenger"
title: "Local LLM Messenger (lollmm)"
hackathon: "Docker AI/ML Hackathon"
organization: "Docker"
winner: true
words: 307
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Local LLM Messenger (lollmm)

> iMessage to the LLM(s) running on your computer

[Devpost](https://devpost.com/software/local-lingo-messenger) · hackathon [[Docker AI-ML Hackathon]]

## Facets

**mechanism** [[on_device_local]]
**substrate** [[video_visual]] [[web_dom]]

**stack** docker, fastapi, ollama, python, sendblue

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for local lingo messenger

## Body

GIF Sending a message and receiving an answer from llama2 GIF An LLM reaction with lasers Inspiration I needed a way to chat with an LLM from my phone with the most mobile-friendly interface possible, messaging. I wanted a way to compare different LLMs easily for day to day questions. I usually think of questions to ask when I'm away from my computer and never remember them when I'm back at my computer. I wanted a simple interface, lot's of LLMs, and no on-going hosting charges. What it does The app intercepts messages sent to a sendblue number and forwards them to the LLM. It will receive the answer back from a variety of LLMs and reply via iMessage. It works with ollama models locally and can also call OpenAI ChatGPT if an API key is provided. How we built it The main app is a FastAPI backend that connects messages from sendblue to Ollama. It can run slash commands / and has support for other short codes (e.g. @ mention LLM) and matching words for extra message flare. Challenges we ran into There was some difficulty making the app work with ChatGPT and Ollama APIs because of the different features they support. Accomplishments that we're proud of Making the interface feel more human with typing indicators and message flare. Because it can all run locally it also allows someone to get a public URL via ngrok or Tailscale funnel to talk directly to their computer. What we learned Learned how to use sendblue API and Ollama API. Packaging everything with docker compose to make it easier to deploy was easy but needed some work to make the startup easier. What's next for Local Lingo Messenger Adding support for image generation when the LLMs support it. Adding context handling for Ollama when their API supports it. <div