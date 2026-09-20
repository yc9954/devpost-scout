---
slug: "memento-1p0jel"
url: "https://devpost.com/software/memento-1p0jel"
title: "Memento"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 845
team_size: 4
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/elder_child_care"
  - "user/patient_family"
  - "substrate/document_pdf"
  - "substrate/structured_db"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# Memento

> Memento helps elderly people connect with their families by reflecting on and sharing cherished memories, sparking meaningful conversations that strengthen bonds across generations.

[Devpost](https://devpost.com/software/memento-1p0jel) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[deterministic_policy]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]] [[elder_child_care]]
**user** [[patient_family]]
**substrate** [[document_pdf]] [[structured_db]] [[video_visual]] [[web_dom]]

**stack** chroma, deepgram, gemini, groq, python, reflex

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for memento

## Body

Inspiration Our inspiration came from the importance of connecting with family and cherishing proud personal stories. We recognized that many elderly people in nursing homes feel isolated from their families, despite the wealth of memories they carry. These memories hold so much value about family history, wisdom, and identity. By creating a platform that enables them to reflect on and share these moments, we aimed to bridge generational gaps and strengthen family bonds. Through storytelling, we want to foster a tight family bond, ensuring that cherished memories are passed down and that the elderly feel heard, valued, and connected. We wanted to emphasize the story aspect of these memories. When people want to share their memories with their family, especially virtually, they aren't able to fully relive or cherish that memory- a simple text message can't fully do justice to a fond memory. Thus, we wanted to bring life into these memories that shared within families online and especially provide elderly people who might not meet their families often to have an immersive experience with their family's memories. What it does Memento allows families to document fond memories that they have, and share them to the user. Families can upload memories that contain a date, description, and image. We target this product to the elderly in nursing homes who are usually alone and can benefit from having someone like family to talk to. The elderly user can then speak to the application and can have a conversation about the details of any memory. The application will also display the most relevant image to the conversation to help improve the experience. This enables the elderly user to feel like they are talking to a family member or someone they know well. It allows them to stay connected with their loved ones without the continuous presence of them. How we built it We designed Memento to be simple and accessible for both elderly users and their families. For this reason, we used Reflex to implement an elegant UI, and implemented a Chroma database to store the memories and their embeddings for search. We also integrated Whisper, a speech-to-text model through Groq’s fast inference API to decode what the elderly person is saying. Using this input, we query our database, and feed this information through Gemini , an LLM developed by Google, to give a coherent response that incorporates information from the families’ inputs. Finally, we used Deepgram’s text-to-speech model to convert the LLM’s outputs back to an audio format that we could speak back to the elderly user. Challenges we ran into Integration : It was difficult to integrate all of the sponsor’s softwares into the final application; we had to pore over documentation while becoming familiar with each API, which led to many hours of debugging. Non-determinism : Our models were non-deterministic; errors caused by specific outputs from the LLM were hard to replicate. Due to the background noise, we also could not efficiently test our speech-to-text model’s accuracy. Inference speed : Throughout this application, we make many API calls to large models, such as Whisper, Gemini, and the Aura TTS model. Because of this, we had to find clever optimizations to speed up the inference time to quickly speak back to the elderly user, especially since the WiFi was unusable most of the time. Accomplishments that we're proud of Design and User Experience : We are proud of our design since it encompasses the mood we were aiming for – a warm, welcoming environment, focusing on the good things that happen in life. Large Language Model and Vector Search : We are especially proud of how the LLM turned out and how well the RAG model worked. We spent lots of time prompting the different components to create the warm, empathetic, and welcoming environment the LLM provides. TTS and STT : Although we struggled a bit with this part, we are really proud about how it turned out. We feel we did a great job encompassing the ideals of the product by allowing users to reflect on past memories and connect closer with family. What we learned Working with STT and TTS models: many members of our group had never worked with speech-to-text or text-to-speech models, so this was a learning experience for all of us. We learned about the impressive accuracy that the state-of-the-art models are able to achieve but also encountered some of the drawbacks of these models, since many of them don’t work as well with moderate levels of background noise. How to make a great UI: What's next for Memento Because of time constraints, there were many features and improvements we wanted to implement but could not. Continuous LLM Conversation : We wanted to be able to talk to the LLM continuously without having to press a microphone button. Due to time constraints, we were not able to implement this feature User Personalization and Customization : We aimed to personalize the website to users by adding custom themes, colors, and fonts, but we ran out of time to do so. <div