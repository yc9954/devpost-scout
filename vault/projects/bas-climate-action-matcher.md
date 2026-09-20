---
slug: "bas-climate-action-matcher"
url: "https://devpost.com/software/bas-climate-action-matcher"
title: "BAS Climate Action Matcher"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 803
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "mechanism/retrieval_grounding"
  - "domain/climate_energy"
  - "domain/scientific_research"
  - "substrate/document_pdf"
  - "substrate/structured_db"
---

# BAS Climate Action Matcher

> A tool to match companies to relevant climate actions. Embedding search to find climate initiatives and agentic workflows+tool usage to discover corporate climate actions from sustainability reports

[Devpost](https://devpost.com/software/bas-climate-action-matcher) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[graph_reasoning]] [[retrieval_grounding]]
**domain** [[climate_energy]] [[scientific_research]]
**substrate** [[document_pdf]] [[structured_db]]

**stack** dain, gemini, google, intersystems-db, langchain, nvidia-llama

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for bas climate action matcher

## Body

Inspiration Mitigating climate change is only possible through a patchwork of collective action. The future of our planet will be determined by our ability to change previous destructive corporate processes radically. However, companies often struggle to find concrete solutions and actions to reduce their carbon footprint while advancing their business goals. We partner with Race to Zero to create a climate action matcher . Through a user-friendly interface and an agentic workflow grounded in tool usage, we match THE USER COMPANY with relevant UN-catalogued Cooperative Climate Initiatives and provide them with sustainability reports from similar companies and peer corporate actions to inspire concrete action. Ultimately, we want to transform how we approach climate change – from apathy to collective action. By connecting companies and their initiatives, we want to show that action is possible, popular, and influential – especially when done together as an industry, nation, and planet. What it does Our tool matches companies to relevant climate initiatives. We provide an agentic system with tools like RAG embedding search on a custom database of company sustainability reports, and UN-cataloged Cooperative Climate Initiatives, web scraping on websites like https://zerotracker.net/ and https://nzdpu.com/home , and more to discover corporate climate actions. How we built it DAIN Butterfly : We use the DAIN Butterfly agentic workflow with tool usage as our central orchestrator for user interface interactions. We built custom tools that find companies similar to THE USER COMPANY based on industry sector and country, match companies to UN-catalogued Cooperative Climate Initiatives, and find relevant climate actions from hundreds of sustainability reports from a custom database we built. We provide the agent with the initial context of its foal (e.g., it is trying to write a report that should reference its sources). Still, the agent can choose which tools to use and autonomously decide its tool strategy depending on the outcomes of previous actions and details specified by THE USER COMPANY. To ensure responsible usage, we instruct the agent to include sources to its information (which it can do as our tools return the href links they got their information from) in its findings, allowing THE USER COMPANY to confirm and dive deeper into the sources. We used the DAIN UI components to format the responses engagingly and professionally. InterSystems Embedding Database : We use InterSystems as our database. We collected and embedded 172 UN-catalogued Cooperative Climate Initiatives with descriptions and over 17,000 paragraphs from scraped sustainability reports. NVIDIA Llama Embeddings : We use Llama-3.2-nv-embedqa-1b-v2 embeddings for our embedding database and query embedding in our RAG vector search. LangChain : We use LangChain to load sustainability PDF reports directly from the web and recursively split the text for subsequent chunk embeddings. Google Gemini Scoring and Classification : We implement company sector classification using Gemini Flash Experimental 2.0. Moreover, we use Gemini to score corporate actions based on their reproducibility and return on investment for action ranking and matching. Scrapybara : We implement an agent to find concrete PDF links on corporate websites that may be deep in the link structure of the page. Selenium Web Browser : We implement web scraping using Selenium. Challenges we ran into Finding relevant climate actions first proved tricky since sustainability reports can be pretty vague, and embedding similarity search works best if we try to match the target report structure as closely as possible. We solved the problem by having the DAIN agent brainstorm climate initiatives the company could be doing and then verify these ideas by finding actual climate actions by companies in their sustainability reports. Another challenge was to have the agent perform enough actions to take advantage of all our tools. We ended up spending some time on prompt engineering and writing clearer tool descriptions which had a clear boost in performance. Accomplishments that we're proud of Created an end-to-end pipeline to match companies with sustainability efforts. Created an embedding vector database with hundreds of sustainability reports to be open-sourced to the broader community after the event. Developed core technical skills in web scraping, database manipulation, embedding models, document parsing, and tool creation. Built our understanding of sustainability reporting and found many avenues for continued work. What We Learned We learned a ton during the hackathon! On the technical side, we learned web scraping, document embeddings, how to work with Docker containers, and connecting Python and Typescript! On the environmental side, we opened the door to the vast world of sustainability reporting and tracking. Seeing all the initiatives already underway was inspiring, and we are incredibly excited to keep pushing for more action. What's next for BAS Climate Action Matcher Extend the initiatives into a dynamic knowledge graph to track the impacts of climate actions. Extend scoring to include nature-based solutions, collaborations, estimated impact, and cost. Create a dashboard to standardize climate reporting for easier comparison. <div