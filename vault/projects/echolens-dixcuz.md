---
slug: "echolens-dixcuz"
url: "https://devpost.com/software/echolens-dixcuz"
title: "ScholarMatch"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 531
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
---

# ScholarMatch

> ScholarMatch: Unlocking the $100 Million. We use AI to instantly match students with the scholarships they're most qualified to win.

[Devpost](https://devpost.com/software/echolens-dixcuz) · hackathon [[Student HackPad 2025]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]]

**stack** json, pandas, python, streamlit

## How they structured the write-up

- 🎓 scholarmatch — project story
- 🌟 inspiration
- 🚀 what i built
- 🛠️ how i built it
- 🧠 what i learned
- ⚔️ challenges i faced
- 🌍 impact & future
- 👥 team members
- 🤖 ai tools disclosure

## Body

🎓 ScholarMatch — Project Story 🌟 Inspiration The spark behind ScholarMatch came from a simple, frustrating truth: students miss out on millions in available scholarships—not because they're unqualified, but because the search process is a nightmare. I’ve watched brilliant students—especially from underserved backgrounds—believe college was out of reach, just because they didn’t know the right scholarships existed. So I decided to build something for students, by a student . Something fast, intelligent, and actually helpful. Something that removes the guesswork from funding education. That’s how ScholarMatch was born. 🚀 What I Built ScholarMatch is an AI-powered scholarship matching platform that takes a student’s profile and instantly ranks real opportunities based on a weighted scoring system. The platform: Analyzes GPA, major, grade level, location, demographics, interests, and special circumstances Computes a personalized match score using a 7-factor weighted algorithm: $$ \text{match_score} = \left( \frac{\sum_{i} w_i \cdot f_i}{\sum_{i} w_i} \right) \times 100 $$ Provides analytics, deadline urgency, and a clean UI. Filters out scholarships the student is not eligible for. All under 30 seconds , from profile → results → insights. 🛠️ How I Built It Tech Stack Python for logic + data handling Streamlit for the UI Pandas for scoring + dataset operations JSON for persistent scholarship storage Plotly for interactive analytics Core Matching Algorithm Requirements are mapped to seven weighted factors: Factor Weight GPA 20% Major 25% Grade Level 20% Location 10% Demographics 10% Interests 10% Special Circumstances 5% Every factor contributes a weighted score, which is normalized to a final percentage. 🧠 What I Learned 1. Data design matters more than code Creating a clean, consistent, real-world scholarship dataset was way harder than expected. I learned how crucial it is to structure data before coding anything. 2. Matching systems are more nuanced than I thought I learned matching systems are complex, requiring careful handling of weights, normalization, fairness, and eligibility exclusions . It made me appreciate how recommendation engines work. 3. UX is everything A technically good tool means nothing if users get lost. I learned the importance of color-coded deadlines and why analytics help users trust the results. 4. Shipping beats perfection Deadlines force clarity. I learned to decide what was essential — and build that well. ⚔️ Challenges I Faced 1. Building a meaningful matching algorithm Balancing weights for a “fair” score was tough. Too strict gives few matches, too lenient gives useless ones. Getting it right required extensive iteration. 2. Dataset integrity Real-world scholarships have messy eligibility rules (fuzzy GPA cutoffs, vague demographics). Standardizing this data for automation took serious effort. 🌍 Impact & Future ScholarMatch already works with 60+ U.S. scholarships , but my long-term goal is bigger: Build the first open, global, crowdsourced scholarship database for Bangladesh + the Global South. In future versions, I plan to add ML-powered match refinement, an AI essay assistant, and a full application management suite (user accounts, tracking, push reminders). The dream is simple: make education accessible, one student at a time. 👥 Team Members Solo Project Built by Tamzid Ahmed . 🤖 AI Tools Disclosure I used GitHub Copilot during development to assist me with code generation for efficiency. Thanks for reading — and happy shipping! 🚀 <div