---
slug: "doracodelens"
url: "https://devpost.com/software/doracodelens"
title: "DoraCodeLens"
hackathon: "Code with Kiro Hackathon"
organization: "Kiro"
winner: true
words: 642
team_size: 2
has_repo: false
has_live: true
has_video: false
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# DoraCodeLens

> A VS Code super-power for Python devs. It builds mind maps of modules, classes, functions with complexity scores, sketches DB diagrams and JSON tools - making code exploration visual & lightning-fast.

[Devpost](https://devpost.com/software/doracodelens) · hackathon [[Code with Kiro Hackathon]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
  <sub>weak: legal_professional</sub>
**substrate** [[code_repository]] [[geospatial]] [[sensor_telemetry]] [[structured_db]]
  <sub>weak: web_dom</sub>

**stack** chart.js, css, cytoscape, extension, html, javascript, kiro, python, typescript

## How they structured the write-up

- inspiration
- note to the judges
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for doracodelens

## Body

Inspiration Every developer knows the pain of diving into an unfamiliar codebase — endless scrolling, manual tracing, and juggling scattered tools. We wanted to replace that friction with clarity : a single workspace inside VS Code where a Python project comes alive as a visual mind map . That’s how DoraCodeLens was born. Note to the judges Cytoscape js for current file or full code analysis mindmap is not loading on marketplace vs code extension due to .vscodeignore, so there are 2 options to test option 1 Clone https://github.com/devendradora/dora-codelens Click on Run on VS Code or Kiro > Start Debugging option 2 can I push new package to marketplace with new .vscodeignore with 1 line removed that prevented cytoscape to be loaded as I want my first time users to view code mind map properly ? PR: https://github.com/devendradora/dora-codelens/pull/1/files Blog : https://dev.to/devendradora/doracodelens-4goa What it does It analyzes Python projects and delivers: Mind maps of modules, classes, methods, and functions — annotated with real-time complexity scores of any file or full code and inline complexities displayed on top of functions & classes. Database-schema diagrams , extracted directly from ORM models. Git analytics , including contributor timelines and activity stats. Productivity tools such as JSON minify/beautify and a tree viewer. All of this runs right inside the editor — no context switching, no clutter. How we built it Static Analysis Core Implemented AST-based scanners to detect modules, classes, methods, and functions. Computed complexity metrics in real time for each code element. Database Schema Extraction Parsed ORM models (Django, Flask-SQLAlchemy, FastAPI etx) to infer tables, fields, and relationships. Generated database-schema diagrams directly from source code, giving developers an instant view of data structures. Visualization Engine Used Cytoscape.js to create smooth, interactive mind maps and database diagrams. Built a responsive VS Code webview to host and render graphs with smart layouts. Productivity Add-ons Integrated JSON utilities for formatting, minifying, and exploring data in a tree view. Added Git analytics to visualize contributor timelines, commit frequency, and ownership. AI Pair Programming Leveraged Kiro to generate boilerplate for VS Code panels, suggest AST traversal logic, and craft Cytoscape configurations. Adopted a spec-to-code workflow , letting Kiro implement features from clear specifications, which accelerated development and kept the architecture clean. Challenges we ran into Performance: Large repositories slowed AST parsing, so we built caching and incremental analysis to keep the experience snappy. Graph Readability: Massive projects produced dense visuals — adaptive layouts and filtering solved this. Accomplishments that we're proud of Interactive Mind Maps – Built a smooth, real-time graph of every module, class, method, and function with live complexity metrics. Database Schema Discovery – Automatically parsed ORM models to generate clean relationship diagrams directly from source code. Lightning-Fast Insights – Optimized AST parsing with caching and incremental analysis so even large repos stay responsive. Unified Developer Experience – Brought mind maps, DB diagrams, Git analytics, and JSON tools together inside VS Code — no context switching. AI-Powered Development – Used Kiro to speed up boilerplate generation, improve visualization logic, and keep our codebase well-structured. What we learned Building DoraCodeLens taught us how to blend deep static analysis with intuitive visuals. Along the way, we mastered: Designing clear specs and tasks for Kiro, steering conversations, hooks and “vibe coding” sessions. Parsing Python’s Abstract Syntax Trees (AST) to model structure and measure complexity. Rendering large datasets as mind maps and schema diagrams inside VS Code. Explored complexity metrics What's next for DoraCodeLens Framework Coverage – Extend schema and code analysis to support more frameworks. Deeper Complexity Metrics – Add maintainability index, cognitive complexity, and hotspots over time. Collaboration Tools – Enable sharing mind maps and schema diagrams with teammates in real time. Interactive Docs – Export mind maps and DB diagrams as shareable, auto-updating documentation. AI-Assisted Insights – Use LLMs to explain complex functions, suggest refactors, or highlight risky dependencies. <div