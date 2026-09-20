---
slug: "gdelt-open-intelligence-agent"
url: "https://devpost.com/software/gdelt-open-intelligence-agent"
title: "GDELT Open Intelligence Agent"
hackathon: "Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph"
organization: "ArangoDB"
winner: true
words: 456
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# GDELT Open Intelligence Agent

> A web app that uses LLM agents to help you query the GDELT Open Intelligence knowledge graph in natural language and visualize the output of your queries

[Devpost](https://devpost.com/software/gdelt-open-intelligence-agent) · hackathon [[Building the Next-Gen Agentic App with GraphRAG - NVIDIA cuGraph]]

## Facets

**mechanism** [[graph_reasoning]] [[human_in_the_loop]] [[realtime_stream]] [[retrieval_grounding]]
**substrate** [[geospatial]] [[structured_db]]

**stack** arangodb, cugraph, langchain, langgraph, networkx, openai, python

## How they structured the write-up

- inspiration
- what it does
- how i built it
- challenges
- accomplishments
- what i learned
- what’s next for gdelt open intelligence agent

## Body

Inspiration I wanted to build a single, seamless system where an LLM can analyze geopolitical events (from the GDELT dataset) by leveraging powerful search capabilities, graph analytics, and a user-friendly interface – all orchestrated under an agentic pattern. The potential to glean real-time insights from a massive global events dataset was a compelling challenge and a big inspiration for me. What it does The GDELT Open Intelligence Agent accepts natural language queries about global events, then dynamically selects the appropriate tools to: Retrieve structured data via AQL (including read and write). Perform text-based searching/ranking (FTS) and vector search on event descriptions. Execute advanced spatiotemporal graph analytics accelerated by cuGraph. Return results in a user-friendly format through a Streamlit interface and graph visualization. How I built it Agentic Pattern —> ReWOO: I used a ReWOO-based (Reasoning Without Observation) approach for orchestrating an LLM’s plan-and-execute workflow. Human in the Loop for Update/Delete: Critical updates and deletes require human confirmation to mitigate potential mistakes from the agent. Full text search, Geospatial, & Vector Search: Combined ArangoDB’s native full-text, geospatial, and vector search features for partial matches, location based tasks, semantic similarity queries. Memory: Stored context across conversation turns so the agent can recall prior user queries/decisions. Graph Visualization: Rendered results in a plotly chart, showing how events, actors, and locations interconnect. Streamlit Interface: Provided an accessible UI for interactive queries, letting non-technical users query and visualize results. Challenges Agentic Pattern —> Plan and Execute: While powerful for complex tasks, it can be slower and overkill for simpler queries. ReAct can lead to wasted calls and cost, plus limited traceability. I needed careful orchestration to balance costs and speed. I spent a lot of time trying to get these two patterns to work for me, but they turned out to be unsuitable for my usecase. Accomplishments Successfully handling various types of queries: from partial text searches to advanced network centralities, all under a single agent that reasons about the best tools for each request. What I learned Agentic Design Patterns: I explored how ReWOO, ReAct, and Plan-and-Execute differ and how to best apply each. GPU Acceleration for Graph Analytics: Offloading heavy computations can greatly improve performance. For graphs with over 100k nodes and edges, CPU is infeasible. cuGraph scales very well! Designing Agents for Graph Databases: I discovered best practices for bridging LLM reasoning with ArangoDB’s graph and search features. Features of ArangoDB: Embracing ArangoSearch, multi-model queries (AQL, graph traversals, geospatial, analyzers), vector indexing, and more. What’s next for GDELT Open Intelligence Agent Further refine the Agentic and GraphRAG patterns to boost accuracy and reduce latency. Explore additional embeddings and improved vector indexes for faster semantic search. Expand the Streamlit interface with more interactive analysis and real-time data ingestion. <div