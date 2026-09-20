---
slug: "wiggins-ai-detective-team"
url: "https://devpost.com/software/wiggins-ai-detective-team"
title: "Wiggins － AI Detective Team"
hackathon: "Global AI Hackathon Series with Qwen Cloud "
organization: "Alibaba Cloud"
winner: true
words: 1161
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/labor_employment"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Wiggins － AI Detective Team

> Five AI detectives investigate motive, means & opportunity in parallel, cross-examine each other's findings, and self-correct. Multi-agent reasoning you can watch, on Qwen Cloud.

[Devpost](https://devpost.com/software/wiggins-ai-detective-team) · hackathon [[Global AI Hackathon Series with Qwen Cloud]]

## Facets

**mechanism** [[deterministic_policy]] [[multi_agent]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[labor_employment]]
  <sub>weak: social_worker</sub>
**substrate** [[code_repository]] [[structured_db]]

**stack** alibaba-cloud-ecs, docker, fastapi, langchain, langfuse, langgraph, nginx, pydantic, python, qwen-cloud-(alibaba-dashscope), react, server-sent-events, typescript, uv

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for wiggins

## Body

Data Setup: Enter details manually or load 3 default presets. Case Intake: Manually input the case narrative and suspects. Analyzing: Multi-agent parallel reasoning in progress. Solved: Displays final verdict and explainable evidence breakdown. Wiggins — AI Detective Team Inspiration Most LLMs answer “Who is the murderer?” with a conclusion but no auditable investigative trail. Users cannot verify whether the answer is grounded in complete evidence. Wiggins turns that black-box judgment into an investigation that can be observed, challenged, and traced. Wiggins achieved 94.6% accuracy on a clean 92-case test set—9 more correct answers than a naive single-call baseline—while preserving the full reasoning trail behind every answer. We modeled the system after the division of labor in real investigations, assigning distinct reasoning tasks to specialized agents. The core ideas are simple: An answer alone is not enough; users should see how it was formed. Reasoning quality depends on process design as well as model capability. Explainability makes every conclusion traceable, reviewable, and correctable. We use the murder mystery subset of MuSR (Multistep Soft Reasoning), available from the official public repository . What it does Wiggins takes a case narrative, a suspect list, and a question, then deploys five specialized agents: Three parallel investigators build independent evidence chains for motive, means, and opportunity. One forensic verifier checks whether each claim is supported by the case and sends evidence gaps back to the appropriate investigator. One lead detective combines the three dimensions, identifies the culprit, and explains the decision. The entire process streams live to an Evidence Board: The center displays evidence cards and red-string connections as agents collaborate. The right side shows a suspect × motive/means/opportunity strength matrix. The investigation clearly surfaces supported claims, evidence gaps, reinvestigations, and changes in judgment. The answer is no longer a single sentence. It becomes a complete investigative record that users can review. Rather than asking one model to “think harder” within a single prompt, Wiggins assigns investigation, verification, and synthesis to separate agents. Evidence chains are built independently, cross-checked, and selectively reinvestigated when gaps appear. This division of labor produces not only an answer, but also a mechanism for validating it. How we built it We developed Wiggins along two tracks: productizing the frontend and backend while continuously improving the reasoning core. Frontend and interaction design: The React + TypeScript frontend receives continuous start/step/final events over SSE and translates multi-agent collaboration into a readable visual language for the Evidence Board. API and contracts: FastAPI provides the streaming endpoint, while structured schemas define a stable boundary between the frontend and backend so the interface and reasoning core can evolve independently. Reasoning orchestration: LangGraph implements a “parallel investigation → verification → synthesis” pipeline in which every role focuses on a specialized task: Coordinator-free parallel investigation: Three investigators analyze motive, means, and opportunity simultaneously before sending their findings to the forensic verifier. Removing the unnecessary LLM router reduced the base number of calls per case from 10 to 5 while also lowering latency. Dimension-level evidence verification: The forensic verifier checks motive, means, and opportunity independently against the case evidence instead of merely asking whether the three reports agree. This helps prevent unsupported conclusions from passing simply because they form a coherent narrative. Targeted parallel reinvestigation: A failed dimension is returned to the corresponding investigator with specific feedback. Multiple dimensions can be reinvestigated in parallel without rerunning the entire pipeline, and a hard retry limit guarantees that every case reaches a final decision. Reasoning rules: Wiggins uses three rules to improve the precision of evidence assessment: Three-tier strength labels: Motive, means, and opportunity are classified as strong, weak, or none, distinguishing explicit textual evidence, reasonable inference, and missing support. Loud-decoy defense: Dramatic but crime-irrelevant traits—such as aliases, unusual hobbies, or suspicious habits—are excluded from the evidence. The culprit must have motive, means, and opportunity. Temporal discipline: The system strictly separates presence at the time of the murder from arrival after the crime. Only evidence matching the crime window and location counts as opportunity. Models and observability: Wiggins uses Qwen Cloud with thinking and structured output, while Langfuse and a batch evaluation pipeline record every experiment. Deployment: Docker Compose deploys the system to Alibaba Cloud ECS, with nginx reverse-proxying FastAPI and supporting stable SSE streaming. Challenges we ran into The core challenge was making the multi-agent system perform reliably across accuracy, readability, and evaluation. Multi-agent visualization complexity: Updating the timeline, evidence cards, and matrix simultaneously made it difficult to focus. We introduced a visual hierarchy that emphasizes the central evidence flow during the investigation and the matrix at the final decision. Reinvestigation requires precise feedback: We structured every retry around “which dimension, which suspect, and which evidence gap,” giving the investigator a concrete correction target. Evaluation requires stable measurement: Because thinking mode is nondeterministic, we use repeated runs, batch evaluation, and dataset audits to separate model performance from run-to-run variance and annotation issues. Architectural contribution requires a fair comparison: We give the single-call baseline the same reasoning rules, then track rescues, regressions, and additional cost to isolate the practical gain from multi-agent orchestration. Accomplishments that we're proud of 94.6% accuracy: Wiggins answered 87 of 92 cases correctly on the clean test set, solving 9 more cases than the naive single-call baseline and surpassing a much larger model. No regression on stable cases: Wiggins preserved every case that all five previous versions had consistently solved. A traceable alternative to black-box answers: Every reasoning step can be inspected, challenged, and corrected. Actionable rules derived from observable reasoning: The system helped us identify three-tier strength labels, loud-decoy defense, and temporal discipline as effective reasoning strategies. Best performance on the hard-case set: On 20 difficult cases, the naive single-call baseline solved 10 , the same baseline with reasoning rules solved 15 , and Wiggins solved 16 by combining those rules with specialized roles and independent verification. What we learned Explainability directly accelerates iteration. When we can see exactly where reasoning fails, we can locate and fix the problem faster. Reasoning rules and architecture reinforce each other. Rules improve judgment, while agent specialization allows those rules to be applied independently and cross-checked. Fair comparisons reveal where gains come from. Controlling prompt content lets us separate the contribution of reasoning rules from the effect of specialized roles and independent verification. Reliable evaluation starts with measurement. Dataset audits, repeated runs, and batch tracking make every reported result traceable and more robust. Task complexity is the next axis to test. We expect more suspects, state changes, and conflicting evidence to increase the value of specialization and verification. What's next for Wiggins Take on harder cases: Expand to 3–4 or more suspects, with additional red herrings and cross-paragraph evidence conflicts. Strengthen the final-decision gate: Reduce the chance that persuasive storytelling overrides the evidence. Build a more robust evaluation protocol: Use same-day comparisons, repeated runs, and stratified reporting of variance ranges. Continue improving observability: Let users inspect not only the answer, but also the strength of the evidence behind it. <div