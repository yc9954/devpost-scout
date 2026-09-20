---
slug: "langualine"
url: "https://devpost.com/software/langualine"
title: "LanguaLine"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 662
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/voice_speech"
  - "user/developer"
  - "user/educator_student"
  - "substrate/structured_db"
  - "substrate/transcript_audio"
---

# LanguaLine

> Are you anxious about speaking a foreign language or don't know where to start? Practice your conversational language skills and get real-time feedback with LanguaLine!

[Devpost](https://devpost.com/software/langualine) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[voice_speech]]
**user** [[developer]] [[educator_student]]
**substrate** [[structured_db]] [[transcript_audio]]

**stack** deepgram, express.js, firebase, gemini, javascript, node.js, openai, react, tailwind, vapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for langualine

## Body

Basic Mode Transcript and Summary Page Extra Motivational Mode User Improvements System Architecture Inspiration With a variety of language learning resources out there, we set out to create a tool that can help us practice a part of language that keeps things flowing -- conversation! LanguaLine aims to empower users to speak their foreign language by helping them develop their conversational skills. What it does We wanted to create an interface that can help users practice speaking a foreign language. Through LanguaLine, users can: Select a language they wish to practice speaking in Select how "motivating" they want their Mentor to be (Basic is normal, Extra Motivation is a tough love approach). Enter their phone number and receive a phone call from our AI Mentor Answer questions posed by the Mentor Receive real-time feedback about their performance View a transcript and summary of the call after the conversation is completed View a generalized report on user's language strengths and weaknesses across all conversations How we built it We used React.js for our frontend, and Firebase for our database. To style our components, we utilized TailwindCSS and React MaterialUI . Our backend system is comprised of Node.js and Express.js , which we use to make calls to Google's Gemini model. To create, tune, and prompt engineer our AI Mentor, we used the VAPI.ai API. Our transcriber model is Deepgram's nova-2 multi and our model is gpt-4o-mini provided by Open.AI . We are also using Gemini to implement Retrieval-Augmented Generation (RAG). We use past call transcripts and summaries to train and optimize our model. This training data is maintained in our Firebase database. In addition, this feature analyzes users' call transcripts and generates a report identifying strengths and weaknesses in their speaking skills. Challenges we ran into Our biggest challenge was understanding the VAPI documentation, as it was our first time working with a voice AI API. We had to make a few changes to our project stack to accommodate for VAPI, as we could only make client-side API calls. Since the majority of our team has limited experience working with LLMs and voice AI Agents, we faced some difficulties prompt engineering our Mentor, requiring us to tweak various model parameters and experiment through VAPI's dashboard. Accomplishments that we're proud of The turning point in our development process was when we were able to start conversing with our Mentor. After this was solidified, our project trajectory only went upwards. We're proud of the fact we were able to turn this idea into an operational and functional application. What we learned The team behind LanguaLine had a variety of skill levels; for some, this was their first project using this tech stack, while for others, this was familiar. Some of us mastered the ability to send API calls and parse JSON data. Some of us also learned how to prompt engineer for a particular language choice. There were lessons being learned all throughout the 36 hours of development, which helped us feel connected to the project and motivated to keep creating. What's next for LanguaLine Our biggest goal is to deploy and market this project. Being language learners ourselves, having a service like LanguaLine is invaluable to making progress toward achieving fluency. In addition, this increases accessibility for language learners by encompassing a wide range of supported languages and providing customizable support. Our project aims to support all languages. Due to our lack of control regarding the accuracy across various languages within LLMs, this feature needs more testing and tuning to be perfected. We plan to offer more variation in the Mentors we offer. Right now, we only offer Mentors based off of a language choice and motivation level. In the future, we plan to include language difficulties, personalities, a wider variety of supported languages, custom prompts, and scheduled calling. We also plan to offer improvement plans for grammar, pronunciation, and vocabulary, as well as a scoring system for users' performances during Mentor sessions. <div