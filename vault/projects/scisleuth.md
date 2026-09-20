---
slug: "scisleuth"
url: "https://devpost.com/software/scisleuth"
title: "SciSleuth"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 511
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/education"
  - "domain/health_clinical"
  - "user/educator_student"
  - "substrate/geospatial"
---

# SciSleuth

> An AI-powered platform that diagnoses student misconceptions, maps broken concepts to a knowledge graph, and generates personalized learning recovery paths.

[Devpost](https://devpost.com/software/scisleuth) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[education]] [[health_clinical]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** ai, api, css, education, gemini, google, javascript, next.js, postgresql, react, supabase, tailwind, technology, typescript

## Body

Interactive knowledge graph of a student after diagnostic Landing page of SciSlueth Diagnostic results page of a student AI-generated entire classroom analysis through teacher login Recovery page comparing previous and current diagnostic of a student Inspiration Traditional quizzes tell students whether an answer is right or wrong, but they rarely explain why the student made a mistake. In STEM education, many mistakes are caused by misconceptions—deeply held incorrect beliefs about a concept rather than simple calculation errors. For example, a student may believe that an object needs a continuous force to keep moving. A quiz can identify the answer as wrong, but it usually cannot identify the misconception behind it. We wanted to build a system that diagnoses misconceptions instead of simply grading answers. That idea became SciSleuth. What it does SciSleuth is an AI-powered learning diagnostic platform that helps students understand the reasoning behind their mistakes. The platform: Detects misconceptions from diagnostic assessments Maps misconceptions to specific broken concepts Visualizes conceptual understanding through a knowledge graph Generates personalized AI explanations using Google Gemini Provides guided repair missions to rebuild understanding Tracks concept health and recovery progress Gives teachers visibility into misconception patterns across students Instead of asking "Did the student get it right?", SciSleuth asks "Why did the student get it wrong?" How we built it We built SciSleuth using: Next.js and TypeScript for the frontend Tailwind CSS for the user interface Supabase for authentication and data storage Google Gemini API for personalized explanations and teacher insights Knowledge graph visualization to represent concept relationships Each diagnostic question contains carefully designed distractors that map to specific misconceptions. When a student submits an assessment, the system identifies the misconception, generates explanations, updates concept health, and visualizes the impact on the knowledge graph. Challenges we ran into One of our biggest challenges was designing a system that goes beyond traditional scoring. We needed a way to represent conceptual understanding rather than simply counting correct answers. Designing misconception mappings, concept relationships, recovery pathways, and graph health calculations required multiple iterations. Another challenge was maintaining consistency between diagnostic results, recovery progress, knowledge graph updates, and teacher analytics while keeping the experience intuitive for students. Accomplishments that we're proud of Built a complete misconception-detection workflow Integrated AI-generated personalized explanations Developed an interactive knowledge graph for concept visualization Created recovery missions that guide conceptual repair Built teacher analytics and student drill-down dashboards Successfully deployed the application for public access What we learned This project helped us understand that educational technology becomes far more effective when it focuses on reasoning rather than answers. We also gained valuable experience integrating AI into a real-world learning workflow, designing educational analytics systems, and building a full-stack application using modern web technologies. What's next for SciSleuth Future improvements include: Support for additional STEM subjects beyond Newton's Laws Adaptive assessments based on detected misconceptions More advanced knowledge graph relationships Classroom-level intervention recommendations Long-term misconception tracking and learning analytics Research-backed misconception datasets for multiple domains Our long-term vision is to create a platform that helps students understand concepts deeply rather than memorizing answers. <div