---
slug: "prep-bear"
url: "https://devpost.com/software/prep-bear"
title: "PrepBear"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 473
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/web_dom"
---

# PrepBear

> A web-app developed to help prep students for their technical interviews through the use of AI mock interviewer.

[Devpost](https://devpost.com/software/prep-bear) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]] [[labor_employment]]
**user** [[educator_student]] [[researcher]]
**substrate** [[web_dom]]

**stack** gemini, javascript, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for prep bear

## Body

Homepage Homepage 2 Live Interview Company Research Example Company Insight Inspiration As computer scientists, we know the dread of job interviews. You send out hundreds of applications, fine-tune your resume for hours, and finally land that interview—only to realize… how do you actually prepare? We built PrepBear to give students and jobseekers a way to practice with a realistic, AI-powered interviewer and boost their chances of success. What it does Company Research Tool 🏢 Enter a company’s website, and PrepBear digs up insights about its history, culture, and values. Knowing the company’s story helps applicants tailor their answers and show genuine interest—exactly what real interviewers look for. Mock Interview AI Tool 🎤 Upload your resume and the job description, then sit down with our AI interviewer. Powered by Google Gemini Live API, PrepBear can simulate both behavioral and technical interviews in real time. The AI doesn’t just assess your answers; it listens to your tone, observes your delivery, and gives constructive feedback to help you improve. How we built it Frontend Framework & Core: React, Tailwind CSS, Typescript State Management & Data: Zustand AI & Real-time Communication: AI & Real-time Communication: Google Gemini Live API, Gemini Flash Model, and Gemini 2.0 Multimodal API (via open-source wrapper) Challenges we ran into Learning the ins and outs of the Gemini Live API took some trial and error. Tried (and scrapped) a complex module for logging all user/system speech displaying a history of conversations. Gemini’s Flash model has no concept of time, so instead of setting interview durations, we tracked the number of exchanges. Spent an hour wrestling with environment variables on Vercel. (Turned out so simple) Background noise kept triggering the AI in testing, so we resorted to using noise-cancelling headphones for our demo. Accomplishments that we're proud of Deployed PrepBear online so anyone can try it. Built a tool that genuinely simulates the pressure of a real interview. Created a resource that can help students and jobseekers build confidence and improve their skills. What we learned How to integrate Gemini’s multimodal Live API for real-time voice interactions. The importance of iterating quickly—sometimes it’s better to scrap a feature than sink hours into it. The adaptability and power of Google Gemini AI in real-world scenarios, especially when handling audio/video input. What's next for Prep Bear 📊 Post-Interview Feedback: Provide a detailed summary highlighting strengths, weaknesses, and key moments for review. 🎙️ Voice Customization: Enable users to choose different interviewer voices (supported by Live API, just needs front-end work). 💻 Technical Assessments: Add live coding challenges with AI feedback. ⏳ Smarter Turn-Taking: Improve the conversation flow so the AI waits for the user to finish speaking. 📹 Video Input Support: Extend input triggers beyond just mic activity. 🐻 Continue improving PrepBear’s realism so it feels like sitting across from a real recruiter—without the sweaty palms. <div