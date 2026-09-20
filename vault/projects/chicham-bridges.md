---
slug: "chicham-bridges"
url: "https://devpost.com/software/chicham-bridges"
title: "Chicham Bridges"
hackathon: "Amazon Nova AI Hackathon"
organization: "Amazon"
winner: true
words: 813
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/civic_government"
  - "domain/education"
  - "domain/security_privacy"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/geospatial"
---

# Chicham Bridges

> Voice AI bridge for Peru's indigenous teachers — translates Spanish/Quechua to Awajún using Amazon Nova, preserving language and cultural identity

[Devpost](https://devpost.com/software/chicham-bridges) · hackathon [[Amazon Nova AI Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[civic_government]] [[education]] [[security_privacy]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[geospatial]]

**stack** amazon-bedrock, amazon-ec2, amazon-nova-2-lite, amazon-nova-2-sonic, amazon-web-services, boto3, python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we faced
- what we learned
- what's next for chicham

## Body

landing Inspiration In Peru, 70,000+ Awajún indigenous people face an educational crisis. Teachers assigned to their remote Amazonian communities speak Spanish or Quechua — but not Awajún. The state even sends teachers who speak other native languages, assuming "close enough" works. It doesn't. We didn't learn this from the news. Our multidisciplinary team — educators, engineers, linguists, and social scientists — conducted field visits to Awajún communities, schools, and local government offices in the San Martín and Amazonas regions. We sat with students who couldn't understand their teachers. We spoke with teachers who wanted to connect but had no tools. We met with regional education authorities struggling with a system that fails its most vulnerable. We organized workshops with community leaders, MINEDU officials, and intercultural education experts to map the problem with real data. The numbers were stark: only 24 registered Awajún interpreters for the entire nation. Teachers cycling through communities every few years, never learning the language. Students dropping out because school feels foreign. But we also found a massive opportunity to influence change . The communities are eager. The teachers want tools. The government recognizes the gap. What's missing is the bridge — and that's what we built. The problem isn't just linguistic — it's about cultural identity . When a teacher can't speak about Nugkui (earth spirit), Etsa (sun), or the sacred ikam (forest) in the students' language, an entire worldview is lost. What it does Chicham (meaning "word/language" in Awajún) is a voice-powered AI educational assistant that bridges the gap between teachers and indigenous students: Teacher speaks in Spanish or Quechua → voice is captured and transcribed Amazon Nova 2 Lite translates using a curated Awajún knowledge base (dictionary, grammar rules, cultural context) Student receives text in Awajún with pronunciation guides and cultural notes Reverse direction — student communicates back, teacher understands Lesson generator — creates bilingual educational content integrating Awajún cosmovision Phrase book — classroom, daily, and cultural expressions with pronunciation guides How we built it Field research first — community visits, interviews with students/teachers/authorities, workshops with intercultural education experts to validate the problem and design the solution with real users Amazon Nova 2 Lite ( us.amazon.nova-2-lite-v1:0 ) on Amazon Bedrock — core translation and reasoning engine. We use few-shot prompting with linguistic context (dictionary entries, grammar rules, cultural notes) to guide accurate translations for an underrepresented language Knowledge Base — hand-curated Awajún linguistic data: 60+ dictionary entries across 7 categories, SOV grammar rules with verb conjugation patterns, classroom/daily/cultural phrases with pronunciation guides, all based on MINEDU's official Awajún educational materials (RM N° 2554-2009-ED) and validated during our field workshops Amazon Nova 2 Sonic — architecture designed for bidirectional voice streaming (Spanish speech interface for teachers) Python + Streamlit — accessible web interface with voice recording, real-time translation, lesson generation, and dictionary lookup AWS EC2 + Streamlit Cloud — deployed with HTTPS for browser microphone access Challenges we faced Awajún is severely underrepresented in AI training data. No existing translation API supports it. We solved this with a knowledge-base-augmented approach: feeding Nova 2 Lite curated linguistic data as context Nova 2 Sonic supports only 5 languages natively (EN, FR, IT, DE, ES) — not indigenous languages. We designed a hybrid architecture where Sonic handles the Spanish/Quechua voice interface and Nova 2 Lite handles the Awajún translation with cultural context Cultural sensitivity — during our field visits, community elders emphasized that translation alone isn't enough. We built cultural context features that explain the meaning beyond literal translation, helping teachers understand Awajún worldview Connectivity constraints — many Awajún communities have limited internet. We designed the knowledge base to work with minimal API calls and are exploring offline-capable versions What we learned Being there changes everything. Reading reports about indigenous education is one thing. Sitting in a classroom where a teacher and student literally cannot communicate is another. Our field visits shaped every design decision The gap between "mainstream" indigenous languages (Quechua, ~4M speakers) and smaller ones (Awajún, ~56K speakers) is enormous in terms of digital resources Few-shot prompting with curated linguistic knowledge bases can extend LLM capabilities to underrepresented languages The real problem isn't just translation — it's cultural identity preservation . Technology must respect and transmit cosmovision, not just words The communities, teachers, and authorities are ready for this solution — the demand we found during our visits was overwhelming What's next for Chicham Short term : Expand the Awajún knowledge base with community-validated content from our ongoing field workshops, plus MINEDU's 130+ educational resources Medium term : Add more Peruvian indigenous languages (Shipibo-Konibo, Asháninka, Wampís) — we're already in contact with these communities Long term : Awajún students connected with their culture stay in school longer → more access higher education → return as bilingual Awajún teachers , breaking the cycle from within. Our fieldwork confirmed: this cycle can be broken, and the communities are ready \ <div