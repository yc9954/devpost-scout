---
slug: "smart-research-assistant-agent"
url: "https://devpost.com/software/smart-research-assistant-agent"
title: "Smart Research Assistant Agent"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 494
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/web_dom"
---

# Smart Research Assistant Agent

> An autonomous AI agent powered by Amazon Nova 2 Lite that reasons, selects tools, reads PDFs, and synthesizes intelligent research answers — all without human intervention. #AmazonNova

[Devpost](https://devpost.com/software/smart-research-assistant-agent) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[web_dom]]

**stack** amazon-nova-2-lite, aws-bedrock, boto3, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for smart research assistant agent
- built with

## Body

GIF Inspiration As a student exploring AI, I was fascinated by how modern AI agents can do more than answer questions — they can actually think, plan, and take actions. I wanted to build something that demonstrates this "agentic" behavior using Amazon Nova, showing how a foundation model can power an autonomous research assistant that reasons through problems step by step. What it does Smart Research Assistant Agent is an autonomous AI agent that helps users research topics and analyze documents. When you ask a question, the agent: Reasons about your question using Amazon Nova 2 Lite Decides which tool to use (web search, PDF analysis, or data analysis) Executes the selected tool to gather real information Synthesizes a comprehensive answer using Nova's reasoning The standout feature is real PDF document analysis — the agent can read actual PDF files using PyPDF2, extract text from every page, and use Nova to provide intelligent analysis of the content. How I built it Amazon Nova 2 Lite ( amazon.nova-lite-v1:0 ) via AWS Bedrock Converse API powers all reasoning and synthesis Python for the agent framework with a modular tool system PyPDF2 for real PDF file reading and text extraction boto3 for AWS Bedrock integration The agent uses a structured THOUGHT → ACTION → INPUT loop where Nova decides which tool to use, then synthesizes the results into a final answer Challenges I ran into Getting the Bedrock Converse API message format right — the content field must be a list of content blocks ( [{"text": "..."}] ), not a plain string Handling API throttling gracefully with retry logic when hitting daily token quotas Making the action parser robust enough to handle different LLM output formats (Nova might return ACTION: analyze_pdf("file.pdf") or ACTION: ANALYZE_PDF ) Handling edge cases in PDF extraction where some pages return None from extract_text() Accomplishments that I'm proud of Built a true agentic system that reasons and acts autonomously, not just a chatbot wrapper The PDF analysis feature uses real file I/O — not simulated — making it genuinely useful for research Clean, well-documented code with lazy initialization, error handling, and robust parsing The agent architecture is extensible — adding new tools is as simple as adding a method What I learned How the AWS Bedrock Converse API works and how to integrate Amazon Nova models The difference between a chatbot (prompt → response) and an agent (reason → plan → act → synthesize) How to build a tool-use framework where an LLM decides which tools to call The importance of error handling and retry logic in production AI systems What's next for Smart Research Assistant Agent Connect to real search APIs (Google, DuckDuckGo) for live web research Add multimodal analysis using Amazon Nova's vision capabilities Implement conversation memory so the agent remembers previous questions Support more document formats (Word, Excel, HTML) Deploy as a web application with a proper UI Built with Python, Amazon Nova 2 Lite, AWS Bedrock, PyPDF2, boto3 <div