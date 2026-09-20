---
slug: "jadeai"
url: "https://devpost.com/software/jadeai"
title: "Jade.AI"
hackathon: "Cal Hacks 12.0"
organization: "Cal Hacks"
winner: true
words: 806
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/education"
  - "user/educator_student"
  - "substrate/structured_db"
---

# Jade.AI

> Cursor for Data Analysis

[Devpost](https://devpost.com/software/jadeai) · hackathon [[Cal Hacks 12.0]]

## Facets

**domain** [[education]]
**user** [[educator_student]]
  <sub>weak: researcher</sub>
**substrate** [[structured_db]]

**stack** chart.js, fastapi, groq, pandas, python, react, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for jade.ai

## Body

Jade.AI: Your Conversational Data Analyst Tired of spending 70% of your time cleaning data? Jade.AI is an intelligent, all-in-one platform that lets you clean, analyze, and visualize your data using simple English commands. No code, no app-switching -- just results. Inspiration As a college student passionate about data analysis, I’ve faced a frustrating reality: most of my project time isn't spent on analysis. It's spent on grunt work. I often wasted over 70% of my time just cleaning messy datasets. I was constantly switching between Excel for quick fixes, Pandas for heavy-duty cleaning, SQL for data pulling, and another tool like Tableau for visualization. The process was slow, exhausting, and fragmented. I wanted a single, intelligent, all-in-one solution that could handle all these tasks with just a few natural language commands. I envisioned a "Cursor for data analysis", an AI-first tool that would let me talk to my data. That's why we built Jade.AI. What it does Jade.AI empowers anyone, regardless of their technical background, to work with data effortlessly. It’s as simple as 1-2-3: Upload your data (CSV, Excel, etc.). Type what you want in plain English. Get immediate results. You can clean, manipulate, visualize, and summarize, all in one seamless interface: “Clean the entire dataset” → Jade.AI intelligently handles missing values, removes duplicates, fixes inconsistent formatting, and standardizes data types. “Show a pie chart of the gender distribution” → Instantly generates a beautiful, interactive chart with auto-labeled insights. “What’s the average salary by department?” → Returns a clean summary table or a bar chart, your choice. “Summarize the key findings from this data” → Creates a concise, human-readable report. How we built it We built Jade.AI to be fast, intelligent, and scalable. Frontend: We built a clean and responsive UI using Next.JS to create a seamless, single-page application experience. Backend: We used a Python (FastAPI) backend to create REST APIs that handles all user requests. LLM: We integrated the Groq API as the main LLM to power our natural language-to-action engine. Its incredible speed makes the conversation feel instantaneous. This model interprets user commands and translates them into executable operations. Data Manipulation: The legendary Pandas library is our workhorse. All data cleaning, transformation, and analysis commands are piped through a secure Pandas runtime. Data Visualization: We used Chart.js to generate rich, interactive, and beautiful visualizations that can be embedded directly in the chat interface. Challenges we ran into Prompt Engineering is Deceptive: Getting the LLM to consistently and safely translate a vague command like "fix the messy columns" into the correct sequence of Pandas functions was our biggest hurdle. It required lots of iterative prompt design and building a robust validation layer. Maintaining Data State: Managing the state of a user's DataFrame across multiple, independent API calls was a huge challenge. Our initial implementation was slow and buggy before we used Groq. The Scope Creep: We had so many ideas! We wanted to add SQL database connections, advanced statistical modeling, and more. Focusing on our core loop (Upload → Clean → Analyze → Viz) within the time limit was a real test of discipline. Accomplishments that we're proud of It Actually Works! We have a fully functional, end-to-end demo. You can upload a genuinely messy dataset and walk away with clean data and insightful charts in under two minutes. The "Wow" Moment: The biggest win was testing it on a friend with zero coding experience. They were able to perform a complete data analysis task that would have taken them hours, and they did it with a smile. The "Cursor for Data" Feel: We successfully captured that "magic" feeling. It feels less like a tool and more like an intelligent collaborator, which was our core vision. What we learned LLMs are Interpreters, Not Magicians: The real magic isn't just the LLM; it's the pipeline . The most critical work is building the robust "plumbing" that translates the LLM's intent into safe, executable code . UX is Everything: For a tool aimed at non-technical users, simplicity is the ultimate feature. A single, clear chat box proved to be infinitely more powerful than a complex dashboard. Speed is a Feature: Using an incredibly fast LLM (Groq) was a game-changer. When the analysis feels instant, it encourages creativity and exploration, which is the entire point of data analysis. What's next for Jade.AI We're just getting started. Our vision is to make data analysis as easy as having a conversation. More Data Connectors: We plan to add support for connecting directly to SQL databases, Google Sheets, and other live APIs. Advanced Analytics: We're working on moving beyond descriptive statistics to include predictive modeling. (e.g., "Forecast next quarter's sales based on this data" ). "Analysis History": We want to create a feature that lets users track, revert, and branch their analysis steps, almost like Git for data analysis. <div