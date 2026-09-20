---
slug: "neuroblocks-cz7n9k"
url: "https://devpost.com/software/neuroblocks-cz7n9k"
title: "NeuroBlocks"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 1019
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/simulation_digital_twin"
  - "domain/education"
  - "domain/finance_payments"
  - "domain/scientific_research"
  - "user/developer"
  - "user/educator_student"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# NeuroBlocks

> No setup. No code. Just drag, connect, and learn ML.

[Devpost](https://devpost.com/software/neuroblocks-cz7n9k) · hackathon [[TreeHacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[simulation_digital_twin]]
**domain** [[education]] [[finance_payments]] [[scientific_research]]
**user** [[developer]] [[educator_student]] [[researcher]]
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[structured_db]] [[web_dom]]

**stack** anthropic, claude, fastapi, google-cloud, next.js, openai, postgresql, python, pytorch, runpod, supabase, tailwindcss, typescript, vercel

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for neuroblocks
- tech stack
- links
- team

## Body

Playground for model building Homepage Challenges to learn quickly Agent generating NeuroBlocks Running inference on a trained MINST model Inspiration For all of us on the team, our first interaction with programming was block coding. It taught us logic and thinking without memorization or messy syntax. It developed our love for computer programming. Our goal with NeuroBlocks is to do the same for the next generation of engineers. Machine learning and deep learning are the foundations of the tech products we’ve become familiar with, such as ChatGPT, Gemini, and Claude. By teaching students about the fundamentals of Artificial Intelligence, our team proudly can say that we contributed to a new revolution. What it does NeuroBlocks is a visual, drag-and-drop educational platform for building and understanding complex neural architectures. Think of it as a "LEGO for AI"—not only do we provide the manual for you to learn and understand, but we also give you a playground to create. You can learn the foundation skills in research papers in a sand-boxed environment or choose to start from scratch and figure it all out on your own! Key Features: BlockAI Agent Understand neural architectures better using our AI agent that can design its own networks and help you improve yours Drag-and-Drop Interface : Build neural networks by dragging blocks (layers) onto a canvas and connecting them Real-Time Shape Propagation : Visualize and understand tensor dimensions flow through your network as you build it Interactive Training : Train your networks with live loss graphs and accuracy metrics Custom Datasets : Solve challenges you are interested in by uploading your data Challenge Mode : Complete pre-built challenges to learn neural network concepts progressively Supabase Integration : Save and load your trained models PyTorch Backend : Real training powered by PyTorch, not just simulations Inference : Run inference on your trained models through the UI Whether you're learning the basics with an MNIST digit classifier or experimenting with complex architectures like ResNets, NeuroBlocks makes the abstract concrete. How we built it NeuroBlocks is a full-stack application with a sophisticated visual canvas system: Frontend (Next.js + TypeScript + Tailwind) Built with Next.js 14 using the App Router for modern React patterns Custom-built NeuralCanvas system for the block-based graph editor Block palette with draggable neural network components (Linear, Conv2d, ReLU, Dropout, etc.) Real-time shape propagation engine that validates and displays tensor dimensions Training panel with live loss/accuracy graphs Backend (FastAPI + PyTorch + RunPod) Python REST API built with FastAPI for async operations PyTorch integration for actual neural network training (not just visualization) Dynamic model construction from graph JSON Training endpoints with real-time progress updates Scalable training models on RunPod Database (Supabase) PostgreSQL database for storing user playgrounds and challenges Supabase Auth for user authentication Architecture Highlights: Modular component system: NeuralCanvas is a self-contained feature within the frontend Type-safe with TypeScript throughout Graph-based data model: networks are represented as nodes and edges Shape inference system that validates network architectures before training Challenges we ran into Shape Propagation : Getting tensor dimensions to flow correctly through arbitrary network graphs was complex. We had to implement a topological sort algorithm and handle branching/merging paths (like ResNet skip connections). Real-Time Visualization : Rendering activations and weights for large layers without killing browser performance required careful optimization—we ended up implementing sampling and WebGL rendering for larger tensors. Backend-Frontend Sync : Keeping the visual representation synchronized with the actual PyTorch model was tricky. We built a graph-to-PyTorch translator that validates user-defined architectures. Edge Routing : Drawing smooth, non-overlapping connections between blocks required a custom routing algorithm that considers block positions and avoids collisions. Challenge System : Designing progressive challenges that teach neural network concepts while remaining solvable required careful educational design and testing. Accomplishments that we're proud of The Agent : The BlockAI agent that can understand our custom block language, reason about proper neural architecture design, and drag in blocks to the playground itself. Not only did it help users, but it also helped us propose our own AI systems. Shape Propagation That Just Works : The system automatically validates your architecture and shows you exactly what tensor shapes flow through each layer. No more cryptic "dimension mismatch" errors—you see the problem visually. Real Training, Real Models : Unlike many educational tools that just simulate, NeuroBlocks trains actual PyTorch models that could be exported and used in production. Smooth User Experience : The drag-and-drop interface feels natural and responsive. Building networks is genuinely fun. Educational Impact : We've had complete beginners build their first neural network and understand concepts like convolution, pooling, and activation functions through hands-on experimentation. What we learned Visual abstraction is powerful : Representing complex mathematical operations as draggable blocks makes them accessible. The right metaphor (LEGO blocks) helps people build mental models. Real-time feedback accelerates learning : Seeing shape propagation and activations as you build helps users catch mistakes immediately and understand architecture decisions. Graph-based UIs are hard : Managing state in a visual node-based editor is significantly more complex than traditional forms. We learned a lot about data structures and state management. Performance matters for interactivity : Smooth 60fps interactions were crucial for the "playground" feel. We optimized heavily and learned techniques like Canvas batching and request animation frames. Educational design is an art : Creating challenges that teach without frustrating required iterating on difficulty curves and providing the right hints at the right times. What's next for NeuroBlocks We truly want to connect with educators to spread our product to students: Partner with high schools or universities to integrate our software into the classroom Work with course platforms like Coursera or Udemy to supplement lecture material with interactive network design Connect with researchers who upload their work to our site, which can then be broken down for users Tech Stack Frontend : Next.js 14, TypeScript, Tailwind CSS, React Backend : FastAPI, PyTorch, Python, OpenAI API, RunPod Database : Supabase (PostgreSQL), Supabase Auth Visualization : Chart.js, HTML Canvas API Deployment : Vercel (frontend), GCS (backend) Links GitHub Repository : https://github.com/tupdaily/AIPlayground Live Demo : https://neuroblocks.vercel.app/login Team Motivate others to be smarter, just as others motivated us. <div