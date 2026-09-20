---
slug: "carryover"
url: "https://devpost.com/software/carryover"
title: "Carryover"
hackathon: "Google Cloud Rapid Agent Hackathon"
organization: "Google"
winner: true
words: 784
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/agriculture_food"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/immigration_refugee"
  - "domain/security_privacy"
  - "user/educator_student"
  - "user/government_staff"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# Carryover

> Visa intelligence that protects migrants from agency fraud. Three AI agents on Elasticsearch + Gemini that don't just inform but they detect scams in real time and file real complaints.

[Devpost](https://devpost.com/software/carryover) · hackathon [[Google Cloud Rapid Agent Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[agriculture_food]] [[civic_government]] [[developer_tools]] [[education]] [[finance_payments]] [[immigration_refugee]] [[security_privacy]]
**user** [[educator_student]] [[government_staff]]
**substrate** [[document_pdf]] [[geospatial]]

**stack** elastic-agent-builder, elasticsearch, elser, es-ql, fastapi, firecrawl, gemini-api, google-gemini, mcp, python, react.js, resend, tailwindcss, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for carryover

## Body

Carryover Visa intelligence that protects migrants from agency fraud Three AI agents on Elasticsearch + Gemini that do not just inform, they detect scams in real time and file real complaints. Inspiration Every year migrants lose billions to fake visa agencies promising "guaranteed approval." For many families it is not just money, they sell land or livestock to pay a scammer and lose their one shot at a better life. The cruel part is that the information needed to spot the scam exists, in official policies, refusal statistics, and the patterns of past frauds. It is just scattered and invisible to the person being targeted. We built Carryover to put that intelligence in their hands and to do something most tools never do: act on it. What it does Carryover is a visa intelligence platform powered by three specialist AI agents, orchestrated by a front-door agent called Kibo . Advisor answers official visa requirements, including fees, documents, and processing times, grounded in real government policy with cited sources. Inspector handles fraud detection. Paste an agency post or drop a Telegram handle, and it pulls live posts, indexes them into Elasticsearch, scores each one with ELSER against 1,350+ known scams, and detects phone number and handle reuse across agencies using ES|QL. Reporter is the action agent. On a confirmed scam it files a community warning back into Elasticsearch so the next person is protected, finds the responsible authority's reporting email from crawled government pages, and sends a formal complaint email with a case reference and supporting evidence. The dashboard grades every destination's acceptance odds, calibrated to the user's passport and visa purpose. The scores are honest, not vanity numbers, and update live as users change destination or purpose. How we built it Elasticsearch serves as the system of record and the agents' entire toolset. We use ELSER semantic search over semantic_text fields containing visa policies, known scams, and agency posts. We use ES|QL for analytics and identity reuse detection. All eight specialist tools and both agents live in Elastic Agent Builder and are exposed to Gemini through the Agent Builder MCP server . Google Gemini , through the google-genai SDK, acts as the reasoning layer. It routes questions to the right agents, synthesizes findings into plain language, structures messy policy content, rates fraud risk across languages, performs grounded searches for authority contacts, and drafts complaint letters. Data ingestion includes 5,100+ pages crawled from 20 official immigration authorities using the Elastic Open Crawler. We also scraped public Telegram agency channels, loaded CFPB fraud complaints, and pulled live visa news through Firecrawl. Stack: FastAPI backend, React + TypeScript + Vite + Tailwind frontend, Resend for outbound complaint email, deployed on EasyPanel and Netlify. Challenges we ran into Calibrating honest scores. Early versions showed acceptance rates near 98% for almost every country. We built a per-corridor model that layers editorial openness priors, passport-strength penalties, purpose effects, and live scam pressure so the map reflects reality. A Nigerian work visa reads very differently from an Indian student visa. Scoring posts in any language. Amharic and Hindi scam advertisements scored poorly under English-only heuristics. We moved to a calibrated Gemini rating system that evaluates fraud risk regardless of language. Making multi-agent work visible. Long loading spinners reduce trust, so each agent narrates its actual actions, including pulling Telegram posts, indexing data into Elasticsearch, running ELSER matches, and performing ES|QL checks. Real outbound action, safely. Determining the correct authority email for every corridor required a layered strategy. We use a maintained directory, crawled government sources, and grounded Gemini search, while gracefully degrading when no public reporting address exists. Accomplishments that we're proud of We built an agent that actually does something. Carryover files a real complaint and writes a community warning back into Elasticsearch, creating a feedback loop where every report improves future scam detection. The system is grounded end to end. The same crawled corpus that answers visa policy questions can also provide the authority contact information needed when the Reporter files a complaint. What we learned We learned that building a genuinely agentic system is more about orchestration and grounding than generation. Elastic Agent Builder, ELSER, and ES|QL handled the heavy lifting. Gemini's role was to route, reason, and act on top of trustworthy retrieval. We also learned that showing the work is just as important as doing the work. What's next for Carryover A verified sending domain so complaints deliver directly to authority inboxes. Watchtower alerts that notify users when policies change or new scams appear in a corridor they follow. WhatsApp and Telegram bot delivery so vulnerable users can access the system through tools they already use. A multilingual interface covering the world's highest-volume migration corridors. <div