---
slug: "axisgen"
url: "https://devpost.com/software/axisgen"
title: "AxisGen"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 442
team_size: 3
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "substrate/structured_db"
  - "substrate/video_visual"
---

# AxisGen

> AxisGen turns one robot-task prompt into simulation-ready Physical AI prompts by varying lighting, placement, embodiment, and safety constraints, creating scalable, robust datasets before deployment

[Devpost](https://devpost.com/software/axisgen) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[simulation_digital_twin]]
**substrate** [[structured_db]] [[video_visual]]

**stack** ai, cli, cloud, configuration, dataset, generation, github, gpu, gr00t-compatible, json, lerobot, llm, nebius, npa

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for axisgen

## Body

Inspiration AxisGen was inspired by how tools like LangChain made LLM workflows easier to structure, chain, and deploy. We wanted to bring a similar idea to Physical AI: a layer that turns a simple beginner-level robot task prompt into a broader set of simulation-ready prompts. Robot deployment should not only be accessible to experts with custom simulation knowledge. AxisGen aims to make robotic deployment more accessible for any customized task by helping users quickly generate the diverse scenarios needed for robust training and evaluation. What it does AxisGen takes one robot-task prompt and expands it across environmental axes such as lighting, object placement, clutter, camera viewpoint, distractors, task difficulty, robot embodiment, and safety constraints. Instead of producing one fixed scenario, it generates a body of structured prompts that can be used to create more diverse simulation datasets for robot learning. How we built it We built AxisGen as a prompt expansion pipeline for Physical AI simulation. We designed structured templates that preserve the core task while systematically changing environmental variables. We used Nebius Physical AI, Isaac Lab planning, Python, and prompt-generation logic to connect a simple input task to many simulation-ready scenario descriptions. Challenges we ran into The biggest challenge was balancing variation with consistency. If the generated prompts change too much, they no longer represent the original task. If they change too little, the dataset is not diverse enough. We also had to think carefully about which environmental axes actually matter for robot robustness and how to format the prompts so they are useful for simulation. Accomplishments that we're proud of We are proud that AxisGen turns a single task idea into a scalable set of useful scenario variations. Instead of focusing on one specific robot task, we created a general system that can support many customized tasks. Our proof of concept showed that prompt expansion can become a practical layer in making Physical AI dataset generation more accessible. What we learned We learned that prompt structure matters a lot for robotics. A good robot-learning prompt needs more than a task description; it needs environment details, object variation, safety constraints, and success conditions. We also learned that robustness can start before training, at the data-generation and scenario-design stage. What's next for AxisGen Next, we want to connect AxisGen more directly with Isaac Lab so generated prompts can automatically become simulation configurations. We also want to add scoring for prompt quality, generate larger scenario batches, export datasets into LeRobot or GR00T-compatible formats, and test how much environmental-axis variation improves downstream robot model performance. Long term, we want AxisGen to help make robotic deployment easier for anyone building a customized robot task. <div