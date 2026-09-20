---
slug: "poyovision"
url: "https://devpost.com/software/poyovision"
title: "poyo.ed"
hackathon: "HackUTD 2024: Ripple Effect"
organization: "hackutd"
winner: true
words: 534
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/education"
  - "user/educator_student"
  - "user/government_staff"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# poyo.ed

> Smart Poyo for Smarter Learning: Capture, Transcribe, Summarize.

[Devpost](https://devpost.com/software/poyovision) · hackathon [[HackUTD 2024- Ripple Effect]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]] [[education]]
**user** [[educator_student]] [[government_staff]] [[researcher]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]] [[transcript_audio]] [[video_visual]]

**stack** clerk, groq, materials, next.js, pinata, react-speech-navigation, sambanova, tailwind.css, typescript

## How they structured the write-up

- 🚀 inspiration:
- 🎉 what it does:
- 🛠️ how we built it:
- 🚧 challenges we ran into:
- 🏆 accomplishments that we're proud of:
- 📚 what we learned:
- 🔮 what's next for poyo.ed
- 💻 tech stack:

## Body

webcam + poyo = poyo.ed Live transcription and study helper during lecture Notes are compiled from the live transcription and screen captures The compiled information from a specific lecture Homepage with current courses Lectures are saved for each course 🚀 Inspiration: In modern academics, students often struggle to keep up with fast-paced lectures and large volumes of content. Briefly displayed slides and spoken details can be hard to capture, especially for auditory learners, impacting comprehension, retention, and academic performance. Our team's creativity was further sparked by a charming Poyo keychain, beloved for its delightful design. 🎉 What It Does: Real-time Speech-to-Text Transcription : Converts spoken content into accurate, searchable text during lectures. Visual Capture of Lecture Slides : Automatically processes uploaded slides or captured visuals for seamless integration into notes. Export and Note Generation : Generates structured notes that can be exported as text files or PDFs for later review. Digestable Notes: Implemented large language models (LLMs) to condense lecture content into easily understandable summaries. 🛠️ How We Built It: Frontend: Developed with Next.js for a responsive and performant user interface, styled using Tailwind CSS for sleek, modern aesthetics. Backend: Built with Node.js , leveraging scalable cloud services to process requests and manage data. Database: Implemented a SQLite database to store lecture content and user data for efficient retrieval and scalability. APIs: Integrated the SambaNova Cloud API for advanced transcription capabilities, Pinata File API for secure storage and retrieval of visual content and react-speech-navigation for real-time speech transcription. 🚧 Challenges We Ran Into: Speech-to-Text accuracy: Ensuring reliable transcription in noisy environments and with varying accents required extensive tuning and testing. Slide Capture Integration: Aligning slide visuals with transcriptions in real time presented synchronization challenges. Learning Curve: Exploring and effectively utilizing the SambaNova Cloud API and Pinata File API under time constraints. Dissecting Poyo: Retrofitting the Poyo keychain with a camera was a meticulous task. We spent considerable time carefully disassembling, equipping with the camera, and then reassembling Poyo, ensuring it maintained its charm. 🏆 Accomplishments That We're Proud Of: Successfully implemented real-time transcription and visual processing features within the hackathon timeframe. Achieved seamless integration of diverse tools and technologies for a cohesive user experience. Created an intuitive and visually appealing interface that simplifies note-taking for students. 📚 What We Learned: The importance of clear and well-structured API documentation for rapid development. Techniques for optimizing performance in real-time applications like transcription and slide processing. How to adapt to new technologies and collaborate effectively in a high-pressure environment. The importance of thorough initial planning for maintaining a flexible and extendable codebase. 🔮 What's Next for poyo.ed AI Tutoring Chat Bot: Enhance learning with a personalized assistant that can answer questions based on lecture content. Native Mobile App: Develop mobile applications to enable students to use poyo.ed on the go, with offline capabilities for transcription and note management. Multilingual Support: Expand transcription capabilities to support multiple languages and improve accessibility. Bigger Poyo: We plan to enlarge Poyo to accommodate a better camera, enhancing its image capture quality and functionality. 💻 Tech Stack: Frontend: Next.js, Typescript, TailwindCSS, Materials UI Backend: SQLite, Pinata SDK APIs/Tools: Pinata File API, SambaNova Cloud API, Clerk Auth, React Speech Navigation, Groq API <div