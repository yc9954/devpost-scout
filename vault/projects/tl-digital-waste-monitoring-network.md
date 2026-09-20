---
slug: "tl-digital-waste-monitoring-network"
url: "https://devpost.com/software/tl-digital-waste-monitoring-network"
title: "TL Digital Waste Monitoring Network"
hackathon: "Global AI Agents League"
organization: "Fetch.ai"
winner: true
words: 1132
team_size: 1
has_repo: false
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/multi_agent"
  - "domain/civic_government"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "user/developer"
  - "user/general_public"
  - "user/researcher"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# TL Digital Waste Monitoring Network

> AI agents and community reporting to transform Timor-Leste's waste management through intelligent analysis, hotspot detection, and data-driven cleanup prioritization.

[Devpost](https://devpost.com/software/tl-digital-waste-monitoring-network) · hackathon [[Global AI Agents League]]

## Facets

**mechanism** [[multi_agent]]
**domain** [[civic_government]] [[developer_tools]] [[disaster_emergency]]
**user** [[developer]] [[general_public]] [[researcher]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** agentverse.ai, amazon-web-services, asi1.ai, fetch.ai-sdk, flask, flutter/dart, mysql, next.js, python, s3

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for tl digital waste monitoring network

## Body

Agents on Agentverse Make Report and see the log Public Dashboard - Home Public Dashboard - All Waste Reports Public Dashboard - Report Details Public Dashboard - Maps Public Dashboard - Hotspots Public Dashboard - Leaderboard Our Repositories Mobile Application for make report TL Digital Waste Monitoring Network Inspiration While researching environmental issues in Timor-Leste, I found a JICA study showing Dili creates more than 300 tons of waste every day, but over 100 tons never gets collected. This waste blocks drains during rainy seasons, causing floods and health problems. The old ways of managing waste weren't working well because of limited resources and poor coordination. Living in Dili, I saw these problems myself - plastic trash piling up in streets, blocked waterways during rain, and people having no good way to report waste problems. I thought combining AI technology with community help could create a powerful solution to fix these issues. What it does The TL Digital Waste Monitoring Network creates a complete system for waste management in Timor-Leste through: Citizen Reporting : A mobile app lets people report waste problems by taking photos, marking locations, and adding descriptions. AI-Powered Analysis : Two AI agents process these reports: Reporting Agent : Handles report submission, image storage, and agent coordination Analysis Agent : Uses ASI-1 Mini to analyze waste images, identify waste types, check how serious the problem is, and spot possible environmental impacts Hotspot Detection : Automatically finds areas with multiple waste reports using special grouping methods, helping officials know where to clean up first. Public Dashboard : Shows waste data across Dili with interactive maps, charts, and community leaderboards to encourage participation. System Architecture How we built it I built the system using several connected parts: AI Agents on Agentverse : Made two specialized agents using Fetch.ai's SDK Set up communication between agents through Agentverse messaging Connected ASI-1 Mini for image analysis Mobile Application : Built with Flutter so it works on different phones Made it work well with slow internet in Timor-Leste Backend Infrastructure : Created a secure API with Flask and login protection Designed a database for waste management data Set up AWS S3 for storing images Public Dashboard : Built with Next.js for a fast, responsive website Added interactive maps with Leaflet Created charts and graphs with Tremor and Chart.js I designed the system with Timor-Leste's specific challenges in mind - poor internet, different waste issues, and the need for community involvement. TL Waste Report App interface for citizens to submit and track waste reports TL Waste Dashboard showing waste distribution, analytics, and hotspots across Dili Challenges we ran into Building this system had several tough challenges: Agent Communication : Getting the AI agents to talk to each other reliably required careful work on message handling and error recovery. Image Analysis Balance : Finding the right balance between accurate waste identification and fast processing took lots of testing with ASI-1 Mini. Working with Limited Infrastructure : Making the system work with Timor-Leste's slow internet required optimizations like image compression and offline features. Complex Database Design : Creating a database that could handle location data, user accounts, and analysis results needed careful planning. Accurate Hotspot Finding : Building an algorithm that correctly identified waste problem areas without false alarms took several tries to get right. Accomplishments that we're proud of I'm especially proud of: Complete System Integration : Building a full system from mobile reporting to AI analysis to visualization dashboard. Successful AI Integration : Getting ASI-1 Mini to accurately analyze waste images. Effective Use of Agentverse : Using Fetch.ai's Agentverse platform for agent discovery, registration, and communication. Smart Hotspot Detection : Developing an algorithm that accurately finds waste problem areas. User-Friendly Design : Creating easy-to-use interfaces for both citizens and authorities that work well in Timor-Leste. What We Learned This project taught me important lessons about: Working with AI Agents : I learned how to use Fetch.ai's Agentverse platform to create AI agents that talk to each other. I had to figure out how to manage agent identities, pass messages between them, and design a system where each agent has a clear job. With Agentverse, I could register my agents, set up webhooks, and make sure agents could communicate securely. Combining AI with Images : Using ASI-1 Mini showed me how to analyze photos with AI. I learned how to prepare images, convert them to base64 for safe sending, and write good prompts to get accurate waste classification. I realized how powerful it is to combine image AI with organized data for monitoring the environment. Working with Location Data : The project helped me understand how to work with location data by using Haversine calculations in SQL, creating an algorithm to detect waste hotspots, and making location-based searches faster. Building maps and visualizations with this data was hard but worth it. Development for Limited Connectivity : Building for Timor-Leste's poor internet taught me how to make apps work in places with bad connections. I learned to compress images effectively. Community-Focused Design : Most importantly, I learned how to build systems that get community members involved in solving environmental problems. This meant making easy-to-use interfaces for people with different tech skills, creating feedback so users can see their impact, and adding game-like elements to keep people engaged. What's Next for TL Digital Waste Monitoring Network Our future plans include: Collection Agent : Adding a third agent to coordinate cleanup teams and track progress of waste removal efforts. Smarter Analytics : Building predictive models to forecast waste hotspots before they become critical, using historical data patterns. Government Integration : Working with local authorities to connect the system with official waste management processes and infrastructure. Wider Coverage : Expanding beyond Dili to other areas in Timor-Leste to create a nation-wide monitoring solution. Rewards Program : Creating a reward system for active reporters to increase community participation and engagement. Administrative Dashboard : Developing a comprehensive admin control panel for managing users, reports, and system configuration. Stakeholder Partnerships : Seeking support from NGOs, educational institutions, and government agencies to expand the project's reach and impact. Development Team Expansion : Recruiting skilled developers and environmental specialists to enhance the platform's capabilities and domain expertise. Mobile App Enhancement : Improving the user experience and adding features like offline reporting capabilities for areas with limited connectivity. Community Education Module : Adding educational content about proper waste disposal and environmental protection. AI Enhancements : Refining the waste classification algorithm to handle more specific waste categories and provide better remediation recommendations. Data Integration : Creating APIs to share anonymized waste data with environmental researchers and policymakers. By continuing to develop and expand this system, we aim to create lasting positive impact on waste management in Timor-Leste, transforming how communities monitor and address waste challenges through technology. <div