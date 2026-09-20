---
slug: "sagewell"
url: "https://devpost.com/software/sagewell"
title: "SageWell"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 637
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "user/developer"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# SageWell

> An AI-powered Medical Assistant for the Elderly

[Devpost](https://devpost.com/software/sagewell) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]] [[elder_child_care]]
**user** [[developer]]
**substrate** [[structured_db]] [[transcript_audio]]

**stack** firebase, javascript, llm, monsterapi, react.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for sagewell

## Body

Home Page AI Assistant Inspiration Our inspiration for creating this AI project stemmed from the desire to leverage current technology to enhance the lives of our community members, particularly the elderly. Recognizing the difficulties faced by aging individuals, including our own grandparents, to embrace technological advancements, and their concerns about health conditions, we sought a way to integrate technology and healthcare services seamlessly into their lives. Thus, SageWell was conceived—an AI companion designed to provide personalized support to seniors by navigating medical information alongside their healthcare providers. At SageWell, we believe in accessibility of AI for all age groups. What it does SageWell enables users to seek medical information through natural language interactions, allowing elderly individuals to pose questions verbally and receive spoken responses, mimicking human conversation. How we built it SageWell leverages the capabilities of two Monster APIs: OpenAI-Whisper Large-v2 for speech-to-text conversion and Meta's llama-2-7b-chat-hf for refining our reinforcement learning model. Our model was trained on MedQuAD, a comprehensive dataset containing over 47,000 medical question-answer pairs, Drugs, Side Effects and Medical Condition dataset, and Drugs Related to Medical Conditions dataset. The frontend of the web app was built using React, a JavaScript library, and the service we integrated into our app to store all the audio files was Firebase. Challenges we ran into In the process of developing SageWell, we encountered several challenges. Since there were many integrations in our application, from speech-to-text transcription and MonsterAPIs for fine-tuned LLMs, to storage service providers, we faced difficulties trying to link all the individual pieces together. We learned several new tools and technologies and also spent time fine-tuning models to provide medical information. Additionally, we encountered setbacks when we were finishing up our project as we were facing CORS errors when making API calls from the browser - we were able to work around this by adding a proxy, which served as a bridge between our client and server. Accomplishments that we're proud of We empowered our primary user demographic, the elderly, to engage with SageWell through voice interactions instead of having to type text. We addressed the challenges that many seniors encounter when typing on digital devices, thereby increasing the accessibility of the process of seeking medical information and ensuring inclusivity in AI for all age groups, especially the elderly. Our reinforcement learning model has demonstrated effectiveness, evidenced by the decrease in training loss after each iteration and to 0.756 at the end. This indicates that the model fits well on the training data. We merged three datasets: the Medical Question Answering data set, the Drugs, Side Effects and Medical Condition data set, and the Drugs Related to Medical Conditions data set. By training our model for SageWell on these datasets obtained from NIH websites and drugs.com, we allowed SageWell to provide medical information to users based on reliable, comprehensive databases. What we learned Through this project, we gained valuable insights into the startup ecosystem and developer space. We expanded our skill set by refining our model, working with new APIs and storage providers, and creating a solution that addresses the specific challenges faced by our target audience. What's next for SageWell The journey of SageWell is just beginning. Moving forward, we aim to expand its capabilities to assist in additional areas crucial for the well-being of the elderly, such as medication reminders and guidance on accessing support for domestic chores. Furthermore, we envision integrating features that facilitate connections between seniors and younger generations, including their grandchildren and other youth in their communities. By fostering these intergenerational connections, SageWell will expand its targeting market size by not only keeping the elderly engaged with their loved ones but also ensuring they remain connected to the evolving world around them. Through SageWell, we look forward to continuing to push for accessibility of AI for all age groups. <div