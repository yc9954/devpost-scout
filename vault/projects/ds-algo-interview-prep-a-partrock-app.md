---
slug: "ds-algo-interview-prep-a-partrock-app"
url: "https://devpost.com/software/ds-algo-interview-prep-a-partrock-app"
title: "DS & Algo InterView Prep: A PartRock App"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 752
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/developer"
---

# DS & Algo InterView Prep: A PartRock App

> Cracking a coding interview especially the data structure & algorithm rounds can be daunting. But fear not, There's a new app on the horizon: your one-stop shop for interview preparation/domination.

[Devpost](https://devpost.com/software/ds-algo-interview-prep-a-partrock-app) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**mechanism** [[realtime_stream]] [[voice_speech]]
**domain** [[developer_tools]]
**user** [[developer]]
  <sub>weak: video_visual</sub>

**stack** partyrock

## How they structured the write-up

- inspiration
- what it does
- how we built it
- accomplishments that we're proud of
- what we learned
- what's next for ds & algo interview prep: a partrock app

## Body

DS & Algo InterView Prep: App screenshot User Input Widgets: Topic, Language, Difficulty level, Number of questions Suggested Questions, Practice a different question, Coding Ground Let's Discuss: A widget to get help Feedback & Suggestions for the given question and solurion Get Solutions Inspiration The coding interviews can be daunting, for both aspiring developers and experienced ones when it comes to DS & Algo rounds. Now, what if the software engineering interviews become less stressful and more focused on showcasing your true potential. That's the vision behind DS & Algo InterView Prep app. What it does This app takes a data-driven approach to coach it's users for coding interviews. By combining user-specified topics, languages, difficulty levels, and desired question quantities, it tailors a personalized practice session that perfectly matches your needs. The app helps the user in the following ways: 1. Personalized Learning : Users can tailor their practice sessions to specific topics, preferred programming languages, and interview questions of specified difficulty levels. This targeted approach ensures efficient learning and maximizes preparation for specific interview requirements. 2.Conceptual Clarity : The app's "Topic Primer" widget breaks down complex data structures and algorithms into easily digestible explanations. Concise explanations, code examples for the chosen topic fosters a deeper understanding that goes beyond rote memorization. 3. Personalized Practice : The "Suggested Questions" widget tailors the learning experience by suggesting interview questions based on your given topic, language, difficulty level and number of questions from renowned platform like LeetCode. User can also practice their choice of question as well. These keep users engaged and hone their problem-solving skills to tackle problems relevant to your target interviews. 4. Interactive Learning : Don't get stuck! The "Lets discuss here" chat provides real-time guidance as you solve practice problems. The LLM assistant offers valuable hints, helps identify edge cases, and steers you in the right direction, just like a friendly coding buddy. 5. Instant Feedback & Improvement : The "Feedback & Suggestion" widget analyzes your submitted solutions and offers insights on code clarity, efficiency, correctness, and alternative approaches. This allows you to refine your coding skills and identify areas for improvement before the real interview. 6. Get Unstuck : Sometimes, a helping hand is all you need. The "Get Solution" widget uses advanced large language models to generate well-structured, commented code solutions in your preferred language. These solutions tackle common edge cases and even include unit tests for verification. How we built it We built it using AWS PartyRock that removed the complexity of creating a UI from scratch and the backend to support the application. Accomplishments that we're proud of An working prototype which can solve some real world problems. Such as, getting solutions of the questions in user's preferred programming language, important primers about the given DS and/or Algo topic: just the way we want to prepare things before an exam, Chat with AI to get better understanding of the solution and also feedback for the code submitted by the users. What we learned I learnt a lot about Prompt Engineering. Understood how some simple tweaks to the prompt can significantly improve the results and hence the user experience. Also, as the app needed to be made using given resources(UI, Models) which doesn't have much flexibility, I had to design the app to get most out of the available resources considering the usability of the app. What's next for DS & Algo InterView Prep: A PartRock App The app can be made more powerful if we can build it from scratch using the 3rd party foundational models available on Amazon Bedrock and other AWS services. We can integrate some additional AWS services as well into the app to make it more accessible, user friendly and more powerful. Such as 1. Amazon Codewhisperer : Codewhisperer can be added to the "Coding Ground" widget to have code suggestions based on existing code and comments in real-time. 2. Amazon Codeguru : Codeguru can be used in the "Feedback & Suggestion" widget to get recommendation for code quality improvement. 3. Amazon Transcribe : This service can be used as a automatic speech recognition system(ASR) for voice-based user input, which would increase the accessibility of the application. 4. Amazon Translate : This service can be used to accurately translate text which would make it a multi-lingual application for a wider range of audience. 5. Amazon Poly : Poly can be used to turn texts to lifelike speech to make this application talk to the user, which would again increase the accessibility. <div