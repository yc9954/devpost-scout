---
slug: "eddy-zx9uto"
url: "https://devpost.com/software/eddy-zx9uto"
title: "Eddy"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 490
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/labor_employment"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Eddy

> The autopilot for ideas—Eddy semantically maps your thoughts into an alluring, explorable map, helping you sail your stream of consciousness.

[Devpost](https://devpost.com/software/eddy-zx9uto) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
**domain** [[labor_employment]]
**substrate** [[geospatial]] [[video_visual]]

**stack** chakra-ui, fastapi, figma, huggingface, nltk, openai, python, react, react-flow

## How they structured the write-up

- inspiration
- learnings
- features
- challenges
- future directions
- built with
- mindmap algorithm

## Body

About Page of Eddy Proposed graph analysis of thought map The Eddy TechStack Homepage of Eddy Mindmapping algorithm Inspiration Imagine you're sitting in your favorite coffee shop and a unicorn startup idea pops into your head. You open your laptop and choose from a myriad selection of productivity tools to jot your idea down. It’s so fresh in your brain, you don’t want to waste any time so, fervently you type, thinking of your new idea and its tangential components. After a rush of pure ideation, you take a breath to admire your work, but disappointment. Unfortunately, now the hard work begins, you go back though your work, excavating key ideas and organizing them. Eddy is a brainstorming tool that brings autopilot to ideation. Sit down. Speak. And watch Eddy organize your ideas for you. Learnings Melding speech recognition and natural language processing tools required us to learn how to transcribe live audio, determine sentences from a corpus of text, and calculate the similarity of each sentence. Using complex and novel technology, each team-member took a holistic approach and learned news implementation skills on all sides of the stack. Features Live mindmap —Automatically organize your stream of consciousness by simply talking. Using semantic search, Eddy organizes your ideas into coherent groups to help you find the signal through the noise. Summary Generation —Helpful for live note taking, our summary feature converts the graph into a Markdown-like format. One-click UI —Simply hit the record button and let your ideas do the talking. Team Meetings —No more notetakers: facilitate team discussions through visualizations and generated notes in the background. Challenges Live Speech Chunking - To extract coherent ideas from a user’s speech, while processing the audio live, we had to design a paradigm that parses overlapping intervals of speech, creates a disjoint union of the sentences, and then sends these two distinct groups to our NLP model for similarity. API Rate Limits —OpenAI rate-limits required a more efficient processing mechanism for the audio and fewer round trip requests keyword extraction and embeddings. Filler Sentences —Not every sentence contains a concrete and distinct idea. Some sentences go nowhere and these can clog up the graph visually. Visualization —Force graph is a premium feature of React Flow. To mimic this intuitive design as much as possible, we added some randomness of placement; however, building a better node placement system could help declutter and prettify the graph. Future Directions AI Inspiration Enhancement —Using generative AI, it would be straightforward to add enhancement capabilities such as generating images for coherent ideas, or business plans. Live Notes —Eddy can be a helpful tool for transcribing and organizing meeting and lecture notes. With improvements to our summary feature, Eddy will be able to create detailed notes from a live recording of a meeting. Built with UI: React, Chakra UI, React Flow, Figma AI: HuggingFace, OpenAI Whisper, OpenAI GPT-3, OpenAI Embeddings, NLTK API: FastAPI Supplementary Material Mindmap Algorithm <div