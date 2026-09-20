---
slug: "sympvis-triage-coach"
url: "https://devpost.com/software/sympvis-triage-coach"
title: "SympVis Triage Coach"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 749
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/voice_speech"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/clinician"
  - "user/government_staff"
  - "user/patient_family"
  - "user/social_worker"
  - "substrate/document_pdf"
  - "substrate/geospatial"
  - "substrate/video_visual"
---

# SympVis Triage Coach

> SympVis is a modern web application designed to provide users with health clarity through intelligent, explainable symptom triage.

[Devpost](https://devpost.com/software/sympvis-triage-coach) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[voice_speech]]
  <sub>weak: cross_origin_web</sub>
**domain** [[elder_child_care]] [[health_clinical]] [[mental_health]]
**user** [[clinician]] [[government_staff]] [[patient_family]] [[social_worker]]
**substrate** [[document_pdf]] [[geospatial]] [[video_visual]]

**stack** clerk, gemini, react

## How they structured the write-up

- � inspiration
- ⚕️ what it does
- 🛠️ how we built it
- 🛑 challenges we ran into
- 🏆 accomplishments that we're proud of
- 🧠 what we learned
- 🔮 what's next for sympvis triage coach

## Body

Login Page Dashboard Page Personal Profile Page Sympton Assessment Page Final Confirmation Page Interactive Enquiry Page Result Page Summary of Report in PDF Format � Inspiration We've all spiraled down the rabbit hole of searching symptoms online ("Dr. Google"), only to be met with worst-case scenarios that induce panic rather than clarity. Standard symptom checkers are often rigid, lacking the nuance of a real conversation. We wanted to build a bridge between the user and professional care: a "Triage Coach" that listens like a doctor, understands your specific biological context (age, sex, pregnancy), and—most importantly— explains its reasoning . Our goal was to reduce health anxiety by providing a transparent, evidence-based risk assessment. ⚕️ What it does SympVis is an intelligent, privacy-first triage application that acts as your first line of defense. Contextual Intake : It gathers critical biological markers (Age, Sex, Pregnancy status, Chronic conditions) to tailor its risk model. Visual Symptom Timeline : Users can map out exactly when symptoms appeared, helping the AI understand disease progression (e.g., "Fever started 2 days ago, Rash today"). Interactive Follow-up : Instead of making a guess on vague info, SympVis asks 2-3 targeted clarification questions (generated dynamically) to rule out strict emergencies. Explainable Results : It delivers a coded Risk Level (Green/Yellow/Red) accompanied by a "Confidence Score" and a "Confidence Reason," explicitly citing which user-reported symptoms led to the conclusion. Actionable Output : Users get a generated PDF summary to show their doctor and, in high-risk cases, are immediately shown a directory of nearby emergency facilities. 🛠️ How we built it The Core (AI) : We leveraged Google's Gemini 2.5 Flash for its speed and reasoning capabilities. We used a "Chain of Thought" prompting strategy to force the model to evaluate biological risk factors before generating a final verdict. Frontend : Built with React 19 and Vite for a blazing fast experience. We used Tailwind CSS to create a "Glassmorphism" aesthetic that feels clean, premium, and calming—essential for a health app. State Management : Complex multi-step wizard logic handles the flow from Basic Info -> Timeline -> Triage -> Follow-up -> Results. Security : Integrated Clerk for seamless, secure user authentication. Output : Used jspdf to programmatically generate a professional clinical summary that patients can physically take to a hospital. 🛑 Challenges we ran into The "Uncertainty" Problem : Early versions of the model would confidently guess even when the symptoms were vague. We had to implement a strict "Uncertainty Guardrail" where the AI is instructed to reject the request and ask for more detail if the confidence threshold isn't met. Structured JSON from AI : Getting the LLM to consistently return valid JSON for not just the risk level, but also the dynamic follow-up questions and array of "Observation Signals", was tricky. We refined our schema definition to ensure robust parsing. Visualizing Time : Designing a UI that allows users to easily impute a "Timeline" of symptoms (Day 1 vs Day 3) required several iterations to make it intuitive on mobile. 🏆 Accomplishments that we're proud of The "Explainability" Layer : We didn't just want a black box. Seeing the AI quote specific symptoms back to the user ("I am concerned because you mentioned shortness of breath in combination with chest pain ") builds immense trust. Premium UX/UI : The application feels like a high-end medical device interface. The animations and transitions make the experience less clinical and more comforting. Dynamic Safety : The system automatically adjusts its sensitivity. For example, a fever of 100.4°F triggers a different risk path for a pregnant user versus a general user. 🧠 What we learned Context is King : A symptom check without biological context (age/sex) is nearly useless. Adding these parameters improved our AI's accuracy dramatically. Prompt Engineering is a Safety Feature : You cannot rely on the model's default training for medical advice. You must explicitly instruct it on boundaries (e.g., "Do not diagnose, only assess risk"). User Trust : Users are more likely to accept an AI's advice if it admits when it's unsure, rather than forcing an answer. 🔮 What's next for SympVis Triage Coach Multimodal Analysis : Integrating Gemini's vision capabilities to allow users to upload photos of visible symptoms (rashes, swelling) for analysis. Voice Interface : Adding a "Speak your symptoms" feature for elderly users or those in distress. Live Integration : Connecting the "Emergency Finder" directly to hospital wait-time APIs. Local LLM Support : Exploring on-device models for privacy-focused, offline triage in remote areas. <div