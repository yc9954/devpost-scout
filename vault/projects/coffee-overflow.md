---
slug: "coffee-overflow"
url: "https://devpost.com/software/coffee-overflow"
title: "TrustIssues.AI"
hackathon: "HackUTD 2025: Lost in the Pages"
organization: "hackutd"
winner: true
words: 657
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/human_in_the_loop"
  - "mechanism/multi_agent"
  - "mechanism/provenance_signing"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# TrustIssues.AI

> TrustIssues.AI automates vendor onboarding with a multi-agent AI. Agents extract data, verify identity, and score risk, blending AI speed with human approval for secure, fast compliance.

[Devpost](https://devpost.com/software/coffee-overflow) · hackathon [[HackUTD 2025- Lost in the Pages]]

## Facets

**mechanism** [[deterministic_policy]] [[human_in_the_loop]] [[multi_agent]] [[provenance_signing]]
  <sub>weak: cross_origin_web</sub>
  <sub>weak: developer_tools</sub>
**user** [[researcher]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** nemotron, openaisdk, python, streamlit

## How they structured the write-up

- our vision
- what trustissues.ai does:
- how we built it:
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trustissues.ai

## Body

Login Page Vendor Dashboard Admin Dashboard Upload Document Page Risk Analysis Pending approvals page Our Vision Manually onboarding new vendors and clients is notoriously slow, inconsistent, and fraught with risk. Teams have to manually sift through documents, check multiple databases, and make subjective judgment calls. This process, taking up to SIX MONTHS, creates compliance gaps and security holes. We were inspired to build a system that could automate this entire due diligence process, blending the speed of AI with the critical oversight of a human expert. What TrustIssues.AI does: TrustIssues.AI is an intelligent multi-agent system that automates vendor onboarding. When you submit a vendor's PDF, a team of AI agents is deployed and they collaborate to, 1. Extract: An Extractor agent reads the PDF and pulls out key company data. 2. Verify: A Verifier agent checks this data against company registries and international sanctions lists. 3. Analyze: A Risk Analyst agent calculates a deterministic, rules-based risk score. 4. Explain: The system, powered by NVIDIA Nemotron , provides a human-readable explanation for its risk assessment. 5. Recommend: Finally, it recommends an access level (e.g., "Standard Access" or "Reject") but critically requires a human manager to review the complete audit trail. This human touch is added to give final approval before any system access is granted. How we built it: Much like our team name, Coffee Overflow , a lot of coffee was involved. We built this as a true agentic multi-agent system in Python, not a simple, rigid workflow. 1. Core Logic: We used a ReAct-style (Reason → Act → Observe) pattern for four specialized agents: a Coordinator, Extractor, Verifier, and Risk Analyst. 2. AI Brains: The agents' reasoning and explanation capabilities are powered by NVIDIA Nemotron-49B-Instruct. 3. Tooling: Agents dynamically decide which tools to use via function calling. These tools include a PyPDF2 and regex-based PDF extractor, a FuzzyWuzzy-based sanctions list checker, and a deterministic Python rules engine for calculating the final risk score. 4. Auditability: Every thought process, tool call, and decision from each agent is logged to a JSON file for a transparent audit trail. Challenges we ran into Our biggest challenge was designing the agentic collaboration (and getting enough caffeine). Getting specialized agents to reason autonomously, pass information reliably, and decide the next best action (e.g., "Data is extracted, now I must call the Verifier") was far more complex than a simple script. Another challenge was ensuring reliability. We learned early on that we couldn't trust an LLM to guess a risk score. This led us to a hybrid approach: using the LLM for reasoning and explanation but keeping the actual risk calculation 100% deterministic and rules-based. We also had to build robust error handling for tricky PDF extractions. Accomplishments that we're proud of We are incredibly proud of building a true multi-agent system where agents reason and collaborate, not just a linear pipeline. We're also proud of our core design principle: Human-in-the-Loop . The system provides a powerful recommendation, but all its reasoning is transparent, and it never grants access without final human approval. This makes it a practical, safe tool for real-world enterprise use. What we learned We learned a shocking amount about the power and pitfalls of agentic AI, in equally shocking amount of time. The main takeaway is that for high-stakes tasks like risk and compliance, you can't just prompt your way to a solution. You need a robust architecture that blends the reasoning power of LLMs (like Nemotron) with deterministic, auditable business logic and a non-negotiable human-in-the-loop for safety and accountability. What's next for TrustIssues.AI The current version uses mock APIs for verification. The immediate next step is to plug in real-world APIs for company registries (like OpenCorporates) and sanctions screening services. After that, we plan to expand the system's capabilities by adding new risk factors, integrating more tools (like checking for adverse media), and implementing time-limited and revocable access controls based on the final approved risk level. <div