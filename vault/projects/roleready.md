---
slug: "roleready"
url: "https://devpost.com/software/roleready"
title: "RoleReady"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 459
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/web_dom"
---

# RoleReady

> AI-powered resume tailor that scores your fit and rewrites your resume for any job, powered by Amazon Nova on AWS Bedrock.

[Devpost](https://devpost.com/software/roleready) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[education]] [[labor_employment]] [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[geospatial]] [[web_dom]]

**stack** amazon-nova-lite, amazon-nova-multimodal-embeddings, aws-bedrock, beautiful-soup, chrome, flask, python, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- accomplishments that i am proud of
- what i learned
- what's next for roleready

## Body

The two-column web demo page The fit score result showing 65% Moderate Match The tailored resume output The Chrome extension popup UI Inspiration As a college student applying for internships, I found myself spending hours rewriting my resume for every single application. I built RoleReady to solve my own problem. What it does RoleReady is a Chrome extension + web app that extracts job descriptions from any URL, scores your resume fit using Amazon Nova Multimodal Embeddings, and rewrites your resume using Amazon Nova Lite in seconds. How I built it Amazon Nova Lite ( amazon.nova-lite-v1:0 ) for resume tailoring and JD cleaning Amazon Nova Multimodal Embeddings ( amazon.nova-2-multimodal-embeddings-v1:0 ) for 1024-dim semantic fit scoring AWS Bedrock as the AI platform Python + Flask backend React + TypeScript Chrome Extension (Manifest V3) Challenges The biggest challenge was getting the Chrome MV3 service worker to fetch from localhost, as Chrome blocks this by default. The fix was routing all API calls through the background service worker with Access-Control-Allow-Private-Network: true headers. Accomplishments that I am proud of Getting Amazon Nova Multimodal Embeddings to produce meaningful semantic fit scores was a real milestone. The first time I ran it and got back a score that actually reflected how well my resume matched a job, it felt like the project came together. I'm also proud of shipping a full Chrome extension from scratch in 72 hours, including debugging the MV3 service worker CORS issues that took hours to trace down. Building something I would actually use myself was the most rewarding part. What I learned I learned how to use Amazon Nova Multimodal Embeddings for semantic similarity, generating 1024-dimensional vectors and computing cosine similarity to produce a match score that understands meaning rather than just counting keywords. I also learned how Chrome Manifest V3 service workers handle network requests differently from regular web pages, specifically that direct fetch calls to localhost are blocked, and that the correct pattern is to proxy API calls through the background service worker. On the AWS side, I got hands-on experience with boto3 and the Bedrock runtime API, and learned how to structure prompts effectively for Nova Lite to get consistent, high-quality resume rewrites. What's next for RoleReady The most exciting next step is integrating Nova Act to automate actual job application submission, not just tailoring the resume, but filling out and submitting the application form directly. Beyond that, I want to add cover letter generation, a LinkedIn scraping solution using a headless browser, and an application tracker so users can log which tailored resumes they sent and track response rates. Long term, RoleReady could become a full job search copilot- from finding roles, to tailoring applications, to preparing for interviews using the job description as context. <div