---
slug: "humaads-live"
url: "https://devpost.com/software/humaads-live"
title: "HumaAds.live"
hackathon: "Theta Network 2024 Hackathon"
organization: "Theta Labs"
winner: true
words: 671
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/geospatial"
---

# HumaAds.live

> GenAI-powered in-video ads with live 3D sales agents. Engage viewers, answer queries, and capture feedback. Boost engagement and brand awareness with our cutting-edge, interactive ad solution.

[Devpost](https://devpost.com/software/humaads-live) · hackathon [[Theta Network 2024 Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** edgecloud, fastapi, langchain, llm, react.js, solidity, thetavideoapi, uinty3d

## How they structured the write-up

- 🌟 inspiration
- 📺 what it does
- 🛠️ how we built it
- 🚧 challenges we ran into
- 🏆 accomplishments that we're proud of
- 🚀 what's next for humaads.live
- 🙏 acknowledgements

## Body

🌟 Inspiration In the fast-evolving digital advertising landscape, traditional video ads are often ignored or skipped by viewers. We wanted to create a solution that not only captivates the audience but also provides valuable feedback to advertisers. The idea of an interactive, AI-driven sales agent that can engage viewers in real-time emerged as a revolutionary approach to in-video ads. By leveraging cutting-edge technologies like GenAI, Cloud Rendering, and Theta Edge Cloud, we aim to transform passive ad consumption into an active and engaging experience. 📺 What it does HumaAds.live is a groundbreaking in-video ads solution where a cloud-rendered 3D GenAI sales agent is live-streamed to viewers. Unlike traditional ads that are static and easily skippable, our solution offers an interactive and immersive experience. The GenAI sales agent, tailored to match the brand's aesthetics and environment, effectively pitches products, answers viewer questions, and collects feedback. This innovative approach enhances viewer engagement, increases average watch time, and provides actionable insights into campaign performance. Our platform currently supports in-video ads and has the potential to be used in various ad formats such as display ads, banner ads on websites, and even real-world hoarding ads. 🛠️ How we built it Theta EdgeCloud : LLM/GenAI : We utilize a Large Language Model (LLM) to build a Retrieval-Augmented Generation (RAG) system. This system effectively leverages product and brand information to pitch products and answer viewer queries. https://github.com/ssd39/humaads.live/blob/6c732ff4577eb0e0423a4131563a700845cda153/backend/langchain_llm/llama_edge_cloud.py#L13 . Cloud Rendering : To provide high-quality, aesthetically pleasing video ads, we perform real-time 3D rendering of the ads on Theta EdgeCloud’s GPU-based instances, ensuring cost-effectiveness and scalability. STT/TTS : Speech-to-Text (STT) and Text-to-Speech (TTS) models are employed to generate and deliver responses in real-time. https://github.com/ssd39/humaads.live/blob/6c732ff4577eb0e0423a4131563a700845cda153/backend/tts/whisper_edge_cloud.py#L5 . Live Stream : By utilizing Theta Edge nodes distributed globally, we achieve low latency and cost-effective live streaming of the 3D rendered video to the audience. Theta Blockchain : We have deployed a smart contract on the Theta testnet to manage advertising campaigns and billing. This ensures transparency, convenience, and reliability in billing processes. Unity3D : The 3D environment for the ads is developed using Unity3D. The environment includes various interactive elements and logic, exported as an executable. This executable runs on EdgeCloud for real-time rendering based on inputs from the core server. API/Core : Serving as the brain of the system, our API/Core coordinates the various components. It determines which ads to show, manages interactions with the RAG system, handles cloud rendering, and ensures seamless integration of STT/TTS services. This ensures optimal performance and minimal latency. 🚧 Challenges we ran into Building HumaAds.live presented several challenges: Real-time Rendering : Achieving high-quality real-time rendering without latency was a significant technical hurdle. Integration of Components : Ensuring seamless integration between the LLM, cloud rendering, STT/TTS, and live streaming services required meticulous planning and execution. User Experience : Crafting an engaging and intuitive user interface that enhances the viewer’s experience while maintaining the ad’s effectiveness was challenging. 🏆 Accomplishments that we're proud of Successfully developed a functional demo platform that showcases the capabilities of our in-video ads solution. Achieved real-time, low-latency 3D rendering and live streaming, providing a seamless viewer experience. Created a scalable solution that leverages Theta EdgeCloud’s infrastructure, ensuring cost-effectiveness and reliability. Developed an intuitive UI/UX that enhances viewer engagement and provides valuable feedback to advertisers. 🚀 What's next for HumaAds.live Expansion of Ad Formats : We plan to extend our solution to support display ads, banner ads on websites, and real-world hoarding ads. SDK Development : Developing an SDK to enable developers to integrate our AI-in-video solution into their platforms. Enhanced Personalization : Leveraging more advanced AI and machine learning algorithms to provide even more personalized and engaging ad experiences. Global Scaling : Expanding our infrastructure to support a larger global audience with consistent performance. Continuous Improvement : Continuously refining our technology stack to improve performance, reduce costs, and enhance the overall user experience. 🙏 Acknowledgements Demo videos are used from pexels. https://www.pexels.com Character is built using ReadyPlayerMe. https://readyplayer.me/ 3D icons on landing page used from 3dicons.co/ Logo created using Canva <div