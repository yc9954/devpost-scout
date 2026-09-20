---
slug: "onboardly-3bp9gt"
url: "https://devpost.com/software/onboardly-3bp9gt"
title: "Onboardly"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 845
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/video_visual"
---

# Onboardly

> automate onboarding and training + realtime coaching

[Devpost](https://devpost.com/software/onboardly-3bp9gt) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]] [[runtime_tool_creation]]
**domain** [[developer_tools]] [[education]] [[labor_employment]]
  <sub>weak: supply_logistics</sub>
**user** [[developer]]
**substrate** [[code_repository]] [[video_visual]]

**stack** ai, api, chrome, extension, flask, gooogle, groq, ics, jira, jora, manifest, node.js, react, react-native

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for onboardly

## Body

Inspiration We were inspired by the massive efficiency gap in technical onboarding. Companies often spend days manually provisioning accounts, setting up security, and explaining the same basic cloud concepts repeatedly. This process is intimidating, prone to human error, and lacks real-time guidance for new hires. Our goal was to eliminate this friction entirely, creating an AI that doesn't just create tickets, but actively guarantees a smooth, secure, and educational Day 1 experience by automating both the company-side security setup and the user's hands-on learning process. What it does Onboardly is a Full-Stack, AI-Powered Onboarding Orchestrator that seamlessly bridges IT provisioning and user coaching. For the Company (Automation): From a single form trigger, Onboardly uses the Groq AI to dynamically generate an 8-step, role-specific curriculum (e.g., GCloud training for an SWE Intern). It then uses Jira's API to instantly create a master Epic and all sub-tasks, and SendGrid to deliver a personalized welcome email with a downloadable calendar invite, all assigned directly to the new hire. For the Intern (AI Coach Extension): Once the intern clicks the Jira link and navigates to the Google Cloud Console, our custom Chrome Extension injects an AI Coach panel. This panel uses Gemini Vision AI to capture and analyze the screen, providing real-time, step-by-step guidance on how to complete each task—like a senior developer looking over their shoulder. The entire workflow is tracked, and when the final task is complete, the system automatically transitions the main Jira Epic to DONE. How we built it We built Onboardly using a clean, three-part architecture. 1. The Provisioning Engine (Node.js/Express): This handles the pre-onboarding setup, orchestrating API calls to Groq for curriculum generation, and using the Jira API to create and assign the entire task hierarchy. 2. The AI Brain (Python/Flask with Gemini): This server exposes the vision endpoints. It utilizes Gemini 2.0 Flash for low-latency visual analysis of the screenshot and Gemini 2.5 Pro for sophisticated reasoning and generating clear coaching instructions. 3. The AI Coach Frontend (Chrome Extension): This utilizes a Background Service Worker to securely capture the visible tab screenshot, which the Content Script then sends to the Python backend. The Content Script then renders the real-time coaching UI directly onto the Google Cloud Console interface, providing the interactive guidance needed to complete the Jira tasks. Challenges we ran into The primary challenges involved navigating complex and often fragile enterprise APIs. Jira Provisioning was the biggest obstacle: We faced persistent issues finding the correct internal issue type IDs (10001, 10004) and dealing with the obscure "Epic Name" field ID, which required removal for our simple project. Furthermore, the Jira API user invite process consistently failed on the free tier. We bypassed this by implementing a feature to automatically assign the Epic to the manager's account, ensuring the demo user had instant, authorized access to the tasks. Secondly, AI Key Quotas blocked our progress with an insufficient_quota error, which we resolved by performing a real-time migration to Groq AI's compatible API, maintaining our dynamic curriculum feature. Accomplishments that we're proud of We are most proud of achieving true, end-to-end automation of a complex business process within a short hackathon window. This includes: 1. Zero-Touch Provisioning: Successfully creating a Jira Epic, 8 sub-tasks, and sending a personalized welcome email with a downloadable calendar invite—all from a single Node.js trigger. 2. Dynamic Curriculum: Using Groq AI to generate a highly detailed, accurate 8-step GCloud curriculum in under one second. 3. The Wow Factor: Seamlessly integrating real-time Gemini Vision coaching that actually understands what the user is seeing on a complex external site (GCP Console) and guiding them to complete the automated tasks. What we learned We learned three crucial lessons: 1. AI Compatibility is Key: Utilizing the OpenAI-compatible API structure (as provided by Groq) is vital for rapid prototyping and maintaining provider flexibility when quotas are an issue. 2. API Workarounds are Essential: Complex enterprise APIs (like Jira's) often require deep inspection of error messages and unconventional workarounds (like removing required fields or using specific transition IDs) to integrate successfully in a fast-paced environment. 3. The "Isolation Problem" Requires a Stack: A helpful AI coach cannot be built in one script; it requires a stack of communication (Content Script $\leftrightarrow$ Background Script $\leftrightarrow$ Flask Backend) to securely and effectively capture the user's screen and leverage powerful vision models. What's next for onboardly We plan to implement three key features: 1. Jira Webhook Integration: We will eliminate the final "Mark Complete" button by having Jira trigger a webhook back to our server when all 8 sub-tasks are manually marked "Done," achieving truly touchless final Epic completion. 2. Advanced Security Checks: Integrate the GitHub API (which we built a stub for) to check if the intern has enabled required branch protection rules on their new starter repository before marking that task as complete. 3. Gemini Pro Reasoning: We will leverage the powerful reasoning capabilities of Gemini 2.5 Pro to provide non-visual feedback, such as analyzing the security logs in the next step and providing a summary of the threats found directly to the intern. <div