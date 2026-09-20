---
slug: "compare-drug-sentiment-from-paper-prescriptions"
url: "https://devpost.com/software/compare-drug-sentiment-from-paper-prescriptions"
title: "Compare Drug Sentiment from Paper Prescriptions"
hackathon: "AWS Marketplace Developer Challenge: ML Powered Solutions"
organization: "Amazon"
winner: true
words: 128
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/health_clinical"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# Compare Drug Sentiment from Paper Prescriptions

> Take an image of a prescription and extract drug name for comparison of patient review sentiment compared to other drugs

[Devpost](https://devpost.com/software/compare-drug-sentiment-from-paper-prescriptions) · hackathon [[AWS Marketplace Developer Challenge- ML Powered Solutions]]

## Facets

**domain** [[health_clinical]]
**user** [[patient_family]]
**substrate** [[structured_db]] [[video_visual]]

**stack** comprehend, jupyter, python, textract

## How they structured the write-up

- goal: compare drug sentiment from paper prescriptions

## Body

Goal: Compare Drug Sentiment from Paper Prescriptions This solution is intended to provide more information to patients regarding the medication they receive. Taking a dataset of unstructured text reviews of different drugs, Amazon Comprehend is used to understand the sentiment of the reviews and a function is created to compare sentiment across different drugs. The solution tackles a second problem which is that of paper-based/handwritten prescriptions (still commonly used across various healthcare systems). Amazon Textract is used to extract text from photocopies or images of paper prescriptions and the 7Park Data drug NER identifies the drug name in the unstructured text data. This then feeds the sentiment comparison lookup for an end-to-end solution. The next step is to integrate this pipeline into a web or mobile app. <div