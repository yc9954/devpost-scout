---
slug: "angelshot"
url: "https://devpost.com/software/angelshot"
title: "AngelShot"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 681
team_size: 3
has_repo: true
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/voice_speech"
  - "domain/disaster_emergency"
  - "user/government_staff"
  - "substrate/transcript_audio"
---

# AngelShot

> Natural conversation, safer situation.

[Devpost](https://devpost.com/software/angelshot) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[voice_speech]]
**domain** [[disaster_emergency]]
**user** [[government_staff]]
**substrate** [[transcript_audio]]

**stack** deepgram, elevenlabs, nextjs, react, tailwind, vapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what's next for angelshot

## Body

homepage System diagram Inspiration Whether it's at a college party, a public outing, or during a simple stroll downtown, individuals often find themselves in uncomfortable, unwanted situations due to unwanted attention. In these moments, a discreet way to seek help is crucial. In the bartending world, this concept is known as an " angel shot "—a code word or drink order that discreetly signals to staff that a customer needs assistance. Phone calls are a powerful tool in these uncomfortable situations, as they not only deter unwanted attention by creating an external conversation but also offer a lifeline to contact emergency services or trusted individuals. Thus, they server as angel shots outside of a bartending context. But what if no one is available to answer the call? How can individuals ensure they'll have someone to talk to when they need help the most? What it does AngelShot simulates a realistic phone call a variety of user-customizable AI-based assistants. Users will pre-define assistants that they can request a call from whenever they're placed in an unwanted situation. These assistants can take on roles; for instance, user's can create an assistant meant to be "an uncle that they haven't seen in awhile". Additionally, assistants can be given a conversation starter. This could range from topics like sports, gardening, etc... anything that the user will feel comfortable talking about in an uncomfortable situation. When an individual is in an uncomfortable situation, they can request a call from any of their created assistants to start a normal conversation. However, with each response, the assistant provides the user two discreet, context-based code words . These code words trigger pre-configured safety actions of two levels. For example, in a gardening-themed conversation, the assistant may provide the words "monstera" and "weeding". If the user says the first keyword "monstera" in their response, the assistant will know to share the user’s live conversation with emergency contacts. If the user says the second keyword "weeding" in their response, the assistant will know to forward you to emergency services instantly. How we built it We deployed a Next.js application on Vercel, written in Typescript and styled using Tailwind + Shadcn and a variety of frontend libraries. For authentication, we used Clerk to allow users to quickly signup using their phone numbers. As a means of handling phone communication, we utilized VAPI 's API to efficiently create customizable AI assistants. VAPI streamlined the integration of voice communication in our application, allowing us to simulate realistic phone calls with AI-based assistants. For speech-to-text functionality, we used a Deepgram's Nova 2 Phonecall Model, specifically tailored for low-bit phone calls. This ensures accurate transcription, even if users are calling from remote areas or in noisy environments, guaranteeing that conversations and safety triggers are captured correctly. Then, to simulate natural and context-aware dialogue, we used OpenAI's GPT-4 model. Using VAPI's API, we passed a system prompt to ensure the AI assistant can generate relevant conversations, generate two context-specific code words, and react appropriately via function calls if any of the code words are spoken. Lastly, for text-to-speech conversion, we chose ElevenLabs' models to create high-quality, natural-sounding voices for the AI assistants, enhancing the realism and comfort of the simulated calls. Challenges we ran into Our entire team didn't have WiFi for essentially half the event, so we spent the first half of the event ideating. The last half of the event was when our application truly came to life. Another issue that we ran into was correctly prompt engineering the virtual assistant. Once we found the right prompts, it was smooth sailing. Accomplishments that we're proud of We're proud of developing a discreet safety tool that could potentially save lives. Integrating customizable AI assistants and creating a reliable emergency response system were key milestones that we were able to accomplish. What's next for AngelShot We plan to enhance AngelShot with more customization options, additional safety features such as sharing location and real time stress level analysis. We also aim to improve accessibility, perhaps making the application into a mobile app using technologies like React Native. <div