---
slug: "agentic-analytics-readiness"
url: "https://devpost.com/software/agentic-analytics-readiness"
title: "Agentic Analytics Readiness"
hackathon: "Tableau Next Virtual Hackathon"
organization: "Tableau"
winner: true
words: 1102
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "mechanism/vision_ocr"
  - "domain/health_clinical"
  - "substrate/sensor_telemetry"
  - "substrate/web_dom"
---

# Agentic Analytics Readiness

> Agentic-ready analytics starts here: Tableau Next becomes your hub to triage, take action, and continuously improve the analytics assets in Tableau Cloud your team already relies on.

[Devpost](https://devpost.com/software/agentic-analytics-readiness) · hackathon [[Tableau Next Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[simulation_digital_twin]] [[vision_ocr]]
**domain** [[health_clinical]]
**substrate** [[sensor_telemetry]] [[web_dom]]

**stack** agentforce, chatgpt, flow, graphql, salesforce, slack, tableau-cloud, tableau-desktop, tableau-metadata-api, tableau-prep

## How they structured the write-up

- 🔧 the solution
- 📏 defining readiness
- 🧭 the command center
- 📚 what i learned
- 🧪 challenges i faced
- 🐣 easter egg
- 🧵 final reflections

## Body

Agentic Analytics Readiness The Opportunity The Path to Agentic Analytics A Framework for Action Executive Overview of Agentic Analytics Readiness Scorecard View with Readiness Status & Impact Metric for Data Sources Enrichment Triage where Team Members Can Take Action Tableau Next Semantic Model Fueling Dashboards & Actions Salesforce Flow of Action kicked-off by Enrichment Triage View Automated Messages and Interaction with Agents in Slack Metrics from Overview in Slack Canvas The Result Easter Egg - These custom AI instructions didn't make the demo! 💜 Project Story: Agentic Analytics Readiness I was inspired to create this solution after reflecting on the current realities of analytics inside organizations. For years, we’ve heard the same advice about how to become data-driven , but we’ve never been given a clear path forward. Now that AI is more accessible than ever, there’s a unique opportunity to redefine what analytics can be — and to finally close the gap between data and decision-making. At this year’s Tableau Conference , I noticed something in the room: concern. Not just about AI itself, but about what it would require of us. It wasn’t until later that it clicked. Many of my peers weren’t afraid of AI. They were overwhelmed by the existing analytics problems they haven’t been able to solve. Adding AI just sounded like more complexity and disappointment. But I saw something different. I’ve been obsessed with Tableau since I started using it in 2015 because it gave people a way to connect with their data, learn from it, ask better questions, and ultimately make better decisions. I realized what we need now isn’t to start from scratch or reinvent the core of what analytics is. We need a framework . Something to help analytics teams take what they already have and make it stronger, more usable, and ready for the agentic era. Something they could be proud of. 🔧 The Solution That realization became the foundation of my solution: A workflow that starts with the analytics you already have in Tableau Cloud (or Server), connects to Data Cloud for unified access, and moves through Tableau Next to add metrics, context, and intelligence. Ultimately enabling teams to monitor, triage, and take action. All while becoming agentic analytics ready. It’s an end-to-end readiness loop, built with the Salesforce ecosystem as its engine. I knew from experience that Tableau Cloud provides rich usage data through Admin Insights , like which data sources are used, where they live, and how many users rely on them. I also tapped into the Metadata API for a deeper view of field-level details and lineage. That became the foundation for my readiness model. 📏 Defining Readiness To measure the maturity of a Tableau environment through the lens of agentic analytics, I created a measurement framework across four key pillars : Data Reliability – freshness and certification Semantic Enrichment – naming, descriptions, and context Signal Strength – usage, dependencies, access volume Feedback Validation – agent deployment and trust signals Once I connected all the data and began building dashboards, the next step came naturally: Could I take a set of dashboards built to measure readiness and turn them into a living system that guides teams to improve? 🧭 The Command Center That’s what led me to build the Agentic Analytics Readiness Command Center , complete with: Metrics and dashboards A triage workflow built in Flow Slack integration for real-time collaboration An Agentforce assistant named VISTA (Visualization & Insights Team Assistant) This gives analytics teams a real path forward. Starting with what they already have and empowering them to improve trust, increase visibility, and support AI adoption with clarity. 📚 What I Learned While I’m deeply experienced in Tableau, most of the Salesforce platform was new to me. My only previous experience was embedding dashboards in Visualforce and constructing URL actions to Salesforce records. But through this project, I came to appreciate the power of the Salesforce platform, especially the seamless connectivity across: Tableau Next Data Cloud Flow Slack Agentforce Researching past hackathons helped me understand what taking action really means in the Salesforce context, and that’s when the final shape of the solution came into focus. 🧪 Challenges I Faced Creating synthetic data that mimicked real organizational behavior (and simulated improvement over time) was tough. I relied heavily on Tableau Prep to model the data and visualize the shape as I was building it. I designed proprietary scoring logic for things like field description verbosity and freshness. If I had more time, I would've loved to incorporate advanced modeling concepts, but time constraints forced me to keep it simple. I also hard-coded the trustworthiness score of deployed content due to the synthetic nature of the data. I'd love to have had the opportunity to dive into the data generated from users interacting with agents and include it. I had to retrain my brain from the Tableau world of “build anything, anytime” to the Salesforce mindset of structure, lineage, and governance . At first, that structure felt restrictive, but over time, I saw how powerful it is. It made me think differently about the relationships and accountability that analytics teams often overlook or deprioritize. 🐣 Easter Egg Some of the things I wanted to show didn't make the demo! With only 5 minutes to share, some things had to be cut. One of those was working with Concierge alongside the visualizations. I built out custom instructions via Business Preferences in the semantic model for interactivity and tested it with many of the data sources to see just how much insight I could glean from the information contained in the data model. It also helped me identify the right example for my demo. 🧵 Final Reflections I leaned heavily on Trailhead, help documentation, and the videos provided by the hackathon team. It exposed me to a lot of new learning and understanding. But, what made this project special to me is that the tools were all there. Any idea I had could be brought to life. I just had to research the tools and wire them up. This project reflects everything I love about analytics: Helping people get clarity and democratizing information Building systems that evolve and support improvement Addressing the oft-neglected areas of analytics Turning data into action The saddest part for me is that at the close of this hackathon, I have to move on — whereas I'd much rather take what I've learned and reality-test it for an organization as soon as possible. But I'm left with a hopeful thought: This is our chance to make analytics what it was always meant to be. 💜 <div