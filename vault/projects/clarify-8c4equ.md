---
slug: "clarify-8c4equ"
url: "https://devpost.com/software/clarify-8c4equ"
title: "Clarify"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 572
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Clarify

> Stop just reading. Start understanding. Clarify is the app that reads text aloud with natural voices & uses AI to summarize and instantly define key terms, turning text into an interactive study guide

[Devpost](https://devpost.com/software/clarify-8c4equ) · hackathon [[Student HackPad 2025]]

## Facets

**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** nextjs, react, tailwindcss, zod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for clarify

## Body

Inspiration My inspiration came from a simple, frustrating firsthand experience. I've noticed that many modern tools, even those built for accessibility, are often cluttered, complex, or inaccessible themselves whether through pricing or vendor lock in. For students with dyslexia, ADHD, or other learning differences, a wall of text is a lot more than a minor inconvenience. It's often a blocker, I wanted to use this experience to build a single, focused app that does one job perfectly: transforming dense, complex information into a simple, digestible, and accessible format. Clarify was inspired by the goal of moving a student from passive reading to active understanding What it does Clarify is a single-page web app that transforms a dense wall of complex text into an accessible, simple format. A user can paste in any text or upload a document (PDF/DOCX) and from here we can do four things: Summarise: Providing a concise summary of the core text Extract Key Terms: It pulls out a bullet pointed list of key terms and concepts which can help break down scary buzzwords acting as an automated "study guide" Reads Aloud: It uses groq integration with PlayAI and meta llama models to read the simplified content allowing for a multi-sensory learning approach, helpful for those with dyslexia. Translation features: You can translate into a multitude of languages which you can read from for international students who's first language may not be the one they're studying in. It also supports Translation in Arabic which you can use to read aloud with PlayAI Groq's Arabic TTS Model. How we built it The project was built with v0 vercels coding agent, used to take a low code approach. This also helped with the strict deadline of the 48 hour hackathon. Frontend: I used NextJS / React to build a clean, responsive and accessible UI. Using NextJS allowed for maximum performance with excellent built in accessbility, vital for Clarify. Backend: The core logic is built on API calls through NextJS to groq's LLM's specifically production Llama Models and PlayAI's english / arabic TTS models. I also have included zod validation to ensure that API calls included the required data Challenges we ran into I had to fight the temptation to add more complex features and remind myself of the 48 hour time constraint. Within Clarify you can see the "Upload PDF or DOCX" button. This was my stretch goal. I very quickly learned that file parsing and text extraction from PDFs is a massive, complex challenge in itself. To deliver a working product, I had to descope that feature and focus on the core paste text functionality until I was certain I had enough time to implement other features. Accomplishments that we're proud of Solving the core problem given the time constraint is what I'm proud of. That my accessibility app is actually accessible. I prioritized keyboard navigation and semantic HTML from the start, not as an afterthought and for my first ever hackathon, I love it. What we learned De-scoping and prioritising features is important and getting a working, polished smaller project is way better than a broken ambitious one band app. What's next for Clarify I will continue to work on clarify, ensuring that its up to date and doesn't get lost in time with broken features, inaccessible navigation or even stay stagnant. I'll also speak with other students around my network that will give me vital go-to-market feedback <div