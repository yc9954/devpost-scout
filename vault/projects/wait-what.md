---
slug: "wait-what"
url: "https://devpost.com/software/wait-what"
title: "WaitWhat"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 575
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/transcript_audio"
---

# WaitWhat

> Have you ever been lost in a lecture and thought, “Wait, what?” WaitWhat incorporates AI agents into live classroom settings to augment student-professor interactions, improving learning outcomes.

[Devpost](https://devpost.com/software/wait-what) · hackathon [[NexHacks]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[transcript_audio]]

**stack** bun, convex, gemini, javascript, livekit+deepgram, node.js, react, tailwind, tanstack, typescript, vercel, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments we're proud of
- what we learned
- what's next for waitwhat

## Body

Home Page View Student View with AI Chat Student Join Session Student Chat Help Student Quiz Complete Student Quiz Question View Personalized Notes Summary After Session (Mobile) Student View of Lecture Transcript Student Waiting Screen (Mobile) Teacher Insight Dashboard Teacher Class Content Upload Teacher Join QR Code Teacher Log in Page Teacher Summary of Their Student's Most Frequently Asked Questions with the Personal AI Teacher View of Quiz Results Inspiration As three college students at large universities, we’ve sat through countless massive lectures where falling behind by just a few seconds meant being lost for the rest of class. When a professor moved too fast or skipped a small but crucial piece of background knowledge, it was nearly impossible to recover in real time. This common college experience led us to build WaitWhat to help students fill in knowledge gaps during the lecture itself, ensuring no one leaves class having missed the opportunity to truly learn. What it does WaitWhat is a real-time lecture copilot that lets students fill knowledge gaps instantly via live transcripts and AI-powered Q&As without interrupting the lecture or feeling embarrassed. Instructors get real-time insights through confusion signals, frequently-asked questions, and quick checks-for-understanding, letting them adapt on the fly. After class, each student receives personalized notes generated from the lecture transcript, slides, and their own questions. How we built it We built WaitWhat collaboratively using a React + Tailwind frontend hosted on Vercel and a Convex-backed Node.js backend. LiveKit powers real-time audio streaming and transcription, while Gemini drives context-aware AI Q&A, adaptive note-taking, dynamic class quizzes, and instructor insights. The Token Company enables low-latency communication, allowing seamless interaction between students and professors during large lectures. Challenges we ran into Integrating LiveKit was one of our biggest hurdles. After setting up the initial infrastructure, connecting it smoothly to our platform proved difficult due to the many external dependencies required. At the same time, we wanted WaitWhat to be simple and intuitive for users, which added extra complexity: making a feature-rich system like live speech-to-text, AI Q&A, personalized quiz generation, and tailored notes work seamlessly with just a couple of button presses was a major challenge. Ensuring the AI could generate responses, quizzes, and summaries tailored to each student based on the live transcript and course materials added another layer of technical difficulty. Accomplishments we're proud of We built a tool we would actually use in class while tackling the technical challenge of streaming live audio through a full AI-powered pipeline. We’re proud to have created a solution that augments human teaching, dynamically supporting both instructors and students across a variety of settings. We’re also proud of our ability to load large context windows, entire course materials and long lecture transcripts, without inflating API costs, thanks to The Token Company's compression system, enabling personalized AI-generated responses, quizzes, and notes at scale. What we learned Building WaitWhat taught us how to iterate quickly and navigate complex technical challenges with confidence. We approached every decision from a user-centered perspective, constantly asking what would genuinely improve the learning experience in a real classroom. Working across the full stack, each team member explored new areas, and was able to contribute to all aspects of the project. What's next for WaitWhat We plan to start testing WaitWhat in larger lectures and work toward adoption at universities, with the goal of helping students across the country stay engaged, learn more effectively, and never feel lost in class again. <div