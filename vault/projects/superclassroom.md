---
slug: "superclassroom"
url: "https://devpost.com/software/superclassroom"
title: "Superclassroom"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 484
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/education"
  - "domain/health_clinical"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Superclassroom

> Adaptive Learning Content Generation for Students with Disabilities

[Devpost](https://devpost.com/software/superclassroom) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[accessibility]] [[education]] [[health_clinical]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** intersystems, iris, mistral, rag, vectors

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that we're proud of
- what's next for superclassroom

## Body

Home screen Example of generated notes Generated Practice Exam Dyslexia-friendly overlay Inspiration Every since I could remember, I've happily dedicated countless hours to helping my brother, Zac, digest content and prepare for his exams. Zac was very naturally smart, but always struggled with learning the way that the US education system wanted him to. As it turns out, he wasn't alone -- an overwhelming 74% of students nationwide are dissatisfied with means in which they are provided to learn and absorb concepts, and are proven to perform upwards of 200% better when introduced to more adaptive ways of learning. But it gets bigger than that -- Zac was also diagnosed with dyslexia, making his journey towards academic success an even steeper climb. The support for dyslexia in the US remains a frightening concern, as over 95% of diagnosed dyslexics claim that they do not receive the appropriate accommodations in school, amongst the rigid education system. Inspired by my brother's struggles and the infinite curiosity that lie in the different ways that human beings love to learn -- I wish to create a platform that is able to adapt to each student's individual needs. What it does Superclassroom is a student-adaptive exam preparation and learning material generation tool designed to adapt to each student's needs. Students using the platform will upload course material relevant to their upcoming exam or topics that they want to study, establishing a personalized knowledgebase for each course the student is taking. Superclassroom then uses this information in a RAG pipeline to generate highly-relevant course study material, such as comprehensive notes, topic summaries, adaptive flashcards, and practice exams. There is also a space to leave notes about the student's profile, which is used in the RAG pipeline to generate more personalized results and accommodate disability. How I built it Superclassroom is built with MCP servers and RAG architecture with Intersystem's Iris vectorized database and vector search to store multimodal sources of course content. Superclassroom then uses Mistral's LLM along with the relevant information to create highly accurate and relevant results based on the documents that the student provides. Superclassroom uses a dataset of over 1200 relevant documents in the pipeline related to disability, accessibility, and research on how to best provide a positive learning experience in order to generate adaptive and considerate learning material. Challenges I ran into The hardest challenge for me was definitely finding a way to accommodate all kinds of learners. Incorporating notes about the student's learning styles into the RAG pipeline was a great way to work around it and develop a platform that can truly adapt on its feet. Accomplishments that we're proud of Getting a tool that is functional and something that my younger brother can actually use is a huge accomplishment for me. What's next for Superclassroom Keep building and eventually develop a platform that will change the lives of many students worldwide! <div