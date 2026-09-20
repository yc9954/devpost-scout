---
slug: "ai-mon-artificial-intelligence-activity-observability"
url: "https://devpost.com/software/ai-mon-artificial-intelligence-activity-observability"
title: "AI-Mon: Artificial Intelligence Activity Observability"
hackathon: "TiDB Future App Hackathon 2023"
organization: "PingCAP"
winner: true
words: 764
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# AI-Mon: Artificial Intelligence Activity Observability

> AI-Mon(aka. AI Monitoring) is a advanced successor to Ira (Now a browser extension OSS to record cut/copy/paste events on websites) especially to monitor data with the popularity of AI driven chatbots

[Devpost](https://devpost.com/software/ai-mon-artificial-intelligence-activity-observability) · hackathon [[TiDB Future App Hackathon 2023]]

## Facets

**mechanism** [[cross_origin_web]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[security_privacy]]
**substrate** [[document_pdf]] [[structured_db]] [[web_dom]]

**stack** browser-extension, golang, react, svelte, tidb-serverless, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- why tidb as the preferred database
- why vercel
- challenges we ran into
- accomplishments that we're proud of
- what's next for ai-mon: artificial intelligence activity observability
- concluding notes

## Body

Architecture Diagram Inspiration AI Popularity with GPT based formats is increasing. Making our lives easier, faster, efficient letting us focus on creativity and orchestrating ideas. However, for organization there is a new threat evolving. Lets understand how; * Evolving users search behaviour with the advent of AI Bots * Lets take a minute to understand how traditionally users would search on search engines Traditional way: Input keywords Search multiple websites … Mix + Match logic to suite best among the various browsed websites Apply to create his/her own content Search pattern with AI Chatbot search Input keywords / existing / personalized content Iterate changes with the Chatbots Get direct answers Apply AI is helping find information with ease that everyone is adopting to this. However, as a employee one may end up uploading / copy pasting your organizations information out of pure innocence or in an attempt to prove smartness and efficiency with your bosses or peers. Pasting content on site which assist Ever tempted to paste content on site which assist with grammar correction / code difference checker. That's dangerous too, isn't it? The general awareness gap among employees While organizations conduct training sessions for employees to make aware of the policies of data security, the gap often continues to exists for reasons listed below. Policies vary as you move from organization to organization Time difference between Joining and policy training sessions Recall memory (going on to a website to download .exe, although it looks trusted) Accidental (This websites helps correct grammar, why not paste content there) Miscommunication (Upload document on Drive, it meant company drive not personal drive / share link within organization email not across web and many more examples) While most peoples consciousness stops them from doing, But with AI adoption at an early stage (college life), we tend to consider it as the new normal With some questions in mind; Organization are not blocking sites but are creating policies around it. Why? because they want employees to adopt to AI. They also intend to not sound against AI technology Proxies cant detect if an employee uploaded (pasted) the content or not. What it does AI-Mon is a successor to one of my other projects Ira . A browser extension to make people aware of data security breach. AI-Mon goes beyond just making aware. It does the following; Captures event from users: CUT/COPY/PASTE Records them to a centralized server Applies text analytics (currently ChatGPT for demonstration) Makes dashboards available to security adminstrators How we built it AI-Mon consists of the following; Project Directory Structure (mono repo) analytics: Reporting frontend and backend (Vue3 + Golang + TiDB) backend: API for data ingestion from browser extension (Golang + TiDB) content-tagging: Containerized Job to tag content by user id by Integrating with ChatGPT API prompts (Golang + ChatGPT + TiDB) docs: Host the policy (json file) that decides which sites to track. (As a github.io pages) extension: The browser extension that detects events from websites based on the policy defined (Svelte) simulation: Create requests fake users, domains and content ingestion based on 200 dataset of stackoverflow questions (otherwise, demo might have boring numbers :) ) at 2 requests per 10 seconds (Golang + TiDB) Why TiDB as the preferred database Best HTAP Serverless (Reduced overheads of maintenance, reduced savings since data ingestions may not happen throughout the day) Best of both worlds (Row and Column storages) for fast analytics Why Vercel Quick and Simple Serverless (No overheads of scaling + highly available without needing to be be bare full day costs) Easy deployment Challenges we ran into Apart from the tons of challenges that happened since I am not the UI / CSS/ frontend dev.where the little things to keep in mind with browser extensions Choosing the Charting library Shadow DOM events capturing is still a pain point. Looking forward for help However, the documentation for TiDB and Vercel are sufficient to get you going Accomplishments that we're proud of Making OSS Integrating with AI tool to prevent data leaks to AI What's next for AI-Mon: Artificial Intelligence Activity Observability Migrating the reporting interface to a full fledged Business Intelligence platform (mostly an OSS), thereby focusing on extending features rather than reporting interface Drill down reporting Additional derivations from the data captured Integrating AI-Mon and Ira into one browser extension Plugins for integrating with other text/keywords analytics providers to constraint data going to open world 6.Re-Architecting ingestion components for production readiness and load Keeping it OSS :) Concluding notes Hoping that this project cover the all 3 categories in one application. :P <div