---
slug: "brainforge-ai-pioneering-future-education-w-adaptive-tech"
url: "https://devpost.com/software/brainforge-ai-pioneering-future-education-w-adaptive-tech"
title: "Aspectus - Pioneering Future Education w/ Adaptive Tech"
hackathon: "Boost Hacks II"
organization: "Boost Hacks"
winner: true
words: 570
team_size: 2
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/accessibility"
  - "domain/education"
  - "user/educator_student"
  - "substrate/video_visual"
---

# Aspectus - Pioneering Future Education w/ Adaptive Tech

> Revolutionize learning with AI-powered, adaptive gameplay. Transform any syllabus into quests tailored to each student. Master subjects through play, not textbooks. Learn effortlessly as you game.

[Devpost](https://devpost.com/software/brainforge-ai-pioneering-future-education-w-adaptive-tech) · hackathon [[Boost Hacks II]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[accessibility]] [[education]]
**user** [[educator_student]]
**substrate** [[video_visual]]
  <sub>weak: geospatial</sub>

**stack** c#, firebase, flask, gemini, python, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for aspectus

## Body

Title Screen: Game is called Aspectus to kind of connect w/ diff aspects of learning and that it will have aspectus of magic :) A snapshot of combat, when attack is pressed Gemini will prompt question (assuming steps followed) enter response below and submit The Island Map, users will start at Island 1 then go to island 2 etc Inspiration The inspiration for Aspectus came from observing the limitations of traditional education, especially during the COVID-19 pandemic. There was an opportunity to use AI and gamification to create a more personalized, engaging learning experience that adapts to individual needs and learning styles. What it does Aspectus transforms educational content into an interactive, Unity-based game powered by Google's Gemini AI. It takes uploaded syllabi and creates personalized, adaptive learning experiences through quests, puzzles, and challenges. The system continuously adjusts difficulty based on student performance, making learning both fun and effective. How we built it Integrated Google's Gemini AI model with the Unity game engine to create a dynamic 2D RPG learning environment. Developed algorithms for adaptive pedagogy, diverse challenge generation, and real-time difficulty adjustment, while ensuring seamless AI integration with game features. Challenges we ran into Major challenges faced included: Integrating real-time AI responses with Unity game features, debating on what backend network to use, tried .NET but then went and switched to Flask as it was easier to use. Developing an algorithm for question generation involved alot of research into how it was possiblestay on the same conversation with the AI model in order to retain context and consistent responses, this was difficult as this isn't exactly simple. As well it was difficult to come up with engaging gameplay that was both challenging and educational. One challenge that is still prevalent is ensuring the system works effectively for students with various learning disabilities, as of now, there are only text based questions, but with Gemini's AI capabilities, it will be possible to generate puzzles, video, and image based questions to adhere to other senses. Accomplishments that we're proud of Learned how to successfully combine Unity and Gemini AI for a unique educational experience In addition, while conducting research it led to the creation of a creative adaptive learning system that caters to diverse learning needs, built upon a former project of mine: https://devpost.com/software/visuai-ip7jz4 Learned how to essentially develop a platform that can potentially revolutionize how education is delivered by building a solution that addresses many of the core issues in modern education What we learned Through this project, insights were gained into: The complexities of integrating AI with game development The potential of AI in personalizing education The flaws in the educational system, but most importantly the opportunities that arise from addressing them with edutech solutions What's next for Aspectus Future steps include: Expanding the range of subjects and educational levels covered -> DONE Enhancing the AI's ability to generate more complex, multi-modal challenges as right now we just prompt with text -> DONE Developing partnerships with educational institutions for wider adoption, this can be started with local schools and summer programs to garner feedback and iteratively develop our model -> DONE Incorporating more advanced analytics for educators and parents, as they can use this knowledge to better adhere to student needs at home -> WIP Exploring VR/AR integration for even more immersive learning experiences, this will have to wait for a while, but its something cool to consider <div