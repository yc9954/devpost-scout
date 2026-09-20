---
slug: "signs-of-crime-by-adonous-tech"
url: "https://devpost.com/software/signs-of-crime-by-adonous-tech"
title: "Signs of Crime by Adonous Tech"
hackathon: "Alexa Skills Challenge: In-Skill Purchasing"
organization: "Amazon"
winner: true
words: 342
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
---

# Signs of Crime by Adonous Tech

> A crime-solving simulation for Alexa! You are the detective working with your AI sidekick. Together, you interview a host of AI witnesses. Use your skills of interrogation to solve the case.

[Devpost](https://devpost.com/software/signs-of-crime-by-adonous-tech) · hackathon [[Alexa Skills Challenge- In-Skill Purchasing]]

## Facets

**mechanism** [[simulation_digital_twin]]
  <sub>weak: graph_reasoning</sub>
  <sub>weak: developer_tools</sub>
  <sub>weak: code_repository</sub>

**stack** alexa, amazon-alexa

## Body

Signs of Crime Logo I had the idea to build some type of crime solving simulation Alexa game skill for a couple of years. I first started working on it when the SDK was still in version 1! Consequently, I had to scrap the in-progress skill and start from scratch. I am a huge fan of forensics, so I thought this would be a natural Signs of Crime is a crime solving simulation Alexa Skill. You are a detective working with Alexa as you AI sidekick. After listening to the active case briefing, you can learn about the witnesses for the case. The main currency of the game is interview attempts. You lose interview attempts if you make the wrong choices during witness interviews. You are awarded achievements based on your historical number of interview attempts. After each conversational turn in a witness interview, Alexa will ask you for next steps. If you choose correctly, you can proceed with the dialog. If you choose incorrectly, you lose points (interview attempts). For each conversational turn with a witness, you will have the opportunity to accuse the witness. If you accuse the correct witness, you solve the case. If you incorrectly accuse a witness, you lose multiple interview attempts. This skill offers premium content in the form of additional interview attempts. You can purchase various inskill products to enhance and extend gameplay. I relied on the dialog model, manual dialog handling, and entity resolution for the core game mechanic. The source code is written in TypeScript. I ran into some issues when initially attempting to model the entire dialog in the interaction model and relying on automatic delegation. I quickly learned that you must manually handle the dialog for more complex scenarios, such as interactive games. I am proud to have finished this game which I believe is a unique concept. What's next for Signs of Crime by Adonous Tech We will continue to add new cases and characters. We hope the game becomes popular and customers enjoy playing and solving virtual cases. <div