---
slug: "story-ai-agents-and-others"
url: "https://devpost.com/software/story-ai-agents-and-others"
title: "Story.AI agents and others"
hackathon: "Global AI Agents League"
organization: "Fetch.ai"
winner: true
words: 896
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "user/developer"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Story.AI agents and others

> Story.ai is your AI therapy companion—helping you heal, grow, and rewrite your life story through smart journaling, daily routines, and personalized mental wellness insights.

[Devpost](https://devpost.com/software/story-ai-agents-and-others) · hackathon [[Global AI Agents League]]

## Facets

**mechanism** [[multi_agent]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[developer_tools]] [[mental_health]]
**user** [[developer]]
**substrate** [[geospatial]] [[video_visual]]

**stack** agentverse, fastapi, fetch.ai, firebase, nextjs, uagents

## How they structured the write-up

- ✨ inspiration
- 🧠 story.ai: multi-agent mental health support system
- 🔧 ai workflow planning agent: ai for agent builders
- 🚧 challenges we faced
- 🏆 accomplishments
- 📚 what we learned
- 🔮 future prospects
- 🚀 final thoughts

## Body

Journalling Dashboard 🧠 Story.AI & Workflow Agent: Multi-Agent Mental Health Support System ✨ Inspiration Mental health solutions are often expensive, inaccessible, and generalized. Story.AI was inspired by the idea of decentralizing and democratizing mental wellness through a personalized, always-available network of intelligent AI agents. Powered by the Fetch.ai Agentverse ecosystem, our goal is to make mental health support scalable, intelligent, and deeply personalized—without replacing human therapists, but amplifying their impact. 🧠 Story.AI: Multi-Agent Mental Health Support System Story.AI is a comprehensive mental health support platform powered by a network of specialized AI agents, designed for emotional understanding, behavioral transformation, and cognitive restructuring through journaling, reflection, and conversation. Built entirely on Fetch.ai's Agentverse , it’s designed as a modular, composable ecosystem of six collaborative agents. 🔁 Multi-Agent Architecture Agent Name Role Address Personal Assistant Agent Central orchestrator that analyzes user queries and routes them to specialized agents test-agent://agent1qt7fcalfq80vevam23gz8hlrl9txh6wrcpwn57j670p4sdkdd83j5sgq7ge Journal Analysis Agent Detects emotions and cognitive patterns in journal entries test-agent://agent1qf97yx9eg6r7ycgt68r7a90dfp4qraf8jldwg8urktr204l0futnkyckt5f Exercise Generator Agent Generates personalized CBT exercises and morning reflections test-agent://agent1qtpcdp4gte33ey026qd3pguuadwf89e9dfwl4ezazq9y7ajvv3z6y9h3662 Gratitude Agent Builds gratitude-based practices based on user situations test-agent://agent1qdxlnp47vjqn2dkn5tg5l62apd4x7gn4daygl8jlcfc4jk7c3ca4jm83ukx Therapy Conversation Agent Conducts memory-aware therapy-like conversations test-agent://agent1qftlfn8w5dskw9rd97kg4rt9ul0dynt8y97d99mcfzxkdxcadmnxyjnhrc3 Story.AI Guide Agent Assists in navigation and feature discovery within Agentverse test-agent://agent1q0sm7nt0w330v9cutvkqg6dvjmgghejwvmrejydlu2dhq4e0s8l6xnwyzds Each agent is designed with domain-specific prompts , structured payloads , and secure asynchronous webhooks for inter-agent communication. 🔧 How We Built Story.AI ⚙ Agent Architecture Assistant Agent : Understands user intent and routes queries. Journal Agent : Uses emotion models (e.g. DistilRoBERTa) to extract cognitive patterns. Exercise Generator : Maps journal insights to mental health exercises using LLM prompting. Gratitude Agent : Crafts personalized gratitude prompts with situational context. Therapy Agent : Uses LangChain’s ConversationBufferMemory for therapy-like continuity. Guide Agent : Enables users to explore and use the system via smart recommendations. 🔗 Inter-Agent Communication Webhook System : Asynchronous and secure webhook-based message passing. Structured JSON : All data transferred as validated JSON with typed parameters. Response Validation : Ensures consistent agent interactions and recoverability. 🌍 Agent Registration & Discovery Domain-Specific Capabilities : Each agent registered with structured documentation and expected inputs/outputs. Dynamic Discovery : Agents discover others via Search and Discover APIs on Agentverse. 🤖 LLM Integration Used Google Gemini Pro for: Agent-specific prompts Tuned temperature settings Structured JSON outputs 💾 Stateful Memory Therapy Agent : Stores conversational context using LangChain. Assistant Agent : Maintains routing context and conversation type to ensure smooth flow. 🔧 AI Workflow planning Agent: AI for Agent Builders Workflow Agent is a specialized agent that helps developers create, manage, and deploy agent-based mental health systems. Agent Address : test-agent://agent1q0n0uv6zqgzh6pclzyae4qwzzmcx60cxnc5y4cxmj8ggfntne4glygzffs4 It is a meta-agent that supports: Designing new agent architectures Guiding developers through agent registration and deployment Generating agent prompts and payload specs Validating webhook connections and endpoint behaviors 🧩 Features Step-by-step flow for building new agents Recommends ideal payload formats Generates templated code for webhook handlers Acts as a bridge between technical devs and the Agentverse platform Provides live debugging support through LLM-assisted issue resolution 🚧 Challenges We Faced Challenge Solution Agent Coordination Built robust retry logic and fallback systems for inter-agent routing Identity Management Managed secure agent seed phrases using local vaults Cold Start Routing Designed a fallback routing strategy when new agents were not pre-indexed Response Consistency Unified UI and agent interaction schema with strict JSON validation Webhook Reliability Used exponential backoff and ping validation endpoints Multi-Agent Testing Created simulation harness to test interactions across agents 🏆 Accomplishments ✅ True agent-based architecture with full Fetch.ai Agentverse integration ✅ Seamless routing via Assistant Agent with >90% intent resolution accuracy ✅ Built and deployed six specialized mental health agents ✅ Enabled discovery of external agents via Guide Agent ✅ Created a developer agent (Workflow Agent) to assist in new agent creation ✅ Built robust webhook messaging and async error recovery system 📚 What We Learned Building scalable multi-agent architectures requires clear interface design Webhook-based systems need proactive error handling and response validation Natural language routing can be effectively achieved with LLMs and JSON output formatting Agent discovery is essential for building extensible ecosystems Secure identity and key management is crucial in decentralized agent platforms Agents should remain small and focused for maintainability and composability 🔮 Future Prospects For Story.AI 🧘 Routine Builder Agent : Use voice-based prompts to co-create morning and evening routines Integrate journaling and gratitude flows with personalized activity suggestions Serve as a behavioral nudge assistant to increase adherence to mental health plans 💬 Multi-modal Agent Expansion : Voice journaling, image-based mood boards, TTS therapy agents 🧠 Condition-Specific Agents : Specialized agents for anxiety, depression, ADHD, etc. 🌐 User-Customized Agent Networks : Let users assemble their own support team using preferred agents For Workflow Agent 🤖 AI-Creating-AI Tools : A system where agents help create new agents autonomously Based on user requirements, Workflow Agent can generate entire agent blueprints with prompt strategies, webhook code, and payload formats 🧪 Simulation-Based Testing Toolkit : Build test cases where the Workflow Agent simulates interactions between agents before real deployment 📦 Agent Marketplace SDK : Helps developers list and monetize agents within the broader Agentverse 🚀 Final Thoughts Story.AI and Workflow Agent showcase the power of composable AI agents in solving deeply personal problems like mental health support and system creation. By building on Agentverse, we’ve made a flexible, future-ready platform where both users and developers can thrive. We believe the future is multi-agent — and we’re just getting started. <div