---
slug: "career-architect"
url: "https://devpost.com/software/career-architect"
title: "Career Architect"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 787
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/labor_employment"
  - "domain/mental_health"
  - "user/educator_student"
  - "user/social_worker"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Career Architect

> Stop guessing your future. Career Architect uses AI to analyze your interests, identify your ideal career path, and provide a custom roadmap with free learning resources to get you there.

[Devpost](https://devpost.com/software/career-architect) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]] [[labor_employment]] [[mental_health]]
**user** [[educator_student]] [[social_worker]]
**substrate** [[video_visual]] [[web_dom]]

**stack** ai-generated-code, gemini-3-flash, google-ai-studio, google-gemini, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for career architect

## Body

Home Page Processing answers Career Option Proper Roadmap Inspiration We all are confused with the question: "What do you want to be?" For students and career switchers, the modern job market is overwhelming. There are thousands of career paths, but traditional career guidance hasn't kept up. Most people rely on generic aptitude tests from the 90s or fragmented advice from confused peers. We wanted to build something that feels less like a test and more like a mentor. We were inspired to create Career Architect to bridge the gap between a person's raw interests and their professional future, ensuring that no one settles for a career they don't love simply because they didn't know the roadmap to get there. What it does Career Architect is an AI-powered career counselor that takes you from confusion to a concrete plan. Conversational Discovery: Instead of rigid multiple-choice questions, the AI engages the user in a natural chat to uncover their hobbies, strengths, and hidden interests. Smart Career Matching: It analyzes the user's profile against current market trends to suggest career paths that genuinely fit their personality. The Interactive Roadmap: This is our core feature. Once a career is chosen, the system generates a dynamic, step-by-step timeline (e.g., "Month 1: Learn Python," "Month 2: Data Visualization"). Resource Curation: For every step on the roadmap, the AI provides direct links to the best free courses, YouTube playlists, and documentation, saving the user hours of research. How we built it We built Career Architect entirely using the Gemini App building ecosystem (Google AI Studio). Instead of writing complex backend code, we focused on high-level logic and prompt engineering to create a sophisticated agent. The Engine: We utilized Gemini 1.5 Pro within Google AI Studio. We chose this model for its advanced reasoning capabilities and large context window, which allows it to remember the user's entire conversation history without losing track of early details. System Instructions: We crafted a detailed "Persona" in the System Instructions. We defined the AI's role strictly as a "Professional Career Strategist," ensuring it remains empathetic, encouraging, yet realistic about job market trends. Structured Prompting: We used few-shot prompting techniques to teach the model exactly how to output the "Roadmap" so it follows a clear Month-by-Month structure rather than just writing a generic paragraph. Tuning: We adjusted the Temperature and Top K settings in the app builder to balance creativity (for suggesting unique careers) with consistency (for providing reliable learning paths). Challenges we ran into Defining the Persona: At first, the AI was too generic. It would just say "Follow your passion." We had to iterate on the System Instructions significantly to force it to ask probing questions (like "Do you prefer working with data or people?") before giving advice. Output Formatting: Getting the AI to switch from "Chat Mode" to "Roadmap Mode" was tricky. We had to create specific triggers in the prompt logic so that once the user agrees on a career path, the AI automatically shifts to generating the structured timeline. Hallucinations: We had to instruct the model to avoid inventing specific URLs for courses (which might break) and instead focus on providing highly accurate search terms and platform recommendations (like "Search for 'Google Data Analytics Certificate' on Coursera") Accomplishments that we're proud of Rapid Prototyping: By using the Gemini App builder, we went from an idea to a working logic model in record time, proving the power of no-code/low-code AI development. The "Human" Feel: We are proud that the assessment feels like a genuine chat with a mentor, not a robotic survey. Context Retention: Successfully leveraging Gemini's long context window to ensure the final roadmap actually reflects the small details the user mentioned at the very start of the chat. What we learned Prompt Engineering is Programming: We learned that in the age of Generative AI, writing a good prompt is just as important as writing good code. The structure of our instructions directly dictated the quality of the app. The Power of System Instructions: We discovered how powerful the "System Instruction" field in Google AI Studio is for locking down the AI's behavior and preventing it from going off-topic. User Anxiety: We learned that users prefer "small steps" over "big goals," which influenced us to tune the AI to break roadmaps down into manageable weekly/monthly tasks. What's next for Career Architect Multimodal Inputs: Using Gemini’s vision capabilities to let users upload a photo of their current resume or a project they built to get instant feedback. Live Job Data: Connecting the app to external tools to fetch real-time salary data for the suggested careers. Mock Interviews: Adding a "Interview Mode" where the AI simulates a job interview for the specific career path it recommended. <div