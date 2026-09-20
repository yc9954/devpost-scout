---
slug: "frodo"
url: "https://devpost.com/software/frodo"
title: "Frodo"
hackathon: "UC Berkeley AI Hackathon 2024"
organization: "Cal Hacks"
winner: true
words: 440
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
---

# Frodo

> An AI tutor that seamlessly identifies your mistakes in real-time as you solve problems and provides personalized lessons.

[Devpost](https://devpost.com/software/frodo) · hackathon [[UC Berkeley AI Hackathon 2024]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[education]]
**user** [[developer]] [[educator_student]]
  <sub>weak: video_visual</sub>

**stack** figma, gpt-4o, groq, photoshop, stable-diffusion, sveltekit, tailwindcss, whisper

## How they structured the write-up

- motivations
- features
- technologies
- scaling

## Body

A screenshot of Frodo helping a user with a binary search task in Python. Frodo points at the most problematic line in your response. Frodo also supports different UIs for various user profiles (i.e. kids/adults). Frodo Motivations It's no secret that access to quality education is dictated by your finances. Traditional tutoring services cost anywhere from $25-$50/hour. We wanted to make a platform that our younger siblings could use, unlike the traditional, clunky, and annoying-to-use chatbot that has become ubiquitous today. To level the educational playing field and experiment with an entirely novel AI interface, we developed Frodo. Features Frodo is an AI tutor that you can access through your web browser, but unlike other educational AI tools, there's no chatbox . Instead, we've built a system that intelligently gives feedback on your work when you need it, seamlessly. This means that you never have to type out your prompt to get help. As avid programmers, one of the first things we wanted to integrate was coding lessons. With Frodo, users can attempt various programming tasks within their web browser. When users are stuck and aren't sure how to continue, Frodo moves around the code editor, points to the problematic line, and hints the user on how to solve the problem. These hints are never complete answer to the coding tasks, only guiding messages that point the user in the right direction. Of course, sometimes you want to initiate conversation with Frodo, and ask a question yourself. Sticking to our vision of leaving the chatbox behind, we've implemented an ultra-low latency speech-to-text Groq pipeline that opens up another channel of communication with Frodo! Simply press cmd + b to start the voice chat, and start talking! Along with coding, Frodo also supports any free response questions on any topic. Our demo also includes math and humanities tasks, and our platform can easily support more tasks from any domain. Technologies Frodo leverages a number of AI technologies: OpenAI's GPT-4o for it's advanced reasoning and problem solving Groq-powered whisper-large-v3 for low latency text-to-speech inference Langchain for structured output (i.e. being able to identify problematic lines) Lexica Aperture v4 (Stable Diffusion) for generating the visuals Frodo itself is built on the SvelteKit full-stack web framework. We used TailwindCSS for styling and making custom UI components. The text/code editor is built using Codemirror, and we developed a custom pipeline for code execution. Scaling For the hackathon, we had to manually create tasks and their corresponding test cases. However, Frodo is designed to scale, and we can easily import more tasks from various domains. Thanks for reading; I hope you liked our project! <3 <div