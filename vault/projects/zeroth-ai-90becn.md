---
slug: "zeroth-ai-90becn"
url: "https://devpost.com/software/zeroth-ai-90becn"
title: "Zeroth AI"
hackathon: "Frostbyte Hackathon"
organization: "FrostByte Club"
winner: true
words: 723
team_size: 1
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/simulation_digital_twin"
  - "domain/developer_tools"
  - "user/developer"
  - "user/legal_professional"
---

# Zeroth AI

> An autonomous AI coding agent that generates edge cases, stress-tests solutions, and iteratively fixes code to eliminate hidden test case failures.

[Devpost](https://devpost.com/software/zeroth-ai-90becn) · hackathon [[Frostbyte Hackathon]]

## Facets

**mechanism** [[simulation_digital_twin]]
  <sub>weak: realtime_stream, sensor_fusion</sub>
**domain** [[developer_tools]]
  <sub>weak: finance_payments</sub>
**user** [[developer]] [[legal_professional]]
  <sub>weak: financial_record, sensor_telemetry</sub>

**stack** 3.5, 70b), anthropic, asyncpg, axios, c++17, claude, deepseek, fastapi, flash, framer, gemini, google, gpt-4

## Body

System Telemetry Error Logs and Validation Matrix box full processing page home page my coding area Zeroth AI Inspiration Competitive programming platforms such as Codeforces, LeetCode, and CodeChef evaluate solutions using hidden test cases that are not visible to participants. Many developers rely on generative AI tools to write code, but these tools typically provide a single solution without verifying whether it can handle edge cases, large constraints, or hidden judge scenarios. We noticed a major gap: AI can generate code, but it rarely validates its correctness like a competitive programmer would. This inspired us to build Zeroth AI — an autonomous coding agent designed to simulate the way expert programmers test their solutions. Instead of just generating code, Zeroth AI analyzes the problem, generates edge cases, stress-tests the solution, detects failures, and automatically fixes the code until it becomes robust and optimized. Our goal was to create an AI system that helps developers reach a “zeroth-error state” — code that passes both visible and hidden test cases. What it does Zeroth AI is an autonomous AI coding agent designed to improve developer productivity by validating and strengthening algorithmic solutions. When a user provides a programming problem, Zeroth AI: Analyzes the problem statement and understands constraints and input formats. Generates an initial solution using a large language model. Runs the solution against public test cases. Automatically generates additional edge cases and stress tests that simulate hidden judge scenarios. Detects failures and identifies why the solution breaks. Refines and fixes the code automatically through iterative debugging. Optimizes the algorithm to meet time and space constraints. The result is a robust, optimized solution that is far more likely to pass hidden test cases in competitive programming environments. How we built it We built Zeroth AI using a modular architecture designed around an autonomous agent workflow. Core components include: Problem Analyzer – Parses the problem and extracts constraints. Code Generator – Uses an LLM to produce an initial implementation. Execution Engine – Runs the generated code in a controlled environment. Test Case Generator – Creates additional edge cases and stress tests. Failure Analyzer – Identifies why the code fails on certain inputs. Optimization Module – Improves the algorithm’s efficiency. Tech Stack Python (core backend logic) LLM API for reasoning and code generation Streamlit for the interactive web interface Subprocess-based execution engine for running generated code Algorithmic stress testing and dynamic test generation The system runs in a loop where the agent continuously tests, analyzes, and improves the solution until it becomes stable. Challenges we ran into One of the biggest challenges was designing an agent that could reason about failures instead of just generating code repeatedly. Some key difficulties included: Generating meaningful edge cases that resemble hidden judge tests Automatically identifying why a solution failed Ensuring the agent doesn’t get stuck in infinite correction loops Managing execution safety when running generated code Handling large input constraints and performance optimization We also had to carefully design the workflow so the AI could iteratively improve the solution instead of restarting from scratch each time. Accomplishments that we're proud of We are proud that Zeroth AI goes beyond simple code generation and introduces autonomous verification and improvement. Key achievements include: Successfully building an AI agent that stress-tests its own code Implementing automatic edge case generation Creating a system that can identify and fix logical errors Demonstrating how AI can simulate the workflow of a competitive programmer This transforms AI from a code generator into a self-improving coding assistant. What we learned Through this project we learned: How to design agent-based AI systems How LLMs can be combined with programmatic tools The importance of test-driven development in AI-generated code How iterative feedback loops dramatically improve AI outputs We also discovered that the real power of AI agents comes not from generating answers once, but from testing, analyzing, and improving solutions continuously. What's next for Zeroth AI We believe Zeroth AI has the potential to become a powerful tool for developers and competitive programmers. Future plans include: Supporting multiple programming languages (C++, Java, Python) Building a VS Code extension for real-time coding assistance Integrating with competitive programming platforms Adding advanced algorithm analysis and complexity prediction Implementing distributed stress testing for large-scale evaluation Ultimately, we envision Zeroth AI evolving into a full autonomous coding assistant that ensures code reliability before submission. <div