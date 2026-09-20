---
slug: "stellanet"
url: "https://devpost.com/software/stellanet"
title: "Stellanet"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 444
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# Stellanet

> Stellanet helps students find matched professors and draft better outreach emails using Amazon Nova on AWS, with transparent ranking, tone rewrite, and human-in-the-loop review.

[Devpost](https://devpost.com/software/stellanet) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[human_in_the_loop]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** amazon-bedrock-(nova-2-lite), amazon-ecr, aws-app-runner, docker, git, github, google-oauth, javascript, openalex-api, postgresql-compatible, python, react, resend/smtp, sqlite-(local)

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i am proud of
- what i learned
- what's next for stellanet

## Body

Inspiration Stellanet was inspired by a common challenge for students and early researchers: finding the right faculty mentor and writing meaningful first-contact emails is time-consuming, unstructured, and often discouraging. I wanted to build a practical AI system that makes outreach more focused, transparent, and effective without removing human control. What it does Stellanet helps users run an end-to-end research outreach workflow: Takes user interest, profile, and target universities. Retrieves and ranks relevant faculty candidates using grounded research signals. Shows why a match is relevant with explainable details. Generates personalized outreach drafts. Rewrites drafts by tone (professional, friendly, short). Keeps users in control with human-in-the-loop review before sending. Supports secure auth flows including email/password and Google sign-in. How I built it I built Stellanet as a full-stack web app: Frontend: React + Vite + Tailwind for a responsive workflow UI. Backend: FastAPI with modular services for auth, discovery, and draft rewrite. AI layer: Amazon Nova 2 Lite (via Amazon Bedrock) for ranking/drafting/rewriting. Grounding source: OpenAlex API for research and affiliation signals. Auth/Session: local SQLite in development, production-ready PostgreSQL support. Deployment: Dockerized backend on AWS App Runner and frontend on Vercel. I also implemented environment-based configuration, API abstractions, and route handling improvements for production reliability. Challenges I ran into Production deployment differences between local/dev and cloud environments. Health check failures caused by invalid database host configuration. OAuth origin mismatch issues in Google Cloud setup. Route refresh behavior on production domains for SPA paths like /signin and /about . Double-slash API URL edge cases causing endpoint 404s in production. Ensuring fallback behavior remained user-safe while still being debuggable. Accomplishments that I am proud of Built a complete, usable outreach product instead of a model-only demo. Integrated Amazon Nova into the core user value path. Delivered grounded, explainable ranking and controllable rewrite workflows. Implemented secure auth with Google sign-in support. Deployed backend on AWS App Runner with containerized delivery. Improved UX reliability with route-safe refresh handling and robust error pathways. What I learned AI product quality depends as much on reliability engineering as model quality. Small configuration mismatches (env vars, hostnames, trailing slashes) can break core flows. Grounded generation + transparent reasoning improves trust and usefulness. Shipping with iterative debugging and real user-style testing is critical for production readiness. Building with Nova is strongest when tightly integrated into a practical workflow, not just a chat interface. What's next for Stellanet Improve ranking calibration and confidence transparency. Add persistent workspaces, saved runs, and draft history/versioning. Expand personalization controls for outreach style and intent. Add stronger observability and automated quality checks. Introduce advisor/team review workflows for collaborative outreach. Explore multimodal inputs (CVs, statements, and research docs) for richer context. <div