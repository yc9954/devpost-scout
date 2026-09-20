---
slug: "estireq"
url: "https://devpost.com/software/estireq"
title: "EstiReq"
hackathon: "Red Hat and Intel AI Hackathon"
organization: "Red Hat"
winner: true
words: 670
team_size: 1
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/mental_health"
  - "user/developer"
---

# EstiReq

> Transforming Requirements into Actionable Estimates.

[Devpost](https://devpost.com/software/estireq) · hackathon [[Red Hat and Intel AI Hackathon]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]] [[mental_health]]
**user** [[developer]]
  <sub>weak: financial_record</sub>

**stack** cloud, flask, gemini, jupyter, openai, openshift, openvino, python

## How they structured the write-up

- inspiration
- problem statement
- our solution
- how we built it
- future scope

## Body

Inspiration Team leaders in software development often struggle with managing tasks and meeting tight deadlines. New requirements can appear suddenly, requiring quick and accurate time estimates, which can be difficult to achieve. The process of breaking down tasks and figuring out the time needed for each one often consumes a lot of time, slowing down progress. Miscommunication between team members and stakeholders further complicates this, as unclear instructions can lead to inefficiencies and errors. Additionally, managing task dependencies becomes a challenge, as delays in one task can hold up the rest, making it harder to allocate resources effectively. Moreover, tight deadlines add pressure, making it challenging to maintain quality. Developers may feel rushed and may have to skip planning or thorough testing to meet deadlines, increasing the risk of bugs and unfinished features. These issues not only hinder smooth workflow but also increase the likelihood of delays and decreased product quality, causing burnout among team members. Balancing all of these aspects while keeping the project on track is a constant struggle for team leaders. Problem Statement In current software development processes, team leaders often face challenges in managing multiple tasks and tight deadlines. New requirements can come up unexpectedly, and leaders manually need to estimate how much time each task will take and provide clear instructions on how to build them. This process is usually slow and takes a lot of time, which can delay progress and affect the team’s ability to focus on actual work. Challenges: Slow Time Estimates: Estimating how long tasks will take is a time-consuming process, which can delay the project. Unclear Instructions: It’s difficult to quickly create clear and actionable steps for developers, leading to confusion and mistakes. Changing Requirements: New tasks or changes often come up suddenly, making it hard to keep everything organized and on schedule. Less Focus on Development: A lot of time is spent on planning and estimating, leaving less time for the actual work. Our Solution The solution is an AI-powered tool designed to help development teams by providing quick time estimates and detailed implementation guides for new tasks. Instead of spending hours figuring out how long a task will take, the AI analyzes the requirements and gives an accurate estimate in no time. This helps project managers make better decisions and avoid delays. In addition, the AI generates step-by-step implementation guides, making it easier for junior developers to understand and execute tasks. It provides clear instructions, code snippets, and best practices, so junior developers can work more independently. By leveraging a Retrieval-Augmented Generation (RAG) approach, the AI retrieves relevant information from past tasks and documentation to generate precise and context-aware recommendations. By automating these processes, the team can focus more on building the product and less on planning, keeping the project on track and improving efficiency. How we built it Key Features of the Solution Analyzes User Stories: Uses Sentence Transformers to understand and extract details from project requirements (user stories). Compares with Past Tasks: Implements Retrieval-Augmented Generation (RAG) with FAISS to compare current tasks with similar past ones for better context. Accurate Time Estimates: Provides precise time estimates by analyzing the user stories and using embeddings for comparison with past tasks. Step-by-Step Guides: Generates clear, detailed implementation guides for tasks, helping developers understand what needs to be done. Instructions for Junior Developers: Offers simple, easy-to-follow instructions and code snippets, making it easier for junior developers to execute tasks. Improves Team Efficiency: Automates the planning and estimation process, helping the team focus on development. Hosted on OpenShift, it can be tested via Postman or curl. Future Scope The future scope of the solution includes enhancing AI models for more accurate task estimation and analysis, enabling automated task prioritization to help project managers make better decisions. Expanding integration with more project management tools like Jira and Trello will streamline workflows, Additionally, a user feedback loop will help the AI learn and improve over time, and implementing voice and natural language input will make the system more accessible and user-friendly. <div