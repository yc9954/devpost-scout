---
slug: "concierge-1tjlf5"
url: "https://devpost.com/software/concierge-1tjlf5"
title: "Concierge"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 648
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/structural_withholding"
  - "domain/retail_commerce"
  - "substrate/structured_db"
---

# Concierge

> Stop guessing gifts! Concierge lets 2 Poke agents collaborate with shared context across your email, the web, and your texts, then auto-finds and configures the perfect buy via Browserbase web agents.

[Devpost](https://devpost.com/software/concierge-1tjlf5) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]] [[structural_withholding]]
**domain** [[retail_commerce]]
**substrate** [[structured_db]]

**stack** browserbase, bun, fastmcp, next.js, openai-platform, poke, sqlite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for concierge

## Body

Home page Detailed reasoning view Chain of thought visualization Architecture Chat view Inspiration So much of modern life is hyper-connected and still strangely distant. You care about the people in your life, but between work, family, and everything else, the little moments slip by; Remembering a friend’s favorite color, noticing a new hobby, picking a gift that says “I know you.” Gift-giving used to be how we showed "I was paying attention", but now it feels like another task on an impossible list. We wanted to bring back that sense of human connection in a world of disconnect. Concierge reminds you what you already know, and helps people show up for each other more thoughtfully. What it does Concierge is an Agentic gift-giving workflow built on top of Poke that helps you find deeply personalized gifts through peer-to-peer agent collaboration and research. When you want to buy a gift for someone, your agent talks to their agent. Your recipient’s agent represents their tastes and preferences, and runs an autonomous iMessage subagent that validates gift hypotheses by searching through the recipient’s broader message history, far more than the gSuite knowledge base Poke provides. Concierge recommendations aren’t generic; they’re grounded in real evidence. It then returns a small set of gift ideas with message citations (and surrounding context) showing exactly why each gift fits. Finally, a browser automation agent uses Browserbase + Stagehand to find the right gift, configure the right variant (size, color, model), and generate a ready-to-checkout link with an estimated final price. How we built it We built Concierge as a web app with a real-time dashboard (Next.js + FastMCP) that visualizes agent-to-agent negotiation and tunes the user into a gift ideating chain of thought tree. Under the hood, we extended Poke via MCP servers: a Poke-to-Poke MCP for agent communication, an iMessage Query MCP that searches the local macOS iMessage database using structured SQL queries, and a Browserbase MCP wrapper for shopping workflows. Poke B (the recipient’s agent) orchestrates the end-to-end process: generating hypotheses for , spawning the iMessage subagent loop, synthesizing validated ideas, and calling the browser agent to produce checkout links. We store session metadata and visualizations, but sensitive message data stays local. Challenges we ran into The biggest challenge was balancing “wow” personalization with privacy and reliability. iMessage data is messy, unstructured, and incredibly sensitive. We needed tooling that could search it quickly, extract context, and produce citations without dumping a user’s entire private life into an LLM prompt. Browser automation was also challenging, retail sites vary wildly, and checkouts can break. We had to scope carefully and focus on a flow we could make stable for a demo. Accomplishments that we're proud of We’re proud that Concierge feels human. It doesn’t just recommend “a gift”; it shows the reasoning and evidence behind personalization, which makes it trustworthy. We also built a compelling agent visualization that demonstrates autonomous search and hypothesis refinement in real time. And we integrated real-world tools (Poke’s GSuite knowledge store + iMessage search + Browserbase checkout automation) to prove this can work at scale for anyone. What we learned We learned that great agent products aren’t just about model intelligence. Instead, they’re about the memory, constraints, and interfaces around the model. Evidence-backed personalization is dramatically more convincing than generic suggestions. We also learned that “agent-to-agent” is a powerful metaphor for consent, representation, and trust: the recipient’s agent can advocate for them, even in commerce. What's next for Concierge Next, we want to expand beyond gifting into a true “preferences marketplace” where your agent can represent you across experiences, gifts, recommendations, group plans, and purchases, while keeping you in control. We’d add stronger consent flows, better redaction controls, richer preference modeling, and broader retailer support. The long-term vision is simple: use AI to help people understand each other better, and make everyday acts of care easier and more meaningful. <div