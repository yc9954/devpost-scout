---
slug: "prereq-sg1thw"
url: "https://devpost.com/software/prereq-sg1thw"
title: "Prereq"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1149
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/transportation"
  - "user/educator_student"
  - "user/frontline_worker"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Prereq

> Real-time knowledge graphs that make every lecture impossible to fall behind in

[Devpost](https://devpost.com/software/prereq-sg1thw) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[education]] [[transportation]]
**user** [[educator_student]] [[frontline_worker]] [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[transcript_audio]] [[video_visual]]

**stack** claude, claudehaiku, claudesonnet, express.js, flask, next.js, perplexity, postgresql, python, react, react-force-graph-2d, render, socket.io, supabase

## How they structured the write-up

- problem & inspiration
- what it does
- how we built it
- challenges & accomplishments
- what we learned
- what’s next

## Body

Student view (click for clearer image) - see which concepts SGD depends on, external learning resources, and callbacks to lecture Student view (click for clearer image) - full knowledge graph for a machine learning course Instructor view (click for clearer image) - class mastery heatmap to see understanding in real time Personalized AI tutoring on weak modules post-lecture - LaTeX formatting (click for clearer image) Landing page! (click for clearer image) Study group formation (click for clearer image) - matching based on modules you want to study, chat feature, and automatic Zoom link Problem & Inspiration Education is one of the most powerful drivers of opportunity, yet our classrooms still rely on guesswork to measure understanding. Professors introduce new concepts without knowing who's following along, and students often don't realize they're lost until the exam. Our team has experienced this firsthand and found that these issues are only exacerbated in online settings. Part of the problem is how most classroom tools augment learning. Stanford’s machine learning course (CS229) includes a 200-page reader filled with dense, interconnected concepts. While studying for the midterm, Cynthia manually mapped out all the major topics and their prerequisites to understand how everything fit together. This visual reinforced that learning is cumulative and interconnected . You can’t understand backpropagation without the chain rule, or speak Spanish without mastering conjugations. As a result, we leverage dynamic visual aids that provide professors with real-time feedback that twelve students understand the chain rule while eight are lost on gradient descent. This way, they can adapt their instruction accordingly and give those eight students targeted help. What It Does Prereq is a live, interactive learning copilot that turns lectures into personalized, ever-evolving knowledge graphs. Each student's graph updates in real time, showing what they've mastered, what they're struggling with, and an actionable plan to close relevant gaps. Professors are armed with a live heatmap of class-wide learning progress, pinpointing exactly which concepts and prerequisites to reinforce understanding. For students : As your professor speaks, Prereq transcribes the lecture and automatically identifies concepts being discussed (e.g., "Backpropagation"), lighting them up on your personal graph. In-class Prereq quizzes, exam performance, and conversations with Aaron, our AI tutor, all feed into your graph, so it updates continuously. After class, you can keep collaborating with Aaron, who is personalized to your weak graph nodes. Our study group feature also helps foster community! We match students who opt in based on complementarity: your weak spots are their strengths, and vice versa. One click gives them both a Zoom link at a mutually agreed-upon time and a side‑by‑side view of who can teach what, turning the class into a learning network. For professors : Instead of generic iClicker/PollEV questions, we help professors generate polls from what was just said and aim them at concepts the class is struggling with. They can see each student’s knowledge graph and sort a class mastery heatmap by the most difficult concepts. During the lecture, we also surface live reinforcement suggestions (what to re-explain, which examples to add) to help them adjust in the moment. How We Built It At the start of the semester, a professor uploads their course material as a PDF. Eliminating manual parsing, Claude Sonnet extracts every concept and its prerequisites into a knowledge graph: 35+ concepts from a 200-page textbook in seconds. Each student gets their own copy, and two students in the same lecture will have completely different graphs by Week 2. During a lecture, Zoom's RTMS SDK captures live audio and transcription with precision. Getting that integration right is one aspect we’re extremely proud of. The RTMS SDK helped us handle webhook validation, OAuth, per-teacher credentials, and joining the RTMS stream reliably (more in Challenges). Everything spoken is run through concept detection (Claude Haiku), stored in Supabase via our Flask API, and pushed to student knowledge graphs and the professor heatmap in real time over Socket.IO. We also update graphs based on in-class poll performances. Our study-group feature pairs students by opposite strengths and weaknesses and sends out a Zoom link based on their schedules so they can start a peer session in one click. After the lecture, Claude Sonnet powers Aaron, our Socratic tutoring agent, that adapts to each student's conversation, and we use Perplexity’s Sonar API to surface targeted learning resources (articles, videos, exercises) that complement the course material. Our frontend is built with Next.js, React, Tailwind CSS, and react-force-graph-2d for the interactive knowledge graph. The backend runs Express with a custom Socket.IO server alongside Flask for graph CRUD and mastery logic, all backed by Supabase (PostgreSQL). The app is fully deployed on Render. Render gave us a production-ready API with scaling and load balancing in five minutes with no DevOps overhead. Challenges & Accomplishments Building Prereq was an ambitious goal, and implementing RMTS was technically complex. Beyond passing Zoom’s webhook validation (HMAC-signed challenge) and implementing OAuth for the right streams, we spent hours debugging why RMTS did not work across multiple devices for our Render deployment. This required us to methodically build and test endpoints to inspect active lecture streams. Keeping the live Prereq experience fast and accurate was another focus. To reduce latency for API calls, we built out caching for our AI agents and have a Redis layer. Our backend fully works and is optimized for scalability. Creating a comprehensive knowledge graph from 200+ page course documents was also a challenge. To support more users, we designed a pipeline to extract concepts and prerequisites at scale reliably. Finally, we are proud of how intuitive our UI/UX is to those of all learning styles. We help facilitate social connections through our study group matching platform, encouraging collaboration between students of varying levels. Distinguishing between passive vs. active mastery was an interesting design challenge. What We Learned On the technical side, we applied our knowledge of networking and webhooks to debug APIs. AI tutoring is super popular in EdTech, but we learned that a general, abstract agent was not as useful as an agent recognizing a student in context to their academic history. On the product side, we learned that personalization and context are everything. AI tutoring only works when it understands timestamps the student didn't understand, past mistakes, and missing prerequisites. Also, even a 500ms delay in poll feedback broke the live experience, so we added caching layers, used time-sensitive calls carefully, and designed around a Socket.IO push instead of polling to keep interactions instant. What’s Next We plan on integrating directly with the tools students already live in, such as Canvas, Blackboard, Edpuzzle, and Kahoot. Potential sources like homework accuracy, reading completion, quiz attempts, lecture polls, exam performance could all flow into one shared knowledge graph within our system. Long term, concepts mastered in one class should strengthen performance in the next. Over time, the system becomes a living map of a student’s strengths, weaknesses, and growth. <div