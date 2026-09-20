---
slug: "lingua-franca-6xovi3"
url: "https://devpost.com/software/lingua-franca-6xovi3"
title: "Lingua Franca"
hackathon: "TreeHacks 2024"
organization: "TreeHacks"
winner: true
words: 450
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "user/educator_student"
---

# Lingua Franca

> Immersive VR language learning experience powered by AI.

[Devpost](https://devpost.com/software/lingua-franca-6xovi3) · hackathon [[TreeHacks 2024]]

## Facets

**mechanism** [[voice_speech]]
**user** [[educator_student]]

**stack** oculus, together.ai, unity, wit.ai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- what we learned
- what's next for lingua franca

## Body

VR headset followed by a plus sign and the duolingo maskot Inspiration Conventional language learning apps like Duolingo don’t offer the ability to have freeform and dynamic conversations. Additionally, finding a language partner can be difficult and costly. Lingua Franca tackles this head-on by offering intermediate to advanced language learners an immersive, interactive experience. Although other apps exist that try to do the same thing, their interaction topics are hard-coded, meaning that you encounter yourself in the same dialogue over and over again. By leveraging LLMs, we’re able to ensure that no two experiences are the same! What it does You stumble into a foreign land and must communicate with the townsfolk in order to get by. As you talk with them, you must reply by recording yourself speaking in their language. Aided by LLMs, their responses dynamically change depending on what you say. Additionally, at some points in the conversation, they will give you checkpoints that you must accomplish, which encourages you to talk to other villagers. After each of your responses, you can also see alternative phrases you could’ve said in response to the villager. Seeing these alternative responses can aid in learning vocabulary, grammar, and can help the user branch outside of their usual go-to phrases in the language they are learning. Not only can you guide the conversation to whatever topic you’d like to practice, but to keep the user engaged, we’ve also added backstory to the characters in the village. Each time you talk with them, you can learn something more about their relationship with others in the village! How we built it Development was done in Unity3D. We used Wit.ai to capture and transcribe the user’s recorded responses. Those transcribed responses were then fed into an LLM from Together.ai, along with extra information to give context and guide the LLM to prompt the user to complete checkpoints. The response from the LLM becomes the villager’s response to the player. We created the world using assets from Unity Asset store, and the character models are from Mixamo. What we learned Developing in VR was new to all team members, so developing for the Oculus Quest and using Unity3D was a great learning experience. LLMs aren’t perfect, and working to mitigate poor, harmful, or unproductive responses is difficult. However, we took this challenge seriously while working on this app and carefully tuned our prompts to give the model the context it needed to avoid these situations. What's next for Lingua Franca The next steps for this app include: Adding more languages adding audio feedback from the villagers as an addition to text responses adding new locations, characters, and worlds for more variation in the experience. <div