---
slug: "temp-031caq"
url: "https://devpost.com/software/temp-031caq"
title: "RecallMe"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 927
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# RecallMe

> A smart AI lecture chatbot that follows along in class, lets you ask questions live, gives immediate answers, and keeps track of context across lectures and uploaded recordings.

[Devpost](https://devpost.com/software/temp-031caq) · hackathon [[Cal Hacks 12.0]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
**substrate** [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** flask, letta, livekit, react, reka

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges
- accomplishments that we're proud of
- what we learned
- what's next for recallme

## Body

RecallMe lets you chat with your lecture content in real time, unique to the industry. RecallMe's video library allows users to add and store lecture context for efficient learning RecallMe Inspiration As undergrad students sitting in lecture halls with 200+ students, it becomes incredibly easy to zone out, lose track of important concepts, or feel too intimidated to ask questions in real time. We wanted to change that. RecallMe was born from the idea that learning should be active, engaging, and personalized—not passive and easily forgotten. With live transcription and real-time interaction, RecallMe keeps students focused, curious, and connected to the lecture from start to finish. Instead of waiting for the professor to finish speaking or rewatching hours of recordings later, students can now engage instantly, ask questions the moment confusion strikes, and never miss a key idea again. What it Does RecallMe captures lecture audio in real time, transcribes it instantly, and generates dynamic, structured notes that students can interact with as the lecture is happening. But it doesn’t stop there—every lecture is stored as long-term memory inside our Letta agent, meaning students can return days or even months later and ask questions about previous lectures without having to dig through hours of videos. RecallMe also supports video uploads, where a user can upload a lecture recording, have it transcribed and stored in memory, and then interact with it using a larger context window. It’s like talking to an AI that truly remembers your classes—across time, topics, and video lectures. Using our dynamic database within Letta, we can easily recall information with each video_id. How We Built It We used a variety of tools and sponsors at Calhacks to build RecallMe! With the use of Letta, Reka, and LiveKit, we created RecallMe to achieve low-latency transcription, persistent memory storage, and context-aware interaction. LiveKit handles real-time audio streaming from the lecture, where audio is segmented into PCM chunks and streamed to our backend. These chunks are asynchronously processed and forwarded to two separate Letta agents via API calls. The first agent performs instant summarization and lecture note generation using its reasoning models, while the second agent is dedicated to long-term memory persistence. This memory agent stores each chunk’s transcription into structured core memory blocks, indexed by unique lecture or video IDs to emulate scalable vectorized memory retrieval. For non-live content, such as uploaded lecture videos, we use Reka’s speech-to-text API to batch-process the video stream into high-accuracy transcripts. Since Reka and Letta do not have native interoperability, we built a custom middleware pipeline to transform Reka’s output into Letta-compatible memory schemas before pushing them into the same memory graph used for live sessions. All stored memory is queryable using semantic retrieval, meaning a user can ask context-dependent questions and the system fetches the relevant lecture fragments from long-term storage. The final architecture enables seamless interaction across live lectures, stored sessions, and uploaded videos—allowing users to converse with an AI that maintains temporal continuity, lecture-specific context, and cross-session recall. Challenges None of us had ever used AI agents before, and definitely not all three platforms—Letta, Reka, and LiveKit—at once. Our first challenge was figuring out how to structure memory inside Letta so that lecture information could be stored, retrieved, and referenced over time. Next, we had to integrate Reka and Letta, despite the fact that no direct integration exists. We built a workaround that allowed us to transcribe videos with Reka and send that data into Letta’s memory. LiveKit brought its own challenges, as we had to process audio in real-time chunks and make sure the transcription was fast and accurate enough to be useful during live lectures. But the hardest part was creating one seamless system that could handle live transcription, memory storage, interactive querying, and video processing—while making it feel natural and effortless to the user. Accomplishments that we're proud of We’re proud of our hard work in combining frameworks from three different sponsors into a unified platform, leveraging AI agents, speech-to-text models, and real-time chatbot functionality under a strict development timeline. We formed strong relationships with peers, mentors, and sponsor representatives, gaining valuable insights into agentic technology, startup ecosystems, and the growing scope for innovation in today’s AI-driven world. What we learned We learned how to integrate AI agents and speech-to-text models to develop a real-time, context-aware chatbot capable of processing and responding to live lecture content. Throughout the process, we gained hands-on experience working with three complex sponsor technologies—Letta, LiveKit, and Reka—and learned how to design effective pipelines that connect them seamlessly. We also strengthened our skills in asynchronous event handling, API orchestration, and real-time data streaming, while managing development under a tight hackathon timeline. Beyond the technical side, we learned how to collaborate efficiently under pressure, divide tasks strategically, and iterate quickly to transform an ambitious concept into a functional prototype. What's next for RecallMe Looking ahead, we aim to expand our platform’s intelligence, scalability, and accessibility: Multi-Modal Agent for Interactive Quizzes: We plan to integrate a multi-modal AI agent capable of generating real-time, interactive quizzes based on lecture content, helping students actively test their understanding. Vectorized Database for Efficient Querying: Implementing a vector database will enable faster and more accurate semantic search, improving how the chatbot retrieves and relates lecture information. Multilingual Transcription and Support: To make our platform accessible to a broader audience, we plan to introduce multilingual transcription and translation, allowing students worldwide to benefit from localized lecture understanding. These advancements will strengthen the platform’s educational value and push it closer to a fully intelligent, globally accessible lecture companion. <div