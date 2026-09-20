---
slug: "resonance-ai-1hjbf0"
url: "https://devpost.com/software/resonance-ai-1hjbf0"
title: "Resonance AI"
hackathon: "Qloo LLM Hackathon"
organization: "Qloo"
winner: true
words: 1023
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/health_clinical"
  - "domain/retail_commerce"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Resonance AI

> AI-powered political intelligence that creates culturally authentic campaign messaging

[Devpost](https://devpost.com/software/resonance-ai-1hjbf0) · hackathon [[Qloo LLM Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[health_clinical]] [[retail_commerce]]
**user** [[researcher]]
**substrate** [[geospatial]] [[sensor_telemetry]]

**stack** adk, gcp, gemini, imagen, llm, python, qloo, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for resonance ai

## Body

AI-powered political intelligence that creates culturally authentic campaign messaging Inspiration As a data scientist, I've witnessed technology rapidly transforming every industry - from healthcare to finance to retail. Yet one sector remains surprisingly stagnant: political campaigns. While we have AI revolutionizing customer targeting in e-commerce, political campaigns still rely heavily on outdated methods like cringe-worthy TV attack ads and broad demographic assumptions. This struck me as a massive opportunity. The political campaign industry is worth billions of dollars, dominated by traditional players who haven't embraced the cultural intelligence and AI-powered personalization that modern voters expect. I realized there was real scope to disrupt this market by combining political data analysis with deep cultural insights to create authentic, resonant messaging. What it does ResonanceAI is an AI-powered political campaign intelligence platform that bridges the gap between traditional campaign analytics and modern cultural understanding. It provides: 🎯 Geographic Political Intelligence : Analyzes voter sentiment, candidate popularity, and strategic opportunities across different locations using advanced heatmap analysis. 🎨 Cultural Intelligence : Leverages Qloo's API to understand demographic preferences - from music and entertainment to brand affinities - creating a complete cultural profile of target audiences. 📝 AI-Powered Content Generation : Uses Google's Gemini 2.5 Flash and Imagen4 to create platform-optimized campaign content (social media, email, direct mail, SMS) that authentically connects with specific cultural demographics. 📊 Complete Campaign Packages : Delivers ready-to-deploy materials including copy variants, visual assets, cultural analysis, and deployment strategies. The platform transforms raw political data into culturally intelligent, personalized campaign strategies that actually resonate with voters rather than generic messaging that falls flat. How we built it 🔧 Technical Architecture: Agent Framework : Built using Google's Agent Development Kit (ADK) for intelligent orchestration AI Models : Powered by Gemini 2.5 Flash for analysis and reasoning, Imagen4 for visual content generation Cultural Intelligence : Custom Python wrapper around Qloo's API for demographic and cultural insights Data Processing : Advanced heatmap analysis and geographic targeting algorithms Deployment : Cloud Run for scalable hosting with both API and web UI interfaces 📊 Data Pipeline: Political Analysis : Processes campaign data (coordinates, popularity metrics, strategic segments) Cultural Mapping : Converts political demographics to cultural insights via Qloo API Content Generation : Creates personalized messaging using cultural intelligence Package Assembly : Combines analysis, content, and visuals into deployment-ready campaigns 🏗️ Agent Structure: Political Agent : Core campaign analysis and strategic planning Content Agent : Cultural intelligence and messaging generation Campaign Tools : Complete workflow from analysis to content creation Challenges we ran into ⏰ Time Constraints : This was actually my backup idea! I had another project planned initially, which left me with only 2 days to build ResonanceAI from scratch. Time became the biggest obstacle. 🔍 API Integration : Figuring out Qloo's API structure and building a robust Python wrapper took significant time, especially with limited documentation for some endpoints. 💻 Frontend Limitations : With such tight deadlines, I couldn't build a custom frontend. Had to rely on Streamlit dashboard and ADK's built-in web UI. 🤒 Personal Challenges : Built this entire project while battling COVID, working late nights after my day job. Managing energy levels and focus was tough. 📊 Data Access : Limited access to comprehensive political datasets made testing and validation more challenging than anticipated. Accomplishments that we're proud of 🎯 Unique Market Position : Created something that genuinely fills a gap in the political tech space - combining political intelligence with cultural authenticity in a way I haven't seen before. ⚡ Rapid Development : Built a functioning, deployable AI agent system in just 2 days while working around illness and a full-time job. 🚀 Multi-Platform Deployment : Successfully deployed agents on both Google Cloud Run and Agent Engine, demonstrating scalability and flexibility. 💡 Real Business Potential : This isn't just a hackathon project - it's a genuinely viable business idea with clear revenue potential in a billion-dollar market. 🏥 Perseverance : Pushing through COVID symptoms and exhaustion to deliver something I'm genuinely excited about. What we learned 🎨 Qloo's Potential : Discovered the incredible possibilities of cultural intelligence APIs. Qloo's insights into demographic preferences, entertainment choices, and brand affinities opened up entirely new approaches to audience understanding. ☁️ ADK Mastery : Through this and other recent projects, I've become proficient at deploying AI agents on Google's infrastructure, understanding both Agent Engine and Cloud Run deployment patterns. 📊 Market Gap Recognition : Realized how fragmented the political tech space really is. While there are tools for individual tasks, there's no comprehensive platform that handles the entire workflow from analysis to deployment. 🔗 Integration Complexity : Learned how challenging it can be to integrate multiple AI systems (political analysis + cultural intelligence + content generation) into a cohesive user experience. What's next for Resonance AI 🚀 Immediate Enhancements : Google Search Integration : Add real-time research capabilities to understand current political landscape MCP Server Integration : Connect additional data sources and tools for comprehensive analysis Custom Frontend : Build a polished, campaign-manager-friendly interface 📈 Advanced Features : Automated Outreach : AI-powered email campaigns and phone calls Real-time Insights : Live sentiment tracking and response recommendations Physical Campaign Planning : AI-suggested locations for rallies, canvassing, and in-person events Multi-channel Orchestration : Coordinate messaging across all campaign touchpoints 💼 Business Development : Enterprise Integration : Connect with existing campaign management platforms for expanded data access Revenue Streams : SaaS subscriptions, per-campaign pricing, custom enterprise deployments Market Expansion : Beyond political campaigns to advocacy groups, nonprofits, and issue-based organizations 🎯 Competitive Advantage : From my research, the major players in political tech are either scattered across different niches or focusing on single solutions. I haven't found anything that provides comprehensive real-time insights, automated actions, and end-to-end campaign assistance. ResonanceAI has the potential to become the unified platform that campaigns actually need. The vision is a complete suite of AI-powered campaign tools that understands not just where and who to target, but how to authentically connect with those audiences through culturally intelligent, personalized messaging. Note: Use https://resonanceai.streamlit.app/ for the heatmap comparison Use https://political-agent-service-833868035966.us-central1.run.app/ for the AI agent. Select political_agent from top left window before starting the chat <div