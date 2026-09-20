---
slug: "ai-traffic-control-aitc"
url: "https://devpost.com/software/ai-traffic-control-aitc"
title: "AI Traffic Control (AITC)"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 427
team_size: 3
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/transportation"
  - "substrate/transcript_audio"
---

# AI Traffic Control (AITC)

> AiTC is transforming the aviation industry by automating ATC radio calls and providing analytics for faster, more accurate responses, allowing air traffic controllers to focus on critical situations.

[Devpost](https://devpost.com/software/ai-traffic-control-aitc) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[transportation]]
**substrate** [[transcript_audio]]

**stack** ai, python, reflex, vapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for ai traffic control (aitc)

## Body

Inspiration Our inspiration for AiTC came from our use of various forms of transportation and our close connections with friends in the aviation industry. Seeing firsthand the complexities and challenges that air traffic controllers face, we wanted to create a solution that could alleviate some of the burdens on agents in control towers. AiTC is designed to streamline communication, reduce errors, and enhance the efficiency of air traffic management. What it does AiTC is an AI-driven platform designed to assist air traffic controllers by automating routine radio communication with pilots and providing real-time flight data insights. It leverages advanced speech recognition and natural language processing to analyze ATC-pilot communications, flag potential issues, and ensure that critical information is delivered accurately and on time. The system works in tandem with controllers, acting as a digital assistant to help manage complex airspace efficiently. The long-term goal is to fully automate the ATC communications. How we built it We built AiTC using several powerful tools and technologies. We used Vapi to train the models with out datasets and for real-time flight data integration, providing up-to-the-minute information about flights. We used Deepgram for speech-to-text capabilities, converting real-time ATC communications into actionable data. We used OpenAI to to interpret and assist with communication, as well as to improve decision-making processes within the control tower. We used hugging face datasets of ATC call transcripts and guides to train the AI models ensuring accurate communication processing. Accomplishments that we're proud of We’re super proud of developing a working prototype that integrates real-time flight data with AI-driven communication tools. The ability of AiTC to accurately process and respond to ATC communications is a major milestone, as is its potential to enhance safety and efficiency in one of the most critical sectors of transportation. We’re also proud of how we were able to incorporate machine learning models into a real-time system without sacrificing performance. What we learned Through this project, we learned the importance of handling real-time data effectively. We also gained valuable experience in the integration of various APIs and the unique challenges of real-time communication systems. What's next for AI Traffic Control (AITC) The next step for AiTC is to improve its scalability and robustness. We plan to expand its ability to handle more complex airspaces, integrate additional datasets for more nuanced decision-making, and further reduce latency in communication. The long-term goal is to fully automate this communication system. We also aim to pilot the system with actual air traffic control teams to gather real-world feedback and refine the tool for broader adoption. <div