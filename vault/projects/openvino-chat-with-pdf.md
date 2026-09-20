---
slug: "openvino-chat-with-pdf"
url: "https://devpost.com/software/openvino-chat-with-pdf"
title: "Openvino Chat with PDF"
hackathon: "Red Hat and Intel AI Hackathon"
organization: "Red Hat"
winner: true
words: 126
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "substrate/document_pdf"
---

# Openvino Chat with PDF

> Ask anything from your PDF and get your queries answered without manually going through the All documents.

[Devpost](https://devpost.com/software/openvino-chat-with-pdf) · hackathon [[Red Hat and Intel AI Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**substrate** [[document_pdf]]

**stack** chromadb, huggingface, langchain, llama, openvino, python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for openvino chat with pdf

## Body

Inspiration What it does This is a chat bot which will answer your queries based on the set of pdf documents. It can also summarize the contents of PDF. How we built it We have build it using Openvino, Streamlit and langchain. and running as container in Openshift Cluster on Intel CPU. Challenges we ran into We have faced challenges with model hallucination. Accomplishments that we're proud of We are able to run RAG application on Intel CPU using small parameter model. which is LLama 3.2 3b What we learned We learned how to control hallucination and inference Model on cpu using openvino. What's next for Openvino Chat with PDF We will add multiple document type and enable user login and persist data using collections. <div