---
slug: "insight-ai"
url: "https://devpost.com/software/insight-ai"
title: "InSightAI"
hackathon: "HackMIT 2023"
organization: "HackMIT"
winner: true
words: 419
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "user/educator_student"
  - "substrate/transcript_audio"
  - "substrate/video_visual"
---

# InSightAI

> Empowering anyone, anywhere to seamlessly follow their curiosity

[Devpost](https://devpost.com/software/insight-ai) · hackathon [[HackMIT 2023]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**user** [[educator_student]]
**substrate** [[transcript_audio]] [[video_visual]]

**stack** flask, google-web-speech-api, openai

## How they structured the write-up

- inspiration:
- what it does:
- how we built it :
- challenges we ran into :
- accomplishments that we're proud of :
- what we learned :

## Body

Inspiration: Our inspiration stemmed from the realization that the pinnacle of innovation occurs at the intersection of deep curiosity and an expansive space to explore one's imagination. Recognizing the barriers faced by learners—particularly their inability to gain real-time, personalized, and contextualized support—we envisioned a solution that would empower anyone, anywhere to seamlessly pursue their inherent curiosity and desire to learn. What it does: Our platform is a revolutionary step forward in the realm of AI-assisted learning. It integrates advanced AI technologies with intuitive human-computer interactions to enhance the context a generative AI model can work within. By analyzing screen content—be it text, graphics, or diagrams—and amalgamating it with the user's audio explanation, our platform grasps a nuanced understanding of the user's specific pain points. Imagine a learner pointing at a perplexing diagram while voicing out their doubts; our system swiftly responds by offering immediate clarifications, both verbally and with on-screen annotations. How we built it : We architected a Flask-based backend, creating RESTful APIs to seamlessly interface with user input and machine learning models. Integration of Google's Speech-to-Text enabled the transcription of users' learning preferences, and the incorporation of the Mathpix API facilitated image content extraction. Harnessing the prowess of the GPT-4 model, we've been able to produce contextually rich textual and audio feedback based on captured screen content and stored user data. For frontend fluidity, audio responses were encoded into base64 format, ensuring efficient playback without unnecessary re-renders. Challenges we ran into : Scaling the model to accommodate diverse learning scenarios, especially in the broad fields of maths and chemistry, was a notable challenge. Ensuring the accuracy of content extraction and effectively translating that into meaningful AI feedback required meticulous fine-tuning. Accomplishments that we're proud of : Successfully building a digital platform that not only deciphers image and audio content but also produces high utility, real-time feedback stands out as a paramount achievement. This platform has the potential to revolutionize how learners interact with digital content, breaking down barriers of confusion in real-time. One of the aspects of our implementation that separates us from other approaches is that we allow the user to perform ICL (In Context Learning), a feature that not many large language models don't allow the user to do seamlessly. What we learned : We learned the immense value of integrating multiple AI technologies for a holistic user experience. The project also reinforced the importance of continuous feedback loops in learning and the transformative potential of merging generative AI models with real-time user input. <div