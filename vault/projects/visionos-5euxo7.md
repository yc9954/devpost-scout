---
slug: "visionos-5euxo7"
url: "https://devpost.com/software/visionos-5euxo7"
title: "VisionOS"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 774
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/labor_employment"
  - "domain/retail_commerce"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# VisionOS

> Imagine a Blind Person Could Code

[Devpost](https://devpost.com/software/visionos-5euxo7) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[accessibility]] [[labor_employment]] [[retail_commerce]]
**substrate** [[geospatial]] [[web_dom]]

**stack** agentverse, elasticsearch, electron, langgraph, perplexity, stagehand, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for visionos

## Body

Inspiration My childhood best friend is legally blind. Growing up and navigating the increasingly technology-dependent world was tedious and profoundly boring. Screen readers haven't changed in 15 years. They read pages linearly, break on inaccessible websites, and require dozens of memorized keyboard shortcuts just to do what a sighted person does with a glance. A sighted person doesn't read every element on Amazon, but a screen reader forces it. Why should it work like that? A visually impaired user should get the same experience. For what has become one of the most overlooked issues in modern day society, posing a $7 billion dollar loss to companies every year, we hope to bridge the gap between visual impairment and the growth of technology. What it does Our system is fully conversational agentic operating system for visually-impaired users. Instead of simply listing every element on the screen, speaks to you to learn and take the best possible action on your behalf. Some examples for usage would be allowing those who are visually-impaired a seamless shopping experience, including the purchase of medically-aware items in which our OS will be able to have context on. Our OS also successfully allows one to code a program with just their voice. We architecture a multi-agent, multi-turn system with complete context and several voice-controlled agents capable of controlling your browser, and even your computer. Features: Natural voice conversation with real-time speech recognition and voice response. AI agents see and interact with web pages the way a sighted user would, using vision-based understanding and DOM parsing. This allows our agents to complete complex multi-step tasks with user feedback and context. Beyond the browser, the system controls applications, like skipping songs on Spotify or resuming work in VSCode. Contextual memory that remembers your preferences, budget, and past conversations across sessions. How we built it Conversational Agent : We employed OpenAI GPT-4.1 mini (STT) and Cartesia (TTS) for low latency, accurate conversation. GPT 4.1-mini acts as the “brain,” forming a connection between our agents, contextual layer, and the user-facing conversation. This is all built on an Electron overlay for the UI. Multi Agent Workflow : We employ a variety of agents across tasks, connected via LangGraph . For these agents to delegate tasks smoothly, an orchestration agent routes requests via user intent. Long-term context : ElasticSearch with JINA embeddings powers our semantic memory layer, indexing conversation history and browsing sessions so users can recall past interactions naturally. Web-search : We integrate the Perplexity Sonar API to give our agents grounded, real-time web knowledge. This lets the system make comparisons and recommendations to inform decisions before opening a webpage. Automation Tools : We use Stagehand by Browserbase and Agent-S by Simular AI to create automations for our OS. While Stagehand is useful for all browser related tasks, we use Agent-S for the rest of our desktop experience. Challenges we ran into Implementing a reliable 'Supervisor-Worker' architecture was challenging, as our supervisor initially struggled to accurately route requests among our specialized agents. We decoupled the routing logic into a dedicated classification step using GPT 4.1-mini, enforcing tightly scoped definitions for each worker. By wiring this pipeline with LangGraph, we ensured that the selected agent receives the full conversation context, preventing information loss during handoffs. Accomplishments that we're proud of Multi turn agents: We achieved fluid multi-turn refinement by optimizing agent context. Our system uses a persistent context window to maintain the state of the conversation, allowing users to iterate on ideas ('no, I’m allergic to peanuts') and reason about user intent rather than restarting. This turns the friction of prompt engineering into a natural, refining dialogue where the agent gets smarter with every reply. Natural language flow: We built our system to feel like a real conversation. Users speak naturally, get natural speech back, and can interrupt mid-sentence as if they were talking to another person. What we learned Humans rarely speak in perfect commands or say exactly what they mean right away. They can change their mind or forget crucial details. Therefore, we learned to build a system that acknowledges and considers these inconsistencies. We allow a user to interrupt a task, give refinements, or completely switch when they need to. What's next for VisionOS We were working on a "text-to-braille" live physical translation to work alongside our product. Build a full-fledged accessible OS Assumptions are dangerous in ability based design. Our next priority is to partner with visually impaired users for feedback, ensuring our engineering decisions align with lived reality. VisionOS aims to bridge the digital employment gap, building tools/agents that empower blind users to perform more efficiently in administrative and technical jobs. <div