---
slug: "agentbim"
url: "https://devpost.com/software/agentbim"
title: "AgentBIM"
hackathon: "Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph"
organization: "ArangoDB"
winner: true
words: 379
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# AgentBIM

> RAG enabled BIM authoring and processing using natural language

[Devpost](https://devpost.com/software/agentbim) · hackathon [[Building the Next-Gen Agentic App with GraphRAG - NVIDIA cuGraph]]

## Facets

**mechanism** [[graph_reasoning]] [[retrieval_grounding]]
**domain** [[developer_tools]]
**substrate** [[geospatial]] [[structured_db]]

**stack** arangodb, ifc, langchain, langgraph, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agentbim

## Body

Inspiration I was inspired by the challenge of making BIM data more accessible and interactive. Working with BIM models can be tedious, often with multiple back-and-forths. I wanted to create a tool that would allow them to query and explore building information using natural language, simplifying decision-making and collaboration. What it does AgentBIM is an intelligent agent that leverages natural language processing and graph databases to provide interactive access to BIM data. Users can ask questions about building elements, relationships, and spatial properties using plain English. AgentBIM translates these queries into AQL for an ArangoDB graph, which is built from parsed IFC data using IfcOpenShell and NetworkX. It then returns the relevant information, visualized or in text, making BIM data intuitive and actionable. How we built it I started by developing a Python script using IfcOpenShell to parse IFC files and extract building elements and relationships. This data was then transformed into a NetworkX graph for analysis. I used ArangoDB to store the graph data, leveraging its graph database capabilities. The "ArangoGraphQAChain" was implemented using LangChain, which connected the natural language interface to the ArangoDB database. I also incorporated a front-end interface built with Gradio to enhance user interaction. Challenges we ran into Parsing complex IFC files and accurately mapping them to a graph database proved challenging. I struggled with handling various relationship types and ensuring data consistency. Developing a robust natural language processing pipeline that could accurately interpret diverse queries was also difficult. Integrating all these components into a seamless workflow required extensive debugging and optimization. Accomplishments that we're proud of Created a system that allows users to query BIM data using natural language. AgentBIM demonstrates the potential of AI to revolutionize the construction industry. What we learned I gained valuable experience in working with IFC files, graph databases, and natural language processing. I also discovered the power of natural language interfaces for making complex data accessible. What's next for AgentBIM I plan to expand AgentBIM's capabilities by incorporating more advanced natural language processing techniques, including intent recognition and context awareness. I'll also focus on improving the visualization of query results and adding support for more complex queries. I am going to add more robust error handling and increase the amount of IFC properties that are parsed. <div