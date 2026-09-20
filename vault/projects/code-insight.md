---
slug: "code-insight"
url: "https://devpost.com/software/code-insight"
title: "CodeInsight"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 737
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
---

# CodeInsight

> Help developers understand codebases faster

[Devpost](https://devpost.com/software/code-insight) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]]
  <sub>weak: web_dom</sub>

**stack** flask, groq, html, javascript, mistral, perplexity, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for codeinsight

## Body

Us after understanding all the codebases sample use of our app Inspiration Both of us have worked at big corporate companies where we have had to be onboarded to a certain application very fast. It is often hard as an intern to automatically come in and understand the code base just like that. So we decided to create a tool that allows you to analyze a code base and see the function dependency which is nicely visualized and also chat to mistral AI to learn more about the code base. In terms of UI, we had some inspiration from Obsidian. What it does CodeInsight is an interactive tool that analyzes a codebase to generate a dynamic visualization of function dependencies. It extracts function definitions and their call relationships from a selected repository and displays them as an interactive network graph. Users can click on a node to view the corresponding source code in a draggable, resizable panel, with animated arrows that show the direct call flow—both outgoing (caller to callee) and incoming (callee from caller). In addition, CodeInsight integrates a chatbot powered by an AI model to answer questions about the codebase, helping developers quickly gain an understanding of complex systems. How we built it We built CodeInsight using a combination of Python and JavaScript. On the back end, Python’s AST module performs static analysis to extract functions and their call dependencies from a codebase. This data is then served as JSON via a Flask API. For the front end, we used D3.js to render an interactive, force-directed graph of the function dependencies, adding features like zooming and dragging. We integrated Interact.js to allow code panels (that display the source code for each function) to be draggable and resizable, and Highlight.js provides syntax highlighting. To further enrich the user experience, we integrated a chatbot powered by Groq’s Mistral model (accessed via our configured API client) that lets users ask questions about the codebase. Finally, we packaged the whole thing into a standalone application using pywebview so users can simply select a repository without needing any command-line interaction. Challenges we ran into One of our biggest challenges was ensuring accurate static analysis in a way that filtered out built-in or external functions while capturing the true internal dependencies of a complex codebase. We also had to balance performance with interactivity—making sure our visualization remained responsive even for large repositories. Integrating multiple libraries (D3.js for visualization, Interact.js for UI controls, and Highlight.js for code formatting) and ensuring they all worked harmoniously presented additional hurdles. Finally, deploying the app in a consistent manner across different environments and handling subtle differences in runtime behavior was a significant challenge. Accomplishments that we're proud of We’re proud that CodeInsight not only generates a clear and interactive visualization of function dependencies but also provides an intuitive interface that helps users explore code in a dynamic way. The integration of real-time animated call flows (with directional arrows and moving dots) gives users an immediate sense of the underlying code structure. Additionally, the ability to open detailed code panels and interact with an AI chatbot for further insights makes Code Insight a comprehensive onboarding and analysis tool. Seeing our tool help new developers understand complex codebases quickly is a real win for us. What we learned Working on Code Insight taught us a great deal about static code analysis and the nuances of parsing complex codebases. We gained valuable experience integrating diverse technologies—ranging from Python’s AST for analysis, to D3.js and Interact.js for building a rich, interactive UI, and even leveraging AI via Groq’s Mixtral model. We learned how to manage cross-environment deployments and how subtle differences in runtime or browser behavior can affect the end-user experience. Most importantly, we discovered the critical importance of effective visualizations in speeding up developer onboarding and code comprehension. What's next for CodeInsight Looking ahead, we plan to extend CodeInsight with dynamic analysis features that capture runtime call flows, further enhancing our static analysis results. We’d like to integrate advanced filtering and search options—such as grouping functions by modules or highlighting high-complexity areas—to provide deeper insights into the codebase. Additionally, we aim to expand the chatbot’s capabilities so that it can answer even more nuanced questions about the code. Ultimately, our goal is to create a comprehensive tool that not only accelerates onboarding but also aids in ongoing code maintenance and refactoring, making it an indispensable resource for developers. <div