---
slug: "accordion-jwarge"
url: "https://devpost.com/software/accordion-jwarge"
title: "Accordion"
hackathon: "UC Berkeley AI Hackathon 2026"
organization: "Cal Hacks"
winner: true
words: 891
team_size: 4
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/deterministic_policy"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/agriculture_food"
  - "substrate/code_repository"
---

# Accordion

> Context management you can trust - Say goodbye to /compact

[Devpost](https://devpost.com/software/accordion-jwarge) · hackathon [[UC Berkeley AI Hackathon 2026]]

## Facets

**mechanism** [[deterministic_policy]] [[realtime_stream]] [[structural_withholding]]
**domain** [[agriculture_food]]
  <sub>weak: developer_tools</sub>
  <sub>weak: developer</sub>
**substrate** [[code_repository]]

**stack** claude, javascript, jiti, node.js, pi, qwen2.5-0.5b, rust, svelte-5, sveltekit, tauri-2, typescript, vite, vitest, websocket

## How they structured the write-up

- inspiration
- what it does
- accomplishments we're proud of
- how we built it
- challenges we ran into
- what we learned
- what's next

## Body

Our Stack Accordion - An intelligent context management tool built for developers Inspiration Anyone who has used AI coding agents has seen their context window fills up, and /compact gets called soon after. Just like that your thinking partner has lost 90% of your conversation. Decisions, rules, errors, code, and more gone. We believe this is an inherently naive solution to a problem that deserves real attention. What it does Accordion shows you your entire context window at a glance using a series of blocks in a grid. Each block is colored depending on its type. Those types are user messages, responses, thinking, tool calls and their results. Then, what we call a conductor, reads every block and decides which should be folded, unfolded, or grouped based on custom logic. Folded blocks are replaced with tagged summaries containing a unique code. If the agent needs the original content, it can get it back at any time using our unfold command. Every fold is fully reversible. strategies for conductors range from simple oldest-first folding to harvesting attention from a 500M parameter model to score each blocks relevance to the most recent context. The promise is simple. No blocking calls for compaction, longer smarter coding sessions, and cheaper inference costs. Accomplishments we're proud of Thermocline(one of our conductors) scored 83.3% on SlopCodeBench, 2.5× the 33.3% the same model scored using naive compaction to manage its own context. This is the first conductor to combine attention-based relevance scoring with LLM summaries and block grouping. The result validates that reversible, recall-able folding with intelligent prioritization isn't just theoretically better than naive compaction, it measurably outperforms it on real coding tasks. How we built it Accordion is built around a simple idea: context is a view , not a storage system. We keep the full conversation intact and generate a live view of what gets injected into the model each turn. Folding swaps content for a compact digest; unfolding restores it instantly. The desktop app is built with Tauri , SvelteKit , and TypeScript , while a local WebSocket connection streams live context updates from the running agent to the UI in real time. The Conductor architecture uses a clean synchronous interface — conduct(view) → Command[] — so new folding strategies are a single file to drop in, in any language over the wire or as a direct TypeScript class. One of the biggest technical challenges was preserving tool-call correctness . Since tool calls and their results must remain paired in the provider's message format, Accordion never folds a tool call — only its result — and validates every context view before sending it to the model. Challenges we ran into Control and trust. We wanted automation without sacrificing user control. The final system has a layered trust model: collaborative conductors that users can always override, exclusive conductors with an explicit consent gate showing exactly which controls they claim, and a kill switch (detach) that freezes the current context and hands every control back to you — always, unconditionally. Stable fold handles. When a block is folded, the agent sees a {#code FOLDED} tag in its context — a short handle it can pass back to retrieve the content. That handle has to be stable across sessions, short enough to be noise-free in context, and deterministic so the agent gets the same code every run. We derive it as a stateless hash of the block's durable ID rather than generating it dynamically, so it requires no stored state and survives reconnects cleanly. Automatic folding strategy. Determining what is "important" is harder than it sounds. We ended up building a family of strategies rather than committing to one answer — from a simple oldest-first baseline to an attention-probe-driven scorer (Qwen2.5-0.5B) that identifies which blocks the model is actually attending to. What we learned Treating context manipulation as a UI problem as much as an AI problem unlocked a lot. The hard part wasn't compression — it was giving humans and agents the right level of visibility and control at each layer: what's folded, who did it, and how to get it back. We also learned that the right abstraction is a view over a store , not a store you mutate. Once that clicked, reversibility, attribution, and the agent's ability to reach back for folded content all fell out naturally — no extra infrastructure. Finally: folding strategy is not one thing. The first conductor we built was a clean baseline. The second taught us something the first couldn't. By the time we had nine, each one caught real failure modes the others missed — which is why the architecture is a protocol, not a single algorithm. What's next LLM-generated summaries, computed once and cached — richer prose summaries for individual blocks would make folded content more legible to the agent than raw digests Hierarchical folding — fold the folds, for million-turn sessions: a long session compresses to a handful of headlines you can open to any depth Agent-driven pinning — the agent can already unfold and recall; letting it pin blocks protects them from future automated folding Replay — scrub how the context evolved across a session, so you can see exactly when something got folded, who did it, and what the token budget looked like at each step "Accordion just killed claude" - Tech influencer <div