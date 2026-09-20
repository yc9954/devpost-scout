---
slug: "clarita"
url: "https://devpost.com/software/clarita"
title: "ClariTA"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 596
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/web_dom"
---

# ClariTA

> Meet ClariTA, your late-night study partner! Make studying easier by uploading your PDF lecture that automatically generates practice quizzes, helping you effectively retain information.

[Devpost](https://devpost.com/software/clarita) · hackathon [[ShellHacks 2025]]

## Facets

  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]] [[transcript_audio]] [[web_dom]]

**stack** drizzle, express.js, javascript, node.js, postgresql, react, supabase, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clarita

## Body

Our main page Inspiration Plenty of studies show that memory retention by itself is not enough to guarantee academic success. What really makes a difference are the study techniques students use—strategies like retrieval practice, spaced repetition, and active recall, which have been proven to improve performance. Inspired by this, we wanted to build a tool that goes beyond just guiding you through assignments. Our website is designed to help you actively test your knowledge anytime, making learning more engaging, personalized, and effective. By focusing on evidence-based methods, we aim to support students in studying smarter, not just harder. What it does ClariTA is an AI-powered teaching assistant that transforms lecture slides into interactive learning experiences. By uploading a PDF, educators can instantly generate customizable quizzes with multiple question types, while students can take and review assessments through a sleek, responsive interface. How we built it Frontend: Built with React + TypeScript + Vite, providing a responsive and accessible interface where students can upload slides, adjust quiz settings (difficulty, number of questions), and review results. The frontend integrates PDF.js for previewing documents and a custom quiz runner. Backend: Developed with Node.js + Express (TypeScript) as the API gateway. The backend coordinates parsing, quiz generation, verification, and exporting. Services include: Parsing service to extract text and headings from PDFs Generation service powered by Google Gemini API, used to create multiple-choice, true/false, and short-answer questions. Verification service to cross-check generated answers against slide content and assign confidence scores. Database & Storage: PostgreSQL with Drizzle ORM to manage users, uploads, and quizzes. Files and exports are stored in Supabase/MinIO buckets with signed URLs. Libraries & Tools: Google Gemini API for natural language understanding and quiz generation. PDF.js for rendering slides. Supabase for storage. Challenges we ran into During development, we successfully navigated several key challenges. A primary technical hurdle was optimizing the PDF processing module, which initially had a file size limit of 20MB. We also made a strategic decision to manage the project's scope by focusing on three core quiz types to ensure a high-quality user experience. On the backend, we carefully architected our code to resolve complexities with variable scope and data flow. Finally, the most significant phase was the integration of our frontend and backend systems, which required extensive debugging to ensure seamless communication and full functionality struggle question Accomplishments that we're proud of As a team of first-time hackathon participants, we are incredibly proud to have developed a fully functional web application from concept to execution. Our primary accomplishment is the successful implementation of the site's core feature: the ability for a user to upload a PDF lecture, which the system then intelligently parses to generate a relevant quiz. Furthermore, we delivered a clean and intuitive user interface that makes the study experience both simple and visually appealing. While this initial version offers a focused set of features, it serves as a robust and working foundation for helping students prepare for their exams. What we learned We learned how to work in a team project developing with different technologies. Especially on how to implement API’s to use LLM generation inside the program. What's next for ClariTA Looking ahead, we want to expand ClariTA with features that make studying even more effective and accessible. Some of the next steps include adding new quiz types like matching concepts and scenario-based short answers, supporting video transcripts so students can instantly turn lectures into quizzes, and enabling quiz sharing with classmates for collaborative study. Finally, we plan to publish ClariTA as a mobile app, making it available anytime, anywhere. <div