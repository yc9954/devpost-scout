---
slug: "metropolis-ai"
url: "https://devpost.com/software/metropolis-ai"
title: "Metropolis.ai"
hackathon: "UC Berkeley AI Hackathon"
organization: "Cal Hacks"
winner: true
words: 857
team_size: 3
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
---

# Metropolis.ai

> We empower game studios both small and large to populate massive, bustling cities at the press of a button, where each and every NPC has a unique backstory, goals, and daily routine.

[Devpost](https://devpost.com/software/metropolis-ai) · hackathon [[UC Berkeley AI Hackathon]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]]

**stack** c#, chatgpt, coqui, gpt-4, gradio, langchain, openai, python, tts, unity

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for metropolis.ai

## Body

Generator GUI going through NPC creation. Inspiration A common feature of today's popular role-playing video games (RPGs), is an immersive environment. Games like Skyrim, Red Dead Redemption 2, Grand Theft Auto, etc. represent hundreds, if not thousands of developer hours sunk into making sure that every single non-player character (NPC) has their own dialogue, backstory, and motivations. This is extremely difficult for the largest game studios to pull off, and downright impossible for smaller developers. However, considering modern advances in natural language like Large Language Models (LLMs), we have realized that it doesn't have to be this way. What it does Using ChatGPT, LangChain, and Coqui Studios we are able to automatically mass-generate backstories, names, dialogue options, and daily schedules for fully voiced NPCs. You can feed any lore documents explaining your video game world into Metropolis, and it will automatically take them into account when generating backstories and names, so the NPCs truly feel like they are a part of your world. You can give our tool a list of unique locations and possible actions that NPCs can take at those locations, and Metropolis will automatically create a realistic, goal-driven schedule for the NPCs to roam around the world. Once the NPC’s schedule has been determined, Metropolis automatically generates unique dialogue trees for the player to interact with, that take into account factors like the NPC’s current location, what action they are currently taking, and their personality. How we built it Frontend: With Gradio, we’ve created a clean user interface where developers can input their desired parameters to generate world/story aware NPCs. In this GUI, we provide options to add NPC traits, world lore/history, locations for NPCs to visit, actions to perform at each location, etc. The various parameters are then passed into our backend to generate deep, immersive character details which can be read by game engines such as Unity. Backend: We begin with user-provided lore about the world, which is fed into ChatGPT to develop a unique character backstory and name. We then use this information to ask ChatGPT for a realistic goal for this new character. Now that the character has a backstory, a goal, we employ LangChain’s ReAct framework (instantiated with ChatGPT) to create an plan of action for the character to further their goals, given a user-provided list of locations and actions that the character can perform. The ReAct agent iteratively tries to take actions in an automatically generated, simplified, text-based version of the user’s world to further its goals, such as moving to different locations and taking different actions. We log what actions it takes, and what locations the agent moves to, and this becomes the NPC’s schedule in the real video game. We also query ChatGPT for estimates of how many minutes each action might take, to make the interface easier for the user. In this way, we can generate a unique, goal-driven itinerary for each NPC. At every point in the NPC’s schedule, we prepopulate the NPC’s dialogue tree using ChatGPT. A dialogue tree here refers to what the NPC says when the player walks up to them, the dialogue choices that the player has to respond, the NPC’s possible responses to each of the player’s dialogue choices given what it said before, etc. . The NPC is also automatically assigned a unique voice from Coqui Studios’ library of virtual voice actors, and each of the NPC’s dialogue options is automatically voiced using these text-to-speech (TTS) models. Challenges we ran into We ran into several challenges throughout development, like rate-limiting, lack of structured output from the LLM, and integrating our generated audio files, text data, and game state data together. We solved our rate-limiting issues by minimizing the number of OpenAI API calls we needed to make, by limiting the number of branches in our dialogue trees and asking the LLM to generate shorter dialogue options. In order to get outputs in the structure we needed, we learned valuable prompt engineering tricks, like providing examples, employing logit bias, and being more specific about the type of text we needed. In integrating everything together, we learned to manage a diverse codebase that we built with Python and C#, juggle multiple APIs for text generation, speech synthesis, and embodied action, all while coordinating as a team to make the frontend, backend, and AI aspects of the project come together. Accomplishments that we're proud of We are proud to say that we have a working product; we have an exciting demo to show that contains several of our automatically generated NPCs, each with their own personalities, backgrounds, schedules, and dialogue options. What we learned In our attempts to retrieve valid, structured data from ChatGPT and other LLMs, we were able to gain experience with prompt engineering and giving efficient prompts in general. We also became more familiar with LLM-empowered agents through LangChain, with modern text-to-speech APIs like Coqui, and with text-generation APIs like OpenAI’s ChatGPT. What's next for Metropolis.ai We would like to take the product we have built, apply some polish, and hopefully provide some value to video game studios by building upon this idea to create a startup. <div