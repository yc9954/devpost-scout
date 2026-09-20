---
slug: "askstreets-querying-and-visualizing-street-networks"
url: "https://devpost.com/software/askstreets-querying-and-visualizing-street-networks"
title: "AskStreets: Querying and Visualizing Street Networks"
hackathon: "Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph"
organization: "ArangoDB"
winner: true
words: 933
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/education"
  - "user/developer"
  - "substrate/geospatial"
---

# AskStreets: Querying and Visualizing Street Networks

> An agentic AI app that uses OpenStreetMap data to answer queries and generate insights into geographic street networks.

[Devpost](https://devpost.com/software/askstreets-querying-and-visualizing-street-networks) · hackathon [[Building the Next-Gen Agentic App with GraphRAG - NVIDIA cuGraph]]

## Facets

**mechanism** [[graph_reasoning]]
**domain** [[education]]
**user** [[developer]]
**substrate** [[geospatial]]

**stack** langchain, langgraph, networkx, openai, openstreetmap, osmnx

## How they structured the write-up

- requirements
- running the code
- inspiration
- what it does
- how i built it
- challenges i ran into
- accomplishments that i'm proud of
- what i learned
- citations
- what's next for askstreets

## Body

Retrieving street networks as graph data with OSMnx AskStreets Sample Query 1 (1/2) AskStreets Sample Query 1 (2/2) AskStreets Sample Query 2 (1/2) AskStreets Sample Query 2 (2/2) 🛣️ AskStreets: Query and Visualizing Street Networks using OpenStreetMap, ArangoDB, and LangGraph Author: Adam Munawar Rahman, March 2025 Using powerful open-source libraries like OSMnx, we can retrieve geographic features and street network datasets from OpenStreetMap and persist them as graphs and collections in ArangoDB. Then, via a LangGraph ReAct agent, we feed natural language queries to LLM-based tools to execute complex lookups, run GPU-backed graph algorithms, and visualize geospatial coordinates. This agentic app enables meaningful insights into the network properties of the desired geographic location, and empowers us to address real-world infrastructure challenges. Requirements Python 3.10 An ArangoDB instance, e.g. a local Docker container (for GPU acceleration) Nvidia CUDA toolkit, a compatible NVIDIA GPU, and RAPIDS (follow the install guide here ) A credentials.yml file with API keys for your desired AI platform (see sample file in repo) Running the Code Clone the repo, then in the askstreets directory: python3.10 -m venv env source env/bin/activate pip3 install -r requirements.txt Ensure your ArangoDB instance is running, e.g. to startup the local Docker container: docker run -e ARANGO_ROOT_PASSWORD=<root_password> -p 8529:8529 arangodb/arangodb Then startup the Jupyter server and load the desired notebook: jupyter-notebook askstreets-gpu.ipynb There are two versions of the AskStreets notebook: askstreets-gpu.ipynb which is the hackathon submission with GPU acceleration and fully answered query samples askstreets.ipynb which has cleared cell output and does not have GPU acceleration askstreets-gpu.ipynb also contains output for additional queries that were not demo'd in the video submission. Inspiration During my internship at UNICEF Innovation in NYC, I used OpenStreetMap, OSMnx, and NetworkX to calculate distances between schools and health facilities in UNICEF programme countries using national street and road networks. By writing code to execute graph algorithms, I was able to generate data to address a real-world issue. I would like to generalize this challenge towards a broader use case: if you're a city planner, business owner, architect, etc., you may wish to ask questions about street networks (e.g. accessibility of services, routed distances between landmarks, crowded intersections, etc.) without needing to code lengthy algorithms. This is where AskStreets comes in: by providing the ability to translate natural language queries into street network analysis. What it does The Jupyter Notebook submission contains the proof-of-concept for AskStreets. The agentic app uses a LangGraph ReAct agent that accepts user queries and calls multiple tools that can geocode, generate and run AQL, generate and run OSMnx/NetworkX code, and visualize points on a Folium map. By passing a query to the query_street_network function, it will invoke the ReAct agent to run these tools to interpret the query, execute code, and provide a natural language response or map visualization for the specific question. How I built it I used OSMnx to download street network graphs and geographic features for certain locations, prepared this data to load into ArangoDB, then wrote the LLM-based tools and ReAct agent code for the agentic app. Challenges I ran into Prompt engineering was a large aspect of this project; I needed to revise the prompts per tool multiple times as I continuously tested and analyzed the output of the ReAct agent, so that I could provide the AI models with more context to accurately interpret user queries and assemble the correct code. Modifying the tools to work in tandem with each other to generate the correct intermediate queries to pass between them was also challenging, but ultimately rewarding. Accomplishments that I'm proud of I particularly enjoyed seeing the outcome of these tools, which are able to accurately interpret user queries about street networks and correctly identify the geographic attributes to filter or run algorithms against. I especially appreciated that by loading additional datasets like OpenStreetMap features and health facility data into ArangoDB, along with the graph network, the AQL tool was able to pull data across these sources to answer user queries with a higher degree of specificity. What I learned I learned how to work with the LangChain and LangGraph libraries, how to invoke LLMs and prompt engineer to improve answers to queries, and how to prepare OSMnx data to load into ArangoDB. Citations Boeing, G. (2024). Modeling and Analyzing Urban Networks and Amenities with OSMnx. Working paper. https://geoffboeing.com/publications/osmnx-paper/ What's next for AskStreets Working with geospatial data has so much potential! In the submission notebook, I demonstrate at the end how health facility data can be overlaid with the street network graph and OpenStreetMap features data so that it can also be queried by AQL. By overlaying and combining even more data sets, we can enhance the app's ability to answer many different types of queries. Due to joining the hackathon late, there were tools I would have liked to fully implement but lacked refinement time. For example, a tool to dynamically pull in more data from the OpenStreetMap API based on a user query, a tool to more accurately translate location names, or updates to the visualization tool to draw paths between points. The tool prompts could also be further tuned to be more precise and avoid redundant operations. Different models could be deployed for each tool for their particular use case, with more lightweight models assigned to easier tasks. This app can be further enriched with a UI that can not only accept queries, but also automatically download OSM road networks and features from a user-specified location. It can even be integrated with a sophisticated mapping tool like kepler.gl that offers more visualization options for large geospatial datasets. <div