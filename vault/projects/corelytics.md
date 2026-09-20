---
slug: "corelytics"
url: "https://devpost.com/software/corelytics"
title: "Corelytics"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 630
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "substrate/geospatial"
---

# Corelytics

> Corelytics is an AI-powered email generation system that replaces manual prompting with a structured intent engine, enabling fast, context-aware professional communication.

[Devpost](https://devpost.com/software/corelytics) · hackathon [[Frostbyte Hackathon]]

## Facets

**substrate** [[geospatial]]

**stack** fastapi, json-logic-tree, llm-api, prompt-engineering, python, rest-api-architecture

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for corelytics

## Body

JSON Logic Tree JSON Logic Tree JSON Logic Tree JSON Logic Tree User Interface User Interface User Interface User Interface Output Architecture Overview Inspiration Writing professional emails is something almost everyone does daily. However, most AI tools require users to write detailed prompts to generate a good email. This defeats the purpose for many users who simply want a fast and structured way to communicate. We wanted to explore whether email generation could be automated without requiring the user to write prompts at all. The idea behind Corelytics was to build a system where users simply select their intent, and the system intelligently constructs the email for them. This led to the concept of a promptless AI email generation system driven by a structured intent architecture. What it does Corelytics is an AI-powered email generation system that eliminates the need for manual prompt writing. Instead of asking users to describe what they want, the system guides them through a structured intent flow: Domain → Recipient → Category → Scenario Based on these selections, Corelytics automatically builds the context required to generate a professional email. The system can generate emails for multiple professional scenarios such as: ▸Job applications ▸Internship requests ▸Meeting requests ▸Follow-ups ▸Professional inquiries This makes email generation faster, structured, and accessible even for users who are not familiar with prompting AI systems. How we built it Corelytics was built as a modular AI system with several components working together. Intent Engine : A structured JSON logic tree that maps user selections to communication scenarios. State Manager : Tracks the user's selections and manages the conversation flow. Prompt Compiler : Automatically converts structured intent data into optimized prompts for the language model. AI Generation Layer : Uses a large language model API to generate context-aware professional emails. Backend System : The backend was built using Python and FastAPI, enabling a lightweight and scalable API architecture. This modular architecture allows the system to expand easily with new domains, email scenarios, and workflows. Challenges we ran into One of the biggest challenges was designing the intent architecture. The system had to: ▸Cover a wide range of professional email scenarios ▸Avoid making the selection process too complicated ▸Ensure the generated emails remained natural and context-aware Another challenge was designing the prompt compiler so that structured selections could still produce high-quality natural language outputs. Balancing structure with flexibility required multiple iterations of the intent tree design. Accomplishments that we're proud of ▸Building a fully working promptless AI email generation workflow ▸Designing a scalable intent-driven architecture ▸Creating a modular backend that can easily expand to other communication tasks ▸Demonstrating how AI systems can be made more accessible by removing the need for prompting What we learned Through this project we learned that AI usability is just as important as AI capability. Many powerful AI systems exist today, but users still struggle with how to interact with them effectively. Designing structured interfaces for AI can significantly improve accessibility and user experience. We also gained practical experience working with: ▸FastAPI backend systems ▸Intent-driven architectures ▸Prompt engineering pipelines ▸LLM API integration What's next for Corelytics The current version of Corelytics focuses on structured AI-powered email generation, but the long-term vision is to expand it into a broader professional communication assistant. Future development plans include: ▸Expanding beyond email generation to support professional notices, announcements, formal letters, and internal communications ▸Adding integration with platforms like Gmail and Outlook to allow users to directly send generated emails ▸Introducing customizable communication templates for organizations and institutions ▸Supporting multi-language communication generation ▸Developing a web interface where users can quickly generate different types of professional communication through structured intent selection The long-term goal is to transform Corelytics from a simple email generator into a structured AI communication platform for professional and organizational workflows. <div