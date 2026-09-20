---
slug: "tse"
url: "https://devpost.com/software/tse"
title: "Entia"
hackathon: "Adobe Express Add-ons Hackathon"
organization: "Adobe"
winner: true
words: 835
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/measured_ablation"
  - "domain/supply_logistics"
  - "user/educator_student"
  - "substrate/document_pdf"
  - "substrate/sensor_telemetry"
---

# Entia

> Your go-to Express Add-on for personalized video analytics, Entia (Latin for "beings") unlocks Persona-driven insights for Content Creators, Marketers, and SMB's directly from your videos.

[Devpost](https://devpost.com/software/tse) · hackathon [[Adobe Express Add-ons Hackathon]]

## Facets

**mechanism** [[measured_ablation]]
**domain** [[supply_logistics]]
**user** [[educator_student]]
**substrate** [[document_pdf]] [[sensor_telemetry]]

**stack** adobe, elevenlabs, openai, python, typescript

## How they structured the write-up

- the story behind entia
- solution development
- the learning curve
- what's next for entia
- built with

## Body

Tech Diagram Welcome Page Talk to Persona's Target Audience Individual Feedback The Story Behind Entia When my teammate and I sat down to brainstorm this hackathon, we knew we couldn't just wing it like we usually do. No more "let's build something cool and see what happens" would work — we needed to be strategic. We deccided to take a step back to figure out who we’re building for, what challenges do they face, and where are they already spending their time? We looked through tutorials, templates, and user community posts to find a potential source of discomfort for the users. That's when it hit us: Adobe Express users are constantly creating video content – reels, ads, promotional videos. Cue the next two weeks of watching how to create video's in Adobe Express tutorials in YouTube to completely understand our target customers. We wanted to start user first, and we did that. Marketers, small- and medium-business owners and content creators starting out; people who don't have a purse to splurge. We spent hours researching the current landscape of video analytics tools and honestly? Most of them are either enterprise-focused surveillance systems or basic YouTube analytics dashboards. All of them in fragmented separate areas with a ton of things to track but no way to improve on the video immediately. Now that we had found our target audience, we needed to validate. Did the the customers actually face this problem? Or were we trying to solve a problem that did not exist? Were customers fine with having no analytics and just wanted to edit and post videos? The answer was a resounding no. Customers actually wanted this. Two places helped us confirm this — the Adobe Express feature board, where the top most voted request for marketers was Analytics and Scheduling (which we felt would be better implemented as a core Adobe feature instead of an add-on since social posting and account connection was already present) and the Adobe Fund for Design where our direction of AI based Guidance was reaffirmed. Solution Development Now that we understood there was a need for it , we started thinking through the solution. What to build? How to solve the problem? We took inspiration from two very recent applications - The Nvidia Video Search and Summarization Agent that was released last month with their mind blowing AI that can watch a video and give a chat Q&A experience with every frame, and an app called Growith which had a creator community that could rate other creator videos and post their own to get feedbacks to any questions they set. We also researched how to design the UI, with focus on design principles and Spectrum design system. We used React Spectrum Web Components to design the frontend, keeping accessibility in mind. We also read up on video analytics that we could, in general rule of thumb, predict. We also went through models that could get accurate video related information with the audio if the video is provided and most top LLM models like Gemini 2.5 Pro and GPT-4o could reliably give data. Finally we focused on creating well-rounded personas with varying demographics to provide various outlooks on the video. This lead to some interesting bloopers where a Psychologist persona was trying to ban the video cause it was too techy and boring. The voice feedback was an aspect we wanted to implement because it is increasingly easy to do so with ElevenLabs and it helps connect directly with the customer, letting them have all their doubts clarified without having to tediously type away at their keyboards. The Learning Curve This project pushed us into territories we had never explored before. Video analytics is complex — understanding what makes content engaging isn't just about view counts or retention curves, we had to learn about visual psychology, social media algorithms, and user behavior patterns. Building AI personas that give genuinely helpful feedback (and not just generic advice) required us to understand the creator mindset and the specific challenges they face when trying to optimize their content. Luckily some prior experience in prompt engineering helped us go an extra mile. The design iterations taught us that sometimes you have to be willing to throw everything away and start over. The fourth draft was so much better than the first that it felt like a completely different product. What's Next for Entia We're focusing on the following features: Advanced A/B testing capabilities that go beyond simple metrics Version history and comparison tools Persona fine-tuning based on real feedback from users in the Adobe Express Discord community Letting users choose their own personas The goal is to make Entia the go-to intelligence layer for video creators who are serious about their craft. Built With Frontend : React and Spectrum Backend : Flask server with video processing capabilities AI/ML : Custom trained models for video analysis and persona-based feedback along with LLM's and Elevenlabs API Integration : Adobe Express Document API (with properly configured manifest.json) <div