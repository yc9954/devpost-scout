---
slug: "wingpal"
url: "https://devpost.com/software/wingpal"
title: "WingPal"
hackathon: "The PartyRock Generative AI Hackathon by AWS"
organization: "Amazon"
winner: true
words: 348
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
---

# WingPal

> WingPal is a pitch-crafting wingman. Simply answer 5 questions about yourself, and it will create the perfect elevator pitch for you.

[Devpost](https://devpost.com/software/wingpal) · hackathon [[The PartyRock Generative AI Hackathon by AWS]]

## Facets


**stack** claude

## How they structured the write-up

- inspiration
- project goal
- how we built it
- testing
- learning

## Body

WingPal Poster Inspiration Our inspiration came from people who are shy having difficulties presenting themselves effectively among others. We were inspired to create a "Wingman" – an AI-powered assistant that could help users present themselves memorably, whether in professional settings like job interviews or casual social situations. Project Goal While many people might have already thought of using AI to help them create pitches, not everyone is good at prompt engineering. A good wingman should be able to know a lot about the person that he is going to pitch. So the goal of our project is to simplify the process, making it accessible to non-experts in prompting them to create pitches tailored to their background and needs. How we built it Our inputs are like breaking down the question of “Tell me about yourself” into smaller pieces that are more digestible: Direct inputs: Basic information like name, pitch setting, audience, time limit, and style preferences. AI-generated questions in "chat": The app asks the user five personalized questions to gain deeper insights. With these inputs, we crafted and iteratively refined an initial prompt to generate tailored elevator pitches. Testing Testing and prompt refinement were crucial in this project. We tested various input scenarios, including skipping questions or requesting changes, to ensure robustness. We encountered and addressed issues like: Question count inconsistencies Redundant questions about known information Hallucinations (including unrealistic details) Through testing, we also discovered limitations in certain pitch types, like casual/flirtatious introductions, where the app performed less effectively. Learning This project provided valuable lessons in prompt engineering. We learned how to: Craft clear prompts Break down user inputs for better comprehension Test with diverse scenarios for robustness One aspect we truly appreciated about working with large language models is the relative ease of addressing issues through prompt refinement. Most bugs or limitations could be resolved by simply adding clear and succinct instructions to the prompt, a process far more efficient than traditional software development where significant resources are often required to find and implement solutions. Overall, this experience deepened our understanding of leveraging language models effectively. <div