---
slug: "poltergeist-qa"
url: "https://devpost.com/software/poltergeist-qa"
title: "Poltergeist QA"
hackathon: "Kiroween"
organization: "Kiro"
winner: true
words: 670
team_size: 0
has_repo: false
has_live: false
has_video: true
tags:
  - "project"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/web_dom"
---

# Poltergeist QA

> Summon chaos. Find bugs. Ship confidence

[Devpost](https://devpost.com/software/poltergeist-qa) · hackathon [[Kiroween]]

## Facets

  <sub>weak: cross_origin_web, simulation_digital_twin</sub>
**domain** [[developer_tools]]
  <sub>weak: disaster_emergency</sub>
**user** [[developer]]
  <sub>weak: patient_family</sub>
**substrate** [[web_dom]]
  <sub>weak: code_repository</sub>

**stack** kiro

## Body

Inspiration Every developer has a nightmare: deploying code on Friday at 5 PM, only to have users break it immediately by doing something unexpected. We realized that traditional testing is too polite. It follows happy paths. We wanted to build something evil. Inspired by the concept of "Chaos Engineering" and the Kiroween theme, we asked: "What if we could summon a digital poltergeist to haunt our website, clicking every button and screaming at every input field, just to see if the site survives?" Thus, Poltergeist QA was born—a tool that automates the terror of user testing. What it does Poltergeist QA is a "Chaos Testing" interface. The Summoning: The user enters a target URL (e.g., a staging environment) and clicks "Summon Chaos." The Haunting: Our Playwright-based engine (The Poltergeist) wakes up. It doesn't run a script; it runs a riot. It aggressively clicks buttons, floods forms with "cursed" data, and attempts to trigger race conditions. The Aftermath: The application generates a "Stability Score." If the site crashed, it reports a "Fatal Exorcism." If it survived, it grants a "Survivor Badge." It turns the boring task of QA into a survival horror game for your codebase. How we built it This project fits the Frankenstein category—we stitched together a modern React Frontend with a heavy Automation Backend, brought to life using Kiro. The Skeleton (Architecture): We used a React + Vite + TypeScript stack for the dashboard, styled with Tailwind CSS. The Brain (Kiro Specs): To build this in record time without bugs, we utilized Kiro's Spec-Driven Development. We wrote a master_blueprint.md in the /.kiro/specs directory that enforced: Strict Type Safety (No any allowed). Defensive Coding patterns (Try/Catch blocks everywhere). This prevented Kiro from generating "hallucinated" code, ensuring a production-ready build on the first try. The Skin (Kiro Steering & Vibe Coding): We used Steering Docs to instruct Kiro to adopt a "Digital Necromancer" persona. This allowed us to Vibe Code the UI with "Glitch" animations (Framer Motion) and a dark, uneasy atmosphere without manually tweaking CSS. The Host: We deployed the frontend seamlessly to AWS Amplify, proving that a "Frankenstein" monster can still live in a modern cloud environment. Challenges we ran into The Browser Paradox: Running Playwright (a headless browser automation tool) directly inside a client-side React app is impossible. We had to architect a separation of concerns: building the "Control Center" (UI) first, with a mocked logic layer that simulates the haunting for the demo, while architecting the actual Playwright script (ghost.ts) to run in a future serverless container. Time Constraints: Building a "Production Quality" app in under an hour is stressful. We had to rely entirely on Kiro's ability to generate clean, error-free code from our Specs. Accomplishments that we're proud of Zero Bugs: Thanks to Kiro's Spec-driven approach, our TypeScript compilation had zero errors on the first run. The Aesthetic: We managed to create a UI that feels genuinely "spooky" and thematic without sacrificing usability or accessibility. Frankenstein Deployment: Successfully stitching the code together and hosting it live on AWS Amplify in under 60 minutes. What we learned Spec-Driven Development is a Speed Cheat: Writing the "Rules" first (in the Kiro spec) felt slow for 5 minutes, but it saved us 40 minutes of debugging later. Chaos is Valuable: Building a tool designed to break things taught us how fragile modern web apps actually are. Kiro is a Partner, not a Tool: Using "Steering" to give the AI a persona made the development process feel like pair-programming with a creative director. What's next for Poltergeist QA Full MCP Integration: We plan to use Kiro's MCP (Model Context Protocol) to let the Poltergeist "see" the DOM intelligently. Instead of random clicking, it will use an LLM to identify the "Delete Account" button and try to click it specifically. Serverless Hauntings: Deploying the Playwright engine to AWS Lambda so users can run real hauntings on the cloud. Schedule a Haunting: A feature to let developers schedule the Poltergeist to attack their site every night at 3 AM. <div