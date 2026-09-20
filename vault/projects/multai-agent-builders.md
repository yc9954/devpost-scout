---
slug: "multai-agent-builders"
url: "https://devpost.com/software/multai-agent-builders"
title: "AgentFather"
hackathon: "One Trillion Agents Hackathon"
organization: "NEAR Protocol"
winner: true
words: 591
team_size: 2
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/multi_agent"
  - "mechanism/on_device_local"
  - "domain/developer_tools"
  - "user/developer"
---

# AgentFather

> assistant helping users create agents on the NEAR AI Hub

[Devpost](https://devpost.com/software/multai-agent-builders) · hackathon [[One Trillion Agents Hackathon]]

## Facets

**mechanism** [[multi_agent]] [[on_device_local]]
**domain** [[developer_tools]]
**user** [[developer]]
  <sub>weak: code_repository</sub>

**stack** nearai, python

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for agentfather

## Body

AgentFather Source Code on the NEAR AI Hub Inspiration We were initially motivated by this post on X, where Illia expressed interest in "agents that will build agents." The product vision took inspiration from this paper , Automated Design of Agentic Systems (Shengran Hu, Cong Lu, and Jeff Clune), which presents a simple yet effective algorithm named Meta Agent Search to demonstrate how agents can invent novel building blocks and/or combine them in new ways. Also, we discovered how agents can evolve themselves, thanks to Yohei Nakajima , who developed the BabyAGI framework and Pippin. Ultimately, the goal is to provide a streamlined onboarding experience like BotFather does on Telegram. What it does Our agent serves as an LLM-powered assistant for human agent builders, helping to create and publish agents on the NEAR AI Hub. First, it asks for details of what the user wants to create, then it generates code and uploads the agent via the Registry API. How we built it First, we experimented with various parts of the complete solution, like how the agent calls env.exec_command to leverage nearai CLI tools and the way it reads/writes files in a thread's temporary directory. Then, we connected for a pair programming session to hack on this proof of concept . Since then, we made significant improvements! There are two main functions, and each is a tool in AgentFather's workshop: 1. generate(agent_name, agent_description, agent_technical_plan) This writes a metadata.json file for configuration purposes, and generates the agent.py code based on user input. The underlying system prompt outlines agent requirements and available libraries. 2. upload(version) This registers a generated agent on the NEAR AI Hub. Plus, there is a helper function, _upload(registry, env) , which validates metadata,json and handles the actual file uploading process. AgentFather uses these features of the NEAR AI environment object: env.list_messages() ~ gets conversation history env.completion() ~ makes LLM API calls env.add_reply() ~ adds agent responses to the conversation env.write_file() / env.read_file() ~ handles file I/O env.get_tool_registry() ~ creates a registry for agent tools env.completions_and_run_tools() ~ runs tools based on LLM instructions Technical Details sets default as the Llama v3 70B model provided through Fireworks restricts certain operations (direct OS access, async code, classes) only public APIs that don't require authentication can be used Essentially, this meta agent can launch other agents based on natural language descriptions. Challenges we ran into Sometimes, it was difficult to debug issues, and certain aspects like nearai.config are not yet documented. However, the community and core team were really supportive! Accomplishments that we're proud of This project offers a good starting point for agent builders, and we're finding new opportunities for collaboration. Other NEAR AI developers have already begun to adopt similar patterns. What we learned We figured out how to test NEAR AI agents both locally and in the main hub environment. Also, we've gathered valuable insights on what it takes to develop adaptive multi-agent systems that discover powerful new designs. What's next for AgentFather There are many directions we can go from here... Right now, it only works in some cases. For example, our minimum viable agent builder doesn't know how to interact with supported frameworks and emerging tool registries. We could make it much better at iterating on the code, updating version numbers, and managing secret environment variables. In the near future, we hope to introduce our own meta search algorithm (something like this ) to facilitate growth, refinement, and proliferation of NEAR AI agent registries (onchain). AgentFather is bringing the next-generation of builders into the world! MIT License <div