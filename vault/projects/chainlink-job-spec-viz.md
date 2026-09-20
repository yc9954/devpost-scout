---
slug: "chainlink-job-spec-viz"
url: "https://devpost.com/software/chainlink-job-spec-viz"
title: "Chainlink Job Spec Viz"
hackathon: "Chainlink Spring 2022 Hackathon"
organization: "Chainlink Labs"
winner: true
words: 425
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
---

# Chainlink Job Spec Viz

> Drag, drop, and connect tasks to visually program your Chainlink job spec. Copy the generated code to your Chainlink node and you're good to go!

[Devpost](https://devpost.com/software/chainlink-job-spec-viz) · hackathon [[Chainlink Spring 2022 Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]

**stack** next.js, react, tailwindcss, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chainlink job spec viz

## Body

GIF First, select the job type and enter any required config. GIF Drag tasks to the workspace. Similarly, each task may have required config fields. GIF Connect tasks together to form a pipeline. 'Power' fields give you quick access to input variables you can use. GIF The 'Codegen' panel will change in realtime as you work. Any lines highlighted in red indicate missing or invalid config. GIF Copy the generated TOML to your clipboard ready to paste into your Chainlink node's job spec config panel! Inspiration A little long-winded but I was originally inspired by an interview between Chainlink and Gains Network where there was some difficulty clarifying how Gains' custom Chainlink DON operated and thought it would be very helpful to facilitate the creation of DONs if there were some tool that could visually simulate the interactions between Chainlink nodes. Getting all node operators and users on the same page about how a DON operates will be extremely important... and hard! I worked backward from this big idea to think about what the first steps to achieve it may be and decided that a similar visual tool for the creation of Chainlink job specs (and their simulated execution) would be a great first step. What it does I've created a drag and drop web-based editor to make it easier to generate Chainlink job specs in TOML format. The generated code can be copied into the Chainlink node's job configuration panel. How we built it Everything is client-side. The app is built with Next.js, Tailwind, React Flow and React DnD. Challenges we ran into Other than the challenge of thinking of ways to make the app as intuitive as possible I was just short on time to create something which covers the full range of job configuration options. I have also noticed a few inconsistencies in the Chainlink docs around some of the v2 tasks so I will look to go back and suggest some edits when I get chance to investigate what the correct content should be. Accomplishments that we're proud of Pleased with the overall UX and getting something that kind of works! What we learned Learned more about the huge variety of Chainlink job types, tasks, and configuration options for each. What's next for Chainlink Job Spec Viz Implement remaining job types and tasks. Allow the reverse process (pasting a completed job spec and displaying a visual representation of it). Extend to simulate inputs and execution of the pipeline. Extend to visual simulation of several Chainlink nodes interacting with one another. <div