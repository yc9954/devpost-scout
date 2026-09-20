---
slug: "wolfiesign"
url: "https://devpost.com/software/wolfiesign"
title: "WolfieSign"
hackathon: "The Docusign Hackathon: Unlocked"
organization: "Docusign"
winner: true
words: 381
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "substrate/document_pdf"
---

# WolfieSign

> Manage, generate, and send agreements in one click! Built for non-profits, WolfieSign simplifies paperwork so volunteers can focus on what matters.

[Devpost](https://devpost.com/software/wolfiesign) · hackathon [[The Docusign Hackathon- Unlocked]]

## Facets

**mechanism** [[realtime_stream]]
  <sub>weak: developer_tools, legal_justice</sub>
**substrate** [[document_pdf]]
  <sub>weak: code_repository, video_visual</sub>

**stack** docusign, firabase, firestore, flask, flutter, openai

## Body

🎮 Inspiration & Context WolfieSign is a simple yet effective dashboard for generating and distributing legal agreements, built with non-profits in mind. In fact, The idea behind the name "Wolfie" comes from the Romanian term for the youngest scouts. Having seen the impact firsthand, I realized how much a tool like this could help. Automating the process of handling common agreements, like GDPR and travel forms, makes the already tough job of volunteers around the world just a little bit easier. 🚀 Features Generate agreements using natural language (powered by OpenAI APIs); Make adjustments to the documents using natural language; Preview document changes in real time using client-side preview rendering (powered by 6 hours of debugging on my part); Distribute in bulk agreements to be signed (powered by Docusign's APIs); Watch in real time as your agreements' status updates; Organize your signees in groups for easier distribution. Manage Documents Generate/Modify Documents with AI ⚙️ Docusign Integration Docusign is at the heart of WolfieSign, handling the signing process. I used DocuSign’s APIs (with JWT authentication) to send envelopes to multiple emails and poll their statuses to keep the dashboard updated. Currently, the service is only available for local deployment. If development continues, the next step will be preparing a cloud-ready image—though this will require some changes to the current authentication flow. 🔨 Timeframe & Tools The entire project was developed for this hackathon and during the hackathon's duration (as visible in the provided GitHub repository). The UI web application was written entirely in dart using Flutter. External APIs used by the Web App: Firebase Auth - for handling user authentication via email/password; Firestore DB- for storing additional user information as well as keeping track of group structures and created documents; OpenAI Gpt-4o - for document generation using natural language; as well as document editing via natural language; Docusign APIs - for creating signing requests and viewing agreement status. 🎯 Accomplishments I surprised myself with how many features I managed to cram into this project. I usually aim for simplicity, but since this theme—helping non-profits deal with their paperwork—is close to my heart, I got a bit carried away with the scope. Even though it’s not yet deployed for my volunteer friends to use, I’m really happy with how it turned out. <div