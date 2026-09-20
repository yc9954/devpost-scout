---
slug: "aura-ogqrd4"
url: "https://devpost.com/software/aura-ogqrd4"
title: "Aura"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 534
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
---

# Aura

> Adaptive JEE Study Planning That Converts Syllabus Gaps Into Daily Actionable Schedules

[Devpost](https://devpost.com/software/aura-ogqrd4) · hackathon [[DSH Hacks V1]]

## Facets

**domain** [[developer_tools]] [[education]]
**user** [[educator_student]]

**stack** betterauth, nextjs, postgresql, prisma, tailwindcss, trpc, typescript, vercel

## How they structured the write-up

- inspiration
- why aura ?
- what it does
- how i built it
- challenges i ran into
- future impact
- what's next for aura

## Body

landing page main dashboard screen onboarding screen Inspiration JEE students often know what subjects they are weak at but struggle to convert syllabus gaps, exam dates, revision cycles, and daily availability into an executable plan. Aura automatically transforms those constraints into a day-by-day study schedule that adapts to remaining syllabus coverage and upcoming exams. Why Aura ? Traditional planners require students to manually decide what to study. Aura uses an LLM to interpret syllabus coverage, subject priorities, available study hours, exam timelines, and revision needs to generate personalized study plans that would otherwise require manual planning. Why not ChatGPT? GPT can generate study plans, but it does not understand a student's syllabus coverage, exam timeline, daily availability, revision requirements, and task tracking in a structured way. Aura combines these constraints into an executable study roadmap that can be edited, tracked, and followed over time. What it does Aura analyzes syllabus coverage, exam timelines, available study hours, and subject priorities to generate a personalized JEE preparation plan with built-in revision sessions, practice tests, and daily execution tasks. Traditional Planning Aura Manual scheduling Automated Easy to miss topics Tracks syllabus coverage No revision structure Built-in revision cycles Generic timetable Personalized daily plan How Personalization Works Aura does not generate generic study schedules. When creating a study plan, Aura analyzes multiple factors including: Exam date and remaining preparation time Current syllabus completion for each subject Daily study availability Subject priorities and target focus areas Preferred study session length Revision requirements For example, a student with 20% Mathematics completion and 70% Chemistry completion will receive a different plan than a student with the opposite profile. The generated schedule allocates time according to syllabus gaps, remaining preparation time, and revision needs. The AI then converts these constraints into a structured daily roadmap containing study sessions, revision blocks, and practice tasks that can be edited and tracked inside Aura. How I built it Aura is built with Next.js and Neon Postgres. The core challenge was designing an AI planning system that converts syllabus coverage, exam dates, available study hours, and subject priorities into structured daily study plans. Using the Vercel AI SDK, the model generates revision-aware schedules that are returned as structured data and rendered as editable tasks inside the application. Challenges I ran into One of the important issues i ran into was initially getting structured data of the syllabus to make sure ai doesn't output garbage and topics which don't even exists in the syllabus . A secondary challenge was making the mood/reflection system actually drive plan generation without breaking scheduling constraints — we had to balance softness (mood as a preference signal) with hardness (exam dates, syllabus coverage, daily minute limits). We solved it by making mood adjust the mix and difficulty of tasks within valid bounds, never override hard constraints. Future Impact Aura can evolve beyond planning into adaptive preparation by incorporating mistake tracking, topic mastery estimation, and dynamic schedule adjustment. What's next for Aura Next for Aura is getting it in front of real JEE students and watching where it breaks. I'm prioritizing the study plan and mistake tracking loop first, because that's the core behavior I want to validate before building anything else <div