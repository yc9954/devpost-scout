---
slug: "truthlens-fwo02r"
url: "https://devpost.com/software/truthlens-fwo02r"
title: "TruthLens"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 959
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/media_journalism"
  - "domain/scientific_research"
  - "user/educator_student"
  - "user/legal_professional"
  - "user/researcher"
---

# TruthLens

> Research Guardian helps students evaluate scientific papers by scoring reliability, finding contradictions, and turning complex research into clear, evidence-based insights.

[Devpost](https://devpost.com/software/truthlens-fwo02r) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[graph_reasoning]] [[retrieval_grounding]]
**domain** [[education]] [[media_journalism]] [[scientific_research]]
**user** [[educator_student]] [[legal_professional]] [[researcher]]

**stack** chatgpt, claude, crossrefapi, geminiapi, lovable, openalexapi, sematicscholarapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned
- accomplishments we are proud of
- what's next for truthlens

## Body

Home page Sign In Home Uploading Scored Settings Light Mode History TruthLens Inspiration As a high school student, I genuinely enjoy research. I often work on independent projects where I need to read scientific papers, compare sources, and understand whether the information I am using is actually reliable. However, at some point, all researchers quickly realize that research papers can be difficult to judge. A paper may look credible because it is well-written, highly technical, or published in a respected journal, but that does not always mean its claims are fully reliable. Some papers may have weak evidence, limited methodology, outdated conclusions, internal contradictions, or later studies that challenge their findings. This problem inspired me to build TruthLens. I wanted to create a tool that helps students and researchers go beyond simply reading or summarizing papers. TruthLens is designed to help users ask two more important questions: Can I trust this paper? and Where should I research next? By combining reliability checking with research gap detection, TruthLens helps make research more careful, critical, and useful. TruthLens was inspired by that problem. I wanted to build something that goes beyond summarization. Instead of only asking, "What does this paper say?" , TruthLens asks two deeper questions: Can I trust this paper? Where should I research next? The goal was to create a tool that helps users evaluate scientific reliability and discover unanswered questions in research. What It Does TruthLens has two main functions. First, it works as a research gap finder . Users can upload papers, and TruthLens identifies established knowledge, missing variables, unanswered questions, contradictions, and possible future research directions. This helps users move from reading papers to actually forming new research ideas. Second, it works as a reliability checker . TruthLens evaluates papers based on source credibility, methodology, evidence strength, internal consistency, bias, timeliness, and external validation. It also compares the paper with related scientific literature to determine whether the paper is supported, challenged, or contradicted by other work. The reliability score is based on a weighted system: $$ \text{Final Reliability Score} = \text{Internal Reliability} + \text{External Validation} $$ where: $$ \text{Internal Reliability} = 65\% $$ and: $$ \text{External Validation} = 35\% $$ This matters because a paper should not be judged only by how convincing it looks internally. Scientific reliability also depends on whether later research supports it. How We Built It TruthLens was built using React , TypeScript , Tailwind CSS , Supabase , Gemini API , and OpenAlex API . React and TypeScript were used to build the main web application. Tailwind CSS was used for the interface so the platform would feel clean, modern, and professional. Supabase was used for backend functionality and storage. Gemini was used as the reasoning engine to analyze uploaded papers, explain reliability, and generate research gaps. OpenAlex was used to retrieve external scientific literature so that TruthLens could compare papers with the broader research landscape. The system was designed so that Gemini analyzes the paper, while OpenAlex provides external scientific evidence. This separation is important because AI should not invent support or contradictions. The AI should explain evidence, not replace it. Challenges We Faced The hardest challenge was reliability itself. At first, the app could analyze uploaded papers and generate reasonable-looking scores, but those scores were not always accurate. The system relied too much on the uploaded paper and not enough on external evidence. This caused the AI to sometimes overrate papers that looked strong internally but had later been challenged, contradicted, or retracted. Another challenge was external comparison. Searching for a paper by its exact title was often not enough. To improve this, we had to think about concept-based searching, using keywords, topics, authors, and related ideas instead of only exact titles. We also learned that different types of papers need different scoring systems. A review paper should not be punished for lacking original experiments, because that is not its purpose. An experimental paper, however, should be judged more heavily on methodology, controls, sample size, and reproducibility. What We Learned This project taught us that scientific truth is not simple. A paper is not reliable just because it is well-written, highly cited, or published in a famous journal. Reliability depends on methodology, evidence, replication, external validation, and scientific consensus. We also learned that AI works best when it is grounded in evidence. If an AI model is asked to judge a paper without outside sources, it may produce confident but incomplete results. A stronger system needs both reasoning and retrieval. The most important lesson was that answering "What does this paper say?" is much easier than answering "Should I believe this paper?" TruthLens is built around the second question. Accomplishments We Are Proud Of We are proud that TruthLens is not just another paper summarizer. It attempts to solve a more meaningful problem: helping users evaluate reliability and discover future research opportunities. We are also proud of building a structured reliability scoring system, integrating AI analysis with external literature search, and designing the product around real research workflows. The project changed from a simple idea into a platform that could genuinely help students, researchers, journalists, and professionals think more critically about scientific information. What's Next for TruthLens The next step is improving external validation. Future versions of TruthLens could include stronger retraction detection, citation network visualization, support for review papers and meta-analyses, and a knowledge graph showing how different papers agree or disagree with each other. We also want to improve claim-level analysis, where TruthLens evaluates individual claims inside a paper instead of only scoring the paper as a whole. Eventually, TruthLens could become a platform that helps people navigate research with more confidence, identify weak evidence, and discover the unanswered questions that lead to new ideas. <div