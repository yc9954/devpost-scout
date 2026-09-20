---
slug: "carelink-k1pzeh"
url: "https://devpost.com/software/carelink-k1pzeh"
title: "CareLink"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1034
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "user/clinician"
  - "user/patient_family"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# CareLink

> Voice AI with RAG-powered clinical reasoning that proactively detects post-surgical complications, alerts care providers before symptoms escalate, and prevents costly hospital readmissions

[Devpost](https://devpost.com/software/carelink-k1pzeh) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[health_clinical]]
**user** [[clinician]] [[patient_family]]
**substrate** [[structured_db]] [[transcript_audio]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** claude-sdk, elasticsearch, elevenlabs, esql, express.js, html, javascript, perplexity-sonar, rag, react, tailwind-css, twilio

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for carelink

## Body

Healthcare provider-side dashboard Inspiration 1 in 5 Medicare recipients are readmitted within just a month of discharge from the hospital due to post-surgery complications - complications which would have been highly avoidable had proactive and sufficient follow-up been conducted on discharged patients. Readmissions cost the U.S. hospital system 26 billion dollars a year, exerting stress upon understaffed and busy hospital systems without the bandwidth to ensure patients get consistent care after walking through the doors of the operating room. What it does CareLink aims to take the burden off of doctors, hospital systems, and even patients, by automating the post-surgical follow-up process while keeping medical staff in the loop - resulting in safe and efficient decision-making. The platform accomplishes two main purposes: 1) Automate patient post-surgical follow-up through agentic and adaptive voice call 2) Provide hospitals and doctors with digestible patient care recommendations through RAG-powered clinical reasoning. 48 hours after a patient’s discharge date, our voice AI agent automatically calls the patient for a check-in to ask the patient about any discomfort they’ve experienced and any concerns they have. With access to the patient’s surgery information, preexisting risk factors, and medical documentation on potential surgery complications, the agent dynamically reasons about follow-up questions to extract more information from the patient and determine the possibility of major surgery complications. If the agent believes the patient may be at risk, the hospital-facing dashboard flags the patient as requiring urgent care, alerting doctors to the need for follow-up appointments - preventing escalation of the patient condition and reducing the chances of patient readmission for increasingly severe surgical complications. How we built it We built CareLink with React for the frontend, Express.js for the backend, and a demo patient database stored using Elasticsearch’s powerful vector embedding and retrieval capabilities. 1) Pre-call information retrieval: We use Perplexity API to gather contextual information from credible medical documentation (including PubMed, NCBI, and FDA publications) on the patient’s surgery and potential complications. Next, we use Elasticsearch’s Jina embedding model to convert this doc to embedding vectors for more efficient comparison with the patient’s true symptoms. 2) Automated phone call pipeline: We use the Twilio API to provide the communication infrastructure via a direct phone call 48 hours after the discharge date. We use a combination of Claude and ElevenLabs API to support dynamic, natural conversation with the patient. We leverage Claude's reasoning capabilities to generate personalized questions for the patient and use ElevenLabs for high quality text-to-speech conversion for the phone call. 3) Transcription and summarization: The agent-patient conversation is transcribed and summarized for clinician records. We compare the patient’s symptoms with the expected results retrieved using Perplexity via the vector evaluation system in Elasticsearch, allowing us to present the appropriate actionables in the hospital dashboard. 4) Hospital chatbot: On the hospital UI, we used Elastic Agent Builder via Kibana as part of Elastic Cloud. Specifically, we developed an agent that has access to customized workflows and tools to investigate specific data through semantic reasoning. The chatbot feature allows hospital clinicians to receive information about patients through retrieval-augmented generation that draws directly from patient records and call transcripts from the Elasticsearch database. 5) Clinician dashboards: We also incorporated an analytics dashboard to present various statistics about the patients and surgeries stored in the database. Finally, a full patient list allows clinicians to see individual patients data, call transcripts/summaries, and recommended actionables. In addition, they can manually initiate communication through phone call or email with the patient if needed. Challenges we ran into 1) TTS pipeline: The agent voice generated using the Twilio API for the full phone call pipeline was highly robotic. We integrated the ElevenLabs API for TTS to improve the flow of the agent’s speech; we definitely had to explore a lot of new tools to accomplish our goals for this project. 2) Performance obstacles: Our use of Elastic agents for the hospital chatbot resulted in timing bottlenecks due to the customized nature of the agent to focus on preplanning and RAG using patient information as opposed to immediate content synthesis. We restructured parts of our database pretty late into the hackathon in order to take advantage of faster ES|QL queries. 3) Multiple APIs: The integration of multiple APIs resulted in access and permission issues in the pipeline that required careful debugging to resolve. 4) Integration: Generally, connecting the various parts of the web app was difficult; we weren’t sure at first how to combine all the individual parts that everyone had worked on, but we were ultimately successful through a lot of trial and error. Accomplishments that we're proud of 1) Successfully implementing an autonomous, dynamically reasoning clinical voice AI agent 2) Integrating dynamic reasoning abilities into agent-patient calls with context retrieval through Perplexity 3) Creating a chatbot using RAG for querying patient information and data 4) Managing and updating Elastic database and agents What we learned We definitely learned a lot as a team. None of us had experience in designing and implementing agentic workflows, so diving into that process headfirst was very rewarding. We got to combine multiple state-of-the-art APIs and technologies to build an autonomous voice AI system for realistic patient follow-ups in healthcare, developing a full-stack agentic application using React and Express.js. We also began to think in a very product-design-oriented way, as we had to consider the very specific pain points of our target audience—like designing analytics dashboards with clinician UI/UX in mind and streamlining the patient and clinician experience in sensitive medical settings—which weren't necessarily pain points we'd have thought about before we started building. We found it incredibly cool to experiment with the voice AI and its capabilities; APIs are functional and applicable in ways we couldn’t have imagined, and seeing them work in action was really exciting. What's next for CareLink 1) Semantic filtering in patient dashboard: Allow for more flexible and robust search of patient cards in the patient information tab 2) Computer vision integration: Incorporate CV to analyze images in patients’ medical reports and user-provided images of their symptoms 3) Dynamic monitoring: Initiate repeated follow-ups on a timeline personalized for each patient’s medical conditions and history 4) Performance improvements: Reduce latency of voice agent reasoning in real-time calls <div