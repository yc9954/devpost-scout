---
slug: "smart-clip-ai"
url: "https://devpost.com/software/smart-clip-ai"
title: "Smart Clip AI"
hackathon: "AWS Lambda Hackathon"
organization: "Amazon"
winner: true
words: 445
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/voice_speech"
  - "substrate/transcript_audio"
---

# Smart Clip AI

> Turn long videos into short, high-impact clips—instantly. Powered by AI & AWS, Smart Clip AI helps you educate, entertain, or inspire without lifting a finger.

[Devpost](https://devpost.com/software/smart-clip-ai) · hackathon [[AWS Lambda Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[voice_speech]]
**substrate** [[transcript_audio]]

**stack** bedrock, lambda, mediaconvert, python, stepfunction, streamlit, transcribe

## How they structured the write-up

- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for smart clip ai

## Body

GIF Infrastructure Inspiration I'm an entrepreneur at heart, constantly driven by a passion to build new things. This project was born from my desire to combine AI with Data Engineering , two fields I deeply love. I’m especially passionate about creating automated workflows that deliver cutting-edge, scalable solutions to real-world problems. What it does Smart Clip AI uses AI and AWS serverless architecture to: Upload your video Transcribe the content Detect key moments based on your audience intent Auto-generate short-form clips with captions and hashtags Notify you when your clip is ready to post 💥 How we built it Upload Video: Users drag and drop a video into a Streamlit app, which uploads it directly to an S3 Input Bucket . Trigger the Magic: An EventBridge rule activates a Step Function , orchestrating several Lambda functions that execute the following pipeline: 🎯 State Machine Workflow 🔤 Transcribe the video using Amazon Transcribe 🧠 Detect the most relevant phrases using Bedrock AI , based on the audience's goal 🎬 Extract video segments that match those phrases 💬 Auto-generate captions and hashtags 📩 Notify the user via email when the final clip is ready to share Challenges we ran into The biggest challenge was ensuring precise alignment between the AI-generated phrases (from Bedrock) and the actual video segments. Accurately trimming and stitching those clips in the correct order while preserving meaning and flow was tough. But this step was essential to generate a coherent, high-quality short video that’s shareable and valuable on social media. Accomplishments that we're proud of I'm truly proud of being able to summarize long videos into short, engaging clips based on user preferences and their target audience goals. Successfully extracting the most relevant insights and hashtags from the transcript of a long video—and using them to automatically guide short video editing—was a major achievement. I absolutely love AWS Step Functions, and being able to automate the entire video editing pipeline through Lambda orchestration is something I'm really proud of. What we learned Through this journey, I learned how to master AWS Step Functions to efficiently orchestrate Lambda functions in a sequential and scalable way. I also gained deeper insights into AWS’s powerful serverless ecosystem , leveraging tools like Amazon Transcribe, Elemental MediaConvert, and Bedrock to solve real-life challenges. What's next for Smart Clip AI Expand LLM Support: Integrate additional Amazon Bedrock models to give users greater flexibility and control over AI behavior and tone. Monetization & User Access: Implement a secure login system and explore monetization options to offer tiered plans and premium features. Enhanced Subtitle Experience: Add interactive subtitles with customizable styles—colors, fonts, and effects—for more engaging and brand-aligned short videos. <div