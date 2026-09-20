---
slug: "the-bunny-ear-adventure"
url: "https://devpost.com/software/the-bunny-ear-adventure"
title: "Logic Lift"
hackathon: "Gemini 3 Hackathon"
organization: "Google"
winner: true
words: 1026
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# Logic Lift

> Logic Lift uses Gemini 3 to perform 'Logic Archaeology'—autonomously recovering critical financial business logic from legacy COBOL and verifying it into cloud-native Python with 100% parity.

[Devpost](https://devpost.com/software/the-bunny-ear-adventure) · hackathon [[Gemini 3 Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[video_visual]]

**stack** cobol, gemini, google, google-cloud, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- multi-modal reasoning & vibe engineering
- scalability & investment potential
- what i learned
- what's next for logic lift

## Body

Logo (Ouroboros) Logic Lift Logo & Brand Name (Light Mode) GIF Logic Lift Logo & Brand Name (Animated) GIF dark mode/light mode toggle Logic Lift Logo & Brand Name (Dark Mode) Continuous Deployment (GCP) Landing Page (Light Mode) Landing Page (Dark Mode) Logic Lift Mainframe to Modern Logic Recovery, powered by Gemini 3 Inspiration While navigating the job market, I noticed a surprising surge in advertisements for COBOL —a language created in 1959. Research revealed a critical "COBOL Dilemma": over 95% of ATM swipes and 43% of banking systems still run on these legacy mainframes, yet the experts who maintain them are retiring. Younger developers are hesitant to learn procedural languages, creating a "Black Box" risk for global infrastructure. This is why I was inspired to build a tool that doesn't just "translate" decades-old legacy code, but performs Logic Archaeology to recover the underlying business intelligence for the next generation of engineers. What it does Logic Lift is an autonomous modernization platform that deconstructs monolithic COBOL systems and reconstructs them into future-proof, cloud-native Python. Logic Archaeology: Identifies and extracts buried business rules and PIC-clause data mappings. Autonomous Verification: Generates parity test suites (pytest) to prove the new logic behaves identically to the legacy system. Bulk Export: Aggregates processed modules into a single, deployable system queue file, eliminating manual copy-paste friction. System Blueprint: Maps the global topology of the legacy codebase into a modern distributed architecture. How I Built it Logic Lift was built to be free, accessible, and cloud-agnostic . Core Engine: Initially built in Google AI Studio , leveraging Gemini 3’s massive context window for full-repository reasoning and deconstruction. Local Refinement: After the initial build, the project was pulled into a local Google Antigravity environment to execute comprehensive tests and apply bespoke styling and branding assets. Frontend Stack: Developed with React, TypeScript, and Tailwind CSS for a premium, high-fidelity experience. Intelligence: Utilizes Gemini 3 Pro for research-backed modernization and search-grounded technical documentation. Secure by Design: While hosted in the accessible Google AI Studio environment, Logic Lift is architected with enterprise-grade security in mind, providing a clear pathway for organizations to run these reasoning cycles within their own private Google Cloud VPCs. Challenges I ran into The most significant hurdle was the "83% Stall" : a scenario where the migration pipeline would hang if a specific code chunk encountered a logical error. I had to pivot from a linear process to a Resilient Pipeline architecture, implementing skip/next logic and a robust state machine that ensures 100% completion even if individual modules encounter faults. We also navigated the complexity of mapping procedural COBOL records to modern Python classes without losing data integrity. The One-Way Sync Predicament: Beyond the code logic, I encountered a unique workflow hurdle while moving between Google AI Studio and GitHub . While AI Studio is an incredible engine for initial deployment and pushing code, it currently lacks a mechanism to 'pull' changes back in from a remote repository. This created a 'One-Way Bridge' scenario; I had to meticulously manage external refinements made in Antigravity to ensure the live environment in AI Studio remained the 'Single Source of Truth' for the modernization kernel. This experience forced me to be highly disciplined with my version control strategy to preserve the integrity of the live prototype. Accomplishments that I'm proud of True Parity Validation: Implementing a virtualized execution loop that simulates test results to provide a "Certainty Score" for every migrated module. Bespoke Branding & UX: The Ouroboros Logo: Created in Canva, the logo features the ancient symbol of a serpent eating its own tail—representing renewal and the endless cycle of modernization—while serving as a subtle nod to Python’s snake imagery. Strategic Color Theory: The palette uses Deep Purple (representing AI and prosperity) and Teal/Blue (establishing technological trust), wrapped in a fully responsive Light/Dark mode interface. Neural Correction Loop (Action Era): Beyond translation, Logic Lift implements an autonomous verification cycle. Using Pyodide , the system executes the modernized Python code in a browser-based sandbox. If a test fails, the agent autonomously analyzes the traceback and self-corrects the implementation logic without human intervention. Impact Audit & ROI Dashboard: Translates technical code transformations into strategic business value, tracking Architecture Enrichment (converting legacy procedural lines into type-safe, high-fidelity logic) and Security Posture (Zero Trust/IAM baselines). High-Fidelity UX: Creating a "System Stream" terminal and "Archaeology Report" view that makes the modernization process transparent and engaging. Cloud-Agnostic Output: Ensuring the generated Python code is not locked into a specific vendor, but ready for any modern cloud environment. Multi-Modal Reasoning & Vibe Engineering Logic Lift is built for the Gemini 3 Action Era . It leverages: Recursive Thought Signatures: The agent doesn't just output code; it reasons through execution failures in a closed-loop system, mimicking the behavior of a senior developer. Browser-Side Verification Artifacts: High-fidelity execution logs powered by browser-integrated Python runtimes that prove the integrity of the modernized logic before deployment. Scalability & Investment Potential Logic Lift addresses a multi-billion dollar technical debt crisis. For investors, the platform offers three clear axes of expansion: Horizontal Scaling: Replicating the "Logic Archaeology" kernel to deconstruct other "zombie languages" like PL/I, RPG, and Fortran . Vertical Integration: Transitioning from "simulated verification" to live, air-gapped VPC execution environments on GCP. Market Reach: Transforming from an MVP into a full-scale Migration IDE that facilitates secure, end-to-end legacy-to-cloud transitions for world-class financial institutions. What I learned Building Logic Lift taught us that LLMs like Gemini 3 are no longer just "chatbots"—they are System Architects . We learned the importance of "controlled" UI components in complex AI workflows and how to leverage search grounding to provide developers with the "Why" behind a modernization choice, not just the "How." What's next for Logic Lift To move Logic Lift from a powerful MVP to a production-grade tool, the roadmap includes: The Sandbox: Integrating a secure GCP Cloud Run backend to execute and verify the generated Python code in real-time. Zombie Language Support: Expanding the deconstruction kernel to handle other legacy languages like PL/I, RPG, and Fortran . Enterprise Integration: Developing a "Migration IDE" plugin that connects directly to enterprise GitHub repositories to automate Pull Requests as logic is recovered. <div