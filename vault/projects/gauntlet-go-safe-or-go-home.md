---
slug: "gauntlet-go-safe-or-go-home"
url: "https://devpost.com/software/gauntlet-go-safe-or-go-home"
title: "Gauntlet - Go safe or go home"
hackathon: "UiPath AgentHack"
organization: "UiPath"
winner: true
words: 901
team_size: 1
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/human_in_the_loop"
  - "mechanism/realtime_stream"
  - "mechanism/structural_withholding"
  - "domain/developer_tools"
  - "domain/finance_payments"
  - "domain/housing_homeless"
  - "domain/labor_employment"
  - "domain/security_privacy"
  - "user/government_staff"
  - "user/legal_professional"
  - "substrate/geospatial"
---

# Gauntlet - Go safe or go home

> GAUNTLET sends adversarial AI's to attack your AI service agent with multi-turn fraud. Every breach becomes a regression test in Test Manager, OWASP-tagged and AVSS-scored. Native to UiPath.

[Devpost](https://devpost.com/software/gauntlet-go-safe-or-go-home) · hackathon [[UiPath AgentHack]]

## Facets

**mechanism** [[human_in_the_loop]] [[realtime_stream]] [[structural_withholding]]
**domain** [[developer_tools]] [[finance_payments]] [[housing_homeless]] [[labor_employment]] [[security_privacy]]
**user** [[government_staff]] [[legal_professional]]
**substrate** [[geospatial]]

**stack** anthropic-claude, claude-code, claude-opus-4.7, javascript, langgraph, owasp-llm-top-10, python, react, typescript, uip-cli, uipath, uipath-action-center, uipath-case, uipath-cloud

## How they structured the write-up

- inspiration
- what it does
- how we built it
- challenges we ran into
- accomplishments that we're proud of
- what we learned
- what's next for gauntlet - go safe or go home

## Body

Inspiration UiPath Agent Evaluations tell you whether your agent passes the tests you wrote. They don't tell you what happens when a real attacker shows up with a prompt you never imagined. That gap is the whole pitch behind Gauntlet. Every other agent eval framework we looked at is cooperative: a fixed test set, a graded rubric, a green checkmark. None of them treat the agent the way a real adversary will, by inventing new attacks on the fly, learning from each failure, and chaining exploits across turns. So we built the opposite. A Red Coach agent whose job is to get worse every time the Blue agent successfully defends. More creative, more dangerous, more specific. Think AlphaGo self-play, but for prompt-injection, exfiltration, and tool-abuse against your production agents. What it does Gauntlet runs adversarial fights between a Red Coach (an Opus-authored attacker that mutates strategies between rounds) and a Blue target (any UiPath Agent, Maestro Flow, or external LangGraph target). FightArena (Maestro Case) orchestrates the fight as a long-running case with rounds as tasks RoundOrchestrator (Maestro Flow) runs a single round end-to-end: Red attack, Blue response, judge, score Coach invents new attack personas via Opus when the existing corpus stops scoring hits, auto-populating UiPath Test Manager with the winning attacks so they become permanent regression tests Fix Recommender reads a failed fight and proposes a concrete remediation (system-prompt patch, tool-scope restriction, guardrail rule), then opens an Action Center task for a human to approve Live Threat Dashboard shows real Maestro instances, OWASP LLM Top-10 and MITRE ATLAS coverage heatmap, and a fight ladder vs. each Blue target Today the corpus is 42 fights against fake-ceo-naive (the demo fixture), with the Coach having invented several attacks no human seeded. How we built it Track 3, Test Cloud. The whole thing is structured as a continuous-evaluation system, not a one-shot test. Layer UiPath component Fight orchestration Maestro Case ( FightArena ) + Maestro Flow ( RoundOrchestrator ) Attack & fix authoring Python agents ( gauntlet coach , gauntlet fix ) on LangGraph + Opus Persistent regression set Test Manager (auto-populated by Coach) Human-in-the-loop fix review Action Center tasks Operator surface UiPath Coded App ( gauntletapp ), React + @uipath/uipath-typescript SDK Live data Browser-side calls to maestro.processes.instances , Test Manager, Action Center The Coded App is the demo surface. Sidebar nav, Threat Dashboard, CoachLab, Fix Lab, Analytics. CoachLab's "Run Live" lets a judge paste a session key and watch Opus invent a fresh attack persona in the browser, end-to-end, in real time. Built entirely with Claude Code as the coding agent, which felt thematically right: an agent building a tool to keep agents honest. Challenges we ran into Codedapp indexer wedge. Published four versions in a row that all hung in "still being indexed". No CLI feedback, no error, just silence. Burned an afternoon before we learned to stop retrying. Maestro Case canvas version mismatch. CLI defaults to v20, which crashed the canvas. Had to pin to v19 to author the FightArena Case. Live API calls from a Coded App. Getting the SDK to authenticate from the browser against the user's own tenant (instead of a service principal) took several iterations. We landed on a public clientId flow with the user's session. Making "Run Live" feel honest. We didn't want a faked demo. CoachLab's live mode makes a real Anthropic call with the user's own key pasted into session storage. The persona you see was written during the demo , not pre-recorded. Accomplishments that we're proud of The Coach invents attacks we never seeded. Several of the strongest entries in the Test Manager corpus were authored by Opus mid-fight, not by us. End-to-end on real UiPath surfaces. Maestro Case + Flow, Test Manager auto-population, Action Center HITL, and a deployed Coded App. Not a slide deck, not a localhost demo. OWASP LLM Top-10 + MITRE ATLAS coverage matrix. Every fight is double-tagged, turning vibes-based agent safety into something a compliance officer can actually read. Live browser-side UiPath API calls from the Coded App (Maestro instances, Action Center tasks, Test Manager) using the user's own session. Shipped seven versions in the hackathon window (v0.1 through v0.22), each one closing a real gap rather than adding surface area. What we learned The interesting evals are the ones the human didn't write. Self-play creates evals you'd never think to author. Half the most useful entries in the Test Manager corpus came from Coach iterations. OWASP LLM Top-10 + MITRE ATLAS tagging is the audit moat. Once every fight is tagged with both, agent safety becomes a coverage matrix instead of a feeling. Maestro Case is underrated for long-running adversarial workloads. Rounds-as-tasks maps perfectly onto a fight that needs to pause, branch, and resume. uip CLI 1.0.4 is rough around codedapp deploys. Versions stuck in "still being indexed" for 25+ minutes, Case canvas crashes on v20 and needs v19. Learned to stop retrying and just wait. What's next for Gauntlet - Go safe or go home Wire RoundOrchestrator.flow end-to-end so "Run Fight" in the Coded App kicks off a real Maestro instance (deferred from v0.5, the flow JSON needs validating) Expand Blue targets beyond the LangGraph external target to native UiPath Agent Builder agents Auto-generate the OWASP / MITRE coverage report as a published artifact each time the corpus grows Open-source the attack corpus so other UiPath builders can run their agents through the same gauntlet <div