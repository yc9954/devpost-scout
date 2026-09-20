---
slug: "block-elf"
url: "https://devpost.com/software/block-elf"
title: "Block Elf"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 518
team_size: 3
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "user/researcher"
  - "substrate/financial_record"
---

# Block Elf

> On-chain LLM Search Engine

[Devpost](https://devpost.com/software/block-elf) · hackathon [[-REDACTED- Hackathon]]

## Facets

**user** [[researcher]]
**substrate** [[financial_record]]
  <sub>weak: web_dom</sub>

**stack** ai, blockexplorer, gemini, near, nearblocks

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- what we learned
- what's next for block elf
- contact

## Body

Our Website Execution: Portfolio Execution: Top NFTs Inspiration Our inspiration for this product stems from my time as a venture capitalist, which often requires querying multiple on-chain data sources for due diligence. I realized that accessing on-chain data can be challenging and requires significant technical skills, creating a barrier for many individuals. This insight motivated us to create a solution during the hackathon that simplifies the querying process. What it does BlockElf enables users to query on-chain data using natural language. Our product abstracts the complexities of on-chain queries, making this vital data accessible to everyone, regardless of their technical expertise. How we built it We utilize AI functional agentic technology with our flagship adaptive chain-of-thought, making the AI capable of answering any type of question. Our AI is able to formulate a plan to gather the correct information to provide a final answer to the user. We offer multiple data source for our agent to use. NEAR block data NEAR transaction data NEAR account data NEAR FT and NFT tokens data NEAR protocol stats and native token stats NEAR DEX pair data Internet The agent is also injected with NEAR specific knowledge such as FT/NFT specs, account id, token info, etc. Our Internal AI Framework Our AI framework automates how AI formulate plans to answer query, can be classified into multiple category High Level Planning High level planning are the highest level starting point of agents. In this level, agent will plan overall steps of execution and reasoning. The agent will thought about state of execution, reflection of previous and current execution, memory, and the plan and it's reasoning. This will ensure that the agent will reflect on what to do and what to improve Low Level Planning Low level planning is the level where the agent start to execute and observe the execution data. The agent will manage the execution parameter, and give out the execution task. Execute / Batch Execute Execution is the stage where the tools and data source is being executed and data is gathered. The agent can choose what to execute and reflect on the data. The agent can also choose to do batch execute to reduce the overall execution time. Final Answer The last stage where the answer is given out to user. This make sure that the agent thought "twice" on what being answered and is absolutely sure that the data answered is correct. Challenges we ran into One of the challenges we saw is lack of accessible of quality data source. So we utilize Pikespeak, Nearblocks, Mintbase, and Paras for all the data. What we learned We enhance the product through an adaptive chain of thought, recognizing the importance of retraining our processes to optimize quality within the NEAR data. What's next for Block Elf Our plan for Block Elf is to release the Beta version which invited researchers, VCs, and on-chain enthusiast to test the platform as well as optimize our infrastructure to be more accurate and faster. Furthermore, our team plans to support on-chain data across all ecosystem in Web 3.0 Contact Contact us at https://x.com/Blockelf_ai <div