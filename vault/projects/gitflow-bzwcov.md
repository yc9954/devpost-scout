---
slug: "gitflow-bzwcov"
url: "https://devpost.com/software/gitflow-bzwcov"
title: "GitFlow"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 693
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# GitFlow

> Transform any GitHub repository into an interactive, visual tree structure. AI-powered intelligent insights, smart summaries, and code analysis to help you understand a codebase with confidence.

[Devpost](https://devpost.com/software/gitflow-bzwcov) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** docker, elevenlabs, express.js, fastapi, gemini, githubapi, godaddy, javascript, openai, python, react, reactflow, vercel, voice-delivery-system

## How they structured the write-up

- 💡 inspiration
- 🚀 what it does
- 🛠️ how we built it
- ⚔️ challenges we ran into
- 🏆 accomplishments that we're proud of
- 📚 what we learned
- 🔮 what's next for gitflow

## Body

💡 Inspiration As developers, we've all likely struggled with understanding a Github repository. Whether you're joining a new team, contributing to open source, or exploring innovative projects, understanding complex codebases can be overwhelming and time-consuming. We were inspired by the challenge of making code exploration more intuitive and accessible. We envisioned a tool that could transform the traditional file tree view into something more visual, interactive, and intelligent. The idea was born from our own experiences struggling to understand large repositories and wanting to help other developers navigate codebases with confidence and 𝑐𝑙𝑎𝑟𝑖𝑡𝑦. 🚀 What it does GitFlow is a full-stack web application that revolutionizes how developers explore and understand GitHub repositories. Here's what makes it special: Interactive Repository Visualization : Transforms any GitHub repository into a beautiful, interactive flow graph where files and folders are represented as nodes connected by edges, making the project structure immediately visible and navigable. AI-Powered File Analysis : Click on any file node to get an intelligent summary powered by Google's Gemini AI that explains what the file does, its role in the codebase, and how it connects to other components. Smart Codebase Assistant: Features an interactive AI assistant that can answer questions about the repository by analyzing the actual source code, providing factual insights about technologies used, architecture patterns, and project functionality. Commit History Viewer : Allows users to explore commit history and preview different versions of repositories in an integrated environment. 🛠️ How we built it Frontend : React 19, ReactFlow, TailwindCSS, Vite, ShadCN Component Library. Backend: FastAPI, Google Gemini Pro API, OpenAI GPT-4, GitHub REST API, Uvicorn, Node.Js + Express.js, Docker, ElevenLabs API. Methodologies/tools: Trello, Git feature branch workflow, Atomic development, Vercel, Godaddy domains ⚔️ Challenges we ran into GitHub API Rate Limiting: One of our biggest hurdles was efficiently managing GitHub API requests. With large repositories containing hundreds of files, we needed to implement batching and prioritization to stay within rate limits while still providing comprehensive analysis. AI Model Integration: Integrating multiple AI APIs (Gemini and OpenAI) required careful prompt engineering to ensure consistent, accurate responses. We had to handle API failures gracefully and implement fallback mechanisms. Generalized Dockerfiles: Generating a Dockerfile for every type of project is challenging because different languages, frameworks, and build systems all have unique requirements. Detecting the correct entrypoint is challenging because there is no “one-size fits all" approach. A potential solution to look at in the future is incorporating AI/LLM to generate and test Dockerfiles through repository analysis. 🏆 Accomplishments that we're proud of Successfully integrated two different AI models (Gemini and OpenAI) to provide accurate, context-aware code analysis based on actual source code rather than assumptions. We are also proud of the graph visualization using ReactFlow and real-time analytics about the repository. 📚 What we learned Through this project, we learned to effectively integrate multiple AI APIs (Gemini & GPT-4) with sophisticated prompt engineering to analyze code files. We also developed knowledge in ReactFlow to transform Github repository into an interactive graph. Additionally, we learned how to utilize multiple API services like Github, OpenAI, and Google Gemini. Lastly, we learned to build a dynamic web viewer that can automatically visualize and interact with project data in real time. We explored how to programmatically start applications with custom Dockerfiles. 🔮 What's next for GitFlow To prevent potential DDoS attacks and misuse of our tool, we need to ensure that excessive requests do not deplete our API token resources. We plan to implement rate limiting strategies to control the volume of GitHub API requests and optimize usage of the ElevenLabs API. For ElevenLabs specifically, we are also exploring open-source alternatives as token usage is very limited and costly. The system currently requires manually clearing the temporary folder containing cloned repositories, which can in the future be automated to streamline workflows. A next step is to load repositories into cloud storage such as AWS S3 and automatically start their Docker containers for easier deployment and persistence. We hope our project becomes the go-to tool for many to learn about open-source projects. We also plan to create a an app viewers for applicable apps. Built by team GitFlow 🔵 <div