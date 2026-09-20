---
slug: "concave-frxwcz"
url: "https://devpost.com/software/concave-frxwcz"
title: "concave"
hackathon: "TiDB Future App Hackathon 2024"
organization: "PingCAP"
winner: true
words: 616
team_size: 1
has_repo: false
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/transportation"
  - "user/researcher"
  - "substrate/code_repository"
  - "substrate/financial_record"
---

# concave

> Open Source, TrustedAutonomous Software Engineering

[Devpost](https://devpost.com/software/concave-frxwcz) · hackathon [[TiDB Future App Hackathon 2024]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[transportation]]
**user** [[researcher]]
**substrate** [[code_repository]] [[financial_record]]

**stack** python, tidb, tree-sitter

## How they structured the write-up

- an open-source, reliable automated programming platform
- our target: 'trusted', 'open source' autonomous software engineering
- we're 50% better at identify problems than the best open-source solution detail test report
- links
- what inspired us
- our goal
- what concave does
- how we built it
- challenges we faced
- what we're proud of
- what's next for concave

## Body

Concave An Open-Source, Reliable Automated Programming Platform Our target: 'Trusted', 'Open Source' Autonomous Software Engineering We're 50% better at identify problems than the best open-source solution detail test report Links Homepage: https://concave-ai.vercel.app Docs: https://concave-docs.vercel.app Try our demo Playbook: https://concave-ai.vercel.app/playbook help you understand how L·IDE and Fleet work. Our Tech Report: https://github.com/concave-ai/fleet/blob/main/docs/fleet_report.md The bug we found in TiDB Vector Client, and fixed with Fleet: https://github.com/pingcap/tidb-vector-python/issues/58 What Inspired Us Many researchers and companies have done well on SWE-Bench. But we saw two main problems: Current open-source tools can be much better. For example, Python analysis tools are slow and can't do detailed analysis. Some startup companies have good results, but they don't share their code. We want to fix these issues with Concave by: open-source Using new tech from industry, like better code analysis tools (SCIP, Tree-sitter) and serverless vector search ( TiDB Vector.) Our Goal We're building an open-source, trustworthy, and fully automatic software engineering platform. We made Concave to help current AI models do software engineering more easily. What Concave Does In this hackathon, we built two main parts from scratch: Concave L·IDE: The First IDE Made for LLM (not humans :) ) Gives LLM the best tools Can search for any code part, like function calls or variable settings Searches using both keywords (with TiDB Data Service) and meaning (with TiDB Vector Search) Combines different search types in one system (TiDB Cloud) (HTAVP, Hybrid transactional/analytical/vector processing) Concave Fleet: We made this in one week to test if L·IDE works well It can find the main problem in code and fix it automatically It works really well: 50% better at finding problems than the best open-source tools tech report We even used Fleet to fix a bug we found in TiDB Vector Client while making L·IDE ( link to issue ) How We Built It In one week, we made Concave L·IDE Code Mixed Search using TiDB Serverless: TiDB Serverless Data Service was the best choice for building symbol search, TiDB Cloud Vector Search and LlamaIndex and JinaAI made it easy to develop semantic search from scratch. In another week, we made Concave Fleet using Concave L·IDE: Find the main problem Make code to fix the problem By using Dify and JinaAI, we further create and optimized the behavior of each agent in Fleet, ensuring more accurate outputs. We also made a user interface called Playbook. It helps people understand how L·IDE and Fleet work, making our solution more trustworthy. For code understanding, we looked at tools like Tree-sitter and SCIP to make a better Python analysis tool. Challenges We Faced Main question: How can we make SWE-Bench work better? Our ideas: Make each step work better to improve the overall success. Help AI understand code better to solve more problems. L·IDE and Fleet proved these ideas work. We got 50% better at finding problems in SWE-Bench. Our report shows that finding problems better helps solve them better too. We didn't have time to test everything in SWE-Bench, but we proved our method works. We plan to finish all tests soon. What We're Proud Of We're 50% better at finding problems than the best open-source tools We know how to make SWE-Bench work even better We shared all our tools so other teams can join in making software engineering automatic What's Next for Concave Finish the newest SWE-Bench tests and try to get the best open-source score Make a pre-set up L·IDE for SWE-Bench to help more teams. They can focus on making AI edit code better without worrying about setting up code analysis Add more features to Concave L·IDE, like searching git commits and history Make Concave L·IDE useful for more than just SWE-Bench <div