---
slug: "omni-stem-ai-powered-eco-build-lab"
url: "https://devpost.com/software/omni-stem-ai-powered-eco-build-lab"
title: "Omni-STEM: AI-Powered Eco-Build Lab"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 727
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/vision_ocr"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/scientific_research"
  - "user/developer"
  - "user/educator_student"
  - "user/government_staff"
  - "substrate/video_visual"
---

# Omni-STEM: AI-Powered Eco-Build Lab

> "Turning household waste into a professional engineering lab. Omni-STEM uses AI to scan scrap, gamify physics learning, and teach CAD—democratizing STEM for students at zero hardware cost."

[Devpost](https://devpost.com/software/omni-stem-ai-powered-eco-build-lab) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[vision_ocr]]
**domain** [[developer_tools]] [[education]] [[scientific_research]]
**user** [[developer]] [[educator_student]] [[government_staff]]
**substrate** [[video_visual]]

**stack** google-gemini-api, json, pillow-(pil), python, streamlit

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges we ran into
- accomplishments that we're proud of
- what i learned
- what's next for omni-stem: ai-powered eco-build lab

## Body

"Modular by design: The three-pillar backend powering the Omni-STEM ecosystem." "Spotting the potential: AI that turns everyday clutter into zero-cost blueprints." "Gamified engineering: Prove the physics behind your prototype to level up." "Digital mastery: Learning industrial CAD constraints in your native tongue." Inspiration Diving deep into core subjects like circuit theory and electrodynamics highlights a stark reality: there is a massive gap between textbook equations and hands-on hardware experience. Millions of students lack access to expensive STEM kits, while our households simultaneously generate tons of waste—plastic bottles, cardboard, and discarded electronics. Omni-STEM was born from a simple realization: What if we could turn discarded "kachra" into a zero-cost, high-end engineering laboratory? The goal was to shift the educational paradigm from passive screen time to active, eco-conscious physical prototyping without being limited by a hardware budget. What it does Omni-STEM is a fully gamified, AI-powered EdTech platform featuring three core modules designed to build real engineering intuition: AI Vision Engine: Users upload photos of household scrap. The multimodal AI accurately identifies materials—even in messy backgrounds—and generates scientifically viable, step-by-step eco-prototypes. It also features instant language translation (e.g., Hinglish) to make engineering accessible in the user's native tongue. RPG Master Loop: Rather than spoon-feeding answers, the AI acts as an engaging Dungeon Master. Students must justify the engineering logic behind their assembly. Validated logic is rewarded with XP and level-ups, celebrated with on-screen animations to keep student retention high. Virtual CAD Lab: For students without immediate physical materials, this module bridges the gap between cardboard prototyping and professional 3D software. It digitally teaches industrial-level assembly constraints (like 'Mate', 'Flush', and 'Concentric'), ensuring students understand degrees of freedom. A critical concern with DIY hardware is safety. We specifically engineered the AI prompts to act as a strict safety officer. It will never suggest harmful chemical mixtures, dangerous high-voltage electrical modifications, or the use of hazardous tools, ensuring a 100% safe learning environment for minors. How I built it Omni-STEM is built on a lightweight, highly responsive Streamlit architecture using Python. At the core of the application lies the Google Gemini API, which handles the heavy lifting of multimodal object detection and interactive logic validation. The frontend utilizes custom CSS to create an immersive, gamified user interface that steps away from traditional educational apps. User state management and progression (XP, Levels) are handled persistently using local JSON architecture. For the frontend, we designed custom CSS featuring a calming "Eco-Green" color palette. This isn't just an aesthetic choice to match the sustainability theme; it is specifically designed to reduce eye strain and cognitive fatigue during extended learning sessions. Challenges we ran into The most significant technical hurdle was achieving "intelligent filtering." In a real-world scenario, a student's desk is cluttered. Ensuring the vision model could accurately identify relevant engineering components while ignoring background noise (like hangers or bowls) required extensive prompt engineering and parameter tuning. Additionally, designing the RPG-style validation system was complex; the AI's system instructions had to be strictly fine-tuned to prevent it from giving away the answers, forcing it to act as an evaluator that genuinely tests the student's mechanical intuition. Accomplishments that we're proud of Building a fully functional, full-stack AI application as a solo developer from scratch is a massive milestone. Successfully integrating a seamless reward loop that triggers based on actual physics logic validation fundamentally changes how students interact with AI. Furthermore, proving that the vision engine can take simple scrap and conceptualize complex, functional prototypes—like a working River Surface Water Cleaner—demonstrates the tangible, real-world impact of this platform. What I learned The development process reinforced the immense value of bridging digital intelligence with physical "jugaad" (resourceful engineering). Fine-tuning the LLM to act as a strict educational guide showcased the power of targeted prompt constraints. Most importantly, building Omni-STEM proved that high-quality, hands-on STEM education doesn't require a high-budget hardware kit—it just requires resourcefulness and the right digital environment. What's next for Omni-STEM: AI-Powered Eco-Build Lab The immediate next step is community scalability. The introduction of a global "Eco-Leaderboard" will allow students to compete based on the complexity of their upcycled projects. Furthermore, expanding the Virtual CAD Lab to include direct export integrations to industry-standard software like Autodesk Inventor and Fusion 360 will allow students to eventually 3D print the custom parts they design, completely closing the loop between household scrap and professional digital manufacturing. <div