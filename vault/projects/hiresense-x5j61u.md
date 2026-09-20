---
slug: "hiresense-x5j61u"
url: "https://devpost.com/software/hiresense-x5j61u"
title: "HireSense"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 590
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/labor_employment"
---

# HireSense

> Traditional ATS has limitations, that’s why we wanted to introduce our product that improves the traditional ATS system.

[Devpost](https://devpost.com/software/hiresense-x5j61u) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[simulation_digital_twin]]
  <sub>weak: multi_agent, on_device_local, realtime_stream</sub>
**domain** [[labor_employment]]
  <sub>weak: code_repository, structured_db</sub>

**stack** asi:one, fastapi, fetch.ai, next.js, supabase, tailwind

## Body

Inspiration Traditional ATS systems are broken. They rely on exact keyword matches to rank resumes, which leads to two big problems: Qualified candidates get rejected because they phrased things differently Unqualified candidates beat the system by stuffing their resumes with buzzwords Even with automation, recruiters are overwhelmed. They still spend hours manually reviewing stacks of resumes, often without any intelligent assistance. We thought: what if an AI could simulate a real hiring panel, one that’s explainable, fair, and nuanced That’s why we built HireSense AI HR Council — a smarter, agentic alternative to traditional ATS What it does HireSense is an autonomous hiring pipeline made up of multiple specialized AI agents working together like a hiring committee ResumeAgent Extracts hard facts like skills, years of experience, certifications, and project names from the candidate’s resume JobAgent Breaks down the job description into structured requirements: required skills, level, location, and nice-to-haves EvalAgent Compares ResumeAgent and JobAgent data, highlights alignment or gaps, and produces a match score DebateAgent1 The Optimist Tailors the candidate's strengths to fit the job DebateAgent2 The Skeptic Points out inconsistencies, missing skills, or red flags DebateAgent3 The Arbiter Observes the debate and makes an informed judgment FinalAgent Synthesizes everything and makes a hiring recommendation It’s like simulating a real hiring debate with structured reasoning How we built it We used: Fetch ai uAgents to modularize each agent, ResumeAgent, JobAgent, etc ASI One to power the intelligence and reasoning behind agent responses Model Context Protocol MCP framework to manage communication and memory between agents Supabase to log results and store top candidates Python and FastAPI for backend logic Deployed locally and used Postman for testing endpoints This was our first time working with uAgents, ASI One, and MCP, so we had to learn quickly how to manage agent messaging, memory, and context sharing Challenges we ran into Understanding and wiring uAgents communication was initially confusing — managing agent addresses, protocols, and message handling took time to get right Getting ASI One to generate consistent, accurate debate arguments required careful prompt tuning and context shaping Syncing the evaluation logic and making agents truly autonomous, not just serial API calls, was a learning curve Implementing streaming and handling thoughts from ASI responses required edge-case error handling Accomplishments that we're proud of We built a multi-agent autonomous system that mimics real hiring panels Developed an agent-based debate engine with arguments and counterarguments rather than just matching keywords Created a functional ATS prototype that offers explainable hiring decisions Learned and implemented uAgents, MCP, and ASI One — technologies we had never used before Integrated a database layer with Supabase to track and evaluate top candidates What we learned How to build autonomous agents with uAgents and manage complex communication flows How to use ASI One for structured multi-turn reasoning, including capturing the model’s internal thoughts The power of building modular, explainable AI systems that simulate human workflows How to turn a messy hiring process into a pipeline of intelligent decisions What's next for HireSense AI HR Idea Goal: Build a full Autonomous Hiring Council Enable recruiters to upload job descriptions and get back explainable hiring evaluations in seconds Add interview question generators based on candidate weaknesses Implement confidence scores and personality trait inference from resume wording Expand DebateAgents with special roles like culture fit agent, diversity advocate agent, leadership scout Build a UI dashboard for HR teams to interact with debates and override or approve AI decisions We are building toward a future where hiring is smarter, fairer, and human-inspired powered by AI <div