---
slug: "archaeologistai-code-archaeology-agent"
url: "https://devpost.com/software/archaeologistai-code-archaeology-agent"
title: "ArchaeologistAI — Code Archaeology Agent"
hackathon: "GitLab Transcend Hackathon"
organization: "GitLab"
winner: true
words: 639
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/graph_reasoning"
  - "domain/developer_tools"
  - "user/developer"
  - "substrate/code_repository"
---

# ArchaeologistAI — Code Archaeology Agent

> Stop digging through commits and merge requests. ArchaeologistAI explains why code exists in seconds.

[Devpost](https://devpost.com/software/archaeologistai-code-archaeology-agent) · hackathon [[GitLab Transcend Hackathon]]

## Facets

**mechanism** [[graph_reasoning]]
  <sub>weak: structural_withholding</sub>
**domain** [[developer_tools]]
  <sub>weak: education</sub>
**user** [[developer]]
  <sub>weak: educator_student</sub>
**substrate** [[code_repository]]

**stack** api, gitlab-cli, gitlab-duo-agent-platform, graph, jest, knowledge, modelcontext, node.js, orbit, protocol(mcp), rest, typescript, v4

## Body

Inspiration I am a third-year Information Science student who has spent the last year contributing to open-source projects, including GitLab, Joplin, and GSoC applications. Every time I opened a new codebase, I encountered the same problem. I would find a file I wanted to modify and immediately ask: Why does this file exist? Who created it and what problem were they solving? What depends on this file? Is it safe to modify? Answering these questions often meant spending hours searching through commits, merge requests, issues, and documentation. Many contributors either make changes without enough context or abandon their contribution entirely. This contributor cold-start problem exists in every large codebase. I built ArchaeologistAI to solve it. What It Does ArchaeologistAI is a GitLab Duo Agent powered by GitLab Orbit's Knowledge Graph. Imagine a contributor reviewing a merge request that modifies an unfamiliar file. Instead of manually searching through commit history, issues, and merge requests, they can ask ArchaeologistAI to investigate. ArchaeologistAI automatically: Traverses GitLab Orbit's Knowledge Graph to discover file relationships, definitions, and dependencies Analyzes commit history and related merge requests Identifies ownership and contributors Reconstructs the origin story and purpose of the file Generates a Code Archaeology Report directly inside GitLab Within seconds, contributors receive the context they need to confidently understand and modify unfamiliar code. How I Built It ArchaeologistAI is built as a three-stage intelligence pipeline: GraphTracer Collects data from GitLab Orbit and GitLab APIs, including: File nodes Definition nodes Call graph relationships Commit history Merge request context Linked issues IntentSynthesizer Transforms raw graph and repository data into meaningful insights: Origin story Driving requirement Ownership Risk assessment Architectural context Reporter Generates and publishes a structured Code Archaeology Report directly inside GitLab. GitLab Orbit Integration GitLab Orbit is the foundation of ArchaeologistAI. The agent traverses Orbit's Knowledge Graph to understand relationships between: Files Definitions Contributors Merge Requests Issues During testing, Orbit returned: File node identifiers Definition nodes connected through DEFINES edges Dependency information through CALLS relationships Import relationships between modules This allows ArchaeologistAI to understand how code is connected instead of simply reading source files. Unlike traditional code search or Git blame, Orbit provides architectural context through graph traversal. Example Output When analyzing a modified file, ArchaeologistAI generates a report containing: Origin Story Ownership Analysis Driving Requirement Risk Assessment Dependency Graph Context Orbit Knowledge Graph Insights The result helps contributors understand why code exists before they modify it. Challenges We Ran Into Understanding Orbit's Graph Model The biggest challenge was learning how to effectively traverse Orbit's Knowledge Graph and transform low-level graph data into meaningful developer insights. Combining Multiple Sources Useful archaeology requires combining: Orbit graph relationships Commit history Merge requests Issues Review discussions Bringing these together into a single coherent report required significant experimentation. Balancing Depth and Usability Providing enough context to be useful without overwhelming the developer was a major design challenge. Accomplishments That We're Proud Of Built a working GitLab Duo Agent Successfully integrated GitLab Orbit Knowledge Graph traversal Generated real Code Archaeology Reports inside GitLab Produced ownership, dependency, and historical insights automatically Created a reusable workflow for understanding unfamiliar code Most importantly, we transformed a frustrating contributor experience into a workflow that takes seconds instead of hours. What We Learned Through this project I learned: How GitLab Orbit models software systems as a knowledge graph How graph traversal reveals architectural relationships hidden from traditional search How GitLab Duo Agents can automate complex developer workflows How repository history, issues, and code structure can be combined into actionable insights What's Next Future improvements include: Automatic execution when merge requests are opened Multi-file dependency and blast-radius analysis Security context using Orbit security relationships Contributor onboarding mode for large repositories Cross-project archaeology for monorepos The long-term vision is to make software history instantly accessible so that no contributor has to wonder why code exists before changing it. <div