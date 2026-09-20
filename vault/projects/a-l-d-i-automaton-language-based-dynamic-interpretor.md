---
slug: "a-l-d-i-automaton-language-based-dynamic-interpretor"
url: "https://devpost.com/software/a-l-d-i-automaton-language-based-dynamic-interpretor"
title: "A.L.D.I. — Automaton Language-based Dynamic Interpretor"
hackathon: "TreeHacks 2023"
organization: "Stanford TreeHacks"
winner: true
words: 403
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/voice_speech"
  - "domain/developer_tools"
  - "user/developer"
---

# A.L.D.I. — Automaton Language-based Dynamic Interpretor

> Using LLMs for easy access interfaces for robotic applications. With minimal code, allow LLMs to construct your API calls for complex systems and custom tasks.

[Devpost](https://devpost.com/software/a-l-d-i-automaton-language-based-dynamic-interpretor) · hackathon [[TreeHacks 2023]]

## Facets

**mechanism** [[voice_speech]]
**domain** [[developer_tools]]
**user** [[developer]]

**stack** gpt-3, skydio, whispr

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for a.l.d.i. — automaton language-based dynamic interpretor

## Body

Inspiration LLMs are already revolutionizing software, but how can we use them for hardware 🤖? Consider a drone — we can manually control it pretty easily via a joystick 🕹️. But how can we leverage LLMs to teach it to perform tasks that we want automatically, especially without a dedicated API? APIs are the way to interact with code, but natural language is how people think. User use-cases can be complex, and it’s practically impossible to design a Python wrapper for everything and anything a user might do. Can we do better than static APIs for robotic applications? What it does A developer tool for translating natural language 📖 into automata routines ⚙️. We want to be able to conduct long-horizon automaton tasks based off natural language, even in the absense of formal APIs and documentation. Imagine a search-and-rescue team telling the drone to "search for a person wearing red, and around 1.6m in the 100 meters paramter" and the drone being able to search immediately without code! To do so, we can define a couple basic function primitives, and task LLMs with decomposing our more complex tasks into a series of primitive function calls. Why? Developers are happier, less functions to write! Users are happier, they can perform more complex tasks, without having to write code to automate the drone. How we built it We use a Skydio Drone as our initial use case, using: Skydio Drone Custom-Built Drone SDK Networking + Ethernet local network AI Text Completion (e.g. OpenAI GPT3) AI Voice Recognition (e.g. OpenAI Whisper) Challenges we ran into The Skydio Drone SDK had not been updated in over 4 years and contained many hidden endpoints, so we had to write our own scaffolding to be able to communicate with the drone. Accomplishments that we're proud of Getting the drone to listen to our voice commands and handle non-trivial tasks that it had not been programmed to enact (e.g. "move in a 1 m square without turning"). What we learned Hardware is hard, but we can use LLMs to abstract away a lot of the complexity. What's next for A.L.D.I. — Automaton Language-based Dynamic Interpretor Add more functionality to the drone by finetuning an instruction-following language model to handle even more complex tasks, such as "pick up my package at Tressider", "follow me while I ride my bike and take pictures", "explore a 100m radius and find my bike". <div