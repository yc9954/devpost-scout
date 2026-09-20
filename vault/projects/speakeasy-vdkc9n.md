---
slug: "speakeasy-vdkc9n"
url: "https://devpost.com/software/speakeasy-vdkc9n"
title: "SpeakEasy"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 784
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/labor_employment"
  - "substrate/sensor_telemetry"
  - "substrate/transcript_audio"
---

# SpeakEasy

> AI-powered interview practice tool that helps job seekers master behavioral questions through video-based practice. It delivers real-time feedback on what you say & how you say it, so you can improve

[Devpost](https://devpost.com/software/speakeasy-vdkc9n) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
  <sub>weak: benchmark_measured</sub>
**domain** [[labor_employment]]
**substrate** [[sensor_telemetry]] [[transcript_audio]]
  <sub>weak: geospatial</sub>

**stack** express.js, javascript, node.js, postgresql, python

## Body

PROBLEM : Tons of recruiter-facing video behavioural interview analysis tools, lacking applicant-focused solutions. The market for video behavioral interview analysis is dominated by enterprise-focused platforms such as HireVue, Talview, Modern Hire, MyInterview, InterviewStream, Jobma, VidCruiter, Hireflix, and KABI/INVIEWS. These solutions primarily serve recruiters and HR teams, offering automated screening, AI-driven scoring, and predictive analytics to determine job fit to streamline hiring workflows Applicants only experience these tools when interviewing, not as practice Often job-specific, not generalizing to common behavioural questions found in majority of interview processes Often ridiculed for bias based on identity, with no opportunity for applicants to have a fair chance to improve their AI scoring The few existing applicant-facing “practice-interview” products focus on coaching/communication strategies or basic transcript analysis, not real-time verbal & non-verbal analytics SOLUTION : All-encompassing behavioural interview practice tool empowering job seekers to practice common behavioural interview topics, gain real-time AI-powered scoring, and act upon actionable feedback. HOW WE BUILD : We utilized several AI models to parse the interview video, analyzing it and providing users with feedback on their performance. The analysis is generally composed of verbal & non-verbal analysis. Onboarding : The user is introduced to our platform with a choice of up to 3 out of the 6 most common behavioural interview topics to practice on. From there, an overview discusses how the platform is structured & the type of feedback they will recieve Initial prompting : Before calling Martian Learning's LLM API prompts to analyze the candidate's responses, we receive from the user specific subtopics they want to get practice on (e.g. building trust is one subtopic of leadership), along with the number of questions, length of prep time, and length of response time per question. With these subtopics, we dynamically split them across the total number of questions as equal as possible. With these subtopics & the number of desired questions, Martian Learning's versatile chat completions API is utilized with a carefully crafted prompt (implementing both system & user instructions to maximize clarity) to create concise, 1-sentence interview-mimicking questions that embody the corresponding subtopic(s). Transcription : Now with the user's response to each question, it is passed into Assembly AI to transcribe the text & to intentionally consider/include filler words in the transcript. Then, our algorithm creates 2 cleansed versions of the transcript (one with these intentionally included filler words & one without using an extensive filler word respository - to remove noise for prompts not related to filler words/vocab). The cleansing process includes removing extra whitespace, capitalization, and unwanted punctuation Routing : With these 2 transcripts along with the user's video file (uploaded to Google Firebase ), the appropriate resources are spread among the various AI models used to collect metrics & actionable feedback on verbal & nonverbal skills Verbal part : Our system will evaluate their speech content by taking into consideration the relationship between their response and the question + its correlated subtopic(s). The verbal part is broken down into 5 subscores: Relevance, Clarity/Structure (STARR), Insight Depth/Quality, Vocabulary, and Filler Words. Specifically, we used Martian Learning's versatile chat completions API to leverage gpt-4.1-nano for identifying strengths & weaknesses in the candidate's response's relevance to each question, structure (STARR format) & clarity/cohesion, depth/quality of insights, and complexity of vocabulary. We initially experimented with Anthropic Messages but found greater success using OpenAI chat completions after running several benchmarks & testing each service on various user flows. The prompts are again crafted considering both the model's instructions & user's instructions, using concise metric-driven wording to clearly communicate the desired output & format. After receiving the response, it undergoes rigorous validation testing, including checking that positive feedback is indeed positive (avoids any negative terminology, meets character requirements, that each feedback point is separated by semi-colons, scoring is numeric, and only 1 pro and con is given for each verbal criteria; if this is not passed, it will redo the prompt until it passes validation The vocab & filler words are scored using en-core-web NLP model via FastAPI to integrate python programming in our system. It tokenizes the transcript, extracts the frequency & complexity of each word, and undergoes a custom function to determine the percentage score assigned to vocab complexity & filler word minimalism. Non-verbal part : the non-language aspects, like body movement, hand gestures, and facial expression, that the user performs. We used three models from MediaPipe from Google, by calling them to get the specific body position data, and developing&testing our algorithms and standard to parse that data into actual movement degrees and feedback. From there, we also got specific scores for overall nonverbal performance and its 6 sub-standards: Facial Expression, Eye Movement, Language Pausing, Screen Spatial Distribution, and Hand Gesture. <div