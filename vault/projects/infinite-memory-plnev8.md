---
slug: "infinite-memory-plnev8"
url: "https://devpost.com/software/infinite-memory-plnev8"
title: "Infinite Memory"
hackathon: "AWS Presents: Breaking Barriers Virtual Challenge"
organization: "Amazon"
winner: true
words: 1281
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "domain/finance_payments"
  - "domain/health_clinical"
  - "domain/housing_homeless"
  - "domain/mental_health"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# Infinite Memory

> Never Forget Again

[Devpost](https://devpost.com/software/infinite-memory-plnev8) · hackathon [[AWS Presents- Breaking Barriers Virtual Challenge]]

## Facets

**mechanism** [[graph_reasoning]] [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]] [[elder_child_care]] [[finance_payments]] [[health_clinical]] [[housing_homeless]] [[mental_health]]
**user** [[patient_family]]
**substrate** [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** amazon-web-services, anthropic-claude-4, aws-bedrock, aws-kendra, aws-neptune, elevenlabs-scribe, elevenlabs-tts, google-calendar-api, langchain, pyannote-speaker-diarization, silero-vad

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for infinite memory

## Body

Inspiration The inspiration for INFINITE-MEMORY comes from the profound and deeply personal challenges faced by individuals with dementia and their loved ones. Memory loss isn't just about forgetting keys or appointments; it's a gradual erosion of context, conversation, and connection. Existing digital tools often feel like generic task managers, failing to capture the nuances of daily life. We were inspired to build something more—a true cognitive companion that could act as a seamless, always-on extension of personal memory, providing not just reminders, but genuine, context-aware support to reduce anxiety and foster independence. What it does INFINITE-MEMORY is a full-stack AI cognitive companion that creates a "cognitive safety net" for its users. For the Patient: It's an always-on assistant that listens to their conversations, identifies who is speaking, and automatically builds a searchable, multimodal memory bank. The patient can then ask questions in natural language (via text or voice) to recall information like "What did my daughter say yesterday?" or "Show me my new medication." The AI can also take action on their behalf, such as adding appointments to their Google Calendar. For the Caregiver: It's a comprehensive dashboard that provides peace of mind. Caregivers can securely monitor a patient's memory trends through an analytics dashboard, review conversations, and receive proactive alerts for concerning events. Most importantly, they can add tasks and reminders (e.g., "Take pills at 9 AM") directly into the AI's awareness, closing the loop between proactive care and passive monitoring. How we built it We built INFINITE-MEMORY on a robust, multi-tenant, cloud-native architecture designed for scalability and intelligence, with a Python-based stack. Backend: A FastAPI server acts as the central nervous system, orchestrating all the services. Frontend: A user-friendly web application built with Streamlit provides distinct, secure interfaces for both patients and caregivers. The AI Brain (AWS Bedrock & LangChain): We used LangChain to create a tool-using agent. The agent's reasoning is powered by Anthropic's Claude 3 models on Amazon Bedrock . We use the powerful Opus model for complex analysis (like understanding images) and the fast Haiku model for conversational responses and agentic decisions. The Memory System (A Multi-Database Approach): Amazon Kendra: Serves as our long-term semantic memory. All conversations and image descriptions are indexed here, allowing for powerful, meaning-based search. Amazon Neptune: Functions as our factual, relational memory. This graph database stores the relationships between entities (e.g., (Dr. Smith) -[PRESCRIBED]-> (Advil) ), enabling instant, precise answers. Amazon DynamoDB: Acts as our high-speed operational database. We use it to manage our two most dynamic datasets: the global Speaker Knowledge Base (with voiceprint embeddings) and the Caregiver Task List . Amazon S3: Provides secure, durable storage for all visual memories (images). The Senses (Voice & Vision): Voice Activity Detection (VAD): A PyTorch model runs on the edge (in the browser) to detect speech privately. Transcription & Speech (TTS): The ElevenLabs API provides best-in-class, natural-sounding speech for both transcription and generating responses. Speaker Recognition: We use an open-source pyannote/wespeaker model to generate mathematical "voiceprints" from audio, allowing us to identify and track different speakers over time. Challenges we ran into Dependency Hell: Integrating a complex stack of AI/ML libraries ( langchain , pytorch , pyannote , boto3 ) created significant dependency conflicts, especially around numpy . We had to carefully manage our pyproject.toml file and installation order to find a stable resolution. Real-time Event Loops ( asyncio ): Mixing the asynchronous world of FastAPI with the synchronous code of libraries like gremlin_python (for Neptune) and LangChain's agent executor caused RuntimeError: Cannot run the event loop while another loop is running . The solution was to wrap all synchronous, blocking calls in FastAPI's run_in_threadpool , which isolates them from the main server loop. Cloud-to-Local Connectivity: Connecting our local development machine to a private AWS Neptune database was a major hurdle. We solved this by implementing a standard and secure industry pattern: creating an EC2 bastion host and using an SSH tunnel to forward the database port to our local machine. Prompt Engineering for Persona: Getting the AI to stop sounding like a robotic summarizer ("Based on the context...") was a significant challenge. It required multiple iterations of advanced prompt engineering to create a forceful "persona" (Kai, the AI companion) with strict rules about speaking in the first person, which finally achieved the desired natural, conversational tone. Accomplishments that we're proud of Global Speaker Diarization: This is our most sophisticated feature. Instead of just knowing "Speaker A" and "Speaker B" in one conversation, our system creates persistent voiceprints and clusters them over time in DynamoDB. This allows the AI to truly learn and recognize who the important people in a user's life are, which is a massive leap in contextual understanding. True Multimodal, Multi-Database RAG: We successfully integrated four different AWS database services (Kendra, Neptune, DynamoDB, S3), each for a specific purpose. Our LangChain agent can retrieve context from all of them simultaneously—semantic memories, factual relationships, and caregiver-defined tasks—to form a single, comprehensive answer. Full-Stack, End-to-End Integration: We didn't just build a backend; we built a complete, working application. Integrating the live VAD, the asynchronous backend processing, and the reactive Streamlit UI into a single, seamless experience was a major accomplishment. Secure Multi-Tenancy: From the start, we built the system to be multi-tenant. All data—from memories in Kendra to voiceprints in DynamoDB to images in S3—is partitioned by user_id , ensuring a secure and private experience for every user. What we learned The Right Tool for the Job: We learned that a single database is rarely the answer for a complex AI application. Using a purpose-built database for each data type (vectors, graphs, key-value) leads to a much more powerful and efficient system. The Importance of Personas: We learned that for conversational AI, simply instructing a model to be "helpful" is not enough. You must give it a concrete persona and a strict set of behavioral rules to achieve a truly natural and non-robotic user experience. Async is Hard: Integrating various libraries in an asynchronous web framework is challenging. We gained deep experience in debugging event loop conflicts and using tools like run_in_threadpool to correctly manage synchronous and asynchronous code. The Cloud is a System: We learned to think of AWS not as individual services, but as a connected ecosystem. The real power came from chaining them together: S3 for storage, Bedrock for analysis, and Kendra/Neptune/DynamoDB for different forms of memory. What's next for Infinite Memory The current application is a powerful and stable foundation, but the vision for INFINITE-MEMORY is just beginning. Proactive Reminders & Alerts: The next logical step is to move from reactive answers to proactive assistance. The system could use the task list to initiate conversations, e.g., "Good morning, John. Just a reminder that you have a task to take your heart medication at 9 AM." LLM-Powered Speaker Labeling: We have the infrastructure for voiceprints. The next step is to use the LLM to label these clusters. After a few conversations with speaker_3 , the AI could be prompted: "Based on these conversations, who is speaker_3 ?" and it might answer "daughter, Jane." This would allow the AI to say, "I remember when your daughter Jane called..." Edge AI Deployment: For ultimate privacy and low latency, key models could be moved to the edge. The wespeaker model for voiceprints is small enough to run on a powerful mobile device or a dedicated home hub, sending only the anonymized embedding to the cloud. Expanding Tools: We've proven the tool-calling concept with Google Calendar. We can expand this to include tools for controlling smart home devices ("Turn on the lights"), sending text messages, or starting a music playlist, making Kai a true central hub for the user's digital life. <div