---
slug: "gptethics"
url: "https://devpost.com/software/gptethics"
title: "GPTEthics"
hackathon: "UC Berkeley AI Hackathon 2024"
organization: "Cal Hacks"
winner: true
words: 291
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
---

# GPTEthics

> Compete against AI (or another human) to solve challenging ethics riddles. Receive feedback in near real-time!

[Devpost](https://devpost.com/software/gptethics) · hackathon [[UC Berkeley AI Hackathon 2024]]

## Facets

**mechanism** [[realtime_stream]]
**substrate** [[structured_db]]

**stack** amazon-web-services, bedrock, boto3, digitalocean, flask, groq, openai, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gptethics

## Body

Inspiration In a world where people are continually faced with complicated decisions, our team wanted to see if the latest AI models would be capable of navigating complex social and moral landscapes of the modern day. This inspired our central focus for this project: exploring the intersection of AI and ethical decision-making and creating an engaging way for people to reflect on their own senses of morality. What it does GPTEthics offers an interactive web platform where: Users are presented with a variety of ethical dilemmas. Both the user and an AI agent respond to these scenarios. An AI-powered system evaluates and compares the responses, providing insights into human vs. AI approaches to moral reasoning. How we built it Our solution integrates several key components: A Flask-based web application for scenario presentation An AI agent powered by GPT-4, AWS Bedrock, and Groq for generating responses An AI-driven scoring system to evaluate the ethical reasoning in responses Challenges we ran into Developing an objective and fair AI scoring system for subjective ethical issues Creating a diverse, representative set of ethical dilemmas Optimizing response times from AWS Bedrock through prompt engineering Accomplishments that we're proud of Successfully integrating AI into an ethics-focused, interactive experience Developing a tool that promotes thoughtful engagement with moral issues Implementing a cohesive web application that effectively utilizes multiple LLM APIs What we learned Valuable perspectives on how humans and AI approach ethical decision-making Understanding the complexities of designing impartial AI evaluation systems for subjective topics Recognizing the ongoing challenges LLMs face in providing robust ethical solutions What's next for GPTEthics Expanding our database of ethical scenarios Refining the AI agent and scoring system for improved performance Exploring the integration of user feedback to enhance the platform's effectiveness <div