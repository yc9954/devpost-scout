---
slug: "syllaboard"
url: "https://devpost.com/software/syllaboard"
title: "Syllaboard"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 312
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
---

# Syllaboard

> One upload for who, what, where, and when of every class.

[Devpost](https://devpost.com/software/syllaboard) · hackathon [[Student HackPad 2025]]

## Facets

**mechanism** [[on_device_local]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]]

**stack** googlecalendarapi, next.js-16, openai-api-(gpt-5-nano), react-19, tailwind-css, typescript

## How they structured the write-up

- what i built and why it matters
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what’s next for syllaboard

## Body

What I built and why it matters As a student, it's common to be drowning in PDF syllabi and all the important info the start of every term, so stuff never actually makes it to our calendars. I made a tool that did just that job for students in under a minute. Syllaboard lets you drag in multiple syllabus PDFs, automatically extracts course details (title, instructor, meeting times) and important dates, shows them in a review screen, and then exports selected events directly to your Google Calendar. How I built it I used Next.js 16 (App Router) with React 19 and TypeScript for the web app, Tailwind with custom design tokens for the UI, OpenAI’s API to turn raw PDF text into structured course + event data, and the Google Calendar API (via OAuth) to create calendar events from those parsed results. Throughout the process, Claude and ChatGPT were used for guidance. Challenges I ran into Getting reliable text out of real-world syllabi (weird layouts, tables, headers) and shaping prompts so the model returned predictable JSON took a lot of iteration. Integrating Google OAuth + Calendar in a secure way, handling scopes, and dealing with time zones/date formats also took more time than expected. Accomplishments that I'm proud of I'm proud that the entire flow works end-to-end: upload multiple syllabi, see detected events per course, toggle what you want, and watch them appear in Google Calendar. What I learned I learned how to design prompts around messy, semi-structured documents, how to wire up Google’s OAuth and Calendar APIs responsibly, and how much a small amount of visual polish and copywriting can change how “finished” a project feels. What’s next for Syllaboard Next I'd like to support Outlook/iCal exports, add smarter conflict detection and “deadline heatmaps,” and explore on-device or privacy-preserving extraction so schools with stricter data policies can still use it. <div