---
slug: "readmeplease-ai"
url: "https://devpost.com/software/readmeplease-ai"
title: "READMEplease.ai"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 439
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# READMEplease.ai

> READMEplease.ai: Effortlessly generate README.md files for your projects with embedded text and relevant screenshots from demo videos and GitHub repositories.

[Devpost](https://devpost.com/software/readmeplease-ai) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[code_repository]] [[document_pdf]] [[transcript_audio]] [[video_visual]]

**stack** amazon-web-services, flask, githubapi, openaiapi, python, s3

## How they structured the write-up

- 🌟 about the project
- 🌈 inspiration
- 🛠 how we built it
- 🎓 what we learned
- 🚧 challenges we faced
- 🚀 the future

## Body

Instructions Input fields Generated README markdown READMEplease.ai: Project Story 🌟 About the Project READMEplease.ai was born from a simple yet powerful idea: to simplify the documentation process for developers, researchers, and content creators. Whether you're analyzing a video for key moments or curating information from a GitHub repository, generating clear and concise Markdown documentation often requires a lot of manual effort. This project seeks to eliminate those hurdles by automating the process and embedding relevant content like screenshots and transcriptions directly into Markdown files. 🌈 Inspiration The inspiration for this project came from the stack for personal projects on my Github that does not have a README.md file as me and lot of my friends do not like writing. As developers, we often find ourselves juggling between video tutorials, code repositories, and project updates—each requiring detailed documentation. The idea of automating this tedious process sparked the creation of READMEplease.ai, making documentation smarter and more accessible. 🛠 How We Built It The project leverages a combination of cutting-edge technologies to deliver its functionality: OpenAI Whisper API : For accurate transcription of audio from videos, with timestamped text. FFmpeg & OpenCV : For video processing, including extracting audio and generating screenshots. Flask : The backbone of the application, powering the server-side logic and APIs. Markdown Templates : For embedding transcriptions and screenshots into structured, user-friendly documents. GitHub Integration : To process repositories and extract README data. AWS S3 bucket : S3 was used to store the screenshots on the cloud. 🎓 What We Learned Throughout the development journey, the project team learned: The intricacies of processing large video files efficiently and handling edge cases like variable frame rates. The power of APIs like OpenAI Whisper in simplifying complex tasks like speech-to-text conversion. Challenges in synchronizing multiple tools and technologies into a cohesive application. The importance of user-centered design to ensure the final output meets the practical needs of diverse users. 🚧 Challenges We Faced Performance Optimization : Processing large video files while maintaining a responsive application was a significant challenge. Implementing asynchronous processing helped mitigate this. Keyword Detection : Achieving precise word-boundary-aware matching required fine-tuning the transcription outputs. Cross-Platform Compatibility : Ensuring the application ran consistently across different operating systems required extensive testing. 🚀 The Future This project represents the foundation for a tool that has the potential to transform how we approach documentation. With features like multilingual support, real-time transcription, and enhanced repository integration, READMEplease.ai is poised to become an indispensable tool for anyone looking to streamline their workflow. We hope this project inspires others to innovate and build solutions that simplify complex processes while delivering exceptional value. 😊 <div