---
slug: "flex-se8mtf"
url: "https://devpost.com/software/flex-se8mtf"
title: "FLEX"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 518
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/finance_payments"
  - "user/small_business"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# FLEX

> AI. Blockchain. Freelancing. Find your BEST candidates!

[Devpost](https://devpost.com/software/flex-se8mtf) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[finance_payments]]
**user** [[small_business]]
**substrate** [[financial_record]] [[geospatial]] [[structured_db]]

**stack** deepgram, express.js, fetch.ai, flask, move, next.js, python, singlestore, sui, terraform

## How they structured the write-up

- flex [freelancing linking expertise xchange]
- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for flex

## Body

FLEX [Freelancing Linking Expertise Xchange] Inspiration Freelancers deserve a platform where they can fully showcase their skills, without worrying about high fees or delayed payments. Companies need fast, reliable access to talent with specific expertise to complete jobs efficiently. "FLEX" bridges the gap, enabling recruiters to instantly find top candidates through AI-powered conversations, ensuring the right fit, right away. What it does Clients talk to our AI, explaining the type of candidate they need and any specific skills they're looking for. As they speak, the AI highlights important keywords and asks any more factors that they would need with the candidate. This data is then analyzed and parsed through our vast database of Freelancers or the best matching candidates. The AI then talks back to the recruiter, showing the top candidates based on the recruiter’s requirements. Once the recruiter picks the right candidate, they can create a smart contract that’s securely stored and managed on the blockchain for transparent payments and agreements. How we built it We built starting with the Frontend using Next.JS , and deployed the entire application on Terraform for seamless scalability. For voice interaction, we integrated Deepgram to generate human-like voice and process recruiter inputs, which are then handled by Fetch.ai 's agents. These agents work in tandem: one agent interacts with Flask to analyze keywords from the recruiter's speech, another queries the SingleStore database, and the third handles communication with Deepgram . Using SingleStore's real-time data analysis and Full-Text Search, we find the best candidates based on factors provided by the client. For secure transactions, we utilized SUI blockchain, creating an agreement object once the recruiter posts a job. When a freelancer is selected and both parties reach an agreement, the object gets updated, and escrowed funds are released upon task completion—all through Smart Contracts developed in Move . We also used Flask and Express.js to manage backend and routing efficiently. Challenges we ran into We faced challenges integrating Fetch.ai agents for the first time, particularly with getting smooth communication between them. Learning Move for SUI and connecting smart contracts with the frontend also proved tricky. Setting up reliable Speech to Text was tough, as we struggled to control when voice input should stop. Despite these hurdles, we persevered and successfully developed this full stack application. Accomplishments that we're proud of We’re proud to have built a fully finished application while learning and implementing new technologies here at CalHacks. Successfully integrating blockchain and AI into a cohesive solution was a major achievement, especially given how cutting-edge both are. It’s exciting to create something that leverages the potential of these rapidly emerging technologies. What we learned We learned how to work with a range of new technologies, including SUI for blockchain transactions, Fetch.ai for agent communication, and SingleStore for real-time data analysis. We also gained experience with Deepgram for voice AI integration. What's next for FLEX Next, we plan to implement DAOs for conflict resolution, allowing decentralized governance to handle disputes between freelancers and clients. We also aim to launch on the SUI mainnet and conduct thorough testing to ensure scalability and performance. <div