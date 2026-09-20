---
slug: "nextop"
url: "https://devpost.com/software/nextop"
title: "NextOp"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1393
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "domain/supply_logistics"
  - "user/clinician"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# NextOp

> 200K veterans transition out every year — most without real support. NextOp is a private AI coach that translates military careers into civilian résumés, benefits, and training.

[Devpost](https://devpost.com/software/nextop) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[civic_government]] [[health_clinical]] [[housing_homeless]] [[labor_employment]] [[mental_health]] [[supply_logistics]]
  <sub>weak: developer_tools</sub>
**user** [[clinician]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** anthropic, anthropic-sdk, brightdata, embedding, fastapi, hume, python, react, sqlite, tailwind, typescript, vite

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for nextop

## Body

Main page Recommended civilian position Tailored resume Personalized mock interview Inspiration Approximately 200,000 service members transition out of the military each year. The U.S. government spends over $13 billion annually across 45 programs at 11 agencies to support them — yet a 2024 RAND study examining all 45 federally funded programs concluded there is virtually no evidence that any of them have had a direct effect on transition outcomes. Transition Assistance Program (TAP) participants were actually associated with lower wages than non-participants. Over 95% of the $14.3 billion transition budget goes to education programs, while the direct employment support most veterans need remains drastically underfunded. This project started from a real problem one of our partners ran into. A hospital system wanted to hire veterans through DOD SkillBridge, a program where the military continues paying a service member's salary for up to six months while they work for a civilian employer. Free labor for half a year. But their HR team kept passing on the candidates because they couldn't read the résumés. A veteran applying for a registered nurse position might write: "Provided Role 2 / Role 3 trauma care in austere environments under ATP 4-02.5. Executed TCCC protocols. Maintained accountability of Class VIII supplies." That's emergency medicine in combat conditions. But an HR screener spending six seconds on it sees acronyms they don't recognize and moves on. This wasn't a one-off. 53% of service members were denied access to optional career prep tracks by their commands. Many reported that attending transition workshops signals to leadership that they're planning to leave. Over 4,300 at-risk service members — people identified as lacking stable housing, employment, or financial plans — were never connected to the support agencies they were referred to. The system measures whether someone attended a briefing, not whether anyone's life actually improved. We wanted to build something a veteran could use privately, on their own, without asking anyone's permission — something designed from the ground up to change outcomes, not check boxes. What it does NextOp is an end-to-end AI-powered transition coach with five core capabilities: AI Career Coach (Text + Voice) — A conversational coach that builds a veteran's professional profile through natural dialogue. Veterans talk about their experience in their own words, military jargon and all. The AI translates terminology in real time and populates a structured résumé as the conversation progresses. Veterans can switch to voice mode for a more natural interaction. MOS-to-Civilian Career Explorer — A data-driven career discovery engine that maps military occupation codes to civilian equivalents. Veterans can explore by MOS (direct database lookup) or by skills (semantic search against O*NET occupation profiles). Each career path shows median salary, job growth, key tasks, credential gaps, and education requirements. AI Resume Builder with Position Tailoring — The base résumé built through the coaching conversation can be tailored for specific positions. The AI rewords and reorders content to match target job requirements using enriched O*NET data, while being strictly constrained to only use information the veteran actually provided. Exports to PDF. Personalized Training Center — An AI-driven gap analysis engine that compares the veteran's profile against target position requirements, then recommends training modules ranked by impact. Includes voice-based interview role-play with emotion analysis, interactive exercises with AI feedback, and supplementary content discovered through on-demand web scraping tailored to each veteran's background. Veterans Benefits Navigator — A conversational assistant backed by a curated knowledge base of 15 high-impact federal programs with structured eligibility rules. Takes the veteran's profile and determines which programs they qualify for, what the gotchas are, and what to do first. How we built it The frontend is React + TypeScript with a split-panel coaching interface where veterans chat on the left and watch their profile update in real time on the right. The backend is FastAPI handling all AI orchestration, session management, and data pipelines. The core AI layer uses Claude (Anthropic) with tool-calling in a streaming loop. As a veteran talks about their experience, the model calls structured tools to populate the résumé live. Voice mode is powered by Hume's Empathic Voice Interface with emotion-aware prosody analysis. The career explorer is backed by a custom database combining five government data sources (O*NET, DOD COOL, BLS, MOC Crosswalk) into one unified reference table with ~1,000+ mapped career paths. Semantic search using sentence-transformers lets veterans discover careers beyond their direct MOS mapping. The benefits navigator runs on a curated JSON knowledge base we built by hand from GAO reports and .gov program documentation, with structured eligibility rules the AI can filter against. Challenges we ran into On-demand content generation vs. speed. The personalized training modules scrape and assemble content based on each veteran's specific profile and target position. This means every veteran gets genuinely relevant material instead of generic coursework, but it introduces a real latency tradeoff. We had to balance content quality against wait time and optimize the scraping pipeline to stay responsive. Tool-calling through voice. Our text-based coach uses Claude's tool-calling to update the résumé in real time. Getting the same behavior through Hume's voice pipeline was a significant integration challenge. We needed voice tool calls to route to the same backend endpoints so the profile stays in sync regardless of whether the veteran is typing or talking. Without this, voice mode would have been a separate, disconnected experience. Getting the voice agent to stop talking. The voice agent tends to keep the conversation going indefinitely. Prompting it to recognize natural stopping points and end the call at the right moment required careful iteration. Too aggressive and it cuts veterans off mid-thought. Too passive and it loops through increasingly redundant follow-up questions. No centralized benefits database exists. GAO explicitly noted that no existing inventory gives participants a complete picture of available benefits. We had to manually research each program, verify eligibility rules against current .gov sources, and structure the data ourselves. Several programs had changed status since published reports, requiring additional verification. Accomplishments that we're proud of End-to-End Intelligent Transition Infrastructure. We built a fully integrated system that guides veterans from self-discovery to employment with continuity and precision. Rather than offering isolated tools, NextOp functions as a unified transition engine: translating military experience, mapping civilian career paths, identifying credential gaps, generating personalized training, and preparing users for real interviews — all powered by a single evolving profile. The result is a structured pathway that transforms complex transition friction into an actionable, data-driven roadmap toward employment. Unified profile system across all modules. A veteran's profile is built, stored, and updated across every module on the platform. We also built a memory system with vector embedding search so that each AI agent always has the right context, regardless of which module the veteran is using. This is what makes NextOp feel like one personalized coach rather than five disconnected tools. Communication practice with real evaluation criteria. The mock interview module evaluates against veteran-specific criteria, such as whether the user slipped into military vocabulary without realizing it, which is exactly the kind of thing that confuses civilian interviewers. The emotion analysis layer adds another dimension by flagging confidence drops or stress moments during the conversation. Personalized education through on-demand scraping. Instead of serving the same generic modules to everyone, the training center scrapes and assembles content based on each veteran's background and target position. The philosophy is simple: maintain the structure that makes learning effective, but don't make people restudy things they already know. By scraping on demand, we can tie skill gaps to the veteran's actual areas of interest and surface materials that are relevant to them specifically. What's next for NextOp Better voice agent. Improved prompting and conversation design to cover a wider range of coaching scenarios, including multi-turn benefits Q&A and more nuanced career counseling through voice. AI-designed study modules. We want the agent to eventually design training modules from scratch by building a system that decomposes learning objectives based on learning theory, not just curated content. Outcome tracking. One of the core failures in existing federal programs is that nobody measures whether they work. We want to build feedback loops that track whether veterans who use NextOp actually land jobs, and which features contribute most. Community outreach and employer partnerships. Connect with veteran communities and partner with companies actively trying to hire veterans, closing the loop between veteran-side translation and employer-side demand. <div