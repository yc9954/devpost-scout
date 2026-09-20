---
slug: "commitsense-da5h6s"
url: "https://devpost.com/software/commitsense-da5h6s"
title: "CommitSense"
hackathon: "HackGT 12: Midnight at the Museum"
organization: "HexLabs"
winner: true
words: 735
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# CommitSense

> AI-powered code intelligence that reveals what legacy code does, who wrote it, and why it exists. Uses Snowflake, RAG, and Gemini to turn legacy code into clear, maintainable systems.

[Devpost](https://devpost.com/software/commitsense-da5h6s) · hackathon [[HackGT 12- Midnight at the Museum]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[structured_db]]

**stack** gemini, git, rag, react, shadcnui, snowflakecortex, tailwind, typescript, vite, zod

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for commitsense

## Body

Commit Sense Logo Developer Login Code Explanation Demo Inspiration CommitSense was inspired by our real frustration with legacy code during internships. One teammate spent weeks at a software company trying to decode undocumented fixes and mysterious variables like DONT CHANGE THIS and Magic_Thingy, while the rest of us faced similar onboarding delays in our own roles. We saw how much time and energy were wasted digging through old commits, ticket histories, and scattered comments just to understand why a single line of code existed. These experiences highlighted a clear need for a tool that could instantly explain the purpose, history, and reasoning behind every snippet, sparking our idea to create CommitSense as a way to make onboarding faster and development more efficient. What it does CommitSense is a developer tool that explains legacy code with speed and depth. It stores an entire company’s codebase, commit history, and ticket data in Snowflake, then uses retrieval augmented generation (RAG) to pull precise context for each line of code. This context feeds into the Gemini API, which produces a single clear narrative explaining what the code does, how it works, and why it was written that way. Developers can highlight any snippet to see its full history including who wrote it, when changes occurred, and the reasoning behind every commit, turning scattered documentation into instant actionable insight. How we built it This project was built by integrating Snowflake to securely store and organize large company codebases, commit histories, and ticket data, then connecting that data to a retrieval augmented generation pipeline to provide precise context for each query. We fed this context into the Gemini API to generate clear, line by line explanations that combine functionality, history, and developer intent. We designed an interactive interface where developers can highlight any snippet to instantly see its full narrative, and we refined database schemas, RAG queries, and AI prompts to keep the system fast and accurate across massive, evolving repositories. Challenges we ran into Our biggest challenge was teaching the AI to weave scattered commit messages, ticket histories, and code comments into a single coherent narrative so each explanation felt like one clear story instead of a disconnected list of facts. Legacy repositories often held years of inconsistent naming, missing documentation, and conflicting developer notes, which made it difficult for the retrieval augmented generation pipeline to supply clean context. We had to experiment with data structures, prompt engineering, and context weighting so that Gemini could synthesize these fragments into smooth, accurate explanations while still preserving the technical details that developers rely on. Accomplishments that we're proud of CommitSense turns complex, undocumented codebases into clear, searchable knowledge that developers can trust from day one. The platform securely stores projects in Snowflake, retrieves precise context with retrieval augmented generation, and delivers seamless explanations through the Gemini API. Our interface lets users highlight any snippet to see a full history of commits, developer notes, and reasoning, all presented as one coherent narrative. We are proud that CommitSense not only speeds up onboarding but also sets a new standard for how AI can transform scattered code and comments into immediate, actionable understanding. What we learned Building CommitSense taught us how to work with powerful tools like Snowflake and Gemini at a deep level. We learned how to structure massive codebases and commit histories inside Snowflake for fast, reliable queries, and how to design retrieval augmented generation pipelines that pull only the most relevant context. On the AI side, we gained experience fine tuning prompts and response handling in Gemini so it could merge complex technical details into smooth, human readable explanations. These lessons in data architecture and large language model integration gave us a strong foundation for creating scalable, intelligent developer tools. What's next for CommitSense Looking ahead, we plan to expand CommitSense into a full developer knowledge platform that goes beyond explaining legacy code. Future work will explore deeper integration with version control tools to provide real time insights as new commits are made, advanced analytics to spot patterns in code quality and developer collaboration, and richer context layers such as design documents and test coverage. We also aim to refine our use of Snowflake for even faster querying and extend Gemini’s capabilities to handle larger, more complex repositories. By pursuing these goals, we hope to make CommitSense an essential companion for every software team, turning code history into living, actionable knowledge. <div