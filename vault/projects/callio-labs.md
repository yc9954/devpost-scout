---
slug: "callio-labs"
url: "https://devpost.com/software/callio-labs"
title: "Callio Labs"
hackathon: " GenAI Genesis 2026"
organization: "GenAI Genesis"
winner: true
words: 1213
team_size: 2
has_repo: true
has_live: false
has_video: false
tags:
  - "project"
  - "mechanism/cross_origin_web"
  - "mechanism/multi_agent"
  - "domain/elder_child_care"
  - "domain/scientific_research"
  - "domain/transportation"
  - "user/developer"
  - "user/researcher"
  - "substrate/genomic_bio"
  - "substrate/geospatial"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Callio Labs

> Agentic Genomics

[Devpost](https://devpost.com/software/callio-labs) · hackathon [[GenAI Genesis 2026]]

## Facets

**mechanism** [[cross_origin_web]] [[multi_agent]]
**domain** [[elder_child_care]] [[scientific_research]] [[transportation]]
**user** [[developer]] [[researcher]]
**substrate** [[genomic_bio]] [[geospatial]] [[sensor_telemetry]] [[structured_db]]

**stack** docker, fastapi, fastmcp, geminiapi, json, langflow, markdown, modal, next-auth, next.js, openai, python, radix, react

## How they structured the write-up

- inspiration
- what it does
- how we built it
- langflow!!!
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for callio labs

## Body

Landing Page Home Screen AI Agent Tech Diagram LangFlow (1) LangFlow (2) Inspiration As Biomedical Engineers, we have directly experienced the tedious process of primer generation. From analyzing genomic data, identifying desired regions of DNA and designing PCR primers, to validating their metrics and generating experimental protocols, it can take weeks before a primer is produced and ready to be used. However, it's huge importance in PCR and DNA replication allows for use cases that can pinpoint viruses for early detection, provide molecular forensics tools to track criminals using saliva or blood, or provide invaluable tools for researching new mutations and cells. Primers always provide the first step in battling and developing a cure against viruses, they are used to identify genetic disorders and provide early dementia diaognosis. Thus, we decided to create Callio Labs: a streamlined agentic AI pipeline designed to significantly reduce primer research, preparation, and evaluation. Through levering machine learning models and AI agents, Callio Labs offers an all-in-one system from completing preliminary research, identifying optimal primers, to evaluating and ranking each primer until they are ready for use in the lab. What it does Our goal is to create an AI-powered research assistant which analyzes genetic information from databases including NBCI and other local sources. It integrates the numerous steps involved with primer creation into a single automated agentic pipeline that includes visuals and reasoning to increase understanding of the results. By providing any research topic of interest, our system analyzes genomes and produces PCR ready designs. How we built it The core of the backend is supported by the research chat agent made with LangGraph. By asking our agent a question, the information flows through "search agents", "persona agents", and "evaluator agents" each equipped with specific roles and output formats to feed into the next layer of the system. Agents would also run in parallel, providing simultaneous evaluations of the primers to increase efficiency. Lastly, a final "quality check" agent and "response composer" agent formats the comprehensive report outlining decision making and evaluations of the top primer suggestions for implementation. An NCBI Dataset MCP server hosted by FastMCP is used to integrate public genome/gene data. Agents also have web scrapping access to preform general searches for increase understanding of the user's request. Primer3, hosted by FastAPI, is used to provide the agents with real, viable PCR primers for the specific DNA sequence. The frontend uses a fine-tuned ColabFold machine learning model to predict protein structures from their corresponding DNA sequence, highlighting the effects of changes to the gene on the rest of the body. The model also integrates AlphaFold for a comprehensive 3D view of the protein structure of the gene of interest. The landing page and main page are made using React and ShadCN, and connected to the backend through LangFlow API. LangFlow!!! Callio Labs workflow consists of 52 nodes structured around 10 specialized AI agents each containing their own system prompts, structured schemas, and tools such as MCPs and Web Search capabilities. Building this in pure code would have required significant work for routing, error handling, and data valiadation between agents. Luckily, LangFlow's visual node-based interface allowed us to easily wire agents together, adjust prompts, and interate on the pipeline structure without even touching code! Our pipeline also integrates LangFlow's MCP Tools node that directly connect to our NCBI Dataset MCP Server. This gives the agents access to tools such as search_genome or get_gene_info which are autonomously used by the agents who decide when and how to call these tools. To increase productivity, Callio Labs uses a fan-out pattern where multiple specialized agents can analyze the same information in parallel, with a final "evaluator" agent synthesizing their outputs. LangFlow's nodes naturally represent this structure, making it easy to add/remove/modify agents. Additionally, LangFlow's visualization makes the pipeline legible and understandable to our end users: researchers like biologists or scientists. By opening the LangFlow canvas, these users can examine exactly how thier primer design request flows from the initial query parsing to final report, and even adjust instructions without needing to program. This also offers transparency to users through visual inspection of every decision point, every pormpt, and every data transformation in the pipeline as nodes in LangFlow. Each agent is required to output a valid JSON matching a predefined schema. Thus this acts as validaation gates, preventing hallucinated or malfored data from propagating further downstream. The final output report always includes citations which are explicitly instructed to promote tracibility and verifilibility in the AI's conclusions. Lastly, API keys are handled securly through LangFlow's MCP Tool nodes and LLM nodes which include SSL verification. Challenges we ran into Initially, we used LangFlow to generate the nodes and overall workflow. However, after fixing all missing connections and starting the model, we faced errors with missing requirements or deprecated nodes that included no logs for guidance to overcome the issue. We also ran into issues with context windows in LangFlow where agents would attempt to webscrape too much information to the point where it heavily exceeded the token limit. Using databases such as NCBI often returned huge genome sequences that we had to trucate and fine-tune our agents to enforce size limits. The models hallucinated often and required lots of prompt refinement to provide adequate output. For ColabFold, this model needed to be retrained each time it was loaded, typically requiring at least 7 minutes before producing the 3D protein model. However, by hosting the model on Modal and fine tuning the model for our environment, this significantly reduced the model's load time and allowed for the proteins to be displayed efficiently. Primer3 also proved challenging as certain regions of DNA were impossible to find primers which satisfied our given parameters. However, loosening these parameters resulted in indefinite looping as there were an infinite amount of primers which satisfied our conditions. We addressed this by capping the number of primers returned for each task, using a middle-ground default parameter, and limiting the number of tasks per requests. Lastly, we ran into an issue with API keys as each of our 10 agents in this pipeline required an API key. Although there were free API keys, these models were unpredictable and experienced high traffic which forced us to use our own API keys to overcome this challenge. Accomplishments that we're proud of Developing a highly complex, multi-persona agentic AI research pipeline in LangGraph is very rewarding as a single POST can run the full pipeline and return a synthesized, cited answer with limitations and use cases. Also creating a functional NCBI MCP server after being inspired by SunLife's technical talk allows our agent exposure to credible, widely sourced information, leading to grounded and realistic primer suggestions. What we learned We learned the importance of parameter optimization through overcoming the challenge with Primer3. We also learned how to build scalable, reliable, and efficient agentic AI pipelines targeted at reducing research costs while offering research assistance for primer development. What's next for Callio Labs Every year, about 3.6 to 5.2 billion dollars are spent on synthesizing custom DNA sequences. Once researchers being using Callio Labs, we envision this cost to drop by more than 50% as our agentic AI completes this process in a matter of minues. We're going to ship it. <div