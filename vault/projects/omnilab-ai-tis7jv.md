---
slug: "omnilab-ai-tis7jv"
url: "https://devpost.com/software/omnilab-ai-tis7jv"
title: "OmniLab AI"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 633
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "mechanism/structural_withholding"
  - "domain/education"
  - "domain/scientific_research"
  - "domain/supply_logistics"
  - "user/researcher"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
---

# OmniLab AI

> Experience chemical experiments you've never done before in a virtual lab.

[Devpost](https://devpost.com/software/omnilab-ai-tis7jv) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]] [[structural_withholding]]
**domain** [[education]] [[scientific_research]] [[supply_logistics]]
**user** [[researcher]]
**substrate** [[genomic_bio]] [[geospatial]] [[sensor_telemetry]]

**stack** bootstrap, css3, django, dotenv, git, html5, javascript, openai, python, sqlite, typescript

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- what's next for omnilab ai

## Body

OmniLab core interface showing reactive fluid analytics, dynamic equations, and real-time safety rules inside an Erlenmeyer flask. Fully optimized UI featuring a sleek Dark Mode environment with active thermal heating and bubbling animations. Seamless apparatus selector allowing fluid physics integration across laboratory Beakers, Test Tubes, and Bunsen Burners. The interactive Chemical Grid dropdown menu allowing users to easily select and mix core matrix compounds and elements. Inspiration The inspiration came from remembering how static and unengaging school chemistry textbooks could be, combined with the lack of accessible, high-quality laboratory equipment in many remote schools. I wanted to build a bridge between complex chemical theory and interactive visual learning. By leveraging advanced AI alongside modern web rendering techniques, I realized I could create a safe, virtual environment where anyone could experiment with chemicals without real-world hazards. What it does OmniLab AI is an interactive, academic-grade chemistry simulator that visualizes and find chemical reactions in real time. Users can select and mix compounds within three dynamic glass vessels (Flasks, Beakers, or Test Tubes), apply thermal heat using a virtual Bunsen burner, and see advanced physics-based fluid animations. Instantly, the backend processes the mixture to output balanced molecular equations, thermodynamics analysis, high-density explanations, and critical safety rules with active command verbs for physical execution. How I built it I engineered OmniLab AI using a powerful, multi-layered architecture. The backend is powered by Django, utilizing custom prompt structures connected to LLM APIs for robust JSON processing of reaction analytics. On the frontend, I crafted a high-performance rendering system using HTML5 Canvas and Vanilla JavaScript (ESModules) to simulate real-time fluid waves, dynamic color transitions, and particle-based boiling effects. I integrated TypeScript to ensure strict type-safety, enhance code maintainability, and scale the frontend architecture reliably. I also used Bootstrap 5 for a responsive layout and configured a secure .env system for infrastructure stability. Challenges I ran into One of the toughest challenges was managing the asynchronous state cycle between the AI payload and the frontend rendering loops. Initially, the Canvas loop would try to update fluid colors before the JSON response fully resolved, leading to null pointer exceptions ( TypeError: Cannot read properties of null (reading 'map') ). I also faced edge cases where complex mixtures caused JSON formatting mismatches, which required designing strict validation structures and solid fallback error-handling loops on the client side. Accomplishments that I'm proud of I am incredibly proud of creating a seamless fluid animation system that mathematically calculates fluid height and wave behavior relative to the chosen glassware. Achieving a smooth, cross-fading color transition algorithm that morphs the liquid based on the reaction outcome was a big win. Additionally, creating a highly functional and responsive user interface that switches beautifully between light and dark modes while keeping layout consistency felt deeply rewarding. What I learned Building this project taught me a lot about strict state lifecycle management in modern JavaScript and the importance of precise data-contract enforcement when integrating AI outputs into runtime UI elements. It also deepened my understanding of how TypeScript eliminates runtime errors during complex data binding and structural typing. I also sharpened my skills in UI/UX architecture, discovering how to distill high-density academic and chemical data into a clean, minimalist dashboard that doesn't overwhelm the user. What's next for OmniLab AI The next phase of OmniLab AI will focus on scaling both the laboratory inventory and the rendering complexity. First, I plan to introduce a much wider variety of laboratory apparatus—such as volumetric pipettes, condenser tubes, and distillation setups—while engineering a system that allows them to interconnectedly work together as a synchronized pipeline. Furthermore, I will push the boundaries of the visual engine by optimizing fluid physics, adding intricate phase-change indicators, and implementing advanced thermodynamic visual effects to make the digital experimentation feel even more realistic and immersive. <div