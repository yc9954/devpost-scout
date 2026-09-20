---
slug: "vraille"
url: "https://devpost.com/software/vraille"
title: "Vraille"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 1042
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/supply_logistics"
  - "substrate/video_visual"
---

# Vraille

> Redefining Accessibility: Real-Time Awareness for the Visually Impaired With Gemini-Powered Glasses & Dynamic Braille

[Devpost](https://devpost.com/software/vraille) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[supply_logistics]]
**substrate** [[video_visual]]

**stack** arduino, c++, cohere, facedetection, gemini, meta, multimodal, python, solidworks, supabase, vapi, websockets, windsurf

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for vraille

## Body

Dynamic Braille Interface CAD Dynamic Braille Interface Final Prototype AI Glasses Inspiration Approximately 2.2 billion people worldwide suffer from mild to severe vision impairment, negatively impacting their physical and digital interactions. To that end, the latest advancements in smart glasses and vision technology prioritize convenience features and narrowly defined use cases over comprehensive systems purposefully designed for the visually impaired. As a result, those with visual impairments are unable to tap into the ways technology can change their lives. Think memory recall systems for those who are forced to match faint voices to their dearest loved ones, or navigation tools that provide real-time spatial awareness in complex, unfamiliar environments. The lack of sufficient technological progress in these directions leaves the visually impaired with no choice but to resort to archaic solutions such as guide dogs and canes—tools that, while reliable, fundamentally fail to harness the potential of modern computing. But, what if we could hack the previously antiquated physical and digital systems to bring novelty and the latest advancements to the lives of billions of visually impaired folks around the world? Introducing Vraille (Vision + Braille) — the AI glasses layer built for the visually impaired using Gemini-orchestrated voice automation and a dynamic braille interface. What it does Vraille transforms the way visually impaired individuals interact with their surroundings by combining three core innovations: Real-time environmental understanding: using Meta glasses with live video and audio feeds, Vraille interprets the user’s environment and delivers contextual awareness powered by Gemini’s multimodal AI. Conversational interaction through Gemini tool calling: through Gemini-orchestrated voice automation, users can naturally ask questions and receive immediate, meaningful responses about their environment — from identifying objects to recalling contextual details. Dynamic braille interface: a tactile, adaptive braille pad translates digital and environmental information into touch in real time, offering a discreet alternative to audio cues. This ensures users can navigate and learn without causing disruption in quiet or shared spaces. Together, these features give visually impaired users an intuitive and empowering interface to both their physical and digital worlds. Vraille addresses the long-standing stagnation in accessibility tech by rethinking and adapting the latest advancements (e.g. Multimodal AI, voice agents, tool calling, among other technologies) to create solutions that truly make a lasting difference. How we built it We developed the software and hardware components of Vraille by integrating several cutting-edge technologies and collaborating effectively to make it happen! The notable technologies we adopted to create Vraille include: • Gemini tool calling for real-time multimodal reasoning and environment understanding. • Vapi voice agents to enable seamless, natural conversation between the user and the system. • Cohere embeddings and models to handle contextual memory recall and natural language understanding. • A custom-built dynamic braille pad powered by microcontrollers and actuators, designed to adapt text and environmental information into tactile feedback in real time. • Real-time face detection using the Face++ API Specifically on the hardware side of the project, we designed a custom motorized piston graille pattern to dynamically change the graille text being displayed. This was an ambitious but was achieved due to the amazing resources provided throughout the hackathon. Challenges we ran into On the technical side, applying relatively new technologies like Meta Rayban smart glasses, Vapi voice-control agents, and Gemini Tool calling were the biggest challenges we ran into. Not only did we have to consult company professionals during the event to tackle unprecedented issues, but also did we used multiple layers of processing in order to unleashed the full potential of an existing commercial product. For example, our biggest challenge was to jailbreak the Meta Rayban glasses to use the vision system in our own way by video calling on WhatsApp call, redirecting audio output into the AI Voice Agent in Python, and capturing video feed from the camera on the glasses. The whole process requires a total of 4 additional virtual audio I/O devices. We were constantly working with technologies in ways that not many had done before. Logistically, we faced a teaming crisis where our team of 4 was coming and leaving. Started with the idea of building something with a combination of hardware and software, we purposefully recruited more mechanically focused role. However, the original two people we reached out too left the team before the competition started. One of the other members later decided to quit because of the misalignment of goals and ideas for this project. With the lack of time and mentors in the hardware area, our progress on the hardware component was severely behind when there was almost no 3D printers available towards the end. Therefore, we built everything without 3d printer and it is completely hand-crafted. Accomplishments that we're proud of Hacked for 30+ hours, turning what started out as an idea into something that could be so much more! Worked around challenges involving Vapi package dependency incompatibility and gemini tool calling, eventually turning Vraille as a truly intelligent voice-powered agent that could perform (via tool call) various actions for the user. Last but not least, we were able to integrate our unique strengths to build a hardware and software project that has the potential to leave great impact amongst the visually impaired community, which brings us great personal satisfaction. What we learned • Discuss goals and alignments of ideas ahead of time in the teaming experience • Don't spend too much time on ideas; ideas don’t come fully formed. Start right away and gain some insights along the way, and you might get more sparks! • The hardware component of a project can be the limiting factor for the completion of a project, especially when the team lacks expertise in this area. • Do not rely on materials, resources, and opportunities provided to you. There is no guarantee for what one can get. • Have a structured plan and firm timeline to help the team execute on an idea more efficiently. What's next for Vraille • Refining the dynamic braille interface to improve responsiveness and making it more seamless to use in one’s everyday life • Enhancing context given to the LLM responsible for orchestrating the multimodal tool calling workflows. • Improve video and audio quality output from the Meta Rayban glasses, find alternatives, or build our own market. <div