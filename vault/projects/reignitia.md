---
slug: "reignitia"
url: "https://devpost.com/software/reignitia"
title: "ReIgnitia"
hackathon: "Student HackPad 2025"
organization: "Student Hackpad"
winner: true
words: 1440
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/mental_health"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# ReIgnitia

> Power Your Potential.No Student Left Behind. No Talent Wasted.

[Devpost](https://devpost.com/software/reignitia) · hackathon [[Student HackPad 2025]]

## Facets

**domain** [[education]] [[finance_payments]] [[housing_homeless]] [[mental_health]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** css3, git, github, html5, javascript, json, three.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for reignitia

## Body

Inspiration I did not start ReIgnitia as a nice side project. I started it from fear and anger. I loved science and space. I knew I had talent. Money and lack of guidance still pushed me off track many times. Coaching cost more than my family could spare. Good mentors were rare. I found out about exams, programs and scholarships after deadlines had passed. The problem was not interest or effort. The problem was access. This story repeats in many homes. Poverty still shapes who gets to dream. Many students who count as "middle class" on paper still fight for fees, rent and basic food. A student in a village, a small town or a crowded city hostel often hits the same wall. No clear starting point. Too many random links. No safe place to ask for structured help that does not demand money. ReIgnitia comes from a promise I made to myself. Every student, in every country, should be able to open one site and find real help for learning, mental health, careers, scholarships and global chances without paying anything. No paywalls. No hidden "premium" tier. No gatekeeping by passport, postcode or income. I do not want a single child to drop a dream because of money, location or chaos at home. ReIgnitia is my first serious attempt to turn that feeling into code. A free mission control where no student is left behind and no talent is wasted. What it does ReIgnitia is a free, static, no-login web app for students. It runs fully on the front end and brings six parts of student life into one place. From the dashboard, a student can move into: 🎓 Learning Nexus A curated hub for STEM learning. It groups career roadmaps, concept explanations, virtual labs and open textbooks. Resources link to trusted free sites such as roadmap.sh, PhET simulations, NASA Eyes, MIT OpenCourseWare, OpenStax, Khan Academy and more. The goal is simple. One page where a student can see clear paths and real tools without guessing which link is fake. ⚡ Productivity Command A set of planning and focus tools on one screen. The current build includes: a Pomodoro timer block with session details an Eisenhower matrix layout for tasks guidance for notes and flashcards, plus links to tools like Notion and Anki a custom mind map editor that runs in the browser background sound options such as rain or cafe noise an eye-strain reminder that supports the 20-20-20 rule 🧘 Wellness Sanctuary A quiet space for mental health and self-check. Students can: log a daily mood write simple triggers run a guided breathing exercise view a trends section for recent entries open links for crisis and support in multiple regions Data for this page stays on the device in this version. 🧭 Career Compass A design preview for a deeper career tool. The page shows planned blocks for: skill and interest questions salary and role snapshots by field and location job trend explanations starter project ideas and resource links The copy explains that live data and full logic will come in the next build. 💰 Scholarship Vault A profile-based matcher mock with sample entries. The page includes: questions on level, region and interests a table of example scholarships with amount and deadline filter sections and planned tags text that outlines a future large dataset with global programs In this hackathon version the entries act as example data and structure, not a full live index. 🌍 Global Gateway A design preview for study abroad and global programs. The current screen shows: space for a map or globe view country and region filters program cards with fields for cost, duration and language sections for culture notes, student stories and a budget planner As with Career Compass, the page marks itself clearly as a preview. Across the site, each module states what already works and what is still a plan. Three pillars (Learning Nexus, Productivity Command, Wellness Sanctuary) are usable today. Three pillars (Career Compass, Scholarship Vault, Global Gateway) lay out the next layer that will sit on top of this base. How we built it For this hackathon build I kept ReIgnitia front-end only . No backend, no login, simple hosting. Stack HTML5 for structure and page layout CSS3 for responsive grids, cards and visual style JavaScript for timers, local state, simple charts and widgets such as the mind map and breathing tool The repo stays a standard static site that any student team or NGO can fork and host on GitHub Pages, Netlify or a similar service. Interactions and storytelling The Story page uses scroll based sections with short blocks of text and strong headings. Cards, buttons and links have clear hover and focus states written in CSS. JavaScript hooks handle timers, messages and stateful parts of Productivity Command and Wellness Sanctuary. Content and data model Learning Nexus and other pages link to trusted public resources. Examples include MIT OpenCourseWare, Khan Academy, OpenStax, PhET, NASA Eyes, Project Gutenberg, scholarship platforms and mental health support sites. The Story page uses numbers from global reports on education, poverty and mental health instead of vague claims. Resource groups and sample entries sit in structured blocks or JSON-style lists inside the project. This structure makes it easy to add more records later or move the content into a database. State The current version keeps state in the browser. Mood logs, timer states and local choices live in memory or in localStorage , depending on the page. There is no user account system yet. This keeps the prototype light and safe while still allowing basic persistence on a single device. Challenges we ran into Scope vs time The larger plan covers AI guidance, real salary data, live job and program feeds, a 3D globe, richer charts and peer cohorts. The hackathon timeline forced hard cuts. I chose three deep modules and three clear previews instead of many shallow, broken pages. Honesty in the interface It is easy to write words like "smart" or "AI driven" on cards. The hard part is staying honest when the backend is not ready. Career Compass and Global Gateway show a visible "design preview" overlay. Scholarship Vault text describes its planned dataset instead of pretending it already exists in full. Design for low resource settings ReIgnitia must work on shared lab computers and older phones on weak networks. Heavy 3D scenes and large assets would have locked those students out. I used a calm dark theme, text first layouts and external high quality tools instead of heavy custom visual effects for this first version. Accomplishments that we're proud of Built a working six pillar dashboard plus three deep modules in the short hackathon window, not just a landing page. Shipped a Story page that grounds the project in real data about education, poverty and mental health. Curated a large set of free, serious resources across learning, tools, scholarships and mental health that students can click and use today. Kept the build static and no-login , so schools, clubs and NGOs can fork it and host it without backend skills or paid services. Documented clear next steps inside the UI through preview overlays and copy, so judges and students can see how the platform will grow. What we learned Small front end tools plus strong curation can change access more than a large, half finished backend. Design for low bandwidth and low income pushes different choices. Text, PDFs and stable external tools can matter more than heavy video and complex 3D. Honest labels inside the interface such as "preview" and "coming soon" build more trust than inflated claims. A narrow, working slice of each idea is better than a wide spread of non functional buttons. What's next for ReIgnitia This hackathon version is the first orbit , not the final system. Next steps: Turn Scholarship Vault and Career Compass into real data driven modules with live filters, profiles and deadline tracking. Add a simple backend and optional accounts, so students who want sync can keep progress across devices. Bring richer 3D and data views into Global Gateway and Career Compass, including map or globe views and trend charts. Open source the resource lists and structures so schools, NGOs and student communities can extend ReIgnitia for their countries and education systems. Add a light AI helper on top of curated resources. The goal is to help students choose paths, break tasks into steps and rewrite complex text in simpler language, while keeping the platform free. ReIgnitia's long term goal stays clear. Power your potential. No student left behind. No talent wasted. AI tools: ChatGPT , Perplexity , Gemini TEAM: Pranjal Saxena <div