---
slug: "medknight"
url: "https://devpost.com/software/medknight"
title: "MedKnight"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 856
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "mechanism/vision_ocr"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "domain/disaster_emergency"
  - "user/clinician"
  - "user/frontline_worker"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# MedKnight

> A one-of-a-kind, AR assistant medical system is made to guide first emergency first responders through critical, uncommon medical procedures with real-time support.

[Devpost](https://devpost.com/software/medknight) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]] [[vision_ocr]] [[voice_speech]]
**domain** [[developer_tools]] [[disaster_emergency]]
**user** [[clinician]] [[frontline_worker]]
**substrate** [[structured_db]] [[video_visual]]

**stack** agents, ar, c#, deepgram, fetch.ai, flask, large-language-models, meta, oculus, openai, opencv, python, quest, singlestore

## How they structured the write-up

- inspiration
- what it does
- how we built it
- singlestore
- fetch.ai
- deepgram
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for medknight

## Body

Logo Tech Stack Offsite Medical Professional Dashboard Initial Mock MedKnight Professional medical care in seconds, when the seconds matter Inspiration Natural disasters often put emergency medical responders (EMTs, paramedics, combat medics, etc.) in positions where they must assume responsibilities beyond the scope of their day-to-day job. Inspired by this reality, we created MedKnight, an AR solution designed to empower first responders. By leveraging cutting-edge computer vision and AR technology, MedKnight bridges the gap in medical expertise, providing first responders with life-saving guidance when every second counts. What it does MedKnight helps first responders perform critical, time-sensitive medical procedures on the scene by offering personalized, step-by-step assistance. The system ensures that even "out-of-scope" operations can be executed with greater confidence. MedKnight also integrates safety protocols to warn users if they deviate from the correct procedure and includes a streamlined dashboard that streams the responder’s field of view (FOV) to offsite medical professionals for additional support and oversight. How we built it We built MedKnight using a combination of AR and AI technologies to create a seamless, real-time assistant: Meta Quest 3 : Provides live video feed from the first responder’s FOV using a Meta SDK within Unity for an integrated environment. OpenAI (GPT models) : Handles real-time response generation, offering dynamic, contextual assistance throughout procedures. Dall-E : Generates visual references and instructions to guide first responders through complex tasks. Deepgram : Enables speech-to-text and text-to-speech conversion, creating an emotional and human-like interaction with the user during critical moments. Fetch.ai : Manages our system with LLM-based agents, facilitating task automation and improving system performance through iterative feedback. Flask (Python) : Manages the backend, connecting all systems with a custom-built API. SingleStore : Powers our database for efficient and scalable data storage. SingleStore We used SingleStore as our database solution for efficient storage and retrieval of critical information. It allowed us to store chat logs between the user and the assistant, as well as performance logs that analyzed the user’s actions and determined whether they were about to deviate from the medical procedure. This data was then used to render the medical dashboard, providing real-time insights, and for internal API logic to ensure smooth interactions within our system. Fetch.ai Fetch.ai provided the framework that powered the agents driving our entire system design. With Fetch.ai, we developed an agent capable of dynamically responding to any situation the user presented. Their technology allowed us to easily integrate robust endpoints and REST APIs for seamless server interaction. One of the most valuable aspects of Fetch.ai was its ability to let us create and test performance-driven agents. We built two types of agents: one that automatically followed the entire procedure and another that responded based on manual input from the user. The flexibility of Fetch.ai’s framework enabled us to continuously refine and improve our agents with ease. Deepgram Deepgram gave us powerful, easy-to-use functionality for both text-to-speech and speech-to-text conversion. Their API was extremely user-friendly, and we were even able to integrate the speech-to-text feature directly into our Unity application. It was a smooth and efficient experience, allowing us to incorporate new, cutting-edge speech technologies that enhanced user interaction and made the process more intuitive. Challenges we ran into One major challenge was the limitation on accessing AR video streams from Meta devices due to privacy restrictions. To work around this, we used an external phone camera attached to the headset to capture the field of view. We also encountered microphone rendering issues, where data could be picked up in sandbox modes but not in the actual Virtual Development Environment, leading us to scale back our Meta integration. Additionally, managing REST API endpoints within Fetch.ai posed difficulties that we overcame through testing, and configuring SingleStore's firewall settings was tricky but eventually resolved. Despite these obstacles, we showcased our solutions as proof of concept. Accomplishments that we're proud of We’re proud of integrating multiple technologies into a cohesive solution that can genuinely assist first responders in life-or-death situations. Our use of cutting-edge AR, AI, and speech technologies allows MedKnight to provide real-time support while maintaining accuracy and safety. Successfully creating a prototype despite the hardware and API challenges was a significant achievement for the team, and was a grind till the last minute. We are also proud of developing an AR product as our team has never worked with AR/VR. What we learned Throughout this project, we learned how to efficiently combine multiple AI and AR technologies into a single, scalable solution. We also gained valuable insights into handling privacy restrictions and hardware limitations. Additionally, we learned about the importance of testing and refining agent-based systems using Fetch.ai to create robust and responsive automation. Our greatest learning take away however was how to manage such a robust backend with a lot of internal API calls. What's next for MedKnight Our next step is to expand MedKnight’s VR environment to include detailed 3D renderings of procedures, allowing users to actively visualize each step. We also plan to extend MedKnight’s capabilities to cover more medical applications and eventually explore other domains, such as cooking or automotive repair, where real-time procedural guidance can be similarly impactful. <div