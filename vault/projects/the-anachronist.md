---
slug: "the-anachronist"
url: "https://devpost.com/software/the-anachronist"
title: "The Anachronist"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 977
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/education"
  - "user/educator_student"
  - "user/general_public"
  - "substrate/video_visual"
---

# The Anachronist

> History isn’t just studied, it’s lived. Enter a 3D time-travel adventure.

[Devpost](https://devpost.com/software/the-anachronist) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[education]]
**user** [[educator_student]] [[general_public]]
**substrate** [[video_visual]]

**stack** elevenlabs, gemini, godot, langchain, lumalabs, nitrode, openai

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for the anachronist

## Body

Inspiration When students hear the subject “history,” they are likely reminded of a textbook marred with numbers, dates, and timelines; when in fact history consists of real people and real events, which serve as a powerful tie that conjoins even the most dissimilar individuals through strong ties. Driven by a vision to bridge this rift, we devised a game that promises the development of a deeper, more immersive understanding of history by placing players directly into pivotal moments of the past. By warping through time and stepping into the shoes of people who lived through transformative events, players can experience history not as a collection of facts, but as a living, breathing narrative shaped by human resilience, emotion, and decision-making. Our game takes place at the heart of the Manhattan Project—Los Alamos, 1943—and allows players to bond with eminent historical figures and pedestrians, vicariously reliving the diverse ethical dilemmas, scientific breakthroughs, and political tensions that permeated the age. Through these interactions, players develop empathy and a nuanced appreciation for the complexities of historical events, turning history from a mere paragraph between pages to a dynamic and sentient being, that breathes through us today. What it does The Anachronist is an educational mystery game that “time warps” players into a historical period that is unknown to them prior to completing the game. Their task? Identify the time and place by carefully observing surroundings, interacting with characters, and analyzing historical details, with a slight twist: Don’t get caught! While learning hints and gaining further context through every conversation, the player must also be conscious of the fact that they should not arouse suspicion, that they are potentially from the future. Figures within our game range from children, who were brought to Los Alamos as their parents were involved in the Manhattan Project, to figures who symbolize the Manhattan Project to us today. Navigating this world is not just knowing the “timeline” or “facts” of the events, which we grade through a quiz; but instead understanding the very fabric of the community that they are teleported to. How we built it We built The Anachronist using the Nitrode game engine, custom-made Blender models, and advanced triggers, interactions, and animation loops. Our 20+ NPC characters were designed through reconstruction of historical figures (and others) based on VLMs, and tailored to our purpose through mesh texture rigging. LLMs, such as Open AI and Gemini’s models, allow players to engage in conversations not only with historical figures but also with everyday people from the past, bringing history to life. We implemented LLM-powered dialogue systems, leveraging retrieval augmented generation. As such, we were able to prompt 20+ NPC based on the historical context and agent-specific profiles, which allowed for conversations that were both accurate and consistently “in-character” that performed robustly across diverse conversational inputs of the player, which could range from questions and comments about everyday life, technical questions tailored to the historical protegé in their presence, to conversations which engage with deep ethical questions of the age. Furthermore, we leveraged LangChain to manage our agent workflow, which involved both synchronous generation of “evaluation” of the player’s ability to blend in with their environment, as part of our game objective and generating fruitful interactions, fulfilling our education purpose. Additionally, we integrated the LumaLabs AI API to generate realistic videos, which both open and close our game with an immersive storyline and stunning visuals, which immerse the player in the gaming environment. We also used the ElevenLabs API for high-quality voice synthesis, which enhanced the storytelling experience with authentic-sounding dialogue while providing oral guidance to the player regarding the game-playing rules. Challenges we ran into One of our biggest challenges was balancing historical accuracy with engaging gameplay—ensuring realism without sacrificing playability. On the technical side, building an entire 3D world from scratch was a major hurdle, especially since it was our first time developing a 3D game. Creating lifelike characters with unique traits was complex, but we leveraged VLM and an AI-powered pipeline to generate, rig, and animate 3D models from text-to-image inputs. This pushed us to refine our design and animation processes, making the world feel more immersive and authentic. What we learned Achieving the immersive gameplay of The Anachronist taught us extreme attention to 3D modeling, developing complex programmatic interactions, and learning all the technologies of Godot game development from scratch. The challenge taught us how to learn quickly, experiment iteratively, and come up with novel solutions to problems like building 3D interactive AI NPCs with unique personalities, movement patterns, and levels of comfort with sharing information. Moreover, we gained a deeper appreciation for historical nuance. We discovered how small details, such as speech patterns, architecture, and cultural practices, can reveal a great deal about a historical era. Most importantly, we realized the value of player agency in learning. When users are empowered to make their own independent discoveries in the world and inquire openly about tricky issues, they develop a stronger connection to the material. This is the power of immersive worlds in technology – it heightens their ability to think critically about not just the past, but also the present and the future. What's next for The Anachronist Moving forward, we aim to expand our historical settings to include underrepresented periods and cultures, ensuring a more diverse and comprehensive learning experience. We are also exploring the possibility of adding multiplayer or collaborative modes, where players can work together to deduce their location and time period. Another exciting development is the introduction of VR / AR support, which would create an even more immersive time-travel experience. All in all, The Anachronist has the potential to get into classrooms, museums, and cultural institutions as an interactive history-learning tool. By blending history with interactive problem-solving, we hope our game redefines how we engage with the past—making learning not just informative, but truly thrilling. <div