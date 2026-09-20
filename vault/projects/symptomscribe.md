---
slug: "symptomscribe"
url: "https://devpost.com/software/symptomscribe"
title: "SymptomScribe"
hackathon: "Build your Flutter Butler with Serverpod"
organization: "serverpod"
winner: true
words: 724
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/developer"
---

# SymptomScribe

> Your personal health documentation butler. Describe symptoms in plain words, get structured FHIR records any medical system can read.

[Devpost](https://devpost.com/software/symptomscribe) · hackathon [[Build your Flutter Butler with Serverpod]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[developer]]

**stack** flutter, genui, mistral, postgresql, serverpod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for symptomscribe

## Body

Inspiration I've been building MedKid , a mobile PHR app for families to store and share their children's health records. The dream was always to support a broad range of conditions—including rare diseases where tracking specific symptoms can be critical for diagnosis and treatment. The problem was configuration. Supporting a new condition meant manually defining what to track: which symptoms, what measurements, what scales to use. That's fine when developers do it, but completely impractical for a parent who just learned their child has a condition with a name they can't pronounce. The app needed to be flexible enough to track anything, but the setup complexity was a barrier. I wondered if AI could bridge that gap. Instead of pre-building trackers for every possible condition, what if the app could listen to how parents naturally describe what they're seeing and create the right tracking structure on the fly? What it does SymptomScribe lets you describe health symptoms naturally—the way you'd tell a friend—and transforms them into structured, trackable data. Say "I've been getting headaches after screen time" and the AI creates a personalized tracking template on the spot, informed by medical standards but designed around your words. The app uses a chat interface where interactive cards appear inline during the conversation. When the AI suggests a template or shows a form to fill out, it's right there in the flow—no context switching. All observations are stored as FHIR-compliant resources, ready to share with healthcare providers when needed. How we built it Flutter Web for the frontend, Serverpod for the backend. PostgreSQL with pgvector handles semantic search—matching what you say now to templates you've created before, even if you phrase things differently. Mistral powers the AI side. The architecture separates the "orchestrator" (conversation flow and task states) from the "medical agent" (tools for searching templates, proposing schemas, interpreting qualifiers). LOINC and SNOMED medical standards provide context for the AI without ever being exposed to users. Everything is modeled as FHIR resources under the hood, which means the data is structured in a way that could be shared with healthcare providers or other apps. Challenges we ran into The hardest part was deciding when to match an existing template versus create a new one. "Headache" and "migraine"—same thing or different? There's no universal answer, so I had to build in user confirmation for edge cases and let the library evolve based on how each family actually uses it. Streaming was tricky too. I wanted the UI cards to show up during the AI response, not after it finishes. That required some custom work to handle text and structured components arriving interleaved. Finding the right level of AI autonomy took real iteration. Early versions gave the agent too much conversational freedom—users would ask to log a headache and end up in a meandering discussion. But locking it down with rigid conversation flows felt like the chatbots of 2018. The solution was architectural: the orchestrator gives the AI clear goals and structured decision points—like human-in-the-loop confirmations—while letting the medical agent figure out how to accomplish each step. Structure where it matters, flexibility where it helps. Accomplishments that we're proud of Building a system where medical standards (FHIR, LOINC, SNOMED) inform the AI without ever being exposed to users. You get the benefits of structured healthcare data while talking like a normal person. The streaming architecture for interleaved text and UI components turned out really well. Cards appear naturally during the conversation, making the whole experience feel responsive and cohesive. The human-in-the-loop confirmation flow strikes a good balance—the AI proposes, but users always have the final say on what gets created. What we learned Healthcare data standards are fascinating and frustrating in equal measure. FHIR, LOINC, SNOMED—these systems exist so healthcare software can talk to each other, but they're absolutely not designed for end users. Nobody wants to browse a list of LOINC codes to log a headache. The trick was using them as invisible scaffolding. Fully autonomous AI template creation doesn't work. It sounds good in theory, but in practice you end up with duplicate templates, weird interpretations, and users who don't trust the system. Adding a confirmation step—where the AI proposes and the user approves—made a huge difference. What's next for SymptomScribe Integration into the MedKid app as the natural language input layer for health tracking <div