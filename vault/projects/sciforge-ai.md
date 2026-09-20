---
slug: "sciforge-ai"
url: "https://devpost.com/software/sciforge-ai"
title: "SciForge AI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 1214
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "mechanism/vision_ocr"
  - "domain/accessibility"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/scientific_research"
  - "user/developer"
  - "user/educator_student"
  - "user/legal_professional"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# SciForge AI

> An autonomous AI agent that adapts in real‑time to each student's mastery, tracks their progress across 1,200+ STEM concepts, and makes personalized decisions to close learning gaps – instantly.

[Devpost](https://devpost.com/software/sciforge-ai) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[sensor_fusion]] [[simulation_digital_twin]] [[structural_withholding]] [[vision_ocr]]
**domain** [[accessibility]] [[developer_tools]] [[education]] [[scientific_research]]
**user** [[developer]] [[educator_student]] [[legal_professional]] [[researcher]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[video_visual]]

**stack** groq, local-storage, next.js, node.js, opendyslexic, tailwind-css, vercel

## How they structured the write-up

- the ai stem workspace that catches logic errors before the ink dries.
- inspiration
- the problem
- the solution
- hero demo moment
- key features
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sciforge ai
- built with
- final closing

## Body

SciForge AI Master Workspace Thumbnail SciForge AI: Landing Portal Entrance Cognitive Entrance: The Launch Pad Core Intelligence Console: Real-time STEM Analysis Scribble Analysis Lab: Forensic Vector-Diff Parser Quantum Research Engine: Symbolic Math & Precision Validation Concept Dependency Map: Topological Curriculum Solver Asset Ledger: Automated Milestone History Research Portfolio: Secure AES-256 Telemetry Vault Platform Configuration: Accessibility & Visual Customization SciForge AI High Level Architecture Novus.ai integrated — real-time product analytics & user insights SciForge AI The AI STEM workspace that catches logic errors before the ink dries. 🔗 View the Official SciForge AI 2026 Project Presentation (PDF) (Note to Judges: This presentation outlines our engineering architecture, roadmap, and impact analysis. We highly recommend viewing this deck alongside our live deployment.) Inspiration STEM students don't drop out because the math is too hard; they drop out because the feedback is too slow. Traditional AI tools act like sophisticated search engines—text-bound, conversational, and completely blind to how scientists actually think: on scratchpads, through spatial equations, and across visual topologies. We realized that to truly accelerate technical learning, we didn't need another chatbot. We needed a live environment that could validate logic the moment it's generated. The Problem Modern STEM education is trapped in a high-latency feedback loop. A student spends two hours deriving a complex multi-step equation on paper, making a silent algebraic error on step two. They remain completely unaware of this mistake until a professor grades it a week later. By then, the critical learning window has closed. Existing conversational AIs fail here because they cannot parse spatial, handwritten reasoning, turning rigorous problem-solving into passive, frustrating rote memorization. The Solution SciForge AI is a telemetry-first cognitive workspace that closes this critical feedback gap. Operating as a live compiler for human thought, it continuously validates logical reasoning, interprets structured problem inputs, and maps curriculum mastery. SciForge AI shifts technical study from passive guessing to verified mastery—catching structural mistakes the moment they happen. SciForge AI is not a chatbot – it is a decision‑making agent that analyzes performance, detects missing prerequisites, and automatically updates the student's learning roadmap, ensuring they never repeat the same mistake. Hero Demo Moment This is the frictionless telemetry workflow that defines SciForge AI: Upload: A student submits a typed equation, a structured problem set, or an image of a sketch into the Scribble Analysis Lab . Analyze & Reason: Leveraging the high-throughput logical reasoning of Llama 3.3 (70B) via Groq , the system parses the submitted input, extracts mathematical and structural context, and initiates a rigorous logic check. (Note: Full computer-vision parsing for handwritten diagrams is actively on our roadmap—see architecture deck for details.) Isolate: Instead of just outputting a generic answer, the AI acts forensically—pinpointing the exact step where the logic breaks (e.g., an inverted vector or a dropped variable) with targeted audio/visual coaching. Adapt: The agent decides – based on the error pattern – which foundational concept is missing. It then automatically updates the student’s personalized roadmap, re‑orders the curriculum, and suggests targeted exercises, all without the student having to ask. Key Features Scribble Analysis Lab: A dedicated workspace for uploading problem sketches and structured inputs. The system applies advanced logical deduction to validate structural reasoning, with a planned upgrade to full computer-vision vector-diff parsing for hand-drawn diagrams (already detailed in our architectural roadmap). Sub-42ms Cognitive Mentor: High-throughput streaming guidance powered by Groq and Llama 3.3, delivering instant pedagogical support without the heavy latency of traditional LLM inference. Concept Dependency Graph: Concept Dependency Graph (The Agent's Brain): A live, 1,200+ node curriculum graph that tracks mastery in real time and automatically replans the student's learning path based on their performance – ensuring no concept is left behind. Zero-Click Research Ledger: An automated, persistent local vault that instantly captures queries, generated quizzes, and active study sessions with zero manual saving required. Engineered for Equity: Native integration of OpenDyslexic typography and specialized high-contrast logic environments designed specifically to minimize cognitive load and remove learning barriers during deep focus. How We Built It We engineered a high-throughput, decoupled architecture optimized for absolute minimal latency: Intelligence Layer: Deployed a high-performance backend using Groq's API running Llama 3.3 (70B) to achieve near-instant inference and structured Markdown generation. Math & Logic Pipeline: Architected a modular backend that leverages the LLM for contextual parsing, with a clean API layer explicitly designed to integrate symbolic math engines ( SymPy and JAX ) for raw computational verification in our next iteration. Data & Analytics: Integrated local storage for the persistent portfolio ledger and deployed Novus by Pendo to track real-user telemetry, session replays, and drop-off points. Frontend UI: Built a highly responsive, state-managed interface using Next.js and Tailwind CSS . Challenges We Ran Into Our hardest technical challenge was reconciling the high-precision requirements of mathematical validation with the strict ultra-low latency constraints of a streaming UI. Standard LLMs hallucinate math, and strict mathematical solvers are too slow for a fluid chat interface. We solved this by heavily optimizing our prompt engineering to generate clean, structured educational artifacts instantly, while strictly decoupling the architecture so heavy computation can be offloaded to dedicated symbolic solvers in the future. Additionally, true visual parsing of unstructured handwritten math requires specialized computer vision—which we have strategically placed on our roadmap to ensure we build it right, not fast. Accomplishments That We're Proud Of True Zero-Mock Architecture: Built entirely as a solo developer, every single component is live. Every node in the concept graph (spanning 1,284 dynamic points), every generated quiz, and every ledger entry is driven by real, active LLM streaming inference and telemetry tracking. The "Single Pane of Glass" Interface: Successfully condensed a high-throughput, multi-module technical workspace into a single intuitive pane of glass without compromising on ultra-low latency execution. What We Learned Feedback Latency is the Real Bottleneck: Information is abundant; immediate correction is rare. By prioritizing instantaneous error correction over raw search retrieval, mastery accelerates dramatically. Accessibility Controls Deep Focus: Features like the OpenDyslexic font and High-Contrast logic modes are not superficial add-ons. For neurodivergent students, reducing visual and typographical friction fundamentally changes how long they can maintain deep-work cognitive focus during rigorous STEM study. We learned that a true adaptive agent doesn't just answer questions – it remembers what the student struggles with and acts proactively to prevent the same error from recurring. What's Next for SciForge AI We are currently expanding the Concept Dependency Map to integrate live laboratory simulation data, allowing students to test scientific hypotheses virtually. We are also actively developing the next iteration of the Scribble Analysis Lab to support full computer vision vector-diff parsing and 3D geometric modeling—turning physical 2D sketches into interactive digital objects and closing the loop on handwritten input validation. We are actively building autonomous intervention triggers – where the agent will suggest a mini‑lesson or a new practice set before the student even realizes they need it. Built With LLM / Inference: Groq API, Llama 3.3 (70B) Frontend: Next.js, React, Tailwind CSS Backend: Node.js, Local Storage API Analytics: Novus by Pendo Deployment: Vercel Final Closing We aren't building a better chatbot. We are building the foundational operating system for the next generation of engineers—where failure is caught instantly, logic is verified dynamically, and learning moves at the speed of thought. For any Hackathon information/inquiry about the project, please contact: mahjabeenismail5@gmail.com <div