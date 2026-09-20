---
slug: "trialscope-ai"
url: "https://devpost.com/software/trialscope-ai"
title: "Trialscope AI"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 1241
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/measured_ablation"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "domain/civic_government"
  - "domain/health_clinical"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "user/government_staff"
  - "user/patient_family"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
---

# Trialscope AI

> Your AI-driven clinical trial intelligence platform that reviews, benchmarks, and regenerates protocol drafts into USDM-ready, FDA-aligned docs: Reducing amendments, delays, and cost overruns.

[Devpost](https://devpost.com/software/trialscope-ai) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[benchmark_measured]] [[measured_ablation]] [[retrieval_grounding]] [[simulation_digital_twin]]
**domain** [[civic_government]] [[health_clinical]] [[scientific_research]] [[security_privacy]]
**user** [[government_staff]] [[patient_family]] [[researcher]]
**substrate** [[document_pdf]] [[financial_record]] [[sensor_telemetry]]
  <sub>weak: web_dom</sub>

**stack** anthropic, css, html, next.js, postgresql, python, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for trialscope ai

## Body

Inspiration The members of the Trialscope AI team came into CalHacks with all but a singular question: " Why do SO MANY promising discoveries at the bench fail to reach the patients at the bedside? " In fact, roughly 9 in 10 clinical developments fail between starting Phase I trials and receiving regulatory approval. While many of these failures stem from biological uncertainty, a surprisingly large proportion are lost not in the lab, but in clinical trial design and operations. While wet-lab innovation races ahead, trial design still lives in sprawling word documents/PDFs - Even at leading biopharma companies . These protocols span hundreds of pages, presenting scattered trial design information. When foundational design choices are made inside such unstructured, manual systems, trials become vulnerable to avoidable operational risks : misaligned endpoints, impractical timelines, or regulatory gaps that can compromise even the most promising science. The result? Delayed trials, avoidable amendments, and millions of dollars in wasted effort. Enter TrialScope AI. Our mission? Controlling the controllables, by making clinical trial design as intelligent as the science it tests , narrowing the chasm between therapeutic discovery and approval. What it does TrialScope AI transforms messy, unstructured trial drafts into structured and regulator-aligned designs, followed by regenerating improved versions using AI. Upload any Phase II–III trial draft PDF doc. Convert it into a machine-readable USDM structure (Schedule of Activities, endpoints, arms, eligibility, etc.) Generate insights on factors that may slow down trial progress using data from 1M+ historical clinical studies, benchmarking performance metrics such as duration, procedural burden, and amendment likelihood. Identify missing regulatory elements by cross-referencing FDA guidance documents, while highlighting compliance gaps and potential design inefficiencies. Benchmark trial performance against studies of similar drugs, mechanisms, and phases, providing justification on how design choices (e.g., endpoints, visit frequency, population scope) align with successful precedents. Regenerate an improved, citation-linked draft and export it as USDM-ready JSON/XML for CRO or CTMS integration. How we built it On Friday, we built a simple prototype of next.js frontend with a text box that communicated with a backend via an API to allow for natural language queries to the clinicaltrials.gov api. We spent the rest of the day prototyping a full-stack platform to include features such as finding similar studies to demonstrate average metrics such as cohort size, number of endpoints, etc. We also trained an xgboost ML model to predict the probability of a given protocol to go overtime, as we felt this unanticipated weeks to months led to large expenditures for companies. On Saturday morning, we met with Henry Wei of Regeneron to discuss the direction we were planning on going into and decided we wanted to build a tool to extract insights from clinical trials going from preclinical to phase 1. There, we decided to pivot to stage 2-3 clinical trial protocols, as that time-stage had the most potential to save researchers time through operation parameter changes. We also decided to include a tool to use LLMs to do compliance oversight on a protocol draft utilizing FDA guideline documents. Finally, we decided it would be critical to utilize the USDM format of trial design to standardize all internal operations. Saturday night, we met with Henry for the second time and gained a lot of insights as to the potential of LLM-improved clinical trials. Throughout the night, we added features such as the LLM oversight tool, a modified xgboost model to predict average time of study, additional graphs to visualize insights, and a USDM rewriting tool that showed side-by-side differences. Going into Sunday morning, we had a functional product that could extract a plethora of actionable insights from protocol drafts for researchers targeting phase 2-3 clinical trial success. Challenges we ran into The main challenge we ran into was narrowing down the precise problem scope. As a group that has had minimal experience running clinical trials, we ran mock “customer discovery/insights” interviews with experts in the field (Shout Out Henry Wei, M.D. of Regeneron!) to refine the problem/needs statement and inform our solution landscape + implementation. Pivoting our technical solution based on each interview required a flexible mindset and agile implementation. There were some technical challenges, mainly on the front-end back-end interfacing, as well as resolving merge conflicts between team members. We were able to resolve these challenges with AI assistance. Accomplishments that we're proud of We built a complete, production-ready pipeline capable of turning raw, unstructured clinical trial PDFs into optimized, regulator-aligned designs. The system processes multi-hundred-page protocols and benchmarks them against over half a million historical studies in under ten minutes. It implements CDISC USDM v3.0—the same data model used by top pharmaceutical companies—allowing seamless integration into CRO and CTMS workflows. The platform unites semantic embeddings, Claude API, MCP tools, XGBoost modeling, and rule-based validation into one coherent, automated framework. Our most significant accomplishment wasn’t just the technical complexity, but the practicality of what we built. TrialScope AI functions as a true operational tool, capable of fitting into real biopharma workflows and addressing inefficiencies that cost companies millions. Within just 36 hours, we delivered a prototype that could realistically reduce delays, standardize design choices, and make the process of clinical trial planning as intelligent and data-driven as the science it aims to validate. What we learned Solving a hackathon required full immersion in the problem space - especially as we were working specifically to address needs in the clinical trials space. This required a full-on crash course of the landscape, as further understanding of the technicalities of each clinical trial phase resulted in us challenging and augmenting our own assumptions: whether it was the type of need to address, our entry point into the clinical trial timeline or the modality in which we implemented our solutions. Our process went beyond simply building a prototype: rather, it involved thinking like a real bio-AI software company. We dived into processes like defining our market position, identifying unmet needs, and translating technical insights into product strategy. This hands-on experience revealed how interdisciplinary problem-solving operates in practice, especially at the intersection of biology and AI. The hackathon became less about competition and more about understanding the actual workflow, validation process, and communication style of startups in this space. It showed us how to move from concept to execution within real constraints, and provided the foundation for pursuing further research, development, and innovation in this field beyond CalHacks. What's next for Trialscope AI Short-Term (Next 3 Months) Multi-version protocol generation with A/B testing and citation tracking for every AI-generated recommendation. Track-change visualization between original and optimized drafts. Expand regulatory coverage with 50+ additional FDA guidance documents, ICH standards, and EMA compliance. Improve ML models to predict enrollment success, dropout risk, and time-to-first-patient-in. Add collaboration tools: multi-user access, role-based permissions, comment threads, and version control. Medium-Term (6–12 Months) Pilot partnerships with biotech and pharma companies to validate platform performance and reduce amendment rates. Integrate with EDC and protocol authoring systems (Veeva, Medidata, Word). Add advanced analytics modules for cost estimation, site selection, and feasibility scoring. Extend global regulatory coverage and introduce multi-language support. Long-Term (12+ Months) Implement generative protocol authoring from simple drug or mechanism prompts. Simulate trial outcomes pre-enrollment using predictive models trained on 1M+ trials. Automate regulatory submission workflows, including IND draft generation and FDA response preparation. Release open-source datasets, model weights, and benchmark frameworks for academic collaboration. Achieve <3-minute full analysis time, >0.90 ML accuracy, and scalable performance for 10,000+ concurrent users with HIPAA-compliant security. <div