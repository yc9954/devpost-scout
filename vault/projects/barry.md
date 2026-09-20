---
slug: "barry"
url: "https://devpost.com/software/barry"
title: "CodeSieve"
hackathon: "Nosu AI Hackathon $11,300+ in prizes"
organization: "nosu"
winner: true
words: 499
team_size: 2
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "user/developer"
  - "substrate/code_repository"
---

# CodeSieve

> CodeSieve: Filtering Redundancy, Streamlining Workflows with Machine Learning

[Devpost](https://devpost.com/software/barry) · hackathon [[Nosu AI Hackathon -11-300- in prizes]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]]
**user** [[developer]]
**substrate** [[code_repository]]

**stack** abstract, api, ast, codet5, cosine, faiss, github, json, numpy, python, pytorch, similarity, streamlit, syntax

## Body

Inspiration Software development thrives on collaboration, but in large teams, communication gaps often lead to duplicated efforts, redundant code, and wasted time. Recognizing the inefficiency this creates, we were inspired to build CodeSieve—a tool designed to identify redundancies, surface complementary code, and promote smarter collaboration. By streamlining workflows and reducing technical debt, CodeSieve helps teams focus on innovation rather than repetition. What it does CodeSieve is an advanced code analysis tool that uses FAISS and a CodeT5 model to scan codebases for redundancy and complementarity. It: Takes in a Github repository link, downloads the codebase, parses it into an abstract syntax tree, vectorizes the codebase, and analyzes your codebase. Detects highly similar or duplicate code across large repositories. Recommends complementary classes for methods you write. Offers an intuitive dashboard for developers to visualize and act on results in real time. Think of CodeSieve as a filter for your codebase—sifting out inefficiencies and refining your team’s efforts. How we built it We built CodeSieve using: Python for core functionality, including parsing and analyzing code. FAISS for efficient similarity search, enabling fast and scalable comparisons. CodeT5 for embedding and vectorizing code into a format suitable for similarity analysis. Cosine similarity for redundancy detection between code snippets. Streamlit for an interactive dashboard that visualizes insights, search results, and redundancy analysis. AST (Abstract Syntax Tree) to extract method and class definitions from Python code. GitHub integration to easily fetch and analyze repositories. Challenges we ran into Figuring out how to chunk long pieces of code and compare different granularities, like methods and classes. Parsing diverse codebases and handling edge cases with varying structures and languages. Efficiently vectorizing and comparing large amounts of code while maintaining performance. Balancing the threshold for redundancy detection to minimize false positives without missing meaningful matches. Designing a dashboard that seamlessly integrates insights without overwhelming users. Accomplishments that we're proud of Successfully integrating FAISS and CodeT5 to build a scalable, high-performing solution. Developing a user-friendly Streamlit dashboard that simplifies the visualization of results and encourages developer action. Building a tool that not only identifies redundant code but also surfaces complementary code suggestions. Overcoming technical challenges to deliver a fast, accurate, and intuitive experience. What we learned The strenghts and weaknesses of different methods for code parsing, embedding, and similarity analysis. The power of combining modern tools like FAISS and CodeT5 for efficient and accurate code analysis. How to balance automation with actionable insights to ensure the tool supports, rather than overwhelms, developers. The importance of real-time feedback in improving team collaboration and overall code quality. Best practices for designing intuitive developer tools that integrate seamlessly into existing workflows. What's next for CodeSieve Automated Refactoring: Introducing functionality to automatically refactor redundant code or suggest changes. Advanced Analytics: Providing deeper insights into team coding behavior, technical debt, and opportunities for optimization. AI-Powered Recommendations: Using machine learning to suggest reusable patterns and complementary code across repositories. CI/CD Integration: Embedding CodeSieve directly into CI/CD pipelines to flag redundancies before code is merged. <div