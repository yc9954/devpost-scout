---
slug: "on-second-thought"
url: "https://devpost.com/software/on-second-thought"
title: "On Second Thought"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 362
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "domain/education"
  - "domain/media_journalism"
  - "user/educator_student"
---

# On Second Thought

> Can you spot the fake news? Play & hone your critical thinking skills.

[Devpost](https://devpost.com/software/on-second-thought) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets

**domain** [[education]] [[media_journalism]]
**user** [[educator_student]]

**stack** amazon-web-services, bedrock, claude, llama, partyrock, stable-diffusion

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for on second thought

## Body

Overview of app Generated article Interacting with Skeptibot Inspiration With the lowering of the barrier to create & distribute digital media, critical thinking has become more important than ever. This project aims to help people build these skills in an engaging way. What it does "On Second Thought" is an interactive experience where users analyze scenarios designed to mimic real-world articles that might contain logical fallacies & hidden biases. A chatbot, "Skeptibot," guides them through analysis and prompts deeper thinking. How we built it PartyRock with its widget system was used to create Skeptibot's dialogue and interactive logic and to create the scenarios. Challenges we ran into Ensuring the AI-generated scenarios were believable yet identifiably flawed and also balancing the difficulty of scenarios to be challenging without being discouraging. Considerable effort was also spent tuning the params & prompts provided to each model as well as figuring out which model is suitable for which type of task. I found it necessary to break tasks down into different widgets with each acting as a kind of "Agent" that fed output to other widgets. Fortunately, PartyRock made this wayyyyy less complicated than it could've been. Accomplishments that we're proud of Successfully integrating the AI generator into the critical thinking scenarios. Designing a chatbot personality that is encouraging and helpful. Figuring out the appropriate models, params & prompts for each task. What we learned I learned how easy building Generative AI apps can be! There's no need to deal with multiple programming languages & figure out costs for different APIs, handling tokens etc. I can just focus on exactly what I want to get done instead of all the things I need to do before even starting. I also learned about the pervasiveness of subtle biases and logical fallacies. These can be easily missed, especially if an article is designed to elicit strong emotional reactions. From this, we can see the importance of clear frameworks for critical analysis that can be applied broadly. What's next for On Second Thought Expanding the scenario library to cover more misinformation types. Incorporating difficulty levels to cater to different age groups. Developing a classroom-friendly version with teacher resources. <div