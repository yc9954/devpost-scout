---
slug: "smartcareer"
url: "https://devpost.com/software/smartcareer"
title: "SmartCareer"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 1208
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/labor_employment"
  - "domain/transportation"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# SmartCareer

> SmartCareer is an AI-powered tool that instantly creates and optimizes ATS-friendly resumes with real-time feedback on content, structure, and recruiter appeal.

[Devpost](https://devpost.com/software/smartcareer) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]] [[labor_employment]] [[transportation]]
**substrate** [[geospatial]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** ai, flask, gemini, genai, machine-learning, python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smartcareer

## Body

landing flowchart dashboard Inspiration The journey of SmartCareer.in began with a very personal struggle. When I was a fresher applying for jobs, I often created long, unstructured resumes — listing every skill I knew, sometimes spanning 5–6 pages. Despite having talent and technical knowledge, I kept getting rejected. Over time, as I gained experience and interacted with mentors and coworkers, I realized what went wrong — it wasn’t my lack of skill, but my lack of awareness about how to present it effectively. Many of my friends and candidates I met faced the same issue. They didn’t know what to include in their resumes, how to format them for ATS systems, or how to catch a recruiter’s attention within the first 30 seconds. In developing countries like India, especially in tier-2 and tier-3 cities, access to professional career guidance and advanced tools is limited. Language barriers and lack of technical awareness make it even harder for freshers to build strong resumes. That’s when I decided to build SmartCareer.in — a platform that provides guidance, structure, and AI-powered assistance so no talented individual ever gets rejected just because of a poor resume. What it does SmartCareer.in is an AI-powered career assistant that helps users instantly create and optimize ATS-friendly resumes. It doesn’t just give templates — it provides real-time, intelligent feedback on what to write, how to structure content, and how to make resumes stand out to recruiters. ✨ Key Highlights • AI-powered resume creation and optimization • Real-time ATS feedback to improve visibility in recruiter systems • Built on Google Cloud Run — fast, scalable, and serverless • Future integrations: Voice-to-text resume builder and personalized job matching Unlike other resume builders that only focus on design, SmartCareer.in focuses on content intelligence — helping users understand what truly matters in a resume. How we built it SmartCareer.in is architected with a Flask backend for API orchestration and a Streamlit frontend for the user interface. Both services are containerized using Docker and deployed independently on Google Cloud Run, enabling autoscaling, zero-downtime deployments, and cost-efficient compute usage. We adopted an iterative prompt-engineering workflow within Google AI Studio, refining model outputs for ATS optimization and contextual resume enhancement. Performance benchmarking and feedback loops were established to fine-tune LLM responses and latency under real-world workloads. The platform comprises four core AI-driven modules: Resume Creator – Provides a guided form-based interface, generating structured resume drafts from minimal user input using generative AI APIs. Resume Enhancer – Leverages domain-specific embeddings and context-aware prompt templates to rewrite and optimize resume content for target industries and tech stacks. Template Engine – Dynamically applies templates with modular components and real-time caching for instant preview and export. JD Matcher – Parses job descriptions using NLP pipelines, computes semantic similarity with resume sections, and suggests targeted keyword and phrasing improvements to boost ATS scores. Cloud Run was selected for its serverless, container-native runtime, automatic scaling, and ability to securely expose both REST and Streamlit endpoints behind a managed HTTPS layer. This setup ensures high availability, efficient AI API utilization, and a fully production-ready pipeline capable of supporting thousands of concurrent sessions. Challenges we ran into Building SmartCareer.in came with several technical and architectural challenges, especially around performance, scalability, and session management in a serverless setup: Session & State Management in Streamlit (Frontend) Streamlit runs in a stateless manner inside Cloud Run containers, making user sessions (login/logout, plan selection) unstable. Persistent session variables were lost after container restarts or scale-down events. Solution: Implemented a hybrid caching mechanism using Redis and JWT-based tokens for session continuity, and introduced custom JS hooks to persist state across Streamlit reruns. Caching & Memory Management The app required frequent calls to AI APIs (Gemini/LLM), and repeated queries caused high latency and cost. Solution: Used intelligent response caching with LRU memory storage and per-user cache invalidation to prevent stale data. Also optimized memory usage by clearing Streamlit session caches after every resume generation or upload cycle. Database Refresh & Real-time Sync Resume scores, plan updates, and AI feedback had to refresh instantly on the dashboard. The Cloud Run ephemeral container model caused delays in DB updates and cache invalidation. Solution: Introduced async background jobs via Cloud Tasks and WebSocket-based refresh triggers to keep data in sync without full page reloads. Payment Gateway Integration (Stripe) Payment callback URLs were failing intermittently in Cloud Run due to inactive containers (“cold starts”) during webhook callbacks. Solution: Added a heartbeat mechanism to keep containers warm and retried failed webhooks automatically using exponential backoff logic. Streamlit JavaScript Limitations Streamlit doesn’t natively support advanced frontend logic like popups, dynamic refresh, or heartbeat pings. Solution: Injected custom JavaScript snippets into Streamlit to handle features like auto-refresh, logout triggers, and payment status checks seamlessly. Autoscaling and Resource Limits During traffic spikes, concurrent users caused Cloud Run to spin up multiple containers, hitting memory limits. Solution: Optimized the container’s base image and applied memory-efficient batching for API requests, reducing cold starts and improving concurrency handling. AI Model Latency & Prompt Performance Generating ATS-optimized feedback sometimes took too long due to complex LLM context size. Solution: Used prompt chunking, selective model invocation (different model sizes for different tasks), and response caching to improve performance by 40%. Accomplishments that we're proud of • AI-Powered Resume Optimization Engine Implemented an LLM-driven ATS optimization module using Google Gemini APIs, which analyzes resumes and job descriptions to provide tailored feedback. The system intelligently highlights missing keywords, structure inconsistencies, and domain-specific skill gaps with near-instant response times, thanks to optimized caching and asynchronous request handling. • Performance & Reliability Engineering Achieved seamless user experience by integrating Redis caching, JWT session management, and Cloud SQL for persistent user and plan data. Optimizations reduced model response latency by 40% and memory footprint by 30%, even under concurrent access loads during testing. • Integrated Payment and Subscription Workflow Designed and implemented a secure payment layer with Stripe API, including real-time webhook handling for subscription activation, using a heartbeat mechanism to handle Cloud Run cold starts and webhook reliability challenges. • User-Centric Impact Early beta users successfully created recruiter-ready, ATS-friendly resumes in under 5 minutes — a process that earlier took hours. The tool turned a personal frustration into a scalable, cloud-native platform capable of empowering millions of job seekers globally. • End-to-End Scalable Deployment on Google Cloud Run Successfully containerized and deployed the full SmartCareer.in stack — Flask backend (REST APIs, AI orchestration) and Streamlit frontend (interactive UI) — using Google Cloud Run for automatic scaling, zero-downtime updates, and serverless operation. Each service was built with Docker, deployed via Cloud Build, and monitored through Cloud Logging and Cloud Monitoring for real-time observability. What we learned This journey taught me how to: • Design and deploy serverless applications on Cloud Run • Optimize AI pipelines for real-time performance • Balance technical innovation with human-centered design Most importantly, I learned that technology becomes truly powerful when it solves real human problems. What's next for SmartCareer The roadmap ahead is exciting! • Integrate voice-to-text resume creation for accessibility • Add personalized job recommendations based on AI-driven skill mapping • Expand to global users while keeping the focus on affordability and inclusivity Our vision is clear — to ensure no talented person gets rejected because of a resume. <div