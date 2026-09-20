---
slug: "markcodepolo-by-freakmont-warriors"
url: "https://devpost.com/software/markcodepolo-by-freakmont-warriors"
title: "MarkCodePolo by Freakmont Warriors"
hackathon: "LA Hacks 2026"
organization: "LA Hacks"
winner: true
words: 1316
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/document_pdf"
  - "substrate/financial_record"
  - "substrate/geospatial"
  - "substrate/structured_db"
  - "substrate/web_dom"
---

# MarkCodePolo by Freakmont Warriors

> Agents waste large amounts of tokens for context retrieval. MarkCodePolo fixes this by generating graphs that map out relationships in your codebase for your agent to understand.

[Devpost](https://devpost.com/software/markcodepolo-by-freakmont-warriors) · hackathon [[LA Hacks 2026]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
  <sub>weak: cross_origin_web</sub>
**domain** [[developer_tools]]
**user** [[developer]]
**substrate** [[code_repository]] [[document_pdf]] [[financial_record]] [[geospatial]] [[structured_db]] [[web_dom]]

**stack** agentverse, claude, css, docker, fastapi, fetch.ai, figma, figma-make, gemini, git, github, mcp, mongodb, next.js

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for markcodepolo by freakmont warriors

## Body

tiers visualization page login page profile information projects dashboard home page Inspiration Large codebases are intimidating to navigate, both for human engineers onboarding to unfamiliar repositories and for AI coding agents that consume substantial token budgets retrieving context before producing useful output. The latter problem is structural: every time an agent reads source files to answer a question, it pays a cost in latency, dollars, and context window space. Existing tooling treats this as unavoidable. A second observation reinforced the first. Unified Modeling Language (UML) diagrams — visual representations of class hierarchies, component relationships, and state transitions — have long been the industry's answer to codebase comprehension. They fail in practice because they decay. A diagram drawn at the start of a sprint is stale by the end of it, and no engineer wants to redraw boxes and arrows after every refactor. MarkCodePolo was built at the intersection of these two problems. If a system can automatically extract structural relationships from a repository and present them as a navigable graph, it serves both audiences at once: human engineers get a living architectural map, and AI agents get a compressed structural index they can consult instead of grepping through thousands of files. What it does MarkCodePolo is a website that generates diagrams for both user and agent. Given a repository, it will build a structured index of the codebase and produce a graph of the code that a user can learn from. Instead of having an AI coding agent parse through each individual line of the raw files, MarkCodePolo uses a network of Agents that are handled by an orchestrator and built with Fetch.ai’s uAgents framework to index the codebase and extract relevant symbols, data flow, architectural organization, and implicit constraints. This information is passed through Gemini LLM to produce a structured graph with annotations that the user ultimately sees. This graph can be navigated and used from the website, an MCP server, through OmegaClaw, or directly on the carto-coordinator agent on ASI:One. How we built it We first used Figma Make to document our initial vision of the platform’s UI. Our frontend utilizes Next.js and React to display the website and graphs, using SSE for live updates. The backend incorporates FastAPI and uvicorn in Python, with MongoDB Atlas as our database to store symbols, references, clusters, invariants, and embeddings from the agents’ parsing of the codebase. For parsing, we used tree-sitter with Python and Typescript to conduct a static AST analysis to parse the code without actually running it. Our agent layer utilized Fetch.ai uagents and ugents_core to run a Bureau of six specialized Agents, including an orchestrator, called the coordinator, that receives queries via chat protocol and handles the remaining Agents. The MCP server allows this platform to be connected to any MCP host. The Bureau’s Agents are powered by Fetch.ai’s ASI:One. The coordinator is the only public Agent available on Agentverse, and it virtually handles how the other Agents are called. The Bureau runs each of the six as separate uAgents, but the coordinator is a single entry point centralized ability to classify the queries and call the appropriate specialist agent. This project also incorporates an OmegaClaw skill in the sense that if OmegaClaw is used to call this Agent (the carto-coordinator on Agentverse), the carto-coordinator can receive questions via the chat protocol and continue its actions as it normally would on the web platform. These are written to the MongoDB Atlas and are given a Gemini embedding vector while the graph builds live. The second layer reads the call edges from MongoDB Atlas that were written in layer 1 and then constructs and stores flow records like call paths from A to B to C. These records are stored this way so that the system can follow these chains rather than re-traversing the graph after a user’s query. The third layer handles semantic clustering of the code, and these clusters are passed to Gemini for annotations including name, role, and conventions. This layer also identifies the most representative file, or surface exemplar, of each cluster and dependency edges across clusters based on imports in the code. The fourth and final layer handles invariants by finding implicit constraints on symbols, such as docstrings or comments, and sends to Gemini to extract any pre- or postconditions and link them to the associated symbol. Challenges we ran into As we worked on the Agentverse integration, we quickly realized we had to use a Bureau to run the Agents because without it, there would be more latency in the system since each Agent would have to send messages to each other and be individually deployed, called, and activated on Agentverse. This was against our initial goal of making a more efficient system. Since we had an orchestrator agent, the Coordinator, we decided to deploy only one agent to Agentverse and run the other five virtually as an internal mesh, using the Coordinator to handle those Agents and run them behind the scenes. Using the carto-coordinator on Agentverse resulted in the following error: Please provide a repo_hash. Send JSON: {"repo_hash": "", "question": ""}. It arose because we needed to run the local backend to index a repository, but we didn’t have a repository that had been pre-indexed, which resulted in the above statement being outputted by the agent. This was a challenge that we were eventually able to fix. We had to modify the coordinator in such a way that if it were individually queried on Agentverse with a GitHub link, it would index it and store in the database. The user can then query the Agent about parts of the code to find where different things are stored or handled. Accomplishments that we're proud of MarkCodePolo is a web app that successfully uses a network of Agents in a Bureau to assist software engineers and AI code agents while developing. Since this industry often involves using and understanding sizable codebases, our application provides a unique, scalable, and low-latency solution to a problem faced by countless developers every day. Our network of Agents greatly reduces the toil of intense token consumption by commonly-used AI coding agents. What we learned We learned how to use frameworks we hadn’t been acquainted with before, specifically Fetch.ai’s uagents and Agentverse platform. There was a considerable amount of AI agents used in this hack, which gave us a better understanding of how agentic AI systems can be improved and also used as a network of agents to create more efficient systems. We also learned how to visualize tiers, layers, packages, and classes. We studied UML diagrams and how to display them based on the file hierarchy that is uploaded. What's next for MarkCodePolo by Freakmont Warriors The OmegaClaw integration layer has been coded into the platform. However, due to a time crunch we weren’t able to test the feature on OmegaClaw/ASI:One. A future goal for this project would be to finalize this integration. Also, using the Agent directly from Agentverse brings the issue that repo_hash is not a portable record because it specifies a repo that has been indexed specifically by our local backend. This issue could potentially be solved if we use a remote server and application, or make another agent to index a repo and send that to the coordinator to handle. A new feature we would hope to add would be a search bar to search through files and the graph to make navigation more streamlined. Also, integrating GitHub and implementing a GitHub or Google sign-in would be another big step in improving our platform’s accessibility. Some more helpful additions would be to incorporate Fetch.ai’s Agentverse into our UI so that the capabilities of carto-coordinator can be more deeply combined with the platform’s setup, and potentially adding another agent to produce a simple visualization similar to one on the actual platform in the carto-coordinator chat on Agentverse if prompted. <div