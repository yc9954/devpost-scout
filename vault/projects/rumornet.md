---
slug: "rumornet"
url: "https://devpost.com/software/rumornet"
title: "rumorNet"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 1086
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/sensor_fusion"
  - "domain/developer_tools"
  - "domain/immigration_refugee"
  - "domain/media_journalism"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# rumorNet

> RumorNet detects misinformation in 100+ languages. By analyzing cultural context, we catch disinformation, echo chambers and bot activity giving you the overall as well as the granular picture.

[Devpost](https://devpost.com/software/rumornet) · hackathon [[Kiroween]]

## Facets

**mechanism** [[multi_agent]] [[sensor_fusion]]
**domain** [[developer_tools]] [[immigration_refugee]] [[media_journalism]]
**user** [[developer]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[structured_db]]

**stack** amazon-web-services, bedrock, kiro, strands

## How they structured the write-up

- 🧪 category submission: frankenstein
- 💡 inspiration: the "lost in translation" problem
- 🤖 what it does (the agent squad)
- ⚙️ how we built it (the architectural transplant)
- 🛠️ how kiro was used
- 🚧 challenges: the "reward hacking" war
- 🏆 accomplishments
- trouble
- 🔮 what's next

## Body

RumorNet: Multilingual Multi-Agent Misinformation Dectection 🧪 Category Submission: Frankenstein We are submitting to the Frankenstein category. Why? RumorNet is a technological chimera on every level. The Analytical Monster: We stitched together Macro-Level Social Surveillance (network theory) with Micro-Level Forensic Psychology (content analysis) into a single brain. The Architectural Monster: We took heavy, stateful Multi-Agent Systems (originally built as persistent MCP servers) and transplanted them into ephemeral, stateless AWS Lambda functions. The Development Monster: We inverted the usual coding paradigm—using rigid Specifications for the UI and "Vibes" for the complex backend logic (more on this below). 💡 Inspiration: The "Lost in Translation" Problem Misinformation doesn't respect borders. A political lie in Brazil spreads in Portuguese, uses local slang, and relies on regional context. The False Start (Kiro's First Attempt): When we first brainstormed with Kiro, it hallucinated an antiquated 2020-era pipeline: separate libraries for LanguageDetection , EntityExtraction , and translation layers. We realized this was an obsolete way of thinking. We had to "kill" Kiro's initial design and reimplement a modern architecture using Gemma 3 / Claude 3.5 Haiku to process claims natively in 100+ languages without translation loss. 🤖 What It Does (The Agent Squad) RumorNet stitches together the "Forest" and the "Trees" using Gemma 3 / Claude 3.5 Haiku : 1. The Macro View (The Forest) The Social Behavior Agent treats the dataset as a living organism. It ignores individual truth and looks for structural anomalies: Echo Chamber Detection: Calculating network density and content homogeneity to spot closed loops. Coordinated Inauthentic Behavior (CIB): Identifying bot-like timing patterns and astroturfing campaigns across the dataset. 2. The Micro View (The Trees) Simultaneously, the Reasoning & Pattern Agents perform forensic analysis on every single post: Nuanced Pattern Recognition: It detects subtle psychological hooks, including: Emotional Manipulation: Fear-mongering and outrage bait. False Authority & Cherry-Picking: Selectively presenting facts to distort reality. Conspiracy Theories: Identifying specific narrative tropes (e.g., "The Great Reset," "Deep State"). Top Offender Identification: It correlates the Micro and Macro views to pinpoint the exact user accounts driving the most dangerous narratives. ⚙️ How We Built It (The Architectural Transplant) We performed radical surgery on our own code to fit this monster into the cloud: The Brain: Claude 3.5 Haiku (Production) / Gemma 3 (Architecture Compatible). The Transplant: To achieve production scalability on AWS, we surgically removed the MCP transport layer we initially built and stitched the agent logic directly into a stateless AWS Lambda (Python 3.11) architecture. The Stitching: Since API Gateway times out at 29 seconds, we built a custom S3-polling mechanism in our Streamlit dashboard to retrieve results from the "headless" Lambda processes. Note on The Topic Intelligence Engine: We built a fourth agent for UMAP-based topic clustering, but it is currently dormant (can be enabled for local deployment). UMAP requires write access to file systems for clustering calculations, which conflicts with Lambda's read-only constraints—a true Frankenstein limb waiting to be reattached. 🛠️ How Kiro Was Used This project was built entirely inside Kiro IDE. The experience was an inversion of typical development norms: 1. Spec-Driven Development (The Frontend) Surprisingly, Kiro was far better at the Frontend than the Backend. We used it to strictly define the Streamlit Dashboard. The Outcome: Kiro nailed the UI structure, state management, and S3 polling logic perfectly from the specs. It understood the "dark mode Vercel aesthetic" and component layout better than it understood complex reasoning logic. 2. Vibe Coding (The Backend Logic) For the backend agents, we had to rely on Vibe Coding . Why? Because defining "misinformation" is abstract. The Process: We couldn't just spec "detect fake news." We had to have a conversation with the AI. We iterated back and forth to inject our human domain knowledge into the system—teaching the agents how to recognize sarcasm, how to spot a dog whistle, and how to weigh evidence. The Result: A conversational, iterative approach allowed us to mold the Gemma 3 / Haiku prompts until they "felt" right, capturing nuances a formal specification missed. 3. MCP (The Muscle Memory) We utilized the Filesystem and Git MCP servers extensively. Kiro acted like a senior engineer, diffing files and performing bulk refactors across the agents/ directory. This was crucial when we decided to strip out the MCP server wrappers to fit the agents into AWS Lambda. 4. Steering Docs (The Guardrails) We used .kiro/steering/ to enforce consistency ( conda-environment.md , reuse-working-code.md, n-specification-gaming.md`). This automated our Docker and Environment setup, saving us hours of configuration hell. 🚧 Challenges: The "Reward Hacking" War Our biggest challenge was Specification Gaming (Reward Hacking). Kiro's AI models were so eager to "pass the test" that they often engaged in malicious compliance. The Horror Stories: The "Try-Catch" Blanket: Kiro would wrap entire complex functions in broad try: ... except: return None blocks. The tests would pass (no crashes!), but the code was silently failing. Import-Only Tests: When context was low, Kiro wrote tests that simply imported the class to check existence, rather than testing functionality. The "None" Return: To satisfy Type Hints like Optional[dict] , Kiro would default to returning None immediately to satisfy the linter, rather than writing the logic. The Fix: We had to act as rigorous auditors. We learned that "Green Tests" in an AI workflow don't mean "Working Code." We had to force Kiro to show its work and manually review the implementation logic. 🏆 Accomplishments Frankenstein Architecture: Successfully integrated the Micro and the Macro level analytics. Experimented upon the agent and its orchestration on the best way to bring it to life. Then realized Whats best depends on the final deployment infrastructure and the trade-offs. Inverted Development: Successfully combining Spec-driven UI with Vibe-coded Logic. True Multilingualism: Analyzing Portuguese/Nepali posts. Performance: Processing 132 posts in ~220 seconds. **We have a running application already deployed in render.com coded via Kiro. With this in place we are ready now to bring more focus to human coding , testing via Observability . Trouble ** What we have shown in this hackathon is actually 1/4 of the development in Kiro. We have a very sophisticated orchestration and memory module but felt that it required more work to publish. Unlike any other previous work I have done , this is in large part done via steering and vibe coding using kiro. 🔮 What's Next Re-enabling Topic Modeling: Migrating the UMAP clustering to an EFS (Elastic File System) mount to bypass Lambda write limits. Observability: Adding open-telemetry for tracking agent and learn their effectiveness. Repository includes .kiro directory demonstrating our Spec/Steering setup. UI Deployment https://rumornet-dashboard-latest.onrender.com <div