---
slug: "sahayaai-intelligent-learning-career-platform"
url: "https://devpost.com/software/sahayaai-intelligent-learning-career-platform"
title: "SahayaAI-Intelligent Learning & Career Platform"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 937
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# SahayaAI-Intelligent Learning & Career Platform

> Ace your exams today, land your dream career tomorrow. SAHAYA.AI is an AI-powered ecosystem that bridges the silent gap between classroom grades and real-world employment. Are you ready to level up?

[Devpost](https://devpost.com/software/sahayaai-intelligent-learning-career-platform) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[on_device_local]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]] [[labor_employment]] [[mental_health]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** express.js, framer, gemini-api, groq, javascript, monaco-editor, node.js, postgresql, python, react, scikit-learn, supabase, tailwind-css, webrtc

## How they structured the write-up

- 💡 inspiration
- 🚀 what it does
- 📊 the math & ml engine
- 🛠 how we built it
- 🚧 challenges we faced
- 🎉 accomplishments we're proud of
- 🧠 what we learned
- 🔮 what's next for sahaya.ai

## Body

SAHAYA.AI — Smart Studying meets Career Readiness 💡 Inspiration Modern students are caught in a fragmented learning loop. They navigate one platform for study notes, another for coding practice (LeetCode), a third for video-conferencing, and a fourth to review their resumes. This context switching leads to high cognitive load, lack of motivation, and massive anxiety during career placements. We built SAHAYA.AI to solve this. Sahaya (meaning "help" or "support" in Sanskrit) is an intelligent, gamified learning and career ecosystem that adapts dynamically to every student’s strengths and weaknesses. By bridging the gap between raw academic studying and practical career prep, SAHAYA.AI helps students study smarter, optimize their time using machine learning, and graduate career-ready. 🚀 What it Does SAHAYA.AI is split into two specialized, highly integrated modules: 📚 1. Study World (Academic Optimization) Smart Upload Hub: Students upload PDFs or paste YouTube URLs. Our LLM-orchestrated pipeline parses the content and instantly generates structured lessons, interactive flashcards, customizable quizzes, and targeted practice problems. AI-Powered Timetable Optimizer: Rather than allocating study time randomly, SAHAYA.AI gathers real-time accuracy data and uses a custom optimization algorithm to allocate study budgets per subject based on weaknesses. Performance Prediction Model: Employs a machine learning model to estimate a student's recommended study hours and forecast their upcoming academic performance based on historical behavior. 💼 2. Career World (Placement Readiness) Problem Arena: A fully integrated Monaco-based code editor where students solve DSA problems with a 3-tier progressive AI hint ladder (Nudge $\to$ Approach $\to$ Full Walkthrough) and sandboxed JavaScript test runners. Live Group Discussions (GD): A real-time, WebRTC-powered video conferencing room (powered by ZegoCloud ) where peers practice GDs. Once finished, Gemini reviews the speech transcript, participation, and face metrics to deliver a comprehensive communication score. Resume Hub & JD Scanner: A scanner that compares resumes against target Job Descriptions, providing recruiter-simulation tests and scoring alignment. Algorithm Visualizer: An interactive step-by-step debugger that visualizes data structure operations (trees, graphs, and dynamic programming tables) in real-time. 📊 The Math & ML Engine To make our system scientifically robust, we built three mathematical cores: A. Adaptive Timetable Allocation Model For each subject $i \in {1, \dots, N}$, we compute the correctness accuracy $A_i$ from quiz logs: $$A_i = \left( \frac{C_i}{T_i} \right) \times 100$$ Where $C_i$ is correct questions and $T_i$ is total questions attempted. The priority weight $P_i$ represents user weakness: $$P_i = 100 - A_i$$ We allocate the student's daily study hours budget $H_{\text{total}}$ dynamically using: $$H_i = \left( \frac{P_i}{\sum_{j=1}^{N} P_j} \right) \times H_{\text{total}}$$ B. Machine Learning Performance Forecaster We trained a Random Forest Multi-Output Regressor using scikit-learn . Given a student's feature vector $\mathbf{x}$: $$\mathbf{x} = \begin{bmatrix} h_{\text{planned}} \ f_{\text{focus}} \ b_{\text{breaks}} \ d_{\text{difficulty}} \ s_{\text{previous}} \end{bmatrix}$$ The model predicts the recommended hours budget $\hat{H} {\text{rec}}$ and predicted performance grade $\hat{P} {\text{perf}}$: $$f(\mathbf{x}) \to \begin{bmatrix} \hat{H} {\text{rec}} \ \hat{P} {\text{perf}} \end{bmatrix}$$ C. Career Readiness Score A student's score $R$ is dynamically computed from their problem attempts: $$\text{PassRate} = \frac{N_{\text{passed}}}{N_{\text{total}}}$$ $$\text{Volume} = \min\left(1, \frac{N_{\text{total}}}{20}\right)$$ $$R = \min\left(100, \max\left(0, \text{round}\left(70 \times \text{PassRate} + 30 \times \text{Volume}\right)\right)\right)$$ 🛠 How We Built It SAHAYA.AI is engineered using a robust client-server architecture: Frontend: Built with React 18, Vite, and Tailwind CSS. We integrated Monaco Editor for high-fidelity code writing, and used Framer Motion for micro-animations and sleek dashboard transitions. Backend: Node.js & Express.js server providing REST APIs and handling the execution of Python subprocesses. Database: Supabase (Postgres) with a schema-less custom implementation to store user profiles, quiz scores, and daily quest statistics. WebRTC Video Core: ZegoCloud Prebuilt UI Kit to spin up instantaneous, secure video channels for group discussions. AI Orchestration & Deep Tech: Google Gemini 2.0: Orchestrates structured JSON output generation, complex resume parsing, and code-review generation. Groq (Llama-3): Drives low-latency, real-time hint generation in the Problem Arena and algorithmic step narrations. Python AI Engine: Scikit-Learn, Joblib, Pandas, and Numpy to train, save, and serve the Random Forest Regressor models locally. 🚧 Challenges We Faced WebRTC Latency & Peer Tracking: Synchronizing live video grids for Group Discussions while tracking speaking time and participants joining or leaving in real-time was tricky. We solved this by pairing ZegoCloud's event hooks with real-time state sync. Deterministic Code Debugging/Tracing: Building a Python-based execution tracer ( tracer.py ) that executes code securely and returns variable states line-by-line without running into infinite loops or stack overflows. Structured JSON Fallbacks: LLMs can occasionally return poorly formatted JSON strings, which crashes front-end visualizations. We implemented strict JSON schemas using Gemini's native structured outputs and built error-handling middleware. 🎉 Accomplishments We're Proud Of Sleek, Cohesive UX: Blending study tools and career tools into a unified interface gamified with daily quests, XP levels, and leaderboards. WebRTC to AI Bridge: Successfully sending live GD transcripts and facial attention data to Gemini and receiving a comprehensive communication report within seconds. Live Step-by-Step Algorithm Tracer: A fully functioning visualizer that bridges the gap between written code and visual structural nodes (like graphs and trees). 🧠 What We Learned System Sandboxing: We learned how to securely execute arbitrary Javascript inside a vm context in Node.js, ensuring user code cannot break the server. Multi-Output ML Models: How to format and preprocess complex tabular features in Pandas to predict multiple dependent labels (hours & score) simultaneously. Hybrid AI Architecture: Balancing high-speed Llama models via Groq with highly logical, deep reasoning Gemini models. 🔮 What's Next for SAHAYA.AI Interactive AI Panel Interviews: Upgrading the recruiter simulator to support multi-agent panels, where multiple AI personas ask questions. Voice-to-Voice AI Coaching: Utilizing Gemini's native multimodal audio capabilities to conduct vocal mock interviews. LMS Integration: Connecting to standard Learning Management Systems (Canvas, Moodle) to automatically import syllabus outlines. <div