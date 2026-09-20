---
slug: "livestory"
url: "https://devpost.com/software/livestory"
title: "LiveStory"
hackathon: "Cal Hacks 11.0"
organization: "Cal Hacks"
winner: true
words: 433
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "user/developer"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# LiveStory

> Talk to the characters in your favourite story!

[Devpost](https://devpost.com/software/livestory) · hackathon [[Cal Hacks 11.0]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**user** [[developer]] [[researcher]]
**substrate** [[code_repository]] [[structured_db]]

**stack** 11labs, deepgram, groq, javascript, lottie, python, react, reflex, vapi

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for livestory

## Body

Story Slide Inspiration Our inspiration comes from one of our team member's bedtime story sessions with his little cousin. Whenever he reads him a picture book, his cousin always has questions like, "Why did Goldilocks walk into the house?"—and most of the time, we don’t have the answers. We wished there was a way for him to ask the characters directly, to hear their side of the story. That’s where the idea for LiveStory came from. We wanted to bring storybook characters to life and let kids interact with them directly to get answers to their questions in real time. What it does LiveStory is a children's storybook that comes alive! At ANY point in the story, interact with a character on the page and chat with them; how are they feeling about what just happened? With industry-leading AI voice-to-voice pipelines, readers can feel the emotion of their favourite characters. How we built it Our web application was built primarily using Reflex : Reflex for both frontend and backend React.js for managing the database of each page and character Custom assistants powered by Vapi, Groq, Deepgram, and 11Labs to simulate character interactions Reflex for Deploy Challenges we ran into We initially struggled with Reflex, but over time, it became our go-to tool for building the project. We had to prevent characters from spoiling the story by restricting their responses to what the reader had already seen. To solve this, we fed the accumulative story log into the voice API, ensuring characters only referenced the relevant parts of the story. Accomplishments that we're proud of Completing the project on time and getting it fully functional!!! Learning Reflex and Lottie from scratch and successfully implementing them over the weekend. Collaborating with amazing Reflex engineers to create a solid product based on their platform. Committing 20+ hours and $1,000 on travel from Waterloo, Canada, to make this hackathon happen! What we learned Making a full-stack app in Reflex Implementing beautiful vector animations with Lottie Implementing voice-to-voice models in web apps What's next for LiveStory As time is the biggest limitation during a hackathon, we would have loved to pour more time into the art to make a more beautiful experience. More stories! More animations! Characters could, based on the emotions of their speech, have reactive animations Character Interaction Interface: a more advanced UI can note your emotions Choose your own adventures! With supported stories, the conversations with the characters could influence the story! Customization for reader! We can also try feeding reader's information such as name, hobby and academic interest to serve better user experience. <div