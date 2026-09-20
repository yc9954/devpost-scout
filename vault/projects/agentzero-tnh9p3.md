---
slug: "agentzero-tnh9p3"
url: "https://devpost.com/software/agentzero-tnh9p3"
title: "Agent Zero"
hackathon: "ShellHacks 2025"
organization: "init"
winner: true
words: 499
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/multi_agent"
  - "mechanism/vision_ocr"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# Agent Zero

> False and duplicate invoices cost AP teams money. By routing extraction, matching, and anomaly checks to our best fit model, our benchmark-driven AI provides proof/confidence for acceptance review.

[Devpost](https://devpost.com/software/agentzero-tnh9p3) · hackathon [[ShellHacks 2025]]

## Facets

**mechanism** [[benchmark_measured]] [[multi_agent]] [[vision_ocr]]
**domain** [[finance_payments]] [[legal_justice]]
**user** [[small_business]]
**substrate** [[financial_record]] [[geospatial]] [[sensor_telemetry]]

**stack** bigquery, express.js, fastapi, gemini, node.js, pyarrow, react, tensorflow, typescript, yolov11

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agent zero

## Body

Logo Inspiration Day and night people constantly get scammed by sly, cunning people that are willing to sacrifice their dignity for an extra buck. It comes in all shapes and sizes, but scammers frequently prey on the weak and less fortunate. Those that are unable to afford financial/legal professionals to protect them. In light of this tragedy, AgentZero is designed to serve as last resort of financial warning for unknowing individuals and small businesses. What it does AgentZero is an AI tool that is made up of an array of specialized agents pretrained on financial data to uncover malicious invoices before they make it to a bank statement. Depending on the task, an orchestrator agent decided which specialized agents to summon and begin assessing invoices. Each agent focuses on distinct subtle signs of fraudulent invoices and provides individualized risk scores for each metric depending on a predetermined rubric and the User's context. The results are aggregated behind the scenes in order to provide an intuitive and concise output on the predicted reliability of an invoice. How we built it Frameworks: Frontend: Node.js, Express.js, React, TypeScript Backend: Python (FastAPI, BigQuery, Gemini, TensorFlow, YOLOv11, PyArrow) Most of the brunt of the project was in developing a research framework from which to maximize our accuracy. We determined which models would provide the best accuracy/time ratio in order to improve the user experience which boasting great results. We also sourced invoice data with computer vision (YOLOv11), fraudulent transaction data from the IEEE and financial anomaly data. This data was then used to make our out in-house agents that were specialized at picking out malicious invoices. Challenges we ran into Accuracy and response time was a big concern when starting this project. Base models were not effective at picking out fraudulent invoices and mostly guessed even though they sometimes loaded for extended periods. We overcame the accuracy problem by pretraining our models and summoning multiple agents that focused on doing just one task very well. We also parallelized our agents and run up to 6 agents at a single time with some invoices. Accomplishments that we're proud of We are proud of leaving our comfort zone and push ourselves to learn about technology with our friends. We ran on nothing but caffeine and group morale all night to create a project that we can be excited to talk to our friends/family about. What we learned We learnt many new technologies and libraries together and taught each other along the way. What's next for Agent Zero AgentZero is a monetizable tool that many individuals and small businesses could use to close the gap between the wealthy and the poor and give everyone an even playing field when it comes to financial scams. With more financial data and fine-tuning AgentZero could actually break into the market and become a product that people wished they'd had earlier. We truly believe in the potential behind this idea and will continue to develop it further after this hackathon. <div