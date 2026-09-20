---
slug: "langsketch"
url: "https://devpost.com/software/langsketch"
title: "LangSketch"
hackathon: "Hack the North 2025"
organization: "Hack the North"
winner: true
words: 835
team_size: 5
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "mechanism/vision_ocr"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/video_visual"
---

# LangSketch

> LangSketch is a visual agent builder that leverages Databricks for data processing and Martian rule routing for affordable drag-and-drop agent creation, making agentic workflows accessible for all.

[Devpost](https://devpost.com/software/langsketch) · hackathon [[Hack the North 2025]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]] [[vision_ocr]]
**substrate** [[document_pdf]] [[financial_record]] [[geospatial]] [[sensor_telemetry]] [[video_visual]]
  <sub>weak: web_dom</sub>

**stack** appimage, asteval, chart.js, css, databricks, databricks-vector-search, dateparser, deimos-router, dmg, dotenv, electron, fastapi, font-awesome, git

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for langsketch

## Body

Drag-and-drop interface to visually design agentic workflows without code. Agent creation screen with flexible custom configurations. Utility functions like calculator, date parser, JSON parser, and list ops for agent calls. Settings page to add provider keys and Databricks credentials. Landing page to open local folders and import custom tools for agents. LangSketch: Making Agentic Workflows Accessible Through Visual Design Inspiration The world of AI agents and autonomous workflows has long been dominated by complex frameworks, such as LangChain and LangGraph, creating a steep learning curve that excludes many potential users. We envisioned a future where anyone, regardless of their technical background, could harness the power of agentic workflows through intuitive visual design tools. LangSketch was born from this vision: a no-code, visual development environment that transforms the complexity of agentic workflows into an accessible, drag-and-drop experience. What it does LangSketch is a comprehensive platform that democratizes agentic AI development through a visual, no-code interface. Users can drag and drop agents and functions onto a canvas, connect them visually to create workflows, and instantly compile them into production-ready Python code. The platform leverages the Martian Deimos router for intelligent, cost-optimized model selection, automatically choosing the best AI model based on task complexity and agent capabilities. Our deep Databricks integration offers enterprise-grade data management, featuring Delta Lake storage, RAG embeddings for document retrieval, and comprehensive analytics dashboards that track performance, costs, and execution metrics in real-time. It removes the barriers of learning complex APIs while maintaining the full power and flexibility of modern AI agent systems. How we built it We built LangSketch using a multi-layered architecture combining Electron for the desktop interface, Python for the agent runtime, and Databricks for enterprise analytics. The visual canvas system enables drag-and-drop workflow creation with real-time connection management. The Martian Deimos router integration offers sophisticated model selection through custom routing rules that analyze agent capabilities, task complexity, and message length to automatically select between Claude, GPT-4, and other models for an optimal cost-performance balance. Our Databricks integration leverages Delta Lake for ACID transactions and time-travel queries, stores all agent executions with comprehensive metadata, and enables RAG embeddings through vector search capabilities. The platform uses Databricks notebooks for data processing and visualization. At the same time, the dynamic agent runtime supports dynamic tool loading, comprehensive input/output validation with Pydantic schemas, and visual-to-code compilation that generates production-ready Python from visual workflows. Challenges we ran into The biggest challenges included managing complex state across the visual canvas, agent runtime, and analytics systems, which were solved by building a centralized state management system. Creating intuitive visual connections between workflow components required developing a sophisticated connection system with real-time preview, collision detection, and dynamic redrawing during zoom/pan operations. Implementing intelligent model routing that truly understands agent capabilities required comprehensive agent description generation and context-aware routing rules. Finally, providing enterprise-grade data management and analytics demanded deep integration with Databricks, including Delta Lake storage, RAG embeddings pipelines, and real-time performance monitoring dashboards. Accomplishments that we're proud of We're most proud of creating the first visual-to-code compilation system that generates production Python from drag-and-drop workflows, achieving up to 60% cost reduction through intelligent model routing, and building a truly no-code interface that makes complex agentic AI accessible to non-technical users. The platform successfully combines enterprise-grade capabilities (Delta Lake storage, ACID transactions, comprehensive analytics) with an intuitive visual interface. We also pioneered context-aware model selection that automatically chooses the optimal AI model based on agent capabilities and task complexity, while maintaining complete transparency in routing decisions. What we learned We learned that democratizing complex technology requires not just simplifying the interface, but fundamentally rethinking the entire development workflow. The key insight was that users don't want to learn frameworks; they want to solve problems. We discovered that intelligent routing isn't just about cost optimization, but about matching the right model to the right task based on a comprehensive understanding of agent capabilities. We also learned that enterprise users need both simplicity and power, requiring us to build sophisticated backend systems while maintaining an intuitive frontend. Most importantly, we realized that visual programming can be just as powerful as traditional coding when combined with intelligent compilation and comprehensive tooling. What's next for LangSketch We're expanding LangSketch to support multi-modal agents for image, audio, and video processing, enabling real-time collaborative workflow design, and building a marketplace for community-driven agent and tool sharing. A significant focus is on adding visual fine-tuning capabilities that leverage Databricks MLflow for model training and optimization, allowing users to customize models directly within the visual interface. We're also developing advanced Martian routing rules for specialized use cases, such as domain-specific model selection and custom performance optimization strategies. Additionally, we're working on predictive performance modelling and optimization features, advanced analytics with machine learning insights, and integration with more enterprise data sources. The goal is to create a complete ecosystem where users can design, deploy, monitor, fine-tune, and optimize agentic workflows entirely through visual interfaces, making AI development truly accessible to everyone while maintaining enterprise-grade capabilities and performance. <div