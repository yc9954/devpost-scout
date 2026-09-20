---
slug: "codefusion-v9eq2x"
url: "https://devpost.com/software/codefusion-v9eq2x"
title: "CodeFusion"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 327
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/web_dom"
---

# CodeFusion

> Talk, gesture, and bring your code to life.

[Devpost](https://devpost.com/software/codefusion-v9eq2x) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**substrate** [[web_dom]]

**stack** flask, gemini, intersystems, openai, opencv, visual-studio-code

## How they structured the write-up

- inspiration 💡
- what it does ⁉️
- how we built it 📝
- challenges we ran into 😡
- accomplishments that we're proud of 😸

## Body

Inspiration 💡 We were inspired by the thought of, "what if Cursor could do this?" Cursor composer, a powerful tool in it of itself, how much crazier would it be for Cursor to have access to video and audio, along with our terminals so not only could it write code, it would verify it's capabilities and more. What it does ⁉️ You start with screen recording and talking to describe the issue or enhancement needed. We then process this using gemini flash 2.0 and turn it into a structured schema organized by timestamps. We extract relevant files and urls and then extract html from the web pages and turn them into embeddings. We extract relevant text using a RAG pipeline with Intersystems-IRIS. Once we have all this info we use codegen to edit relevant code and verify correctness by running the application. How we built it 📝 TypeScript/React - VSCode Extension Python-Flask - Server Backend Codegen + Langchain - Agentic Code Editing Gemini - Video recording parsing IRIS - RAG -OpenAI - Embeddings Challenges we ran into 😡 Streaming using the gemini live API was very difficult. We were able to stream video and audio and get real time responses asynchronously, but the text inputs stopped working. We instead processed the video before sending it to gemini flash 2.0 with a specific schema enforced. Setting up the VS Code extension to have the UI in the side panel instead of the tab was challenging. In addition, the extension was a web view and restricted display capture so we had to find a workaround to send video to the backend. Accomplishments that we're proud of 😸 We are proud of getting a fully functional backend with a multifaceted backend. We were able to get 3 distinct components (along with the frontend VS code extension) working: the video processing into a structured schema by gemini, the RAG with intersystems, and the agentic flow and tool calling with codegen. <div