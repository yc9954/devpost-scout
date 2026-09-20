---
slug: "phonaify"
url: "https://devpost.com/software/phonaify"
title: "Phonaify"
hackathon: "Google Chrome Built-in AI Challenge 2025 "
organization: "Google"
winner: true
words: 569
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "user/educator_student"
  - "substrate/web_dom"
---

# Phonaify

> An AI-Powered English Pronunciation Chrome extension that detects pronunciation errors and provides real-time phonetic feedback as users read online.

[Devpost](https://devpost.com/software/phonaify) · hackathon [[Google Chrome Built-in AI Challenge 2025]]

## Facets

**mechanism** [[cross_origin_web]] [[realtime_stream]]
**domain** [[accessibility]] [[developer_tools]] [[mental_health]]
**user** [[educator_student]]
**substrate** [[web_dom]]

**stack** api.ai, crxjs, css, html, javascript, prompt, react, vite

## How they structured the write-up

- why a chrome extension?
- why a language pronunciation learning tool?
- why is ai essential in this case?
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for phonaify

## Body

Phonaify: AI-Powered English Pronunciation Assistant Why a Chrome Extension? Learning without disruption : Hover-based interaction lets users access guidance without leaving the page or breaking focus. Learn in context : Users can practice directly while reading, turning everyday browsing into an interactive experience. Why a language pronunciation learning tool? Most existing Chrome extensions focus on grammar and translation, while pronunciation support is limited. Yet for language learners, speaking accurately and confidently is often the hardest skill to master. Research highlighted three core gaps… Speaking Anxiety : Over 60% of learners struggle with speaking due to pronunciation anxiety and limited feedback. Practice Needs Feedback : Improvement requires real-time feedback to guide accurate practice. * Practice Anytime, Anywhere * : People want to learn without tutors or lessons. Why is AI essential in this case? Traditional methods can’t provide instant, personalized feedback at scale. Speech Analysis : Analyzes voice input to detect accuracy, phonetic errors. Adaptive Feedback : Generates personalized, real-time feedback tailored to users. Contextual Learning : Real-time text recognition to connect learning while reading. What it does Phonaify helps users not only learn word meanings and synonyms but also, most importantly, improve their English pronunciation while reading naturally online. By simply highlighting any word, users can listen to its pronunciation, speak into the microphone, and receive instant phonetic feedback — all without leaving the page. How we built it Working under tight timelines, with two people on the team, we leveraged AI-assisted coding tools, including Gemini CLI, to accelerate development while building primarily with React, HTML, CSS, JavaScript, Vite, CRXJS, and Prompt API. Challenges we ran into Defining the Accuracy Threshold : Determining what level of pronunciation accuracy qualifies as “correct” was complex. A 100% match felt too rigid, yet lowering the bar risked providing misleading positive feedback. The team decided to let the Gemini Prompt API dynamically decide the threshold based on context and phonetic similarity. Handling Phonetic Differences and Edge Cases : Matching phonetic sequences proved difficult when users’ input differed drastically from the expected pronunciation (e.g., “halo” vs. “slkjfdksjfdslhfsdklf lo”). We explored and adopted a simpler character-level matching approach to ensure speed, reliability, and easier integration with the local AI system. Local API - Delay : It ensures user privacy and offline access, but it also introduces a 5–8 second delay while the model is initializing. Accomplishments that we're proud of Model Stability : The Gemini Nano model required parameter adjustments to improve consistency and ensure reliable performance during experimentation. Simplified Phonetic Comparison Algorithm : Selected the Longest Common Sequence (LCS) algorithm to compare phonetic differences efficiently. Its simplicity made it easy to implement, debug, and interpret, ensuring clear, reliable feedback for users. What we learned * Prompt Iteration & Optimization * ： Experimented with multiple prompt structures to identify which formats produced the most accurate and context-aware feedback. * Advanced Prompting Techniques * : Implemented strategies like chain-of-thought prompting to enhance reasoning and output precision in phonetic analysis. What's next for Phonaify Multilingual Translation : Deepen AI integration to enable multilingual translation and support language learning beyond English. Develop System Settings : Let users choose pronunciation styles (e.g., American, British, Australian) and voice types (different genders). Expand the Learning Ecosystem : Add features that let users save words and track pronunciation history, creating a continuous learning loop. User Testing : Conduct testing to ensure usability, and identify any accessibility barriers with diverse user groups <div