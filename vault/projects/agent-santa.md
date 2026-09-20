---
slug: "agent-santa"
url: "https://devpost.com/software/agent-santa"
title: "Agent Santa"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 829
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/simulation_digital_twin"
  - "domain/finance_payments"
  - "domain/retail_commerce"
  - "substrate/financial_record"
---

# Agent Santa

> Agent Santa is a multi-agent system where personality-based agents connect, understand relationships, and deliver perfect personalized gifts end-to-end with payments, intelligently and effortlessly.

[Devpost](https://devpost.com/software/agent-santa) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[multi_agent]] [[simulation_digital_twin]]
**domain** [[finance_payments]] [[retail_commerce]]
**substrate** [[financial_record]]
  <sub>weak: web_dom</sub>

**stack** fetchai, github, html, python, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agent santa

## Body

Agent Santa stats ASI:One recommending Agent Santa for gifting Collaboration between personality agents - Google Events creation Personality agent of Sakshi Personality agent of Parth Personality agent of Devam Inspiration We realized how often people struggle with gifting — not because they lack affection, but because they lack understanding of what would genuinely delight someone. Remembering birthdays, choosing meaningful gifts, and keeping surprises intact can become overwhelming. That’s what inspired Agent Santa — an autonomous gifting ecosystem where agents know you, understand you, and gift like you would. Our idea began with a simple thought: “What if your AI could talk to your friend’s AI and decide the perfect gift — all by itself?” This curiosity led us into the world of multi-agent systems, Fetch.ai’s Agentverse, and ASI.one, where we turned that thought into a working system. What it does Agent Santa consists of four main components: Personality Agents – autonomous representations of each user, powered by Grok-LLaMA. These agents store our interests, preferences, and traits, and can communicate with each other. Agent Santa (Gifting Agent) – the core orchestrator deployed on Agentverse. It queries personality agents, understands who the recipient is, and suggests personalized gifts. Shopping & Comparison Engine – built into the gifting agent to evaluate multiple options, compare prices, and pick the best choice. Payment Layer – simulates secure transactions to complete the gifting process end-to-end. A typical interaction looks like this: User Request on ASI.one→Agent Santa→Recipient Personality Agent→Gift Suggestion + Payment How we built it Framework: uAgents on Fetch.ai Deployment: Fully on Agentverse with seamless integration via ASI.one LLM Backbone: Grok-LLaMA, for reasoning and contextual understanding Architecture: Event-driven, asynchronous message passing between agents using defined protocols Workflow: User prompts on ASI.one →Agent Santa identified as best gifting agent →Queries personality agent for metadata →Runs LLaMA reasoning for suggestions →Compares, finalizes, and simulates secure checkout. Challenges we ran into -Establishing cross-communication between ASI.one personality agents and Agentverse-hosted agents. -Overcoming protocol mismatches (chat protocol vs. custom message protocol). -Managing offline agent availability and mailbox configurations. -Designing an end-to-end pipeline that includes reasoning, recommendation, and simulated payment within Fetch.ai’s decentralized ecosystem. -Coordinating multiple LLaMA-powered agents while keeping the interaction smooth and contextually consistent. Accomplishments that we're proud of End-to-End Autonomous Gifting Flow We successfully built a fully functional multi-agent ecosystem where a user can simply say, “Gift something to Devam for his birthday,” and the agents handle the entire pipeline — from understanding the relationship → fetching personality data → reasoning gift ideas → comparing products → to completing payment — entirely autonomously. This demonstrates the real-world viability of autonomous AI-to-AI collaboration on Fetch.ai’s Agentverse. Cross-Agent Personality Collaboration Each of our Personality Agents can interact, exchange metadata, and understand other users’ preferences — making every gifting decision deeply personalized and socially aware. This was a breakthrough moment: realizing our agents could “know” each other, form friendships, and build trust networks — a microcosm of human-like social intelligence in an AI ecosystem. LLaMA-Powered Reasoning Layer Integrating Grok-LLaMA into every agent gave them contextual intelligence — letting them reason about personality traits, occasions, and sentiment before recommending gifts. The result: contextual empathy — an AI that doesn’t just recommend, but understands why. Seamless Integration of ASI.one and Agentverse We bridged two ecosystems — ASI.one and Agentverse — allowing users to interact naturally through ASI.one, while all autonomous logic ran on Agentverse. This fusion of human-facing interface and agent-facing intelligence is one of the first demonstrations of its kind. End-to-End Payment Simulation Our gifting agent doesn’t stop at recommendations — it carries out the final payment step securely. This creates a truly closed-loop automation pipeline, showcasing how Fetch.ai agents can complete complex, multi-step tasks without human intervention. Vision Expansion Beyond Gifting During development, we discovered that Personality Agents could go beyond gifting — acting as AI versions of us that can represent us online, interact with recruiters, and communicate our personalities authentically. That realization expanded our project’s purpose — from gifting to digital identity representation — a concept we’re incredibly proud to pioneer. Ranked Among Top Agents on ASI.one Our SantaAI agent achieved top ranking in the gifting category on ASI.one, validating both the performance and relevance of our idea in Fetch.ai’s growing ecosystem. What we learned -The power of decentralized AI agents — how independent entities can collaborate without central control. -The importance of protocol design for reliable agent-to-agent communication. -LLM integration in reasoning workflows for context-aware decision making. -The subtle but crucial difference between social collaboration on ASI.one and runtime reachability on Agentverse. -How autonomous systems can move beyond automation into human-level social intelligence. What's next for Agent Santa Agent Santa started as a gifting agent — but it opened a doorway to something much bigger: A future where personality-driven agents represent humans authentically — helping others know, connect, and interact with us without barriers. From surprise gifting to AI-based networking and identity representation, Agent Santa marks a step toward the next generation of socially intelligent AI ecosystems. <div