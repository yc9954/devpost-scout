---
slug: "skillscan-ai-career-gap-analyzer-for-students-vw8imb"
url: "https://devpost.com/software/skillscan-ai-career-gap-analyzer-for-students-vw8imb"
title: "SkillScan — AI Career Gap Analyzer for Students"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 1042
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/agriculture_food"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/labor_employment"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# SkillScan — AI Career Gap Analyzer for Students

> AI that scans your resume, finds your skill gaps, builds your learning roadmap, and scores your job match — so you get hired, not rejected.

[Devpost](https://devpost.com/software/skillscan-ai-career-gap-analyzer-for-students-vw8imb) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[agriculture_food]] [[developer_tools]] [[education]] [[labor_employment]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]] [[video_visual]]

**stack** css, react, supabase

## How they structured the write-up

- 🎯 inspiration
- 💡 what it does
- 🛠️ how i built it
- ⚔️ challenges i faced
- 📚 what i learned
- 📊 impact potential
- 🔮 what's next

## Body

🎯 Inspiration Every semester I watched brilliant students get rejected from jobs they were qualified for. Not because they lacked potential. Not because they didn't work hard. But because nobody ever told them what was actually missing from their profile. A friend with a Computer Science degree applied to 47 data science roles in 3 months. 47 rejections. Zero feedback. She had no idea SQL Advanced was the one skill blocking every single application. That silence — that information gap between students and employers — is what SkillScan was built to destroy. 💡 What It Does SkillScan is an AI-powered career intelligence platform that tells students exactly what stands between them and their dream job — then builds a personalized roadmap to close that gap in 30 days. Four features working together as one system: 📄 Resume Scanner Upload your resume → Gemini AI scores it 0–100 → Flags every weak section → Gives exact rewrites. Not vague advice. Specific fixes that make ATS systems and recruiters stop scrolling. 🔍 AI Career Gap Analyzer Select your dream role → AI compares your skills against real market demand → Returns a Gap Score with every missing skill ranked by hiring priority. Learn the right skills in the right order. 🗺️ Skill Roadmap Generator Gap analysis feeds directly into a personalized 30-day learning plan. Daily tasks, specific resources, milestones, and an estimated job-ready date — all generated in seconds. 🎯 Job Match Score Paste any job description from anywhere → Instant match percentage → Green skills you already have → Red skills standing in your way. Know before you apply. Apply when ready. 🛠️ How I Built It Built entirely as a solo developer using Lovable.dev for rapid full-stack development combining React, TypeScript, Tailwind CSS, and Supabase into a production-ready platform. The AI layer runs on Google Gemini Flash — handling resume analysis, skill gap classification, roadmap generation, JD parsing, and match scoring. The Gap Score Algorithm was the most complex piece to engineer. Generic skill matching gives misleading results — a student who knows Python basics shouldn't score the same as one with advanced ML experience. The solution: $$\text{Career Readiness} = \frac{\sum_{i=1}^{n} w_i \cdot p_i}{\sum_{i=1}^{n} w_i} \times 100$$ Where: \( w_i \) = hiring frequency weight per skill \( p_i \) = student proficiency score (0, 0.5, or 1) Result normalized to \( [0, 100] \) Priority ranking formula: $$\text{Priority}_i = f_i \times d_i$$ Where: \( f_i \) = frequency in job postings (0–1) \( d_i \) = difficulty to acquire (inverse weight) High frequency + lower difficulty = learn first. The Roadmap Generator uses a constraint-based scheduling algorithm — fitting learning tasks into the student's available daily hours while respecting prerequisite dependencies between skills. Architecture: Resume PDF Upload ↓ Gemini Vision → Text Extraction ↓ Skill Entity Recognition ↓ Gap Analysis Engine ↓ Priority Ranking Algorithm ↓ Roadmap Constraint Scheduler ↓ Job Match Comparator ⚔️ Challenges I Faced 1. Resume parsing accuracy Early builds misread PDF formatting — bullet points became garbled text, columns merged incorrectly. Fixed by preprocessing PDF text through Gemini Vision before skill extraction, which handles any resume format reliably. 2. Gap score gaming Beta testers found they could inflate their gap score by selecting all skills as "Advanced." Fixed with a verification prompt — Gemini asks 1–2 quick questions per claimed skill and adjusts the proficiency score based on answers. You can't fake your way to a high match score. 3. Roadmap overwhelm First roadmap designs showed students 15–20 skills to learn simultaneously. Every tester felt overwhelmed and closed the app. Redesigned with a strict 3-skill-at-a-time constraint — focus on the top 3 priority gaps, complete them, then unlock the next 3. Completion rate jumped dramatically. 4. Job description parsing variance JDs from different companies use wildly different formats and terminology. "Proficiency in Python" vs "Python experience required" vs "Python 3.x" all mean the same thing but look different to basic parsers. Fixed with semantic matching via Gemini — understands meaning, not just keywords. 📚 What I Learned Information asymmetry is the real skills gap AI is most powerful when it replaces guessing with data-driven clarity Overwhelming users with too much data is as bad as giving them none The best career tool feels like a mentor — honest, specific, and actionable Solo building forces every feature to earn its place in the product 📊 Impact Potential If SkillScan helps just 1% of India's 8 million annual engineering graduates identify and close their skill gaps: $$\text{Students Helped} = 8{,}000{,}000 \times 0.01 = 80{,}000$$ At even a 30% improvement in hiring success rate, that translates to: $$\text{Additional Hires} = 80{,}000 \times 0.30 = 24{,}000 \text{ students hired}$$ Every one of those represents a family changed, a career launched, a life transformed. 🔮 What's Next AI mock interview simulator LinkedIn profile analyzer College placement cell dashboard WhatsApp skill check bot Salary predictor per skill combination 500K student dataset for better AI The gap between a student and their dream job is not talent. It's information. SkillScan closes that gap. --- ## 🛠️ BUILT WITH React TypeScript Tailwind CSS Framer Motion Recharts Supabase PostgreSQL Google Gemini API Lovable Netlify GitHub --- ## 🔗 TRY IT OUT LINKS Link 1 — Live Demo: https://skill-path-finder-58.lovable.app/ Label: "🚀 Try SkillScan Live" Link 2 — GitHub Repository: https://github.com/Vijayalakshmi2608/skill-path-finder-58/ Label: "💻 View Source Code" Link 3 — Demo Video: https://youtu.be/XOd-IyFhl5k Label: "🎬 Watch 4-Min Demo" --- ## 🖼️ IMAGE GALLERY Upload these 4 screenshots in this order: Image 1 — Resume Scanner → Score card visible + weakness tags Image 2 — Career Gap Analyzer → Gap score + missing skills ranked Image 3 — Skill Roadmap → 30-day week by week plan visible Image 4 — Job Match Score → Green ticks + red crosses visible All screenshots: ✅ Fullscreen (F11) before capturing ✅ Use demo profile with pre-filled data ✅ 3:2 ratio crop before uploading ✅ JPG format under 5MB each --- ## ✅ Final Submission Checklist ☑️ Project name filled ☑️ Elevator pitch filled ☑️ About the project pasted ☑️ Math formulas rendering correctly ☑️ Built with tags added ☑️ Live demo link added ☑️ GitHub link added ☑️ YouTube demo link added ☑️ Thumbnail uploaded ☑️ Save & Continue clicked 🏆 <div