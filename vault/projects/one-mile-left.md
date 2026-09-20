---
slug: "one-mile-left"
url: "https://devpost.com/software/one-mile-left"
title: "One Mile Left"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 733
team_size: 1
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "substrate/financial_record"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# One Mile Left

> Projects fail not from execution, but unclear planning. Our AI turns goals into clear milestones, highlights risks early, and delivers actionable visual plans.

[Devpost](https://devpost.com/software/one-mile-left) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]]
**substrate** [[financial_record]] [[structured_db]] [[web_dom]]

**stack** django, openai, python, supabase

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for one mile left

## Body

Inspiration Most projects fail not because of execution, but because planning is unclear. We wanted to help teams see their goals clearly and avoid risks early. What it does One Mile Left transforms high-level ambitions into structured, executable plans. It automatically breaks down complex goals into realistic, dependency-aware milestones, ensuring that teams move forward with clarity rather than guesswork. The system proactively surfaces potential risks before they escalate, enabling teams to mitigate issues early instead of reacting too late. Through an intuitive and visual roadmap interface, users can clearly understand task relationships, progress, and responsibilities. Additionally, our AI-powered scheduling engine intelligently distributes milestones across a timeline, generating a practical execution calendar that aligns planning with real-world constraints. How we built it The platform is built using the Django framework for backend development, providing a robust and scalable server-side architecture. We integrate large language models through the OpenRouter API to power intelligent milestone decomposition and risk analysis. Supabase is used as our database layer, ensuring reliable data persistence and real-time capabilities. The frontend is developed with HTML, CSS, and JavaScript, delivering a responsive and interactive user experience. Challenges we ran into One of the biggest challenges was ensuring that AI-generated milestone structures were both logically consistent and practically executable. Large language models can produce plausible outputs, but not always structurally valid ones. We had to design validation layers to prevent circular dependencies, incomplete breakdowns, and unrealistic sequencing. Another major challenge was integrating real-time AI responses with a responsive frontend. Since LLM calls introduce latency, we optimized backend handling in Django and implemented asynchronous processing to maintain a smooth user experience. We also faced difficulties in balancing flexibility and control. While we wanted users to freely adjust AI-generated plans, we needed safeguards to preserve structural integrity. This required careful separation between AI reasoning, backend validation, and frontend visualization logic. Accomplishments that we're proud of One of our biggest achievements is designing an AI-powered milestone decomposition engine that can transform vague objectives into structured, executable plans. We built validation mechanisms to ensure that AI-generated dependencies are coherent and logically sound, reducing the risk of structural errors. We are also proud of creating a smooth integration between Django, OpenRouter, and Supabase, enabling real-time AI-assisted planning with reliable data persistence. Most importantly, we turned complex AI reasoning into a clear and interactive visual experience that users can confidently work with. What we learned Throughout this project, we gained a deeper understanding of the gap between AI generation and production-level reliability. While large language models can produce impressive outputs, ensuring structural correctness, dependency validity, and consistency requires additional validation logic and system safeguards. We learned that building AI-powered systems is not just about prompting models effectively, but about designing control layers that verify, sanitize, and transform model outputs into deterministic, executable structures. On the engineering side, we strengthened our understanding of scalable backend architecture using Django, API orchestration with OpenRouter, and reliable data persistence with Supabase. We also learned how critical state management and transactional integrity are when AI-generated data directly impacts database structure. Most importantly, we realized that AI is most powerful when it augments human planning rather than replaces it. Designing tools that maintain user control while leveraging AI automation was one of the most valuable lessons of this project. What's next for One Mile Left Due to time constraints, several advanced features remain on our roadmap. One of our primary next steps is to develop an adaptive plan-restructuring engine. In real-world projects, plans rarely remain static. When goals shift or constraints change, teams often need to rebuild their roadmap from scratch, resulting in duplicated effort and wasted progress. We aim to design an intelligent restructuring system that can minimally modify an existing milestone graph, preserving completed work while recalculating only the necessary branches. Technically, this involves building a constraint-aware optimization layer that analyzes dependency structures and performs incremental graph updates instead of full regeneration. The objective is to reduce disruption while maintaining logical consistency across the project structure. Beyond restructuring, we plan to: -Introduce predictive timeline adjustments based on milestone completion velocity -Enhance AI risk modeling with dynamic probability updates -Implement collaborative editing with real-time synchronization -Develop performance analytics that correlate milestone patterns with project outcomes Our long-term vision is to evolve One Mile Left from a planning assistant into an intelligent project co-pilot — one that continuously adapts, optimizes, and learns alongside its users. <div