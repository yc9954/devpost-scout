---
slug: "ai-thena"
url: "https://devpost.com/software/ai-thena"
title: "mentis.ai"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 887
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# mentis.ai

> AI-powered tutor designed to be accessible, interactive and audiovisual.

[Devpost](https://devpost.com/software/ai-thena) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[multi_agent]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[code_repository]] [[structured_db]] [[video_visual]]

**stack** bun, fastapi, javascript, llm, monsterapi, nextjs, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for mentis.ai

## Body

Our user interface Intersectionality Inspiration The inspiration behind Mentis emerged from a realization of the vast potential that a personalized learning AI platform holds in transforming education. We envisioned an AI-driven mentor capable of adapting to individual learning styles and needs, making education more accessible, engaging, and effective for everyone. The idea was to create an AI that could dynamically update its teaching content based on live user questions, ensuring that every learner could find a path that suits them best, regardless of their background or level of knowledge. We wanted to build something that encompasses the intersection of: accessibility, interactivity and audiovisual. What it does Mentis is an AI-powered educational platform that offers personalized learning experiences across a wide range of topics. It is able to generate and teach animated lesson plans with both visuals and audio, as it generates checkpoint questions for the user and listens to the questions of its users and dynamically adjusts the remainder of the teaching content and teaching methods to suit their individual learning preferences. Whether it's mathematics, science, or economics, Mentis provides tailored guidance, ensuring that users not only receive answers to their questions but also a deep understanding of the subject matter. How we built it At its core, a fast API backend powers the intelligent processing and dynamic delivery of educational content, ensuring rapid response to user queries. This backend is complemented by our use of advanced Large Language Models (LLMs), which have been fine-tuned to understand a diverse range of educational topics and specialize in code generation for the best animation, enhancing the platform's ability to deliver tailored learning experiences. We curated a custom dataset in order to leverage LLMs to the fullest and reduce errors in both script and code generation. Using our curated datasets, we were able to fine-tune models using MonsterAPI tailoring our LLMs and improve accuracy.. We implemented several API calls to ensure a smooth and dynamic operation of our platform, for general organization of the lesson plan, script generation, audio generation with ElevenLabs, and code generation for the manim library we utilize to create the animations on our front end in Bun and Next.js. Fine tuned open source model Curated custom dataset Challenges we ran into Throughout the development of Mentis, we encountered significant challenges, particularly in setting up environments and installing various dependencies. These hurdles consumed a considerable amount of our time, persisting until the final stages of development. Every stage of our application had issues we had to address: generating dynamic sections for our video scripts, ensuring that the code is able to execute the animation, integrating the text-to-speech component to generate audio for our educational content all introduced layers of complexity, requiring precise tuning and a lot of playing with to set up. The number of API calls needed to fetch, update, and manage content dynamically, coupled with ensuring the seamless interaction between the user and our application, demanded a meticulous approach. We found ourselves in a constant battle to maintain efficiency and reliability, as we tried to keep our latency low for practicality and interactivity of our product. Accomplishments that we're proud of Despite the setbacks, we are incredibly proud of: Technical Overcomes: Overcoming significant technical hurdles, learning from them and enhancing our problem-solving capabilities. Versatile System: Enabling our platform to cover a broad range of topics, making learning accessible to everyone. Adaptive Learning: Developing a system that can truly adapt to each user's unique learning style and needs. User-Friendly UI: Creating a user-friendly design and experience keeping our application as accessible as possible. API Management: Successfully managing numerous API calls, we smoothed the backend operation as much as possible for a seamless user experience. Fine tuned/Tailored Models: Going through the full process of data exploration & cleaning, model selection, and configuring the fine-tuned model. What we learned Throughout the backend our biggest challenge and learning point was the setup, coordination and training of multiple AI agents and APIs. For all of us, this was our first time fine-tuning a LLM and there were many things we learned through this process such as dataset selection, model selection, fine-tuning configuration. We gained an appreciation for all the great work that was being done by the many researchers. With careful tuning and prompting, we were able to greatly increase the efficiency and accuracy of the models. We also learned a lot about coordinating multi-agent systems and how to efficiently have them run concurrently and together. We tested many architectures and ended up settling for one that would optimize first for accuracy then for speed. To accomplish this, we set up an asynchronous query system where multiple “frames” can be generated at once and allow us not to be blocked by cloud computation time. What's next for mentis.ai Looking ahead, Mentis.ai has exciting plans for improvement and expansion: Reducing Latency: We're committed to enhancing efficiency, aiming to minimize latency further and optimize performance across the platform. Innovative Features: Given more time, we plan to integrate cutting-edge features, like using HeyGen API to create natural videos of personalized AI tutors, combining custom images, videos, and audio for a richer learning experience. Classroom Integration: We're exploring opportunities to bring Mentis into classroom settings, testing its effectiveness in a real-world educational environment and tailoring its capabilities to support teachers and students alike. <div