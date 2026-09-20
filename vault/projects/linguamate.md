---
slug: "linguamate"
url: "https://devpost.com/software/linguamate"
title: "Lingomate"
hackathon: "EducateHacks 2024"
organization: "EducateHacks"
winner: true
words: 528
team_size: 2
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/education"
  - "user/educator_student"
---

# Lingomate

> Lingomate allows students to master new languages through active dialogue and personalized feedback while providing teachers with unparalleled visibility into each student's learning journey.

[Devpost](https://devpost.com/software/linguamate) · hackathon [[EducateHacks 2024]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[education]]
**user** [[educator_student]]
  <sub>weak: transcript_audio, video_visual</sub>

**stack** dash, fastapi, google-web-speech-api, openai, python, react, typescript

## Body

Screenshot of lingomate Inspiration The inspiration for Lingomate came from recognizing the gap in language learning platforms, particularly in the area of speaking practice. From my personal experience living in Germany and trying to learn German, my friend and I struggle with speaking due to limited opportunities for practice and feedback. In addition, both us and our teacher are unaware of our speaking issue. Hence I aimed to create a solution that empowers learners to practice speaking anytime, anywhere, while receiving instant feedback to accelerate their learning process. In addition, the insights from the practice can be translated into the classroom where the teacher know what is our issue and helps us from there. What it does Lingomate allows students to engage in speaking exercises in their target language and receive immediate feedback on grammar and appropriateness. It emphasizes areas where they can improve by allowing retries and fostering learning through repetition and correction. For teachers, Lingomate offers tools to track student progress, identify common areas of difficulty, and provide targeted support to students who need it most. How we built it Lingomate was developed using a combination of advanced language learning models and speech recognition technology. The backend, built with FastAPI, handles audio processing and interaction with language models. The front end, developed using React, provides an intuitive interface for students and teachers. Feedback on grammar and appropriateness is generated through integration with OpenAI's Gpt 3.5, offering precise and actionable insights. Also with the time left I created a dashboard where teachers can view insights based on the speaking practice, find where the students lack and potentially help them. Challenges we ran into One of the main challenges was ensuring accurate speech-to-text transcription across various languages and accents. After testing some APIs, eventually google speech to text does the job. Additionally, providing meaningful feedback on grammar and appropriateness required fine-tuning the language models and prompt engineering to understand the context of spoken responses accurately. While the quality of feedback may not be the best now, it still does the job for this hackathon. Accomplishments that we're proud of We are proud of developing a platform and a dashboard to showcase the overall idea. Given the limited time, I was able to quickly develop the student practice module and dashboard to showcase my overall idea. Even though it is buggy and have issues, it overall prove across the point I want to show. What we learned Throughout the development of Lingomate, I was able to learn how LLM works and the power of speech recognition technologies. Also I was able to explore the cool features of dash to make graphs quickly to showcase the teacher dashboard. What's next for Linguamate Looking ahead, if I can get some recognition, I am looking forward to connecting with like-minded people to bring this idea forward. I feel that unlike other language learning app, this idea of lingomate with LLM and AI can change classroom education and allow students to take charge of their learning further. In addition, I am looking to add features like a pronunciation analyser or add the LLM feature into the dashboard which is hard coded currently <div