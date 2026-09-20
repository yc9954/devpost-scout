---
slug: "veritas-gtiw48"
url: "https://devpost.com/software/veritas-gtiw48"
title: "Veritas"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 608
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
  - "substrate/geospatial"
---

# Veritas

> Learn anything in one hour

[Devpost](https://devpost.com/software/veritas-gtiw48) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[scientific_research]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** css, hosted-on-vercel, javascript, node.js, typescript, vscode

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for veritas

## Body

Inspiration The inspiration for this project came from my own experience as a student. Whenever I wanted to learn something new—whether it was quantum physics, machine learning, or a topic for a competition—I often found myself spending more time figuring out where to start than actually learning. I would jump between YouTube videos, articles, textbooks, and forums, only to end up with dozens of tabs open and no clear understanding of the subject. I realized that the biggest obstacle was rarely a lack of information; it was information overload. Important concepts were buried beneath hours of content, making the learning process slow and inefficient. This led me to wonder: what if there were a system that could do the compression for you? Instead of spending hours searching, filtering, and organizing information, what if you could immediately access the essential ideas, understand how they connect, and receive guidance tailored to your level of knowledge? That question became the foundation of the Time Compression Learning Engine—a platform designed to help people reach understanding faster without sacrificing depth. What it does Veritas helps users learn complex topics in a fraction of the usual time. Users enter a topic they want to learn, and the platform generates a structured learning path containing distilled core concepts, simplified explanations, mental models, and interactive questions. How I built it I spent a significant amount of time studying the psychology of learning and reading research papers. I wanted to incorporate these evidence-based learning techniques into a tool that could help people understand complex subjects more efficiently. I built Veritas as a full-stack web application designed around an adaptive learning pipeline. The frontend was developed using React and TypeScript, providing a dynamic interface where users can input a topic, navigate generated learning modules, answer questions, and receive real-time feedback. On the backend, I developed a multi-stage AI pipeline that converts any topic into a structured learning path. The system performs concept extraction, prerequisite mapping, and dependency analysis to build a hierarchical concept graph. Large language models are then orchestrated through specialized prompt chains to generate summaries, mental models, assessments, and adaptive follow-up content. User responses are continuously evaluated to estimate concept mastery, allowing the system to dynamically adjust content depth and question difficulty in real time. Challenges I ran into major challenge was information compression. Large language models are highly capable of generating explanations, but producing explanations that are simultaneously concise, accurate, and pedagogically effective is considerably more difficult. Excessive simplification risks losing essential details, while excessive detail defeats the purpose of accelerated learning. Achieving the right balance required extensiveeffort and iterative refinement of the content generation pipeline. Accomplishments that I'm proud of I am particularly proud of creating a system that transforms overwhelming topics into clear, structured learning experiences. The adaptive questioning mechanism successfully creates the feeling of a personalized tutor rather than a static educational resource. I'm also proud of developing an end-to-end platform that combines AI-generated content, real-time adaptation, interactive assessments, and user-friendly design into a cohesive learning product. What I learned There is a significant amount of research you have to put in before building a project if you actually want that project to be helpful to people. Like I read research papers on Psychology of learning beofre making this tool so that the method in which it teaches is scientifically proven to work. What's next for Veritas The next phase of the project will focus on improving personalization through deeper learner modeling and more sophisticated knowledge-gap detection. Future versions will include visual learning tools, spaced repetition, progress analytics, collaborative learning features, and support for a wider range of educational content formats. <div