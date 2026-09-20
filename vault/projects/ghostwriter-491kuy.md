---
slug: "ghostwriter-491kuy"
url: "https://devpost.com/software/ghostwriter-491kuy"
title: "GhostWriter"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 706
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# GhostWriter

> your silent partner in progress

[Devpost](https://devpost.com/software/ghostwriter-491kuy) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[document_pdf]] [[sensor_telemetry]] [[structured_db]] [[transcript_audio]]

**stack** chroma, deepgram, gemini, groq, llama, python, react, reflex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for ghostwriter

## Body

Our system design Product page Inspiration Introducing Ghostwriter: Your silent partner in progress. Ever been in a class where resources are so hard to come by, you find yourself practically living at office hours? As teaching assistants on increasingly short-handed course staffs , it can be difficult to keep up with student demands while making long-lasting improvements to your favorite courses. Imagine effortlessly improving your course materials as you interact with students during office hours. Ghostwriter listens intelligently to these conversations , capturing valuable insights and automatically updating your notes and class documentation. No more tedious post-session revisions or forgotten improvement ideas. Instead, you can really focus on helping your students in the moment . Ghostwriter is your silent partner in educational excellence, turning every interaction into an opportunity for long-term improvement. It's the invisible presence that delivers visible results, making continuous refinement effortless and impactful. With Ghostwriter, you're not just tutoring or bug-bashing - you're evolving your content with every conversation . What it does Ghostwriter hosts your class resources, and supports searching across them in many ways (by metadata, semantically by content). It allows adding, deleting, and rendering markdown notes. However, Ghostwriter's core feature is in its recording capabilities. The record button starts a writing session. As you speak, Ghostwriter will transcribe and digest your speech, decide whether it's worth adding to your notes, and if so, navigate to the appropriate document and insert them at a line-by-line granularity in your notes, integrating seamlessly with your current formatting. How we built it We used Reflex to build the app full-stack in Python, and support the various note-management features including addition, deleting, selecting, and rendering. As notes are added to the application database, they are also summarized and then embedded by Gemini 1.5 Flash-8B before being added to ChromaDB with a shared key. Our semantic search is also powered by Gemini-embedding and ChromaDB. The recording feature is powered by Deepgram's threaded live-audio transcription API. The text is processed live by Gemini, and chunks are sent to ChromaDB for queries. Distance metrics are used as thresholds to not create notes, add to an existing note, or create a new note. In the latter two cases, llama3-70b-8192 is run through Groq to write on our (existing) documents. It does this through a RAG on our docs, as well as some prompt-engineering. To make insertion granular we add unique tokens to identify candidate insertion-points throughout our original text. We then structurally generate the desired markdown, as well as the desired point of insertion, and render the changes live to the user. Challenges we ran into Using Deepgram and live-generation required a lot of tasks to run concurrently, without blocking UI interactivity. We had some trouble reconciling the requirements posed by Deepgram and Reflex on how these were handled, and required us redesign the backend a few times. Generation was also rather difficult, as text would come out with irrelevant vestiges and explanations. It took a lot of trial and error through prompting and other tweaks to the generation calls and structure to get our required outputs. Accomplishments that we're proud of Our whole live note-generation pipeline! From audio transcription process to the granular retrieval-augmented structured generation process. Spinning up a full-stack application using Reflex (especially the frontend, as two backend engineers) We were also able to set up a few tools to push dummy data into various points of our process, which made debugging much, much easier. What's next for GhostWriter Ghostwriter can work on the student-side as well, allowing a voice-interface to improving your own class notes, perhaps as a companion during lecture. We find Ghostwriter's note identification and improvement process very useful ourselves. On the teaching end, we hope GhostWriter will continue to grow into a well-rounded platform for educators on all ends. We envision that office hour questions and engagement going through our platform can be aggregated to improve course planning to better fit students' needs. Ghostwriter's potential doesn't stop at education. In the software world, where companies like AWS and Databricks struggle with complex documentation and enormous solutions teams, Ghostwriter shines. It transforms customer support calls into documentation gold, organizing and structuring information seamlessly. This means fewer repetitive calls and more self-sufficient users! <div