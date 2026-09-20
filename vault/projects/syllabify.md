---
slug: "syllabify"
url: "https://devpost.com/software/syllabify"
title: "Syllabify"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 374
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Syllabify

> Transform Class Syllabus into Calendar Events with AI. Extract dates, deadlines, and events from your Syllabus in seconds. Never miss a deadline again

[Devpost](https://devpost.com/software/syllabify) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]] [[supply_logistics]]
**user** [[educator_student]] [[researcher]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]]

**stack** claude, langchain, nextjs, supabase

## How they structured the write-up

- inspiration
- what i learned
- how i built it
- challenges faced
- built with
- try it out

## Body

GIF Transform syllabus into calendar in seconds Transform Class Syllabus into Calendar Events with AI Inspiration The idea for this project was inspired by the frustration of manually organizing academic schedules. As students, we often find ourselves buried under a pile of syllabi, trying to identify deadlines, assignments, and exam dates. This repetitive task inspired me to create a solution that could automatically extract important dates from PDF syllabi and integrate them seamlessly into a calendar. The goal was to make time management easier and allow students to focus on their studies rather than logistics. What I Learned This project taught me a lot about working with large language models and integrating them into real-world applications. I deepened my understanding of document parsing, natural language processing, and streaming data for AI-based predictions. Handling asynchronous processing and ensuring that the application remained responsive during streaming was one of the biggest technical lessons I gained. Additionally, it was fascinating to explore how AI could transform unstructured documents into actionable insights. How I Built It The app was built using a combination of cutting-edge tools and technologies: Frontend : Developed with Next.js to create a smooth, user-friendly interface. AI Model : Powered by LangChain and Claude , ensuring accurate extraction of important dates, deadlines, and events. Database : Used Supabase to store user data, extracted events, and provide real-time syncing capabilities. Backend : Set up APIs to handle file uploads, parse the documents, and process the extracted data into calendar-friendly formats. Streaming Implementation : Implemented streaming to ensure users could see intermediate results while the AI processed the full document, making the experience interactive and efficient. Challenges Faced One of the toughest challenges was implementing streaming for real-time feedback. Managing the balance between responsiveness and accuracy required significant optimization of both the AI processing pipeline and the frontend rendering logic. Another challenge was ensuring that the AI could handle diverse syllabus formats, from detailed multi-page PDFs to sparse one-pagers, without compromising accuracy. Built With Next.js : For a seamless frontend experience. LangChain : To power the AI-based natural language understanding. Claude : For advanced AI processing. Supabase : For real-time data storage and management. Try It Out Syllabify App GitHub Repository Transform your academic life today! <div