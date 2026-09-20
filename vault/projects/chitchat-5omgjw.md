---
slug: "chitchat-5omgjw"
url: "https://devpost.com/software/chitchat-5omgjw"
title: "ChipChat"
hackathon: "UC Berkeley AI Hackathon 2025"
organization: "Cal Hacks"
winner: true
words: 983
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
  - "substrate/web_dom"
---

# ChipChat

> Chips and circuits, from ideation to fabrication in a matter of seconds

[Devpost](https://devpost.com/software/chitchat-5omgjw) · hackathon [[UC Berkeley AI Hackathon 2025]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[geospatial]] [[sensor_telemetry]] [[video_visual]] [[web_dom]]

**stack** bash, css, digitaljs, docker, gemini, git, html, javascript, klayout, letta, node.js, openlane, python, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for chipchat

## Body

User Interface for Physical Display Inspiration Designing hardware is hard. Engineers spend countless hours writing Verilog and refining circuit layouts, while students face a steep learning curve with abstract logic gate diagrams. As undergraduates, we've struggled to actively engage with circuits and learn through hands-on experimentation. We've also seen PhD students spend years iterating on chip designs through long cycles of development and testing. That’s why we built ChipChat - a natural language interface that lets users describe a circuit and instantly gain access to an end-to-end chip development pipeline. From prompt ideation to Verilog code to the final manufacturing file, our goal is to make hardware design more intuitive, accessible, and fast. What it does ChipChat takes multimodal user inputs (as written prompts or image queries) for a circuit description and provides the complete Verilog code, to model the circuit, as well as the comprehensive circuit design diagram and pipeline. Not only can you bring your circuit to life with interactive inputs, but you can also navigate through every component to understand the nontrivial details. You can even take your circuits to the final stage through our chip development channel, where we provide a final .GDS file, which can go straight to the manufacturer. And if you’re stuck, we’ve even provided a circuit assistant, where you can ask questions about the code or diagram and receive accurate, real-time answers. No setup, no simulation hurdles; just type, generate, and explore the logic behind the design in seconds How we built it Through ChipChat, we’ve bridged the gap between hardware description and visual understanding - transforming ideas like “make a 4-bit adder” into interactive Verilog and logic circuits. Specifically, our pipeline output is five-fold: RTL Design (Verilog): Write high-level behavioral code that defines how the circuit should function logically. Synthesis (Synthesized Verilog): Translate the behavioral Verilog into a gate-level netlist using standard logic cells. Place and Route (DEF): Determine the physical locations of each gate and route interconnections on the chip layout. Layout Generation (GDS): Create the final mask layout file containing all geometric layers needed for chip fabrication. Here’s how we did it!: Prompt Input or Hand-Drawn Circuit: Users can either describe a circuit in simple terms or upload a sketch of a hand-drawn logic diagram. Gemini + Letta Integration: The natural language prompt is passed to Gemini, orchestrated through a Letta agent that maintains memory, handles context, and manages tool invocations. Gemini then generates clean Verilog code based on the refined prompt. Backend Yosys (Open-Source Synthesis Tool): The Verilog output is fed into Yosys, which parses and synthesizes the HDL() into a gate-level JSON netlist. This tool handles logic simplification and ensures a consistent hardware structure. The synthesized verilog file is parsed through a scratch-made parser to create a .def file. OpenLane (Open-Source Circuit File Conversion Tool) We used OpenLane to create a proprietary file conversion algorithm between the initial verilog file an the final .gds file output. DigitalJS (Open-Source Visualizer): We use DigitalJS, an open-source digital circuit visualization library, to transform the JSON netlist into a browsable HTML circuit schematic. This is fed into Digital.js, which renders the gates, wires, and data paths using HTML and SVG (scalable vector graphics). Frontend: The final circuit is embedded in our web interface, where users can pan around and explore the structure of their very own design. The frontend was built using React + TypeScript, powered by Vite. The UI is responsive, with interactive panels for circuit assistant chat, Verilog code modules, and circuit visualization. Users can type prompts, view the generated code, and play around the logic schematic, all entirely in a seamless interface. Challenges we ran into There’s (un)surprisingly little data for chip design, making it quite difficult to find an initial approach to generate end-to-end circuit designs. We were able to find tools like Yosys and DigitalJS, that allowed us to convert complex Verilog logic into HTML and SVG-based components. We also filled in the gaps between missing dependencies and mismanaged packages by creating a custom-built parser from scratch to convert synthesized Verilog Files to .DEF files in preparation for tapeout (chip manufacturing). At times, Gemini would generate incomplete or incorrect Verilog, which caused synthesis errors in Yosys (e.g. generating the circuit) and all subsequent pipeline stages. Accomplishments that we're proud of We’re incredibly proud of the pipeline that we’ve created over the past 24 hours. We’ve consistently struggled with circuit design in our research, classes, and personal projects. To have a resource that could help us grow as well as thousands of others aspiring to learn the nuances of circuit design is a tremendous feeling. What we learned From deploying on Vercel to integrating essential and critical agents like Letta, we learned a plethora of exciting things during the past 24 hours. Letta was an entirely new tool for us, but it quickly became the backbone of our pipeline – coordinating tasks, triggering inference, and maintaining flow between all of our components. Paired with Gemini’s instant image-to-text processing, we were able to generate Verilog, visualize circuits, and complete the entire process in seconds. While we began this project with only a high-level understanding of chip design, we finished with a comprehensive view of the entire hardware development lifecycle — from Verilog generation and synthesis to placement, routing, and GDS layout generation. Along the way, we also learned how to make UIs that are not just functional but simple, intuitive, and deeply impactful. What's next for ChipChat Within only a day, we’ve been able to create an end-to-end circuit design platform, that’s not only interactive and educational, but also provides key files for fabrication. We strive to now develop a proprietary model to help understand how to build full-scale analog and digital circuits, and eventually complex hardware such as CPU and GPUs. These applications could redefine industry and research, where billions of dollars are spent on chip performance and efficiency. <div