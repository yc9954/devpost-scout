---
slug: "sentinelai-devops-security-agent"
url: "https://devpost.com/software/sentinelai-devops-security-agent"
title: "SentinelAI – DevOps Security Agent"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 368
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "substrate/video_visual"
---

# SentinelAI – DevOps Security Agent

> An AI-powered surveillance agent for real-time security and DevOps incident automation.

[Devpost](https://devpost.com/software/sentinelai-devops-security-agent) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[developer_tools]]
**substrate** [[video_visual]]

**stack** docker, flask, jenkins, keras, material-ui, opencv, postgresql, python, react.js, slack-api, tensorflow

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sentinelai
- what's next for sentinelai – devops security agent

## Body

Inspiration What it does Inspiration During a college project on AI-powered CCTV surveillance, I noticed how many security incidents and DevOps alerts go unnoticed because of information overload. Traditional monitoring tools generate thousands of alerts daily, and security teams struggle to prioritize what matters. This inspired me to build SentinelAI — an intelligent agent that acts as a 24/7 security sentinel. What it does SentinelAI is an AI-powered surveillance and DevOps security agent that: Monitors real-time CCTV feeds and system logs Detects anomalies and security threats using machine learning Automatically creates incident tickets and alerts the right teams Provides a dashboard for security teams to track and respond to incidents How we built it We built SentinelAI using Python for the backend, with TensorFlow/Keras for the AI model training. The system uses OpenCV for image processing on CCTV feeds, Flask for the REST API, and PostgreSQL for storing incident data. For the frontend dashboard, we used React.js with a Material-UI component library. We integrated with DevOps tools like Jenkins and Slack for automated incident notifications. Challenges we ran into The biggest challenge was training the AI model to accurately distinguish between normal activity and actual security threats. We also faced difficulties integrating multiple data sources (CCTV feeds, system logs, cloud monitoring) into a unified pipeline. Optimizing real-time processing latency was another major hurdle. Accomplishments that we're proud of Built a working AI model that can detect suspicious activity with high accuracy Created a real-time dashboard that updates every 5 seconds Successfully integrated with Slack and email for automated alerts Achieved sub-second response time for critical security incidents What we learned We learned how to build end-to-end AI systems, from data collection to model deployment. We also gained experience in DevOps practices, cloud infrastructure, and security monitoring. Most importantly, we learned how to work as a team under deadline pressure. What's next for SentinelAI Add support for multiple camera feeds simultaneously Integrate with more DevOps tools (PagerDuty, Jira, ServiceNow) Implement advanced anomaly detection using deep learning Add mobile app support for on-the-go monitoring ## How we built it Challenges we ran into Accomplishments that we're proud of What we learned What's next for SentinelAI – DevOps Security Agent <div