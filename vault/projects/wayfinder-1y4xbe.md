---
slug: "wayfinder-1y4xbe"
url: "https://devpost.com/software/wayfinder-1y4xbe"
title: "Wayfinder"
hackathon: "USAII® Global AI Hackathon 2026"
organization: "USAII"
winner: true
words: 1279
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/structural_withholding"
  - "domain/civic_government"
  - "domain/immigration_refugee"
  - "domain/legal_justice"
  - "domain/mental_health"
  - "user/legal_professional"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/regulation_legal_text"
  - "substrate/structured_db"
---

# Wayfinder

> Your personal AI caseworker for U.S. refugee benefits. Answer a few questions, see what you qualify for, and let Wayfinder auto-fill your applications so you never have to figure out the system alone.

[Devpost](https://devpost.com/software/wayfinder-1y4xbe) · hackathon [[USAII- Global AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[structural_withholding]]
**domain** [[civic_government]] [[immigration_refugee]] [[legal_justice]] [[mental_health]]
**user** [[legal_professional]] [[social_worker]]
**substrate** [[document_pdf]] [[regulation_legal_text]] [[structured_db]]

**stack** chrome, css, esbuild, eslint, javascript, jose, next.js, pdf-lib, pdf.js, pdfjs-dist, postgresql, react, react-dropzone, sharp

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for wayfinder

## Body

Landing Page Create Account Action Plan Fill out form with AI Wayfinder A personal AI caseworker for refugees navigating the U.S. benefits system. Inspiration Refugees arriving in the U.S. have just 90 days of formal resettlement support. After that, they are expected to navigate dozens of federal benefit programs on their own — programs that were designed for them but are often nearly impossible to access without help. The U.S. Department of Health and Human Services has documented that many eligible immigrants never apply at all , not because they do not need the help, but because they cannot read the application, do not know what they qualify for, and have no one left to guide them. Caseworkers are already carrying two to three times their recommended caseload, and cash assistance windows can be as short as four months . We built Wayfinder because the gap between “eligible” and “enrolled” should not exist — and it does not have to. What It Does Wayfinder acts as a personal AI caseworker for refugees navigating U.S. benefits. A user answers a short onboarding questionnaire covering their immigration status, arrival date, household size, and income. Wayfinder then instantly shows them: Which of 27 federal programs they likely qualify for When each deadline is , ranked by urgency What documents they need What to do next , all in their native language When it is time to apply, Wayfinder auto-fills application forms using information the user already provided, so they never have to re-enter the same details across multiple programs. Sensitive fields like Social Security numbers are never touched by the app; users enter those directly on official government sites. Nothing is ever submitted on their behalf. Users must review all information — and consult an attorney if needed — before submission. How We Built It We built a structured benefits database from scratch covering 27 federal programs , compiling eligibility rules, deadlines, required documents, and program conditions from publicly available government sources, including ORR policy documents, USCIS guidance, and federal statutes. Each entry is manually reviewed for accuracy and includes source citations and a last-verified date. The deterministic eligibility engine runs each user’s profile against this database and surfaces matched programs ranked by deadline urgency , so the most time-sensitive opportunities never get buried. The form auto-fill system uses a blocklist that ensures sensitive fields are never auto-populated, and a mandatory review checkbox keeps the human in control before they ever leave the app. For benefits that require legal counsel, the fill button is disabled entirely and replaced with a referral to legal aid — determined by a hardcoded rule rather than a model decision. Crucially, we did not build Wayfinder in a vacuum. We ran a small pilot program with five refugee volunteers , and their feedback shaped the product at every stage. They told us our first onboarding flow was too long and asked too much at once, so we cut it down and rewrote every question in plainer language . They showed us that a wall of eligible programs was overwhelming, which is exactly why we moved to ranking by deadline so people see the one thing they need to act on first. Their hesitation around “what happens if I get something wrong?” directly drove how seriously we treated the review-before-you-leave step. The people we built this for did not just test Wayfinder at the end — they helped design it. Challenges We Ran Into Federal benefits policy is complex, constantly changing, and spread across dozens of sources that do not always agree with each other. Building a database we could actually trust meant going back to primary government sources, reading them carefully, and making judgment calls about what each rule means in practice. We solved this by structuring every entry with its own source citations and a last-verified date, and by requiring a human to review and approve any update before it goes live , so the data never drifts out of sync with reality. The harder challenge was responsible AI design : deciding where to draw the line between helpful automation and dangerous over-reliance. Immigration applications carry real legal consequences, and a single wrong field can cost someone food assistance or affect their status for years. We solved this structurally instead of relying on the model to behave: Sensitive fields are blocklisted in code so they can never be filled. The button to continue to the official site stays disabled until the user checks a mandatory review box. Legal cases are routed to attorneys by a hardcoded rule that no model output can override. Rather than trusting the AI to avoid the worst-case outcome, we made the system incapable of causing it. Our pilot users sharpened this thinking. Watching real people move through the app made the difference between “automation that helps” and “automation that overreaches” feel far more concrete than any design discussion could. Accomplishments That We’re Proud Of We are proud that Wayfinder is genuinely useful to the people it was built for — not just a demo that looks good, but a tool that could realistically help someone navigate a system that has historically excluded them. We do not just believe that; we watched it happen in our pilot, where five refugees used Wayfinder and helped us refine it into something that actually fits the way they move through the world. We are especially proud that the responsible AI guardrails are not bolted on as an afterthought — they are built into the architecture. Sensitive fields are blocklisted in code. The submit path stays locked until review is complete. Legal cases go to attorneys, not to a model. We designed a system that is structurally incapable of causing the outcome we were most worried about, and that intentionality is the part we are proudest of. What We Learned We learned that responsible AI is not just about what a model says — it is about what the system around it allows. The most important design decisions we made had nothing to do with prompting and everything to do with the actions the app structurally cannot take. We also learned how much is lost in the gap between policy and practice . The rules exist, the programs exist, the funding exists — but for someone who does not speak English and just arrived in a new country, none of that is accessible without a guide. Our pilot drove this home more than anything else: the features we thought mattered were not always the ones that mattered to the people using it. Closing that gap turned out to be less about technology and more about meeting people exactly where they are — and the only way to know where that is, is to ask them. What’s Next for Wayfinder Expanding the Benefits Database Beyond Federal Programs Our biggest priority is growing past the current 27 federal programs to cover state-level programs , which vary significantly from state to state and are often where the most critical gaps are. Voice Mode Many of the people Wayfinder serves are far more comfortable speaking than reading or typing — especially in a new language, and especially on a phone. We want to add a voice mode that lets users complete onboarding, hear which programs they qualify for, and get their next steps entirely through spoken conversation in their native language . For someone who cannot comfortably read an English form or a translated one, being able to simply talk to Wayfinder could be the difference between getting help and giving up. It is the most natural extension of our core mission: meeting people exactly where they are . <div