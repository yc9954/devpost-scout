---
slug: "unnamed-pzmyes"
url: "https://devpost.com/software/unnamed-pzmyes"
title: "blueprint"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 608
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/benchmark_measured"
  - "mechanism/graph_reasoning"
  - "mechanism/realtime_stream"
  - "domain/developer_tools"
  - "domain/security_privacy"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# blueprint

> Teams ship faster than they can reason. Our devtool, the missing layer in AI editors, increases leverage and understanding for developers. We make vibe engineering compatible with trust and scale.

[Devpost](https://devpost.com/software/unnamed-pzmyes) · hackathon [[NexHacks]]

## Facets

**mechanism** [[benchmark_measured]] [[graph_reasoning]] [[realtime_stream]]
**domain** [[developer_tools]] [[security_privacy]]
**user** [[developer]]
**substrate** [[code_repository]] [[structured_db]]

**stack** arizeai, ast, gemini, next.js, python, react, react-flow, thetokencompany, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for blueprint

## Body

blueprint displays a relational overview of the codebase blueprint labels high risk vulnerabilities blueprint has dark mode! :) Inspiration LLMs have changed the way people at large -- not only developers -- code. However, with people pushing code faster than they can think, risk increases. Current tools for understanding code (e.g. long paragraphs of documentation) are often not user-friendly or convenient. We wanted to make vibe-engineering more accessible, understandable, trustworthy, and scalable for both developers and non-developers alike by providing detailed insight into repositories through an intuitive and informative developer tool. What it does blueprint is an interactive code editor extension that allows you to visualize any codebase via many different scales of observation and provides unprompted insight to catch your mistakes before you make them. We feature expandable knowledge graphs illustrating file and folder relationships and dependencies, with the ability for developers to summarize at different scales, toggle different file and feature views, add their own "sticky notes" to the viewer, and learn and understand what any codebase does in an instant. blueprint also traces potential vulnerabilities in the code and proactively provides feedback on what should be fixed for best practices and what could break if edited to protect your project. How we built it We used typescript to build an extension and agent that analyzes any codebase in your editor at multiple scales -- higher level structure (subdirectories and file relationships) using AST compression, and smaller features within and across files through efficient codebase compression with The Token Company's bear-1 model and Gemini. The extracted data is mapped to various interactive graphs and explanations that allow you to understand your codebase visually, without losing the bigger picture in infinitely long documentation. This information is also used to search the database, summarize, and identify vulnerabilities and improvements. We also integrated Arize AI to provide observability data about the model's performance for tuning of the agent. Challenges we ran into We took a while to decide how to best display and visualize code for users; we had so many ideas for how to construct our UI that it was difficult to settle on a few key features. We also took a lot of time to evaluate what degree of compression resulted in optimal results and ensuring that we had an accurate agent. Merge conflicts were also a challenge that we had to resolve over the course of the project. Accomplishments that we're proud of We made a practical tool that all of us would genuinely enjoy using with our codebases and can see having a real-world impact on others. We also put a lot of effort and thought into designing the UI/UX, and integrated many of features that we ideated despite the time constraint. What we learned We learned how to improve our collaboration over the course of building the project and how to more effectively subdivide different parts of the codebase to minimize merge conflicts and problems. We also learned about methods for extracting data in a more organized schema rather than freeform summaries, designing informative graphs for users, as well as how to benchmark trust for our AI agents in a measurable way. What's next for blueprint Our next steps would be to reduce latency and cost by finding even more effective methods of compression and LLMs. We would like to implement real-time updating of the extension viewer with user changes by using token compression and git diff, stronger evaluation dashboards for the agent performance that can be used to auto-update and improve the agent as a specific codebase evolves, and upgrade scalability for large repos as we cut down on latency and cost. <div