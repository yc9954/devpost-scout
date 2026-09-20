---
slug: "prompt-guard"
url: "https://devpost.com/software/prompt-guard"
title: "Red Teaming Your LLM"
hackathon: "Databricks Asia Pacific LLM Cup 2023"
organization: "Databricks"
winner: true
words: 413
team_size: 4
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "domain/scientific_research"
  - "domain/security_privacy"
  - "domain/transportation"
  - "user/frontline_worker"
  - "substrate/code_repository"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Red Teaming Your LLM

> Red Teaming Your LLM: Your shield against data breaches. Exclusive jailbreak prompts fortify security, ensuring protection beyond conventional measures. Elevate your defense now.

[Devpost](https://devpost.com/software/prompt-guard) · hackathon [[Databricks Asia Pacific LLM Cup 2023]]

## Facets

**domain** [[developer_tools]] [[scientific_research]] [[security_privacy]] [[transportation]]
**user** [[frontline_worker]]
**substrate** [[code_repository]] [[sensor_telemetry]] [[structured_db]]

**stack** amazon-web-services, databricks, datasets, flask, huggingface, jsonlines, langchain, openai, peft, plotly, python, streamlit, transformers

## How they structured the write-up

- inspiration
- what it does
- how we built it
- dataset
- challenges we ran into
- accomplishments that we're proud of
- what we learnt
- what's next for red teaming llm

## Body

LLM Vulnerabilities Evaluator Red Prompt Rephraser Red Prompt Enhancer Inspiration The rate of LLM adoption has outpaced the establishment of comprehensive security protocols, leaving many applications vulnerable to high-risk issues, as listed in the OWASP Top 10 for LLM applications. We felt that more work should be focused on safeguarding LLMs. To understand what the vulnerabilities are, we start with red teaming the LLM. Our methodology is inspired by 2 research papers: Red Teaming Language Models with Language Models link MasterKey: Automated Jailbreak Across Multiple Large Language Model Chatbots link What it does Our solution is a red-teaming solution to identify the vulnerabilities of a target LLM to different categories of harmful queries. How we built it We built it using: Code - Databricks Compute Clusters and Notebook Serving - Databricks Model Serving Endpoint and Cluster Driver Proxy Endpoint Data Store - Databricks Unity Catalog Model Store - Databricks MLflow Model Registry Applications - Streamlit, Langchain, Flask, Hugging Face Transformers, and OpenAI API. Dataset advbench/harmful_behaviours.csv link as harmful queries. Jailbreak Questions from MasterKey/Jailbreaker paper link as harmful queries. Jailbreakchat.com for jailbreak prompts Challenges we ran into OSError faced when transformers ' trainer completed training. Inability to serve PEFT models as it is being actively developed. Despite this, Databricks provides the flexibility to serve these models on the cluster driver proxy endpoint instead. specifically, after logging the model using pyfunc, we were faced with peft not found error to loaded it. Crafting prompts for fine-tuning required some experimentation. OpenAI API calls were slow during the hackathon period. Accomplishments that we're proud of We broke Gandalf at level 5 using our experimental features. Showing that generated JB prompts are more effective at tearing down the guardrails of open-sourced LLMs. Consolidation of jailbreak prompts from various sources. Completing our first hackathons. What we learnt A good platform/UI facilitates development work; having MLFlow integrated to review the metrics gave good insights. Coding assistance allowed for seamless debugging, making resolving issues easier to handle. Always reach out to the relevant chats to seek assistance or clarification. Finetuning LLMs on limited compute resources. What's next for Red Teaming LLM Develop guardrails and provide guardrail services.​ Improve the harmfulness evaluation model.​ Categorize jailbreak prompts to ensure coverage.​ Train red team LLM to generate category-specific harmful queries.​ Train red team LLM to generate a greater variety of jailbreak prompts.​ Update the repository with publicly released jailbreak prompts automatically.​ Discover novel jailbreak prompts through reinforcement learning.​ Provide multilingual prompts and guardrails.​ <div