---
slug: "the-new-evolution-for-genetic-algorithm-in-nlp"
url: "https://devpost.com/software/the-new-evolution-for-genetic-algorithm-in-nlp"
title: "PromptZ"
hackathon: "OpenD/I: Shaping Data & Infrastructure for the next 10-20 Years"
organization: "Openmesh Network"
winner: true
words: 312
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/security_privacy"
---

# PromptZ

> Our genetic algorithm focuses on safeguarding large language models against abuse by identifying potentially malicious prompts.

[Devpost](https://devpost.com/software/the-new-evolution-for-genetic-algorithm-in-nlp) · hackathon [[OpenD-I- Shaping Data - Infrastructure for the next 10-20 Years]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[security_privacy]]

**stack** chatgpt, huggingface, hypercycle, nltk, openai, openmesh, poetry, python, pytorch, spacy, tornado

## How they structured the write-up

- what it does
- how we built it
- what's next

## Body

Frontend - Step 1 Frontend - Real-time GA full-trace Frontend - Interactive with the chromosomes (click in a node) Algorithm overview Chromosome and population diagram Mixing algorithm and mutation This study of developing a genetic algorithm for prompt generation within a Large Language Model (LLM) was inspired by the possibility of safeguarding language models against misuse by discovering prompts that can be potentially malicious. What it does Our solution is a ready to implement framework that generates and refines a list of prompts based on a target response. This functionality is designed to facilitate vulnerability testing for LLMs, offering a proactive approach to mitigate abuse and misuse. How we built it We constructed a Genetic Algorithm (GA) framework that optimizes prompts against specific target objectives. The definition of chromosomes, pivotal to the GA process, can be achieved through keywords or a more sophisticated approach involving natural language. The generation process adapts accordingly, utilizing mutations and crossovers, either through a KeywordsGenerator or NLGenerator, depending on the chosen chromosome definition. The evaluator module, akin to a fitness function, plays a critical role in assessing whether the Large Language Model under Test (LLMUT) outputs align with predefined objectives. We implemented two evaluators: SemanticSimilarityEvaluator, which leverages semantic analysis to measure similarity, and ObjectiveSimilarityFunction, which evaluates based on defined objectives, such as generating harmful sentences or extracting privileged information. Prioritizing usability, we incorporated both frontend and backend components into our system. The RestAPI with a hypercycle server allows efficient retrieval of optimal results, while the bidirectional real-time interaction between the frontend and backend provides a comprehensive trace of the algorithm's execution. This approach enables a deeper understanding of the LLM's behavior by identifying words or sentences prone to achieving better performance. What's next We are excited to make the project open-source, and we invite all enthusiasts from the community to shape the future of this project. <div