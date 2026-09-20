---
slug: "sage-yvlpqb"
url: "https://devpost.com/software/sage-yvlpqb"
title: "Sage"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 1335
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/transportation"
  - "user/developer"
  - "user/educator_student"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/geospatial"
---

# Sage

> Grounded AI tutoring, built on your curriculum, Interactive Learning

[Devpost](https://devpost.com/software/sage-yvlpqb) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[on_device_local]] [[retrieval_grounding]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[developer_tools]] [[education]] [[transportation]]
**user** [[developer]] [[educator_student]]
**substrate** [[code_repository]] [[document_pdf]] [[geospatial]]

**stack** cloudinary, cognition, elevenlabs, fastapi, fetch, fetchai, groq, katex, mermaid, nextjs, python, railway, react, react-three-fiber

## How they structured the write-up

- inspiration
- problem
- solution
- what it does (teacher workflow)
- what it does (student workflow)
- interactive learning layer
- research layer
- voice + on-device support
- how we built it
- apis / infra used
- challenges
- accomplishments we’re proud of
- what we learned
- what’s next
- social

## Body

Interactive 3D Simulations Curated Course Curriculums SAGE Inspiration Sage came from a problem we kept seeing in real learning environments: teachers and students are drifting into separate systems. Teachers are stuck managing large classes, rigid pacing, and administrative load, while students increasingly use AI outside class because they feel it explains things faster and more personally. The result is a broken loop: teachers cannot see how students are actually learning, and students cannot reliably map AI help back to their curriculum. We built Sage to reconnect those loops in one platform. Instead of forcing teachers to become prompt engineers or forcing students to stitch together five disconnected apps, Sage is designed as one workflow where curriculum creation, tutoring, exploration, and assessment feed each other. Problem The current market has two extremes that both fail in practice. On one side, generic AI chatbots are good at fluency but weak on grounded instructional consistency, so students can get explanations that sound right but are disconnected from their course sequence. On the other side, many educator tools focus on productivity (lesson generation, worksheets, admin workflows) but stop short of building a truly adaptive student learning experience. This creates tool fragmentation: students jump from chatbot to video to notes to quiz to coding site, while teachers have no coherent view of where understanding breaks down. Our view is that education AI fails when it treats teacher tooling and student learning as separate products. Solution Sage is a two-sided system with a shared knowledge and interaction layer. The teacher side is about creating and publishing high-quality interactive curriculum quickly. The student side is about learning in an adaptive way through grounded tutoring and multimodal explanations. The key is the bridge between the two: content generated and improved by educators is what powers tutoring quality, and student interaction signals are what should eventually inform curriculum improvements. That architecture lets Sage function both as a curriculum engine and as an active tutor, rather than a static content system or a detached chatbot. What It Does (Teacher Workflow) The teacher/creator workflow is structured as a staged pipeline so quality is controllable, not accidental. A creator starts with topic shaping and outline generation, then moves through lesson drafting, web-based enrichment, and quality review before publishing. This makes course creation fast while preserving human oversight. In the app today, this flow exists as concrete creation and review surfaces rather than a single “generate everything” button. The intent is to make curriculum production iterative: creators can inspect structure, patch weak sections, and then publish learning paths students can immediately consume inside the same system. What It Does (Student Workflow) The student experience centers on guided learning paths plus live tutoring support. Students can navigate course lessons and engage with a tutor that supports multiple teaching modes: Default, ELI5, Analogy, Code-first, and Deep Dive. Explanation style can match learner preference in the moment. This matters because students do not struggle in the same way: some need intuition first, others need formal detail, and others need implementation examples. SAGE also includes quiz and exploration flows so learning is not just passive reading or passive chat. The structure is designed to support students who are in classrooms and students learning independently. Interactive Learning Layer Sage does not limit instruction to plain text. The platform can render math via LaTeX, visual structure via Mermaid, executable code via sandboxed blocks, and inline 3D simulations for topics where spatial/physical reasoning helps. This multimodal layer is one of the core differentiators: instead of asking learners to leave the tutoring context to open separate tools, the explanation medium can be chosen inside the same flow. In practical terms, this reduces context switching and increases the chance that a learner stays engaged long enough to reach understanding. Research Layer Sage includes a Deep Research surface for source discovery and deeper topic investigation. Users can run research queries and review ranked results with summaries in-app, which supports both lesson-building and advanced self-study. For educators, this helps tighten content quality and source grounding during curriculum refinement. For students, it provides a structured way to go beyond lesson-level explanations without fully leaving the learning environment. The long-term role of this layer is to make source-backed learning a first-class behavior, not an afterthought. Voice + On-Device Support Voice is integrated to make tutoring interaction more natural and accessible, especially for users who think out loud or prefer conversational pacing. Sage uses ElevenLabs for voice session support and intent-driven actions. The platform also includes an on-device Pocket tutor path with WebLLM, which shows a direction toward more local, low-latency study experiences and reduced dependence on constant cloud calls for every interaction. This is important both for accessibility and for practical use cases where users want lightweight study sessions without heavy setup. How We Built It Sage is built as a modern full-stack web system. The frontend uses Next.js App Router with React and TypeScript, styled with Tailwind and custom UI patterns for learning-heavy interactions. Interactive educational rendering is powered by KaTeX, Mermaid, and React Three Fiber. The backend uses FastAPI with SQLModel and SQLite, with endpoints for tutoring, course creation, research, assessments, and media/document workflows. The system is designed around composable routes and services so product surfaces (create, learn, research, docs, pocket, etc.) can evolve without rewriting the core application. APIs / Infra Used The codebase includes integrations across inference, media, research, and communication tooling. Groq is used in LLM-related paths, ElevenLabs powers voice, Tavily supports research search, and Cloudinary powers major media/document upload and delivery flows. Additional integrations include Hunter, Apollo, SendGrid, and OpenAlex in outreach/research-oriented plumbing. The project also contains hackathon-track integrations for Fetch.ai and Cognition, plus on-device WebLLM support. Deployment is split across Vercel (frontend) and Railway (backend), reflecting real-world multi-service delivery constraints. Challenges The hardest engineering challenge was not any one feature, but making the full system coherent under hackathon constraints. Grounding quality and response reliability require careful retrieval/prompt behavior, especially when users ask beyond strict lesson boundaries. Multimodal rendering introduces complexity in deciding when to use text vs diagram vs code vs simulation. The creator pipeline required stabilization and sanitization to reduce generation failure modes before publish. Deployment introduced another layer of complexity: cross-service env management, domain routing, and runtime compatibility issues can easily break demos unless treated as first-class engineering work. Accomplishments We’re Proud Of We shipped a real two-sided education platform with meaningful depth on both sides, not a single-surface chatbot prototype. The product includes creator pipeline flow, grounded tutoring with mode switching, multimodal outputs, interactive simulations, voice support, research integration, and assessment/document systems inside one application. We are especially proud that the architecture supports both educator and independent learner use cases, because most products optimize for one and hand-wave the other. Even where parts are still evolving, the core platform direction is working and demoable. What We Learned The biggest lesson is that education AI quality is systems work, not just model work. Better prompts alone do not solve curriculum quality, workflow friction, or learner retention. The product wins when content creation quality, learning UX, grounding discipline, and adaptation signals are connected. We also learned that “adaptive learning” must be explicit in instrumentation and feedback loops; it does not emerge automatically from having chat history. Finally, building for both teachers and students in one platform is harder, but it produces a more defensible and more useful product. What’s Next The next phase is deepening adaptation and feedback loops. On the learner side, that means stronger use of behavioral signals (performance patterns, concept difficulty trajectories, interaction history) to improve personalized pathways. On the educator side, that means clearer analytics about where students stall, which lessons underperform, and which resources actually move outcomes. We also plan to continue hardening reliability and expanding interactive instructional mediums so SAGE becomes not just a smart tutor layer, but a complete adaptive learning operating system for classrooms and independent learners. Social If you would like to keep in touch with the project follow the Instagram : @sage_ucla <div