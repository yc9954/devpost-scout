---
slug: "pep-your-compassionate-physical-therapy-agent"
url: "https://devpost.com/software/pep-your-compassionate-physical-therapy-agent"
title: "Pep - your compassionate Physical Therapy Agent"
hackathon: "ElevenLabs x 16z Worldwide Hackathon"
organization: "ElevenLabs"
winner: true
words: 488
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/health_clinical"
  - "domain/mental_health"
  - "user/developer"
  - "user/patient_family"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# Pep - your compassionate Physical Therapy Agent

> Duolingo for physical therapy with ambient real-time coaching powered by 11 labs

[Devpost](https://devpost.com/software/pep-your-compassionate-physical-therapy-agent) · hackathon [[ElevenLabs x 16z Worldwide Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[health_clinical]] [[mental_health]]
**user** [[developer]] [[patient_family]]
**substrate** [[code_repository]] [[financial_record]]

**stack** 11labs, gpt, swift, vision

## How they structured the write-up

- inspiration💡
- what pep does 🎯
- vision 🔭

## Body

GIF Pep - Your Compassionate Physical Therapy Agent 🏋️‍♂️🎙 Inspiration💡 We both have a lot of physical therapy experiences and realized that the biggest problem with PT is that patients often fail to stick to their prescribed exercises. This inspired us to create Pep – a Duolingo-style experience for physical therapy, making it fun, engaging, and easy to stay committed. What Pep does 🎯 Physical therapy only works if you actually do it – but it's hard to stay motivated without instant rewards or feedback. Pep fixes this. Here’s how Pep helps users stick to their PT exercises (not all have been implemented): Pep sends an endearing reminder at the right time. Gamification sparks motivation for each micro-exercise. One-tap start minimizes friction and makes it easy to begin. Pep’s in-exercise voice offers feedback and companionship throughout. Pep proactively logs symptoms and improvements with real-time honesty. Pep celebrates your progress, showing how today’s effort builds toward PT goals. Powered by AI, every interaction with Pep is fresh and personal – a compassionate companion guiding users through their PT journey. Vision 🔭 While physical therapy exhibits a real need, the roadblocks to motivation and consistency are universal — loss of novelty, transactional interactions, lack of feedback, forgetfulness, loneliness, etc. AI can effectively tackle this at a fraction of the cost of carefully designing a personalized, humanistic support system by hand (like Duolingo does). Pep can extend to other things people need help executing, whether it’s saving money, taking medication, making time for a hobby, or practicing better parenting. How we built it 🔧 Pep is a Swift iOS app. We mainly use the 11labs Conversation AI Swift SDK to create a voice UI that interacts with users, providing live coaching and feedback. We had a lot of fun customizing client tools within the 11labs SDK. We also integrated Apple’s Vision Framework to detect user joints and evaluate exercise accuracy in real time. Challenges we ran into 🛠 🔹 Memory Safety Issues in 11labs SDK The Swift SDK isn't designed well in terms of memory safety. Incorporating it with the Vision Framework caused severe conflicts in AVFoundation, leading to crashes on iPhones during testing. 🔹 Chaining Multiple AI Agents We struggled with chaining two different AI agents to get the client tool usage correct. We had to carefully manage context switching and session persistence for seamless user interactions. 🔹 Lack of Developer Resources We spent a lot of time debugging due to limited documentation and tool-use templates. We hope that in the future, 11labs provides better tool-use templates to simplify AI agent chaining. What we learned 📚 How powerful conversational AI SDKs have become! 🤯 How to integrate AI with multimodal interfaces (voice + vision). The challenges of real-time AI coaching and synchronizing AI agent transitions. Team Member + Contributions Lanruo: ElevenLabs conversational AI's (client) tool use and dynamic variables Yan: vision setup, swift boilerplate, concurrency, and cute dog gif! <div