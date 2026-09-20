---
slug: "lablens-rtavzo"
url: "https://devpost.com/software/lablens-rtavzo"
title: "LabLens"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 774
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "user/educator_student"
  - "substrate/geospatial"
---

# LabLens

> A Socratic STEM tutor that diagnoses misconceptions — not just answers questions.

[Devpost](https://devpost.com/software/lablens-rtavzo) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[vision_ocr]]
**domain** [[education]] [[finance_payments]] [[health_clinical]]
**user** [[educator_student]]
**substrate** [[geospatial]]

**stack** 15, css, css-frameworks-next.js-15, css?-next.js-15, featherless.ai, languages-typescript, openai, react-19-platforms-vercel-apis-featherless.ai-(openai-compatible), typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for lablens

## Body

Inspiration Most AI tutoring tools solve the wrong problem. When a student asks ChatGPT why they got a physics question wrong, it gives them the right answer — which they copy down and move on. The misconception that caused the error in the first place is never touched. We kept thinking about a student who genuinely believes "current gets used up across resistors" — no matter how many times they read the correct explanation, that wrong mental model persists. The real intervention isn't correction; it's diagnosis . That's what LabLens is built around: finding the exact flaw in a student's thinking and collapsing it through their own reasoning, not ours. What it does LabLens is a Socratic STEM tutor that diagnoses cognitive misconceptions rather than just correcting wrong answers. Students start by interacting with a live mini-lab — adjusting circuit voltages, mole ratios, or function inputs — before typing anything. Their lab behavior already reveals their mental model. Then they explain their reasoning in free text, and LabLens classifies the exact misconception, issues a targeted Socratic question (never the answer), and deepens the hint one level per turn until the student finds the insight themselves. A follow-up check with a structurally identical question verifies the misconception was actually repaired. Every session produces a teacher-ready report: misconception diagnosed, hint chain used, progress level, and recommended next pedagogical step. We cover 6 subjects: Physics (series circuits), Calculus (derivatives), Chemistry (stoichiometry), Biology (osmosis), Mechanics (Newton's Third Law), and Algebra (quadratics). How we built it The stack is Next.js 15 with React 19 App Router on the frontend, deployed to Vercel Edge. The AI backbone is Qwen/Qwen2.5-72B-Instruct, accessed through Featherless.ai's OpenAI-compatible API. The core of the system is a hand-authored misconception taxonomy per subject — a structured map of the most common wrong mental models and the Socratic questions that best expose each one. This taxonomy is injected into the system prompt on every API call, and the model returns structured JSON containing the misconception class, hint text, cognitive progress chips, and the recommended next move. The mini-labs are built as interactive React components with live parameter controls that feed their state into the chat context alongside the student's explanation. Challenges we ran into Getting the model to never give the answer directly was the hardest prompt engineering challenge. General-purpose LLMs default to being helpful by explaining things — fighting that instinct while still producing pedagogically useful Socratic questions required extensive iteration on the system prompt and the misconception taxonomy. We also found that structured JSON output consistency was tricky at the 72B scale — we had to carefully constrain the output schema and add fallback parsing to handle edge cases. On the UI side, making the mini-lab state feel natural and intuitive while also being rich enough diagnostic signal for the AI took several iterations. Accomplishments that we're proud of The moment when a student in testing said "oh — so the current doesn't actually get used up ?" after two Socratic questions from LabLens — without us ever saying the word "conservation" — that was the validation we needed. On the technical side, we're proud of the misconception taxonomy system: it's not just prompt engineering, it's a structured pedagogical knowledge base that makes the AI's responses genuinely targeted rather than generic. We're also proud of shipping a full product — working AI, live mini-labs, teacher reports, and a polished UI — in 36 hours. What we learned Pedagogy is a domain of its own. We came in thinking the hard part was the AI integration — it turned out the hard part was understanding why specific misconceptions are sticky and what kinds of questions actually dislodge them. Reading research on conceptual change theory mid-hackathon was not something we expected to do. We also learned that Featherless.ai's access to open-weight models like Qwen2.5-72B is genuinely competitive with closed APIs for structured reasoning tasks — the instruction-following quality exceeded our expectations for a model we could access without a waitlist. What's next for LabLens Persistent student profiles that track misconception history across sessions and flag recurring gaps for teacher review. Curriculum alignment — tagging each misconception to AP, IB, and Common Core standard codes so the teacher report maps directly to what needs to be addressed before the next unit. A classroom dashboard with real-time misconception heatmaps across a cohort. And more subjects: Statistics (p-value misinterpretation is epidemic), Thermodynamics, and Organic Chemistry are the next candidates. The longer-term vision is a tool where a teacher can see — in one view — exactly which mental models their entire class is holding wrong, before the exam reveals it. <div