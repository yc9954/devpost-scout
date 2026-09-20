---
slug: "sci-sim"
url: "https://devpost.com/software/sci-sim"
title: "Sci Sim"
hackathon: "DSH Hacks V1"
organization: "DreamWeave"
winner: true
words: 885
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/realtime_stream"
  - "mechanism/runtime_tool_creation"
  - "mechanism/sensor_fusion"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "domain/education"
  - "domain/scientific_research"
  - "user/educator_student"
  - "substrate/sensor_telemetry"
---

# Sci Sim

> The context-aware 3D laboratory where science comes alive through AI.

[Devpost](https://devpost.com/software/sci-sim) · hackathon [[DSH Hacks V1]]

## Facets

**mechanism** [[multi_agent]] [[realtime_stream]] [[runtime_tool_creation]] [[sensor_fusion]] [[simulation_digital_twin]]
**domain** [[developer_tools]] [[education]] [[scientific_research]]
**user** [[educator_student]]
**substrate** [[sensor_telemetry]]

**stack** css3, html5, javascript, next.js, openrouter, react, react-katex, rk-4, tailwindcss, three.js, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for sci sim

## Body

Inspiration Science is incredible, but the way we teach it is often tragic. The reality is that so many schools across the globe are deeply underfunded. Kids never get to experience the magic of a real chemistry lab because the school simply can't afford the chemicals, or teachers are terrified that an eager student will drop and shatter an incredibly expensive glass flask. Instead, they are forced to read about these concepts in a textbook or watch a mind-numbingly boring 2D simulation of a pendulum swinging back and forth. No wonder kids get bored and tune out. We built Sci Sim because we believe every student deserves access to a state-of-the-art laboratory that is completely free, 100% unbreakable, and genuinely captivating. We wanted to build a world where kids can splash colorful chemicals, shoot 3D cannons, and fall in love with STEM without costing their schools a dime. What it does There are hundreds of science simulation websites on the internet. But they are almost all entirely static—if a student doesn't understand the complex mathematics happening on screen, they are left behind. Sci Sim is the world's first Context-Aware Autonomous WebGL Laboratory. Yes, students get to interact with beautifully lit 3D environments (pouring titrants, firing parabolic cannons). But the true magic is the Omniscient AI Tutor that acts as the core of the application. The AI Tutor has "eyes" on your simulation. It ingests your live telemetry in real-time (pH levels, trajectory angles, velocities, kinetic energy). It doesn't just act like a generic chatbot; it actually knows that you just launched a ball at 45° with 30m/s velocity, and it will proactively generate interactive, LaTeX-formatted quizzes on the fly to test your comprehension of the exact physical state you just created. How we built it We built the application using Next.js and TailwindCSS to create a stunning, responsive, glassmorphism UI. For the heavy lifting in the labs, we used React Three Fiber (R3F) and Three.js to render the photorealistic 3D environments. We wrote custom physics engines (including Runge-Kutta integration for the pendulum) and piped them directly into the R3F render loop to ensure a buttery smooth 60 FPS. To make the AI Tutor "omniscient", we built a hidden telemetry pipeline that continuously captures the exact math and physics states from the 3D engine (angles, velocity, energy). This raw telemetry is injected as a hidden system context payload via the Vercel AI SDK hooked up to OpenRouter. This clever architecture ensures that whenever a student asks a question, the LLM already inherently knows exactly what they are looking at on screen, allowing it to generate perfectly contextualized LaTeX math formatting and structured JSON quizzes. Challenges we ran into This was a chaotic, ad-hoc build, and we suffered for it! WebGL vs React State: Trying to keep the React UI in sync with a 60FPS 3D physics engine without completely melting the browser or dropping frames was a massive headache. 3D Coordinate Nightmares: We spent hours doing trigonometry just to figure out why our math projectile was literally clipping and warping through the walls of our 3D cannon barrel as it launched. Library Quirks: We battled obscure internal memory crashes (RangeError: offset is out of bounds in Float32Array) when dynamically toggling the 3D trajectory trails. Backslash Hell: The AI Tutor was a nightmare to stabilize. The LLM kept returning improperly escaped LaTeX strings (like \pi) inside its JSON quiz payloads, which would instantly crash the native browser JSON.parse. We had to write a highly aggressive, custom regex interceptor just to sanitize the AI's output on the fly. Accomplishments that we're proud of We are incredibly proud of successfully bridging the gap between raw physics mathematics and generative AI. Building a 3D simulation is hard, but building an AI that can read that simulation is infinitely harder. Having an AI that doesn't just act like a generic chatbot, but actually knows that you just launched a ball at 45° with 30m/s velocity on the surface of Mars, and actively grills you on the precise time of flight, is a complete game-changer for personalized education. We essentially built an autonomous science teacher that lives inside the browser. What we learned We learned that 3D web development is highly unforgiving but incredibly rewarding. We gained a deep understanding of how to manage mutable refs versus React state to optimize performance. We also learned that when dealing with Large Language Models, you absolutely must build robust, fault-tolerant parsing nets, because the AI will find a creative way to break standard JSON. What's next for Sci Sim The ultimate vision for Sci Sim is to evolve our TutorBot into a Multi-Agent Proctor and Curriculum Guide. Instead of a single LLM, we envision a swarm of specialized agents: one agent monitoring the physical telemetry to catch mathematical errors, a psychological agent monitoring engagement and frustration levels (e.g., if a student fails a quiz three times, it shifts to a more empathetic, visually-guided teaching style), and a curriculum agent dynamically generating a multi-year personalized syllabus. Beyond the AI, we want to introduce Multiplayer Labs where students from different computers can join the same 3D room and collaborate on an experiment together, and eventually implement WebXR support so kids can put on a VR headset and literally hold the chemistry flasks in their hands. <div