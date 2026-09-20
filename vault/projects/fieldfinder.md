---
slug: "fieldfinder"
url: "https://devpost.com/software/fieldfinder"
title: "FieldFinder"
hackathon: "Youth Code x AI"
organization: "Youth Code Foundation"
winner: true
words: 686
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/structural_withholding"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/legal_justice"
  - "domain/mental_health"
  - "user/clinician"
  - "user/educator_student"
  - "user/legal_professional"
  - "user/researcher"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# FieldFinder

> AI maps every career, course, university, and opportunity in any field, personalized to exactly where you are in school.

[Devpost](https://devpost.com/software/fieldfinder) · hackathon [[Youth Code x AI]]

## Facets

**mechanism** [[structural_withholding]]
**domain** [[education]] [[labor_employment]] [[legal_justice]] [[mental_health]]
**user** [[clinician]] [[educator_student]] [[legal_professional]] [[researcher]] [[social_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]] [[web_dom]]

**stack** claude, css, groq, html, javascript, llama

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for fieldfinder

## Body

cool little image i told AI to make. I liked it!!! Inspiration Career planning for students is broken. You search online and get outdated articles, your school counselor is overbooked, and when you ask your parents the answer is always doctor or lawyer. Nobody hands students a real map. I'm 16, a junior in high school, and I was living this problem myself. I wanted something that could actually show me what careers exist in a field I'm curious about, what I should be doing right now to get there, and what the path looks like from where I am. That tool didn't exist, so I built it. What it does FieldFinder lets any student type in a field they're interested in, enter their age, and instantly receive a fully personalized career and education plan. The platform covers nine areas: careers in the field, courses to take in school with links to free learning resources, opportunities like clubs and internships matched to their stage, university recommendations tagged as Safety, Match, or Reach based on their academic profile, salary and job outlook data, skills employers actually hire for, scholarships with real amounts and deadlines, a step-by-step career roadmap, and a resume scanner that redacts personal information before the AI ever sees it and returns a full breakdown of the student's strengths, gaps, and career alignment. Every section adapts based on whether the student is in middle school, high school, college, or graduate school. How we built it The entire project was built solo — frontend, backend, and AI integration. The frontend is vanilla HTML, CSS, and JavaScript with a custom design system and a panel caching layer so navigating between sections never re-fetches data unnecessarily. The backend is a FastAPI server in Python that connects to Groq's API using four keys in round-robin rotation with automatic failover. If the primary model hits its daily token limit, the backend silently switches to a faster fallback model so the app stays live. The resume scanner uses pypdf for text extraction, Groq's vision model for image-based uploads, and a regex-based scrubber that strips names, emails, phone numbers, and other PII before anything reaches the AI. Challenges we ran into The biggest challenge was rate limits. All four API keys share an org-level daily token budget, and during testing the entire quota was exhausted simultaneously. I had to build automatic model fallback logic mid-hackathon to keep the app functional. Getting the LLM to return reliable structured JSON across nine different endpoints with different schemas was also harder than expected, I ended up writing a best-effort parser that handles the model's occasional formatting inconsistencies gracefully. Accomplishments that we're proud of Building a complete, polished full-stack application solo in two weeks across nine distinct AI-powered features is something I'm genuinely proud of. The PII redaction running before any user data reaches the model was a deliberate design decision, not an afterthought and I think that matters when the users are students uploading personal documents. The backend staying live under real API pressure through key rotation and model fallback was a technical challenge I didn't anticipate at the start but figured out under pressure. What we learned I learned how to design prompts that return reliable structured data at scale across many different use cases, and how to build a backend that handles failure gracefully rather than crashing. More than anything, I learned how much faster you move when you genuinely care about the problem you're solving. This isn't a project I built to win a hackathon but it's a tool I actually needed, and that made every hard part worth figuring out. What's next for FieldFinder The immediate priorities are saved profiles so students can pick up where they left off, and a mobile version since these are questions students ask on their phones. Longer term, I want to build mentor matching to connect students with professionals in their chosen field, a college application tracker built on top of the university finder, and school partnerships that bring FieldFinder into counselor workflows so it extends their reach rather than sitting outside the system. <div