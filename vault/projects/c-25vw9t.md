---
slug: "c-25vw9t"
url: "https://devpost.com/software/c-25vw9t"
title: "Haven"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 682
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/elder_child_care"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# Haven

> An Alzheimer-Friendly Voice Agent When Memories Feel Distant

[Devpost](https://devpost.com/software/c-25vw9t) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
**domain** [[elder_child_care]] [[health_clinical]] [[mental_health]]
**user** [[patient_family]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** elevenlabs, gemini, geminifilesearch, geminiflash, n8n

## How they structured the write-up

- inspiration behind haven
- what it does
- how we built it
- challenges we ran into
- accomplishments that we’re proud of
- what we learned
- what’s next for haven

## Body

Inspiration Behind Haven Alzheimer’s affects millions of people worldwide, gradually taking away their ability to remember personal details, daily routines, and even the people closest to them. During moments of confusion, patients often need reassurance more than raw information. I wanted to explore how AI, when designed thoughtfully, could act as a supportive cognitive companion , not just a chatbot. This project was inspired by the idea that technology can help preserve dignity, emotional safety, and independence for Alzheimer’s patients in their everyday lives. What it does This project is an AI-powered voice assistant workflow built in n8n for Alzheimer’s patients. The assistant can hold calm, reassuring conversations and help patients remember personal details, daily routines, and loved ones. Key capabilities include: Answering personal questions using a RAG (Retrieval-Augmented Generation) tool powered by Gemini File Search API based on the patient’s life history and caregiver notes Checking and creating google calendar events to support daily structure Accessing a contact list of loved ones stored in a google spreadsheet, allowing the assistant to help patients reach family members when in distress or when feeling lonely. Responding with a gentle, slow-paced voice powered by ElevenLabs designed to reduce anxiety and confusion. The system is designed to prioritize emotional reassurance and familiarity for Alzheimers patients. How we built it The entire agentic system is built on n8n , where each capability is implemented as a modular workflow. Gemini is used as the core reasoning and retrieval model for both the workflow AI Agent as well as the ElevenLab's Agent. Patient memory documents are indexed using the Gemini File Search API , enabling fast and context-aware RAG responses. Gemini Flash was chosen for its low latency, which is critical for natural voice interactions. ElevenLabs powers the voice output. We selected a calm, warm voice and adjusted pacing to be slower and more soothing, which is important for Alzheimer’s patients. Google Calendar API tools allow the agent to retrieve and create events for reminders and daily orientation. A structured Google spreadsheet stores contact information for loved ones, making it easy for the agent to identify caregivers and close family members. A Gmail API tool allows the user to send emails by simply chatting with the agent. The workflow includes intent detection and state handling so the voice assistant can respond differently during confusion, routine questions, or emotional distress. Challenges we ran into One of the main challenges was designing responses that are emotionally safe . Alzheimer’s patients may repeat questions or express confusion, and a typical assistant response can feel cold or dismissive. We had to carefully shape prompts and retrieval logic to avoid contradiction or gaslighting. Another challenge was balancing speed and reliability . Voice interactions feel unnatural if responses are delayed, which made Gemini Flash’s fast inference especially valuable. Designing the RAG documents so they retrieved the “right kind” of memory, comforting rather than overwhelming, also required iteration. Accomplishments that we’re proud of Building a fully working RAG subagent integrated into an n8n AI workflow Successfully combining Gemini’s fast retrieval with ElevenLabs’ expressive voice synthesis for a voice-first experience Designing the system with ethical and emotional considerations , not just technical performance Creating a modular workflow that can easily be extended with more tools or safeguards What we learned This project reinforced that AI in healthcare-adjacent spaces must be designed with empathy first. We learned how powerful RAG can be when the data is deeply personal, and how much voice quality and pacing affect user trust. Gemini’s speed and flexibility made it easy to iterate on retrieval logic, while ElevenLabs showed how voice alone can significantly change the emotional tone of an interaction. What’s next for Haven Next, we want to: Add emotional state detection to automatically switch into calming or escalation modes Introduce a caregiver dashboard for safely updating memories and routines Implement emergency workflows that notify caregivers during prolonged distress Explore multilingual support so patients can interact in their native language Long term, the goal is to evolve this into a reliable, ethical cognitive support system that complements, not replaces, human caregiving. <div