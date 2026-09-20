---
slug: "dead-project-snipper"
url: "https://devpost.com/software/dead-project-snipper"
title: "Dead Project Snipper"
hackathon: "[REDACTED] Hackathon"
organization: "NEAR Protocol"
winner: true
words: 913
team_size: 3
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "mechanism/retrieval_grounding"
  - "domain/labor_employment"
  - "user/developer"
  - "user/legal_professional"
  - "substrate/financial_record"
  - "substrate/sensor_telemetry"
  - "substrate/structured_db"
---

# Dead Project Snipper

> Track social activity of projects that received grants, to see if them projects have met an unfortunate end.

[Devpost](https://devpost.com/software/dead-project-snipper) · hackathon [[-REDACTED- Hackathon]]

## Facets

**mechanism** [[realtime_stream]] [[retrieval_grounding]]
**domain** [[labor_employment]]
**user** [[developer]] [[legal_professional]]
**substrate** [[financial_record]] [[sensor_telemetry]] [[structured_db]]

**stack** colab, github, langchain, masa, nearblocks, next.js, rag

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for dead project snipper
- sponsor tracks we are applying for

## Body

Inspiration Team GBH come from a builder's group, with about 40 llm engineers as members. Our group gather every Wednesday to share and practice new techs and knowledge to better our selves. Some of us wanted more than building a side projects that no one really uses. We wanted to build a project where there would be actual users which would give us real production experience with LLM building, and at the same time would give us freedom to choose our own task, tech stacks, and overall challenge. the Funding Agent of AI-PGF fit our needs. We would build something that could matter, get actual feedback, and give back to open source community and public goods 'paying it forward'. This was perfect because it was not so 'crypto heavy' to scare us off, yet enough to get us understanding on blockchain ecosystem. It was also relevant with challenges in GovTech and other public sectors painpoints; we could use what we built into innovating these areas once we could get this implemented. It could be a good use case for LLM engineering and Web3 Techs. This possibility excited us. By getting grants from AI-PGF, some of us could dedicate more portion of their time to focus on building this. Three of us are the more dedicated members who carried the team, but behind that there were little pieces of contribution from the whole group. In a way, this was our group's transformation into a decentralized guild of LLM builders. What it does Problem According to Gitcoin’s State of the Web3 Grant Report , there are over 1B $USD of grant issued across 5,900 projects in 2023. However, it lacks a standardized and automated measure to assess the activity of the project such that it requires extra effort for validation and the fund may be allocated to the wrong project. Solution Dead Project Snipper offers an automated agent that Collects data from the projects’ social(ex. X), building(ex. Github), and user(ex. onchain transaction) activity and store it on the activity database Calculates the activity score based on the score calculator algorithm for “Dead” and “Active” analysis Reports whether the project is dead or alive with the analysis data to back up the judgement. The report will be stored onchain for further verification System Architecture System Flow The project consist of three main flows, which is coded alphabetically. Collect & organize data points: This means figuring out which project is the target for monitoring, and acquiring the project's social/github/wallet address. This part is less about programming; it's more about coordinating with funded projects for information. Collect activity data: Once data points are set, we use APIs to monitor and collect activity data in regular cycle. Judgement and action: Activity data is ingested to llm-based algorithm. Based on the result score, fact-based reports are created (by llm), actions may be called, and the info is updated to offchain DB & mainnet. Impact Historical Grant Assessment: Check and see whether previous grant projects are still in progress or not Grant Project Management: Check the current grant projects to see if their activity should be eligible for the amount Grant Criteria Setup: Set up metrics for the least / preferred required activities for the grant recipient How we built it Tech stack Data point / Collector: Github API, Masa node for Twitter Data, Nearblocks Indexer API for transaction records Data Sets for the Metrics: Projects are chosen from Potlock Directory (currently building data for only top 15 projects over $1000 gross grant recieved for cost reasons.) Score Calculator: Multipath reasoning algorithm that utilizes LLM-as-a-judge Report writing: Instruction based prompt engineering with RAG on Langchain Report UI: Next.js SME Experiment UI : Colab with metrics and instructions on how to customize them Challenges we ran into Getting to know near ecosystem were painful; we wasted time from lack of info. For example, we tried 'indexer for explorer' only to find out it is discontinued. We did not know that and spend some time tryting to debug connection to dead database. Lake framework offered data on s3 storage, but we could not find how and what the uploaded files did. Luckily nearblocks explorer worked as we expected. Accomplishments that we're proud of We got to use Masa! It's awesome. This would be helpful for many more features to come. What we learned Organizing "decentralized" project development effort is much more difficult. What's next for Dead Project Snipper Scope Phase - MVP Objective: More dataset / product level UI to start the service adoption Larger dataset for comparison / score calculation Web based UI for datapoint / reporting. Any project can be registered Product ready level for the grant project(ex. Gitcoin, Potlock) integration Phase - Expansion Objective: Develop into a project assessment agent In theory, Dead Project Snipper can be generally applied as a project assessment that can not only be applied to Grant Projects outside of Web3, but also any project that requires performance metrics (ex. investment, employment, etc) In order for expansion, it will require multiple data points for the assessment and more developed scoring metrics that befits the purpose of the area of application Sponsor Tracks we are applying for Masa - Build AI Agent with FREE Masa Twitter Data We built with data from their node! Create an AI agent using real-time Masa Twitter data for innovative use cases. Potlock - AI Agent Bounty This is agent to automate grants funding workflows, leveraging Potlock contracts and AI technologies. <div