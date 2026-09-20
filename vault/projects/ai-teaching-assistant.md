---
slug: "ai-teaching-assistant"
url: "https://devpost.com/software/ai-teaching-assistant"
title: "AI Academic Feedback Assistant"
hackathon: "HackAI - Dell and NVIDIA Challenge"
organization: "Dell"
winner: true
words: 435
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/finance_payments"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# AI Academic Feedback Assistant

> The all-in-one platform to quickly assess, publish, and re-evaluate students' assignments!

[Devpost](https://devpost.com/software/ai-teaching-assistant) · hackathon [[HackAI - Dell and NVIDIA Challenge]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[education]] [[finance_payments]]
**user** [[educator_student]] [[researcher]]
**substrate** [[document_pdf]] [[geospatial]] [[structured_db]]

**stack** gradio, langchain, nvidia-workbench, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ai academic feedback assistant

## Body

AI Academic Feedback Assistant Recursive summarization Email handling Requirement, Assignments, Feedback RAG Inspiration Recently my assignment took 5 weeks to be marked! I was so discouraged at first, but then I found out 2 graders were marking over 350 assignments! So I built this app to help them streamline the marking process! Knowing that many graders lack technical AI knowledge or computing resources, NVIDIA AI Workbench is a great solution! What it does We built AI Academic Feedback Assistant , which is an NVIDIA AI Workbench native app. It utilizes NVIDIA Workbench's ability to quickly spin up a GenAI application! You can load assessment criteria documents and student assignments, and our Assistant will give marking suggestions for you! You can also let AI generate summary or response email for you! You can either choose the local Phi-3 mini model, or use NVIDIA hosted NIMs! How we built it NVIDIA AI Workbench Gradio LangChain Phi-3 NVIDIA API Catalog NIMS I have a GPU laptop, but I mainly code on my Mac. NVIDIA AI Workbench is really convenient since I can code on my Mac and run on my GPU laptop. I don't have to worry much about building the container, and mapping ports, as those tasks are all automated for me. The ability to edit build scripts and env variables directly through a user-friendly GUI brings non-DevOps people into the game! Challenges we ran into We want our project to be compatible with low-performance GPUs, as not all graders have access to good GPUs. Therefore, we aim to minimize the model size to decrease generation time. However, the documents are usually large, and small models hallucinate a lot! Solution: RAG We store documents in a vector database and only retrieve relevant chunks of text. For smaller models and weaker GPUs, this technique reduces inference time dramatically! Accomplishments that we're proud of We managed to provide a pretty accurate response with Phi-3-4k-mini-instruct. Its performance is on par with 7B mistral or 8B llama. We are happy that we solved a real problem, and we hope our project will positively impact AI in the education domain. We also made a great video pitching our idea! Check it out [here]( What we learned We learned how NVIDIA AI Workbench automates time-consuming tasks for us! What's next for AI Academic Feedback Assistant We find out that the process of assessment, reading complaint emails, and returning formal responses is a repetitive task not only in the education domain, but in others as well, like insurance, consultant, or retails. We hope to generalize the application to many domains in the future. <div