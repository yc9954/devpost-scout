---
slug: "ai-flashcard-maker"
url: "https://devpost.com/software/ai-flashcard-maker"
title: "AI Flashcard Maker"
hackathon: "Adobe Express Add-ons Hackathon"
organization: "Adobe"
winner: true
words: 202
team_size: 5
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
  - "substrate/document_pdf"
---

# AI Flashcard Maker

> Instantly turn documents and notes into engaging and print-ready flashcards, utilizing AI and auto-layout

[Devpost](https://devpost.com/software/ai-flashcard-maker) · hackathon [[Adobe Express Add-ons Hackathon]]

## Facets

**domain** [[developer_tools]] [[education]] [[scientific_research]]
**user** [[educator_student]]
**substrate** [[document_pdf]]

**stack** add-on-sdk, google-cloud, gpt-4o-mini, javascript, llmproxy, pdfjs-dist, react, tesseract

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- special thanks

## Body

Inspiration For teachers, turning teaching materials into flashcards often means spending hours coming up with questions, formatting layouts, and preparing files for print. Thats why we built AI Flashcard Maker in Adobe Express, so that teachers with less design experience could easily make beautiful flashcards on the platform that simplifies graphic creation. What it does With automated text extraction, AI, and auto-layout, it instantly turns documents and notes into engaging and print-ready flashcards. How we built it Using tools like pdfjs, tesseract, it supports extracting text from frequently used file types like PPTX, PDF, PNG, and JPG. With GPT-4o mini, it extracts important concepts within the documents to generate Questions and Answers. With the AddOn SDK, we then calculate the layouts and insert the flashcards into the pages. By putting our backend on Google Cloud, we are allowed to put all our code into an Adobe Express Add-on private listing. Challenges we ran into Packaging for production environment, navigating the add-on documentation, and deploying to Google Cloud. Special Thanks Than you for the Networking at Tufts Lab at Tufts University for providing the LLMProxy, which is made possible by their research paper LLMProxy: Reducing Cost to Access Large Language Models . <div