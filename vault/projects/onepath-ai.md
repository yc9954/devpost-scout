---
slug: "onepath-ai"
url: "https://devpost.com/software/onepath-ai"
title: "OnePath AI"
hackathon: "Agentforce Virtual Hackathon"
organization: "Salesforce"
winner: true
words: 1100
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/civic_government"
  - "domain/disaster_emergency"
  - "domain/health_clinical"
  - "domain/legal_justice"
  - "user/government_staff"
  - "substrate/geospatial"
---

# OnePath AI

> In critical moments, OnePath AI unites Service Cloud, Slack, and Agentforce to instantly brief, assign, and align incident response teams, so nothing is missed when it matters most.

[Devpost](https://devpost.com/software/onepath-ai) · hackathon [[Agentforce Virtual Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[civic_government]] [[disaster_emergency]] [[health_clinical]] [[legal_justice]]
**user** [[government_staff]]
**substrate** [[geospatial]]

**stack** agentforce, apex, flows, prompt-template, salesforce, service, slack

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for onepath ai

## Body

Inspiration We’re passionate about creating technical solutions that make a real difference in people’s lives. Our inspiration for this project comes from a desire to support those doing critical, high-impact work in society—whether they’re in public service, community health, non-profits, or emergency response. These people shouldn't be buried in manual processes. We believe technology should amplify their impact, not get in their way. This project is about designing intelligent automation that lets real humans focus on the meaningful work—while the tech handles the rest. What It Does OnePath AI transforms the critical first moments of incident management. The solution leverages Agentforce, Slack, and Salesforce Service Cloud to automatically and intelligently identify the right stakeholders, generate a clear and structured incident brief, and create an actionable task list - all within Slack. It’s fast, AI-driven, human-centered, and built to support high-pressure teams with clarity and coordination from the very first click, whether they’re working from a desktop or on the go on mobile. By automating incident-response tasks through Agentforce, the solution cuts manual triage and coordination time, freeing agents to focus on resolution instead of administration. When an incident is logged, a dedicated Slack channel is created automatically, the right stakeholders are invited, and an AI-generated brief is posted with a concise summary, clear timeline, and next-step task list—eliminating the minutes (or hours) previously spent assembling the team and writing the incident briefs. Streamlined automation ultimately reduces average handling time, lowering operational costs while increasing capacity without adding headcount. Altogether, this end-to-end automation translates saved hours and faster collaboration into measurable cost savings, and a clear, top-line ROI. Most importantly, the organisation managing the incident can resolve it faster—and in critical situations where lives are at risk, that speed is priceless. How We Built It We built the solution using Salesforce’s out-of-the-box (OOTB) capabilities—primarily Agentforce, Service Cloud, Flow Builder, Slack, and Prompt Templates. Where limitations arose, we extended functionality using Apex to bridge the gaps (particularly in Slack-to-Salesforce interactions). Our goal was to stay as declarative as possible, using Agentforce and Salesforce’s AI capabilities to handle the heavy lifting. By maximising out-of-the-box tools, the solution remains scalable, easy to maintain, and aligned with Salesforce’s continuous innovation. This approach is especially valuable for non-profits, public sector teams, and mission-driven organisations that need future-ready technology without high technical overhead. By embedding Agentforce and AI into the process, we’ve replaced traditionally complex, logic-heavy flows with intelligent automation. Agentforce brings decision-making and task generation to life and Prompt Template providing dynamic text generation and contextual awareness - allowing teams to receive summaries, timelines, and actions in natural language. This not only reduces build complexity but also makes the solution more intuitive and responsive for users in high-pressure environments. Solution Details We began by introducing a custom object to model Incident Response Teams . This allows organisations to configure and maintain dynamic team structures—defining specific roles (e.g. Operations Lead, Legal Advisor, Communications Officer) and mapping them to internal users for each client. This ensured role-based accuracy and accountability from the outset. To generate immediate insight into each incident, we used Salesforce Prompt Templates . These allow us to apply AI intelligence to case records - automatically creating a summary of what occurred and generating a chronological timeline of events . This summary is embedded directly into the Slack canvas, giving every responder instant context. Agentforce was at the heart of our task orchestration. It interprets the nature of the incident, determines what tasks need to be created, and dynamically assigns them based on the configured team roles. This eliminated manual task creation and ensured that the right people are always notified, fast. We integrated Slack to enable real-time collaboration. Using Slack’s Canvas API, we automatically generate a canvas for each incident—containing the AI-generated summary, timeline, people involved, and actionable tasks. This allows response teams to coordinate from anywhere, whether they’re in the field or at their desk. Finally, we used Salesforce Flows to bring everything together. Flows orchestrate the entire process: triggering case creation, reading the Incident Response Team configuration, launching Agentforce to generate tasks, invoking prompt templates for AI summaries, and sending everything to Slack. This no-code/low-code orchestration layer ensures maintainability while still delivering powerful automation. The result is a connected, intelligent response framework—built to support organisations during their most critical moments. The solution showcases the power of combining three key capabilities: Slack, Flow and Agentforce. By using Flow as the central orchestrator, we’re able to autonomously trigger Agentforce and Prompt Templates when needed, based on incident context. This architecture avoids the complexity of having Agentforce manage multiple Flows, and instead positions it as a powerful, on-demand service within a scalable, flow-driven system. This approach provides greater technical control, modularity, and alignment with Salesforce's out-of-the-box functionality. It enables seamless use of Slack's native flow actions and by anchoring the solution in Flow, we’ve created a flexible, scalable framework where Slack, Agentforce, and AI collaborate within a unified, automation-first incident response model. Challenges We Ran Into We encountered challenges when trying to programmatically connect a custom Slack app to Salesforce, particularly with joining channels dynamically. Slack's API limitations required custom Apex workarounds—and we still couldn’t fully meet the need to join private channels, which we'll explore with future architecture enhancements. These gaps tested our integration design but opened up valuable insights for future solutions. Accomplishments That We're Proud Of We’ve created a polished, modular package that functions like a product—and can be implemented by any organisation needing smarter incident coordination. It aligns perfectly with our values: empowering mission-driven teams, supporting people in high-stakes roles, and ensuring technology helps them—not hinders them. We’re proud to offer a tool that’s elegant, practical, and ready to drive real-world impact. What We Learned We learned that even the most intuitive platforms have integration edge cases, and designing around limitations can lead to stronger architectural thinking. We also saw firsthand the power of combining low-code tools with targeted custom code to create scalable, adaptable solutions. What's Next for OnePath AI We see OnePath AI as a launchpad for smarter teamwork. Whether your organisation already use Slack or not, this solution is a compelling entry point—especially for incident response teams who need instant clarity and collaboration. From here, the product can grow to support mid-incident coordination, post-incident review, and swarming capabilities. Looking ahead, we envision a broader role for Agentforce in ongoing incident management and aftercare. We also plan to explore Einstein summarisation and AI-driven swarming logic to enhance collaboration. Eventually, we want to tie the solution into predictive analytics—so response doesn’t just begin when something happens, but before it does. <div