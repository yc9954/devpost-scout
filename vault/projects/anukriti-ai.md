---
slug: "anukriti-ai"
url: "https://devpost.com/software/anukriti-ai"
title: "Anukriti AI"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 597
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/simulation_digital_twin"
  - "user/researcher"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Anukriti AI

> Anukriti uses Amazon Nova AI agents to simulate how ideas perform in complex real-world scenarios, helping innovators detect risks early and design better solutions before launch.

[Devpost](https://devpost.com/software/anukriti-ai) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[simulation_digital_twin]]
  <sub>weak: health_clinical</sub>
**user** [[researcher]]
  <sub>weak: patient_family</sub>
**substrate** [[structured_db]] [[video_visual]]

**stack** ai-agents, amazon-bedrock, amazon-nova, amazon-web-services, fastapi, generative-ai, python, rag, vector-database

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned

## Body

Anukriti Cover Image Anukriti Main Screen Screenshot Anukriti BatchMode page Screenshot Anukriti Patient Genetics Screenshot Anukriti Similar Drugs Retrieved Screenshot Anukriti Simulation Results - Predicted Response + Risk Screenshot Inspiration Many innovations fail not because the ideas are bad, but because their real-world behavior cannot be fully understood during early testing. Controlled environments rarely capture the diversity and complexity of real-world conditions. We were inspired to explore whether AI could help simulate complex scenarios earlier in the development process. If researchers and innovators could explore different outcomes before deployment, they could detect risks sooner and design better solutions. Anukriti was created to demonstrate how generative AI can act as a reasoning engine for simulation — helping teams explore possible outcomes before they happen in the real world. What it does Anukriti is an AI-powered simulation platform that helps innovators explore how ideas may behave across diverse real-world scenarios. Using Amazon Nova models, users can describe a scenario or upload contextual information. The system analyzes the input and generates simulated insights about potential outcomes, risks, and patterns. Key capabilities include: Scenario-based simulation using AI reasoning Context-aware analysis of user inputs AI-generated insights that highlight possible risks and improvements Interactive exploration of potential outcomes Conceptually, the system evaluates potential outcomes across different conditions: $$ Outcome = f(Context, Variables, Constraints) $$ This allows users to explore how different factors may influence the behavior of a solution before it is deployed. How we built it Anukriti is built as a modular AI system using Amazon Nova models through Amazon Bedrock. The architecture consists of several components: 1. AI Reasoning Layer Amazon Nova models process user queries, interpret contextual inputs, and generate structured insights. 2. Scenario Processing Engine User inputs are converted into structured simulation scenarios that AI agents can evaluate. 3. Context Retrieval System Relevant contextual information is retrieved using vector embeddings, enabling the AI to reason with supporting information. 4. Simulation Pipeline AI agents analyze different aspects of the scenario, including contextual signals, potential risks, and outcome patterns. 5. Interface Layer A lightweight interface allows users to interact with the system and explore generated insights. Technologies used: Amazon Nova models via Amazon Bedrock Python backend FastAPI for APIs Vector database for contextual retrieval AWS infrastructure for deployment Challenges we ran into Designing meaningful simulations with generative AI was one of the biggest challenges. AI models can generate responses easily, but ensuring those responses reflect structured reasoning required careful system design. Another challenge was balancing system complexity with the constraints of a hackathon project. We needed an architecture that was powerful enough to demonstrate the concept while still being implementable within a limited timeframe. We also experimented with different prompt structures and agent workflows to improve the quality and consistency of the generated insights. Accomplishments that we're proud of Building a working AI-powered simulation prototype Integrating Amazon Nova models into a multi-component architecture Designing a modular system that can be extended with additional agents and datasets Demonstrating how generative AI can support decision-making through scenario exploration Within a short hackathon timeframe, we were able to transform a complex idea into a functional prototype. What we learned Through building Anukriti, we learned that generative AI can be far more powerful when used as a reasoning and simulation tool rather than simply as a text generator. We also learned how important system architecture is when building AI applications. Combining contextual retrieval, structured inputs, and reasoning models significantly improves the usefulness of AI-generated insights. Finally, this project gave us deeper experience working with Amazon Nova models and building scalable AI-powered workflows on AWS. <div