---
slug: "washedmcp"
url: "https://devpost.com/software/washedmcp"
title: "WashedMCP"
hackathon: "NexHacks"
organization: "FII"
winner: true
words: 580
team_size: 4
has_repo: true
has_live: true
has_video: true
tags:
  - "project"
  - "mechanism/retrieval_grounding"
  - "domain/developer_tools"
---

# WashedMCP

> WashedMCP is a token efficient semantic code search server that returns the function plus callers and callees in one search, and can recommend and install MCP tools using hook based tool call memory

[Devpost](https://devpost.com/software/washedmcp) · hackathon [[NexHacks]]

## Facets

**mechanism** [[retrieval_grounding]]
**domain** [[developer_tools]]

**stack** chromadb, claude, leanmcp, mcp, nextjs, pypi, python, toon, typescript

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for washedmcp

## Body

Without our algorithm: 338k tokens With our algorithm: 71k tokens Recommendation and installation pipeline Frontend Inspiration We kept hitting the same wall with AI coding assistants on real repos. Search would return one isolated snippet, then we had to run multiple follow up searches to figure out who calls it, what it calls, and what file context matters. That loop wasted tokens and broke momentum. We also noticed setup pain. People install and configure the same MCP tools over and over, and assistants repeat the same tool calls without learning. We wanted the tool layer to be smarter and more automatic. What it does WashedMCP is a token efficient semantic code search MCP server that returns full context in one search. It finds code by meaning, not keywords, and returns: The best matching function or class CALLS (callees) CALLED BY (callers) Same file neighbors that are likely relevant Configurable depth for multi hop expansion To reduce token overhead, results are formatted in TOON, a token optimized object notation. On top of that, we built a recommendation and auto installation MCP pipeline using LeanMCP. It intercepts tool calls with hooks, remembers repeated patterns, and can recommend and auto install the right MCP tools so assistants stop repeating setup work. How we built it Parsing and relationships We used tree sitter to parse multiple languages and extract symbols and call relationships. Semantic retrieval We embed functions and chunks using sentence transformers (all MiniLM L6 v2) and compare with cosine similarity. Storage We store embeddings in ChromaDB for persistent vector search, plus relationship metadata for context expansion. Context expansion After a match, we walk the code graph to add callers, callees, and same file neighbors. Depth controls how far the expansion goes. Token efficient output We designed TOON to keep structure while reducing repeated keys and formatting overhead versus JSON. Automation layer Using LeanMCP hooks, we intercept tool calls, track repetition, and trigger recommendations or auto install steps based on tool call memory. Optional token math we use to think about overhead: \(\text{Savings} = 1 - \frac{T_{toon}}{T_{json}}\) Challenges we ran into AST complexity Extracting reliable call relationships across complex JS and TS patterns (imports, arrow functions, dynamic calls). Context window optimization Picking the right amount of context so results are actually useful without blowing token budgets. Output format tradeoffs Designing TOON to be smaller than JSON but still consistent and easy to parse. Hook based interception reliability Making recommendations feel helpful and not disruptive, and only triggering when there is a clear repeated pattern. Accomplishments that we're proud of One search returns actionable context instead of a single snippet. Multi language support across Python, JavaScript, TypeScript, JSX, TSX. Depth based context expansion that helps trace real debugging chains. TOON output that cuts token overhead while staying structured. A working LeanMCP pipeline that recommends and auto installs MCP tools using remembered tool call patterns. What we learned Token cost is a real product constraint, not a nice to have optimization. The biggest UX win is reducing loops, not adding more buttons. Code intelligence is mostly edge cases and reliability work. Smart defaults make demos feel fast and magical. What's next for WashedMCP Better ranking that mixes semantic similarity with graph importance. Smarter context selection that expands only into the most relevant files and symbols. Incremental indexing and caching for large repos. A lightweight UI to browse results and the code graph. Safer auto install flows with clearer user control and per project profiles. <div