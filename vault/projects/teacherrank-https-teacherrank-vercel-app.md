---
slug: "teacherrank-https-teacherrank-vercel-app"
url: "https://devpost.com/software/teacherrank-https-teacherrank-vercel-app"
title: "TeacherRank"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 333
team_size: 1
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
---

# TeacherRank

> A platform to rank and rate teachers to help other students make informed decisions.

[Devpost](https://devpost.com/software/teacherrank-https-teacherrank-vercel-app) · hackathon [[DSH Hacks V1]]

## Facets

**domain** [[education]]
  <sub>weak: labor_employment</sub>
**user** [[educator_student]]
  <sub>weak: structured_db</sub>

**stack** javascript, sql, supabase, typescript, vercel

## Body

Landing Page. Picking professors is guessing. You ask around, find an old Reddit thread, sign up, and by week three, the syllabus turns out to be fiction. I wanted a place where students could just say what a class was actually like. So that's the site. Search teachers by institution and department, leave an anonymous rating, and read what other students wrote. 5 stars, halves count. Top teachers get badges. It runs as a PWA, so it works on a phone with a bad signal. The stack is React 18, TypeScript, Vite, Tailwind, and DaisyUI. Forms use React Hook Form with Zod. Server state goes through React Query because my own cache layer kept being wrong. Backend is Supabase: Postgres with Row Level Security, Edge Functions, Google OAuth with PKCE. Anonymous users get a browser fingerprint so they can rate without an account, but can't easily spam. The ranking is the part I thought hardest about. One 5-star review shouldn't beat 200 reviews at 4.6, so I used a Bayesian average: $$ S = \frac{v}{v+m} R + \frac{m}{v+m} C $$ ( R ) is the teacher mean, ( v ) is their vote count, ( m ) is a threshold, ( C ) is the platform mean. Low vote counts get pulled toward the global average. Real volume wins out. Things I learned the hard way. RLS is unforgiving. I wrote a policy that looked fine and would have leaked every email in the database. Now I test policies one role at a time. Service workers served stale JS after a deploy until I versioned the cache keys. Search got slow around 5k teachers and a Postgres trigram index fixed it. Password reset emails went to spam for two weeks because I hadn't set up SPF and DKIM. The spam problem was the scariest one. One angry student with twenty burner accounts could tank a professor. Fingerprinting plus rate limits plus RLS insert checks handles most of it. I still watch it. <div