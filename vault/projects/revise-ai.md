---
slug: "revise-ai"
url: "https://devpost.com/software/revise-ai"
title: "Revise AI Chrome Extension"
hackathon: "Dropbox Sign AI-Powered Agreements Hackathon"
organization: "Dropbox"
winner: true
words: 462
team_size: 1
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/on_device_local"
  - "mechanism/provenance_signing"
  - "domain/finance_payments"
  - "domain/legal_justice"
  - "user/general_public"
  - "user/legal_professional"
  - "substrate/structured_db"
---

# Revise AI Chrome Extension

> Revise AI automates contract negotiation workflows - instantly draft revisions in Gmail, securely upload/send for e-signature with Dropbox. AI-powered productivity for lawyers.

[Devpost](https://devpost.com/software/revise-ai) · hackathon [[Dropbox Sign AI-Powered Agreements Hackathon]]

## Facets

**mechanism** [[cross_origin_web]] [[on_device_local]] [[provenance_signing]]
**domain** [[finance_payments]] [[legal_justice]]
**user** [[general_public]] [[legal_professional]]
**substrate** [[structured_db]]

**stack** cpp, flask, node.js, pytorch

## How they structured the write-up

- revise ai chrome extension

## Body

Revise AI Gmail Chrome extension Using Revise AI extension for contract revision Accept or request new revision with Revise AI Revised contract negotiation workflow Under the hood Revise AI Chrome Extension Revise AI is a Gmail Chrome extension to automate contract negotiation workflows with large language models. Revise AI helps lawyers negotiate, revise and request signature for contracts without ever leaving their Gmail. Fast, easy to use, customizable and locally deployable. Has the client asked for changes to the contract? Simply click the Revise AI Chrome extension and let it do the heavy work. Revise AI analyzes the email exchange, determines the contract and clauses to be changed, revises the contract to fit the client's need and lawyer's requirements, and instantly creates an editable revised draft. Once done, simply click the Accept button to upload and request a signature for the revised contract via Dropbox Sign API. Important Clarification Note We'd like to note that getting a Chrome extension listed on the Chrome Web Store requires a review and approval process by Google.This approval process typically takes around 1.5-2 weeks. Given the timeframe of the hackathon, it was not feasible to stream it from there. However, to ensure evaluators can experience its full functionality, we're providing the local installation code for the Chrome extension and a test script to directly test the backend API functionality. Why we chose this project Large corporations, banks, and legal firms constantly have to deal with the tedious process of revising contracts and getting signatures. We wanted to integrate AI and e-signature APIs to automate these workflows without taking away lawyers' decision making or adding additional software. How we built it Chrome extension: Developed using Node JS Revise AI backend: Employed the Llama 2 chat model, which was further refined using a manually annotated legal revision dataset, served as an API built with Flask on Google App Engine and Replicate. Challenges We faced hurdles integrating the AI model with the extension. The diverse nature of legal terminology also posed challenges during the AI training phase. Accomplishments that we're proud of We have a state-of-the-art open source language model running on a consumer grade computer as an API. We also carefully curated and engineered a high quality legal dataset that we are planning to open source. What we learned The importance of narrowing the scope - focusing on specific contract types made the AI more accurate. We also learned a lot about fine-tuning, optimizing and serving open source large language models as APIs. What's next for Revise AI We're keen on broadening the AI's competencies to cover additional types of contracts. We're also exploring the possibility of integrating features like calendar booking, with an overarching goal of creating an AI-powered legal assistant that can revolutionize contract workflows. <div