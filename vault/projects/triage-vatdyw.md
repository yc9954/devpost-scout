---
slug: "triage-vatdyw"
url: "https://devpost.com/software/triage-vatdyw"
title: "Triage"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 744
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/revocation_withdrawal"
  - "domain/education"
  - "domain/health_clinical"
  - "user/educator_student"
  - "substrate/code_repository"
---

# Triage

> Study smart. Skip the rest.

[Devpost](https://devpost.com/software/triage-vatdyw) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[revocation_withdrawal]]
**domain** [[education]] [[health_clinical]]
**user** [[educator_student]]
**substrate** [[code_repository]]

**stack** framer-motion, git, github, google-gemini-api, localstorage, next.js-14, node.js, npm, react-18, recharts, tailwind-css, typescript, vercel, zustand

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for triage

## Body

Inspiration Students usually aren't failing because they never tried. They're failing because time is finite and study hours get spent in the wrong places. When you've got eight topics, a syllabus you barely opened, and an exam in 12 hours, the honest question isn't "what should I study?" It's what can I actually skip without paying for it tomorrow. We built Triage because every study app we tried gave us generic plans or told us to study everything. That's not realistic at 11pm the night before. We wanted something closer to a triage mindset: respect the time you actually have, the weight of each topic, and what you already know. What it does Triage helps students prioritize study time with a time aware planning approach, then makes the output easy to act on: Ruthless priority board: You plug in your subject, time left, topics, and a quick 1 to 5 confidence rating. You get back a four zone plan: Study Hard, Study Smart, Quick Pass, and Skip It. The skip feature: Triage explicitly tells you what not to study and why. No other tool we've used is willing to do that. Time adaptive scheduling: A week out gives you a spaced plan. A few days out compresses to your biggest gaps. Tonight gives you pure triage with an hour by hour schedule. Topic detail panel: Open any topic to see 2 to 3 specific study tips, a time estimate, and a checklist you can mark off as you go. Demo friendly: Built in demo mode with a realistic AP Chemistry plan so anyone can try the full experience without an API key. How we built it We shipped Triage as a Next.js 14 app using the App Router with TypeScript and Tailwind. Animations are powered by Framer Motion, state is handled with Zustand, and the AI side runs on Google Gemini 2.5 Flash through the free tier. For the hackathon timeline we leaned on localStorage so plans and progress persist without standing up a backend. The planner core is one structured Gemini prompt that returns a strictly typed JSON plan, paired with a parsing layer that strips fences, extracts the JSON, and validates every field so the app never breaks on a bad response. Challenges we ran into Getting Gemini to return consistent structured output was harder than it looked. The model would sometimes wrap JSON in markdown fences or return slightly malformed responses, so we had to build a defensive parsing layer that could survive whatever the model threw at us. We also had a real security scare. We accidentally committed an API key to GitHub early on. We caught it, revoked the key, and rebuilt the entire key system to use localStorage with a user facing input instead, so anyone using the app brings their own key safely. The confidence sweep UX was especially picky. Early designs felt like a quiz and made people second guess themselves, so we reworked it into emoji based one tap ratings until rating eight topics felt fast and low pressure. Accomplishments that we're proud of We're glad we didn't ship another fuzzy "AI study assistant" with no point of view. Triage has a stance: tell students what to skip. We're also proud the product feels cohesive: intentional motion, a clear input to plan loop, and a demo path that feels complete end to end (setup, plan generation, priority board, schedule, history). The whole flow from opening the app to seeing your plan takes under 90 seconds. What we learned When you frame studying as tradeoffs, students engage more when the app shows why something is prioritized, not just what to do next. The skip feature is the whole product, and once we framed everything around it the rest of the design clicked. We also learned that prompting is real engineering. Getting Gemini to return reliable structured JSON took way more iteration than we expected. Strong constraints and ruthless cuts matter, in both the prompt and the UI. What's next for Triage If we had more time, we'd pursue: A trained model on actual past AP, SAT, and ACT papers for real data backed topic frequency scores A post exam feedback loop so students can rate how well the priorities matched what actually appeared Progress tracking across sessions so repeat use of the same subject gets smarter over time A mobile app with a study block widget that closes the gap between planning and actually starting <div