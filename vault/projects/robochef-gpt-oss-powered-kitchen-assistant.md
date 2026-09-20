---
slug: "robochef-gpt-oss-powered-kitchen-assistant"
url: "https://devpost.com/software/robochef-gpt-oss-powered-kitchen-assistant"
title: "RoboChef: GPT-OSS Powered Kitchen Assistant"
hackathon: "OpenAI Open Model Hackathon"
organization: "OpenAI"
winner: true
words: 552
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/on_device_local"
  - "mechanism/realtime_stream"
  - "substrate/structured_db"
---

# RoboChef: GPT-OSS Powered Kitchen Assistant

> Ask for a dish, get it done. Our GPT-OSS kitchen assistant turns natural language into robot actions, orchestrating Isaac GR00T with a live UI that tracks progress and next steps.

[Devpost](https://devpost.com/software/robochef-gpt-oss-powered-kitchen-assistant) · hackathon [[OpenAI Open Model Hackathon]]

## Facets

**mechanism** [[on_device_local]] [[realtime_stream]]
**substrate** [[structured_db]]

**stack** gpt-oss, gr00t, huggingface, lerobot, love, ollama, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- why end-to-end ai models for controlling the robot instead of classical inverse kinematics?
- what's next for robochef: gpt-oss powered kitchen assistant

## Body

Inspiration We wanted to push the boundaries of what open models can do in robotics. Kitchens are complex environments with many objects, actions, and sequences. A true assistant needs reasoning, planning, and physical execution, so we combined GPT-OSS with NVIDIA Isaac GR00T and the SO-100 robotic arm to bring the idea of an AI-powered robotic chef to life. What it does RoboChef takes natural language instructions like “make me a pineapple smoothie” and breaks them down into executable steps. GPT-OSS generates the sequence of actions needed, expressed in natural language (e.g., “open the cabinet door”, “pick up the pineapple”, “place it in the pot”). These instructions are passed to the execution tool, which drives Isaac GR00T and the SO-100 robotic arm to carry them out. While RoboChef is executing, a live UI keeps the user informed: showing the current kitchen state, the action in progress, and what’s coming next. By blending reasoning, robotics, and feedback, the system feels like a true assistant. How we built it GPT-OSS handles reasoning and generates flexible natural-language actions. A single execution tool takes any action GPT-OSS outputs and passes it to the robotics layer. Isaac GR00T translates these instructions into precise motions for the SO-100 robotic arm . A real-time UI visualizes progress, the current state of the kitchen, and the next action. Isaac GR00T was fine-tuned to our embodiment (SO-100 robotic arm) for reliable, precise control, using training data that we collected by teleoperating the robot. Explore our dataset on Hugging Face (first 1200 episodes kept private) Challenges we ran into Handling uncertainty and variability in the kitchen environment. Designing a UI that feels intuitive while hiding technical complexity under the hood. Accomplishments that we're proud of Built an end-to-end pipeline from natural language to robotic execution. Successfully demonstrated multi-step cooking tasks like preparing a pineapple smoothie. Integrated open models with state-of-the-art robotics (GPT-OSS + Isaac GR00T + SO-100 arm). Designed a clean, informative UI for real-time kitchen updates. Ran the entire pipeline locally on a single RTX 4090 (24GB VRAM), proving that advanced reasoning and robotics can work without cloud dependency. What we learned GPT-OSS is powerful at reasoning through multi-step tasks when paired with a general execution interface. Robotics requires a balance between high-level reasoning and low-level motor control. Clear user feedback builds trust in autonomous systems. Hackathons are great for stress-testing ambitious integrations across AI, robotics, and UI. Why end-to-end AI models for controlling the robot instead of classical inverse kinematics? Classical control methods like inverse kinematics excel in highly controlled environments such as factories, where every object's position, shape, and condition are predetermined. But home kitchens are unpredictable, objects may be placed differently, containers vary in size, and conditions change. With an end-to-end vision-language-action (VLA) model like Isaac GR00T , our system adapts to these dynamic environments. Instead of relying on rigid control pipelines, RoboChef can interpret instructions and act flexibly in real-world settings, making it far better suited for personal assistants in everyday homes. What's next for RoboChef: GPT-OSS Powered Kitchen Assistant Expand the action set to cover more cooking scenarios and recipes. Improve the UI with voice feedback and multimodal updates (text + vision). Experiment with a humanoid platform such as Unitree G1 , exploring how RoboChef could operate in a form factor closer to a human assistant. <div