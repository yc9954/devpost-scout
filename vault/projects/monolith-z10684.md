---
slug: "monolith-z10684"
url: "https://devpost.com/software/monolith-z10684"
title: "Monolith"
hackathon: "TreeHacks 2026"
organization: "TreeHacks"
winner: true
words: 412
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "domain/labor_employment"
  - "substrate/code_repository"
  - "substrate/structured_db"
---

# Monolith

> Shared coding agent context powered by RLMs. One Context, Run Everywhere.

[Devpost](https://devpost.com/software/monolith-z10684) · hackathon [[TreeHacks 2026]]

## Facets

**domain** [[labor_employment]]
  <sub>weak: developer_tools</sub>
**substrate** [[code_repository]] [[structured_db]]

**stack** claude, cloudflare, mcp, modal, openai, python, uv

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for monolith

## Body

Tui view of our coding agent plugin Modal sandboxes for RLM subagents GIF Full MCP call for debugging Inspiration RLMs are an elegant solution to the problem of context rot that let LLMs easily scale to millions of tokens, basically for free. Monolith lets you take advantage of RLMs for coding agents by giving each repo its own single chat history across devs working on the repo. This gives the agent a native understanding of your previous sessions and insights, such as design decisions, from other devs' sessions without you doing anything. What it does Monolith is implemented as a plugin to any coding agent that supports MCP tooling, which allows it to query and interact with the shared context via the RLM harness described in the original paper. One context, run everywhere. How we built it We used a couple of key technologies: Modal serverless functions Modal sandboxes Modal volumes OpenAI API Cloudflare Workers & Containers For some quick background, the RLM paradigm exposes the context as an object in a REPL environment for the root LM to interact with and inspect with sub-LMs to avoid polluting the main context. We implement the root LM with a Modal serverless function, which can provision sandboxes for the sub-LMs to do analysis on chunks of the context. The context is exposed as a file system in a Modal volume, which is mounted to all sandboxes. Challenges we ran into Existing RLM implementations are very barebones, so we had to do a lot of engineering to make things work in the cloud on Modal. Designing the system was also an interesting problem. Initially, we wanted to store the monocontext in object storage (S3), however, we found that this was not a good primitive for slice and append heavy workloads, which is what our use case demanded. Accomplishments that we're proud of Getting the whole thing to actually work by 4 am-ish. What we learned A lot about designing systems, agentic harnesses (this is what the "RLM" is at the end of the day), and Modal. What's next for Monolith We don't know if this is THE way to implement a massive mutable shared context, maybe the best implementations just converge to some kind of database. However, we think it is an interesting idea that has potential. We envision Monolith eventually incorporating git history (commit messages, PR comments, etc.) into the context and having the option of automatic initialization of Monolith into GitHub repos. <div