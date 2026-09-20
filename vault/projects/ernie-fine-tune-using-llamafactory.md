---
slug: "ernie-fine-tune-using-llamafactory"
url: "https://devpost.com/software/ernie-fine-tune-using-llamafactory"
title: "ERNIE Fine-Tune using LlamaFactory"
hackathon: "ERNIE AI Developer Challenge"
organization: "Baidu"
winner: true
words: 1002
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
  - "user/general_public"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# ERNIE Fine-Tune using LlamaFactory

> "The Emperor's Voice, Digitally Preserved"

[Devpost](https://devpost.com/software/ernie-fine-tune-using-llamafactory) · hackathon [[ERNIE AI Developer Challenge]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[education]] [[scientific_research]]
**user** [[educator_student]] [[general_public]] [[researcher]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** css, ernie-0.3b, finetuning, html, javascript, llamafactory, peft, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ernie fine-tune using llamafactory

## Body

Inspiration The idea for this project was born from a simple question: How can we make history more engaging and accessible? Pu Yi's life story—from child emperor to prisoner to ordinary citizen—is one of the most extraordinary narratives of the 20th century, yet it remains largely unknown outside academic circles.We were inspired by the potential of Large Language Models to not just retrieve information, but to embody historical perspectives in a conversational format. By fine-tuning ERNIE on Pu Yi's autobiography "From Emperor to Citizen," we aimed to create an AI that doesn't just know about history—it speaks from within it, offering students, researchers, and history enthusiasts an unprecedented way to explore early 20th-century China through first-person narrative. What it does Our project transforms the ERNIE-4.5-0.3B-PT model into a specialized historical conversational AI that can: Answer questions in first-person as Pu Yi, drawing from his complete autobiography Provide historically accurate responses covering his entire life from 1906-1967 Engage in natural conversations about complex historical events like the fall of the Qing Dynasty, the Manchukuo period, and his re-education Maintain temporal consistency across different life periods -Preserve cultural context while making history accessible to modern audiences Users can ask questions like "What was it like to become emperor at age two?" or "How did you feel during your trial?" and receive thoughtful, contextually accurate responses grounded in primary source material. How we built it Data Pipeline Engineering Extracted and processed 200,000+ words from Pu Yi's autobiography Segmented content into 9 strategic chapters covering his entire life arc Used Google Gemini 2.5 Flash to generate 7,411 high-quality instruction-output pairs Implemented quality assurance through JSON validation, deduplication, and source attribution Dataset Creation Designed an Alpaca-style format for instruction fine-tuning Ensured first-person narrative consistency throughout Balanced distribution across life periods (32% childhood, 25% imperial period, 18% Manchukuo, etc.) Created diverse question types: direct questions (40%), personal queries (25%), analytical (20%), descriptive (15%) Model Fine-Tuning Selected ERNIE-4.5-0.3B-PT as base model for its multilingual capabilities Applied LoRA (Low-Rank Adaptation) for efficient fine-tuning Used LLaMA Factory framework for streamlined training pipeline Configured optimal hyperparameters: learning rate 5e-5 to 3e-4, batch size 4-8, 3-5 epochs Technology Stack Data Generation: Python, Google Gemini API, custom extraction scripts Training Framework: LLaMA Factory, PaddlePaddle/PyTorch Fine-tuning Method: LoRA adapters Dataset Format: Alpaca-style JSON Challenges we ran into Historical Accuracy vs. Narrative Flow Balancing factual precision with engaging first-person narrative was challenging. We solved this by implementing source attribution for every training pair and cross-referencing multiple historical sources. Handling Sensitive Historical Content Pu Yi's collaboration with Japanese forces during WWII is historically controversial. We addressed this by presenting balanced perspectives and ensuring the AI acknowledges complexity without judgment. Data Generation at Scale Generating 7,400+ high-quality question-answer pairs required careful prompt engineering with Gemini. We implemented batch processing with intelligent chunking (8000 chars/chunk) and temperature tuning (0.8) to maintain quality. Temporal Consistency Ensuring responses remained consistent with Pu Yi's age and circumstances at different life stages required careful chapter segmentation and metadata tagging. JSON Parsing Errors API responses occasionally returned malformed JSON. We built robust error recovery with regex-based salvaging for partial responses. Limited Compute Resources Fine-tuning even a 0.3B parameter model required significant GPU memory. We optimized using LoRA's low-rank adaptation and gradient accumulation to work within constraints. Accomplishments that we're proud of Created 7,411 high-quality training pairs from a single primary source—one of the largest domain-specific historical datasets for LLM fine-tuning Achieved comprehensive coverage of all major life periods spanning 61 years (1906-1967) Maintained first-person narrative consistency throughout, creating an authentic conversational experience Built a production-ready pipeline that can be easily adapted to other historical figures or biographical sources Demonstrated practical ML pipeline engineering from raw PDF extraction through model deployment Balanced technical excellence with historical sensitivity, handling controversial topics responsibly Made history accessible through natural conversation rather than dense academic text What we learned Technical Insights: LoRA is incredibly efficient for domain-specific fine-tuning—we achieved strong results with minimal parameter updates Data quality > quantity: Our focused, high-quality 7K pairs outperformed approaches using larger but noisier datasets Gemini 2.5 Flash is excellent for synthetic data generation when properly prompted LLaMA Factory significantly streamlines the fine-tuning workflow compared to raw transformers Domain Knowledge: Historical NLP requires special care—temporal consistency, source attribution, and bias awareness are critical First-person narrative training creates more engaging outputs than third-person factual responses Chapter-based segmentation preserves contextual coherence better than random sampling Project Management: Iterative pipeline development is crucial—we refined our data generation process through multiple iterations Documentation matters—thorough tracking of sources and methodology ensures reproducibility Ethical considerations should be built into the pipeline from day one, not added later What's next for ERNIE Fine-Tune using LlamaFactory Immediate Next Steps: Multi-turn Conversation Capability - Enable extended dialogues that maintain context across exchanges Source Citation System - Automatically reference specific chapters/pages from the autobiography Web Demo Interface - Deploy an interactive chat interface for public access Quantitative Evaluation - Conduct formal testing on historical accuracy, perplexity, and BLEU scores Medium-term Goals: Expand to Other Historical Figures - Apply the same pipeline to other autobiographies (Gandhi, Malcolm X, Anne Frank) Multilingual Support - Train parallel Chinese version for native language access Image Integration - Add multi-modal capabilities to analyze historical photographs Educational Curriculum - Partner with schools to integrate into history education Long-term Vision: Historical Figures Database - Create a comprehensive library of AI-powered historical personas Virtual Museum Integration - Deploy in cultural heritage sites as interactive exhibits VR/AR Experiences - Enable immersive historical conversations in virtual environments Research Platform - Build tools for historians to quickly query and cross-reference biographical sources Temporal Question Answering - Advanced capabilities to answer "what if" scenarios and comparative historical questions Open Source Contribution: Release the Puyi Historical Dataset publicly for academic research Share our data generation pipeline as a reusable framework Publish fine-tuning guidelines for historical and biographical LLM applications This project proves that LLMs can do more than answer questions—they can preserve voices from history, making the past more accessible and engaging for future generations. <div