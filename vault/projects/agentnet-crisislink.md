---
slug: "agentnet-crisislink"
url: "https://devpost.com/software/agentnet-crisislink"
title: "AgentResQ"
hackathon: "Agentforce Virtual Hackathon"
organization: "Salesforce"
winner: true
words: 219
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/geospatial"
---

# AgentResQ

> AgentResQ is an AI-powered assistant that automates crisis response—engaging victims, predicting aid demand, creating records, assigning volunteers, and slack updates—all in real time.

[Devpost](https://devpost.com/software/agentnet-crisislink) · hackathon [[Agentforce Virtual Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[geospatial]]

**stack** agent, and-agent-actions-?-ensuring-every-aid-request-is-routed, and-severity.-output-is-displayed-in-real-time-through-a-lightning-web-component.-**automation-&-engagement**-behind-every-chat-is-a-powerful-orchestration-layer-of-flows, apex, api, built-with-einstein-studio, chat, combining-**generative**-and-**predictive**-intelligence-with-salesforce-automation.-**generative-ai**-using-einstein-prompt-builder, einstein, einsteinpredective, flows, forecasts-aid-volume-based-on-crisis-type, glm, gpt

## How they structured the write-up

- 🌍 inspiration
- 🤖 what we built

## Body

AgentResQ techstack and capabilities Experience portal we have built to host AgentResQ AgentResQ use Agent SafeHeaven to see rounded responses with aidtypes from the predictive model, Predictions are created upon crisis record creation LWCs we have built Apex Classes we have built 🌍 Inspiration In times of crisis, victims need immediate support — but most aid systems still rely on manual processes, disconnected teams, and delayed responses. We set out to change that. AgentResQ was born from the idea that AI can do more than just automate — it can respond, predict, and coordinate relief operations with empathy and precision. 🤖 What We Built AgentResQ is a real-time, AI-powered crisis response assistant, built entirely on Salesforce’s Agentforce platform. Through a single conversation, it transforms victim outreach into a fully automated, intelligent aid pipeline. Here’s what AgentResQ does: 🌐 Detects the victim’s location via a custom dummy IP-based API 💬 Engages victims conversationally to collect personal and family details ⚙️ Triggers Salesforce Flows to create Contacts, Cases, Aid Requests, and Line Items ✍️ Uses Einstein Generative Prompt to generate empathetic case subjects and fundraising content 📍 Assigns volunteers based on regional routing logic 📈 Predicts future aid demand using a Einstein Predictive GLM model trained on 100K+ historical records[Agent SafeHeaven] 🔔 Sends real-time fundraising and coordination alerts to Slack <div