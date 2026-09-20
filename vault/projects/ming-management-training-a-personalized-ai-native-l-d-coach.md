---
slug: "ming-management-training-a-personalized-ai-native-l-d-coach"
url: "https://devpost.com/software/ming-management-training-a-personalized-ai-native-l-d-coach"
title: "Ming Management Training, a personalized AI-native L&D coach"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 508
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "domain/labor_employment"
  - "user/developer"
---

# Ming Management Training, a personalized AI-native L&D coach

> Transforming today’s technical talent into tomorrow’s executives using personalized AI-native training simulations and advanced coaching analytics.

[Devpost](https://devpost.com/software/ming-management-training-a-personalized-ai-native-l-d-coach) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[multi_agent]]
**domain** [[labor_employment]]
**user** [[developer]]
  <sub>weak: transcript_audio</sub>

**stack** ai-native, cedaros, cloudflare, gemini, github, google-natural-language-processing-api, mastra, mcp, multi-agentic-ai, next.js, react, shadcn, tailwindcss, typescript

## How they structured the write-up

- what it does
- what inspired us:
- what we learned:
- how we built our project:
- the challenges we faced:
- what’s next for ming management training:

## Body

The main interface of Ming, featuring realtime voice chat, live sentiment analysis, and a detailed scenario overview. Our analysis page, with an annotated transcript, summary, and voice-integrated chat to receive further feedback. LLM architecture. Full-stack infrastructure. The landing page. What it does Ming Management Training is an AI-native application that uses a multi-agent LLM architecture to help current and aspiring engineers-turned-managers practice managing real-world workplace scenarios. Users engage in role-playing difficult conversations (performance reviews, conflict resolution, or layoffs) with LLM-driven NPCs, receiving detailed analysis, actionable feedback, and new personalized scenarios based on their managerial strengths and weaknesses analyzed from the conversations. What Inspired Us: A desire to help people learn and build skills As AI automation reshapes work, which jobs will endure, and how do we bridge displaced workers into roles the industry needs in this AI economy? We realized that there is a lack of efficient and affordable training for the soft skills needed in technical managerial roles High cost of hiring new managers compared to upskilling in-house technical employees, and may lack in-depth technical expertise, culture understanding and connection to the people in the company. Desire to improve upon the generic and ineffective training solutions of the present ( cough cough AlcoholEdu training) What if engineers could be trained to become managers who combine deep technical expertise with excellent managerial skills? What we learned: How to implement scalable multi-agentic architecture Effective teamwork makes the dream work! (fr tho) The best approach to building something is just to get started - we had setbacks and dead ends, but we were always making progress Supplemented human capabilities with LLM-targeted feedback Plan ahead! 8 PM Friday is when you start coding, not when you start ideating How we built our project: First design server & multi-agentic architecture Divide the task based on expertise and component structure (e.g., one for layout, another for conversation UI etc) Next.js front-end with React, Tailwind, and ShadCN CedarOS to integrate all of the above with all of the below Mastra backend connected to Gemini APIs (LLM and Sentiment-Analysis) Deployed full stack to Cloudflare, hosted on our own domain The challenges we faced: Shipping to Production: We initially bundled our Next.js and Mastra server as a single server with Cloudflare Wrangler, but had to split them into two separate servers and point our Next.js server at Mastra. Implementing multi-agentic workflow & orchestrator LLM pipelines (see diagrams) Validating our idea with an MVP - it was tricky knowing when we had actually achieved our MVP and deciding where to go next Integrating variable outputs from LLMs caused us to rewrite our parser ~6 times We tried live video generation, but it was too expensive (~$9/min) and we settled for a pre-generated video Smoothly integrating interdependent components created by different teammates (so many merge conflicts…) What’s next for Ming Management Training: Talk and test with stakeholders Scaling to learn patterns among employees in a specific company culture Multi-conversational-agent scenarios, e.g. resolving a conflict between two coworkers Ultra-low latency agent interactions Immersive AR/VR interactions Seamless mobile support <div