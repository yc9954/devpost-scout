---
slug: "prime-papers"
url: "https://devpost.com/software/prime-papers"
title: "Prime Papers"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 621
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/video_visual"
---

# Prime Papers

> Prime Papers helps students find exam past papers instantly and get AI-powered help with solving questions, understanding concepts, and preparing for exams.

[Devpost](https://devpost.com/software/prime-papers) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[video_visual]]

**stack** appwrite, deepseek, gpt-4o, mongodb, nextjs

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for prime papers

## Body

Snaaping for AI to assist AI assisstance Search Paper Section Landing Page Prime Papers Inspiration Access to quality revision materials remains a major challenge for many students. While past papers are one of the most effective tools for exam preparation, they are often scattered across different sources and lack intelligent support for learning. We were inspired to build a platform that transforms static past papers into an interactive learning experience powered by artificial intelligence. What it does Prime Papers is an AI-powered educational platform that enables students to discover, analyze, and learn from exam past papers. The platform provides advanced search capabilities that allow users to locate relevant papers using courses, subjects, years, examination types, and natural language queries. In addition, students can submit text-based questions or upload images of exam questions for AI-assisted analysis. The system generates structured solutions, explains concepts, identifies question categories, and supports contextual follow-up discussions, creating a personalized learning environment around past examination content. How we built it Prime Papers was built using Next.js with a full-stack architecture that integrates document retrieval, computer vision, natural language processing, and conversational AI. At the core of the platform is a searchable repository of past papers supported by intelligent indexing and retrieval mechanisms. For AI-assisted learning, we developed a classification and solution-generation pipeline capable of processing both textual and visual inputs. The system analyzes incoming questions, extracts educational context, identifies subject domains, estimates complexity, and generates structured explanations tailored to the student's query. To support image-based questions, we implemented multimodal processing that enables the system to understand and reason over uploaded screenshots and photographs of examination questions. We also designed a conversational layer that preserves context across interactions, allowing students to ask follow-up questions and receive progressively deeper explanations. The platform further incorporates caching, cloud-based storage, usage management, and optimized API workflows to ensure scalability and responsiveness. Challenges we ran into One of the primary challenges was designing a system capable of handling the wide variety of formats found in examination questions, including mathematical expressions, diagrams, structured problem-solving questions, and image-based submissions. Another challenge was maintaining contextual continuity during follow-up interactions while ensuring responses remained relevant to the original question. We also had to develop efficient retrieval mechanisms capable of searching large collections of examination materials while delivering results with minimal latency. Balancing computational efficiency with the quality and depth of educational explanations was another key engineering challenge throughout development. Accomplishments that we're proud of Developed a unified platform that combines past paper discovery and AI-assisted learning. Built a multimodal question analysis system capable of understanding both text and image inputs. Implemented contextual conversational learning that allows students to engage in interactive discussions around exam questions. Created an intelligent classification pipeline that automatically categorizes questions and educational domains. Designed a scalable architecture capable of supporting large repositories of examination materials and concurrent users. Delivered a practical educational solution that addresses real challenges faced by students during exam preparation. What we learned This project deepened our understanding of information retrieval systems, multimodal AI, conversational learning systems, and large-scale application architecture. We gained valuable experience in designing educational AI systems that go beyond answer generation and focus on improving student understanding and engagement. We also learned the importance of combining efficient retrieval systems with intelligent reasoning capabilities to create meaningful educational experiences. What's next for Prime Papers Our next goal is to evolve Prime Papers into a comprehensive AI learning ecosystem. We plan to introduce personalized learning paths, performance analytics, topic mastery tracking, AI-generated practice assessments, and adaptive revision recommendations based on student performance. We also aim to expand our repository to include examination materials from more institutions and educational levels, making high-quality learning resources accessible to students at scale. <div