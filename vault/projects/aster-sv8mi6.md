---
slug: "aster-sv8mi6"
url: "https://devpost.com/software/aster-sv8mi6"
title: "Aster"
hackathon: "ML Empowerment Build Challenge 2.0"
organization: "ML Empowerment Foundation"
winner: true
words: 1440
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/accessibility"
  - "domain/education"
  - "domain/labor_employment"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/document_pdf"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Aster

> Aster speaks the part of a lecture nobody says out loud, so blind and low-vision students can follow any YouTube lesson. It stays silent when the teacher has already explained it.

[Devpost](https://devpost.com/software/aster-sv8mi6) · hackathon [[ML Empowerment Build Challenge 2.0]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[accessibility]] [[education]] [[labor_employment]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[document_pdf]] [[transcript_audio]] [[video_visual]]
  <sub>weak: financial_record</sub>

**stack** azure, docker, express.js, ffmpeg, gemma, google-ai-studio, next.js, node.js, pdf.js, react, tailwindcss, typescript, web-speech-api, yt-dlp

## How they structured the write-up

- project title
- links
- project files
- project description
- problem statement
- solution overview
- key features
- technologies used
- target users
- team details

## Body

Project Title Aster — Learning You Can Hear Links Live demo https://aster-coral.vercel.app Source https://github.com/AuvroIslam/Aster Video https://youtu.be/ANY_swvypIY Project Files They require at least one file showing functionality or design . Upload in this order: File What it shows docs/screenshots/04-description-timeline.png 25 moments examined · 12 described — the AI's judgement as a number docs/screenshots/05-speaking-caption.png A description holding the video, revealed as it is spoken docs/screenshots/10-study-page-explained.png A real diagram-heavy page with Aster's explanation underneath docs/screenshots/08-voice-search.png Spoken search — a lesson found with no sight docs/screenshots/00-demo-thumbnail.png Cover image Video (optional here): https://youtu.be/ANY_swvypIY Project Description Category: Machine Learning/AI · Social Good Problem Statement A student goes to YouTube because that is where the syllabus is taught for free. It is the great equaliser of this generation: a student in a village can watch the same lecture as a student in a capital city, and it costs neither of them anything. Then, fourteen minutes in, the teacher stops talking, draws a parabola on the board, and says four words: "As you can see here…" For a blind student the lesson ends right there. Not because the physics is beyond them, but because nobody said out loud what was on the screen. A sighted classmate takes in the curve in half a second and moves on; a blind learner hears silence, then a sentence that assumes they saw it. This repeats every few minutes, in every subject, for their entire education. The scale of this is not niche. 43 million people are blind and 2.2 billion live with vision impairment — and 90% of them are in low- and middle-income countries . That is precisely where free video is the only affordable teacher, and precisely where professionally described course material will never arrive. The gap sits directly on top of the largest body of free teaching ever assembled, and it widens every year that body grows. Why the existing options do not close it: Option Why it fails Screen readers They read the interface , not the lesson. The play button is announced; the diagram is not. Captions & transcripts They carry the words the teacher said — and the entire problem is what the teacher didn't say. "As you can see here" is captioned perfectly and means nothing. Describe-everything AI It narrates every frame and talks over the instructor. Two voices at once is noise, not a lesson. Waiting for accessible content Audio description is the real fix, but it is manual and expensive, so it exists for almost no educational video — and never for the lecture needed tonight. Solution Overview Aster uses a multimodal AI model to ask a different question than every other tool in this space. For each candidate moment it does not ask "what is on screen?" — it asks: "Can the learner follow this without seeing it?" Only when the answer is no does it generate a description, and it places that description inside a natural pause in the narration, so it never overlaps the instructor. This decide-first, describe-second design is the core of the project. On a real 18-minute lecture, Aster examined 25 candidate moments and described only 12 — staying silent at the other 13. That ratio is the system working, not failing. A tool that described all 25 would be far easier to build and useless to listen to. The rule behind everything: silence is better than a wrong description. How the AI decides. The model returns a confidence score with every judgement, and three thresholds govern what happens next: ≥ 0.85 — speak normally 0.60 – 0.85 — speak only when the visual information is genuinely critical < 0.60 — discard it and stay silent Two timing constraints decide where a description may go: a silence must be at least 1.2 seconds to be worth speaking into, and no two descriptions may fall within 8 seconds of each other. When a description is too long for the pause it lands in, Aster holds the video until the sentence genuinely finishes, then resumes — which is exactly WCAG 2.2 Success Criterion 1.2.7, Extended Audio Description . The behaviour implements a recognised accessibility standard rather than being an ad-hoc choice. Key Features 1. Decide-first audio descriptions. Every moment is a decision before it is a description. Most of the time the decision is silence. 2. Never talks over the teacher. Descriptions land in natural pauses. A long explanation pauses the video instead of being cut short, and if the learner resumes playback mid-sentence, speech stops immediately so two voices never collide. 3. Ask about the exact frame on screen. Pause anywhere and ask — by keyboard, by one of eight one-key preset questions, or out loud. Answers are grounded in that frame and that lesson, so "read the code" returns the code actually displayed rather than a plausible invention. 4. Practice built from the gap, not the lesson. This is the teaching method and it is what separates Aster from a quiz generator. Two signals drive every practice question: a visual Aster had to describe (the concept arrived through the ear — second-hand, single pass, nothing to glance back at) and a question the learner asked (a timestamped admission of uncertainty). A concept the instructor narrated fully is never tested — the learner received it on equal terms with a sighted student, so there is no gap to close. Miss a question and the concept is re-explained from a different angle, never in the same words, then asked again later. 5. Beyond video — notes and textbooks. The same treatment for PDFs and textbook chapters, describing the figures, tables and diagrams that a plain text extraction silently discards, then generating quizzes from the student's own syllabus. 6. Multilingual by default. Aster reads the video's own caption language and describes the lesson in that same language, so a Bengali physics lecture is described in Bengali. 7. Usable with no sight at all. Full keyboard control, screen-reader announcements, and spoken search — hold one key, say what you want to learn, and the results are read back aloud. Technologies Used Layer Technology AI model Gemma 4 (multimodal, gemma-4-31b-it ) via the Google AI Studio / Gemini API — generates every description, answer and practice question Reliability A three-rung fallback ladder: primary key → second key on a separate account → alternate host, so a free-tier quota exhausted mid-video does not end the lesson Transcripts The video's own caption tracks (json3 / WebVTT) Media pipeline yt-dlp (retrieval and search) · ffmpeg / ffprobe (frame extraction) Documents PDF.js — text, tables, formulas and figure extraction Speech Web Speech API — synthesis and recognition run in the browser, so spoken search and spoken answers need no key and no server round trip Backend Node.js · Express — the full description pipeline and caching layer Frontend Next.js · React · TypeScript Deployment Docker · Azure App Service (API, with a persistent cache) · Vercel (web app) Caching is keyed by video, model, prompt version, language and pipeline settings, so a second viewing costs zero downloads and zero model calls — while changing any of those inputs correctly invalidates the result. This is what makes the project affordable to run at scale: each video is processed exactly once, ever. Target Users Primary — blind and low-vision students. Low vision is far more common than total blindness, and those learners are usually left out entirely: captions do not help them, and describe-everything tools are as unusable for them as for anyone else. Because Aster speaks only where the screen carries information the narration leaves out, it is useful to someone who can see some of the screen but not the small print in a terminal or the labels on a diagram. Especially students in low- and middle-income countries , where 90% of vision loss is concentrated and where free online video is often the only accessible teacher available. Secondary beneficiaries: Teachers and institutions serving blind students, who currently have no affordable way to make existing video material accessible Auditory learners and anyone studying without looking at a screen — commuting, or with tired eyes Content creators , who gain accessible versions of their lectures without doing any work themselves The goal: any lecture video on the internet becomes usable by a blind student, without asking the creator to do anything. Team Details Member Role Tasnim Hossain Orna Concept, narrative and communication — idea generation and problem framing, user research and positioning, presentation design, demo video production Oitijya Islam Auvro Full-stack and AI engineering — the complete technical build: AI description pipeline and prompt design, Gemma integration, backend and API, frontend, accessibility implementation, and cloud deployment <div