---
slug: "sweet-by-metabolic-company-of-calhacks"
url: "https://devpost.com/software/sweet-by-metabolic-company-of-calhacks"
title: "Sweet by Metabolic Company of CalHacks"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 598
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Sweet by Metabolic Company of CalHacks

> Sweet is an iMessage native diabetes management AI assistant.

[Devpost](https://devpost.com/software/sweet-by-metabolic-company-of-calhacks) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]]
**domain** [[agriculture_food]] [[developer_tools]] [[health_clinical]]
**user** [[developer]] [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** dexcomshareapi, fastmcp, geminiapi, poke, python, twilioapi, uvicorn

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sweet by metabolic company of calhacks

## Body

Dexcom CGM Poke - MCP Automation Flow Chart Inspiration Living with diabetes means juggling between multiple tasks everyday from checking glucose levels to calculating carbs to giving right dosing of insulin, all while trying to live normally. We thought, what if instead of using complex apps and manual tracking, you could simply text your phone like you're talking to a friend, and get instant, intelligent help with your diabetes management? What it does Sweet lets users manage diabetes through conversational text messages with an AI assistant. The AI analyzes meals, monitors glucose levels, and calculates insulin doses using real-time data integration. Users text the Poke AI to get instant health insights, and the system learns patterns over time to provide personalized recommendations. Real-time Dexcom CGM integration AI-powered meal analysis from photos Personalized insulin dose calculations Glucose pattern tracking based on food/activity and send alerts when needed SMS-based conversational interface How we built it Sweet is built as an MCP (Model Context Protocol) server that integrates multiple APIs and AI services: FastMCP Framework : Used FastMCP as the foundation for our MCP server, enabling seamless integration with Poke's conversational interface Dexcom Integration : Connected to Dexcom's Share API for real-time CGM data retrieval and glucose trend analysis AI-Powered Intelligence : Integrated Gemini API for NLP, food recognition, and personalized nutrition analysis SMS Communication : Implemented Twilio for reliable text message alerts in an urgent situation Python Backend : Built custom modules for insulin calculation algorithms, carb ratio management, and pattern recognition logic Challenges we ran into MCP Learning Curve : First-time developers struggling with Model Context Protocol architecture and tool structuring Stateless Communication : Managing HTTP requests without persistent state for real-time health data Multi-API Coordination : Synchronizing Dexcom, Gemini, and Twilio APIs in a single conversational flow Medical Data Reliability : Ensuring accurate, safe handling of critical health information under all conditions. (Our tool is still in its early stages, so insulin dosage and macros predictions may not yet be fully reliable.) Dexcom API Complexity : Navigating between Sandbox and Share APIs, understanding authentication flows, and parsing complex glucose data structures Accomplishments that we're proud of Seamless Multi-API Integration : Successfully unified Dexcom, Gemini AI, and Twilio into the MCP server Natural Conversation Interface : Transformed complex diabetes management into simple text-based interactions Adaptive Pattern Learning : Created a system that learns and personalizes to individual users over time Real Impact Potential : Built something that could genuinely reduce the daily burden of diabetes management What we learned We learned that working with healthcare data requires serious responsibility. Even a tiny mistake can have big consequences. Our goal is to build something that genuinely helps people, but safety always comes first. Creating our first healthcare MCP taught us how important it is to spot patterns and use context, so our tool can truly support users where it matters. What's next for Sweet by Metabolic Company of CalHacks Multi-Platform Expansion : Bring Sweet to Discord, Slack, WhatsApp, and native mobile apps Predictive Intelligence : ML-powered glucose forecasting and smart meal database that learns from users Clinical Integration : Web dashboard with comprehensive weekly/monthly reports for patients, healthcare provider access. Connect Poke with closed loop insulin pump for insulin dosage automation. Community Platform : Enable users to share interesting use cases and strategied they find while using the chat interface. Disclaimer: Sweet is still in development. While real-time glucose data is pulled from your sensor, macro tracking and insulin dosage suggestions are early-stage and may not be fully reliable. Please do not rely on these features for critical decisions. <div