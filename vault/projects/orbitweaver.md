---
slug: "orbitweaver"
url: "https://devpost.com/software/orbitweaver"
title: "OrbitWeaver"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 602
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/graph_reasoning"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/transportation"
  - "user/developer"
  - "substrate/code_repository"
  - "substrate/geospatial"
  - "substrate/structured_db"
---

# OrbitWeaver

> Eliminating the AI "blast radius" blindspot with autonomous, graph-driven architectural migrations.

[Devpost](https://devpost.com/software/orbitweaver) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[deterministic_policy]] [[graph_reasoning]] [[retrieval_grounding]]
**domain** [[developer_tools]] [[finance_payments]] [[transportation]]
**user** [[developer]]
**substrate** [[code_repository]] [[geospatial]] [[structured_db]]

**stack** kahn's, mcp, mermaid.js, node.js, ollama, qwen, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for orbitweaver

## Body

MCP server Spooling up the agent via curl call Problem Existing Solution Mermaid Diagram Complete Loop done by Agent Orbitweaver MR Inspiration Current AI coding assistants have a massive, systemic blindspot during large enterprise refactors: the context-window blast radius . Standard tools rely on fuzzy vector proximity search to guess which files are relevant to a code change. When an engineering team deprecates or migrates a core interface, vector search routinely misses deeply nested downstream callers. The result? A trail of broken builds, silent runtime errors, and completely jammed CI/CD pipelines. We built OrbitWeaver to replace black-box context guessing with mathematical, graph-driven architectural certainty. What it does OrbitWeaver is a native GitLab Agent designed to execute complex, multi-file code migrations with absolute safety. When triggered directly from a GitLab Issue comment, OrbitWeaver maps out the true structural dependencies of the codebase. Instead of throwing all files at an LLM simultaneously or processing them at random, it calculates a precise execution sequence. It systematically refactors the lowest-level base dependencies first, moves up through implementations, and modifies top-level callers last. To provide full transparency, it automatically generates an interactive Mermaid.js dependency diagram inside the final, automated Merge Request, allowing developers to visually verify the migration path before merging. How we built it OrbitWeaver is built on a highly reliable, deterministic orchestration stack: Orchestration Layer: Built using TypeScript and Node.js to handle asynchronous webhook traffic and git operations via the GitLab API. Context Engine: Integrates with the GitLab Orbit Model Context Protocol (MCP) server to pull exact structural AST (Abstract Syntax Tree) schemas rather than reading raw text embeddings. Graph Mechanics: Implements Kahn’s Algorithm to perform structural dependency sorting, automatically identifying and resolving tight topological orderings. Inference Pipeline: Leverages Ollama running local LLM instances ( qwen3:8b ) to execute the individual code diffs based on strict isolation scopes provided by the orchestration layer. Challenges we ran into One of our biggest hurdles was navigating local inference hardware limits during multi-file migrations; executing structured code generation across 12 heavily interdependent files back-to-back easily hit 2-minute safety timeouts on local machines. We solved this by strictly separating the deterministic graph traversal logic from the generative AI step, allowing us to enforce hyper-focused context windows per file. We also wrestled with strict compiler rules regarding unused variables and imports when structuring our orchestration logic, which taught us to aggressively modularize our code generation templates. Accomplishments that we're proud of 100% Deterministic Traversal: Successfully isolated and mapped a 12-file deep dependency chain with zero false positives or missed callers. Flawless GitLab Integration: Engineered a zero-touch developer loop where an agent handles the entire life cycle: reading an issue, checking out a branch, committing ordered diffs, and filing a polished MR. Visual Verification: Auto-compiling a clean, perfectly scoped Mermaid.js syntax output inside Markdown that natively renders complex multi-layered architecture graphs directly inside GitLab. What we learned We learned that the future of reliable AI engineering isn't about feeding larger context windows into bigger models—it's about combining deterministic classical algorithms with generative models . By allowing a graph database and a topological sorting algorithm to handle the "thinking structure," the underlying LLM is freed up to do what it does best: write highly precise, local code modifications. What's next for OrbitWeaver We want to take OrbitWeaver from a single-repository agent to a true multi-repo service-mesh migration engine. Our next milestones include extending our MCP integration to map microservice dependencies across distributed repositories, adding automated compilation and test execution gates directly inside the agent loop before commits are pushed, and supporting broader language paradigms beyond TypeScript, such as Go and Rust. <div