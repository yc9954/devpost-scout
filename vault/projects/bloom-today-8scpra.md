---
slug: "bloom-today-8scpra"
url: "https://devpost.com/software/bloom-today-8scpra"
title: "Bloom Today"
hackathon: "Mind the Product presents World Product Day: Everyone Ships Now"
organization: "Mind the Product"
winner: true
words: 1085
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "domain/security_privacy"
  - "user/educator_student"
  - "user/legal_professional"
  - "substrate/transcript_audio"
---

# Bloom Today

> Because no mom should have to heal alone. Bloom Today is a postpartum emotional support platform that gives every new mother a personalized AI companion she can talk to anytime, about anything.

[Devpost](https://devpost.com/software/bloom-today-8scpra) · hackathon [[Mind the Product presents World Product Day- Everyone Ships Now]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[education]] [[health_clinical]] [[mental_health]] [[security_privacy]]
**user** [[educator_student]] [[legal_professional]]
**substrate** [[transcript_audio]]
  <sub>weak: video_visual</sub>

**stack** amazon-web-services, aurora, gemini, novus, react, talkinghead, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for bloom today

## Body

Options video call with AI companion daily check landing page bloom note mood scores AWS Aurora DB usage Architecture diagram novus dashboard Inspiration I am the youngest in my family, the only son, born years after my two older sisters. By the time I was growing up, my sisters were already starting families of their own. I watched them give everything to their children, my two nephews, whom I absolutely adore, but I also watched them go through something nobody in our family fully understood. After their pregnancies, both my sisters quietly struggled. One would cry for no reason she could explain. The other stopped sleeping, stopped eating, stopped being herself, and nobody knew what to say. Our family loved them, but love without understanding is not always enough. That curiosity stayed with me. I started reading, not as a student, but as a brother who wanted to understand. I learned that postpartum depression is not just "feeling sad." It is a clinically recognized medical condition that affects up to 1 in 5 mothers, and yet many suffer in silence because society has conditioned women to suppress their pain, smile through exhaustion, and treat motherhood as something that should come naturally. Research consistently shows that one of the most impactful supports for postpartum mental health is having someone to talk to: someone who listens, validates, and does not judge. That insight became the foundation of Bloom Today. What it does Bloom Today is built around a personalized AI companion that a mother can call in real time. It greets her by name, remembers context from past conversations, listens with warmth, and responds with care. A mother can name her companion, choose its voice, customize its personality, and give it specific instructions. She shapes who she talks to, not the other way around. Using the Gemini Live API with native audio streaming, mothers can have natural conversational calls with their companion. The companion appears as a 3D animated avatar powered by Three.js and the TalkingHead library, with lip-sync and contextual gestures like nodding during heavy moments or smiling during lighter ones. Bloom Today also lets a mother connect her therapist through a secure key. The therapist can view a dedicated dashboard with Gemini-powered conversation analysis, send notes to the mother, and provide instructions that shape how the AI companion responds. A mother can also connect a trusted person through a shareable key. That person gets a simple dashboard with a status label, a plain-language summary, and gentle suggestions like "Bring her favorite tea tonight" or "Ask her about the baby's feeding, she mentioned it was stressful." Every conversation is analyzed by Gemini to extract 8 signal scores: mood, energy, sleep, stress, support, self-kindness, coping, and bonding. Bloom Today also identifies themes, tracks mood direction, and generates personalized quick tips and YouTube resource recommendations without requiring forms or questionnaires. The Bloom Score is a gamified engagement score that measures how consistently a mother is seeking support, not her mental state. How I built it I built Bloom Today around a companion pipeline. During onboarding, the mother names her companion, chooses a voice, optionally writes personality instructions, and selects a 3D avatar. When a call starts, the frontend opens a WebSocket to the Gemini Live API with a system instruction that includes the companion name, personality, therapist guidance, and memories from past conversations. A custom recorder captures 16kHz PCM audio from the microphone and streams it as base64 chunks. Incoming audio is decoded and played through the Web Audio API. A TalkingHead instance renders a Three.js ReadyPlayerMe avatar. A procedural viseme engine syncs mouth movement with AI audio, while a gesture mapper triggers contextual expressions from transcript text. Server-side voice activity detection handles interruptions. When the user speaks over the AI, queued audio is flushed, avatar animation resets, and the model responds to the latest user input. Transcripts are saved to PostgreSQL. On call end, Gemini analyzes the conversation with structured output to produce signal scores, risk assessment, therapist notes, and trusted-person guidance. Challenges I ran into I spent significant time researching what actually matters for postpartum mental health: which signals are meaningful, how to present emotional data without making it feel like a medical report, and how to keep the interface light enough that a tired, overwhelmed mother would actually want to open it. I studied scales like the PHQ-9 and the Edinburgh Postnatal Depression Scale to understand what signals to track, then translated those ideas into warm, non-intimidating language. Building three different dashboard views from the same conversation data required a lot of iteration on both the Gemini prompts and the frontend presentation. The mom sees encouragement, the therapist sees structured analysis, and the trusted person sees simple actionable guidance. Accomplishments that I'm proud of A 3D companion that feels present: Procedural lip-sync and contextual gestures make the companion feel alive during a conversation. Three dashboards from one conversation: Bloom Today generates a warm reflection for the mom, structured analysis for the therapist, and a plain-language action guide for the trusted person. The trusted person system: This feature helps people who care understand what is going on and exactly how they can help, without guilt or awkwardness. Full companion personalization: Mothers can name, voice, and instruct their own companion while therapists can layer guidance on top. What I learned Postpartum depression is not "baby blues." It is a condition that deserves the same engineering rigor we give to any health problem. Building Bloom Today pushed me to understand the PHQ-9, the Edinburgh Postnatal Depression Scale, risk stratification, and the challenge of translating clinical concepts into language a tired, overwhelmed mother could actually find comforting. The Gemini Live API is powerful for real-time conversational agents, but it requires careful engineering around streaming, turn management, interruptions, and the gap between "model done generating" and "audio done playing." Structured output from Gemini is also a game-changer for building dashboards from unstructured conversations. Combining response schemas with post-processing normalization gives reliable typed data from complex emotional analysis prompts. Most importantly, design matters as much as engineering when the user is vulnerable. Every color choice, word, and animation needs to feel warm, safe, and non-intimidating. What's next for Bloom Today Persistent memory across calls: Use vector embeddings so the companion can naturally reference things shared weeks ago. Mood journaling: Add a voice-first journal that captures daily reflections and feeds the insight engine. Native mobile app: Wrap the PWA in a React Native shell for push notifications and background audio. ``` <div