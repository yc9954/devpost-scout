---
slug: "ragis"
url: "https://devpost.com/software/ragis"
title: "RAGIS (Retrieval-Augmented Generation Incident Summary)"
hackathon: "HackAI - Dell and NVIDIA Challenge"
organization: "Dell"
winner: true
words: 407
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "user/researcher"
  - "substrate/document_pdf"
---

# RAGIS (Retrieval-Augmented Generation Incident Summary)

> Project uses NVIDIA AI Workbench to easily build an assistant to help security analysts quickly identify false positives, reducing manual effort by using a RAG model for accurate predictions.

[Devpost](https://devpost.com/software/ragis) · hackathon [[HackAI - Dell and NVIDIA Challenge]]

## Facets

**mechanism** [[retrieval_grounding]]
**user** [[researcher]]
**substrate** [[document_pdf]]

**stack** azure, gradio, langchain, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for ragis

## Body

RAGIS Inspiration Security analysts often spend significant time investigating false positives, which can lead to inefficiencies. Study shows that nearly a third of their time is spent on incidents that pose no actual threat. This creates alert fatigue and slows down response times, motivating us to create a solution that reduces this burden and helps analysts focus on real security threats. What it does Our project, RAGIS (Retrieval-Augmented Generation Incident Summary), helps security analysts determine whether an incident is a false positive, or a true positive needing further investigation. It leverages generative AI and company data such as Microsoft Entra ID user details and previously closed incidents to make accurate predictions, saving valuable time and reducing the noise from false incidents. How we built it We are using LangChain to build our RAG analyzer, Gradio as UI framework, and Nvidia cloud endpoints to run models. Azure queries are done with msgraph and azure.monitor.query . The RAG part of our app starts with ChromaDB vectorstore loading, where vector embedding is done with NV-Embed-QA . We prompt meta/llama-3.1-70b-instruct chat model to act as an assistant tasked with determining if an input incident is a "true positive" or "false positive", and give the retrieved documents from ChromaDB as context. Retriever is parameterized to include some added diversity in the data, without sacrificing too much accuracy. Challenges we ran into Tuning the prompt to be accurate but still allow the chat model to generalize to different use cases was a challenging task. Even more challenging was tuning the ChromaDB retriever to include relevant documents with enough diversity to allow for different use cases, without decreasing retrieval accuracy. Documentation for the Azure python packages was seemingly lackluster, we had some difficulty figuring out the queries. Accomplishments that we're proud of We successfully created a functional system that automates a previously time-consuming task for analysts, increasing their efficiency by filtering out false positives and providing context-aware incident analysis. What we learned We learned to utilize AI Workbench to collaborate easily with orchestration automation. Our team consisted of one security architect and one data scientist, which allowed both to learn about the other's field. By collaborating on the data integration between the AI application and Azure, we both learned how the python-AI-Azure interplay works. What's next for RAGIS We plan to scale RAGIS by incorporating additional data sources, improving model accuracy, and integrating more advanced security use cases to tackle evolving cyber threats. <div