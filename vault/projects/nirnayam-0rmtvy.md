---
slug: "nirnayam-0rmtvy"
url: "https://devpost.com/software/nirnayam-0rmtvy"
title: "Nirnayam"
hackathon: "Prometheus July AI Challenge"
organization: "Prometheus"
winner: true
words: 641
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
---

# Nirnayam

> Learn Smarter. Decide Better. Find Your True North

[Devpost](https://devpost.com/software/nirnayam-0rmtvy) · hackathon [[Prometheus July AI Challenge]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[geospatial]]

**stack** chatgpt, claude, firebase, github, vercel, vscode

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for nirnayam

## Body

Academic Chatbot Decision-Maker Chatbot Starting Screen Inspiration The inspiration for Nirnayam didn't come from a YouTube short or a trending idea; it came from my own experiences as a student. Every day, I found myself struggling with decision fatigue: Should I finish my homework first? Revise for tomorrow's exam? Learn a new concept? When I spent too much time deciding what to do, my productivity and concept clarity suffered. After talking to friends, I realised I wasn't alone—countless students face the same challenge every day. While AI chatbots like ChatGPT and Claude are excellent at answering questions, they can't truly personalise their guidance because they don't know who the student is or how they learn. That realisation inspired me to build Nirnayam —an AI-powered educational companion that personalises every interaction, helping students make smarter academic decisions and learn in the way that works best for them. What it does Nirnayam is an AI-powered educational companion that helps students learn more effectively and make smarter academic decisions. Instead of acting like a generic chatbot, it personalises every interaction based on the student's grade, learning goals, and preferred teaching style. Whether a student needs help deciding what to study first, understanding a difficult concept, or creating a study plan, Nirnayam provides clear, actionable guidance that adapts to how they learn. By combining personalised tutoring with intelligent decision-making, it helps students spend less time feeling overwhelmed and more time making meaningful progress. How we built it Nirnayam was built using React and Vite for a fast, responsive frontend, with Firebase Authentication and Firestore handling user accounts and personalised preferences. It is deployed on Vercel. The AI is powered by Google's Gemini 3.1 Flash Lite, with carefully engineered prompts that dynamically adapt based on each student's onboarding choices. Features such as voice input and output, Markdown and LaTeX rendering and intent routing were used to create a seamless learning experience that works across devices while remaining lightweight and responsive. Challenges we ran into One of the biggest challenges was designing an AI that genuinely felt personalised rather than simply passing user preferences into every prompt. Building the onboarding system, storing preferences, dynamically injecting them into prompts, and ensuring the AI consistently followed them across different types of conversations required several iterations of prompt engineering and testing before the responses became reliable. Accomplishments that we're proud of I'm proud of building a fully functional AI-powered educational companion that goes beyond simple question answering. Nirnayam successfully combines personalised onboarding, adaptive tutoring, intelligent decision-making, voice interaction, and modern web technologies into one cohesive platform. I'm especially proud that the AI adapts its teaching style automatically based on each student's preferences, creating a learning experience that feels unique instead of generic. Delivering all of this within a polished, responsive interface while maintaining a smooth user experience is something we're incredibly proud of. All in all, making Nirnayam was a huge accomplishment for me. What we learned Building Nirnayam taught me that creating an effective AI application is about much more than connecting to a language model. I learned the importance of prompt engineering, personalisation, user experience design, state management, and balancing AI capabilities with practical educational needs. I also gained valuable experience working with React, Firebase, real-time streaming responses, and deploying production-ready AI applications while continuously debugging and improving the overall experience. I also learnt a lot about good UI/UX, which is the most important thing for a student. What's next for Nirnayam Our vision is to make Nirnayam an even more comprehensive learning companion. Future updates include AI-generated weekly assessments, progress tracking, achievement and motivation systems, Google Calendar integration for intelligent study scheduling, and deeper personalisation that continuously adapts as students learn. We also plan to expand multilingual support, improve accessibility features, and introduce more advanced educational tools that help students build consistent learning habits over time. <div